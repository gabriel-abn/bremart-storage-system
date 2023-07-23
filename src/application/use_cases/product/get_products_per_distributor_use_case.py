from src.application.common import ApplicationError
from src.application.repositories import IDistributorRepository, IProductRepository
from src.domain.use_cases.product import (
    GetProductsPerDistributor,
    GetProductsPerDistributorParams,
    GetProductsPerDistributorResult,
)


class GetProductsPerDistributorUseCase(GetProductsPerDistributor):
    def __init__(
        self,
        products_repository: IProductRepository,
        distributor_repository: IDistributorRepository,
    ) -> None:
        self.products_repository = products_repository
        self.distributor_repository = distributor_repository

    async def execute(
        self, params: GetProductsPerDistributorParams
    ) -> GetProductsPerDistributorResult:
        distributor = await self.distributor_repository.find_by_cnpj(params["cnpj"])

        if not distributor:
            raise ApplicationError(
                "Distributor not found.", "GetProductsPerDistributorUseCase"
            )

        products = await self.products_repository.find_with_filter(
            {"distributor_id": distributor["cnpj"]}
        )

        if products == []:
            raise ApplicationError(
                "Products not found.", "GetProductsPerDistributorUseCase"
            )

        return {
            "products": products,
        }
        ...
