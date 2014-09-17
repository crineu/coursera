def find_second(text, search):
	first = text.find(search)
	return text.find(search, first + 1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"
# print find_second(danton, 'audace')

def bigger(a, b):
	if a > b:
		return a
	else:
		return b

def biggest(a, b, c):
	return bigger(a, bigger(b,c))

# print biggest(6, 2, 3)
# print biggest(6, 2, 7)

def print_numbers(number):
	i = 1
	while i <= number:
		print i
		i = i + 1

# print_numbers(8)

def factorial(n):
	fac = 1
	while n > 1:
		fac = fac * n
		n = n - 1
	return fac

# -----

def get_next_target(s):
	start_link = s.find('<a href=')
	if -1 == start_link:
		return None, 0
	start_quote = s.find('"', start_link)
	end_quote = s.find('"', start_quote + 1)
	url = s[start_quote + 1:end_quote]
	return url, end_quote

def print_all_links(page):
	while (page):
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			page = None

ppage = '<head prefix="og: http://ogp.me/ns#  http://ogp.me/ns/fb# githubog: http://ogp.me/ns ineu/udacity</title> <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" /> <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" /> <link rel="apple-touch-icon-precomposed" sizes="57x57" <a href="apple-touch-icon-114.png" /> <link rel="apple-touch-icon-precomposed" sizes="114x114" href="apple-touch-icon-114.png" /> <link rel="apple-touch-icon-precomposed" sizes="72x72" href="apple-touch-icon-144.png" /> <link rel="apple-touch-icon-pr"msapplication-TileColor" content="#ffffff"> <link rel="icon" type="image/x-icon" <a href="/favicon.ico" />'

print_all_links(ppage)

### HOMEWORK ###

def median(a, b, c):
	maximum = biggest(a, b, c)
	if maximum == a:
		return bigger(b, c)
	if maximum == b:
		return bigger(a, c)
	if maximum == c:
		return bigger(b, a)

# print median(7,9,7)
# print median(8,7,6)

def countdown(positive):
	while positive > 0:
		print positive
		positive = positive - 1
	print 'Blastoff'

# countdown(3)

def find_last(string, search_string):
	location = string.find(search_string)
	last_good_location = location
	while location > -1:
		last_good_location = location
		location = string.find(search_string, location + 1)
	return last_good_location

# print find_last("bbbbbbasdfasd fadsb", "sb")

def print_multiplication_table(n):
	left = 1
	while left <= n:
		right = 1
		while right <= n:
			print str(left) + ' * ' + str(right) + ' = ' + str(left * right)
			right = right + 1
		left = left + 1	

print_multiplication_table(3)
