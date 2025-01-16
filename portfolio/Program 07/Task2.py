#Write and test three functions that each take two words (strings) as parameters and return sorted lists (as defined above) representing respectively: Letters that appear in at least one of the two words. 
#Letters that appear in both words. 
# Letters that appear in either word, but not in both.
# Hint: These could all be done programmatically, but consider carefully what topic we have been discussing this week! Each function can be exactly one line.

def union_letters(word1, word2):
    return sorted(set(word1) | set(word2))  # Letters that appear in at least one word

def intersection_letters(word1, word2):
    return sorted(set(word1) & set(word2))  # Letters that appear in both words

def difference_letters(word1, word2):
    return sorted(set(word1) ^ set(word2))  # Letters that appear in either word, but not both

# User input
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

print("Union:", union_letters(word1, word2))  
print("Intersection:", intersection_letters(word1, word2)) 
print("Difference:", difference_letters(word1, word2))  