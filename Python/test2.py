# Answer 2

def highest_frequency_length(input_string):
    word_freq = {}
    max_frequency = 0
    words = input_string.split()

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
        max_frequency = max(max_frequency, word_freq[word])
        
    highest_frequency_word_length = max(len(word) for word in word_freq if word_freq[word] == max_frequency)

    return highest_frequency_word_length

# Example input string
input_string = "this this is is ineuron ineuron assessment assessment assessment"

# Example output
output = highest_frequency_length(input_string)
print("Length of the highest-frequency word:", output)  # Output: 10 And the word assessment has the heighest frequrmcy is 3 and so its length == 10.
