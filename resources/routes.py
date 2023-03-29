from resources.seller_resources import RegisterSeller, LoginSeller
from resources.user_resource import RegisterUser, LoginUser
from resources.product_resource import ProductList, ApproveProductPurchase, RejectProductPurchase

routes = (
    (RegisterSeller, "/seller/register"),
    (LoginSeller, "/seller/login"),
    (RegisterUser, "/user/register"),
    (LoginUser, "/user/login"),
    (ProductList, "/seller/products"),
    (ApproveProductPurchase, "/products/purchase/<int:id_>/approve"),
    (RejectProductPurchase, "/products/purchase/<int:id_>/reject")
)