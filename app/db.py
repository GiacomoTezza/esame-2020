import pymysql as mariadb
from pymysql.constants import CLIENT
import click
from flask import current_app, g
from flask.cli import with_appcontext
from os import getenv


def get_db():
    """
    Function that creates the connection to the database
    using the enviroment variables of the .env file
    and stores this connection in the app context 
    so it's accessible from all the pages
    """
    if 'db' not in g:
        g.db = mariadb.connect(
            host=getenv('DB_HOST'),
            user=getenv('DB_USER'),
            password=getenv('DB_PWD'),
            database='drivingschool',
            client_flag=CLIENT.MULTI_STATEMENTS
        )
    return g.db


def close_db(e=None):
    """
    Function that closes the connection 
    and free the context from the connection
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """
    Function that loads the ddl instructions and initializes the database
    creating it if it doesn't exists yet
    """
    instance = mariadb.connect(
        host=getenv('DB_HOST'),
        user=getenv('DB_USER'), 
        password=getenv('DB_PWD')
    )
    cursor = instance.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS drivingschool')
    instance.close()

    db = get_db()
    cursor = db.cursor()

    with current_app.open_resource('db/schema.ddl.sql') as f:
        cursor.execute(f.read().decode('utf8'))
    
    db.commit()
    cursor.close()


def fill_db():
    """
    Function that loads the dump instructions and fills the database
    creating fake records for development and showcase purposes
    """
    db = get_db()
    cursor = db.cursor()

    with current_app.open_resource('db/data.dump.sql') as f:
        cursor.execute(f.read().decode('utf8'))
    
    db.commit()
    cursor.close()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Association of the initialization function
    with the click-library cli command
    """
    click.echo(getenv('DB_HOST'))
    init_db()
    click.echo('Database initialized.')


@click.command('fill-db')
@with_appcontext
def fill_db_command():
    """
    Association of the data-fill function
    with the click-library cli command
    """
    fill_db()
    click.echo('Database filled.')


def init_app(app):
    """
    Registration of the click-library cli commands
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(fill_db_command)