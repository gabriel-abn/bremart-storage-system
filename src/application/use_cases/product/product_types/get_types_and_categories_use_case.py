from src.domain.entities.product_types import categories
from src.domain.use_cases.product.product_types import (
    GetTypesAndCategories,
    GetTypesAndCategoriesResult,
)


class GetTypesAndCategoriesUseCase(GetTypesAndCategories):
    def execute(self) -> GetTypesAndCategoriesResult:
        types: list[dict[{"type": str, "categories": list[str]}]] = [
            {"type": "", "categories": []}
        ]

        for type in categories:
            types.append({"type": type[0].value, "categories": type[1]})

        return {"types_list": types}
