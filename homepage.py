from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastros.db'  # Caminho do banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/cadastros")
def cadastros():
    return render_template("cadastros.html")

@app.route("/novocadastro")
def novocadastro():
    return render_template("novocadastro.html")

class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.String(50), nullable=False)
    owner_name = db.Column(db.String(100), nullable=False)
    phone1 = db.Column(db.String(50), nullable=False)
    phone2 = db.Column(db.String(50), nullable=True)
    current_date = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Cadastro {self.pet_name}>'


if __name__ == "__main__":
    app.run(debug=True)