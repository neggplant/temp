from django.shortcuts import render

# Create your views here.
import time
import datetime
import threading
import os


def apples_red():
    print('apple_red', time.strftime('%Y-%m-%d %H:%M:%S'))
    # print('red threading:', threading.currentThread().ident)
    # print('red getpid:', os.getpid())
    # print('red getppid:', os.getppid())
    time.sleep(10)

def apples_green():
    print('apple_green', time.strftime('%Y-%m-%d %H:%M:%S'))
    # print('green threading:', threading.currentThread().ident)
    # print('green getpid:', os.getpid())
    # print('green getppid:', os.getppid())
    time.sleep(4)