.SUFFIXES: .cpp .o
CC = g++
FLAGS = -g -Wall
EXEC = project
OBJS = main.o

${EXEC}: ${OBJS}
	${CC} ${FLAGS} -o ${EXEC} ${OBJS}

.cpp.o:
	${CC} ${FLAGS} -c $<


main.o: main.cpp

clean:
	rm -f ${EXEC} ${OBJS}
