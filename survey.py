"""testing classes in python"""


class AnonymousSurvey:
    """collects anonymous answer to a survey question"""

    """defining the attributes of the class"""
    def __init__(self, question):
        """store a question and prepare to store response"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """stor a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """show all responses that has been given"""
        print("Survey responds:")
        for response in self.responses:
            print(f"-{response}")