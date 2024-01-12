from models import Person, Movie
from neomodel import db
from neomodel.exceptions import DoesNotExist


# List all Tom Hanks movies...
# MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(tomHanksMovies) RETURN tom,tomHanksMovies
# Fetch the 'Person' node for Tom Hanks
tom_hanks = Person.nodes.get(name="Tom Hanks")

# Fetch all the 'Movie' nodes related to Tom Hanks via the 'ACTED_IN' relationship
tom_hanks_movies = tom_hanks.acted_in.all()
print("List all Tom Hanks movies...")
print(tom_hanks_movies)
print()

# Who directed "Cloud Atlas"?
# MATCH (cloudAtlas {title: "Cloud Atlas"})<-[:DIRECTED]-(directors) RETURN directors.name
print('Who directed "Cloud Atlas"?')
# Fetch the 'Movie' node for "Cloud Atlas"
cloud_atlas = Movie.nodes.get(title="Cloud Atlas")
# Fetch all the 'Person' nodes related to "Cloud Atlas" via the 'DIRECTED' relationship
directors_of_cloud_atlas = cloud_atlas.directors.all()
# Extract the names of the directors
print(directors_of_cloud_atlas)
print()

# Tom Hanks' co-actors...
# MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors) RETURN coActors.name
print("Tom Hanks' co-actors...")
# Fetch the 'Person' node for Tom Hanks
tom_hanks = Person.nodes.get(name="Tom Hanks")
# Initialize an empty set to hold unique co-actor names
co_actors_names = set()
# Loop through each movie Tom Hanks acted in
for movie in tom_hanks.acted_in.all():
    # For each movie, find all actors who are not Tom Hanks
    for co_actor in movie.actors:
        if co_actor.name != "Tom Hanks":
            co_actors_names.add(co_actor.name)

# Convert the set to a list to remove duplicated
co_actors_names = list(co_actors_names)
print(co_actors_names)
print()

# Version fetching relations
co_actors_names = set()
for _, _, _, co_actor, _ in (
    Person.nodes.filter(name="Tom Hanks").fetch_relations("acted_in__actors").all()
):
    co_actors_names.add(co_actor.name)
print(list(co_actors_names))
print()

# Version with custom query
query = """
MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors)
RETURN coActors
"""

# Execute the raw Cypher query
results, _ = db.cypher_query(query)

# Inflate results into Person objects
co_actors_names = set()
for record in results:
    # Extract node id
    node_id = record[0].element_id
    try:
        # Inflate node into a Person object
        co_actor = Person.inflate(record[0])
        co_actors_names.add(co_actor.name)
    except DoesNotExist:
        # Handle the case where the node does not exist
        print(f"Node with id {node_id} does not exist")
print(list(co_actors_names))
print()


# Version with custom query and self inflate
co_actors_names = tom_hanks.co_actors_names()
print(co_actors_names)
print()

# How people are related to "Cloud Atlas"...
# MATCH (people:Person)-[relatedTo]-(:Movie {title: "Cloud Atlas"}) RETURN people.name, Type(relatedTo), relatedTo
print('How people are related to "Cloud Atlas"...')
# Fetch the 'Movie' node for "Cloud Atlas"
cloud_atlas = Movie.nodes.get(title="Cloud Atlas")

# Initialize a list to hold the results
results = []

# Check all possible relationships defined in your NeoModel
for relation in [
    cloud_atlas.actors,
    cloud_atlas.directors,
    cloud_atlas.producers,
    cloud_atlas.reviewers,
    cloud_atlas.writers,
]:
    for person in relation.all():
        # Fetch the relationship instance
        rel_instance = relation.relationship(person)

        # Append the person's name, relationship type, and relationship properties
        results.append(
            (
                person.name,
                relation.definition["relation_type"],
                rel_instance.__properties__,
            )
        )
print(results)
print()
