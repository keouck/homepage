from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/shenanigans')
def shenanigans():
    return render_template('shenanigans.html')

@app.route('/devnull')
def devnull():
    return render_template('devnull.html')

if __name__ == '__main__':
    app.run(debug=True)