# Demo Flask

# Import
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def index():
    return 'Index Page - Start page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

# main driver function
if __name__ == '__main__':
	app.run()
