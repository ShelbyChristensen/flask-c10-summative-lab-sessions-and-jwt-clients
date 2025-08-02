from app import app, db
from models import User, Note
from faker import Faker

fake = Faker()

with app.app_context():
    print("Seeding database...")
    db.drop_all()
    db.create_all()

    # Create a test user
    user = User(username="demo")
    user.password = "password"
    db.session.add(user)
    db.session.commit()

    # Create sample notes
    for _ in range(10):
        note = Note(
            title=fake.sentence(nb_words=5),
            content=fake.paragraph(nb_sentences=3),
            user_id=user.id
        )
        db.session.add(note)

    db.session.commit()
    print("Seeding complete.")
