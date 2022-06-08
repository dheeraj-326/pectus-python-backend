from flask import Flask
from flask_caching import Cache
from routes.expanses_data import expanses_data_route

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache"
}


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_mapping(config)
    app.register_blueprint(expanses_data_route, url_prefix='/expanses_data')

    @app.route('/')
    def check():
        return "Yes, working"

    cache = Cache(app)
    app.run(host='0.0.0.0')
