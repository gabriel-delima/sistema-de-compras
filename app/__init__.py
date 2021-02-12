from flask import Flask
from app.config import Config
from app.extensions import db, migrate, mail, jwt

from app.carrinho.routes import carrinho_api
from app.endereco.routes import endereco_api
from app.pedido.model import Pedidos # rotas nao implementadas 
from app.produto.model import Produtos, ImagensProduto # rotas nao implementadas 
from app.produtos_compra.routes import produto_compra_api
from app.usuario.routes import usuario_api
from app.association import  association_pedidos_produtos_compra, association_pedidos_produtos_compra


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)
    jwt.init_app(app)
    
    # rotas implementadas 
    app.register_blueprint(carrinho_api)
    app.register_blueprint(usuario_api)
    app.register_blueprint(endereco_api)
    app.register_blueprint(produto_compra_api)
    

    return app