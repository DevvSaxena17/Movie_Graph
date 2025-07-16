import os
from neo4j import GraphDatabase
from pyvis.network import Network

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
query = '''
MATCH (a:Actor)-[:ACTED_IN]->(m:Movie)-[:IN_GENRE]->(g:Genre)
RETURN a.name AS actor, m.title AS movie, g.name AS genre
LIMIT 100
'''
nodes = set()
edges = []
with driver.session() as session:
    for record in session.run(query):
        actor = record['actor']
        movie = record['movie']
        genre = record['genre']
        nodes.add(('actor', actor))
        nodes.add(('movie', movie))
        nodes.add(('genre', genre))
        edges.append((actor, movie, 'ACTED_IN'))
        edges.append((movie, genre, 'IN_GENRE'))
driver.close()
net = Network(height='700px', width='100%', notebook=False)
for ntype, name in nodes:
    if ntype == 'actor':
        net.add_node(name, label=name, color='lightblue', shape='dot')
    elif ntype == 'movie':
        net.add_node(name, label=name, color='orange', shape='box')
    elif ntype == 'genre':
        net.add_node(name, label=name, color='lightgreen', shape='ellipse')
for src, dst, rel in edges:
    net.add_edge(src, dst, label=rel)
net.show('movie_graph.html')
print('Graph visualization saved as movie_graph.html') 