def clean_feedback(feedback):
    feedback = feedback.strip()
    feedback = " ".join(feedback.split())
    return feedback


def count_words(feedback):
    return len(feedback.split())


def count_characters(feedback):
    return len(feedback)


def find_keywords(feedback):

    feedback = feedback.lower()

    good = feedback.count("good")
    bad = feedback.count("bad")
    excellent = feedback.count("excellent")

    return good, bad, excellent


def generate_summary(feedback):

    feedback = clean_feedback(feedback)

    good, bad, excellent = find_keywords(feedback)

    print("Words:", count_words(feedback))
    print("Characters:", count_characters(feedback))
    print("Excellent:", excellent)
    print("Good:", good)
    print("Bad:", bad)


feedback = input("Enter feedback: ")

generate_summary(feedback)
