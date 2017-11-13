from flask_script import Manager

from app import create_app, db
from flask_migrate import Migrate,MigrateCommand,upgrade#数据库迁移引入
app=create_app()
manager=Manager(app)

#数据库迁移的关于
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.command
def dev():
    from livereload import Server
    live_server=Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=False)


@manager.command
def test():
    pass

@manager.command
def deploy():
    upgrade()



if __name__ == '__main__':

    manager.run()
