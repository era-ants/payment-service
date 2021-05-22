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


@router.get("/{client_id}",
            response_model=schemas.Money,
            responses={
                status.HTTP_404_NOT_FOUND: {
                    "content": {"application/json": {}},
                    "description": "Could not found that account"
                }
            }
            )
def get_money_account(client_id: int, session=Depends(get_db_session)):
    """Endpoint return first user"""

    account = data_manager.get_money(session, client_id)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not found that accounts",
        )
    return account


@router.post("/add",
             response_model=schemas.Payment,
             responses={
                 status.HTTP_404_NOT_FOUND: {
                     "content": {"application/json": {}},
                     "description": "Could not found that account"
                 }
             }
             )
def replenishment(payment: schemas.Payment, session=Depends(get_db_session)):
    """Endpoint return first user"""

    account = data_manager.replenishment(session, payment)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return account


@router.post("/substruct",
             response_model=schemas.Payment,
             responses={
                 status.HTTP_404_NOT_FOUND: {
                     "content": {"application/json": {}},
                     "description": "Could not found that account"
                 }
             }
             )
def write_off(payment: schemas.Payment, session=Depends(get_db_session)):
    """Endpoint return first user"""

    account = data_manager.write_off(session, payment)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return account


@router.post("/",
             response_model=schemas.Money,
             responses={
                 status.HTTP_400_BAD_REQUEST: {
                     "content": {"application/json": {}},
                     "description": "Account already exist"
                 }
             }
             )
def write_off(client_id: int, session=Depends(get_db_session)):
    """Endpoint return first user"""

    account = data_manager.create_account(session, client_id)
    if not account:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account already exist"
        )
    return account
