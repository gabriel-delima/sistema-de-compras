from flask import Blueprint

from app.carrinho.controllers import CarrinhoDetails, PaginaCarrinhos

carrinho_api = Blueprint('carrinho_api', __name__)

carrinho_api.add_url_rule(
    '/carrinhos', view_func= CarrinhoDetails.as_view('carrinho_details'), methods=['GET','POST']
)

carrinho_api.add_url_rule(
    '/carrinhos/<int:id>', view_func= PaginaCarrinhos.as_view('pagina_carrinho'), methods=['GET','PUT','PATCH','DELETE']
)