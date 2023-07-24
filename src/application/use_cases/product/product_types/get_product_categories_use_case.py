from src.domain.entities.product_types import categories
from src.domain.use_cases.product.product_types import (
    GetProductCategories,
    GetProductCategoriesParams,
    GetProductCategoriesResult,
)


class GetProductCategoriesUseCase(GetProductCategories):
    def execute(self, params: GetProductCategoriesParams) -> GetProductCategoriesResult:
        product_categories = []

        for type in categories:
            if params["product_type"] == type[0].value:
                product_categories = type[1]

        return {"product_categories": product_categories}
