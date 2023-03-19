#!/usr/bin/env python
# coding: utf-8

# In[3]:


############# Python Basic Code #############


# In[11]:


# Single line execution = Ctrl + enter
# Multiple line execution = Shift + enter
# Making comments = # or Ctrl + /

Help() # call documentation for functions, modules, etc.
dir() # call valid attributions of the object


# In[59]:


############# Allocation of elements ############
val = 1           # put integer element into 'val' 
val2 = 'Python'   # put string element into 'val2' 
val3 = True       # put boolean element into 'val3'
val4 = 2.3        # put decimal element into 'val4'


# In[60]:


print(val)
print(val2)
print(val3)
print(val4)


# In[33]:


# Show all registered elements
get_ipython().run_line_magic('whos', '')


# In[101]:


############# Operators ############
1+2       # add
2-1       # subtract
2*2       # multiply
2**3      # Square
13/2      # classic division (with decimal value)
13//2     # floor division   (without decimal value)
13%2      # remainder


# In[79]:


# Data properties
print('type=', type(val2))
print('identity=', id(val2))
print('length=', len(val2))


# In[115]:


############# tuple date ############
tuple = ("python",10,1.2,5,4,3,2) 
print(tuple)

tuple2 = tuple + ("club", True)
print(tuple2)


# In[118]:


# call index in tuple data (from 0 to n-1/ reverse from -n to -1)
tuple[0]    # same as tuple[-3]
tuple[1]    # same as tuple[-2]
tuple[2]    # same as tuple[-1]


# In[121]:


# tuple slicing (from 0 : n-1)
tuple[0:3]


# In[124]:


# tuple nesting
character = (5,2,("men","women"),(6,4))
print(character)


# In[190]:


character[2]       # Nested elements are indexed together
character[2][1]    # Call second element in the third nested index
character[2][1][0] # Call first caracter in the second element in the third nested index


# In[194]:


# tuple data sorting
num = (10,4,3,5,7)
numsor = sorted(num)
print(numsor)


# In[184]:


########### List data ###########   
# List data is mutable, while tuple data is unmutable
# All codes are the same as tuple data

list = ["name",1889,[3,'a'],[4,'b']]
print(list)


# In[185]:


list.extend(["region",10])  # Adding each element (in this case, 2 new elements)
print(list)


# In[186]:


list.append(["region",10])  # Adding one indexed element (in this case, 1 indexed element)
print(list)


# In[187]:


#list mutating
list[0] = "last name"    # change element 0 of list as 'last name'
print(list)


# In[188]:


# list data deleting
del(list[0])
print(list)


# In[175]:


# list data split
"A,B,C,D".split(",")   #split by comma, space


# In[178]:


# list data aliasing   (IMPORTANT! Difference from R code !!!!!)
A = ["pan","table",112]
B = A                    # B has the same and linked elements of A
B[0] = "PAAAAN"          # If the element of B is changed, the element of A will also changed

print(A)
print(B)


# In[189]:


# list data copying     (IMPORTANT! Difference from R code !!!!!)
A = ["pan","table",112]
C = A[:]                 # C has the copy elements of A
C[0] = "PAAAAN"          # If the element of C is changed, the element of A will not be changed

print(A)
print(C)


# In[196]:


########## Dictionaries data ##########
# dictionaries consist of the 'keys' and 'values' 
# The keys are immutable 

dic = {"key1" : "Jane", "key2":1933, "key3":"Korea", "Key4":[75,4,36]}
print(dic)


# In[202]:


# indexing value using key
dic['key1']


# In[206]:


# adding new key and value
dic["key5"]=(5,5,5)
print(dic)


# In[207]:


# deleting key and value
del(dic["key5"])
print(dic)


# In[212]:


# find keys
'key1' in dic


# In[215]:


# find all keys
dic.keys()


# In[217]:


# find all values
dic.values()


# In[226]:


########## Set data ##########
# Set do not record element position
# Set has a particular element (duplicated items are not presented)
# Set is ordered

set1 = {"Jane", "Jane", "Jane", "seoul", 10,5,3}
print(set)


# In[235]:


# Adding set items
set1.add("Korea")
print(set1)


# In[236]:


# Deleting set items
set1.remove("Korea")
print(set1)


# In[254]:


# Find set items
"seoul" in set1


# In[255]:


# print set1 and set2
set2 = {"Gray", "seoul", 1167,1144,3535}
set1,set2     


# In[259]:


# Find intersection between set1 and set2
print(set1&set2)
set1.intersection(set2)


# In[250]:


# Find difference

set1.difference(set2) #different set1 items from set2


# In[242]:


# Union of multiple set items .union (involving all items in multiple sets)

set1.union(set2)


# In[260]:


# Check subset (set2 is subset of set1?)
set2.issubset(set1)     


# In[261]:


# Check superset (set2 is superset of set1?)
set2.issuperset(set1)

