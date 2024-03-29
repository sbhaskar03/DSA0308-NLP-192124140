import nltk

def recognize_dialog_acts(dialog):
    dialog_acts = []

    for utterance in dialog:
        tokens = nltk.word_tokenize(utterance)
        tagged_tokens = nltk.pos_tag(tokens)

        if "?" in utterance:
            dialog_acts.append("question")
        elif utterance.endswith(("!", ".", "...")):
            dialog_acts.append("statement")
        elif any(tag.startswith("VB") for _, tag in tagged_tokens):
            dialog_acts.append("request")
        else:
            dialog_acts.append("other")

    return dialog_acts


dialog = [
    "Hello, how are you?",
    "I'm doing well, thanks!",
    "Could you pass me the salt, please?",
    "Sure, here you go.",
    "What do you think about the weather today?"
]

dialog_acts = recognize_dialog_acts(dialog)
for i, act in enumerate(dialog_acts, 1):
    print(f"Utterance {i}: {dialog[i-1]} --> Dialog act: {act}")
