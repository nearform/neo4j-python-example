from models import Person, Movie


# Find the actor named "Tom Hanks"...
tom_hanks = Person.nodes.get(name="Tom Hanks")
print('Find the actor named "Tom Hanks"...')
print(tom_hanks)
print()

# Find the movie with title "Cloud Atlas"...
cloud_atlas_movie = Movie.nodes.get(title="Cloud Atlas")
print('Find the movie with title "Cloud Atlas"...')
print(cloud_atlas_movie)
print()

# Find 10 people...
people_names = [person.name for person in Person.nodes[:10]]
print("Find 10 people...")
print(people_names)
print()


# Find movies released in the 1990s...
nineties_movies_titles = [
    movie.title for movie in Movie.nodes.filter(released__gte=1990, released__lt=2000)
]
print("Find movies released in the 1990s...")
print(nineties_movies_titles)
