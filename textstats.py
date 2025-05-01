
def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def counter(text):
    text = text.lower()
    counts = {}
    for c in text:
        if c in counts:
            counts[c] = counts[c] + 1
        else:
            counts[c] = 1
    return counts

def create_character_reports(char_counts):
    filtered = []
    for char, count in char_counts.items():
        if char.isalpha():
            filtered.append({'char': char, 'num': count})

    filtered.sort(key=lambda x: -x['num'])

    return filtered
