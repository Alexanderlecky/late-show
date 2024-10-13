import csv

def seed_database():
    with open('guests.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            guest = Guest(name=row['Raw_Guest_List'], occupation=row['GoogleKnowledge_Occupation'])
            # Your code to save the guest...
