from flask import Flask

from src.routes.expanses_data import expanses_route
from src.util.caching import cache

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache"
}


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(expanses_route, url_prefix='/expanses_data')
    app.config.from_mapping(config)


    @app.route('/')
    def check():
        return "Yes, working"

    cache.init_app(app)
    app.run(host='0.0.0.0')
