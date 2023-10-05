from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API of the regional electricity demand for the spread of 6 million heat pumps in Germany in 2030"
    )

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/regions/{region_code}", response_model=list[schemas.RegionRecordBase])
def read_region_hp_electricity_demands(region_code: str, db: Session = Depends(get_db)):
    region_hp_electricity_demands = crud.get_records_for_region_reference(db, region_code=region_code)
    return region_hp_electricity_demands
