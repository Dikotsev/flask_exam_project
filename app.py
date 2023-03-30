from config import create_app
from flask_migrate import Migrate
from db import db
from sqlalchemy.orm.session import close_all_sessions


app = create_app()

@app.before_first_request
def create_tables():
    db.init_app(app)
    db.create_all()

#@app.after_request
#def return_resp(resp):
#    db.session.commit()
#    return resp
@app.after_request
def close_sessions(response):
    close_all_sessions()
    return response


migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
