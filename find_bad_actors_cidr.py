'''THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE AND
NON-INFRINGEMENT. IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR ANYONE
DISTRIBUTING THE SOFTWARE BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

# Bitcoin Cash (BCH)   qpz32c4lg7x7lnk9jg6qg7s4uavdce89myax5v5nuk
# Ether (ETH) -        0x843d3DEC2A4705BD4f45F674F641cE2D0022c9FB
# Litecoin (LTC) -     Lfk5y4F7KZa9oRxpazETwjQnHszEPvqPvu
# Bitcoin (BTC) -      34L8qWiQyKr8k4TnHDacfjbaSqQASbBtTd

# contact :- github@jamessawyer.co.uk



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