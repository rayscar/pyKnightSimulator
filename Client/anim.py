# coding=utf-8
import tools
import time


def __tabs__():
    print "\n\n\t\t"


def __tabs2__():
    print "\n\n"


def __welcome__(data):
    __tabs__()
    print data
    __tabs2__()
    time.sleep(2)
    tools.clear()


def __message__(mes, bdelay, adelay):
    time.sleep(bdelay)
    __tabs__()
    print mes
    __tabs2__()
    time.sleep(adelay)
