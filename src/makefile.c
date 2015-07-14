.SUFFIXES: .c .o
CC = gcc
FLAGS = -g -Wall
EXEC = project
OBJS = main.o

${EXEC}: ${OBJS}
	${CC} ${FLAGS} -o ${EXEC} ${OBJS}

.c.o:
	${CC} ${FLAGS} -c $<


main.o: main.c

clean:
	rm -f ${EXEC} ${OBJS}
