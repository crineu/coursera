# import urllib
# def get_page(url):
#     try:
#         return urllib.urlopen(url).read()
#     except:
#         return ""

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return  '<html> <body> This is a test page for learning to crawl! <p> It is a good idea to  <a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a> before you try to  <a href="http://www.udacity.com/cs101x/walking.html">walk</a> or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. </p> </body> </html> '
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return  '<html> <body> I have not learned to crawl yet, but I am quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>. </body> </html>'
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '<html> <body> I cant get enough  <a href="http://www.udacity.com/cs101x/index.html">crawling</a>! </body> </html>'
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '<html> <body> The magic words are Squeamish Ossifrage! </body> </html>'
    except:
        return ""
    return ""


def get_next_target(s):
	start_link = s.find('<a href=')
	if -1 == start_link:
		return None, 0
	start_quote = s.find('"', start_link)
	end_quote = s.find('"', start_quote + 1)
	url = s[start_quote + 1:end_quote]
	return url, end_quote

def get_all_links(page):
	links = []
	while (page):
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			page = None
	return links

def union(list_a, list_b):
	for e in list_b:
		if e not in list_a:
			list_a.append(e)

def add_to_index(index, keyword, url):
	for element in index:
		if keyword == element[0]:
			element[1].append(url)
			return
	index.append([keyword, [url]])

def lookup(index, keyword):
	for entry in index:
		if keyword == entry[0]:
			return entry[1]
	return []

def add_page_to_index(index, url, content):
	words = content.split()
	for word in words:
		add_to_index(index, word, url)

def crawl_web_max_pages(seed, max_pages):
	tocrawl = [seed]
	crawled = []
	while tocrawl and len(crawled) < max_pages:
		page = tocrawl.pop()
		if page not in crawled:
			union(tocrawl, get_all_links(get_page(page)))
			crawled.append(page)
	return crawled

def crawl_web_max_depth(seed, max_depth):
	tocrawl = [seed]
	crawled = []
	next_depth = []
	depth = 0
	while tocrawl and depth <= max_depth:
		page = tocrawl.pop()
		if page not in crawled :
			union(next_depth, get_all_links(get_page(page)))
			crawled.append(page)
		if not tocrawl:
			tocrawl, next_depth = next_depth, []
			depth = depth + 1
	return crawled


def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index, page, content)
			union(tocrawl, get_all_links(content))
			crawled.append(page)
	return index



source = 'http://www.udacity.com/cs101x/index.html'
print crawl_web(source)
# print crawl_web(source, 2)

