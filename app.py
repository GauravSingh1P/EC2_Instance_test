from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    if request.method == 'POST':
        # This catches the data sent from the HTML form
        user_input = request.form.get('food_item')
    
    return render_template('index.html', user_input=user_input)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)