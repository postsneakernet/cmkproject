#!/usr/bin/python

import os, sys, shutil


src = os.path.dirname(os.path.realpath(__file__)) + "/src/"

def usage():
    print("Usage: cmkproject.py c|cpp project [source [t (if c++ template)]]")
    sys.exit()


def create_project_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        print("Project directory already exists, exiting...")
        sys.exit()
    return path + "/"


def update_file(filename, line_num, text):
    with open(filename, 'r') as file:
        data = file.readlines()
    data[line_num - 1] = text
    with open(filename, 'w') as file:
        file.writelines(data)


def mk_project(dst, author, project_type, project_name):
    main_temp = ""
    makefile = ""

    if project_type == 'c':
        main_temp = "main.c"
        makefile = "makefile.c"
    else:
        main_temp = "main.cpp"
        makefile = "makefile.cpp"

    shutil.copyfile(src + main_temp, dst + main_temp)
    shutil.copyfile(src + makefile, dst + "makefile")
    update_file(dst + main_temp, 2, "// " + author + "\n")
    update_file(dst + main_temp, 3, "// " + project_name + " driver\n")
    update_file(dst + "makefile", 4, "EXEC = " + project_name + "\n")


def mk_project_w_source(dst, author, project_type, project_name, source_name):
    main_temp = ""
    source_temp = ""
    header_temp = ""
    header_ext = ""
    source = ""
    header = ""

    if project_type == 'c':
        main_temp = "main.c"
        source_temp = "source.c"
        header_temp = "header.h"
        header_ext = "_H"
        source = source_name + ".c"
        header = source_name + ".h"
    else:
        main_temp = "main.cpp"
        source_temp = "source.cpp"
        header_temp = "header.hpp"
        header_ext = "_HPP"
        source = source_name + ".cpp"
        header = source_name + ".hpp"

    if project_type == 't':
        source_temp = "template.tpp"
        source = source_name + ".tpp"

    mk_project(dst, author, project_type, project_name)
    shutil.copyfile(src + source_temp, dst + source)
    shutil.copyfile(src + header_temp, dst + header)
    update_file(dst + header, 1, "// " + header + "\n")
    update_file(dst + header, 2, "// " + author + "\n")
    update_file(dst + header, 3, "// " + source_name + " declaration\n")
    update_file(dst + header, 5, "#ifndef " + source_name.upper() +
            header_ext + "\n")
    update_file(dst + header, 6, "#define " + source_name.upper() +
            header_ext + "\n")
    update_file(dst + header, 10, "#endif // " + source_name.upper() +
            header_ext + "\n")

    update_file(dst + source, 1, "// " + source + "\n")
    update_file(dst + source, 2, "// " + author + "\n")
    update_file(dst + source, 3, "// " + source_name + " implementation\n")
    update_file(dst + source, 5, "#include " + '"' + header + '"\n')

    update_file(dst + main_temp, 6, "#include " + '"' + header + '"\n')

    if project_type != 't':
        update_file(dst + "makefile", 5, "OBJS = " + source_name +
                ".o main.o\n")
        update_file(dst + "makefile", 13,
                source_name + ".o: " + source + " " + header + "\n")
        update_file(dst + "makefile", 14,
                "main.o: " + main_temp + " " + header + "\n")
    else:
        # special stuff for template
        update_file(dst + header, 8, "#include " + '"' + source + '"' + "\n")
        update_file(dst + "makefile", 14,
                "main.o: " + main_temp + " " + header + " " + source + "\n")


def get_project_type():
    return sys.argv[1]


def get_project_name():
    return sys.argv[2]


def get_source_name():
    return sys.argv[3]


def main():
    project_root = os.environ.get('C_PROJECT_ROOT', "") # set before use
    author = os.environ.get('C_PROJECT_AUTHOR', "author")

    project_type = ""
    project_name = ""

    if not project_root:
        print("Please set the project root first in cmkproject.py")
        return

    if len(sys.argv) <= 2:
        usage()
    else:
        project_type = get_project_type()
        if project_type != 'c' and project_type != 'cpp':
            usage()
        project_name = get_project_name()

    if len(sys.argv) == 3:
        project_path = create_project_dir(project_root + project_name)
        mk_project(project_path, author, project_type, project_name)
    elif len(sys.argv) == 4:
        project_path = create_project_dir(project_root + project_name)
        source_name = get_source_name()
        mk_project_w_source(project_path, author, project_type, project_name,
                source_name)
    elif len(sys.argv) == 5:
        if sys.argv[4] != 't' or project_type != 'cpp':
            usage()
        project_path = create_project_dir(project_root + project_name)
        project_type = 't'
        source_name = get_source_name()
        mk_project_w_source(project_path, author, project_type, project_name,
                source_name)
    else:
        usage()


if __name__ == "__main__":
    main()
