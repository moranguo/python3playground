#!/usr/bin/python

import xml.etree.ElementTree as ET
import glob
import csv

with open('result.csv', 'wb') as csvfile:
    mywriter = csv.writer(csvfile, delimiter=',')
    mywriter.writerow( ('sender', 'senderip', 'policy_domain','recipient') )
    for file in glob.glob('/data/erich/*.meta'):
        root = ET.parse(file).getroot()
        #print file
        sender_e=root.find("user-data/smtp-session/sender")
        if sender_e is not None:
           sender=sender_e.text
        else:
           sender=''
        senderip=root.find("user-data/smtp-session/senderip").text
        policy_domain=root.find("user-data/policy/policy_domain").text
        recipient=root.find("user-data/smtp-session/recipients/recipient").text

        mywriter.writerow((sender,senderip,policy_domain,recipient))


