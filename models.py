import csv
from models import db, Guest
from app import app

def seed_database():
    with app.app_context():
        with open('data/guests.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                guest = Guest(name=row['name'], occupation=row['occupation'])
                db.session.add(guest)
            db.session.commit()

if __name__ == '__main__':
    seed_database()
