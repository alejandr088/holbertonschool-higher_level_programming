#!/usr/bin/python3
"""
function that indent input text
"""


def text_indentation(text):
    """
    defined function text_indentatin
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text = text.replace('.', '.\n\n').replace('?', '?\n\n') \
               .replace(':', ':\n\n')
    lines = text.split('\n')
    result = '\n'.join(line.strip() for line in lines)
    print(result, end="")
