from flask import Blueprint

from app.endereco.controllers import EnderecoDetails, PaginaEnderecos

endereco_api = Blueprint('endereco_api', __name__)

endereco_api.add_url_rule(
    '/enderecos', view_func= EnderecoDetails.as_view('endereco_details'), methods=['GET','POST']
)

endereco_api.add_url_rule(
    '/enderecos/<int:id>', view_func= PaginaEnderecos.as_view('pagina_endereco'), methods=['GET','PUT','PATCH','DELETE']
)
