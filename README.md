# madlib-cli

**A madlib is a story that you fill in the details of as you go. Once you select a file, you'll be prompted with a series of words to fill in. Once you've finished, you'll be presented with your completed story!**

This is a simple python script that parses user input into a template. It can accept new text file templates in the madlib_cli/assets folder, formatted with the mutable user inputs in curly brackets, for example:
`The {Noun} is {adjective} because the {Noun} {Verb, past tense}`
The mutables can be any string, they just have to be contained in curly brackets, and any number of mutables and story sections can be added. Curly brackets cannot be used except to denotate mutables.
It has simple input validation and a numeric menu for selecting files. It is designed to be run as a script.
