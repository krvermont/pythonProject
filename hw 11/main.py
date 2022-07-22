
from utils import get_all_candidates
from utils import get_candidate_by_id
from utils import get_candidate_by_name
from utils import get_candidate_by_skills
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    """Главная страница"""
    candidates: list[dict] = get_all_candidates()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:idx>')
def page_candidate(idx):
    """Поиск кандидата"""
    candidate: dict = get_candidate_by_id(idx)
    if not candidate:
        return "Кандидат не найден"
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_page_candidate(candidate_name):
    """Поиск кандидата"""
    candidates: list[dict] = get_candidate_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)

@app.route('/skill/<candidate_skill>')
def search_candidates_skills(candidate_skill):
    """Поиск кандидата"""
    candidates: list[dict] = get_candidate_by_skills(candidate_skill)
    return render_template('skill.html', candidates=candidates)

app.run()

