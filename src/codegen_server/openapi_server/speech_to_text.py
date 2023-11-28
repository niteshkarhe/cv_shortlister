def compare(expected_answer, actual_answer):
    expected_answer_words = expected_answer.split()
    actual_answer_words = actual_answer.split()

    if expected_answer in actual_answer:
        return 100
    else:
        return 0