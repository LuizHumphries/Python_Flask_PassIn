from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.check_in_handler import CheckInHandler
from src.errors.error_handler import handle_errors

check_in_route_bp = Blueprint("check_in_route", __name__)

@check_in_route_bp.route("/attendees/<atendee_id>/check-in", methods=["POST"])
def create_check_in(atendee_id):
    try:
        http_request = HttpRequest(param={"attendee_id": atendee_id})
        check_in_handler = CheckInHandler()
        http_response = check_in_handler.register(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code