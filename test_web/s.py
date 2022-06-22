import string
def wave(people):
    
    result = []
    for i,value in enumerate(people):
     if value in string.ascii_letters:
      
      temp = list(people.lower())
      temp[i] = temp[i].upper()
      result.append("".join(e for e in temp))
    # Code here
    return result
    
print(wave("Hello"))
    # Code here

    
