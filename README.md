# cmkproject
Python script for simplfying C/C++ project creation outside of IDEs

Works in Linux and OS X and anywhere you'd expect gcc/g++ to (works in Cygwin)

### Usage:
* Set project_root to desired project path e.g. "/Users/elliot/dev/"
* Optionally set author to your name
* Specify c or cpp, project name, and optionally source name, and if cpp optionally t if source is to be a template class

cmkproject.py c|cpp project [source [t (if c++ template)]]

### Examples:
cmkproject.py c heap heap
* creates directory named heap in the project root with main.c, heap.h, heap.c, and makefile
* heap.h is included in main.c and heap.c
* running make creates heap executable with gcc
* running the above with cpp creates uses .hpp/.cpp and makefile uses g++

cmkproject.py cpp hw1
* creates directory named hw1 in the project root with main.cpp and makefile
* running make creates hw1 executable

cmkproject.py cpp hw2 stack t
* creates directory named hw2 in the project root with main.cpp, stack.hpp, stack.tpp, and makefile
* stack is intended to be a template class to be defined in stack.tpp and included at bottom of stack.hpp so it compiles properly

### Note:
* cmkproject.py needs to remain at same level as src
* Editing the templates in src may likely break things
