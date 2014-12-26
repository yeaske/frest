from flask import Flask, render_template, jsonify

service = Flask(__name__)


@service.route('/')
def index():
    return render_template('index.html')


@service.route('/deeds/userid/<userid>')
def get_deeds(userid):
    lst = [
        {'userid': userid, 'deed': {'a': 66, 'b': 222}},
        {'userid': userid, 'deed': {'a': 33, 'b': 111}},
        ]
    return jsonify(result=lst)

if __name__ == '__main__':
    service.run(
        host="0.0.0.0",
        port=int("8001"),
        debug=True
    )
