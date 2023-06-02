from fastapi import Depends, FastAPI
from api import crud,schema,models

from api.database import Base,engine,sessionLocal
from sqlalchemy.orm import Session


app = FastAPI()



def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
Base.metadata.create_all(engine)
@app.get("/health_check")
def health_check():
    return {"status":"ok"}

@app.get("/audiences")
def get_all_audiences(db:Session=Depends(get_db)):
    users = crud.get_audiences(db)
    return users

@app.post("/create_audience",status_code=200)
def create_audience(audience:schema.AudienceSchema,db:Session=Depends(get_db)):
    db_user=crud.create_audience(audience,db)
    return db_user

@app.get("/audience_count",status_code=200)
def get_audience_count(db:Session=Depends(get_db)):
    count=crud.get_audience_count(db)
    return {"Audience Count":count}