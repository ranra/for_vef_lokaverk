import pymysql
from bottle import *

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2209922929', passwd='mypassword', db='2209922929_lokaverk')
cur = conn.cursor()



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

    nafn = request.forms.get("nafn")

    global row
    cur.execute("SELECT * FROM highscore")
    for row in cur:
        if str(nafn) in row :
            return template("online.tpl", row = row)
        else:
            pass
            #return template("looser.tpl", name = name)
    cur.close()
    conn.close()



@post("/eyda")
def doit():
    global name
    cur.execute("Delete from highscore where name = %s " % name)
    conn.commit()
    cur.close()
    conn.close()

def go ():
    run()

