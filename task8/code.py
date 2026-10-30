import string

def detect_repeated_words(paragraph):
    cleaned = ""
    for char in paragraph:
        if char.isalnum():
            cleaned += char.lower()
        else:
            cleaned += " "
            
    tokens = [word for word in cleaned.split(" ") if word != ""]
    
    unique_words = []
    counts = []
    positions = []
    
    for idx in range(len(tokens)):
        word = tokens[idx]
        if word in unique_words:
            w_idx = unique_words.index(word)
            counts[w_idx] += 1
            positions[w_idx].append(idx)
        else:
            unique_words.append(word)
            counts.append(1)
            positions.append([idx])
            
    repeated = []
    for i in range(len(unique_words)):
        if counts[i] > 1:
            repeated.append({
                "word": unique_words[i],
                "count": counts[i],
                "positions": positions[i]
            })
            
    return repeated

text = input()
results = detect_repeated_words(text)

for item in results:
    print(f"Word: '{item['word']}', Count: {item['count']}, Positions: {item['positions']}")
