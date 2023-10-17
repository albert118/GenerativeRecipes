# from flask_injector import FlaskInjector
# from connexion.resolver import RestyResolver
from infrastructure.ModelProvider import ModelProvider


def configure_modules(binder):
    binder.bind(
        ModelProvider
    )


def configure_api(app):
    app.add_api('swagger.yaml')


def configure_app(app):
    configure_api(app)
    configure_modules(app)

    return app
    
