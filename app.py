from flask import Flask, json, jsonify, render_template, request
from tools.col import myzip
from tools.numbers.simp import addition, subtraction
from tools.numbers.comp import ispal, sumofdigits

app = Flask(__name__)

from jinja2 import Environment, FileSystemLoader

def render_template_with_zip(template_name, list1, list2):
    env = Environment(loader=FileSystemLoader('./templates'))

    template = env.get_template(template_name)

    # Zip the two lists together
    zipped_data = myzip(list1, list2)

    result = template.render(data=zipped_data)
    return result

def render_template_with_results(template_name, num, func1_result, func2_result):
    env = Environment(loader=FileSystemLoader('./templates'))

    template = env.get_template(template_name)

    data = {
        'num': num,
        'sum_of_digits_result': func1_result,
        'is_palindrome_result': func2_result
    }

    result = template.render(data=data)
    return result

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/zip", methods=["POST"])
def zip_lists():
    try:
        # Get the input lists from the request
        data = request.get_json()
        list1 = data.get("list1", [])
        list2 = data.get("list2", [])

        # Zip the lists and return the zipped data as JSON
        zipped_data = myzip(list1, list2)
        return jsonify(result=zipped_data)

    except Exception as e:
        return jsonify(error=str(e))
    
@app.route("/calculate_simp", methods=["POST"])
def calculate_simp():
    try:
        data = request.get_json()
        num1 = int(data.get("num1", 0))
        num2 = int(data.get("num2", 0))

        # Perform addition and subtraction
        result_addition = addition(num1, num2)
        result_subtraction = subtraction(num1, num2)

        # Return the results as JSON
        return jsonify(result_addition=result_addition, result_subtraction=result_subtraction)

    except Exception as e:
        return jsonify(error=str(e))

@app.route("/calculate_sum_of_digits", methods=["POST"])
def calculate_sum_of_digits():
    try:
        data = request.get_json()
        num = int(data.get("num", 0))

        # Calculate sum of digits
        result_sum_of_digits = sumofdigits(num)

        # Return the result as JSON
        return jsonify(result_sum_of_digits=result_sum_of_digits)

    except Exception as e:
        return jsonify(error=str(e))
    
@app.route("/calculate_is_palindrome", methods=["POST"])
def calculate_is_palindrome():
    try:
        data = request.get_json()
        num = int(data.get("num", 0))

        # Check if the number is a palindrome
        result_is_palindrome = ispal(num)

        # Return the result as JSON
        return jsonify(result_is_palindrome=result_is_palindrome)

    except Exception as e:
        return jsonify(error=str(e))
    
if __name__ == '__main__':
    app.run(debug=True)