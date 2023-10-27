from enum import Enum
from fastapi import Depends, FastAPI
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


@app.get("/germany/{heat_option}", response_model=list[schemas.GermanyRecordBase])
def get_hourly_heat_pump_electricity_demand_for_germany(heat_option: HeatOption, db: Session = Depends(get_db)):
    if heat_option == HeatOption.COLDSHANDHW:
        region_hp_electricity_demands = crud.get_records_for_germany_cold(db)
    elif heat_option == HeatOption.COLDSHONLY:
        region_hp_electricity_demands = crud.get_records_for_germany_space_heat_only_cold(db)
    elif heat_option == HeatOption.REFERENCESHANDHW:
        region_hp_electricity_demands = crud.get_records_for_germany_reference(db)
    elif heat_option == HeatOption.REFERENCESHONLY:
        region_hp_electricity_demands = crud.get_records_for_germany_space_heat_only_reference(db)
    elif heat_option == HeatOption.HOTSHANDHW:
        region_hp_electricity_demands = crud.get_records_for_germany_hot(db)
    elif heat_option == HeatOption.HOTSHONLY:
        region_hp_electricity_demands = crud.get_records_for_germany_space_heat_only_hot(db)
    else:
        region_hp_electricity_demands = []
    return region_hp_electricity_demands


@app.get("/nuts-1/{region_code}/{heat_option}", response_model=list[schemas.NUTS1RegionRecordBase])
def get_hourly_heat_pump_electricity_demand_for_single_nuts1_region(region_code: str, heat_option: HeatOption, db: Session = Depends(get_db)):
    if heat_option == HeatOption.COLDSHANDHW:
        region_hp_electricity_demands = crud.get_records_for_single_nuts1_cold(db, region_code=region_code)
    elif heat_option == HeatOption.COLDSHONLY:
        region_hp_electricity_demands = crud.get_records_for_single_nuts1_space_heat_only_cold(db, region_code=region_code)
    elif heat_option == HeatOption.REFERENCESHANDHW:
        region_hp_electricity_demands = crud.get_records_for_single_nuts1_reference(db, region_code=region_code)
    elif heat_option == HeatOption.REFERENCESHONLY:
        region_hp_electricity_demands = crud.get_records_for_single_nuts1_space_heat_only_reference(db, region_code=region_code)
    elif heat_option == HeatOption.HOTSHANDHW:
        region_hp_electricity_demands = crud.get_records_for_single_nuts1_hot(db, region_code=region_code)
    elif heat_option == HeatOption.HOTSHONLY:
        region_hp_electricity_demands = crud.get_records_for_single_nuts1_space_heat_only_hot(db, region_code=region_code)
    else:
        region_hp_electricity_demands = []
    return region_hp_electricity_demands


@app.get("/nuts-3/{region_code}/{heat_option}", response_model=list[schemas.NUTS3RegionRecordBase])
def get_hourly_heat_pump_electricity_demand_for_single_nuts3_region(region_code: str, heat_option: HeatOption, db: Session = Depends(get_db)):
    if heat_option == HeatOption.COLDSHANDHW:
        region_hp_electricity_demands = crud.get_records_for_single_nuts3_cold(db, region_code=region_code)
    elif heat_option == HeatOption.COLDSHONLY:
        region_hp_electricity_demands = crud.get_records_for_single_nuts3_space_heat_only_cold(db, region_code=region_code)
    elif heat_option == HeatOption.REFERENCESHANDHW:
        region_hp_electricity_demands = crud.get_records_for_single_nuts3_reference(db, region_code=region_code)
    elif heat_option == HeatOption.REFERENCESHONLY:
        region_hp_electricity_demands = crud.get_records_for_single_nuts3_space_heat_only_reference(db, region_code=region_code)
    elif heat_option == HeatOption.HOTSHANDHW:
        region_hp_electricity_demands = crud.get_records_for_single_nuts3_hot(db, region_code=region_code)
    elif heat_option == HeatOption.HOTSHONLY:
        region_hp_electricity_demands = crud.get_records_for_single_nuts3_space_heat_only_hot(db, region_code=region_code)
    else:
        region_hp_electricity_demands = []
    return region_hp_electricity_demands