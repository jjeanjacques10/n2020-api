import os
from flask import Flask, render_template, jsonify, request
from flask_api import FlaskAPI
from flask_cors import CORS 
from repository.suggestion_repository import SuggestionRepository      
from repository.user_repository import UserRepository      
from repository.database_helper import DatabaseHelper

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

suggestionsRepository = SuggestionRepository()
userRepository = UserRepository()
     
@app.route("/suggestions", methods=["GET"])
def hello():
    database = DatabaseHelper() 
    response = suggestionsRepository.findAll(database)
    return jsonify(response)

@app.route("/user/login", methods=["GET"])
def login_user():
    email = request.args.get('email')
    password = request.args.get('password')

    database = DatabaseHelper() 
    response = userRepository.login(database, email, password)
    return jsonify([response])

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()