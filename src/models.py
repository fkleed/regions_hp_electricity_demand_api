from sqlalchemy import Column, String, Numeric

from database import Base

class RegionRecordReference(Base):
    __tablename__ = "reference"

    nuts3_code = Column(String(5), primary_key=True)
    time = Column(String(11), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class RegionRecordCold(Base):
    __tablename__ = "cold"

    nuts3_code = Column(String(5), primary_key=True)
    time = Column(String(11), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class RegionRecordHot(Base):
    __tablename__ = "hot"

    nuts3_code = Column(String(5), primary_key=True)
    time = Column(String(11), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class RegionRecordSHOnlyReference(Base):
    __tablename__ = "space_heat_only_reference"

    nuts3_code = Column(String(5), primary_key=True)
    time = Column(String(11), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class RegionRecordSHOnlyCold(Base):
    __tablename__ = "space_heat_only_cold"

    nuts3_code = Column(String(5), primary_key=True)
    time = Column(String(11), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class RegionRecordSHOnlyHot(Base):
    __tablename__ = "space_heat_only_hot"

    nuts3_code = Column(String(5), primary_key=True)
    time = Column(String(11), primary_key=True)
    hourly_electricity_demand = Column(Numeric)