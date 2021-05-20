"""
Module: endpoints.py
Author: vgolubev

Module describe API Endpoints.  
"""


from fastapi import APIRouter, Depends, HTTPException, status
from src.dependencies import get_db_session
from src import service
from src import data_manager
from src import schemas

router = APIRouter()

@router.get("/",
	response_model=schemas.HelloMessage,
	responses={
		status.HTTP_404_NOT_FOUND: {
		"content": {"application/json": {}},
		"description": "Could not found any users"
		}
	}
)
async def root(session = Depends(get_db_session)):
	"""Endpoint return first user"""
	
	user = data_manager.first_user(session)
	if not user:
		raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not found any users",
        )
	message: str = service.get_hello_message_for_user(user)
	return schemas.HelloMessage(message=message)
