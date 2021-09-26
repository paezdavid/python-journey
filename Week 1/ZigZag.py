import time, sys
indent = 0 # how many spaces to indent
indentIncreasing = True # whether the indentation is increasing or not

try:
    while True:
    #    1 - by multiplying the space to a number we aument the number of spaces.
        print(' ' * indent, end='')
    #    2 - print eight asterisks
        print('********')
    #    3 - await for 1 millisecond
        time.sleep(0.1)

        if indentIncreasing:
        #   increase the number of spaces
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()