from .edit_storage import EditStorage, EditStorageParams, EditStorageResult
from .get_all_storages import GetAllStorages, GetAllStoragesResult
from .get_storage_by_id import (
    GetStorageById,
    GetStorageByIdParams,
    GetStorageByIdResult,
)
from .register_storage import (
    RegisterStorage,
    RegisterStorageParams,
    RegisterStorageResult,
)
from .remove_storage import RemoveStorage, RemoveStorageParams, RemoveStorageResult
from .stock_products import StockProducts, StockProductsParams, StockProductsResult
from .unstock_products import (
    UnstockProducts,
    UnstockProductsParams,
    UnstockProductsResult,
)

__all__ = [
    # RegisterStorage
    "RegisterStorage",
    "RegisterStorageParams",
    "RegisterStorageResult",
    # GetStorageById
    "GetStorageById",
    "GetStorageByIdParams",
    "GetStorageByIdResult",
    # EditStorage
    "EditStorage",
    "EditStorageParams",
    "EditStorageResult",
    # StockProducts
    "StockProducts",
    "StockProductsParams",
    "StockProductsResult",
    # UnstockProducts
    "UnstockProducts",
    "UnstockProductsParams",
    "UnstockProductsResult",
    # RemoveStorage
    "RemoveStorage",
    "RemoveStorageParams",
    "RemoveStorageResult",
    # GetAllStorages
    "GetAllStorages",
    "GetAllStoragesResult",
]
