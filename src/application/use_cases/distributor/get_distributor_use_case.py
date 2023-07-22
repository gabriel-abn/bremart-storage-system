from src.application.apis import IDataValidation
from src.application.common import ApplicationError
from src.application.repositories import IDistributorRepository
from src.domain.use_cases.distributor import (
    GetDistributor,
    GetDistributorParams,
    GetDistributorResult,
)


class GetDistributorUseCase(GetDistributor):
    def __init__(
        self,
        distributor_repository: IDistributorRepository,
        data_validation: IDataValidation,
    ) -> None:
        self.distributor_repository = distributor_repository
        self.data_validation = data_validation

    async def execute(self, params: GetDistributorParams) -> GetDistributorResult:
        if not await self.data_validation.validate_cnpj(params["cnpj"]):
            raise ApplicationError("Invalid CNPJ.", "GetDistributorUseCase")

        distributor = await self.distributor_repository.find_one(params["cnpj"])

        return {
            "distributor": distributor,
        }
