from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

episodes = [
    {"id": 1, "date": "1/11/99", "number": 1},
    {"id": 2, "date": "1/12/99", "number": 2}
]

guests = [
    {"id": 1, "name": "Michael J. Fox", "occupation": "actor"},
    {"id": 2, "name": "Sandra Bernhard", "occupation": "Comedian"},
    {"id": 3, "name": "Tracey Ullman", "occupation": "television actress"}
]

appearances = []

# a. GET /episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    return jsonify(episodes)

# b. GET /episodes/:id
@app.route('/episodes/<int:episode_id>', methods=['GET'])
def get_episode(episode_id):
    episode = next((ep for ep in episodes if ep['id'] == episode_id), None)
    if episode is None:
        return jsonify({"error": "Episode not found"}), 404
    
    episode_appearances = [
        {
            "episode_id": episode_id,
            "guest": next((guest for guest in guests if guest['id'] == appearance['guest_id']), None),
            "guest_id": appearance['guest_id'],
            "id": appearance['id'],
            "rating": appearance['rating']
        }
        for appearance in appearances if appearance['episode_id'] == episode_id
    ]
    
    response = {
        **episode,
        "appearances": episode_appearances
    }
    return jsonify(response)

# c. GET /guests
@app.route('/guests', methods=['GET'])
def get_guests():
    return jsonify(guests)

# d. POST /appearances
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')
    
    if not episode_id or not guest_id or 'rating' not in data:
        return jsonify({"errors": ["validation errors"]}), 400

    episode_exists = any(ep['id'] == episode_id for ep in episodes)
    guest_exists = any(guest['id'] == guest_id for guest in guests)
    
    if not episode_exists or not guest_exists:
        return jsonify({"errors": ["validation errors"]}), 400

    appearance_id = len(appearances) + 1
    new_appearance = {
        "id": appearance_id,
        "rating": data['rating'],
        "guest_id": guest_id,
        "episode_id": episode_id
    }
    appearances.append(new_appearance)

    response = {
        "id": appearance_id,
        "rating": new_appearance['rating'],
        "guest_id": new_appearance['guest_id'],
        "episode_id": new_appearance['episode_id'],
        "episode": next(ep for ep in episodes if ep['id'] == episode_id),
        "guest": next(guest for guest in guests if guest['id'] == guest_id)
    }
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)