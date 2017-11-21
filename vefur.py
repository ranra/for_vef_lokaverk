import pymysql
from bottle import *

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2209922929', passwd='mypassword', db='2209922929_lokaverk')
cur = conn.cursor()



def save():
    searchWords = ["name", "score" ]
    highScore = []
    t = 0
    for x in searchWords:

        highScore.append(request.forms.get(x))
        t +=1

    cur.execute(
        "Insert into highscore values('{}','{}')".format(

            highScore[0],
            highScore[1],))
    conn.commit()
    cur.execute("SELECT * FROM highscore")
    for row in cur:
        if row[0] == highScore[0]:
            return template("online.tpl", row = row )
        else:
            print("blargh")



@route("/")
def main ():
    return template("index.tpl")


@post("/check")
def check ():
    global name
    name = request.forms.get("name")

    global row
    cur.execute("SELECT * FROM highscore")
    for row in cur:
        if row[0] == name :
            return template("online.tpl", row = row)
        else:
            return template("looser.tpl", name = name)
    cur.close()
    conn.close()



@post("/eyda")
def doit():
    global name
    cur.execute("Delete from highscore where name = %s " % name)
    conn.commit()
    cur.close()
    conn.close()



run()

