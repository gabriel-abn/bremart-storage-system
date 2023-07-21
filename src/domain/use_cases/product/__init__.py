from .edit_product import EditProduct, EditProductParams, EditProductResult
from .get_all_products import GetAllProducts, GetAllProductsResult
from .get_product import GetProduct, GetProductParams, GetProductResult
from .get_products_per_distributor import (
    GetProductsPerDistributor,
    GetProductsPerDistributorParams,
    GetProductsPerDistributorResult,
)
from .register_many_products import (
    RegisterManyProducts,
    RegisterManyProductsParams,
    RegisterManyProductsResult,
)
from .register_product import (
    RegisterProduct,
    RegisterProductParams,
    RegisterProductResult,
)

__all__ = [
    # RegisterProduct
    "RegisterProduct",
    "RegisterProductParams",
    "RegisterProductResult",
    # GetProduct
    "GetProduct",
    "GetProductParams",
    "GetProductResult",
    # GetAllProducts
    "GetAllProducts",
    "GetAllProductsResult",
    # EditProduct
    "EditProduct",
    "EditProductParams",
    "EditProductResult",
    # GetProductsPerDistributor
    "GetProductsPerDistributor",
    "GetProductsPerDistributorParams",
    "GetProductsPerDistributorResult",
    # RegisterManyProducts
    "RegisterManyProducts",
    "RegisterManyProductsParams",
    "RegisterManyProductsResult",
]
