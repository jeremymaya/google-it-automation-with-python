def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    # Removes puntuations while normalizing the letters into lower case and create a list of words
    no_puntuations = ""
    for char in file_contents:
        if char not in punctuations:
            no_puntuations += char.lower()
    words = no_puntuations.split()
    
    # Iterates through the uninteresting_words to create a set of uninteresting words for faster search later
    uninteresting_words_set = set()
    for word in uninteresting_words:
        if word not in uninteresting_words_set:
            uninteresting_words_set.add(word)
    
    # Iterates through the words to create a dictionary of words and their frequency while excluding uninteresting words
    words_dictionary = {}
    for word in words:
        if word not in words_dictionary and word not in uninteresting_words_set:
            words_dictionary[word] = 0
        if word in words_dictionary and word not in uninteresting_words_set:
            words_dictionary[word] += 1
    return words_dictionary

file_contents = "This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever.  You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org"

print(calculate_frequencies(file_contents))