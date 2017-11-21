import graphene

import pprint

from models import Poll


class PollObjectType(graphene.ObjectType):
    title = graphene.String()
    questions = graphene.List(graphene.String)


class Query(graphene.ObjectType):
    polls = graphene.List(PollObjectType)

    def resolve_polls(self, info):
        return Poll.get_all()


schema = graphene.Schema(query=Query)

result = schema.execute('{ polls { title, questions } }')

pprint.pprint(result.errors, indent=4)
pprint.pprint(result.data, indent=4)
