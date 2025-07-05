class Quiz:
    def __init__(self, questions, category, answers):
        self.questions = questions
        self.category = category
        self.answers = answers
        self.score = 0

    def start(self):
        self.score
        for index, line in enumerate(self.questions):
            answer = input(f" {line}\n").strip().lower()
            if answer == self.answers[index].strip():
                self.score += 1
        print(f"Your final Score is {self.score}")


with open("./questions.txt", "r") as questions, open("./FormAnswer.txt") as answers:
    questionList = questions.readlines()
    answersList = answers.readlines()
    print(answersList)
    print(questionList)
    print(len(questionList))
    print(len(answersList))
    if len(questionList) != len(answersList):
        print("Your question list and answer list is not equal")
    else:
        quizGame = Quiz(questionList, "Finance", answersList)
        quizGame.start()
