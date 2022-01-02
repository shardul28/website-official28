import flask


# Create the application.
app= flask.Flask(__name__)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)