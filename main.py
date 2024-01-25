from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def resul():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")        
        operacion = request.form.get("operacion")
        
        if operacion == "suma":
            return "La {} de {} + {} = {}".format(operacion, num1, num2, str(int(num1) + int(num2)))
        elif operacion == "resta":
            return "La {} de {} - {} = {}".format(operacion, num1, num2, str(int(num1) - int(num2)))
        elif operacion == "multiplicacion":
            return "La {} de {} X {} = {}".format(operacion, num1, num2, str(int(num1) * int(num2)))
        elif operacion == "division":
            return "La {} de {} / {} = {}".format(operacion, num1, num2, str(int(num1) / int(num2)))

if __name__=="__main__":
    app.run(debug=True)
