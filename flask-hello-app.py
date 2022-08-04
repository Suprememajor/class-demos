from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://suprememajor:12345678@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Person(db.Model):
	__tablename__ = 'persons'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), nullable=False)
	
	def __repr__(self): #For debugging purposes
		return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all() # Better to do this using migrations
person = Person(name='John')
db.session.add(person)
person = Person(name='Mary')
db.session.add(person)
db.session.commit()


@app.route('/')
def index():
	value = ''
	persons = Person.query.all()
	for person in persons:
		value += 'Hello {} \n'.format(person.name)
	return value
