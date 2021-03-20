from flask import Flask


def create_app():
    app = Flask("test")

    @app.route("/")
    def home():
        return "Hello, world!"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
