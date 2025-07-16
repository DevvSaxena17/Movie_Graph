// Create constraints
CREATE CONSTRAINT ON (m:Movie) ASSERT m.title IS UNIQUE;
CREATE CONSTRAINT ON (a:Actor) ASSERT a.name IS UNIQUE;
CREATE CONSTRAINT ON (g:Genre) ASSERT g.name IS UNIQUE;

// Sample Movies
CREATE (m1:Movie {title: 'Inception', year: 2010});
CREATE (m2:Movie {title: 'The Revenant', year: 2015});
CREATE (m3:Movie {title: 'Titanic', year: 1997});
CREATE (m4:Movie {title: 'The Wolf of Wall Street', year: 2013});

// Sample Actors
CREATE (a1:Actor {name: 'Leonardo DiCaprio'});
CREATE (a2:Actor {name: 'Kate Winslet'});
CREATE (a3:Actor {name: 'Tom Hardy'});
CREATE (a4:Actor {name: 'Joseph Gordon-Levitt'});

// Sample Genres
CREATE (g1:Genre {name: 'Drama'});
CREATE (g2:Genre {name: 'Thriller'});
CREATE (g3:Genre {name: 'Romance'});
CREATE (g4:Genre {name: 'Crime'});

// Relationships
// Inception
MATCH (m:Movie {title: 'Inception'}), (a:Actor {name: 'Leonardo DiCaprio'}) CREATE (a)-[:ACTED_IN]->(m);
MATCH (m:Movie {title: 'Inception'}), (a:Actor {name: 'Joseph Gordon-Levitt'}) CREATE (a)-[:ACTED_IN]->(m);
MATCH (m:Movie {title: 'Inception'}), (g:Genre {name: 'Thriller'}) CREATE (m)-[:IN_GENRE]->(g);
MATCH (m:Movie {title: 'Inception'}), (g:Genre {name: 'Drama'}) CREATE (m)-[:IN_GENRE]->(g);
// The Revenant
MATCH (m:Movie {title: 'The Revenant'}), (a:Actor {name: 'Leonardo DiCaprio'}) CREATE (a)-[:ACTED_IN]->(m);
MATCH (m:Movie {title: 'The Revenant'}), (a:Actor {name: 'Tom Hardy'}) CREATE (a)-[:ACTED_IN]->(m);
MATCH (m:Movie {title: 'The Revenant'}), (g:Genre {name: 'Drama'}) CREATE (m)-[:IN_GENRE]->(g);
// Titanic
MATCH (m:Movie {title: 'Titanic'}), (a:Actor {name: 'Leonardo DiCaprio'}) CREATE (a)-[:ACTED_IN]->(m);
MATCH (m:Movie {title: 'Titanic'}), (a:Actor {name: 'Kate Winslet'}) CREATE (a)-[:ACTED_IN]->(m);
MATCH (m:Movie {title: 'Titanic'}), (g:Genre {name: 'Romance'}) CREATE (m)-[:IN_GENRE]->(g);
MATCH (m:Movie {title: 'Titanic'}), (g:Genre {name: 'Drama'}) CREATE (m)-[:IN_GENRE]->(g);
// The Wolf of Wall Street
MATCH (m:Movie {title: 'The Wolf of Wall Street'}), (a:Actor {name: 'Leonardo DiCaprio'}) CREATE (a)-[:ACTED_IN]->(m);
MATCH (m:Movie {title: 'The Wolf of Wall Street'}), (g:Genre {name: 'Crime'}) CREATE (m)-[:IN_GENRE]->(g);
MATCH (m:Movie {title: 'The Wolf of Wall Street'}), (g:Genre {name: 'Drama'}) CREATE (m)-[:IN_GENRE]->(g); 