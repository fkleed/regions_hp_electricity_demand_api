from sqlalchemy import Column, String, Numeric

from database import Base

class RegionRecordReference(Base):
    __tablename__ = "nuts3_reference_sh_and_hw"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class RegionRecordCold(Base):
    __tablename__ = "nuts3_cold_sh_and_hw"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class RegionRecordHot(Base):
    __tablename__ = "nuts3_hot_sh_and_hw"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class RegionRecordSHOnlyReference(Base):
    __tablename__ = "nuts3_reference_sh_only"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class RegionRecordSHOnlyCold(Base):
    __tablename__ = "nuts3_cold_sh_only"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class RegionRecordSHOnlyHot(Base):
    __tablename__ = "nuts3_hot_sh_only"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)