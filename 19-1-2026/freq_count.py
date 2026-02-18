# we are using hashing to calculate frequence of each element and then going to return high and low frequency element.
# diff bt dict and hashmap in python -> 
    # you can use string index into hashmap/hashtable.
    # Hashtable/hashmap is internal data structure while dictonary is a pyhon specific implementaion of hashtable.

from collections import defaultdict


arr = [1,2,3,1,23,12,4,4,233,12,2,3,3,3,3,33]
freq=defaultdict(int)
for i in arr:
    freq[i]+=1

high=0
high_val=0
low=max
for key in freq:
    if(high<freq[key]):
        high=freq[key]
        high_val=key
        
print(high)
print(high_val)