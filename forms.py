from wtforms import Form, StringField, RadioField
# Aquí de los validadores importamos el dato obligatorio y el email
from wtforms import validators#, DataRequired, Email

class UserForm(Form):
    x1 = StringField('x1')
    x2 = StringField('x2')
    y1 = StringField('y1')
    y2 = StringField('y2')
    
    # Palabras en inglés
    ingles = StringField('ingles',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 2, max = 50, message = 'Ingresa una palabra válida')
    ])
    
    #Palabras en español
    espanol = StringField('espanol',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 2, max = 50, message = 'Ingresa una palabra válida')
    ])
    
class BuscarForms(Form):
    #Palabra buscada
    palabra = StringField('palabra',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 2, max = 50, message = 'Ingresa una palabra válida')
    ])
    
    #Opciones para búsqueda
    opciones_idiomas = RadioField('opciones_idiomas', choices=[('ingles', 'Inglés'), ('espanol', 'Español')],
        validators=[validators.DataRequired(message= 'Debes seleccionar al menos un idioma')]
    )
    