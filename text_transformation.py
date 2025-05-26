from collections import Counter
# 🧵 Python Text Transformation Toolkit
print("🧠 Welcome to the Text Transformation Toolkit!")
text = input("Enter text: ")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")

command = int(input("Choose number: "))
reversed_text = ""
vowel_counter = 0

if command == 1:
    for letter in text[::-1]:
        reversed_text += letter
    print(reversed_text)
elif command == 2:
    text = text.upper()
    print(text)
elif command == 3:
    text = text.lower()
    print(text)
elif command == 4:
    text = text.title()
    print(text)
elif command == 5:
    for letter in text:
        if letter in "aeyuio":
            vowel_counter+=1
    print(f"{vowel_counter} vowels found!")
elif command == 6:
    text = text.replace(" ", "")
    print(text)
elif command == 7:
    for i in text:
        if i in "aeyuio":
            text = text.replace(i,"*")
    print(text)
elif command == 8:
    for letter in text[::-1]:
        reversed_text += letter
    if reversed_text == text:
        print(f"{text} - is palindrome")
    else:
        print(f"{text} - is not palindrome")
elif command == 9:
    print(Counter(text.split()))
else:
    print("❌ Invalid choice! Please restart the program.")
