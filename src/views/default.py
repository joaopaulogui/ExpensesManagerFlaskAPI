from flask import Flask
from flask import render_template, request, redirect, url_for
from src.controllers.expense_register_controller import RegisterExpenseForm
from src.controllers.expense_register_controller import ExpenseRegisterController
from src.controllers.expense_lister_controller import ExpenseListerController
from src.controllers.total_divider_controller import TotalDividerController
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    selected_date = request.args.get("date") or datetime.today().strftime("%d/%m/%Y")
    query_date = datetime.strptime(selected_date, "%d/%m/%Y").strftime("%Y-%m-%d")

    form = RegisterExpenseForm()
    if request.method == "POST":
        if "date" in request.form:
            selected_date = request.form.get("date")
        elif "cost" in request.form and form.validate_on_submit():
            expense_register_controller = ExpenseRegisterController()
            expense_register_controller.insert_expense(
                form.description.data,
                form.type.data,
                query_date,
                form.cost.data
            )
        return redirect(url_for("index", date=selected_date))
    
    expense_lister_controller = ExpenseListerController()
    lister_response = expense_lister_controller.select_expense_by_date(query_date)

    if lister_response["success"]:
        expenses = lister_response["response"]["expenses"]
    else:
        expenses = []

    total_divider_controller = TotalDividerController()
    response = total_divider_controller.divide_total(query_date)

    if response["success"]:  
        divided_total = response["response"]["infos"]
        total = response["response"]["total"]
    else:
        divided_total = {}
        total = 0

    return render_template(
        'index.html',
        selected_date=selected_date,
        form=form,
        expenses=expenses,
        divided_total=divided_total,
        total=total
    )