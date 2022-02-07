"""importing fron our survey class"""

from survey import AnonymousSurvey
# define a question and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#show the questions and store response to the question
my_survey.show_question()
print("enter 'q' at anytime to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
