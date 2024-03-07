from fastapi import FastAPI, Depends, HTTPException, status
from . import auth, models, schemas
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

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: schemas.TokenRequestForm = Depends()):
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user