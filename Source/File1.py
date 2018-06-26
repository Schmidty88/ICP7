from bs4 import BeautifulSoup
import urllib.request

# pulling url and and setting it to a variable to be called
url = "https://en.wikipedia.org/wiki/Python"
source = urllib.request.urlopen(url)
soup = BeautifulSoup(source, "html.parser")

# this loop is extracting all the data in the source
for s in soup(["s", "style"]):
    s.extract()

source = soup.get_text()

# here we are looking at the lines then after we do that we look at the chumks of source
lines = (line.strip() for line in source.splitlines())
c = (phrase.strip() for line in lines for phrase in line.split(" "))

fh = open('input.txt', 'w', encoding="utf-8")
# this part of code is to be sure that the chunks being brought together after the split
source = '\n'.join(chunk for chunk in c if chunk)
fh.write(source)
fh.close
print(source)
