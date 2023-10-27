from enum import Enum
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API for the regional electricity demand in kWh for the spread of 6 million heat pumps in Germany in 2030"
    )

class HeatOption(Enum):
    COLDSHANDHW = "cold_space_heat_and_hot_water"
    COLDSHONLY = "cold_space_heat_only"
    REFERENCESHANDHW = "reference_space_heat_and_hot_water"
    REFERENCESHONLY = "reference_space_heat_only"
    HOTSHANDHW = "hot_space_heat_and_hot_water"
    HOTSHONLY = "hot_space_heat_only"


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/nuts-3/{region_code}/{heat_option}", response_model=list[schemas.NUTS3RegionRecordBase])
def read_region_hp_electricity_demands(region_code: str, heat_option: HeatOption, db: Session = Depends(get_db)):
    if heat_option == HeatOption.COLDSHANDHW:
        region_hp_electricity_demands = crud.get_records_for_nuts3_cold(db, region_code=region_code)
    elif heat_option == HeatOption.COLDSHONLY:
        region_hp_electricity_demands = crud.get_records_for_nuts3_space_heat_only_cold(db, region_code=region_code)
    elif heat_option == HeatOption.REFERENCESHANDHW:
        region_hp_electricity_demands = crud.get_records_for_nuts3_reference(db, region_code=region_code)
    elif heat_option == HeatOption.REFERENCESHONLY:
        region_hp_electricity_demands = crud.get_records_for_nuts3_space_heat_only_reference(db, region_code=region_code)
    elif heat_option == HeatOption.HOTSHANDHW:
        region_hp_electricity_demands = crud.get_records_for_nuts3_hot(db, region_code=region_code)
    elif heat_option == HeatOption.HOTSHONLY:
        region_hp_electricity_demands = crud.get_records_for_nuts3_space_heat_only_hot(db, region_code=region_code)
    else:
        region_hp_electricity_demands = []
    return region_hp_electricity_demands