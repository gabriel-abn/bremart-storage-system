from src.application.common import ApplicationError
from src.application.protocols import ICrypter, IUUIDGenerator
from src.application.repositories import IDistributorRepository, IProductRepository
from src.domain.entities import Product
from src.domain.use_cases.product import (
    GetProductCategories,
    GetProductTypes,
    RegisterProduct,
    RegisterProductParams,
    RegisterProductResult,
)


class RegisterProductUseCase(RegisterProduct):
    def __init__(
        self,
        product_repository: IProductRepository,
        distributor_repository: IDistributorRepository,
        uuid_generator: IUUIDGenerator,
        crypter: ICrypter,
        get_product_types: GetProductTypes,
        get_product_categories: GetProductCategories,
    ) -> None:
        self.product_repository = product_repository
        self.distributor_repository = distributor_repository
        self.uuid_generator = uuid_generator
        self.crypter = crypter
        self.get_product_types = get_product_types
        self.get_product_categories = get_product_categories

    async def execute(self, params: RegisterProductParams) -> RegisterProductResult:
        product = params["product"]

        distributor = await self.distributor_repository.find_by_id(
            product["distributor_id"]
        )

        if not distributor:
            raise ApplicationError("Distributor not found", "RegisterProductUseCase")

        if product["product_type"] not in self.get_product_types.execute():
            raise ApplicationError("Invalid product type.", "RegisterProductUseCase")

        if product["product_category"] not in self.get_product_categories.execute(
            {"product_type": product["product_type"]}
        ):
            raise ApplicationError("Invalid category.", "RegisterProductUseCase")

        id = self.uuid_generator.generate()

        new_product = Product.create(product, id)

        save = await self.product_repository.register(new_product)

        return {
            "crypted_id": self.crypter.encrypt(save["id"]),
        }
