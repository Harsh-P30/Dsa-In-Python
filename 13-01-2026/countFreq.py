# Count frequency of each element in the array
from collections import defaultdict
arr=[1,2,1,2,1,2,16,4,5,1,5,61,1,2,1]

# Create a defaultdict to store frequency of each element
freq_map = defaultdict(int)

for num in arr:
    freq_map[num]+=1

for key in freq_map:
    print("value - ",key,":","freq - ",freq_map[key])
    
# The defaultdict(int) auto-initializes missing keys to 0, so freq_map[num] += 1 safely increments the count for each element encountered. Element 1 appears 6 times in the array.