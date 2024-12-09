from ninja import Router
from typing import List,Any
from django.http import HttpRequest

from backend.models import Project
from backend.schemas import ProjectSchema
router = Router()

@router.get("/projects",response=List[ProjectSchema],tags=["Projects"])
def projects(_)->List[ProjectSchema]:
    return Project.objects.all()