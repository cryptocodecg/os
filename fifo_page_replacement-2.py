# -*- coding: utf-8 -*-
"""FIFO-page-replacement.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZnPIAaEgUI1efrGOhmpL5A638LxgI3f3
"""

# Python3 implementation of FIFO page 
# replacement in Operating Systems. 
from queue import Queue  
  
# Function to find page faults using FIFO  
def pageFaults(pages, n, capacity): 
      
    # To represent set of current pages.  
    # We use an unordered_set so that we 
    # quickly check if a page is present 
    # in set or not  
    s = set()  
  
    # To store the pages in FIFO manner  
    indexes = Queue()  
  
    # Start from initial page  
    page_faults = 0
    for i in range(n): 
          
        # Check if the set can hold  
        # more pages  
        if (len(s) < capacity): 
              
            # Insert it into set if not present  
            # already which represents page fault  
            if (pages[i] not in s): 
                s.add(pages[i])  
  
                # increment page fault  
                #page_faults += 1
  
                # Push the current page into 
                # the queue  
                indexes.put(pages[i]) 
  
        # If the set is full then need to perform FIFO  
        # i.e. remove the first page of the queue from  
        # set and queue both and insert the current page  
        else: 
              
            # Check if current page is not  
            # already present in the set  
            if (pages[i] not in s): 
                  
                # Pop the first page from the queue  
                val = indexes.queue[0]  
  
                indexes.get()  
  
                # Remove the indexes page  
                s.remove(val)  
  
                # insert the current page  
                s.add(pages[i])  
  
                # push the current page into  
                # the queue  
                indexes.put(pages[i])  
  
                # Increment page faults  
                page_faults += 1
  
    return page_faults 
  
# Driver code  
if __name__ == '__main__': 
#    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]  
#    pages = [0, 2, 1, 6, 4, 0, 1, 0, 3, 1, 2, 1]
    pages = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
    n = len(pages)  
    capacity = 4
    print(pageFaults(pages, n, capacity))

#pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]  
pages = [0, 2, 1, 6, 4, 0, 1, 0, 3, 1, 2, 1]
#pages = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
stack = []

n = len(pages)    #the length of the pages stream
capacity = 4      #the capacity of the stack

count = 0         #count the index for replacement
fault = 0
for i in range(len(pages)):
  if len(stack) < capacity:
    if pages[i] not in stack:
      print(pages[i], "fault")
      stack.append(pages[i])
      fault = fault + 1
  else:
    if pages[i] in stack:
      print(pages[i], "hit")
    else:
      print(pages[i], "fault")
      print("count = " + str(count))
      stack[count] = pages[i]
      count = count + 1
      fault = fault + 1
      if count == capacity:
        count = 0
      
  print(stack)

print("fault: ", fault)
print("failure rate: ", fault/len(pages))