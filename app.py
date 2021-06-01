from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/startup')
def startup():
    return render_template('startup_form.html')


@app.route('/datascience')
def datascience():
    return render_template('data_science_form.html')


@app.route('/result')
def result():
    return render_template('score.html')

if __name__ == "__main__":
    app.run(debug=True)