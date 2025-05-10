from app import app
from models import Production, db, CrewMember

with app.app_context():
    # Reset the database (drop and recreate tables)
    db.drop_all()
    db.create_all()

    # Optional: Clear existing rows without dropping tables
    # Production.query.delete()
    # CrewMember.query.delete()

    # Create Productions
    p1 = Production(
        title='Inception',
        genre='Sci-Fi',
        budget=160000000,
        imageUrl='https://example.com/inception.jpg',
        director='Christopher Nolan',
        description='A thief who steals corporate secrets through the use of dream-sharing technology...'
    )
    p2 = Production(
        title='The Godfather',
        genre='Crime',
        budget=6000000,
        imageUrl='https://example.com/godfather.jpg',
        director='Francis Ford Coppola',
        description='An organized crime dynasty\'s aging patriarch transfers control...'
    )
    p3 = Production(
        title='The Dark Knight',
        genre='Action',
        budget=185000000,
        imageUrl='https://example.com/darkknight.jpg',
        director='Christopher Nolan',
        description='When the menace known as the Joker emerges...'
    )
    p4 = Production(
        title='Pulp Fiction',
        genre='Crime',
        budget=8000000,
        imageUrl='https://example.com/pulpfiction.jpg',
        director='Quentin Tarantino',
        description='The lives of two mob hitmen, a boxer, a gangster\'s wife...'
    )

    # Create Crew Members
    crew1 = CrewMember(name="Alice", role="Director of Photography", production=p1)
    crew2 = CrewMember(name="Bob", role="Stunt Coordinator", production=p1)
    crew3 = CrewMember(name="Cathy", role="Composer", production=p2)
    crew4 = CrewMember(name="David", role="Editor", production=p3)
    crew5 = CrewMember(name="Eve", role="Production Designer", production=p4)

    # Add and commit
    db.session.add_all([p1, p2, p3, p4, crew1, crew2, crew3, crew4, crew5])
    db.session.commit()

    print("✅ Database seeded successfully with productions and crew members!")
