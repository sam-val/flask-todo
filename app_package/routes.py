from app_package import app

@app.route('/')
@app.route('/index1')
def index():
    return "hello, world."





