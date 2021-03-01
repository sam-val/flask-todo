from app_package import app, db
from app_package.models import User, Task

@app.shell_context_processor
def make_shell_context():
    return {'User': User, 'db': db, 'Task': Task}
