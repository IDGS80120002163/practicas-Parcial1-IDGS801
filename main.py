from flask import Flask, render_template, request
import forms, forms_resistencias
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

@app.route("/resistencia", methods=["GET", "POST"])
def calcularResistencias():
    b1 = 0
    b2 = 0
    b3 = 0
    tolerancia = 0
    valor = 0
    valor_maximo = 0
    valor_minimo = 0
    color_b1 = None
    color_b2 = None
    color_b3 = None
    color_tolerancia = None
    clase_resistencias = forms_resistencias.ResistenciasForms(request.form)

    if request.method == 'POST':
        b1 = clase_resistencias.b1.data
        b2 = clase_resistencias.b2.data
        b3 = clase_resistencias.b3.data
        print(b3)
        tolerancia = clase_resistencias.tolerancia.data

        opciones_colores = [(0, 'Negro'), (1, 'Café'), (2, 'Rojo'), (3, 'Naranja'), (4, 'Amarillo'),
                            (5, 'Verde'), (6, 'Azul'), (7, 'Violeta'), (8, 'Gris'), (9, 'Blanco')]
        opciones_tolerancia = [(.05, 'Oro'), (.1, 'Plata')]

        # Obtener el color seleccionado para b1
        color_b1 = next((color for valor, color in opciones_colores if valor == int(b1)), None)
        # Obtener el color seleccionado para b2
        color_b2 = next((color for valor, color in opciones_colores if valor == int(b2)), None)
        # Obtener el color seleccionado para b3
        color_b3 = next((color for valor, color in opciones_colores if valor == int(b3)), None)
        # Obtener el color seleccionado para tolerancia
        color_tolerancia = next((color for valor, color in opciones_tolerancia if valor == float(tolerancia)), None)

        # Concatenar los valores de b1 + b2
        concatenado = float(str(b1) + str(b2))

        # Calcular el valor de la resistencia
        if int(b3) == 0:
            valor = concatenado * 1
        elif int(b3) == 1:
            valor = concatenado * 10
        elif int(b3) == 2:
            valor = concatenado * 100
        elif int(b3) == 3:
            valor = concatenado * 1000
        elif int(b3) == 4:
            valor = concatenado * 10000
        elif int(b3) == 5:
            valor = concatenado * 100000
        elif int(b3) == 6:
            valor = concatenado * 1000000
        elif int(b3) == 7:
            valor = concatenado * 10000000
        elif int(b3) == 8:
            valor = concatenado * 100000000
        elif int(b3) == 9:
            valor = concatenado * 1000000000
            
        print("Este es el valor: ", valor)

        # Calcular el valor máximo y el valor mínimo
        porcentaje = float(valor) * float(tolerancia)
        valor_maximo = float(valor + porcentaje)
        valor_minimo = float(valor - porcentaje)

    return render_template("resistencias.html", form=clase_resistencias, b1=b1, b2=b2, b3=b3,
                           tolerancia=tolerancia, valor=valor,
                           valor_maximo=valor_maximo, valor_minimo=valor_minimo,
                           color_b1=color_b1, color_b2=color_b2, color_b3=color_b3,
                           color_tolerancia = color_tolerancia)
    
@app.route("/diccionario", methods=["GET", "POST"])
def diccionario():
    ingles = '' #Inicializar palabra en inglés
    espanol = '' #Inicializar palabra en español
    palabra = '' #Inicializar palabra para buscar
    traduccion = '' #Inicializar la palabra traducida
    opciones_idiomas = None
    alumno_clase = forms.UserForm(request.form) #Inicializamos el objeto de la clase UserForm del archivo forms.py
    clase_buscar = forms.BuscarForms(request.form)
    if request.method == 'POST' and alumno_clase.validate():
        # Verificamos si el usuario buscará o registrará
        if "btn1" in request.form:
            ingles = alumno_clase.ingles.data
            espanol = alumno_clase.espanol.data
            
            archivo1 = open('archivo.txt', 'a') #Abrimos el archivo en modo lectura
            palabras = '\n' + espanol.lower() + ':' + ingles.lower()  #Corregimos la construcción de la palabra en español
            archivo1.write(palabras)  #Escribimos la palabras en español e inglés en el archivo
            archivo1.close()  #Cerramos el archivo
            
        elif "btn2" in request.form:
            palabra = clase_buscar.palabra.data
            opciones_idiomas = clase_buscar.opciones_idiomas.data
            
            # Abrimos el archivo en modo de lectura para leer su contenido
            with open('archivo.txt', 'r') as archivo:
                # Leemos línea por línea y creamos un diccionario con las traducciones
                traducciones = {}
                for linea in archivo:
                    # Eliminamos los caracteres especiales como saltos de línea y espacios
                    linea = linea.strip()
                    # Dividimos la línea en español e inglés usando ':' como separador
                    partes = linea.split(':')
                    # Añadimos la palabra en español como clave y la palabra en inglés como valor al diccionario
                    traducciones[partes[0]] = partes[1]
                    # Añadimos también la palabra en inglés como clave y la palabra en español como valor
                    traducciones[partes[1]] = partes[0]

            # Buscamos la palabra en el diccionario invertido
            if palabra.lower() in traducciones:
                traduccion = traducciones[palabra.lower()]
            else:
                traduccion = "Esta palabra no existe en el diccionario"
                
    
    return render_template("diccionario.html", form = alumno_clase, ingles = ingles, espanol = espanol,
                           palabra = palabra, opciones_idiomas = opciones_idiomas, buscar_form = clase_buscar,
                           traduccion = traduccion)

if __name__=="__main__":
    app.run(debug=True)
