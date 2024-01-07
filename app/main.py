from fastapi import FastAPI, Depends, HTTPException
from . import models, schemas
from sqlalchemy.orm import Session
from .dependencies import get_db

app = FastAPI()


@app.get("/status")
def read_status():
    return {"status": "Service is up and running"}


@app.post("/packages/", response_model=schemas.Package)
def create_package(package: schemas.PackageCreate, db: Session = Depends(get_db)):
    db_package = models.Package(**package.dict(), status="Created")
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package


@app.get("/packages/{package_id}", response_model=schemas.Package)
def get_package(package_id: str, db: Session = Depends(get_db)):
    db_package = (
        db.query(models.Package).filter(models.Package.id == package_id).first()
    )
    if db_package is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return db_package
