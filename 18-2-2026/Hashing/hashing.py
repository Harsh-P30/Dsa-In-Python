

# diff bt dict and hashmap in python -> 
    # you can use string index into hashmap/hashtable.
    # Hashtable/hashmap is internal data structure while dictonary is a pyhon specific implementaion of hashtable.

# ord(): Return the Unicode code point for a one-character string.(Ascii value)
def get_hash(key):
    h=0
    for i in key:
        h+=ord(i)       
    return h%10

print(get_hash('world'))
    
    
class HashTable:
    def __init__(self):
        self.Max=10
        self.arr=[None for i in range(self.Max)]
    
    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h % self.Max
    
HashTable.get_hash('5','va')