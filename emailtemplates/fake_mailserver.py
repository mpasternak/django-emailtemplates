#! /usr/bin/python

"""This module is a simple, fake mailserver that you can 
run on localhost."""

import asyncore
import smtpd

class TestMailServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print "-" * 78
        print "Fake mail server received a message:"
        print self
        print peer
        print mailfrom
        print rcpttos
        print data
        
if __name__ == "__main__":

    tms = TestMailServer(('127.0.0.1', 25), None)
    print "Fake mail server starting!"
    asyncore.loop()
