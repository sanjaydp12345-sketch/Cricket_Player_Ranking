import requests

datasets = ['player', 'batsmen', 'bowlers', 'allrounder']

for dataset in datasets:
    payload = {
        'dataset': dataset,
        'top': 2,
        'sort_by': 'average'
    }

    try:
        response = requests.post('http://127.0.0.1:5000/api/players', json=payload, timeout=5)
        data = response.json()
        print(f'{dataset}: {len(data)} players returned')
        if data:
            print(f'  First: {data[0].get("name", "N/A")}')
    except Exception as e:
        print(f'{dataset}: Error - {e}')