#def reverse_dict(old_dic):
#    new_dict = {old_dic[k]: kIGNORECASE for k in old_dic}
#    return new_dict


#word_len = {word: len(word) for word in 'Алиса в стране чудес'.split()}

#len(word) = reverse_dict(word_len)

#print(len_word)



#def greetings():
#    user_name = input("Как вас зовут? ")
#    print('Hello, {}!'.format(user_name))

#greetings()


import re

def get_data(filename):
    raw = ''
    with open(filename) as f:
        raw = f.read
    print(raw[:50])
    return(raw)

def preprocess(text):
    
    
