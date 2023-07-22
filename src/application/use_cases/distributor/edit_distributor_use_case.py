from src.application.common.application_error import ApplicationError
from src.application.protocols.crypter import ICrypter
from src.application.repositories.distributor_repository import IDistributorRepository
from src.domain.entities.distributor import Distributor
from src.domain.use_cases.distributor.edit_distributor import (
    EditDistributor,
    EditDistributorParams,
    EditDistributorResult,
)


class EditDistributorUseCase(EditDistributor):
    def __init__(
        self, distributor_repository: IDistributorRepository, crypter: ICrypter
    ):
        self.distributor_repository = distributor_repository
        self.crypter = crypter

    async def execute(self, params: EditDistributorParams) -> EditDistributorResult:
        distributor = await self.distributor_repository.find_by_cnpj(
            params["distributor"]["cnpj"]
        )

        if not distributor:
            raise ApplicationError(
                "Distributor not found",
                "EditDistributorUseCase",
            )

        distributor = Distributor.create(params["distributor"], "")

        id = await self.distributor_repository.update(distributor)

        return {"crypted_id": self.crypter.encrypt(str(id))}
