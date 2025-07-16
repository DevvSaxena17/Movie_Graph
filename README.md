# Movie Graph Explorer

A beginner-friendly Python app to explore movies, actors, and genres using Neo4j.

Neo4j Desktop Screenshot:

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/83f4545f-89f7-4e56-afd8-34b8f8f86f58" />

Query Tool Screenshot:

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/dd3d7254-0469-4ada-b830-2e8bb5144272" />

## Features
- Explore movies, actors, and genres in a Neo4j graph database
- Find all movies featuring a specific actor
- List genres shared by multiple movies
- Interactive command-line interface
- Robust error handling and user-friendly output

## Project Summary
Movie Graph Explorer is a Python-based tool that demonstrates the power of graph databases for movie data exploration. It leverages Neo4j to model complex relationships between movies, actors, and genres, and provides an interactive interface for querying the data. This project highlights skills in Python, Cypher, data modeling, and professional software documentation.

## Project Structure
- `data/` — Sample data files (CSV, JSON, etc.)
- `scripts/` — Python scripts to interact with Neo4j
- `schema/` — Cypher queries for schema and data
- `screenshots/` — Project screenshots and visualizations

## Requirements
- Python 3.x
- Neo4j Desktop (recommended) or Neo4j Aura (free tier)
- Install all dependencies:
  ```sh
  pip install -r scripts/requirements.txt
  ```

## Environment Variables
- Create a `.env` file in the project root with:
  ```
  NEO4J_URI=bolt://localhost:7687
  NEO4J_USER=neo4j
  NEO4J_PASSWORD=your_password_here
  ```

## Data and Schema
- `/data/` — For sample data files (CSV, JSON, etc.)
- `/schema/` — Contains `create_schema.cypher` and `sample_data.cypher` (famous movies/actors)

## Loading Sample Data
- To load the famous movies/actors dataset, open `schema/sample_data.cypher` in Neo4j Desktop's Query tool and run it.

## Testing Your Setup
- Run the test script to verify your connection:
  ```sh
  python scripts/test_connection.py
  ```

## Example Queries Performed by the Script
- Find all movies featuring Leonardo DiCaprio
- List genres shared by multiple movies

## Troubleshooting
- **Cannot connect to Neo4j:** Ensure your database is running and the URI, username, and password are correct.
- **No results or warnings about missing labels:** Make sure you have loaded the movie dataset as described above.
- **APOC errors:** The provided setup does not require APOC. All data is loaded via Cypher script.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
