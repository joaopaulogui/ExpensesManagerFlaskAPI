import datetime
from src.models.settings.connection import DBConnectionHandler
from src.models.entities.expenses import Expense as ExpenseEntity

class ExpensesRepository:

    @classmethod
    def insert_expense(cls, description: str, type: str, date: str, cost: int) -> ExpenseEntity:
        with DBConnectionHandler() as database:
            try:
                new_registry = ExpenseEntity(description, type, date, cost*100)
                database.session.add(new_registry)
                database.session.commit()
                return new_registry
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    @classmethod
    def select_expense_by_type(cls, type: str) -> any:
        with DBConnectionHandler() as database:
            try:
                expenses = (
                    database.session
                        .query(ExpenseEntity)
                        .filter(ExpenseEntity.type == type)
                        .all()
                )
                return expenses
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    @classmethod
    def select_expense_by_date(cls, date: str) -> any:
        with DBConnectionHandler() as database:
            try:
                y, m, d = date.split("-")

                expenses = (
                    database.session
                        .query(ExpenseEntity)
                        .filter(ExpenseEntity.date == datetime.date(int(y), int(m), int(d)))
                        .all()
                )
                return expenses
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def delete_expense(cls, id: int) -> None:
         with DBConnectionHandler() as database:
            try:
                database.session.query(ExpenseEntity).filter(ExpenseEntity.id == id).delete()
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception