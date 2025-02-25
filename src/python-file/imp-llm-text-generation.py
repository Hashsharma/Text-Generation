from transformers import pipeline

model_path = "../../models/"
nlp = pipeline(
    "document-question-answering",
    model=model_path,
)

ans = nlp(
    "../resource/Screenshot 2025-02-25 201713.png",
    "What is dot?"
)

print(ans)
