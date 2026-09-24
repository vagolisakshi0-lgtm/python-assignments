def clean_message(message):
    message = message.strip()
    message = " ".join(message.split())
    return message


def is_question(message):
    return message.endswith("?")


def count_words(message):
    return len(message.split())


def detect_keyword(message):

    message_lower = message.lower()

    keywords = ["order", "payment", "delivery", "refund", "help"]

    for keyword in keywords:
        if keyword in message_lower:
            return keyword

    return "No keyword"


def generate_response_type(message):

    keyword = detect_keyword(message)

    if is_question(message):
        response_type = "Question"
    else:
        response_type = "Statement"

    print("Clean Message:", message)
    print("Type:", response_type)
    print("Words:", count_words(message))
    print("Keyword Detected:", keyword)


message = input("Enter message: ")

message = clean_message(message)

generate_response_type(message)
