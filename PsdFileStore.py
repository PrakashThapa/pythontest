#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt
import os
from urllib import urlretrieve, urlopen
import optparse

class PsdFileStore:
    options =()
    count = 0
    def __init__(self):
        self.options = self.parse()
        
    def validate(self, options):
        if not os.path.isfile(options.file):
            print 'Input file "'+options.file+'" does not exits'
            exit(0)
        if not os.path.exists(options.dir):
            try:
                os.makedirs(options.dir)
            except:
                print 'could not create directory'
                exit(0)

    def parse(self):
        parser = optparse.OptionParser()
        parser.add_option(
            '-f',
            '--file',
            action='store',
            dest='file',
            help='Input File',
            default='sample.txt',
            )
        parser.add_option(
            '-d',
            '--dir',
            action='store',
            dest='dir',
            help='Directory to store the downloaded file',
            default='data',
            )
        (options, args) = parser.parse_args()
        self.validate(options)
        return options
    def counter(self):
        print str(self.count)+" file(s) Downloaded"
    def store(self): 
        options = self.options
        try:
            f = open(options.file, 'r')
            data = f.read().splitlines()
            f.close()
        except:
            print "could not read file '" + options.file + "'"
            exit(0)
        for line in data:
            try:
                url = urlopen(line)
                if url.code == 200:
                    filename = line.split('?')[0].split('/')[-1]
                    urlretrieve(line, options.dir+'/' + filename)
                    self.count = self.count  + 1
                else:
                    print "The Url '" + line + "' does not exits"
            except:
                print "There is error:   the line '" + line + "' is invalid URL or URL does not exits."
                
# check user's input whether they are correct or not

psd = PsdFileStore()
psd.store()
psd.counter()
print "Done!!! "

			