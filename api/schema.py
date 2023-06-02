from typing import List
from pydantic import BaseModel, Field


class AudienceSchema(BaseModel):
    id:int
    country:str=Field(...,min_length=2,max_length=10,description="Audience Country Code")
    name:str=Field(...,description="Audience Name")
    label:str=Field(...,description="Audience Label")
    description:str=Field(...,description="Audience Description")
    class Config:
        orm_mode=True
    
class AudienceValuesSchema(BaseModel):
    audience_value:str      
    audience_label:str      
    audience_description:str    

class AudienceListSchema(BaseModel):
    audience_list: List[AudienceValuesSchema]