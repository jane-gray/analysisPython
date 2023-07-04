{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6c0baf42-caf4-4be8-ac3b-b43fa6e63eb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "############# Python Basic Code #############"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "10be03d5-abcb-41a8-956d-9675af710229",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Single line execution = Ctrl + enter\n",
    "# Multiple line execution = Shift + enter\n",
    "# Making comments = # or Ctrl + /\n",
    "\n",
    "Help() # call documentation for functions, modules, etc.\n",
    "dir() # call valid attributions of the object"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "fa708779-4dca-4f3e-97fe-9f49e2e0dac4",
   "metadata": {},
   "outputs": [],
   "source": [
    "############# Allocation of elements ############\n",
    "val = 1           # put integer element into 'val' \n",
    "val2 = 'Python'   # put string element into 'val2' \n",
    "val3 = True       # put boolean element into 'val3'\n",
    "val4 = 2.3        # put decimal element into 'val4'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "57c05d28-42be-4608-93fb-91ce2aaa81aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "Python\n",
      "True\n",
      "2.3\n"
     ]
    }
   ],
   "source": [
    "print(val)\n",
    "print(val2)\n",
    "print(val3)\n",
    "print(val4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "8343a4dd-eca3-4b53-a10e-4122cf1267ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable   Type     Data/Info\n",
      "-----------------------------\n",
      "val        int      1\n",
      "val2       str      Python\n",
      "val3       bool     True\n",
      "val4       float    2.3\n"
     ]
    }
   ],
   "source": [
    "# Show all registered elements\n",
    "%whos             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "8654c5b9-a8da-4700-9358-bc8159d48a26",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "############# Operators ############\n",
    "1+2       # add\n",
    "2-1       # subtract\n",
    "2*2       # multiply\n",
    "2**3      # Square\n",
    "13/2      # classic division (with decimal value)\n",
    "13//2     # floor division   (without decimal value)\n",
    "13%2      # remainder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "9cdd9fb1-7058-4ddb-814a-23821880310a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "type= <class 'str'>\n",
      "identity= 140172727740592\n",
      "length= 6\n"
     ]
    }
   ],
   "source": [
    "# Data properties\n",
    "print('type=', type(val2))\n",
    "print('identity=', id(val2))\n",
    "print('length=', len(val2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "6f685cb3-f0a7-4b83-b065-6d491a21899b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('python', 10, 1.2, 5, 4, 3, 2)\n",
      "('python', 10, 1.2, 5, 4, 3, 2, 'club', True)\n"
     ]
    }
   ],
   "source": [
    "############# tuple date ############\n",
    "tuple = (\"python\",10,1.2,5,4,3,2) \n",
    "print(tuple)\n",
    "\n",
    "tuple2 = tuple + (\"club\", True)\n",
    "print(tuple2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "id": "a12ee663-c30e-410a-9f7f-e2ada72a5b3f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.2"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# call index in tuple data (from 0 to n-1/ reverse from -n to -1)\n",
    "tuple[0]    # same as tuple[-3]\n",
    "tuple[1]    # same as tuple[-2]\n",
    "tuple[2]    # same as tuple[-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "9fbe0728-34a8-4834-a981-6fd449ddce58",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('python', 10, 1.2)"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# tuple slicing (from 0 : n-1)\n",
    "tuple[0:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "554a46c8-ff45-4e8b-afca-ea0980e2f671",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(5, 2, ('men', 'women'), (6, 4))\n"
     ]
    }
   ],
   "source": [
    "# tuple nesting\n",
    "character = (5,2,(\"men\",\"women\"),(6,4))\n",
    "print(character)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "497fb217-3b70-469d-9fcd-e23b0e6c8eea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'w'"
      ]
     },
     "execution_count": 190,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "character[2]       # Nested elements are indexed together\n",
    "character[2][1]    # Call second element in the third nested index\n",
    "character[2][1][0] # Call first caracter in the second element in the third nested index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "id": "1c2879d4-e54d-4e3e-bff2-7ced64fae8a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 4, 5, 7, 10]\n"
     ]
    }
   ],
   "source": [
    "# tuple data sorting\n",
    "num = (10,4,3,5,7)\n",
    "numsor = sorted(num)\n",
    "print(numsor)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "id": "83df5ffe-7b8e-4df3-ba0b-35f778ad5fb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['name', 1889, [3, 'a'], [4, 'b']]\n"
     ]
    }
   ],
   "source": [
    "########### List data ###########   \n",
    "# List data is mutable, while tuple data is unmutable\n",
    "# All codes are the same as tuple data\n",
    "\n",
    "list = [\"name\",1889,[3,'a'],[4,'b']]\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "id": "0e882e7d-78f7-43c1-85e6-01d49de75e27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['name', 1889, [3, 'a'], [4, 'b'], 'region', 10]\n"
     ]
    }
   ],
   "source": [
    "list.extend([\"region\",10])  # Adding each element (in this case, 2 new elements)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "3c3d0789-b405-45c2-bc12-89a5d5e22ae1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['name', 1889, [3, 'a'], [4, 'b'], 'region', 10, ['region', 10]]\n"
     ]
    }
   ],
   "source": [
    "list.append([\"region\",10])  # Adding one indexed element (in this case, 1 indexed element)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "029a35d3-78c7-4548-af35-dce5b57f3c81",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['last name', 1889, [3, 'a'], [4, 'b'], 'region', 10, ['region', 10]]\n"
     ]
    }
   ],
   "source": [
    "#list mutating\n",
    "list[0] = \"last name\"    # change element 0 of list as 'last name'\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "id": "3c7969d7-f808-4565-a26a-35593708fe91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1889, [3, 'a'], [4, 'b'], 'region', 10, ['region', 10]]\n"
     ]
    }
   ],
   "source": [
    "# list data deleting\n",
    "del(list[0])\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "id": "2f8674b5-1419-454f-9a74-201f0c21bb8b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['A', 'B', 'C', 'D']"
      ]
     },
     "execution_count": 175,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# list data split\n",
    "\"A,B,C,D\".split(\",\")   #split by comma, space"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "1d9d13e1-bcf5-4ec7-a04c-6866d864a371",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['PAAAAN', 'table', 112, 12.3]\n",
      "['PAAAAN', 'table', 112, 12.3]\n"
     ]
    }
   ],
   "source": [
    "# list data aliasing   (IMPORTANT! Difference from R code !!!!!)\n",
    "A = [\"pan\",\"table\",112]\n",
    "B = A                    # B has the same and linked elements of A\n",
    "B[0] = \"PAAAAN\"          # If the element of B is changed, the element of A will also changed\n",
    "\n",
    "print(A)\n",
    "print(B)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "id": "1034a54c-fb67-42ed-a515-3796bc0167fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['pan', 'table', 112]\n",
      "['PAAAAN', 'table', 112]\n"
     ]
    }
   ],
   "source": [
    "# list data copying     (IMPORTANT! Difference from R code !!!!!)\n",
    "A = [\"pan\",\"table\",112]\n",
    "C = A[:]                 # C has the copy elements of A\n",
    "C[0] = \"PAAAAN\"          # If the element of C is changed, the element of A will not be changed\n",
    "\n",
    "print(A)\n",
    "print(C)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "id": "bdd37823-63c2-4803-8081-334e48bbc619",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'key1': 'Jane', 'key2': 1933, 'key3': 'Korea', 'Key4': [75, 4, 36]}\n"
     ]
    }
   ],
   "source": [
    "########## Dictionaries data ##########\n",
    "# dictionaries consist of the 'keys' and 'values' \n",
    "# The keys are immutable \n",
    "\n",
    "dic = {\"key1\" : \"Jane\", \"key2\":1933, \"key3\":\"Korea\", \"Key4\":[75,4,36]}\n",
    "print(dic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "id": "ddde39f9-29d9-449a-976d-d2b0d14606bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Jane'"
      ]
     },
     "execution_count": 202,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# indexing value using key\n",
    "dic['key1']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "id": "e8e20f67-bdc0-418f-8b75-f20d87d2a976",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'key1': 'Jane', 'key2': 1933, 'key3': 'Korea', 'Key4': [75, 4, 36], 'key5': (5, 5, 5)}\n"
     ]
    }
   ],
   "source": [
    "# adding new key and value\n",
    "dic[\"key5\"]=(5,5,5)\n",
    "print(dic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "id": "f266234a-8049-4ff1-b020-5bc4d5aa19f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'key1': 'Jane', 'key2': 1933, 'key3': 'Korea', 'Key4': [75, 4, 36]}\n"
     ]
    }
   ],
   "source": [
    "# deleting key and value\n",
    "del(dic[\"key5\"])\n",
    "print(dic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "id": "f4fb9f9e-4ebe-450d-bf8d-ee4264be4469",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 212,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# find keys\n",
    "'key1' in dic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "id": "0c66d5a1-b61e-4ce2-b46c-242b4754c2a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['key1', 'key2', 'key3', 'Key4'])"
      ]
     },
     "execution_count": 215,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# find all keys\n",
    "dic.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "id": "303a8a71-a83a-4549-a3e4-060df105f23b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values(['Jane', 1933, 'Korea', [75, 4, 36]])"
      ]
     },
     "execution_count": 217,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# find all values\n",
    "dic.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 226,
   "id": "68bbc814-0873-4854-97c1-a065fa633be9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'seoul', 3, 5, 'Jane', 10}\n"
     ]
    }
   ],
   "source": [
    "########## Set data ##########\n",
    "# Set do not record element position\n",
    "# Set has a particular element (duplicated items are not presented)\n",
    "# Set is ordered\n",
    "\n",
    "set1 = {\"Jane\", \"Jane\", \"Jane\", \"seoul\", 10,5,3}\n",
    "print(set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "id": "da67cc32-5f97-4d07-888d-b02d7e6b67ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'seoul', 3, 5, 'Jane', 10, 'Korea'}\n"
     ]
    }
   ],
   "source": [
    "# Adding set items\n",
    "set1.add(\"Korea\")\n",
    "print(set1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "id": "eba4df7d-493f-4f95-8703-8436780e322a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'seoul', 3, 5, 'Jane', 10}\n"
     ]
    }
   ],
   "source": [
    "# Deleting set items\n",
    "set1.remove(\"Korea\")\n",
    "print(set1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 254,
   "id": "15f6a2db-200a-4910-8192-2df2e1ddc3b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 254,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find set items\n",
    "\"seoul\" in set1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 255,
   "id": "5d8d0b50-d1b4-485e-af54-66a436810528",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "({10, 3, 5, 'Jane', 'seoul'}, {1144, 1167, 3535, 'Gray', 'seoul'})"
      ]
     },
     "execution_count": 255,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# print set1 and set2\n",
    "set2 = {\"Gray\", \"seoul\", 1167,1144,3535}\n",
    "set1,set2     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "id": "9d4bcacf-b970-4f23-a5b1-c44e22f3837c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'seoul'}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{'seoul'}"
      ]
     },
     "execution_count": 259,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find intersection between set1 and set2\n",
    "print(set1&set2)\n",
    "set1.intersection(set2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "id": "ef05aca6-9d62-44aa-8523-a4be05683f14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 3, 5, 'Jane'}"
      ]
     },
     "execution_count": 250,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find difference\n",
    "\n",
    "set1.difference(set2) #different set1 items from set2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "id": "395c5ba7-40e0-4518-9710-e2a6bc17036f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 1144, 1167, 3, 3535, 5, 'Gray', 'Jane', 'seoul'}"
      ]
     },
     "execution_count": 242,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Union of multiple set items .union (involving all items in multiple sets)\n",
    "\n",
    "set1.union(set2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 260,
   "id": "e2a99dd9-b24b-4926-8bcd-c8b9250b1e08",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 260,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check subset (set2 is subset of set1?)\n",
    "set2.issubset(set1)     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "id": "6681f4a0-0249-45d0-a54d-1e21c47c11d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 261,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check superset (set2 is superset of set1?)\n",
    "set2.issuperset(set1)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
