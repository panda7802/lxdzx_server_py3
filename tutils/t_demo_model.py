# coding=utf-8

"""
Created on 2016�?12�?13�?

@author: pangt
"""


class TDemoToy():
    def __init__(self, name="", price=1.0):
        self.name = name
        self.price = price


class TDemoZAddr():
    def __init__(self, detail_addr="", street=""):
        self.detail_addr = detail_addr
        self.street = street


class TDemoPerson(object):
    _get_toys_arr_type = TDemoToy

    def __init__(self, name='', sex='', birth='', job='', addr=TDemoZAddr('703', 'pmx')):
        self.name = name
        self.sex = sex
        self.birth = birth
        self.job = job
        self.addr = addr
        self.toys = []

    def __unicode__(self):
        return self.name + "\t" + self.sex + "\t" + self.birth + "\t" + self.job + "\t" + str(self.addr.__dict__)
