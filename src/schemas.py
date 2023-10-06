from pydantic import BaseModel

class RegionRecordBase(BaseModel):
    nuts3_code: str
    time: str
    hourly_electricity_demand: float

    class Config:
        from_attributes = True