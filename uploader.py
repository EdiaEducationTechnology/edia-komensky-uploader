import json

import requests
from fire import Fire
from tqdm import tqdm


def main(file_name, api_host='https://api.komensky.edia.nl', api_key=''):
    with open(file_name) as f:
        json_data = json.load(f)
        for item in tqdm(json_data):
            skillID = item['id']
            name = item['name']
            description = _get_description(item)
            category = item['category']
            resp = requests.get(f'{api_host}/api/taxonomy/{skillID}', headers=_get_headers(api_key))
            if resp.status_code == 200:
                continue
            elif resp.status_code == 404:
                data = {'skillID': skillID,
                        'name': name,
                        'description': description,
                        'category': category}
                resp = requests.post(f'{api_host}/api/taxonomy?tag=1', json=data, headers=_get_headers(api_key))
                if resp.status_code not in [200, 201]:
                    print(f'Unexpected response code: {resp.status_code}, reason: {resp.reason}')
                    break
            else:
                print(f'Unexpected response code: {resp.status_code}, reason: {resp.reason}')
                break


def _get_headers(api_key) -> dict:
    return {'Authorization': f'Bearer {api_key}'}


def _end_punc(val: str):
    return val.endswith('.') or val.endswith('?') or val.endswith('?')


def _clean_and_fix(value: str) -> str:
    value = value.strip()
    if not _end_punc(value):
        value += '.'
    value += '\n'
    return value


def _get_description(item):
    description_ = _clean_and_fix(item['description'])
    for level in item['levels']:
        for description in level['description']:
            description_ += _clean_and_fix(description)
        for knowledge in level['knowledge']:
            description_ += _clean_and_fix(knowledge)
        for ability in level['ability']:
            description_ += _clean_and_fix(ability)
    return description_


if __name__ == '__main__':
    Fire(main)
