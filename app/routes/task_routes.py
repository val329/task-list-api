from flask import Blueprint, abort, make_response, request, Response
from app import db
from app.models.task import Task
from app.routes.route_utilities import create_model, validate_model
from datetime import datetime

bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp.get("")
def get_all_tasks():

    query = db.select(Task)

    title_param = request.args.get("title")
    if title_param:
        query = query.where(Task.title.ilike(f"%{title_param}"))

    sort_param = request.args.get("sort")
    if sort_param == "asc":
        query = query.order_by(Task.title.asc())
    elif sort_param == "desc":
        query = query.order_by(Task.title.desc())

    tasks = db.session.scalars(query)

    response = []
    for task in tasks:
        response.append(task.to_dict())
    return response


@bp.get("/<task_id>")
def get_one_task(task_id):
    task = validate_model(Task, task_id)
    return task.to_dict()


@bp.post("")
def create_task():
    request_body = request.get_json()
    task = create_model(Task, request_body)

    db.session.add(task)
    db.session.commit()

    return task.to_dict(), 201


@bp.put("/<task_id>")
def edit_task(task_id):

    task = validate_model(Task, task_id)
    request_body = request.get_json()

    task.title = request_body.get("title")
    task.description = request_body.get("description")
    task.completed_at = request_body.get("completed_at")
    task.is_complete = request_body.get("is_complete")
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.delete("/<task_id>")
def delete_task(task_id):

    task = validate_model(Task, task_id)
    db.session.delete(task)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.patch("/<task_id>/mark_complete")
def mark_complete(task_id):
    task = validate_model(Task, task_id)
    task.completed_at = datetime.now()
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.patch("/<task_id>/mark_incomplete")
def mark_incomplete(task_id):
    task = validate_model(Task, task_id)
    task.completed_at = None
    db.session.commit()

    return Response(status=204, mimetype="application/json")
