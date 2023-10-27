from sqlalchemy.orm import Session

from models import *

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