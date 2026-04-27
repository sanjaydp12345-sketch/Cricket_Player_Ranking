from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from ranking import load_players, assign_rank
from filter import (
    filter_by_team,
    filter_by_role,
    filter_by_min_runs,
    filter_by_max_average,
)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

DATASETS = {
    'cricket_final': 'cricket_final.csv',
    'player': 'player.csv',
    'batsmen': 'batsmen_leaderboard.csv',
    'bowlers': 'bowlers_leaderboard.csv',
    'allrounder': 'allrounder_leaderboard.csv',
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/datasets', methods=['GET'])
def get_datasets():
    return jsonify(list(DATASETS.keys()))


@app.route('/api/players', methods=['POST'])
def get_players():
    data = request.json
    dataset = data.get('dataset', 'cricket_final')
    team = data.get('team')
    role = data.get('role')
    min_runs = data.get('min_runs')
    max_average = data.get('max_average')
    sort_by = data.get('sort_by', 'average')
    top = data.get('top', 10)

    file_path = DATASETS.get(dataset, DATASETS['cricket_final'])
    players = load_players(file_path)

    if not players:
        return jsonify([])

    players = assign_rank(players, key=sort_by, reverse=True)

    if team:
        players = filter_by_team(players, team)
    if role:
        players = filter_by_role(players, role)
    if min_runs is not None:
        players = filter_by_min_runs(players, min_runs)
    if max_average is not None:
        players = filter_by_max_average(players, max_average)

    return jsonify(players[:top])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
