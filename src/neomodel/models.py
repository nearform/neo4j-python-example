from neomodel import (
    IntegerProperty,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    StructuredRel,
)


class ActedIn(StructuredRel):
    roles = StringProperty()


class Review(StructuredRel):
    summary = StringProperty()
    rating = IntegerProperty()


class Person(StructuredNode):
    name = StringProperty(unique_index=True)
    born = IntegerProperty()

    acted_in = RelationshipTo("Movie", "ACTED_IN", model=ActedIn)
    directed = RelationshipTo("Movie", "DIRECTED")
    produced = RelationshipTo("Movie", "PRODUCED")
    reviewed = RelationshipTo("Movie", "REVIEWED", model=Review)
    wrote = RelationshipTo("Movie", "WROTE")
    follows = RelationshipTo("Person", "FOLLOWS")


class Movie(StructuredNode):
    title = StringProperty(unique_index=True)
    released = IntegerProperty()
    tagline = StringProperty()

    actors = RelationshipTo("Person", "ACTED_IN", model=ActedIn)
    directors = RelationshipTo("Person", "DIRECTED")
    producers = RelationshipTo("Person", "PRODUCED")
    reviewers = RelationshipTo("Person", "REVIEWED", model=Review)
    writers = RelationshipTo("Person", "WROTE")
