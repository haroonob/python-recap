def get_user_input():
    """
    Prompts the user to enter a noun, verb, and adjective for the story.

    Returns:
        tuple: A tuple containing the user's noun, verb, and adjective input.
    """
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    return noun, verb, adjective


def create_story(noun, verb, adjective):
    """
    Fills in the blanks in the story using the user's input.

    Args:
        noun (str): A noun provided by the user.
        verb (str): A verb provided by the user.
        adjective (str): An adjective provided by the user.

    Returns:
        str: The complete story with user-provided words.
    """
    story = (
        f"Once upon a time, there was a {adjective} {noun} that loved to {verb}."
        " Every day, it would wander through the fields, bringing joy and laughter to everyone it met."
        " People would gather to watch, amazed by the {adjective} {noun}'s wonderful skill to {verb}."
    )
    return story


# Main program execution
if __name__ == "__main__":
    noun, verb, adjective = get_user_input()
    completed_story = create_story(noun, verb, adjective)
    print("\nHere's your story:")
    print(completed_story)
