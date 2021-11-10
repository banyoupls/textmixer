import random

file = open("m.txt",encoding='utf-8')
m = file.read().split("\n")
file.close()


#создаёт все возможные варианты модифицации текста (лучше использовать одно слово)
def mixer(text):
 def add(w,s):
  l = []
  for i in m:
   if s in i:
    for ii in list(i):
     l.append(w+ii)
    break
  if len(l) == 0:
   return [w+s]
  return l

 l = [""]
 for i in list(text):
  l2 = []
  for ii in l:
   l2 += add(ii,i)
  l = l2
 return l


#рандомная замена, один вариант
def mixer_1(text):
 r = []
 for s in list(text):
  k = len(r)
  for i in m:
   if s in i:
    r.append(random.choice(list(i)))
    break
  if len(r) == k:
   r.append(s)
 return "".join(r)



print(mixer("tgs"))
print(mixer_1("Немного текста, Some text"))