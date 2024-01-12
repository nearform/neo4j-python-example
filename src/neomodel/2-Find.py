from models import Person, Movie


# Find the actor named "Tom Hanks"...
# MATCH (tom {name: "Tom Hanks"}) RETURN tom
tom_hanks = Person.nodes.get(name="Tom Hanks")
print('Find the actor named "Tom Hanks"...')
print(tom_hanks)
print()

# Find the movie with title "Cloud Atlas"...
# MATCH (cloudAtlas {title: "Cloud Atlas"}) RETURN cloudAtlas
cloud_atlas_movie = Movie.nodes.get(title="Cloud Atlas")
print('Find the movie with title "Cloud Atlas"...')
print(cloud_atlas_movie)
print()

# Find 10 people...
# MATCH (people:Person) RETURN people.name LIMIT 10
people_names = [person.name for person in Person.nodes[:10]]
print("Find 10 people...")
print(people_names)
print()


# Find movies released in the 1990s...
# MATCH (nineties:Movie) WHERE nineties.released >= 1990 AND nineties.released < 2000 RETURN nineties.title
nineties_movies_titles = [
    movie.title for movie in Movie.nodes.filter(released__gte=1990, released__lt=2000)
]
print("Find movies released in the 1990s...")
print(nineties_movies_titles)
