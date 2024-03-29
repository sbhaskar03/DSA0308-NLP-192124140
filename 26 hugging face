from transformers import MarianMTModel, MarianTokenizer


model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_to_french(english_text):

    inputs = tokenizer(english_text, return_tensors="pt", padding=True, truncation=True)


    outputs = model.generate(**inputs)


    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translated_text


english_text = "Hello, how are you?"
french_translation = translate_to_french(english_text)
print("English Text:", english_text)
print("French Translation:", french_translation)
