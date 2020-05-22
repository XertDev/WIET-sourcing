import graphene
from graphene import relay
from graphene_sqlalchemy_filter import FilterSet

from WIET_sourcing.models.question_set import QuestionSet
from WIET_sourcing.schemes.question_set.question_set_node import QuestionSetNode


class QuestionSetConnection(relay.Connection):
    total_count = graphene.Int()

    class Meta:
        node = QuestionSetNode

    def resolve_total_count(self, info):
        return self.iterable.count()


class QuestionSetFilter(FilterSet):
    class Meta:
        model = QuestionSet
        fields = {
            "name": ["eq", "ne", "in", "like", "ilike"],
            "creation_date": [...],
            "close_date": [...],
        }
