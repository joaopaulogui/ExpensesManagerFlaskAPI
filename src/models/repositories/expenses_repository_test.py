from .expenses_repository import ExpensesRepository

def test_repository_expense():
    mocked_description = "description"
    mocked_type = "type"
    mocked_cost = 0
    mocked_date = "2000-01-01"

    expenses_repository = ExpensesRepository()

    expenses_repository.insert_expense(mocked_description, mocked_type, mocked_date, mocked_cost)    

    response = expenses_repository.select_expense_by_type("type")
    print()
    print(response)

    for expense in response:
        expenses_repository.delete_expense(expense.id) 
