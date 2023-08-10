def findMostCommonPrefix(strs: 'list'=[]) -> 'str':
    """Find most common prefix from a list of strings. Function accepts empty values"""
    prefix_dict = {} # stores prefix as key and count of repetitions as value

    for words in strs: #iterate through list
        x = 0 # setting counter to iterate through words in list
        while x < len(words) - 1:
            word_prefix = words[:-x] if x > 0 else words # slice of prefix
            if prefix_dict.get(word_prefix): # update to dictionary based on prefix and repetition
                prefix_dict[word_prefix] = prefix_dict.get(word_prefix) + 1
            else:
                prefix_dict[word_prefix] = 1

            x += 1

    result = prefix_dict.values() # finding max value of prefix repetition

    if result and max(result) > 1:
        final = [item for item in [i for i in prefix_dict if prefix_dict[i] == max(result)]][0]
    else:
        final = ""

    print(f"Most common prefix is: {final}") if final else print("No common prefix found")


findMostCommonPrefix(['hey', 'heya', 'heyo', 'flight', 'flower', 'flow', 'flawless'])
# findMostCommonPrefix(['','',''])
# findMostCommonPrefix(['hey','hey','hey'])
# findMostCommonPrefix(['','hey','hi','hi'])