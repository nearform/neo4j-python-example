from neomodel import (
    IntegerProperty,
    RelationshipTo,
    RelationshipFrom,
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
    followed_by = RelationshipFrom("Person", "FOLLOWS")

    def co_actors_names(self):
        results, _ = self.cypher(
            "MATCH (a:Person) WHERE elementId(a)=$self MATCH (a)-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors) RETURN coActors"
        )
        return list(set([self.inflate(row[0]).name for row in results]))


class Movie(StructuredNode):
    title = StringProperty(unique_index=True)
    released = IntegerProperty()
    tagline = StringProperty()

    actors = RelationshipFrom("Person", "ACTED_IN", model=ActedIn)
    directors = RelationshipFrom("Person", "DIRECTED")
    producers = RelationshipFrom("Person", "PRODUCED")
    reviewers = RelationshipFrom("Person", "REVIEWED", model=Review)
    writers = RelationshipFrom("Person", "WROTE")
