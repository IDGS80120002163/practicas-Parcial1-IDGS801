from wtforms import Form, StringField, TelField, EmailField, IntegerField
# Aquí de los validadores importamos el dato obligatorio y el email
from wtforms.validators import DataRequired, Email

class UserForm(Form):
    x1 = StringField('x1')
    x2 = StringField('x2')
    y1 = StringField('y1')
    y2 = StringField('y2')