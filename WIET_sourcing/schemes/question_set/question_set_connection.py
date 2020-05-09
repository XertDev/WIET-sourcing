from graphene import relay
from graphene_sqlalchemy_filter import FilterSet

from WIET_sourcing.models.question_set import QuestionSet
from WIET_sourcing.schemes.question_set.question_set_node import QuestionSetNode


class QuestionSetConnection(relay.Connection):
    class Meta:
        node = QuestionSetNode


class QuestionSetFilter(FilterSet):
    class Meta:
        model = QuestionSet
        fields = {
            "name": ["eq", "ne", "in", "like", "ilike"],
            "creation_date": [...],
            "close_date": [...],
        }
