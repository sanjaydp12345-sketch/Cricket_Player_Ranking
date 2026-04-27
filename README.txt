Cricket Player Ranking

Usage:
  python main.py --top 5
  python main.py --dataset player --team India --top 5
  python main.py --dataset batsmen --sort-by runs --top 5
  python main.py --file player.csv --min-runs 500 --top 10

Options:
  --dataset     Choose a built-in dataset: cricket_final, player, batsmen, bowlers, allrounder.
  --file        Path to a CSV file to load (overrides --dataset).
  --team        Filter output by team name.
  --role        Filter output by player role.
  --min-runs    Show players with at least this many runs.
  --max-average Show players with average no greater than this.
  --sort-by     Sort players by average, runs, or wickets.
  --top         Number of top players to display (default 10).
