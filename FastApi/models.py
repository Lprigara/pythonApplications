from pydantic import BaseModel

class Iris(BaseModel):
    sepal_width: float
    sepal_length: float
    petal_width: float
    petal_length: float
    species: str
    
class IrisPredictable(BaseModel):
    sepal_width: float
    sepal_length: float
    petal_width:float
    petal_length:float