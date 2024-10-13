from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# GET /episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

# GET /episodes/:id
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict())
    else:
        return jsonify({"error": "Episode not found"}), 404

# GET /guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

# POST /appearances
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    # Validation for rating
    if not (1 <= rating <= 5):
        return jsonify({"errors": ["Rating must be between 1 and 5"]}), 400

    # Create the Appearance
    appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify(appearance.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
