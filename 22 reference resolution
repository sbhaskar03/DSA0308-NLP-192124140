def resolve_references(text):
    entities = {}
    resolved_text = ""

    for word in text.split():
        if word.endswith(":"):
            entity_name = word[:-1]
            entities[entity_name] = resolved_text
            resolved_text += entity_name + ":"
        elif word.startswith("@"):
            reference = word[1:]
            if reference in entities:
                resolved_text += entities[reference] + " "
            else:
                resolved_text += word + " "
        else:
            resolved_text += word + " "

    return resolved_text.strip()

# Example usage
text = """
Alice: Alice went to the park. Bob saw her at the park.
Bob: Bob also saw Charlie there. Charlie was with his dog.
@Alice: She was playing with her dog.
@Bob: Bob greeted her.
"""

resolved_text = resolve_references(text)
print(resolved_text)
