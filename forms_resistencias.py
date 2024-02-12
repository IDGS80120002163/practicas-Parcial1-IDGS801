from wtforms import Form, SelectField, RadioField

class ResistenciasForms(Form):
    opciones_colores = [(0, 'Negro'), (1, 'Café'), (2, 'Rojo'), (3, 'Naranja'), (4, 'Amarillo'),
                        (5, 'Verde'), (6, 'Azul'), (7, 'Violeta'), (8, 'Gris'), (9, 'Blanco')]  # Opciones para los selectores
    opciones_tolerancia = [(.05, 'Oro'), (.10, 'Plata')]  # Opciones para el radio button

    b1 = SelectField("b1", choices=opciones_colores)
    b2 = SelectField("b2", choices=opciones_colores)
    b3 = SelectField("b3", choices=opciones_colores)
    tolerancia = RadioField("tolerancia", choices=opciones_tolerancia)
    