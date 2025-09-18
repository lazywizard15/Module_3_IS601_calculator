# Python Calculator

![CI](https://github.com/lazywizard15/Calculator-In-Python/actions/workflows/python-app.yml/badge.svg)

A simple Python calculator application in Python. Supports addition, subtraction, multiplication, and division. Includes automated testing using pytest and continuous integration using GitHub Actions.
---

## Setup Instructions (WSL / Ubuntu)

1. Clone the repository:

git clone https://github.com/lazywizard15/Calculator-In-Python.git
cd Calculator-In-Python

2. Create a virtual environment:

python3 -m venv venv

3. Activate the virtual environment:

source venv/bin/activate

4. Install dependencies:

pip3 install --upgrade pip
pip3 install -r requirements.txt

---

## Running the Interactive Calculator (REPL)

Run the calculator:

python3 main.py

- Supported operations: add, subtract, multiply, divide
- Example session:

Enter operation and two numbers (e.g., add 5 3): add 5 3
Result: 8
Enter operation and two numbers (e.g., add 5 3): multiply 4 2
Result: 8
Enter operation and two numbers (e.g., add 5 3): divide 10 0
Cannot divide by zero.
Enter operation and two numbers (e.g., add 5 3): exit
Exiting calculator...

- Type exit to quit the calculator.

---

## Running Automated Tests

Run all tests using pytest:

pytest -v

- Tests include:
  - Addition, subtraction, multiplication, division
  - Division by zero

- Example output:

test_calculator.py .....                                           [100%]

---

## Continuous Integration

GitHub Actions is configured to run tests automatically on each push to the repository.  
The workflow file is located at:

.github/workflows/python-app.yml

