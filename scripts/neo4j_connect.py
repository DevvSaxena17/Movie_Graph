# Movie Graph Explorer
# This script allows you to explore the movie graph database using Neo4j.
# It provides functionality to find movies featuring a specific actor and list genres shared by multiple movies.
# Author: Devv Saxena
# Date: 2024-07-16

import os
from neo4j import GraphDatabase
from typing import List, Dict

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

class MovieGraphExplorer:
    def __init__(self, uri: str, user: str, password: str):
        try:
            self.driver = GraphDatabase.driver(uri, auth=(user, password))
        except Exception as e:
            print(f"Error connecting to Neo4j: {e}")
            raise
    def close(self):
        self.driver.close()
    def find_movies_by_actor(self, actor_name: str) -> List[Dict]:
        query = (
            "MATCH (a:Actor {name: $actor_name})-[:ACTED_IN]->(m:Movie) "
            "RETURN m.title AS title, m.year AS year"
        )
        try:
            with self.driver.session() as session:
                result = session.run(query, actor_name=actor_name)
                return [record for record in result]
        except Exception as e:
            print(f"Query error: {e}")
            return []
    def list_shared_genres(self) -> List[Dict]:
        query = (
            "MATCH (m:Movie)-[:IN_GENRE]->(g:Genre)<-[:IN_GENRE]-(other:Movie) "
            "WHERE m <> other "
            "RETURN g.name AS genre, collect(DISTINCT m.title) AS movies "
            "ORDER BY genre"
        )
        try:
            with self.driver.session() as session:
                result = session.run(query)
                return [record for record in result]
        except Exception as e:
            print(f"Query error: {e}")
            return []
if __name__ == "__main__":
    explorer = MovieGraphExplorer(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
    print("\n=== Movie Graph Explorer ===\n")
    actor = input("Enter actor name to search for movies (e.g., Leonardo DiCaprio): ").strip()
    movies = explorer.find_movies_by_actor(actor)
    if movies:
        print(f"\nMovies featuring {actor}:")
        for record in movies:
            print(f"- {record['title']} ({record['year']})")
    else:
        print(f"\nNo movies found for actor: {actor}")
    print("\nGenres shared by multiple movies:")
    genres = explorer.list_shared_genres()
    if genres:
        for record in genres:
            print(f"- {record['genre']}: {', '.join(record['movies'])}")
    else:
        print("No shared genres found.")
    explorer.close() 