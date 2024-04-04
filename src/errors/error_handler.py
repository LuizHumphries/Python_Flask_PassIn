from src.http_types.http_response import HttpResponse
from .error_types.http_conflict import HttpConflictError
from .error_types.http_not_found import HttpNotFoundError

def handle_errors(error: Exception) ->HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpConflictError)):
        return HttpResponse(
            body={
                "errors": [{"title": error.name, "details": error.message}]
            },
            status_code= error.status_code
        )
    return HttpResponse(
        body={
            "errors": [{
                "title": "Error",
                "details": str(error),                
            }]
        }
    )