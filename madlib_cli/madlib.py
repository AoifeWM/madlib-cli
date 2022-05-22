import re
import glob


# Given a filepath open a file, read it and write the contents to a variable, close the file, and return the variable
def read_template(filepath):
    with open(filepath) as template:
        stripped = template.read()
    return stripped


def parse_template(raw_template):
    # Split a stripped template into a list based on curly brackets. By splitting this way every other index is an input
    # and every other index is a non-input (i.e. a story element that surrounds the user's inputs to make the story)
    temp_list = re.split(r"[{}]", raw_template)
    # Set up holding arrays
    noninputs = []
    inputs = []

    # The for-loop below assumes that temp_list begins with a NON-INPUT (i.e. not in curly brackets). If this is not
    # the case, which we can detect by checking if the first character of the template is a curly bracket,
    # then we must insert a blank index so that the next function works properly:
    if raw_template[0] == "{":
        temp_list.insert(0, "")

    # Because of the way it's split, the every other index is assumed an input, beginning with a non-input. See above
    for chunk in temp_list:
        if temp_list.index(chunk) % 2 == 1:
            inputs.append(chunk)
        else:
            noninputs.append(chunk)

    # Re-concatenate the noninputs list into a string with {} between each index. I'd rather just keep it as a list
    # and wait to concatenate the final string until the user sends inputs, but we're supposed to use the
    # string.format method, so I have to do it this way.
    cleaned_template = ""
    for chunk in range(len(noninputs)):
        # Add the current index of noninputs to the concatenated string
        cleaned_template += noninputs[chunk]

        # if-statement prevents the {} from being added to the string at the final position if there isn't really one
        # there by checking the length of inputs (allowing it to function properly regardless of whether the final index
        # of the original split template list is an input or not)
        if chunk < len(inputs):
            # Add the {} between each index to the concatenated string
            cleaned_template += "{}"

    return cleaned_template, tuple(inputs)


def merge(cleaned_template, input_types):
    user_input = []
    for item in input_types:
        if re.match(r"[aeiouAEIOU]", item):
            user_item = str(input("Enter an " + item + ": "))
        else:
            user_item = str(input("Enter a " + item + ": "))
        user_input.append(user_item)
    return cleaned_template.format(*user_input)


def welcome_menu():
    # Use glob to make a list with all the filenames available in assets. Save it as variable "assets" because we'll
    # use it a lot later.
    # (thanks to https://pynative.com/python-glob/ for explaining how glob works)
    assets = glob.glob("assets/*")

    # Print menu screen
    print("--------------------------------------------")
    print("Welcome to my madlib command line interface!")
    print("--------------------------------------------\n\n")
    print("A madlib is a story that you fill in the de-")
    print("tails of as you go. Once you select a file, ")
    print("you'll be prompted with a series of words to")
    print("fill in. Once you've finished, you'll be ")
    print("presented with your completed story! \n\n")

    # Don't break the loop until the user selects a valid template
    valid_selection = False
    while not valid_selection:
        print("To continue, please select a file from the")
        print("list:")
        print("--------------------------------------------")
        for template in assets:
            # Putting [7:-4] after the template cuts off the "assets/" at the start and the ".txt" at the end for better
            # readability.
            print(str(assets.index(template)+1) + ": " + template[7:-4])
        print("--------------------------------------------")
        selection = None
        # Loop until valid selection is made
        while selection is None:
            try:
                # Subtract 1 so that counting numbers (1, 2, 3) are converted to indexes properly (0, 1, 2) when we use
                # selection later to reference indexes in the assets list
                selection = int(input("Please select a number: ")) - 1
                # Assert this selection is in range
                assert selection < len(assets)
            # ValueError will catch if the input can't be made into an int
            except (AssertionError, ValueError):
                print("Invalid input!")
                # Reset selection to none so this keeps looping (no valid input yet)
                selection = None

        # Not strictly necessary because "assert selection < len(assets)" above should catch this. However, just in case
        # the file has been moved or something, we'll double-check that we can access it before we proceed.
        try:
            read_template(assets[selection])
            # At this point the file must be readable, so we break from the enclosing while loop.
            valid_selection = True
        # if the file isn't readable:
        except FileNotFoundError as e:
            print("\nFile not found! Please try again.\n\n")
        # Just in case something goes really wrong, the program can keep running.
        except Exception as e:
            print("Unexpected error! " + type(e) + ": " + str(e))

    # Valid selection has been made, confirm the selection to user in the readable format as explained above ("[7:-4]")
    print("You selected " + assets[selection][7:-4] + "!\nProcessing story...\n\n")
    # Store the parsed template to feed to merge function
    a, b = parse_template(read_template(assets[selection]))
    # Get user input, etc.
    completed_story = merge(a, b)
    print("\n\nYour MadLib is ready!")
    print("--------------------------------------------")
    print(assets[selection][7:-4])
    print("\n" + completed_story)


# Make sure the menu loads when run as a script.
if __name__ == "__main__":
    welcome_menu()