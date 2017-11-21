import pymysql
from bottle import *

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2209922929', passwd='mypassword', db='2209922929_...þínkt_vef2Verk11')
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
                 highScore[1],)
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
    skraningarnumer = request.forms.get("numer")

    global row
    cur.execute("SELECT * FROM bilar")
    for row in cur:
        if row[0] == skraningarnumer :
            return template("online.tpl", row = row)
        else:
            return template("signup.tpl")
    cur.close()
    conn.close()


@route("/new")
def new ():
    return template("signup.tpl")





@route("/breytingar")
def breytingar():
    info = request.query.get("Nytt")
    return template("breyta.tpl", info = info)

@post("/breyta")
def doit():
    cur.execute("Update bilar set "
                "skraningarnumer='{}', "
                "tegund='{}', "
                "verksmidjunumer='{}',"
                "skraningardagur='{}',"
                "co2='{:d}',"
                "þyngd='{:d}',"
                "skodun='{}',"
                "stada='{}' "
                "where skraningarnumer='{}'"
                .format(nr, t, v, sd, u, ti, s, st, nr))



run()






"""
# eyða einum með ákv. kt
cur.execute("Delete from vinur where kt = 5")
conn.commit()
cur.close()
conn.close()
"""

"""
# breyta einum eftir ákv. kt
cur.execute("Update vinur set nafn='Andaya', gsm=7771234 where kt = 5")
conn.commit()
cur.close()
conn.close()
"""