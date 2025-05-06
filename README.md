# 🧮 Break-Even & NPV Calculator

This Flask web app estimates the required investment price for a rental property based on your desired break-even time. It calculates discounted net present value (NPV) over time and shows a monthly breakdown table and chart.

---

## 📊 Features

- 🔢 **Inputs**:
  - Number of units
  - Monthly rent per unit
  - Monthly expenses
  - Annual discount rate (%)
  - Desired break-even time (in months)

- 📈 **Outputs**:
  - Required investment price (based on discounted cash flow)
  - Discounted & nominal NPV over 60 months
  - Table of monthly gross revenue, expenses, and NPV values
  - Interactive chart using Chart.js

---

## 🚀 How to Run It

1. **Clone the repository**

   ```bash
   git clone https://github.com/allieshepherd11/flask-npv-calculator.git
   cd flask-npv-calculator
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv
   # Activate:
   venv\Scripts\activate   # on Windows
   source venv/bin/activate   # on Mac/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install flask
   ```

4. **Run the Flask app**

   ```bash
   python app.py
   ```

5. **Open your browser** and visit:
   ```
   http://127.0.0.1:5000/
   ```
