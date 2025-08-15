from src.models.entities.expenses import Expense as ExpenseEntity
from src.controllers.expense_lister_controller import ExpenseListerController
from typing import Dict

class TotalDividerController:
    def divide_total(self, date:str):
        try:
            self.__validate_fields(date)
            total = self.__total_by_date(date)
            divided_total = self.__divide_total(date)
            response = self.__format_response(divided_total, total)
            return {"success": True, "response": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}
        
    def __validate_fields(self, date: str) -> None:
        if not isinstance(date, str):
            raise Exception("Invalid date")
        
    def __divide_total(self, date: str) -> Dict:
        expense_lister_controller = ExpenseListerController()
        expenses = expense_lister_controller.select_expense_by_date(date)["response"]["expenses"]

        cost_by_type = {}
        total = 0

        for expense in expenses:
            if expense["type"] in cost_by_type:
                cost_by_type[expense["type"]] += expense["cost"]
            else:
                cost_by_type[expense["type"]] = expense["cost"]
            
            total += expense["cost"]

        divided_total = {}

        for key in cost_by_type:
            divided_total[key] = (cost_by_type[key]/total)*100

        return divided_total
    
    def __total_by_date(self, date: str) -> int:
        expense_lister_controller = ExpenseListerController()
        expenses = expense_lister_controller.select_expense_by_date(date)["response"]["expenses"]
        
        total = 0
    
        for expense in expenses:  
            total += expense["cost"]

        return total
    
    def __format_response(self, divided_total: Dict, total: int) -> Dict:
        return {
            "count": 1,
            "type": "Dict",
            "infos": divided_total,
            "total": total
        }