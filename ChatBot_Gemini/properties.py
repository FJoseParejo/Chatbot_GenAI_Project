import textwrap


def to_markdown(text):
    text = text.replace("•", "  *")
    return textwrap.indent(text, "-->", predicate=lambda _: True) # Predicate is a parameter that in itself is a function that decides whether a line should be indented or not; 
    # with the lambda function whose parameter is _, and always True, we ensure that all lines (-->) will be identified at the beginning of each line break.
