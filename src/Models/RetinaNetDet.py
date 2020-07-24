from interface import implements
from Preprocessing.RetinaNet.Interfaces.IGenerateTrainingFilesService import IGenerateTrainingFilesService
from Preprocessing.RetinaNet.Services.GenerateTrainingFilesService import GenerateTrainingFilesService
from Preprocessing.RetinaNet.Interfaces.ISeparateImagesFromAnnotationsService import ISeparateImagesFromAnnotationsService
from Preprocessing.RetinaNet.Services.SeparateImagesFromAnnotationsService import SeparteImagesFromAnnotationsService
from injector import Binder, Injector, inject
from Models.IModelService import IModelService
from typing import Dict

class RetinaNetDet(implements(IModelService)):
    @inject
    def __init__(self, generateTrainingFilesService: IGenerateTrainingFilesService,
                       separateImagesFromAnnotationsService: ISeparateImagesFromAnnotationsService):
        self.generateTrainingFilesService = generateTrainingFilesService
        self.separateImagesFromAnnotationsService = separateImagesFromAnnotationsService

    @staticmethod
    def Create(bindServices):
        inject: Injector = Injector(bindServices)
        return inject.get(RetinaNetDet)

    def Preprocess(self, config: Dict):
        self.separateImagesFromAnnotationsService.SeparateImagesFromAnnotations(imagesFolder = config["imagesFolder"], 
                                                                                annotationsFolder = config["annotationsFolder"])
        self.generateTrainingFilesService.GenerateTrainingFiles(imagesFolder = config["imagesFolder"],
                                                                mainFolder = config["mainFolder"],
                                                                valSize = config["valSize"])
    
    def Train(self):
        print("training retinanet")
    
    def Predict(self):
        print("testing retinanet")
    
    def __BindServices(self, binder: Binder):
        binder.bind(IGenerateTrainingFilesService, to=GenerateTrainingFilesService())
        binder.bind(ISeparateImagesFromAnnotationsService, to=SeparteImagesFromAnnotationsService())
