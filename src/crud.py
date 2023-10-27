from sqlalchemy.orm import Session

from models import *

# For Germany
# For the cold temperature series
def get_records_for_germany_cold(db: Session):
    return db.query(GermanyRecordCold)

def get_records_for_germany_space_heat_only_cold(db: Session):
    return db.query(GermanyRecordSHOnlyCold)

# For the reference temperature series
def get_records_for_germany_reference(db: Session):
    return db.query(GermanyRecordReference)

def get_records_for_germany_space_heat_only_reference(db: Session):
    return db.query(GermanyRecordSHOnlyReference)

# For the hot temperature series
def get_records_for_germany_hot(db: Session):
    return db.query(GermanyRecordHot)

def get_records_for_germany_space_heat_only_hot(db: Session):
    return db.query(GermanyRecordSHOnlyHot)


# For single nuts-1 region
# For the cold temperature series
def get_records_for_single_nuts1_cold(db: Session, region_code: str):
    return db.query(NUTS1RegionRecordCold).filter(NUTS1RegionRecordCold.nuts1_code == region_code)

def get_records_for_single_nuts1_space_heat_only_cold(db: Session, region_code: str):
    return db.query(NUTS1RegionRecordSHOnlyCold).filter(NUTS1RegionRecordSHOnlyCold.nuts1_code == region_code)

# For the reference temperature series
def get_records_for_single_nuts1_reference(db: Session, region_code: str):
    return db.query(NUTS1RegionRecordReference).filter(NUTS1RegionRecordReference.nuts1_code == region_code)

def get_records_for_single_nuts1_space_heat_only_reference(db: Session, region_code: str):
    return db.query(NUTS1RegionRecordSHOnlyReference).filter(NUTS1RegionRecordSHOnlyReference.nuts1_code == region_code)

# For the hot temperature series
def get_records_for_single_nuts1_hot(db: Session, region_code: str):
    return db.query(NUTS1RegionRecordHot).filter(NUTS1RegionRecordHot.nuts1_code == region_code)

def get_records_for_single_nuts1_space_heat_only_hot(db: Session, region_code: str):
    return db.query(NUTS1RegionRecordSHOnlyHot).filter(NUTS1RegionRecordSHOnlyHot.nuts1_code == region_code)


# For single nuts-3 region
# For the cold temperature series
def get_records_for_single_nuts3_cold(db: Session, region_code: str):
    return db.query(NUTS3RegionRecordCold).filter(NUTS3RegionRecordCold.nuts3_code == region_code)

def get_records_for_single_nuts3_space_heat_only_cold(db: Session, region_code: str):
    return db.query(NUTS3RegionRecordSHOnlyCold).filter(NUTS3RegionRecordSHOnlyCold.nuts3_code == region_code)

# For the reference temperature series
def get_records_for_single_nuts3_reference(db: Session, region_code: str):
    return db.query(NUTS3RegionRecordReference).filter(NUTS3RegionRecordReference.nuts3_code == region_code)

def get_records_for_single_nuts3_space_heat_only_reference(db: Session, region_code: str):
    return db.query(NUTS3RegionRecordSHOnlyReference).filter(NUTS3RegionRecordSHOnlyReference.nuts3_code == region_code)

# For the hot temperature series
def get_records_for_single_nuts3_hot(db: Session, region_code: str):
    return db.query(NUTS3RegionRecordHot).filter(NUTS3RegionRecordHot.nuts3_code == region_code)

def get_records_for_single_nuts3_space_heat_only_hot(db: Session, region_code: str):
    return db.query(NUTS3RegionRecordSHOnlyHot).filter(NUTS3RegionRecordSHOnlyHot.nuts3_code == region_code)