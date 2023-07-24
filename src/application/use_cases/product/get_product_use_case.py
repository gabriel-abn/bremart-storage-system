from src.application.common import ApplicationError
from src.application.repositories import IProductRepository
from src.domain.use_cases.product import GetProduct, GetProductParams, GetProductResult


class GetProductUseCase(GetProduct):
    def __init__(self, product_repository: IProductRepository) -> None:
        self.product_repository = product_repository

    async def execute(self, params: GetProductParams) -> GetProductResult:
        product = await self.product_repository.get_by_barcode(params["bar_code"])

        if not product:
            raise ApplicationError("Product not found.", "GetProductUseCase")

        return {
            "product": product,
        }
