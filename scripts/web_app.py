import os
from flask import Flask, render_template_string, request
from neo4j import GraphDatabase

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

app = Flask(__name__)

def get_driver():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

@app.route('/', methods=['GET', 'POST'])
def index():
    movies = []
    actor = ''
    if request.method == 'POST':
        actor = request.form.get('actor', '').strip()
        if actor:
            query = (
                "MATCH (a:Actor {name: $actor_name})-[:ACTED_IN]->(m:Movie) "
                "RETURN m.title AS title, m.year AS year"
            )
            with get_driver().session() as session:
                movies = [record for record in session.run(query, actor_name=actor)]
    return render_template_string('''
        <h2>Movie Graph Explorer (Web)</h2>
        <form method="post">
            <input name="actor" placeholder="Enter actor name" value="{{actor}}" required>
            <button type="submit">Search</button>
        </form>
        {% if movies %}
            <h3>Movies featuring {{actor}}:</h3>
            <ul>
            {% for m in movies %}
                <li>{{m['title']}} ({{m['year']}})</li>
            {% endfor %}
            </ul>
        {% elif actor %}
            <p>No movies found for actor: {{actor}}</p>
        {% endif %}
        <hr>
        <a href="/genres">View shared genres</a>
    ''', movies=movies, actor=actor)

@app.route('/genres')
def genres():
    query = (
        "MATCH (m:Movie)-[:IN_GENRE]->(g:Genre)<-[:IN_GENRE]-(other:Movie) "
        "WHERE m <> other "
        "RETURN g.name AS genre, collect(DISTINCT m.title) AS movies "
        "ORDER BY genre"
    )
    with get_driver().session() as session:
        genres = [record for record in session.run(query)]
    return render_template_string('''
        <h2>Genres shared by multiple movies</h2>
        {% if genres %}
            <ul>
            {% for g in genres %}
                <li><b>{{g['genre']}}</b>: {{g['movies']|join(', ')}}</li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No shared genres found.</p>
        {% endif %}
        <a href="/">Back to search</a>
    ''', genres=genres)

if __name__ == '__main__':
    app.run(debug=True) 