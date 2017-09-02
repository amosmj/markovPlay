from bs4 import BeautifulSoup
from urllib.request import Request, urlopen




site= 'https://www.tor.com/2017/08/29/oathbringer-brandon-sanderson-chapter-1-3/'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'lxml')
for paraClass in soup.findAll('p',{'class':'frontmatter'}):
    #print(str(para))
    paraClass.decompose()
for anchor in soup.findAll('a'):
    #print(str(anchor))
    anchor.decompose()
for span in soup.findAll('span'):
    span.decompose()
#soup.span.decompose()
for blockquote in soup.findAll('blockquote'):
    blockquote.decompose()
#soup.blockquote.decompose()
for h3 in soup.findAll('h3'):
    h3.decompose()
for emphasis in soup.findAll('em'):
    emphasis.unwrap()
for ebookstuff in soup.findAll('div',{'class':'ebook-link-wrapper'}):
    ebookstuff.decompose()
for hr in soup.findAll('hr'):
    hr.decompose()
for styledText in soup.findAll('p',{'style':'text-align: center'}):
    styledText.decompose()
for ebookstuff in soup.findAll('div',{'class':'ooter-favorite-wrapper'}):
    ebookstuff.decompose()
mydivs = soup.findAll("div", { "class" : "entry-content" })
for x in soup.find_all():
    if len(x.text) <= 1:
        x.extract()
#print(mydivs)
#for importantDiv in soup.findAll('div'):
#    importantDiv.unwrap()
for para in soup.findAll('p'):
    para.unwrap()

outFile = open('./Oathbringer.txt', 'w')
outFile.write(str(mydivs).strip())