from flask import Blueprint

from app.usuario.controllers import UsuarioDetails, PaginaUsuario, UsuarioLogin

usuario_api = Blueprint('usuario_api', __name__)

usuario_api.add_url_rule(
    '/usuarios', view_func= UsuarioDetails.as_view('usuario_details'), methods=['GET','POST']
)

usuario_api.add_url_rule(
    '/usuarios/<int:id>', view_func= PaginaUsuario.as_view('pagina_usuario'), methods=['GET','PUT','PATCH','DELETE']
)

usuario_api.add_url_rule(
    '/usuarios/login', view_func= UsuarioLogin.as_view('usuario_login'), methods=['POST']
)

