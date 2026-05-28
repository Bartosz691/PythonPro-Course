from flask import Flask
app = Flask(__name__)

@app.route('/calc/<func>/<int:num1>/<int:num2>')
def calc(func, num1, num2):
    match func:
        case "add":
            return str(num1 + num2)
        case "mul":
            return str(num1 * num2)
        
if __name__ == "__main__":
    app.run(debug=True)