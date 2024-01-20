# Install Flask using: pip install Flask

from flask import Flask, request, jsonify

app = Flask(__name__)

# Store statistics
request_stats = {}

@app.route('/fizzbuzz', methods=['GET'])
def fizzbuzz():
    int1 = int(request.args.get('int1'))
    int2 = int(request.args.get('int2'))
    limit = int(request.args.get('limit'))
    str1 = request.args.get('str1')
    str2 = request.args.get('str2')

    result = []
    for i in range(1, limit + 1):
        output = ""
        if i % int1 == 0:
            output += str1
        if i % int2 == 0:
            output += str2
        if not output:
            output = str(i)
        result.append(output)

    # Update statistics
    params = (int1, int2, limit, str1, str2)
    request_stats[params] = request_stats.get(params, 0) + 1

    return jsonify(result)

@app.route('/statistics', methods=['GET'])
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



'''from flask import Flask, request, jsonify, render_template
from collections import Counter

app = Flask(__name__)

# Dictionary to store request statistics
request_stats = Counter()

@app.route('/buzzfizz', methods=['GET', 'POST'])
def buzzfizz():
    if request.method == 'POST':
        int1 = int(request.form.get('int1',3))  # Default to 3 if not provided
        int2 = int(request.form.get('int2',5))  # Default to 5 if not provided
        limit = int(request.form.get('limit',100))  # Default to 100 if not provided
        str1 = request.form.get('str1', 'buzz')  # Default to 'buzz' if not provided
        str2 = request.form.get('str2', 'fizz')  # Default to 'fizz' if not provided
    elif request.method == 'GET':
        int1 = int(request.args.get('int1',3))  # Default to 3 if not provided
        int2 = int(request.args.get('int2',5))  # Default to 5 if not provided
        limit = int(request.args.get('limit',100))  # Default to 100 if not provided
        str1 = request.args.get('str1', 'buzz')  # Default to 'buzz' if not provided
        str2 = request.args.get('str2', 'fizz')  # Default to 'fizz' if not provided

    result = [
        str1 + str2 if i % int1 == 0 and i % int2 == 0 else
        str1 if i % int1 == 0 else
        str2 if i % int2 == 0 else
        str(i)
        for i in range(1, limit + 1)
    ]

    # Update request statistics
    request_params = (int1, int2, limit, str1, str2)
    request_stats[request_params] = request_stats.get(request_params, 0) + 1

    #return jsonify(result)
    return render_template('index.html',result=result)

@app.route('/buzzfizz/statistics', methods=['GET'])
def buzzfizz_statistics():
    most_used_request = max(request_stats, key=request_stats.get, default=None)
    hits = request_stats.get(most_used_request, 0)

    return jsonify({
        'most_used_request': most_used_request,
        'hits': hits
    })

if __name__ == '__main__':
    app.run(debug=True)'''

