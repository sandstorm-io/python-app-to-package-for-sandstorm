#!env/bin/python

import os

from flask import Flask, render_template
import oursql

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    HIT_COUNTER_PATH = "/var/number.txt"
    # if no hit count exists, create one
    if not os.path.exists(HIT_COUNTER_PATH):
        with open(HIT_COUNTER_PATH, "w") as f:
            f.write("0\n")
    # load hit count
    hit_count = None
    with open(HIT_COUNTER_PATH) as f:
        hit_count = int(f.read().strip(), 10)
        hit_count += 1 # increment hit count
    # save hit count
    with open(HIT_COUNTER_PATH, "w") as f:
        f.write(str(hit_count) + '\n')

    # Test database connection
    conn = oursql.connect(host='127.0.0.1', user='root', passwd="")
    curs = conn.cursor()
    curs.execute("SELECT 1 + 1")
    dbresult = curs.fetchone()

    return render_template("index.html", hit_count=hit_count, dbresult=dbresult)

application = app.wsgi_app
print "Prepared."
