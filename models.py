class Poll:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    @classmethod
    def get_all(cls):
        return [
            Poll('Example', ['a', 'b', 'c'])
        ]
