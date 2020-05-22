import urllib.request
from bs4 import BeautifulSoup

class Scraper:
	def __init__(self,site):
		self.site = site

	def scrape(self):
		r = urllib.request.urlopen(self.site)
		f = open('links.txt','a')
		html = r.read()
		parser = "html.parser"
		sp = BeautifulSoup(html, parser)
		for tag in sp.find_all("a"):
			url = tag.get("href")
			print("\n",url)
			f.write(url+"\n\n")
		f.close()

scrape = Scraper("https://news.google.com")
scrape.scrape()	