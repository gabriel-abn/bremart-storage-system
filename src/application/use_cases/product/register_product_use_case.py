from src.application.common import ApplicationError
from src.application.protocols import ICrypter, IUUIDGenerator
from src.application.repositories import IDistributorRepository, IProductRepository
from src.domain.entities import Product, ProductTypes, categories
from src.domain.use_cases.product.register_product import (
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
    ) -> None:
        self.product_repository = product_repository
        self.distributor_repository = distributor_repository
        self.uuid_generator = uuid_generator
        self.crypter = crypter

    async def execute(self, params: RegisterProductParams) -> RegisterProductResult:
        product = params["product"]

        distributor = await self.distributor_repository.find_by_id(
            product["distributor_id"]
        )

        if not distributor:
            raise ApplicationError("Distributor not found", "RegisterProductUseCase")

        if product["product_type"] not in ProductTypes.__members__.keys():
            raise ApplicationError("Invalid product type.", "RegisterProductUseCase")

        for category in categories:
            if product["product_type"] == category[0].value:
                if product["product_category"] not in category[1]:
                    raise ApplicationError(
                        "Invalid category.", "RegisterProductUseCase"
                    )

        id = self.uuid_generator.generate()

        new_product = Product.create(product, id)

        save = await self.product_repository.register(new_product)

        return {
            "crypted_id": self.crypter.encrypt(save["id"]),
        }
