import os
from flask import Flask, render_template, jsonify, request
from flask_api import FlaskAPI
from flask_cors import CORS 
from repository.suggestion_repository import SuggestionRepository      
from repository.database_helper import DatabaseHelper

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

suggestionsRepository = SuggestionRepository()
     
@app.route("/suggestions", methods=["GET"])
def hello():
    database = DatabaseHelper() 
    response = suggestionsRepository.findAllSuggestion(database)
    return jsonify(response)

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()