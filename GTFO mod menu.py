from transformers import pipeline

# Create a question-answering pipeline
qa_pipeline = pipeline("question-answering")

# Define your question
question = "What is the capital of France?"

# Use the pipeline to get the answer
answer = qa_pipeline(question=question)

# Print the answer
print(answer["answer"])