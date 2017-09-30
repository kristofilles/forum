from flask import Flask, render_template, redirect, url_for, request

import datahandler
import queries

app = Flask(__name__)


@app.route('/')
def route_list():
    jobs = datahandler.query_select(queries.SELECT_ALL_JOBS)
    return render_template('main.html', jobs=jobs)


if __name__ == "__main__":
    app.run(
        debug=True
    )