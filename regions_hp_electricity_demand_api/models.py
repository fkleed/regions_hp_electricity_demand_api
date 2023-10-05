from sqlalchemy import Column, String, Numeric

from database import Base

class RegionRecordReference(Base):
    __tablename__ = "reference"

    nuts3_code = Column(String(5), primary_key=True)
    time = Column(String(11), primary_key=True)
    hourly_electricity_demand = Column(Numeric)