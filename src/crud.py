from sqlalchemy.orm import Session

from models import RegionRecordReference, RegionRecordCold, RegionRecordHot, RegionRecordSHOnlyReference, RegionRecordSHOnlyCold, RegionRecordSHOnlyHot

# For space heating and hot water together
def get_records_for_region_reference(db: Session, region_code: str):
    return db.query(RegionRecordReference).filter(RegionRecordReference.nuts3_code == region_code)

def get_records_for_region_cold(db: Session, region_code: str):
    return db.query(RegionRecordCold).filter(RegionRecordCold.nuts3_code == region_code)

def get_records_for_region_hot(db: Session, region_code: str):
    return db.query(RegionRecordHot).filter(RegionRecordHot.nuts3_code == region_code)


# For space heating only
def get_records_for_region_space_heat_only_reference(db: Session, region_code: str):
    return db.query(RegionRecordSHOnlyReference).filter(RegionRecordSHOnlyReference.nuts3_code == region_code)

def get_records_for_region_space_heat_only_cold(db: Session, region_code: str):
    return db.query(RegionRecordSHOnlyCold).filter(RegionRecordSHOnlyCold.nuts3_code == region_code)


def get_records_for_region_space_heat_only_hot(db: Session, region_code: str):
    return db.query(RegionRecordSHOnlyHot).filter(RegionRecordSHOnlyHot.nuts3_code == region_code)