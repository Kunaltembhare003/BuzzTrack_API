from flask import Flask, request, jsonify
from marshmallow import ValidationError
from schemas import FizzBuzzSchema
#from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
fizz_buzz_schema = FizzBuzzSchema()
# Store statistics
request_stats = {}
#app.config["JWT_SECRET_KEY"] = "kunal_learning"
#jwt= JWTManager(app)

'''@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Validate the username and password (this is just an example, use a secure method)
    if username == 'your_username' and password == 'your_password':
        # Create an access token
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401'''

@app.route('/fizzbuzz', methods=['GET'])
#@jwt_required()
def fizzbuzz():
    try:
        data = fizz_buzz_schema.load(request.args)
    except ValidationError as e:
        return jsonify({"error": "Input validation failed", "details": e.messages}), 400

    int1 = data['int1']
    int2 = data['int2']
    limit = data['limit']
    str1 = data['str1']
    str2 = data['str2']
    '''data = request.get_json()
    int1 = data.get('int1', 3)
    int2 = data.get('int2', 5)
    limit = data.get('limit', 100)
    str1 = data.get('str1', 'fizz')
    str2 = data.get('str2', 'buzz')'''
    result = [
        str1 + str2 if i % int1 == 0 and i % int2 == 0 else
        str1 if i % int1 == 0 else
        str2 if i % int2 == 0 else
        str(i)
        for i in range(1, limit + 1)
    ]

    # Update statistics
    params = (int1, int2, limit, str1, str2)
    request_stats[params] = request_stats.get(params, 0) + 1

    return jsonify(result)

@app.route('/statistics', methods=['GET'])
#@jwt_required()
def statistics():
    if not request_stats:
        return jsonify({"message": "No statistics available"})

    most_used_request = max(request_stats, key=request_stats.get)
    return jsonify({
        "most_used_request": {
            "int1": most_used_request[0],
            "int2": most_used_request[1],
            "limit": most_used_request[2],
            "str1": most_used_request[3],
            "str2": most_used_request[4],
        },
        "hits": request_stats[most_used_request]
    })

# Run the server
if __name__ == '__main__':
    app.run(debug=True)

