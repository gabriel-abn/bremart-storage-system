from src.application.repositories import IProductRepository
from src.domain.use_cases.product import GetAllProducts, GetAllProductsResult


class GetAllProductsUseCase(GetAllProducts):
    def __init__(self, product_repository: IProductRepository) -> None:
        self.product_repository = product_repository

    async def execute(self) -> GetAllProductsResult:
        products = await self.product_repository.get_all()

        return {"products": products}
