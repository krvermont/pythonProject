import json


def load_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def get_all_candidates() -> list[dict]:
    return load_json()

def get_candidate_by_id(idx: int) -> dict | None:
    candidates = get_all_candidates()

    for candidate in candidates:
        if candidate['pk'] == idx:
            return candidate
    return None


def get_candidate_by_name(candidate_name: str) -> list[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if candidate_name in candidate['name']:
            result.append(candidate)
    return result

def get_candidate_by_skills(candidate_skill: str) -> list[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if candidate_skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

