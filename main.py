import argparse
import pandas as pd
from ranking import load_players, assign_rank
from filter import (
    filter_by_team,
    filter_by_role,
    filter_by_min_runs,
    filter_by_max_average,
)

DATASETS = {
    'cricket_final': 'cricket_final.csv',
    'player': 'player.csv',
    'batsmen': 'batsmen_leaderboard.csv',
    'bowlers': 'bowlers_leaderboard.csv',
    'allrounder': 'allrounder_leaderboard.csv',
}
DEFAULT_DATASET = 'cricket_final'


def print_players(players):
    if not players:
        print('No players found.')
        return

    print(f"{'Rank':<5} {'Name':<20} {'Team':<12} {'Role':<12} {'Matches':<8} {'Runs':<6} {'Wkts':<5} {'Avg':<6}")
    print('-' * 80)
    for player in players:
        print(
            f"{player.get('rank', ''):<5} {player.get('name', ''):<20} {player.get('team', ''):<12} {player.get('role', ''):<12} "
            f"{player.get('matches', 0):<8} {player.get('runs', 0):<6} {player.get('wickets', 0):<5} {player.get('average', 0):<6.2f}"
        )


def main():
    parser = argparse.ArgumentParser(
        description='Cricket player ranking and filtering using the provided dataset'
    )
    parser.add_argument(
        '--dataset',
        choices=DATASETS.keys(),
        default=DEFAULT_DATASET,
        help='Choose a provided dataset to load',
    )
    parser.add_argument(
        '--file',
        help='Path to a CSV file to load (overrides --dataset)',
    )
    parser.add_argument('--team', help='Filter players by team')
    parser.add_argument('--role', help='Filter players by role (Bowler/Batsman)')
    parser.add_argument('--min-runs', type=int, help='Show players with at least this many runs')
    parser.add_argument('--max-average', type=float, help='Show players with average no greater than this')
    parser.add_argument(
        '--sort-by',
        choices=['average', 'runs', 'wickets'],
        default='average',
        help='Sort players by this field',
    )
    parser.add_argument('--top', type=int, default=10, help='Show top N players')

    args = parser.parse_args()
    source_file = args.file or DATASETS.get(args.dataset, DATASETS[DEFAULT_DATASET])

    print(f"Loading dataset: {source_file}")
    players = load_players(source_file)
    if not players:
        print('No data loaded. Check your CSV file path and content.')
        return

    players = assign_rank(players, key=args.sort_by, reverse=True)

    # Apply filters
    if args.team:
        players = filter_by_team(players, args.team)
    if args.role:
        players = filter_by_role(players, args.role)
    if args.min_runs is not None:
        players = filter_by_min_runs(players, args.min_runs)
    if args.max_average is not None:
        players = filter_by_max_average(players, args.max_average)

    print(f"\nShowing top {args.top} players")
    print_players(players[:args.top])


if __name__ == '__main__':
    main()
