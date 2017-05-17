

from termcolor import colored
import time
import sys


INIT_TIME = time.time()


def perf():
    ''' Return the performance time '''
    millis = time.time() - INIT_TIME
    return "--------------------------------\n" \
        "Performance time: %s" % millis


def error():
    ''' Massage if not supported entering '''
    print colored("..::Incorrect amount of arguments::..", 'red')
    print colored("\tEnter just one integer", 'blue')
    quit()


def main():
    if len(sys.argv) != 2:
        error()  # check error() to edit the massage
    # let's begin
    perf()


if __name__ == '__main__':
    main()
