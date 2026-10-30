### Problem Statement

Given an input text paragraph, normalize all letters to lowercase, remove punctuation, and extract words using basic string and list operations. Track the occurrence count of each word alongside its 0-indexed positions within the tokenized sequence. Identify and display all words that appear more than once, listing their total count and exact positional indices.

---

### Algorithm

1. Read the input paragraph string.
2. Initialize an empty string for cleaned text.
3. Iterate through each character in the paragraph:
* If the character is alphanumeric, convert it to lowercase and append it to the cleaned text.
* If the character is a whitespace, append a single space.
* Otherwise, replace punctuation or symbols with a space.


4. Split the cleaned text by whitespace into a list of words.
5. Initialize empty lists to track unique words, their frequencies, and their position lists.
6. Iterate through the tokenized list using indices from `0` to `len(words) - 1`:
* If the word exists in the unique words list:
* Find its index in the unique words list.
* Increment its frequency counter by 1.
* Append the current token index to its position list.


* If the word does not exist:
* Append the word to the unique words list.
* Append `1` to the frequency list.
* Append a new list containing the current token index to the positions list.




7. Iterate through the recorded words and filter those with a frequency greater than 1.
8. Output the repeated words along with their counts and positions.

---

### Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Read Input Paragraph/]
    B --> C[Initialize clean_text = '']
    C --> D[Normalize Case & Replace Punctuation with Space]
    D --> E[Split clean_text into words list]
    E --> F[Initialize unique_words = [], counts = [], positions = []]
    F --> G[Iterate through words with index i]
    G --> H{Is words[i] in unique_words?}
    H -- Yes --> I[Find index pos in unique_words]
    I --> J[counts[pos] += 1]
    J --> K[positions[pos].append i]
    H -- No --> L[Append words[i] to unique_words]
    L --> M[Append 1 to counts]
    M --> N[Append [i] to positions]
    K --> O{More words?}
    N --> O
    O -- Yes --> G
    O -- No --> P[Filter items where counts > 1]
    P --> Q[/Display Repeated Words, Counts, and Positions/]
    Q --> R([End])

```

---

### Python Source Code

```python
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

```

---

### Sample Input

```text
The cat chased the mouse, but the cat was too slow to catch the mouse.

```

---

### Sample Output

```text
Word: 'the', Count: 4, Positions: [0, 3, 6, 12]
Word: 'cat', Count: 2, Positions: [1, 7]
Word: 'mouse', Count: 2, Positions: [4, 13]

```
