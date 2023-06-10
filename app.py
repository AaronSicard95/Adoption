from flask import Flask, render_template, redirect
from models import *
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adoption"
app.config['SECRET_KEY'] = 'WOAHLMAO'

connect_db(app)
with app.app_context():
    db.create_all()

@app.route('/')
def root():
    animals = Pet.query.all()
    return render_template('home.html', animals = animals)

@app.route('/add', methods=['GET', 'POST'])
def addPet():
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes,
            available=available
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('addPet.html', form=form)

@app.route('/<int:petid>', methods=['GET', 'POST'])
def editPet(petid):
    pet = Pet.query.get_or_404(petid)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet.name=name
        pet.species=species
        pet.photo_url=photo_url
        pet.age=age
        pet.notes=notes
        pet.available=available
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('petView.html', pet=pet,form=form)
