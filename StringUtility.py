class StringUtility:
  def __init__(self, string):
   self.string = string
  #The __init__() takes a string as a parameter an ores it as an instance variable.
 #All methods will operate on this string, but only return a modified copy of the altered string. You should not overwrite the original string.


  def __str__(self):
   return self.string
  
  def vowels(self):
    '''returns the count of vowels in a string as a string, prints many if it has 5 or more, arugument and return type is string'''
    vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
    word = list(self.string)
    x = 0
    for char in word:
      if char in vowel_list:
       x+=1
    if x >= 5:
     x = "many"
       
    return str(x)
    
  def bothEnds(self):
    '''returns a string of the first 2 and last characters of string, if it is less than 2 characters it returns the string itself. Argument and parameter type is string'''
    word = list(self.string)
    if len(word)> 2:
     word = word[:2] + word[-2:]
    else:
     word = []
 
    return "".join(word)


     
  def fixStart(self):
    '''Returns a string with the intances of the first letter changed to *, except the first. Argument and parameter type is string'''
    if len(list(self.string))<= 1:
     actualword = self.string
    else:
     word = self.string
     firstchar = word[0]
     firstword = word.replace(word[0],"*")
     actualword = firstchar + firstword[1:] 
    return actualword

  def asciiSum(self):
   '''returns the sum of all acsii value in a string. Paremeter type is string and return type is interger'''
   sum = 0
   for i in self.string:
     sum += ord(i)
   return sum

  def cipher(self):
   '''returns and encoded string that is incremented by the length of that string. Paramter and return type is string'''
   x = ""
   for i in self.string:
     if i ==' ':
       ord_value = ord(i)
     if i.islower():
      ord_value = ord(i) + len(self.string)
      while ord_value > ord('z'):
       ord_value -= 26
     elif i.isupper():
       ord_value = ord(i)+len(self.string)
       while ord_value > ord("Z"):
         ord_value-=26
     x += chr(ord_value)
   return x
     
   
     
    
  

  

