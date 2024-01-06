from models import Person, Movie

# Retrieve all Person nodes
all_persons = Person.nodes.all()

# Retrieve all Movie nodes
all_movies = Movie.nodes.all()

# You can then iterate over these lists to access individual nodes
for person in all_persons:
    print("Deleting person:", person.name)
    person.delete()

for movie in all_movies:
    print("Deleting movie:", movie.title)
    movie.delete()
