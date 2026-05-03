import json
from datetime import datetime

FILE_NAME = "history.json"

# Ensure file exists
def init_file():
    try:
        with open(FILE_NAME, "x") as f:
            json.dump([], f)
    except FileExistsError:
        pass


# Save operation to JSON
def save_history(operation, a, b, result):
    data = {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open(FILE_NAME, "r") as f:
        history = json.load(f)

    history.append(data)

    with open(FILE_NAME, "w") as f:
        json.dump(history, f, indent=4)


# Calculator operations
def calculate(operation, a, b):
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b == 0:
            return {"error": "Division by zero"}
        result = a / b
    elif operation == "**":
        result = a ** b
    elif operation == "%":
        result = a % b
    else:
        return {"error": "Invalid operation"}

    save_history(operation, a, b, result)

    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }


# Get history
def get_history():
    with open(FILE_NAME, "r") as f:
        return json.load(f)