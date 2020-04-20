letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def word_multiset(word):
    dict = { l:0 for l in letters }
    for l in word:
      dict[l] += 1
    return list(dict.values())
def test_anagram(word1, word2):
    return word_multiset(word1) == word_multiset(word2)
def get_all_anagrams(word, word_list):
    return list(filter(lambda x: test_anagram(word, x), word_list))