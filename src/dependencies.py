"""
Module: dependencies.py
Author: vgolubev

Module describe injectable dependencies in project.  
"""

from src.database import Session


def get_db_session():
    """Dependency that create database session with pool of connections"""
    
    session = Session()
    try:
        yield session
    finally:
        session.close()