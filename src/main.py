from enum import Enum
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API of the hourly electricity demand in kWh of the NUTS-3 regions for the spread of 6 million heat pumps in Germany in 2030"
    )

class HeatOption(Enum):
    REFERENCE = "reference"
    COLD = "cold"
    HOT = "hot"
    REFERENCESHONLY = "reference_space_heat_only"
    COLDSHONLY = "cold_space_heat_only"
    HOTSHONLY = "hot_space_heat_only"


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/regions/{region_code}/{heat_option}", response_model=list[schemas.RegionRecordBase])
def read_region_hp_electricity_demands(region_code: str, heat_option: HeatOption, db: Session = Depends(get_db)):
    if heat_option == HeatOption.REFERENCE:
        region_hp_electricity_demands = crud.get_records_for_region_reference(db, region_code=region_code)
    elif heat_option == HeatOption.COLD:
        region_hp_electricity_demands = crud.get_records_for_region_cold(db, region_code=region_code)
    elif heat_option == HeatOption.HOT:
        region_hp_electricity_demands = crud.get_records_for_region_hot(db, region_code=region_code)
    elif heat_option == HeatOption.REFERENCESHONLY:
        region_hp_electricity_demands = crud.get_records_for_region_space_heat_only_reference(db, region_code=region_code)
    elif heat_option == HeatOption.COLDSHONLY:
        region_hp_electricity_demands = crud.get_records_for_region_space_heat_only_cold(db, region_code=region_code)
    elif heat_option == HeatOption.HOTSHONLY:
        region_hp_electricity_demands = crud.get_records_for_region_space_heat_only_hot(db, region_code=region_code)
    else:
        region_hp_electricity_demands = []
    return region_hp_electricity_demands