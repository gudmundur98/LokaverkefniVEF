# Guðmundur Breiðfjörð

from bottle import *
import pymysql
import json, urllib.request

#static files route
@route("/static/<filename>")
def staticFile(filename):
    return static_file(filename, root="./static/")

@route("/")
def index():
    with urllib.request.urlopen("http://www.apis.is/concerts") as skra:
        data = json.loads(skra.read().decode())
    data = data["results"]
    return template("index.tpl",data=data)

@route("/about")
def index():
    with urllib.request.urlopen("http://www.apis.is/concerts") as skra:
        data = json.loads(skra.read().decode())
    data = data["results"]
    return template("about.tpl",data = data)

@route("/<breyta>",method=['GET', 'POST'])
def index(breyta):
    if request.forms.get("name"):
		###########################################
		###########################################
		###########################################
        connection = pymysql.connect(host='tsuts.tskoli.is',
                                     port=3306,
                                     user='0112982819',
                                     passwd='mypassword',
                                     db='0112982819_lokaverkvef')
        name = request.forms.get("name")
        email = request.forms.get("email")
        time = request.forms.get("concert")
        with connection.cursor() as cursor:
            sql = "INSERT INTO skraning (name, email, concert, time) VALUES ('"+name+"', '"+email+"', '"+breyta+"', '"+time+"')"
            cursor.execute(sql)
            connection.commit()
            connection.close()
		###########################################
		###########################################
		###########################################
    with urllib.request.urlopen("http://www.apis.is/concerts") as skra:
        data = json.loads(skra.read().decode())
    data = data["results"]
    listi = []
    for i in data:
        if i["eventDateName"] == breyta:
            listi.append(i)
    return template("concert.tpl",data=listi,)

run(host='0.0.0.0',  port=os.environ.get('PORT'))
