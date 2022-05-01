from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = "0"  # Default value for the result

    if request.method == "POST":
        button = request.form.get("button")  # Get the button pressed
        current_expr = request.form.get("expression", "")  # Get the current expression

        if button == "AC":
            result = "0"  # Clear the screen if AC is pressed
        elif button == "=":
            try:
                # Replace the operator symbols with their Python equivalents
                expression = current_expr.replace("×", "*").replace("÷", "/")
                result = str(eval(expression))  # Use eval to calculate the result
            except Exception as e:
                result = "Error"  # In case of any errors, display "Error"
        else:
            if current_expr == "0":
                result = button  # Start with the first number if it's 0
            else:
                result = current_expr + button  # Append to the current expression

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
