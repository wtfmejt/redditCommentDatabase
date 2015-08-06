# BeautifulSoup mess-around script
# Nicolas Hahn

import markdown2 as md
from bs4 import BeautifulSoup as bs

# body = (open('sampleBody','r')).read()
body = """
# header1
## header2
### header3 #######

*italic ~nested strikethrough~ more italic*
"""

def convertAndClean(body):
	body = body.replace('&gt;','>')
	body = body.replace('&amp;','&')
	body = body.replace('&lt;','<')
	body = md.markdown(body)
	body = body.replace('<p>','')
	body = body.replace('</p>','')
	return body

mdbody = convertAndClean(body)

bsbody = bs(mdbody, 'html.parser')
print(bsbody.prettify())