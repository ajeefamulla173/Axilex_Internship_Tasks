data = {
    "python": "Programming language",
    "ai": "Artificial Intelligence",
    "ml": "Machine Learning"
}

word = input("Enter word to search: ").lower()

if word in data:
    print("Meaning:", data[word])
else:
    print("Word not found.")
