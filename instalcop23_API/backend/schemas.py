from typing import List
from ninja import ModelSchema
from backend.models import Project

class ProjectSchema(ModelSchema):
    class Config:
        model= Project
        model_fields = "__all__"