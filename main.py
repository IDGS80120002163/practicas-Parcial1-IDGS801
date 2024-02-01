from flask import Flask, render_template, request
import forms
import math

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

@app.route("/distancia", methods=["GET", "POST"])
def alumnos():
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    resultado = 0
    alumno_clase = forms.UserForm(request.form)
    if request.method == 'POST':
        if alumno_clase.x1.data is not None:
            x1 = float(alumno_clase.x1.data)
        if alumno_clase.x2.data is not None:
            x2 = float(alumno_clase.x2.data)
        if alumno_clase.y1.data is not None:
            y1 = float(alumno_clase.y1.data)
        if alumno_clase.y2.data is not None:
            y2 = float(alumno_clase.y2.data)
        print('Punto x1: {}'.format(x1))
        print('Punto x2: {}'.format(x2))
        print('Punto y1: {}'.format(y1))
        print('Punto y2: {}'.format(y2))
        resultado = math.sqrt((y1-x1)**2+(y2-x2)**2)
        print('El resultado es: {}'.format(resultado))
    
    return render_template("distancia.html", form = alumno_clase, x1 = x1, x2 = x2, y1 = y1, y2 = y2, resultado = resultado)

if __name__=="__main__":
    app.run(debug=True)
