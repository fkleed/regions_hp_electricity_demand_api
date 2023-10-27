from sqlalchemy import Column, String, Numeric

from database import Base

class NUTS3RegionRecordCold(Base):
    __tablename__ = "nuts3_cold_sh_and_hw"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class NUTS3RegionRecordSHOnlyCold(Base):
    __tablename__ = "nuts3_cold_sh_only"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)   

class NUTS3RegionRecordReference(Base):
    __tablename__ = "nuts3_reference_sh_and_hw"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class NUTS3RegionRecordSHOnlyReference(Base):
    __tablename__ = "nuts3_reference_sh_only"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class NUTS3RegionRecordHot(Base):
    __tablename__ = "nuts3_hot_sh_and_hw"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class NUTS3RegionRecordSHOnlyHot(Base):
    __tablename__ = "nuts3_hot_sh_only"

    nuts3_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)