from views import *
from app import db

db.create_all()







if __name__ == '__main__':
    app.run(debug=True)
