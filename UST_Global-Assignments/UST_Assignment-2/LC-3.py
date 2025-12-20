# Write a list comprehension to extract all words 
# that are longer than 4 characters from a sentence.

s= " Dancing in the dark listening to my favourite song"

l=s.split(" ")
rl=[i for i in l if len(i)>4]
print(rl)