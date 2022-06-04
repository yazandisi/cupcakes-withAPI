from email.mime import image
from models import db, connect_db, Cupcake
from app import app

db.drop_all()
db.create_all()

cupcakes = [
    Cupcake(flavor='Coco', size='large', rating=4.5, image=""),
    Cupcake(flavor='Vanila', size='Small', rating=2.3, image=""),
    Cupcake(flavor='Chery', size='XLarge', rating=1.3),
    Cupcake(flavor='Dog', size='SLarge', rating=5.3),
    
]

db.session.add_all(cupcakes)
db.session.commit()