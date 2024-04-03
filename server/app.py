from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from db import db


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from models import Message
migrate = Migrate(app, db)

@app.route('/messages', methods=['POST', 'GET'])
def create_message():
    data = request.json
    email = data.get('email')
    content = data.get('content')

    
    new_message = Message(
        email=email,
        content=content
    )

    db.session.add(new_message)
    db.session.commit()

    return jsonify({'message': 'Message created successfully'}), 201

if __name__ == "__main__":
    app.run(debug=True)
