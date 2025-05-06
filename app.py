from flask import Flask, render_template, request

app = Flask(__name__)

def compute_npv_and_break_even(price, monthly_revenue, monthly_expense, rate, max_months=60):
    discounted_npv = []
    nominal_npv = []
    revenue_total = []
    expense_total = []

    cumulative_discounted = -price
    cumulative_nominal = -price

    break_even_month = None

    for t in range(1, max_months + 1):
        gross = monthly_revenue * t
        expense = monthly_expense * t
        nominal = gross - expense
        discount_factor = (1 + rate / 12) ** t
        discounted = (monthly_revenue - monthly_expense) / discount_factor

        cumulative_discounted += discounted
        cumulative_nominal += (monthly_revenue - monthly_expense)

        discounted_npv.append(round(cumulative_discounted, 2))
        nominal_npv.append(round(cumulative_nominal, 2))
        revenue_total.append(round(gross, 2))
        expense_total.append(round(expense, 2))

        if break_even_month is None and cumulative_discounted >= 0:
            break_even_month = t

    return discounted_npv, nominal_npv, revenue_total, expense_total, break_even_month

@app.route("/", methods=["GET", "POST"])
def index():
    price = None
    npv_table = []
    months = []
    break_even_input = None

    if request.method == "POST":
        try:
            units = float(request.form["units"])
            rent = float(request.form["rent"])
            expense = float(request.form["expense"])
            rate = float(request.form["rate"]) / 100
            break_even_input = int(float(request.form["break_even"]))

            revenue = units * rent
            monthly_profit = revenue - expense

            if monthly_profit <= 0:
                price = "Not possible (expenses too high)"
            else:
                # Calculate discounted price based on break-even input
                discounted_price = 0
                for t in range(1, break_even_input + 1):
                    discount_factor = (1 + rate / 12) ** t
                    discounted_price += monthly_profit / discount_factor
                price = round(discounted_price, 2)

            # Generate NPV data using discounted price
            discounted_npv, nominal_npv, revenues, expenses, _ = compute_npv_and_break_even(
                price, revenue, expense, rate, max_months=60)

            months = list(range(1, len(discounted_npv) + 1))
            npv_table = list(zip(months, discounted_npv, nominal_npv, revenues, expenses))

        except ValueError:
            price = "Invalid input"

    return render_template(
        "form.html",
        price=price,
        npv_table=npv_table,
        months=months,
        discounted_npv=[x[1] for x in npv_table],
        break_even_input=break_even_input
    )

if __name__ == "__main__":
    app.run(debug=True)
