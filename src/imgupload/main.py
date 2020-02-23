import flask
from werkzeug import secure_filename

imgupload = flask.Flask(__name__)


@imgupload.route('/', methods=['POST'])
def index():
    if flask.request.method == 'POST' and flask.request.files:
        filename = secure_filename(flask.request.files['file'].filename)
        print(filename)
        return f'{filename}'
    else:
        return flask.redirect(flask.url_for('mockform'))


@imgupload.route('/mockform')
def mockform():
    return ''' <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="/" method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>'''


if __name__ == '__main__':
    imgupload.run(port='8080', debug=True)