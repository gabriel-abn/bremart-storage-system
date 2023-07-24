from src.domain.entities.product_types import ProductTypes
from src.domain.use_cases.product.product_types import (
    GetProductTypes,
    GetProductTypesResult,
)


class GetProductTypesUseCase(GetProductTypes):
    def execute(self) -> GetProductTypesResult:
        product_types = []

        for type in ProductTypes.__members__.keys():
            product_types.append(type)

        return {"product_types": product_types}
