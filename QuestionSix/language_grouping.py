from collections import Counter

languages = [['English'], ['English'], [], ['English'], ['English'], [], ['English'], [], [], [], ['English'], ['English'], ['English'], [], ['English'], ['zbMATH Open Web Interface contents unavailable due to conflicting licenses.'], [], ['zbMATH Open Web Interface contents unavailable due to conflicting licenses.'], ['English'], ['zbMATH Open Web Interface contents unavailable due to conflicting licenses.'], [], ['English'], [], ['English'], ['English'], ['English'], [], ['English'], ['English'], ['English'], ['English'], [], ['English'], [], ['English'], ['English'], ['English'], ['English'], ['English'], [], [], [], ['English'], [], ['English'], [], [], ['English'], ['zbMATH Open Web Interface contents unavailable due to conflicting licenses.'], ['English'], [], [], ['English'], ['English'], ['English'], ['English'], ['English'], ['English'], ['English'], ['English'], ['English'], ['English'], [], ['English'], ['English'], [], [], ['English'], ['English'], ['English'], ['English'], ['English'], ['German'], ['English'], ['English'], ['zbMATH Open Web Interface contents unavailable due to conflicting licenses.'], ['English'], ['English'], ['English'], ['English'], ['English'], [], ['English'], [], [], ['English'], [], ['English'], ['English'], [], ['English'], ['English'], ['English'], [], ['English'], ['English'], ['zbMATH Open Web Interface contents unavailable due to conflicting licenses.'], ['English'], [], ['English']]

# Filter out empty lists and specific unwanted strings
filtered_languages = [lang[0] for lang in languages if lang and lang[0] != "zbMATH Open Web Interface contents unavailable due to conflicting licenses."]

# Count occurrences of each language
language_counter = Counter(filtered_languages)

# Print the counts for each language
for language, count in language_counter.items():
    print(f"{language}: {count}")
