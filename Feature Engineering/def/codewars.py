## 1
  def spin_words(sentence):
      res=[]

      for w in sentence.split():
          if len(w)>=5:
              res.append(w[::-1])
          else:
              res.append(w)
    return ' '.join(str(x) for x in res)
  
  def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
  
## 2 Jaden Casing Strings
  def to_jaden_case(string):
    return ' '.join(x.capitalize() for x in string.split() ) 
  
## 3 Descending Order
  def Descending_Order(num):
    return int(''.join((sorted(str(num)))[::-1]))
  
## 4 Replace With Alphabet Position
  import re
  def alphabet_position(text):
      text=text.lower()
      if bool(re.match('[0-9]',text))==True:
          return ''
      else:
          listc='abcdefghijklmnopqrstuvwxyz'
          lista=[]
          for k in range(0,len(text)):
              for i in range(26):
                  if text[k]== listc[i]:

                      lista.append(i+1)
          return ' '.join(str(x) for x in lista)  
      
  def alphabet_position(s):
    return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())
      
## 5 Get the Middle Character
def get_middle(s):
    if len(s)%2==1:
        return s[int((len(s)-1)/2)]
    elif len(s)%2==0:
        return ''.join(s[i] for i in range(int(len(s)/2)-1,int(len(s)/2+1)))
      
 def get_middle(s):
    return s[(len(s)-1)//2:len(s)//2+1]
  
## 6 Convert string to camel case
def to_camel_case(s):
    return s[0] + s.title().replace("-",'').replace('_','')[1:] if s else s
  
# 7 Moving Zeros To The End
def move_zeros(array):
    list1=[]
    list2=[]
    for i in array:
        if i!=0:
            list1.append(i)
        elif i==0:
            list2.append(i)
    
    return list1+list2

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

# 8 Multiples of 3 or 5
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# 9 Human Readable Time
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

# 10 Build Tower
def tower_builder(n_floors):
    return [' '*(n_floors-i-1)+'*'*(i*2+1)+' '*(n_floors-i-1) for i in range(n_floors)]

def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]


