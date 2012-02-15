freedns
=======
This is a simple, unofficial client for the dynamic DNS-service 
to be found at freedns.afraid.org.

It makes use of the ASCII- Programmer's API, so in contrast to
many other clients out there, you will not need to mess around
with the authentication tokens each time, those changed.

Usage
-----
Just edit the file freedns.py and insert your credentials 
(USERNAME and PASSWORD). Also you need to specify, which
domains you want to update (UPDATE_DOMAINS). If you add
the key "ALL" into the list, all domains will be updated.

Cron
----
The script does not daemonize and contains no loop. In order 
to automatically update your domains every n minutes, you will
need to run it via crontab, for example:

*/10 * * * *         python2 /home/USER/freedns/freedns.py

This will run the script every 10 minutes



