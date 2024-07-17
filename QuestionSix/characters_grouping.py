from collections import Counter

categories = ['j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', None, 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'a', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'j', 'b', 'b', 'j', 'j', 'j', 'j', 'j', 'a', 'j', 'a', 'j', 'j', 'j', 'j', 'j', 'a', 'j', 'j', 'j', 'j', 'a', 'j', 'j', None, 'a', 'j', 'j', 'j', 'j', 'j', 'a', 'j', 'j', 'a', 'j', 'j', 'j', 'j', 'j', 'j', 'j', None, 'j', 'a', 'j', 'j', 'j', 'j', 'j', None, 'j', 'j', 'j', 'j', None, 'a', 'j']

# Extract the first character from each category and count occurrences
first_letters_counter = Counter([category[0].lower() for category in categories if category is not None])

# Output the counts for each letter
for letter, count in first_letters_counter.items():
    if count > 0:
        print(f"{letter}: {count}")
