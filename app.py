from flask import Flask, render_template, request, session, jsonify

import requests

app = Flask(__name__)

app.secret_key = 'super_secret_key'


@app.route('/', methods=['GET', 'POST'])
def home():
    data = requests.get('https://api.covid19india.org/state_district_wise.json').json()
    output = dict(data)

    state_list = []
    active_list = []
    confirmed_list = []
    recovered_list = []
    deceased_list = []
    for key, value in output.items():
        if key != 'State Unassigned':
            for key2, value2 in value.items():
                if type(value2) == dict:
                    total_active = sum(d['active'] for d in value2.values() if d)
                    total_confirmed = sum(d['confirmed'] for d in value2.values() if d)
                    total_recovered = sum(d['recovered'] for d in value2.values() if d)
                    total_deceased = sum(d['deceased'] for d in value2.values() if d)

                    state_list.append(key)
                    confirmed_list.append(total_confirmed)
                    active_list.append(total_active)
                    recovered_list.append(total_recovered)
                    deceased_list.append(total_deceased)

    return render_template("home.html", **locals())


@app.route('/state', methods=['POST'])
def state():
    state = request.args.get('value')
    session['state'] = state
    return jsonify({'reply': 'success'})


@app.route('/districts', methods=['GET'])
def display():
    data = requests.get('https://api.covid19india.org/state_district_wise.json').json()
    output = dict(data)

    if session.get('state', None):
        state = session.get('state', None)

        district_list = []

        state_split = state.split(" ")
        del state_split[0]
        seperator = ' '
        state_name = seperator.join(state_split)

        for key, value in output.items():
            if key == state_name:
                value1 = output[key]
                for key2, value2 in value1.items():
                    if type(value2) == dict:
                        for key3, value3 in value2.items():
                            district_list.append(key3)

                        total_active_district = [d['active'] for d in value2.values() if d]
                        total_confirmed_district = [d['confirmed'] for d in value2.values() if d]
                        total_recovered_district = [d['recovered'] for d in value2.values() if d]
                        total_deceased_district = [d['deceased'] for d in value2.values() if d]

        return render_template('state.html', **locals())


if __name__ == "__main__":
    app.run(debug=True)



