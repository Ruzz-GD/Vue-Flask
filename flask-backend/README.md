# Before proceeding make sure you already install the python globally in your system if not you can go to there website "https://www.python.org/downloads" and install the latest python version or Python 3.12.3 

# If you already configure python in your system you can follow this step

# (1) Create a Virtual Environment: 
Navigate to your project's main directory(Vue-Flask) then run this command 
```
python -m venv .venv
```

# (2) Activate the Virtual Environment: 
By running this command in main directory(Vue-Flask)
``` 
.venv\Scripts\activate
```
You can si if it's already activate when you see this (.venv)

# (3) Install Dependencies: 
While the virtual environment is active, install all dependencies listed in the requirements.txt file by running 
```
pip install -r requirements.txt 
```
To ensure all dependencies are installed run 
```
pip list
```
this will display a list of all installed packages in the virtual environment.
or you can do the configuration bellow in bottom about dependencies you need to install in this project

# (4) Use your Virtual Environment as interpreter: 
Open your project in Visual Studio Code and open any python file for example FlaskApp.py then in the 
right bottom corner you can see python and -> the version click the version to pop up the list of available interpreters in the list you can see a "Enter interpreter PATH" click it and find or navigate to the PATH of .venv you created and continue to "Scripts\python" like on me 
-> "C:\Users\ruzhe\Vue-Flask\ .venv\Scripts\python" 
this my path and this only a example

# (5) Configure the Database: 
Navigate to DatabaseConnector.py and edit the database configuration settings according to your database setup, including the host, username, password, and database name. This file is responsible for creating database tables using SQLAlchemy. 

# (6) Run the Flask Application: 
In any terminal navigate to FlaskApp.py and execute "python FlaskApp.py" to run the Flask application. Ensure the virtual environment is active before running the Flask application. 
Or you can direct run it by "right clicking" the FlaskApp.py and run code but make sure you already configure the -> "(4) Use your Virtual Environment as interpreter" 


# install this while you'r virtual environment was active
## you dont need to do this if you do the (3) Install Dependencies

### Flask: Flask is a lightweight web framework for Python. It's designed to be simple and easy to use, allowing developers to quickly build web applications.
```
pip install Flask
```
### Flask-Cors: Flask-Cors is an extension for Flask that adds support for Cross-Origin Resource Sharing (CORS). CORS is a mechanism that allows web servers to specify which origins are permitted to access their resources.
```
pip install flask-cors
```
### SQLAlchemy: SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a set of high-level abstractions for working with databases, allowing developers to interact with databases using Python objects rather than raw SQL queries.
```
pip install SQLAlchemy
```
### mysqlclient: mysqlclient is a MySQL database connector for Python. It's a fork of MySQL-Python and provides a Python interface for connecting to and interacting with MySQL databases.
```
pip install mysqlclient
```

