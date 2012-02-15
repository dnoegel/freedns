#!/usr/bin/env python2
# coding:utf-8

#
# Config
#

## Your Freedns.afraid.org username
USERNAME = ""
## Your password
PASSWORD = ""

## Which domains do you want to update from this machine?
# ["ALL"] will update all domains
UPDATE_DOMAINS = ["mydomain.mooo.com", ] 

########################################################################

from hashlib import sha1
import urllib2
import datetime 
import os

API_URL = "https://freedns.afraid.org/api/?action=getdyndns&sha={sha1hash}"

## create hash over credentials
def get_sha1(username, password):
    return sha1("{0}|{1}".format(username, password)).hexdigest()


## read a given url
def read_url(url):
    try:
        return urllib2.urlopen(url).read()
    except (urllib2.URLError, urllib2.HTTPError) as inst:
        return "ERROR: {0}".format(inst)

if __name__ == "__main__":
    shahash = get_sha1(USERNAME, PASSWORD)
    url = API_URL.format(sha1hash=shahash)
    
    with open(os.path.expanduser("~/.freedns_log"), "a") as fh:
        result = read_url(url)
        domains = []
        if result.startswith("ERROR"):
            print result
        else:
            for line in result.splitlines():
                service, ip, update_url = line.split("|")
                domains.append(line.split("|"))
                
                if service.strip() in UPDATE_DOMAINS or "ALL" in UPDATE_DOMAINS:
                    result = read_url(update_url.strip())
                    print "Updating {0}".format(service), 
                    print result
            
                    fh.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M: "))
                    fh.write("Updating {0} ".format(service))
                    fh.write(result)
    
            
