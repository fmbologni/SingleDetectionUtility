from interface import implements
from Models.IModelFactory import IModelFactory
from Models.IModelService import IModelService
from Models.RetinaNetDet import RetinaNetDet

class ModelFactory(implements(IModelFactory)):
    def CreateModel(self, model: str) -> IModelService:
        if model == "retinanet":
            return RetinaNetDet.Create(bindServices = RetinaNetDet.BindServices)