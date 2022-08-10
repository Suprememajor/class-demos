from flask import Flask, jsonify

def create_app(test_config=None):
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
        
    @app.route('/new')
    def hello_world_json():
        return jsonify({'message':'Hello, World!'})

    return app
