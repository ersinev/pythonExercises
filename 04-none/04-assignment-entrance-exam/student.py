def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    taken_test = 0
    skipped_tests = 0
    total_grade = 0

    if(grade1 is None):
        skipped_tests = skipped_tests + 1
    else:
        taken_test = taken_test + 1
        total_grade = total_grade + grade1    

    if(grade2 is None):
        skipped_tests = skipped_tests + 1
    else:
        taken_test = taken_test + 1
        total_grade = total_grade + grade2

    if(grade3 is None):
        skipped_tests = skipped_tests + 1
    else:
        taken_test = taken_test + 1
        total_grade = total_grade + grade3

    if(grade4 is None):
        skipped_tests = skipped_tests + 1
    else:
        taken_test = taken_test + 1
        total_grade = total_grade + grade4

    if(grade5 is None):
        skipped_tests = skipped_tests + 1
    else:
        taken_test = taken_test + 1
        total_grade = total_grade + grade5

    if(taken_test == 0):
        return False        

    avarage = total_grade/taken_test        

    return(skipped_tests<=1 and avarage>=12 )        
