with open('./questions.txt','r') as questions:
    for line in  questions.readlines():
        answer=input(f' {line}\n')
        with open ('./FormAnswer.txt','a') as answers:
            answers.write(f' {answer}\n')

            