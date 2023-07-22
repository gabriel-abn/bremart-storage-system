from src.application.apis import IDataValidation
from src.application.common import ApplicationError
from src.application.protocols import ICrypter, IUUIDGenerator
from src.application.repositories import IDistributorRepository
from src.domain.entities.distributor import Distributor
from src.domain.use_cases.distributor import (
    CreateDistributor,
    CreateDistributorParams,
    CreateDistributorResult,
)


class CreateDistributorUseCase(CreateDistributor):
    def __init__(
        self,
        distributor_repository: IDistributorRepository,
        crypter: ICrypter,
        uuid_generator: IUUIDGenerator,
        data_validation: IDataValidation,
    ) -> None:
        self.distributor_repository = distributor_repository
        self.crypter = crypter
        self.uuid_generator = uuid_generator
        self.data_validation = data_validation

    async def execute(self, params: CreateDistributorParams) -> CreateDistributorResult:
        if not await self.data_validation.validate_cnpj(params["distributor"]["cnpj"]):
            raise ApplicationError("Invalid CNPJ", "CreateDistributorUseCase")

        id = self.uuid_generator.generate()

        if not id:
            raise ApplicationError("Error to generate id", "CreateDistributorUseCase")

        distributor = Distributor.create(params["distributor"], id)

        distributor_id = await self.distributor_repository.create(distributor)

        return {
            "crypted_id": self.crypter.encrypt(str(distributor_id["id"])),
        }
