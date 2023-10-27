from pydantic import BaseModel

class GermanyRecordBase(BaseModel):
    date_iso: str
    hourly_electricity_demand: float

    class Config:
        from_attributes = True

class NUTS1RegionRecordBase(BaseModel):
    nuts1_code: str
    date_iso: str
    hourly_electricity_demand: float

    class Config:
        from_attributes = True

class NUTS3RegionRecordBase(BaseModel):
    nuts3_code: str
    date_iso: str
    hourly_electricity_demand: float

    class Config:
        from_attributes = True