from database import db

class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.String(50), nullable=False)
    owner_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    current_date = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Cadastro {self.pet_name}>'