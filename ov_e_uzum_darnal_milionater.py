import random;
questions = [
        "What is capital of Armenia:?Yerevan,Pekin,Gyumri,Buenos Aires",
        "What is capital of France:?Paris,Erevan,Gyumri,London",
        "What is capital of China:?Pekin,Paris,Pekin,Tbilisi",
        "What is capital of USA:?Washington,Paris,Pekin,London",
        "What is capital of Brazil:?Brazil,Washington,Pekin,Brazil",
        "What is capital of Georgia:?Tbilisi,Washington,Lisbon,Brazil",
        "What is capital of Germany:?Berlin,Erevan,Lisbon,Roma",
        "What is capital of Austria:?Vienna,Erevan,Lisbon,Roma",
        "What is capital of Italy:?Roma,Washington,Lisbon,Brazil",
        "What is capital of Spain:?Madrid,Paris,Madrid,London",   
        "What is capital of United Kingdom:?London,Erevan,Madrid,Lisbon",
        "What is capital of Italy:?Roma,Washington,Madrid,Tbilisi",
        "What is capital of UAE:?Abu Dhabi,Washington,Gyumri,Tbilisi",
        "What is capital of Portugaly:?Lisbon,Washington,Gyumri,Buenos Aires",
        "What is capital of Argentina:?Buenos Aires,Washington,Gyumri,Buenos Aires",
]

def choose_10_questions(questions):
    tmp = []
    while len(tmp) < 10:
        num = random.randint(0, len(questions) - 1)
        if questions[num] not in tmp:
            tmp.append(questions[num])
    return tmp


def gquestions(tmp):
    gquestion = []
    for el in tmp:
        q, a = el.split("?")
        gquestion.append((q.strip(), a.split(',')))
    return gquestion


def shuffle_print(gquestion):
    count = 0
    for q, a_list in gquestion:
        print(q)
        correct = a_list[0].strip()
        random.shuffle(a_list)
        for i, el in enumerate(a_list, start=1):
            print(f"{i}. {el.strip()}")
        answer = input('Enter your answer: ').strip()
        if answer.lower() == correct.lower():
            print('Correct')
            count += 1
        else:
            print('Incorrect, the correct answer was', correct)
    return 'You got %d/10' % count



    


def main():
    quest = choose_10_questions(questions)
    gquest = gquestions(quest)
    game = shuffle_print(gquest)
    return game
    

print(main())


