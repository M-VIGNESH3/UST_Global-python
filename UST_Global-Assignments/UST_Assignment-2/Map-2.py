# How would you use the map() function to convert 
# all string elements of a list to uppercase?


l=["one","two","three"]
print("Original list: ",l)
nl= map(lambda i:i.upper(),l)
print( "Modified list: ",list(nl))