from src.application.repositories import IDistributorRepository
from src.domain.use_cases.distributor import (
    GetAllDistributors,
    GetAllDistributorsResult,
)


class GetAllDistributorsUseCase(GetAllDistributors):
    def __init__(self, distributors_repository: IDistributorRepository):
        self.distributors_repository = distributors_repository

    async def execute(self) -> GetAllDistributorsResult:
        distributors = await self.distributors_repository.find_all()

        return {"distributors": distributors}
