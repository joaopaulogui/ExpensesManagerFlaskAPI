from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired

from src.models.entities.expenses import Expense as ExpenseEntity
from src.models.repositories.expenses_repository import ExpensesRepository
from typing import Dict

class RegisterExpenseForm(FlaskForm):
    description = StringField("description", validators=[DataRequired()])
    type = StringField("type", validators=[DataRequired()])
    cost = DecimalField("cost", validators=[DataRequired()], places=2)

class ExpenseRegisterController:
    def insert_expense(self, description: str, type: str, date: str, cost: int) -> Dict:
        try:
            self.__validate_fields(description, type, date, cost)
            expense = self.__add_expense(description, type, date, cost)
            response = self.__format_response(expense)
            return {"success": True, "response": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __validate_fields(self, description: str, type: str, date: str, cost: int) -> None:
        if not isinstance(description, str):
            raise Exception("Invalid description")
        
        if not isinstance(type, str):
            raise Exception("Invalid type")
        
        if not isinstance(date, str):
            raise Exception("Invalid date")
        
        try: int(cost)
        except: raise Exception("Invalid cost")
        
    def __add_expense(self, description: str, type: str, date: str, cost: int) -> ExpenseEntity:
        expenses_repository = ExpensesRepository()
        expense = expenses_repository.insert_expense(description, type, date, cost)
        return expense
    
    def __format_response(self, expense: ExpenseEntity) -> Dict:
        return {
            "count": 1,
            "type": "Expense",
            "Infos": {
                "id": expense.id,
                "description": expense.description,
                "type": expense.type,
                "date": expense.date,
                "cost": expense.cost
            }
        }