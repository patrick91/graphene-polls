from collections import namedtuple

import graphene

import pprint

Poll = namedtuple('Poll', ['title', 'questions'])

POLLS = [
    Poll('Example', ['a', 'b', 'c'])
]


class PollObjectType(graphene.ObjectType):
    title = graphene.String()
    questions = graphene.List(graphene.String)


class Query(graphene.ObjectType):
    polls = graphene.List(PollObjectType)

    def resolve_polls(self, info):
        return POLLS


schema = graphene.Schema(query=Query)

r = schema.execute('{ polls { title, questions } }')

pprint.pprint(r.errors, indent=4)
pprint.pprint(r.data, indent=4)
