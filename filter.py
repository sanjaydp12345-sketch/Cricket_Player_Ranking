from typing import List, Dict


def filter_by_team(players: List[Dict[str, object]], team: str) -> List[Dict[str, object]]:
    return [p for p in players if p['team'].lower() == team.lower()]


def filter_by_role(players: List[Dict[str, object]], role: str) -> List[Dict[str, object]]:
    return [p for p in players if p['role'].lower() == role.lower()]


def filter_by_min_runs(players: List[Dict[str, object]], min_runs: int) -> List[Dict[str, object]]:
    return [p for p in players if p['runs'] >= min_runs]


def filter_by_max_average(players: List[Dict[str, object]], max_average: float) -> List[Dict[str, object]]:
    return [p for p in players if p['average'] <= max_average]
