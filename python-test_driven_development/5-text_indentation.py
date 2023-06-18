#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text = text.replace('.', '.\n\n').replace \
        ('?', '?\n\n').replace(':', ':\n\n')
    lines = text.split('\n')
    result = '\n'.join(line.strip() for line in lines)
    print(result, end="")
