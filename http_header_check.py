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



import requests.exceptions
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib
import re
from fake_useragent import UserAgent
import requests
import urllib3
from collections import defaultdict
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def leaders(xs, top=10):
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)

    return u" ".join(t.strip() for t in visible_texts)


def tag_visible(element):
    if element.parent.name in [
        'style',
        'script',
        'head',
        'title',
        'meta',
            '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


word_list = []  # all sites, all of the time
unique_headers_list = []

# add code to loop round list of urls

try:
    r = requests.get('', verify=False)
    r.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xxx
except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
    print("Down")
except requests.exceptions.HTTPError:
    print("4xx, 5xx")
else:
    print("HTTP 200 OK!")
################################################
    # Proceed to do stuff with `r`
    # print (r.content)
    # print (r.text)
################################################
    urls_to_parse = []
    soup = BeautifulSoup(r.text)
    for link in soup.findAll(
        'a', attrs={
            'href': re.compile("^https://")}):
        # print(link.get('href'))
        urls_to_parse.append(link.get('href'))
    for link in soup.findAll(
        'a', attrs={
            'href': re.compile("^http://")}):
        # print(link.get('href'))
        urls_to_parse.append(link.get('href'))
    print(urls_to_parse)
################################################
    for url in urls_to_parse:
        try:
            r = requests.get(url, verify=False)
            r.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xxx
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            print("Down")
        except requests.exceptions.HTTPError:
            print(str(url) + "....4xx, 5xx")
        else:
            print(str(url) + "....HTTP 200 OK!")
            try:
                print(r.headers['Server'])
                if str(r.headers['Server']) not in unique_headers_list:
                    unique_headers_list.append(str(r.headers['Server']))
            except BaseException:
                print("No header information returned!")
                pass
            # word_list.extend(text_from_html(r.text).split())
################################################
    # counts = {}
    # for n in word_list:
        # counts[n] = counts.get(n, 0) + 1
    # print (leaders(counts))
################################################

print(unique_headers_list)
# print (pd.Series(word_list).value_counts())
