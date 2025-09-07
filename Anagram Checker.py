def if_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

#Test Case
print(if_anagram("war", "raw"))

#Test Case 2
print(if_anagram("elbow","below"))
       