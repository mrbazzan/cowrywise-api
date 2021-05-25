from flask import Flask, jsonify
from sqlalchemy.types import String, TypeDecorator
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
import linked_list

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSON_SORT_KEYS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

db = SQLAlchemy(app)


class UUID(TypeDecorator):
    impl = String

    def __init__(self):
        self.impl.length = 16
        TypeDecorator.__init__(self, length=self.impl.length)

    @staticmethod
    def process_bind_param(self, value, dialect=None):
        if value and isinstance(value, uuid.UUID):
            return value.hex
        elif value and not isinstance(value, uuid.UUID):
            raise ValueError('value %s is not a valid uuid.UUID' % value)
        else:
            return None

    @staticmethod
    def process_result_value(self, value, dialect):
        if value:
            return value
        else:
            return None


class Api(db.Model):
    __tablename__ = 'api'
    id = db.Column(UUID(), primary_key=True)
    date = db.Column(db.DateTime)


@app.route('/', methods=['GET'])
def index():

    new_data = Api(
        id=uuid.uuid4(),
        date=datetime.now(),
    )
    db.session.add(new_data)
    db.session.commit()

    all_data = Api.query.all()
    the_list = linked_list.LinkedList()
    for data in all_data:
        the_list.insert_beginning(data)

    return jsonify(the_list.to_dict())


if __name__ == '__main__':
    app.run()  # TODO: use waitress to serve
