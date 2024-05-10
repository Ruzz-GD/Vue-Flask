from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DatabaseTable import Base 

def db_conn():
    engine = create_engine('mysql://root:@localhost/try_db')
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        Base.metadata.create_all(engine) #this create all table register in Base
        print("Successfully connected to the database")
        return session
    except Exception as e:
        print(f"Error connecting to database or creating tables: {e}")
        return None
    
# Update this engine configuration according to your database settings.
# Replace 'root' with your database user, 'localhost' with your database host,
# and 'try_db' with your database name.
# If you have a password, include it in the connection string like this:
# engine = create_engine('mysql://user:yourpassword@host/database')
# Example:
# engine = create_engine('mysql://root:yourpassword@localhost/try_db')


