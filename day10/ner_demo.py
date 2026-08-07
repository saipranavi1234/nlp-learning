import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

text = "Sundar Pichai is the CEO of Google and lives in California."

doc = nlp(text)

print("Named Entities:\n")

for entity in doc.ents:
    print(f"{entity.text} --> {entity.label_}")