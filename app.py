from crypt import methods
from flask import Flask, request, jsonify, render_template, redirect
from models import db, connect_db, Cupcake
from forms import AddCupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret"

connect_db(app)

@app.route('/')
def home():
    cupcakes = Cupcake.query.all()
    return render_template('index.html', cupcakes=cupcakes)

@app.route('/api/cupcakes', methods=["GET", "POST"])
def get_all_cupcakes():
    """Returns Json for all cupcakes"""
    form = AddCupcake()
    if form.validate_on_submit():
        flavor = form.flavor.data
        size = form.size.data
        rating = form.rating.data
        image = form.image.data
        new_cupacake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
        db.session.add(new_cupacake)
        db.session.commit()
        all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
        json_info = jsonify(cupcakes=all_cupcakes)
        return redirect('/') 
    else:
       return render_template('add_cupcake_form.html', form=form)

# Refactor to split homepage and forms 


@app.route('/api/cupcakes/<int:id>')
def get_a_cupcake(id):
    """Returns a single cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json.get("image", "https://tinyurl.com/demo-cupcake"))
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return(response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def patch_cupcake(id):
        cupcake = Cupcake.query.get_or_404(id)
        cupcake.flavor = request.json.get('flavor', cupcake.flavor)
        cupcake.size = request.json.get('size', cupcake.size)
        cupcake.rating = request.json.get('rating', cupcake.rating)
        cupcake.image = request.json.get('image', cupcake.image)
        db.session.commit()
        return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message=f"cupcake with id:{id} has been deleted")

    

