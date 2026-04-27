from typing import List, Dict

try:
    import pandas as pd
except ImportError:
    pd = None


def load_players(file_path: str) -> List[Dict[str, object]]:
    players = []
    if pd is not None:
        try:
            df = pd.read_csv(file_path)
            for _, row in df.iterrows():
                name = row.get('name') or row.get('Player_Name') or row.get('player_name') or ''
                team = row.get('team') or row.get('Team') or ''
                role = row.get('role') or row.get('Role') or ''
                average = row.get('average') or row.get('Average') or 0
                players.append({
                    'name': str(name).strip(),
                    'team': str(team).strip(),
                    'role': str(role).strip(),
                    'matches': int(row.get('matches') or row.get('Matches') or 0),
                    'runs': int(row.get('runs') or row.get('Runs') or 0),
                    'wickets': int(row.get('wickets') or row.get('Wickets') or 0),
                    'average': float(average or 0),
                    'rank': int(row.get('rank') or row.get('Rank') or 0),
                })
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as exc:
            print(f"Error reading CSV with pandas: {exc}")
    else:
        import csv
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row.get('name') or row.get('Player_Name') or row.get('player_name') or ''
                    team = row.get('team') or row.get('Team') or ''
                    role = row.get('role') or row.get('Role') or ''
                    average = row.get('average') or row.get('Average') or 0
                    players.append({
                        'name': name.strip(),
                        'team': team.strip(),
                        'role': role.strip(),
                        'matches': int(row.get('matches') or row.get('Matches') or 0),
                        'runs': int(row.get('runs') or row.get('Runs') or 0),
                        'wickets': int(row.get('wickets') or row.get('Wickets') or 0),
                        'average': float(average or 0),
                        'rank': int(row.get('rank') or row.get('Rank') or 0),
                    })
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as exc:
            print(f"Error reading CSV: {exc}")
    return players


def sort_players(players: List[Dict[str, object]], key: str, reverse: bool = True):
    return sorted(players, key=lambda p: p.get(key, 0), reverse=reverse)


def assign_rank(players: List[Dict[str, object]], key: str = 'average', reverse: bool = True):
    sorted_players = sort_players(players, key=key, reverse=reverse)
    for position, player in enumerate(sorted_players, start=1):
        player['rank'] = position
    return sorted_players
