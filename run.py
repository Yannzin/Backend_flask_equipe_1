

#if __name__ == "__main__":
##    app.run()


# Configurações para WINDOWS

from waitress import serve
from app import app
from app import app, db

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
