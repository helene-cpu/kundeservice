from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired

class ComplainForm(FlaskForm):
    title = StringField("Tittel", validators=[InputRequired()])
    category = SelectField("Hva gjelder saken?", choices= [
        ("---", ""),
        ("feil_vare", "Motatt feil vare"),
        ("forsinket", "Forsinket levering"),
        ("skadet", "Skadet produkt"),
        ("ikke_mottatt", "Ikke mottatt produkt"),
        ("betaling", "Betalingsproblemer"),
        ("annet", "Annet")
        ], validators=[InputRequired()]
    )
    ordernumber = StringField("Ordrenummer", validators=[InputRequired()])
    description = StringField("Beskrivelse", validators=[InputRequired()])
    submit = SubmitField("Send inn")