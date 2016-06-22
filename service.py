from flask import Flask, render_template, jsonify, request, make_response, abort

service = Flask(__name__)

users = [
    {
        'id': 1,
        'name': 'Test',
        'age': 100,
        'approved': False,
        'detail': 'Sample Details'
    }
]


@service.route('/')
def index():
    return render_template('index.html')


@service.route('/users/all', methods=['GET'])
def get_tasks():
    return jsonify({'Users': users})


@service.route('/users/user/name/<userName>', methods=['GET'])
def get_deeds(userName):
    user = [user for user in users if user['name'] == userName]
    if len(user) == 0:
        abort(404)
    return jsonify({'User': user[0]})


@service.route('/users/user/add', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    try:
        id_t = users[-1]['id']
    except:
        id_t = 0
    user = {
        'id': id_t + 1,
        'age': request.json['age'],
        'name': request.json['name'],
        'detail': request.json.get('detail', ""),
        'approved': False
    }
    users.append(user)
    return jsonify({'User': user}), 201


@service.route('/users/user/update/id/<int:id>', methods=['PUT'])
def update_users(id):
    user = [user for user in users if user['id'] == id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    user[0]['name'] = request.json.get('name', user[0]['name'])
    user[0]['detail'] = request.json.get('detail', user[0]['detail'])
    user[0]['approved'] = request.json.get('done', user[0]['approved'])
    return jsonify({'user': user[0]})


@service.route('/users/user/remove/id/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = [user for user in users if user['id'] == id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})


@service.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'End Point Not found'}), 404)


if __name__ == '__main__':
    service.run(
        host="0.0.0.0",
        port=int("8001"),
        debug=True
    )
