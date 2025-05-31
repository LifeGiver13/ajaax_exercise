from flask import Flask, render_template, make_response, request, jsonify
import json


app = Flask(__name__)


@app.route('/data')
def data():
    with open('club.json', 'r') as club:
        club_json = club.read()
    response = make_response(club_json)
    response.headers['Content-type'] = 'application/json'
    return response


@app.route('/upData/<int:id>', methods=['GET', 'PUT'])
def update_data(id):
    if request.method == 'GET':
        return render_template('ajax.html')
    if request.method == "PUT":
        data = request.get_json()
        name = data.get('name')
        handle = data.get('handle')

        with open('club.json', 'r') as club:
            club_json = json.load(club)

            for club_info in club_json:
                club = club_info.get('data')
                if club and str(club.get('id')) == str(id):
                    club['name'] = name
                    club['handle'] = handle
                    break

        with open('club.json', 'w') as club:
            json.dump(club_json, club, indent=4)

        return jsonify(
            {
                'message': "Success Updating info",
                'name': name,
                'handle': handle
            })


if __name__ == "__main__":
    app.run(debug=True)
