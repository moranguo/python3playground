from urllib.request import urlopen
from html.parser import HTMLParser

def isjob(url):
    try:
        #print(url)
        a, b, c, d = url.split('/')
    except ValueError:
        return False
    return a == d == '' and b == 'jobs' and c.isdigit()

class Scraper(HTMLParser):
    in_link = False

    def handle_starttag(self, tag, attrs):
        #print(type(attrs))
        #print(attrs)
        # attrs is a list of tuple, for example, [('href', '/jobs/3638/')]
        # [('href', '/jobs/type/image-processing/'), ('title', 'More Image Processing jobs')]
        attrs = dict(attrs)
        url = attrs.get('href', '')
        if tag == 'a' and isjob(url):
            self.url = url
            self.in_link = True
            self.chunks = []

    def handle_data(self,data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_link:
            print('{}({})'.format(''.join(self.chunks), self.url))
            self.in_link = False

text = urlopen('http://python.org/jobs').read().decode()
parser = Scraper()
parser.feed(text)
parser.close()