def anagrammes(str1, str2):

    if len(str1) != len(str2):
        return False
    
  
    return sorted(str1) == sorted(str2)


print(anagrammes("tame", "meta")) 
print(anagrammes("tame", "mate"))  
print(anagrammes("tame", "team"))  
print(anagrammes("tabby", "batty"))  
print(anagrammes("python", "java")) 
