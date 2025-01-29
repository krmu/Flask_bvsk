from flask import Flask, jsonify,render_template,request
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tests")
def tests():
    return render_template('tests.html')

@app.route("/bildes")
def bildes():
    return render_template('bildes.html')

@app.route("/tabula")
def tabula():
    return render_template('tabula.html')

@app.route("/formas",methods=['GET','POST'])
def formas():
    kluda = ""
    ok = 0
    lietotaji = {"admin":"admin","lietotajs":"parole"}
    if "autorizet" in request.form:
        if request.form["username"] == "" or request.form["parole"] == "":
            kluda = "Nav aizpildīti visi lauciņi!"
        else:
            if request.form["username"] in lietotaji:
                if request.form["parole"] == lietotaji[request.form['username']]:
                   ok = 1
                else:
                    kluda = "Lietotājs vai parole nav pareizs!"
            else:
                kluda = "Lietotājs vai parole nav pareizs!"
                    
    return render_template('forma.html',kluda=kluda,ok=ok)

@app.route("/joki")
def joki():
    izsaukums = requests.get("https://api.chucknorris.io/jokes/random")
    atbilde = izsaukums.json()
    return render_template('chuck_norris.html',atbilde = atbilde)

@app.route("/sodienas_datums")
def datums():
    return "06.01.2025."

@app.route("/universitates",methods=['GET','POST'])
def universitates():
    kluda = ""
    dati = []
    if "meklet" in request.form:
        if request.form["valsts"] == "":
            kluda = "Jānorāda valsts"
        else:
            izsaukums = requests.get("http://universities.hipolabs.com/search?country=" +  request.form["valsts"])
            dati = izsaukums.json()
            if len(dati) == 0:
                kluda = "Neko neatrada"
    return render_template('universitates.html',kluda=kluda,dati=dati)


@app.route("/api/sodienas_datums_laiks",methods=['POST'])
def sodienas_datums_laiks_api():
    now = datetime.now()
    datums = now.strftime("%d.%m.%Y")
    laiks = now.strftime("%H:%M:%S")
    
    atbilde = {"datums":datums,"laiks":laiks}
    
    return jsonify(atbilde)

@app.route("/sodienas_datums_laiks",methods=['GET'])
def sodienas_datums_laiks():
    
    return render_template('sodienas_datums_laiks.html') 

app.run(debug=True,host='0.0.0.0',port=80)