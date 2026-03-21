# Day 5

# Function for String Analysis
def string_analyzer():
    print("\n🔤 String Analyzer")

    text = input("Enter a word or sentence: ")

    # Basic operations
    print("\n--- Result ---")
    print("Original Text:", text)
    print("Length:", len(text))
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())

    # Vowel count
    vowels = "aeiou"
    count = 0

    for ch in text.lower():
        if ch in vowels:
            count += 1

    print("Vowel Count:", count)


# Loop to repeat
while True:
    string_analyzer()

    choice = input("\nDo you want to try again? (yes/no): ")
    if choice.lower() != "yes":
        print("Thank you! 👋")
        break
