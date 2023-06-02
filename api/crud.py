from sqlite3 import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session
# from api.models import AudienceModel,AudienceValuesModel
from api import main,database
# from api.database import sessionLocal
from api import schema,models

def get_audiences(db:Session):
    return db.query(models.AudienceModel).all()

def create_audience(audience:schema.AudienceSchema,db:Session):
    try:
        new_aud = models.AudienceModel(id = audience.id ,
                                country=audience.country,
                                name=audience.name,
                                label=audience.label,
                                description = audience.description)
    except IntegrityError as e:
        raise HTTPException(status_code=500,detail="Audience Details Already added")
    db.add(new_aud)
    db.commit()
    return {"message":"Audience Created Successfully"}

def get_audience_count(db:Session):
    return db.query(models.AudienceModel).count()
