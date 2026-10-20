from flask import abort, make_response
from ..db import db


def create_model():
    pass


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        response = {"message": f"{cls.__name__} {model_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"ssage": f"{cls.__name__} {model_id} not found"}
        abort(make_response(response, 404))

    return model
