# cmkproject
Python script for simplfying C/C++ project creation outside of IDEs

Works in Linux and OS X and anywhere you'd expect gcc/g++ to (works in Cygwin)

### Usage:
* Set project_root to desired project path with trailing / in cmkproject.py e.g. "/Users/elliot/dev/"
* Optionally set author to your name
* Alternatively you can set environment variables C_PROJECT_ROOT and C_PROJECT_AUTHOR
* Specify c or cpp, root or directory in root, project name, and optionally source name, and if cpp optionally t if source is to be a template class

cmkproject.py c|cpp root|directory project [source [t (if c++ template)]]

### Arguments Explanation:
* 1st arg: must be 'c' or 'cpp'
* 2nd arg: must be 'root' or a directory or path in project root (will be created if it doesn't
  exist)
* 3rd arg: name of project
* 4th arg: optional, name of source
* 5th arg: optional, cpp only, must be 't'

### Examples:
cmkproject.py c root heap heap
* creates directory named heap in the project root with main.c, heap.h, heap.c, and makefile
* heap.h is included in main.c and heap.c
* running make creates heap executable with gcc
* running the above with cpp creates uses .hpp/.cpp and makefile uses g++

cmkproject.py cpp root hw1
* creates directory named hw1 in the project root with main.cpp and makefile
* running make creates hw1 executable

cmkproject.py cpp cs50 hw2 stack t
* creates directory named hw2 in the directory cs50 in project root with main.cpp, stack.hpp, stack.tpp, and makefile
* stack is intended to be a template class to be defined in stack.tpp and included at bottom of stack.hpp so it compiles properly

### Note:
* cmkproject.py needs to remain at same level as src
* Editing the templates in src may likely break things
* Names for project and source need to be valid filenames and legal in c/cpp
