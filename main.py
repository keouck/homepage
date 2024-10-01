from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/degoogling-1')
def degoogling_one():
    return render_template('degoogling-1.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
