# 3-Given a list of words, create a dictionary where the keys are the words and the values are the number of times they appear.
word_list=["jose","jose","jose","juan","juan","luis"]
word_dictionary ={}

for key_word in word_list:
    if key_word in word_dictionary:
        word_dictionary[key_word]=word_dictionary[key_word]+1
    else:
        word_dictionary[key_word] = 1
        
print(word_dictionary)