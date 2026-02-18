{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "6eabe83e-2215-4dc4-afe3-9ef5e558e788",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'bool'>\n",
      "<class 'int'>\n",
      "<class 'str'>\n",
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "print()\n",
    "len()\n",
    "type()\n",
    "input()\n",
    "input()\n",
    "int(),float(),str(),bool()\n",
    "max(),min()\n",
    "sum()\n",
    "abs()\n",
    "sorted()\n",
    "range()\n",
    "\"\"\"\n",
    "a=True\n",
    "print(type(a))\n",
    "a=25\n",
    "print(type(a))\n",
    "a=\"25\"\n",
    "print(type(a))\n",
    "a=2.5\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7a020fce-6a42-43ed-96da-1ed6a59bf6ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50\n"
     ]
    }
   ],
   "source": [
    "a=\"25\"\n",
    "print(int(a)*2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "0c4977af-030d-4c36-8a7f-65a6fae52c0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8 1\n"
     ]
    }
   ],
   "source": [
    "l=[1,2,5,8]\n",
    "print(max(l),min(l))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "426679ea-b0d9-41ae-8c71-71db79c88fee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "l=[2,5,6,7]\n",
    "print(sum(l))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f1244efc-2b72-4b06-98f3-4078513deadd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[22, 24, 54, 99]\n",
      "[1, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "l=[22,99,24,54]\n",
    "print(sorted(l))\n",
    "t=(1,5,3,4) #returns a sorted list\n",
    "print(sorted(t))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9f5f475e-ba2b-43d1-891b-3c50f5c22974",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "a=-4\n",
    "print(abs(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "24bd9a0c-0fde-4430-a39d-0d07a664a174",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "for i in range(9,1,-1):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "49e010e3-1fba-413e-a4b0-bb0df90a3475",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "77\n"
     ]
    }
   ],
   "source": [
    "add=lambda a,b:a+b #anonymous or throwaway functions\n",
    "print(add(22,55))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "cc3993e2-ecc2-4018-82b7-d59cdef2d638",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[484, 2025, 4489, 7921]\n"
     ]
    }
   ],
   "source": [
    "a=[22,45,67,89]\n",
    "square=list(map(lambda x:x*x,a))\n",
    "print(square)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "id": "791fe330-9d30-48d6-b84c-9df4f3ecf614",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "def lambda_holder_function(a):\n",
    "    return lambda b:a*b\n",
    "c=lambda_holder_function(5)\n",
    "print(c(6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "ed2ecff7-8c1c-4b52-8be8-04e5a73edc58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(224, 88)\n"
     ]
    }
   ],
   "source": [
    "a=[224,45,67,88]\n",
    "divide=tuple(filter(lambda x:x%2==0,a))\n",
    "print(divide)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "002f5516-4851-4df8-8957-421b9308206e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Functions\n",
    "\"\"\"\n",
    "def first_function():\n",
    "    print(\"Hello world\")\n",
    "first_function()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "c832cda4-76bd-4237-b260-5c6680d1b991",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "def sum_two_nums(a,b):\n",
    "    return a+b\n",
    "print(sum_two_nums(3,8))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "01e6249b-0d63-4526-a336-0ad3245e89e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum is 1\n"
     ]
    }
   ],
   "source": [
    "def min_three_numbers(a,b,c):\n",
    "    if a<b and a<c:\n",
    "        return a\n",
    "    elif b<a and b<c:\n",
    "        return b\n",
    "    else:\n",
    "        return c\n",
    "print(\"Minimum is\",min_three_numbers(5,8,1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "33dc461e-1ccd-40cc-ae6c-f5b7d54fd2b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "def factorial(n):\n",
    "    fact=1\n",
    "    for i in range(1,n+1):\n",
    "        fact*=i\n",
    "    return fact\n",
    "print(factorial(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "c60f7271-c4b7-4692-9d41-068bde2f27af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n",
      "10\n",
      "3\n",
      "19\n",
      "22\n",
      "21\n",
      "15\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Different types of parameters\n",
    "\"\"\"\n",
    "#Default parameters\n",
    "def sum_two_nums(a=1,b=2):\n",
    "    return a+b\n",
    "print(sum_two_nums(3,8))\n",
    "print(sum_two_nums(8))\n",
    "print(sum_two_nums())\n",
    "#Keyword arguments\n",
    "def sum_two_nums(a=1,b=2,c=3,d=5):\n",
    "    return a+b+c+d\n",
    "print(sum_two_nums(a=3,b=8))\n",
    "print(sum_two_nums(b=3,a=9,d=7))\n",
    "print(sum_two_nums(b=3,a=9,d=7,c=2))\n",
    "#note:non default arguments follow default arguments is an error,so non default arguments comes before default arguments\n",
    "#:def sum_two_nums(c=3,d=5,a,b) is not possible\n",
    "def sum_two_nums(a,b,c=3,d=5):\n",
    "    return a+b+c+d\n",
    "print(sum_two_nums(2,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "d3306cb2-f499-4d3e-902d-d8dc2af2bae5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "3\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "#scope of function\n",
    "c=5\n",
    "def sum_two_nums(a=1,b=2):\n",
    "    global c\n",
    "    c=a+b\n",
    "    return c\n",
    "print(c)\n",
    "print(sum_two_nums())\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "b3134998-5242-4ede-afd0-565d31d83cf5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "#nested function\n",
    "def outside_function():\n",
    "    a=5\n",
    "    def inside_function():\n",
    "        a=20\n",
    "        print(a)\n",
    "    inside_function()\n",
    "    print(a)\n",
    "outside_function()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "99a11ad0-f8c6-4af6-9dec-a40cdbe902e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "20\n",
      "30\n"
     ]
    }
   ],
   "source": [
    "a=30\n",
    "def outside_function():\n",
    "    a=5\n",
    "    def inside_function():\n",
    "        nonlocal a\n",
    "        a=20\n",
    "        print(a)\n",
    "    inside_function()\n",
    "    print(a)\n",
    "outside_function()\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "85f91246-9723-4a6a-af05-7e54839872f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "def isprime(n):\n",
    "    c=0\n",
    "    for i in range(2,n+1):\n",
    "       if n%i==0:\n",
    "           c+=1\n",
    "    if c>2:\n",
    "        return False\n",
    "    return True\n",
    "print(isprime(6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "a52440b0-beb2-4be7-89db-aae9fe28b808",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "def num_of_vowels(a):\n",
    "    c=0\n",
    "    for i in a:\n",
    "        if i in \"AEIOUaeiou\":\n",
    "            c+=1\n",
    "    return c\n",
    "print(num_of_vowels(\"Hello World\"))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "id": "42a4bd53-a81d-4c97-8136-ac6feac01950",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3]\n"
     ]
    }
   ],
   "source": [
    "def prime(n):\n",
    "    c=0\n",
    "    for i in range(2,n+1):\n",
    "       if n%i==0:\n",
    "           c+=1\n",
    "    if c>2:\n",
    "        return False\n",
    "    return True\n",
    "def prime_factors(n):\n",
    "    l=[]\n",
    "    m=[]\n",
    "    for i in range(2,n+1):\n",
    "        if n%i==0:\n",
    "            l.append(i)\n",
    "    for i in l:\n",
    "        if prime(i):\n",
    "            m.append(i)\n",
    "    return m\n",
    "print(prime_factors(6))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "id": "61e27b66-f198-4449-b6a6-6ba150c0c634",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['e', 'o']\n"
     ]
    }
   ],
   "source": [
    "def vowels(a):\n",
    "    l=[]\n",
    "    for i in a:\n",
    "        if i in \"AEIOUaeiou\":\n",
    "            if i not in l:\n",
    "                l.append(i)\n",
    "    return l\n",
    "print(vowels(\"Helloo\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61b4f5b3-35b2-438d-b86f-f0d743ae477a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
