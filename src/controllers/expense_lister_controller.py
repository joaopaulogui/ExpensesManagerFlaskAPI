from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.validators import DataRequired

from src.models.entities.expenses import Expense as ExpenseEntity
from src.models.repositories.expenses_repository import ExpensesRepository
from typing import Dict

class DateForm(FlaskForm):
    date = DateField("description", validators=[DataRequired()], format="%d/%m/%Y")

class ExpenseListerController:
    def select_expense_by_date(self, date: str) -> Dict:
        try:
            self.__validate_fields(date)
            expenses = self.__find_by_date(date)
            response = self.__format_response(expenses)
            return {"success": True, "response": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __validate_fields(self, date: str) -> None:
        if not isinstance(date, str):
            raise Exception("Invalid date")
        
    def __find_by_date(self, date: str) -> list[ExpenseEntity]:
        expenses_repository = ExpensesRepository()
        expenses = expenses_repository.select_expense_by_date(date)

        if len(expenses) == 0: raise Exception("No expense found")

        return expenses
    
    def __format_response(self, expenses: list[ExpenseEntity]) -> Dict:
        result = {
            "count": len(expenses),
            "type": "list[Dict]",
            "expenses": []
        }

        for expense in expenses:
            result["expenses"].append({
                "id": expense.id,
                "description": expense.description,
                "type": expense.type,
                "date": expense.date,
                "cost": expense.cost
            })

        return result