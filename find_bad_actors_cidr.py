#!/usr/bin/env python

import re
import socket, struct
import datetime

ips = []

with open("merged-file3") as f:
    for line in f:
        try:
            line = line.rstrip('\n')
            socket.inet_aton(line)
            ips.append(str(line))
        except socket.error:
            pass

# print (ips)
raw_rules_set = []
tmp_lst = []
raw_rules_set_dist = []
count = 0

for ip in ips:
    try:
        # print ("iptables -A OUTPUT -s " + str(ip) + "/32 -d 0/0 -j DROP; iptables -A OUTPUT -s " + str(ip) + "/32 -d 0/0 -j LOG --log-prefix 'firehol-iptables-rule-js")
        print ("checking ... " + str(ip))
        count = count + 1
        print (str(count) + "/" + str(len(ips)))
        iptables_rule = str("-A OUTPUT -s " + str(ip) + "/32 -d 0/0 -j DROP") 
        raw_rules_set_dist.append(iptables_rule)
        iptables_rule = "-A OUTPUT -s " + str(ip) + "/32 -d 0/0 -j LOG --log-prefix 'firehol-iptables-rule-js'"
        raw_rules_set_dist.append(iptables_rule)
        # print(datetime.datetime.now().time())
    except Exception as e: 
        print(e)
        pass

for iptable_rule in raw_rules_set_dist:
    print(iptable_rule)
    print(datetime.datetime.now().time())

# with open('/etc/iptables/rules.v4', 'a') as f:
with open('iptables_rules.txt', 'w') as f:
    for item in raw_rules_set_dist:
        f.write("%s\n" % item)

f.close()