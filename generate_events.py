import random
import datetime
from datetime import timedelta
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'wes'
EVENTS_COLLECTION = 'events'
THREATS_COLLECTION = 'threats'

def random_protocol():
    """
    Returns a random protocol from a predefined list.
    """
    protocols = ['HTTP', 'HTTP', 'HTTP', 'HTTP', 'SMTP', 'SMTP', 'SMTP', 'FTP', 'IRC']
    return random.choice(protocols)

def random_category():
    """
    Returns a string representing one of the available threat categories.
    """
    tvs = ['Suspicious Adobe Documents', 'Signature Hits', 'Intelligence Hits', 'Suspicious Emails', \
            'Suspicious Web Download', 'C2 Activity', 'SQL Injection', \
            'DDoS Attack', 'Remote Access Trojans']
    return random.choice(tvs)

def random_date():
    """
    This function will return a random datetime between two datetime objects.
    """
    start = datetime.datetime.strptime('2015-09-15', '%Y-%m-%d')
    end = datetime.datetime.strptime('2016-01-29', '%Y-%m-%d')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    date = str(start + timedelta(seconds=random_second))
    return '-'.join(date.split('-')[:3]).split(' ')[0]

def random_user_agent():
    """
    This function returns a random UA from a predefined list.
    """
    uas = ['Google Bot', 'Cygwin Setup', 'Internet Explorer', 'Opera', 'Mozilla 4.0', \
            'BioRad KnowItAll', 'Cyberb0b iPhone', 'McHttp', 'GoogleEarth', 'Windows-Update-Agent', \
            'ie', 'MyIE 1.0', 'curl 7.7', 'Download']
    return random.choice(uas)

def random_host():
    """
    This function returns a random hostname.
    """
    hosts = ['www.wopxs.com', 'sovietrussia.cn', 'www.mirekw.com', 'mw1.google.com', \
            'cache.google.ru', '216.252.110.31', 'updates.netbeans.com', 'www.doi.gov', \
            'classicbike.biz', 'dhs.gov', 'rollacity.org', 'ftp.ni.com', 'peeps.redhat.com', \
            'infowars.com', 'www.faa.gov', 'cns3.grizzly.info', 'kovsutap.cn', 'wmata.com', \
            'itu.int', 'fires.nist.gov', 'babycakes.biz', 'influizing.cn']
    return random.choice(hosts)

def random_event_status():
    """
    This function returns a random event status.
    """
    statuses = ['Under Review', 'Pending', 'Confirmed Malicious', 'False Positive', 'Clean']
    return random.choice(statuses)

def random_subject():
    """
    This function returns a random SMTP subject.
    """
    subjects = ['Notice of Underreported Income', '2nd Request', 'Urgent!', 'New Test Plan', \
            'Notice of Underreported Income', 'Notice of Underreported Income', \
            'ME Course Docs', 'FW: Your E-Invite', 'DHL Service', 'Australian Lotery Winner.', \
            'Scan from a Xerox Machine', 'October Events', 'shipping tomorrow', 'RE: Youre Fired.', \
            'RE: Home Inspection', 'Bob Barker Invites You...', 'Timecards', 'Tuesdays RFP', 'RQQ']
    return random.choice(subjects)


def generate_events():
    """
    Connects to the wes database, threats collection, and inserts 4000+ events.
    """
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    tvs_collection = connection[DBS_NAME][THREATS_COLLECTION]
    for x in range(0, 4519):
        event = {}
        event['timestamp'] = str(random_date())
        event['category'] = random_category()
        event['status'] = random_event_status()
        event['protocol'] = random_protocol()

        # If proto is HTTP or SMTP, add a few more items to the event dict.
        event['hostname'] = random_host()
        event['user_agent'] = random_user_agent()
        event['subject'] = random_subject()

        # Insert the event into the threatss collection.
        tvs_collection.insert(event)

if __name__ == '__main__':
	generate_events()

