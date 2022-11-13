import re
import string


def count_me():
    freq = {} #to store the word and its corresponding word count
    
    file_obj = open('count.txt', 'r')
    word_content = file_obj.read().lower() #turn all the words in our document to lowercase 
    
    reg_exp = re.findall(r'\b[a-z]{3,15}\b', word_content)
    
    
    for word in reg_exp:
        count = freq.get(word, 0) #count the frequency for words present in our document
        freq[word] = count + 1
        
        freq_list = freq.keys()
        
        for word in freq_list:
            print word, freq[word]
            
            if __name__ == '__main__':
                count_me()