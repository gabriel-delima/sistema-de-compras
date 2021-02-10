from flask import Flask
from app.config import Config
from app.extensions import db, migrate

from app.carrinho.controllers import carrinho_api
from app.endereco.controllers import endereco_api
from app.pedido.model import Pedidos
from app.produto.model import Produtos, ImagensProduto
from app.produtos_compra.model import ProdutosCompra
from app.usuario.controllers import usuario_api
from app.association import  association_pedidos_produtos_compra, association_pedidos_produtos_compra


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(carrinho_api)
    app.register_blueprint(usuario_api)
    app.register_blueprint(endereco_api)
    

    return app