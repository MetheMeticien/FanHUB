from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Features.social_media.notifications.schema import NotificationCreate, NotificationOut
import Features.social_media.notifications.crud as crud
from Utils.db_dependencies import get_db
from typing import List

router = APIRouter()

@router.post("/notifications", response_model=NotificationOut)
def create_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    return crud.create_notification(db=db, notification=notification)

@router.get("/notifications/{user_id}", response_model=List[NotificationOut])
def get_notifications_by_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_notifications_by_user(db=db, user_id=user_id)

@router.patch("/notifications/{notification_id}", response_model=NotificationOut)
def mark_notification_as_read(notification_id: int, db: Session = Depends(get_db)):
    db_notification = crud.mark_notification_as_read(db=db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification
