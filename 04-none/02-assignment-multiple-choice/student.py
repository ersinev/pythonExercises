def multiple_choice(right_answer, given_answer):
    points = 0

    if(given_answer):
        if(right_answer is given_answer):
            points = points + 1
        else:
            points = points - 0.2


    return points