import os
from flask import Flask, render_template, jsonify, request
from flask_api import FlaskAPI
from flask_cors import CORS 
from repository.suggestion_repository import SuggestionRepository      
from repository.user_repository import UserRepository      
from repository.messages_repository import MessageRepository
from repository.database_helper import DatabaseHelper

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

suggestionsRepository = SuggestionRepository()
userRepository = UserRepository()
messageRepository = MessageRepository()
     
@app.route("/suggestions", methods=["GET"])
def hello():
    database = DatabaseHelper() 
    response = suggestionsRepository.findAll(database)
    return jsonify(response)

@app.route("/user/login", methods=["POST"])
def login_user():
    user = request.get_json()
    print(user)

    database = DatabaseHelper() 
    response = userRepository.login(database, user)
    return jsonify([response])

@app.route("/user", methods=["POST"])
def insert_user():
    user = request.get_json()
    database = DatabaseHelper() 
    response = userRepository.insert(database, user)
    return jsonify(response)

@app.route("/user/<userId>", methods=["PUT"])
def update_user(userId):
    
    user = request.get_json()
    print(user)
    
    database = DatabaseHelper() 
    response = userRepository.update(database, user, userId)
    
    return jsonify(response)

@app.route("/messages/<userId>", methods=["GET"])
def messages_list(userId):

    database = DatabaseHelper() 
    response = messageRepository.findById(database,userId)
    return jsonify(response)

@app.route("/messages", methods=["POST"])
def messages_insert():
    message = request.get_json()
    print(message)
    
    database = DatabaseHelper() 
    response = messageRepository.insert(database, message)
    
    return jsonify({"id":1})

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()