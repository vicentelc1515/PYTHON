# faz uma analise do site
import request
from bs4 import BeautifulSoup
import operator
from collections import Counter # manipulação de listas, tuplas etc

def start (url):

    wordlist=[] # todo o conteudo do site vem pra cá
    source_code = resquest.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser') # faz a requisição dos dados do site e transforma em html

    for each_text in soup.find.All('div',{'class': 'entry-content''})
        content = each_text.text # pega tudo que tem div ou class e vai pegar o que existe de conteudo, e vai transformar em string
        
        words= content.lower().split() # cada conteudo será uma linha
        
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)
        
        
    def clean_wordlist(wordlist):
        clean_list = []
        for word in wordlist:
            symbols = '!@#$%¨&*()_-+<>:;^}~?°?{[ªº]}].+-*/\|'
            # romevendo simbolos indesejados
            for i in range(0, len(symbols)):
                word = word.replace(symbols[i], '')
                
            if len (word) > 0:
                clean_list.append(word)
        create_dictionary(clean_list)
        
        
def create_dictionary(clean_list):
# cria um dicionario de palavras e as mais utlizadas no site
    word_count = {}
    
    for word in clean_list:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1
            
            
            
    for key, value in sorted(word_count.items(),key = operator.itemgetter(1)):
        print("% S : % S " % (Key, value))
        # contador de palavras
    c = Counter(word_count)
    top = c.most_common(10)
    print(top)
    
    
    
if __name__ == '__main__':
start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")