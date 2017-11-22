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
    list = []
    nafn = request.forms.get("nafn")

    cur.execute("SELECT * FROM highscore")
    for row in cur:
        if str(nafn) in row :
            list.append([row])
            return template("online.tpl", listi=list)


        else:
            print(row[0])
            print("nei")
            #return template("looser.tpl", name = name)



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

def go ():
    run()

