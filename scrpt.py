def duplicate_count(text):
    text = text.lower()  # Convert the input text to lowercase
    count = 0  # Initialize the count of duplicates
    unique_chars = set()  # Set to store unique characters
    duplicates = set()  # Set to store duplicate characters

    for char in text:
        if char in unique_chars:
            duplicates.add(char)
        else:
            unique_chars.add(char)

    count = len(duplicates)
    return count
