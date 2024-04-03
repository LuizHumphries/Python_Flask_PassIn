from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest

event_route_bp = Blueprint("event_rout", __name__)

@event_route_bp.route("/events", methods=["POST"])
def create_event():
    http_request = HttpRequest(body=request.json)
    
    return jsonify({"message": "Worked"}), 200