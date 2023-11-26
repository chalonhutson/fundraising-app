import os
import server
import models
from faker import Faker

fake = Faker()

os.system("dropdb fundraising")
os.system("createdb fundraising")

models.connect_to_db(server.app)

with server.app.app_context():
    models.db.create_all()

    user1 = models.User("test", "test@test.com", "password")
    user2 = models.User("johnsmith", "johnsmith@email.com", "password")
    models.db.session.add_all([user1, user2])
    models.db.session.commit()

    for _ in range(50):
        donor = models.Donor(
            name=fake.name(),
            status=fake.random_element(elements=("prospect", "ask", "pledge", "donor")),
            prospect_amount=fake.random_element(elements=(100, 500, 1000, 5000, 10000)),
            user_id=fake.random_element(elements=(user1.id, user2.id))
        )
        models.db.session.add(donor)

    models.db.session.commit()

    print("Database seeded!")

