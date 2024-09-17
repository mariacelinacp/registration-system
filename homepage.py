from flask import Flask, render_template, request, redirect, url_for, flash
from database import db
from models import Cadastro

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@localhost:5432/registration_system'  # Caminho do banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '3SA41F56WE4W561VE6AS4T3464R6WQ1SDF12'    

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/cadastros", methods=['GET', 'POST'])
def cadastros():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query:
            # Busca no banco de dados usando o input
            resultados = Cadastro.query.filter(Cadastro.pet_name.ilike(f'%{search_query}%')).all()
            if not resultados:
                flash('Nenhum resultado encontrado.', category='info')
            return render_template("resultados.html", resultados=resultados, search_query=search_query)
    return render_template("cadastros.html")


@app.route("/novocadastro", methods=['GET', 'POST'])
def novocadastro():
    if request.method == 'POST':
        info_pet_name = request.form.get('pet_name')
        info_age = request.form.get('age')
        info_weight = request.form.get('weight')
        info_owner_name = request.form.get('owner_name')
        info_phone = request.form.get('phone')
        info_email = request.form.get('email')
        info_current_date = request.form.get('current_date')

        if not info_pet_name or not info_age or not info_weight or not info_owner_name or not info_phone or not info_current_date:
            flash('Por favor, preencha todos os campos obrigatórios.', category='error')
        else:
            new_info = Cadastro(pet_name=info_pet_name, age=info_age, weight=info_weight, owner_name=info_owner_name, phone=info_phone, email=info_email, current_date=info_current_date)
            db.session.add(new_info)
            db.session.commit()
            flash('Configuração salva!', category='success')

    return render_template("novocadastro.html")


if __name__ == "__main__":
    app.run(debug=True)