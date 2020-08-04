import os
from flask import Flask
from pocket_blog.models import *
from pocket_blog import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
db.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    # db.create_all()
