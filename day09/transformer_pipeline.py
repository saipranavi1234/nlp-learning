# Hugging Face Transformer Pipeline Demo

from transformers import pipeline


# Sentiment Analysis
classifier = pipeline("sentiment-analysis")

text = "I love learning Natural Language Processing"

result = classifier(text)

print("Sentiment Result:")
print(result)


# Named Entity Recognition

ner = pipeline("ner", grouped_entities=True)

sentence = "Apple was founded by Steve Jobs in California"

entities = ner(sentence)

print("\nNamed Entities:")
print(entities)


# Text Generation

generator = pipeline("text-generation")

output = generator(
    "Artificial Intelligence is",
    max_length=50
)

print("\nGenerated Text:")
print(output)