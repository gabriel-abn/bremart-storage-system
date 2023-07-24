from src.application.repositories import IProductRepository
from src.domain.use_cases.product import (
    EditProduct,
    EditProductParams,
    EditProductResult,
)


class EditProductUseCase(EditProduct):
    def __init__(self, product_repository: IProductRepository) -> None:
        self.product_repository = product_repository

    async def execute(self, params: EditProductParams) -> EditProductResult:
        raise NotImplementedError()
