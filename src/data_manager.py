from sqlalchemy.exc import IntegrityError
from src import models
from src import schemas


def replenishment(session, payment: schemas.Payment):
    """"Add money to account"""

    money = session.query(models.Money).filter(models.Money.c.id == payment.client_id).first()
    if money:
        money.update({"digits": models.Money.c.digits + payment.digits})
        session.commit()
        return money
    return None


def write_off(session, payment: schemas.Payment):
    """Substruct money from account"""

    money = session.query(models.Money).filter(models.Money.c.id == payment.client_id).first()

    if payment.digits > money.digits:
        return None
    else:
        session.query(models.Money).filter(models.Money.c.id == payment.client_id). \
            update({"digits": models.Money.digits - payment.digits})
        session.commit()
        return money.digits


def create_account(session, client_id):
    account = models.Money(client_id=client_id, digits=0, currency="Руб.")
    session.add(account)
    try:
        session.commit()
    except IntegrityError:
        return None
    return schemas.Money.from_orm(account)


def get_money(session, client_id: int):
    """Get money from account with Client ID"""
    for row in session.query(models.Money).filter(models.Money.c.id == client_id):
        money = row.digits
    return money
