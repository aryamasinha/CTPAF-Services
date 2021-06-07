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


@app.route('/result_datascience')
def result_ds():
    return render_template('result_datascience.html')

@app.route('/result_startup')
def result_st():
    return render_template('result_startup.html')

if __name__ == "__main__":
    app.run(debug=True)