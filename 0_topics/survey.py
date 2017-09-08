# Anonymous survey class


class AnonymousSurvey():
    """Collects a survey stuff"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """Definition"""
        print(self.question)

    def store_response(self, response):
        """store a response"""
        self.responses.append(response)

    def show_results(self):
        """Definition"""
        print("Survey results:")
        for r in self.responses:
            print("- {}".format(r))
