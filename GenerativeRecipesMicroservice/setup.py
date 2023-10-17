from connexion import FlaskApp
from configuration import configure_app, AppSettings

app_settings = AppSettings()
app = FlaskApp(__name__)
app = configure_app(app)

if __name__ == '__main__':
    app.run(
        port=app_settings.api_port, 
        debug=app_settings.is_development()
    )
