from neomodel import db

# Delete all nodes at once
query = "MATCH (n) DETACH DELETE n"
results, meta = db.cypher_query(query)
