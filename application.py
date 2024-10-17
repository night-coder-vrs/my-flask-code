from flask import Flask, render_template, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dbmsproject469539'

# Home page - Index
@app.route('/')
def index():
    return render_template('index.html')

    
# Auto Server running
if __name__ == '__main__':
    app.run(debug=True)
