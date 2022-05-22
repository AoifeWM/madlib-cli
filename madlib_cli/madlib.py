import re


def read_template(filepath):
    print(filepath)
    with open(filepath) as template:
        stripped = template.read()
    print(stripped)
    return stripped


def parse_template(raw_template):
    temp_list = re.split(r"[{}]", raw_template)
    noninputs = []
    inputs = []
    print(temp_list)
    # Loop assumes that temp_list begins with a NON-INPUT (ie. not in curly brackets). If this is not the case, the
    # count must be offset by one so that the function works properly:
    if raw_template[0] == "{":
        temp_list.insert(0, "")
    # Because of the way it's split, the every other index is assumed an input, beginning with a non-input. See above
    for chunk in temp_list:
        if temp_list.index(chunk) % 2 == 1:
            inputs.append(chunk)
        else:
            noninputs.append(chunk)
    print(inputs)
    print(noninputs)
    # Re concatenate the noninputs list into a string with {} in every other position. I'd rather just keep it as a list
    # and wait to concatenate the final string until the user sends inputs, but we're supposed to use the string.format
    # method, so I have to do it this way
    cleaned_template = ""
    for chunk in range(len(noninputs)):
        cleaned_template += noninputs[chunk]
        # prevents the {} from being added to the string at the final position
        if chunk < len(inputs):
            cleaned_template += "{}"
    return cleaned_template, tuple(inputs)






def merge(cleaned_template, input_types):

    for item in input_types:
        x=1;





parse_template(read_template("assets/dark_and_stormy_night_template.txt"))
