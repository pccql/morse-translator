from flask_swagger_ui import get_swaggerui_blueprint

swagger_blueprint = get_swaggerui_blueprint(
    '/docs',
    '/static/swagger.yaml',
    config={
        'app_name': "Morse Code Translator"
    }
)
