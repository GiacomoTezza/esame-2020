# Elaborato Individuale di Informatica e Sistemi e Reti
ITI G. Marconi, Verona

Class 5AI, Student: TEZZA GIACOMO

## Prerequisites
```
python3.x
virtualenv
mariadb
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

You can optionally start a virtual enviroment
```
virtualenv venv
source venv/bin/activate
```

Install dependencies
```
pip install -r requirements.txt
```

Check now the file `.env` end edit the username and password for your mariadb instance

Initialize the database
```
cd ..
flask init-db
flask fill-db
```

Run the application
```
flask run
```

Now you can open a browser and go on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)