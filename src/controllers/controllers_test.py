from .expense_lister_controller import ExpenseListerController
from .expense_register_controller import ExpenseRegisterController
from .total_divider_controller import TotalDividerController
from src.models.repositories.expenses_repository import ExpensesRepository

def test_select_expense_by_date():
    mocked_description = "description"
    mocked_type = "type"
    mocked_cost = 1
    mocked_date = "1500-01-01"

    expense_register_controller = ExpenseRegisterController()
    expense_lister_controller = ExpenseListerController()
    total_divider_controller = TotalDividerController()
    expenses_repository = ExpensesRepository()

    for i in range(5):
        response = expense_register_controller.insert_expense(mocked_description, mocked_type, mocked_date, mocked_cost)

        if not response["success"]:
            print()
            print(response["error"])

    response = expense_lister_controller.select_expense_by_date(mocked_date)
    print()
    print(response)

    divided_total = total_divider_controller.divide_total(mocked_date)
    print()
    print(divided_total)

    for expense in response["response"]["expenses"]:
        expenses_repository.delete_expense(expense.id)