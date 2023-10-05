from sqlalchemy.orm import Session

from models import RegionRecordReference

def get_records_for_region_reference(db: Session, region_code: str):
    return db.query(RegionRecordReference).filter(RegionRecordReference.nuts3_code == region_code)