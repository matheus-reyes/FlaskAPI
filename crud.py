from flask import Flask

app = Flask(__name__)


@app.route('/inicio')
def helloWorld() -> str:
    return "<h1> Hello World!</h1>"


app.run()
