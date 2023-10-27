from sqlalchemy import Column, String, Numeric

from database import Base

# For nuts-1 regions
class NUTS1RegionRecordCold(Base):
    __tablename__ = "nuts1_cold_sh_and_hw"

    nuts1_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class NUTS1RegionRecordSHOnlyCold(Base):
    __tablename__ = "nuts1_cold_sh_only"

    nuts1_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)   

class NUTS1RegionRecordReference(Base):
    __tablename__ = "nuts1_reference_sh_and_hw"

    nuts1_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class NUTS1RegionRecordSHOnlyReference(Base):
    __tablename__ = "nuts1_reference_sh_only"

    nuts1_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class NUTS1RegionRecordHot(Base):
    __tablename__ = "nuts1_hot_sh_and_hw"

    nuts1_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)

class NUTS1RegionRecordSHOnlyHot(Base):
    __tablename__ = "nuts1_hot_sh_only"

    nuts1_code = Column(String(5), primary_key=True)
    date_iso = Column(String(20), primary_key=True)
    hourly_electricity_demand = Column(Numeric)


# For nuts-3 regions
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