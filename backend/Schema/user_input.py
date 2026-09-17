from pydantic import BaseModel, Field, field_validator ,computed_field
from typing import Literal, Annotated, Optional

class UserInput(BaseModel):
    Gender: Annotated[Literal['F','M'],Field(default=None,description="Gender can be F, M, O only")]
    Age: Annotated[(int,Field(...,description='Age of the user'))]
    Occupation: Annotated[(Optional[str],Field(default=None,description='Pimary occupation of person',examples=['Architect']))]
    City_Category: Annotated[(str,Field(...,description='the city were store is present '))]
    Stay_In_Current_City_Years: Annotated[(int,Field(...,description='years stayed in the current city'))]
    Marital_Status: Annotated[(int,Field(...,description='0 means single, 1 means married'))]
    Product_Category_1:Annotated[(int,Field(...,description='number of product purchased of 1st category'))]
    Product_Category_2:Annotated[(int,Field(...,description='number of product purchased of 2nd category'))]
    Product_Category_3:Annotated[(int,Field(...,description='number of product purchased of 3rd category'))]

    
    @computed_field 
    @property
    def age_bin(self) -> str:
        if self.Age < 17 :
            Age = "0-17"
            return Age
        elif self.Age <25:
            Age = "18-25"
            return Age
        elif self.Age <35:
            Age = "26-35"
            return Age
        elif self.Age <45:
            Age = "36-45"
            return Age
        elif self.Age <55:
            Age = "46-55"
            return Age
        else:
            Age = "55+"
            return Age
