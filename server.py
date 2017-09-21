from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def route_list():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(
        debug=True
    )