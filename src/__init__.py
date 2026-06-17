# configuracao das bibliotecas externas/dependecias
# instanciar aqui e configurar
# configurar a connection para apontar para o confiig object do flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object('connection')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
api = Api(app)


swagger = Swagger(app, config={
    # cabeçalho extra da requisição
    # configura a autenticação
    "headers":[],
    "specs":[
        {
            # http://localhost:5000/apispec.json
            "endpoint":"apispec",
            "route": "/apispec.json",
            # incluir todas as rotas
            "rule_filter": lambda rule: True,
            # inclui todas as models na docs
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui" : True,
    "specs_route": "/docs/"
})


# TODO : Apontar os modelos criados para a orm conseguir criar as tabelas

from .models.usuario_model import UsuarioModel


# TODO: Apontar quem são as minhas views
from .views import usuario_view