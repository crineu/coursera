#Define a procedure, add_to_index, that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

#If the keyword is already in the index, add the url to the list of urls associated with that keyword.
#If the keyword is not in the index, add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index, keyword, url):
    for element in index:
        if keyword == element[0]:
            element[1].append(url)
            return
    index.append([keyword, [url]])


add_to_index(index, 'udacity', 'http://udacity.com')
add_to_index(index, 'computing', 'http://acm.org')
add_to_index(index, 'udacity', 'http://npr.org')
#print index => [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

print index

# ---

#Define a procedure, lookup, that takes two inputs:
#   - an index
#   - keyword

#The output should be a list of the urls associated with the keyword. If the keyword
#is not in the index, the output should be an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

def lookup(index, keyword):
    for entry in index:
        if keyword == entry[0]:
            return entry[1]
    return []

#lookup(index,'udacity') => ['http://udacity.com','http://npr.org']
print lookup(index, 'udacity')

# ---

#Define a procedure, add_page_to_index, that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

#It should update the index to include all of the word occurences found in the
#page content by adding the url to the word's associated url list.

index = []

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

add_page_to_index(index, 'fake.text', "This is a test")
add_page_to_index(index, 'real.text', "This is not a test")
print index #=> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']], ['test', ['fake.text']]]

print (4300 / 0.1) / 300000


# HOMEWORK

#The built-in <string>.split() procedure works okay, but fails to find all the words on a page
#because it only uses whitespace to split the string. To do better, we should also use punctuation
#marks to split the page into words.

#Define a procedure, split_string, that takes two inputs: the string to split and a string containing
#all of the characters considered separators. The procedure should output a list of strings that break
#the source string up by the characters in the splitlist.

def split_string(source, splitlist):
    words = [source]
    i = 0
    while i < len(splitlist):
        symbol = splitlist[i]
        i = i + 1
        new_words = []
        for word in words:
            new_words = new_words + (word.split(symbol))
        words = new_words
    return filter(None, words)

out = split_string("This is a test-of the,string separation-code!", " ,!-")
print out #=> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out #=> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']


# HOMEWORK 2

#The current index includes a url in the list of urls for a keyword multiple times if the keyword appears
#on that page more than once.

#It might be better to only include the same url once in the url list for a keyword, even if it appears
#many times.

#Modify add_to_index so that a given url is only included once in the url list for a keyword,
#no matter how many times that keyword appears.

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            if url not in entry[1]:
                entry[1].append(url)
            return
    # not found, add new keyword to index
    index.append([keyword, [url]])


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

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

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

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

index = crawl_web("http://www.udacity.com/cs101x/index.html")
print lookup(index,"is") #=> ['http://www.udacity.com/cs101x/index.html']
