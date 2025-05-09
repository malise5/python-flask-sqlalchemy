from app import app
from models import Production, db

# db.init_app(app)

with app.app_context():
    Production.query.delete()

    p1 = Production(
        title='Inception',
        genre='Sci-Fi',
        budget=160000000,
        imageUrl='https://example.com/inception.jpg',
        director='Christopher Nolan',
        description='A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.'
    )
    p2 = Production(
        title='The Godfather',
        genre='Crime',
        budget=6000000,
        imageUrl='https://example.com/godfather.jpg',
        director='Francis Ford Coppola',
        description='An organized crime dynasty\'s aging patriarch transfers control of his clandestine empire to his reluctant son.'
    )
    p3 = Production(
        title='The Dark Knight',
        genre='Action',
        budget=185000000,
        imageUrl='https://example.com/darkknight.jpg',
        director='Christopher Nolan',
        description='When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.'
    )
    p4 = Production(
        title='Pulp Fiction',
        genre='Crime',
        budget=8000000,
        imageUrl='https://example.com/pulpfiction.jpg',
        director='Quentin Tarantino',
        description='The lives of two mob hitmen, a boxer, a gangster\'s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'
    )

    db.session.add_all([p1, p2, p3, p4])  # ✅ Correct
    db.session.commit()
    print("Database seeded with initial data.")