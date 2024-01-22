import mysql.connector
from mysql.connector import errorcode
import random
from faker import Faker

# Create a connection to the MySQL server
def create_connection():
    try:
        cnx = mysql.connector.connect(
            user="root",
            password="osmi0207",
            host="localhost",  # Change this to your MySQL server host if needed
            database="film3"
        )
        print("Connection established with the database")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None


connection = create_connection()

# Create a cursor object
cursor = connection.cursor()

# Create a Faker instance
fake = Faker()

# Number of records to generate
num_records = 1000000

# Create Film table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Film (
        Film_id INTEGER,
        Title VARCHAR(255),
        ReleaseDate DATE,
        Genre VARCHAR(255),
        Runtime INTEGER
    )
"""
)

# Create CrewMember table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS CrewMember (
        Crew_id INTEGER,
        Crew_Member_Name VARCHAR(100),
        Crew_Member_Role VARCHAR(100),  
        Film_id INT,
        FOREIGN KEY(Film_id) REFERENCES Film(Film_id)
    )
"""
)

# Create Soundtrack table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Soundtrack (  
        Soundtrack_id INT AUTO_INCREMENT PRIMARY KEY,
        SongTitle VARCHAR(255),
        Film_id INT,
        ReleaseDate DATE,
        FOREIGN KEY(Film_id) REFERENCES Film(Film_id)
    )
"""
)

# Generate and insert data for Film table
for _ in range(num_records):
    title = fake.catch_phrase()
    release_date = fake.date_this_decade()
    genre = fake.word()
    runtime = random.randint(60, 180)

    cursor.execute(
        """
        INSERT INTO Film (Title, ReleaseDate, Genre, Runtime)
        VALUES (%s, %s, %s, %s)
    """,
        (title, release_date, genre, runtime),
    )

# Commit the changes for Film table
connection.commit()

# Generate and insert data for CrewMember table
film_ids = [i for i in range(1, num_records + 1)]  # Assuming Film_id starts from 1

for _ in range(num_records):
    crew_id = random.randint(1, 999999)
    crew_member_name = fake.name()
    crew_member_role = fake.job()
    film_id = random.choice(film_ids)

    cursor.execute(
        """
        INSERT INTO CrewMember (Crew_id, Crew_Member_Name, Crew_Member_Role, Film_id)
        VALUES (%s, %s, %s, %s)
    """,
        (crew_id, crew_member_name, crew_member_role, film_id),
    )

# Commit the changes for CrewMember table
connection.commit()

# Generate and insert data for Soundtrack table
for _ in range(num_records):
    soundtrack_id = random.randint(1, 999999)
    song_title = fake.catch_phrase()
    film_id = random.choice(film_ids)
    release_date = fake.date_this_decade()

    cursor.execute(
        """
        INSERT INTO Soundtrack (Soundtrac_id, SongTitle, Film_id, ReleaseDate)
        VALUES (%s, %s, %s, %s)
    """,
        (soundtrack_id, song_title, film_id, release_date),
    )

# Commit the changes for Soundtrack table
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()