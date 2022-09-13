import os

from marshmallow.exceptions import ValidationError  # type: ignore
from flask import Flask, request, abort

from project.exceptions import FailRequest
from project.schema import Requests, RequestsSchema
from project.classes import Search
from settings import DATA_DIR

app = Flask(__name__)


@app.route("/perform_query/", methods=['GET', 'POST'])
def perform_query():  # type: ignore
    try:
        if request.method == 'GET':
            requests: Requests = RequestsSchema().load(request.args)
        else:                                                               # Получаем параметры запроса
            requests: Requests = RequestsSchema().load(request.json)
        if not os.path.exists(DATA_DIR):
            raise FailRequest

        with open(DATA_DIR, 'r') as file:           # getattr - возвращает значение атрибута объекта
            cmd1_result = getattr(Search, requests.cmd1)(file, requests.value1)
            cmd2_result = getattr(Search, requests.cmd2)(cmd1_result, requests.value2)

    except (ValueError, FileNotFoundError, TypeError, IndexError, ValidationError) as e:
        abort(400, e)

    return app.response_class(cmd2_result, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
