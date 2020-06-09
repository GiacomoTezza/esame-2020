# Elaborato Individuale di Informatica e Sistemi e Reti
ITI G. Marconi, Verona

Class 5AI, Student: TEZZA GIACOMO

## Prerequisites
```
python3.8+
virtualenv
mariadb
```
Python libraries:
```
click==7.1.2
Flask==1.1.2
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
PyMySQL==0.9.3
Werkzeug==1.0.1
```

## Configuration & Installation Procedure
To clone and run this application, you'll need Git, Python, virtualenv and MariaDB installed on your computer. From your command line:


Clone this repository
```
git clone https://github.com/GiacomoTezza/esame-2020
```

Go into the repository
```
cd esame-2020/
```

Start the virtual enviroment
```
virtualenv venv
source venv/bin/activate
```

Install dependencies
```
pip3 install Flask PyMySql
```

Configure Flask enviroment variables
```
cd ..
export FLASK_APP=esame-2020
export FLASK_ENV=development
```

Initialize the database
```
flask init-db
flask fill-db
```

Run the application
```
flask run
```

Now you can open a browser and go on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)