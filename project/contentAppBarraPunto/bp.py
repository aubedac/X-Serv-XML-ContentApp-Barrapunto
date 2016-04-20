#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Simple XML parser for the RSS channel from BarraPunto
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2009
#
# Just prints the news (and urls) in BarraPunto.com,
#  after reading the corresponding RSS channel.

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string
import urllib2

def normalize_whitespace(text):
    return string.join(string.split(text), ' ')

class myContentHandler(ContentHandler):

    def __init__(self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.line = ""

    def startElement(self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
                self.title = self.theContent
            elif name == 'link':
                self.inContent = True

    def endElement(self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                self.title = normalize_whitespace(self.theContent)
                # To avoid Unicode trouble
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
                self.link = normalize_whitespace(self.theContent)
                self.line += "<li><a href=" + self.link + ">" + self.title + "</a></li>"
                #print self.line.encode("utf-8")
                self.inContent = False
                self.theContent = ""

    def characters(self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars

# Load parser and driver
def get_bp():
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)
#xmlfile = open('barrapunto.txt', "r")
#theParser.parse(xmlfile)
    f = urllib2.urlopen('http://barrapunto.com/index.rss')
    theParser.parse(f)
    return theHandler.line
