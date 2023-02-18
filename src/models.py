from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
        
class Planetas(db.Model):

    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    diametro = db.Column(db.String(250), nullable=False)
    periodo_orbital = db.Column(db.String(250), nullable=False)
    poblacion =  db.Column(db.String(250), nullable=False)
    # favoritos = db.relationship('Favoritos',backref='planetas', lazy=True)
    
    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "diametro": self.diametro,
            "periodo_orbital": self.periodo_orbital,
            "poblacion": self.poblacion,
            # do not serialize the password, its a security breach
        }
        
class Personajes(db.Model):
    
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    altura = db.Column(db.String(250), nullable=False)
    genero =  db.Column(db.String(250), nullable=False)
    peso =  db.Column(db.String(250), nullable=False)
    # favoritos = relationship('Favoritos',backref='personajes', lazy=True)
    
    def __repr__(self):
        return '<Personajes %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "altura": self.altura,
            "genero": self.genero,
            "peso": self.peso,
            # do not serialize the password, its a security breach
        }
        
class Usuario(db.Model):
   
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    fecha_suscripcion =  db.Column(db.String(250), nullable=False)
    apellido =  db.Column(db.String(250), nullable=False)
    email =  db.Column(db.String(250), nullable=False)
    # favoritos = relationship('Favoritos',backref='usuario', lazy=True)
    
    def __repr__(self):
        return '<Usuario %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha_suscripcion": self.fecha_suscripcion,
            "apellido": self.apellido,
            "email": self.email,
            # do not serialize the password, its a security breach
        }