from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, HiddenField
from wtforms.validators import InputRequired

class ComplainForm(FlaskForm):
    title = StringField("Tittel", validators=[InputRequired()])
    epost = StringField("E-post", validators=[InputRequired()])
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

class RegisterForm(FlaskForm):
    navn = StringField("Navn", validators=[InputRequired()])
    brukernavn = StringField("Brukernavn", validators=[InputRequired()])
    passord = PasswordField("Passord", validators=[InputRequired()])
    submit = SubmitField("Registrer")

class LoginForm(FlaskForm):
    brukernavn = StringField("Brukernavn", validators=[InputRequired()])
    passord = PasswordField("Passord", validators=[InputRequired()])
    submit = SubmitField("Logg inn")

class AnswerForm(FlaskForm):
    svar = StringField("Svar", validators=[InputRequired()])
    submit = SubmitField("Send svar")