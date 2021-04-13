from flask import Flask
from critics import get_critics, pick_random_critic, specific_critic

def create_app():
    app = Flask("test")

    @app.route("/")
    def home():
        return "yay!"

    @app.route('/critics/', methods=["GET"])
    def all_critics():
        return get_critics()

    @app.route('/critics/random', methods=["GET"])
    def random_critic():
        return pick_random_critic(id)

    @app.route('/critics/<int:id>', methods=['GET'])
    def get_specific_critic(id):
        return specific_critic(id)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)