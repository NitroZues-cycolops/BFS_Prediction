from pydantic import BaseModel, Field

class predict_response(BaseModel):
    prediction:float = Field(...,description= "The predicted BFS purchase of a customer", example="13074.3746")