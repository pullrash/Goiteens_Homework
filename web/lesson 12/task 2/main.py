import random
from flask import Flask, render_template, abort, redirect, url_for

app = Flask(__name__)

MOVIES = {
    1: {"title": "Інтерстеллар", "desc": "Науково-фантастичний фильм про подорожі крізь червоточину."},
    2: {"title": "Початок", "desc": "Професійний злодій краде секрети з глибин підсвідомості під час сну."},
    3: {"title": "Темний лицар", "desc": "Бетмен піднімає ставки у боротьбі з хаотичним Джокером."},
    4: {"title": "Матриця", "desc": "Хакер дізнається від повстанців про справжню природу його реальності."}
}

@app.route('/')
def index():
    return render_template('index.html', movies=MOVIES)

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    if movie_id not in MOVIES:
        abort(404)
    return render_template('movie.html', movie=MOVIES[movie_id])

@app.route('/random')
def random_movie():
    random_id = random.choice(list(MOVIES.keys()))
    return redirect(url_for('movie_detail', movie_id=random_id))

@app.errorhandler(404)
def page_not_found():
    return "<h1>404 — Фільм не знайдено!</h1><p>Такого фільму в нашій базі немає.</p><a href='/'>На головну</a>", 404

if __name__ == '__main__':
    app.run(debug=True)