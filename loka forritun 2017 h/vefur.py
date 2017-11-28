import os
import pymysql
from bottle import *

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2209922929', passwd='mypassword', db='2209922929_lokaverk')
cur = conn.cursor()

@route("/<stylesheet>")
def server_static(stylesheet):
    return static_file(stylesheet, root = './')


def save(name, score):

    cur.execute(
        "Insert into highscore values('{}','{}')".format(name, score))
    conn.commit()
    cur.execute("SELECT * FROM highscore")


@route("/")
def main ():
    return template("index.tpl")


@post("/check")
def check ():
    list = []
    nafn = request.forms.get("nafn")

    cur.execute("SELECT * FROM highscore")
    for row in cur:
        if str(nafn) in row :
            list.append([row])
            return template("online.tpl", listi=list)


    else:
        return template("loser.tpl", name = str(nafn))



@route("/all")
def all ():
    list = []

    cur.execute("SELECT * FROM highscore")
    for row in cur:
        list.append([row])

    return template("online.tpl", listi=list)




@post("/eyda")
def doit():
    global name
    cur.execute("Delete from highscore where name = %s " % name)
    conn.commit()
    cur.close()
    conn.close()

#def go ():
#run()

if os.environ.get('Is_Heroku') is None:
    run()
else:
    run(host="0.0.0.0", port=os.environ.get('PORT'))