from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .database import get_db
from .models import User, Camera, Log
from .schemas import UserCreate, UserOut, CameraCreate, CameraOut, LogOut
from .auth import get_current_user, get_password_hash, verify_password, create_access_token

router = APIRouter()

@router.post('/register', response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, password=hashed_password, role=user.role, branch=user.branch)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/login')
def login(form_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post('/camera', response_model=CameraOut)
def add_camera(camera: CameraCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    new_camera = Camera(ip=camera.ip, location=camera.location, source_name=camera.source_name, added_by=current_user.id)
    db.add(new_camera)
    db.commit()
    db.refresh(new_camera)
    return new_camera

@router.get('/cameras', response_model=list[CameraOut])
def get_cameras(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    cameras = db.query(Camera).all()
    return cameras
