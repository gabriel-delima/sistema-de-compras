from flask import Blueprint

from app.produtos_compra.controllers import  ProdutosCompraDetails, PaginaProdutosCompra

produto_compra_api = Blueprint('produto_compra_api', __name__)

produto_compra_api.add_url_rule(
    '/produtos_compra', view_func= ProdutosCompraDetails.as_view('produto_compra_details'), methods=['GET','POST']
)

produto_compra_api.add_url_rule(
    '/produtos_compra/<int:id>', view_func= PaginaProdutosCompra.as_view('pagina_produto_compra'), methods=['GET','PUT','PATCH','DELETE']
)