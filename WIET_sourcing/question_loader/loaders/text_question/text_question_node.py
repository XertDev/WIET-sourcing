import graphene


class TextQuestionNode(graphene.ObjectType):
	multi_answer = graphene.Boolean()
	question = graphene.String()
	answers = graphene.List(graphene.String)
	submitted_answers = graphene.List(graphene.Int)
