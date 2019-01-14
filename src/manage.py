# -*- coding: utf-8 -*-
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand

from benandfrank import app, models


migrate = Migrate(app, models.db)

@migrate.configure
def configure_alembic(config):
    print(config)
    # modify config object
    return config

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
