from typing import Any
from ninja import NinjaAPI

from django.http import HttpRequest,HttpResponse
from backend.controllers import (project_router)

class Api(NinjaAPI):
    """
    API INHERITED TYPES FROM DJANGO
    """
    def create_response(
        self,request:HttpRequest, data: Any, *,
        status:int = None,temporal_response:HttpResponse=None
    )->HttpResponse:
        response = super().create_response(request,data,status=status,temporal_response=temporal_response)
        return response

api = Api()
api.add_router("/",project_router)