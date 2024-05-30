from init import app
from db.connect import db

print("RODANDOOOOOOOOOOOOOOOOOOOOOOOO")
print(__name__)

if __name__ == "app":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)


