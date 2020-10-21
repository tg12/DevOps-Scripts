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



import dns.zone
# note
################################################################
# http://www.dnspython.org/docs/1.14.0/dns.rdatatype-module.html
# NONE = 0
# A = 1
# NS = 2
# MD = 3
# MF = 4
# CNAME = 5
# SOA = 6
# MB = 7
# MG = 8
# MR = 9
# NULL = 10
# WKS = 11
# PTR = 12
# HINFO = 13
# MINFO = 14
# MX = 15
# TXT = 16
# RP = 17
# AFSDB = 18
# X25 = 19
# ISDN = 20
# RT = 21
# NSAP = 22
# NSAP_PTR = 23
# SIG = 24
# KEY = 25
# PX = 26
# GPOS = 27
# AAAA = 28
# LOC = 29
# NXT = 30
# SRV = 33
# NAPTR = 35
# KX = 36
# CERT = 37
# A6 = 38
# DNAME = 39
# OPT = 41
# APL = 42
# DS = 43
# SSHFP = 44
# IPSECKEY = 45
# RRSIG = 46
# NSEC = 47
# DNSKEY = 48
# DHCID = 49
# NSEC3 = 50
# NSEC3PARAM = 51
# TLSA = 52
# HIP = 55
# CDS = 59
# CDNSKEY = 60
# CSYNC = 62
# SPF = 99
# UNSPEC = 103
# EUI48 = 108
# EUI64 = 109
# TKEY = 249
# TSIG = 250
# IXFR = 251
# AXFR = 252
# MAILB = 253
# MAILA = 254
# ANY = 255
# URI = 256
# CAA = 257
# TA = 32768
# DLV = 32769

ids = [
    'NONE',
    'A',
    'NS',
    'MD',
    'MF',
    'CNAME',
    'SOA',
    'MB',
    'MG',
    'MR',
    'NULL',
    'WKS',
    'PTR',
    'HINFO',
    'MINFO',
    'MX',
    'TXT',
    'RP',
    'AFSDB',
    'X25',
    'ISDN',
    'RT',
    'NSAP',
    'NSAP-PTR',
    'SIG',
    'KEY',
    'PX',
    'GPOS',
    'AAAA',
    'LOC',
    'NXT',
    'SRV',
    'NAPTR',
    'KX',
    'CERT',
    'A6',
    'DNAME',
    'OPT',
    'APL',
    'DS',
    'SSHFP',
    'IPSECKEY',
    'RRSIG',
    'NSEC',
    'DNSKEY',
    'DHCID',
    'NSEC3',
    'NSEC3PARAM',
    'TLSA',
    'HIP',
    'CDS',
    'CDNSKEY',
    'CSYNC',
    'SPF',
    'UNSPEC',
    'EUI48',
    'EUI64',
    'TKEY',
    'TSIG',
    'IXFR',
    'AXFR',
    'MAILB',
    'MAILA',
    'ANY',
    'URI',
    'CAA',
    'TA',
    'DLV',
]


with open(r'\able.txt', 'r') as myfile:
    data = myfile.read()
# print (data)

zone = dns.zone.from_text(data, origin='able.', check_origin=False)
# print (zone)

for each in ids:
    try:
        print("#####################" + str(each) + "########################")
        for (name, rdataset) in zone.iterate_rdatasets(each):
            for rdata in rdataset:
                print(name)
                print(rdata.address)
                # print(rdata) #what else is in here?
        print("#####################" + str(each) + "########################")
    except:
        pass
