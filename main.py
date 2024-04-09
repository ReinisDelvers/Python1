from flask import Flask, render_template, request
from dati import nolasit_rind, pierakstit

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def teksts():
    return render_template("teksts.html")

@app.route("/saraksts")
def saraksts():
    saraksts = []
    bildes = []
    kopejais_saraksts = []
    faila_rind = nolasit_rind()
    for rind in faila_rind:
        elements = rind.split(", ")
        kopejais_saraksts.append(elements)
        saraksts.append(elements[0])
        bildes.append(elements[1])

    return render_template("saraksts.html", vardi = saraksts, bildes = bildes, garums = len(saraksts), visi = kopejais_saraksts)

@app.route("/info", methods=["POST", "GET"])
def info():
    if request.method == "POST":
        rinda=""
        nosaukums = request.form["nosaukums"]
        adrese = request.form["adrese"]
        rinda = nosaukums + ", " + adrese
        pierakstit(rinda)
    return render_template("info.html")




if __name__ == "__main__":
    app.run(port = 5000)
