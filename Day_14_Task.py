{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'list1' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-e32a67e7e257>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#name error\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mlist\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m12\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlist1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'list1' is not defined"
     ]
    }
   ],
   "source": [
    "#name error\n",
    "list=12\n",
    "print(list1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "must be str, not int",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-2e178e6c53c4>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#Type error\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'123'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0ma\u001b[0m\u001b[0;34m+=\u001b[0m\u001b[0;36m123\u001b[0m  \u001b[0;31m# int is added with string\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m: must be str, not int"
     ]
    }
   ],
   "source": [
    "#Type error\n",
    "a='123'\n",
    "a+=123  # int is added with string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'list' object cannot be interpreted as an integer",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-3b3fb02e4682>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0ml\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m56\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m7\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: 'list' object cannot be interpreted as an integer"
     ]
    }
   ],
   "source": [
    "l=[1,2,3,4,5,56,6,7]\n",
    "for i in range(2,l):\n",
    "    print(i+1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-4-b56a74be04fd>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-4-b56a74be04fd>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    for i range(1,10):  #for i in range(1,10):   in keyword missing\u001b[0m\n\u001b[0m              ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#Syntax errror\n",
    "for i range(1,10):  #for i in range(1,10):   in keyword missing\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-5-1373c5f361e4>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-5-1373c5f361e4>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    in =123 # keyword is used as variable\u001b[0m\n\u001b[0m     ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "in =123 # keyword is used as variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "56\n",
      "6\n",
      "7\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-6-d398d1c77bf5>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0ml\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m5\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m56\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m7\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "#index error\n",
    "l=[1,2,3,4,5,56,6,7]\n",
    "for i in range(len(l)):\n",
    "    print(l[i+1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'modulexyz'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-7-c98313728f2e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#Module not found error\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mmodulexyz\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'modulexyz'"
     ]
    }
   ],
   "source": [
    "#Module not found error\n",
    "import modulexyz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "23",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-8-380b1431ed6d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mdict1\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mdict1\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;36m12\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m11\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;36m12\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m13\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;36m14\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdict1\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m23\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m: 23"
     ]
    }
   ],
   "source": [
    "#Key error\n",
    "dict1=dict()\n",
    "dict1={1:12,11:12,13:14}\n",
    "print(dict1[23])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'x'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-10-44b679b53596>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#Import error\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mmath\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mx\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m: cannot import name 'x'"
     ]
    }
   ],
   "source": [
    "#Import error\n",
    "from math import x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'abc'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-11-cfbae703fbb8>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#Value error\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"abc\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m: invalid literal for int() with base 10: 'abc'"
     ]
    }
   ],
   "source": [
    "#Value error\n",
    "int(\"abc\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-12-26d369139690>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#Zero Division Error\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;36m100\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#Zero Division Error\n",
    "100/0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate():\n",
    "    try:\n",
    "        print('+')\n",
    "        print('-')\n",
    "        print('*')\n",
    "        print('/')\n",
    "        print('%')\n",
    "        print('**')\n",
    "        operation = input(\"Select an operator:n\")\n",
    "        print(\"Enter two numbers\")\n",
    "        number_1 = int(input())\n",
    "        number_2 = int(input())\n",
    "        if operation == '+': # To add two numbers\n",
    "            print(number_1 + number_2)\n",
    "        elif operation == '-': # To subtract two numbers\n",
    "            print(number_1 - number_2)\n",
    "        elif operation == '*': # To multiply two numbers\n",
    "            print(number_1 * number_2)\n",
    "        elif operation == '/': # To divide two numbers\n",
    "            print(number_1 / number_2)\n",
    "        elif operation == '%': # To remainder two numbers\n",
    "            print(number_1 % number_2)\n",
    "        elif operation == '**': # To num1 exponent num2\n",
    "            print(number_1 ** number_2)\n",
    "        else:\n",
    "            print('Invalid Input')\n",
    "    except Exception as e:\n",
    "        print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+\n",
      "-\n",
      "*\n",
      "/\n",
      "%\n",
      "**\n",
      "Select an operator:n*\n",
      "Enter two numbers\n",
      "24\n",
      "rv\n",
      "invalid literal for int() with base 10: 'rv'\n"
     ]
    }
   ],
   "source": [
    "calculate()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name 'b' is not defined\n"
     ]
    }
   ],
   "source": [
    "#print one message if the try block raises a NameError and another for other errors\n",
    "try:\n",
    "    a = 123\n",
    "    if a==123:\n",
    "        print(b)\n",
    "        raise NameError(\"Name error\")\n",
    "    if a >0:\n",
    "        raise ValueError(\"Value error\")\n",
    "except NameError as ne:\n",
    "        print(ne)\n",
    "except ValueError as ve:\n",
    "    pritn(ve)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your age: nineteen\n",
      "You have entered an invalid value.\n"
     ]
    }
   ],
   "source": [
    "#When try-except scenario is not required?\n",
    "\n",
    "###Python Exceptions are error scenarios that alter the normal execution flow of the program The process of The code inside the else block is executed if there are no exceptions raised.\n",
    "\n",
    "#Try getting an input inside the try catch block\n",
    "\n",
    "try:\n",
    "    age=int(input('Enter your age: '))\n",
    "except:\n",
    "    print ('You have entered an invalid value.')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
