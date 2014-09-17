# print 'udacity'
# print 'udacity'[3 + 1]
# print 'udacity'[2:4]  # initial : final position
# print 'udacity'[:4]       # until position 4
# print 'udacity'[2:]       # until the end

# s = 'audacity'
# print 'U' + s[2:]

pythagoras = "There is geometry in the humming of the strings, there is music in the spacing of the spheres"
print pythagoras.find('string')
print pythagoras[40:]
print pythagoras.find('T')
print pythagoras.find('inexistent') # returns -1
print pythagoras.find('')           # returns 0

print pythagoras.find('the', 22)    # from that position on


# Extract a link from a page
page = '<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://www.xkcd.com">'

start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1:end_quote]

print url

#Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
#write Python code that prints out udacious without using any quote characters in your code.
print s[:-2] + t[-3:]

#Write Python code that prints out the position
#of the second occurrence of 'zip'
#in text, or -1 if it does not occur
#at least twice.

#For example,
#   text = 'all zip files are zipped' -> 18
#   text = 'all zip files are compressed' -> -1

text = "all zip files are zipped"

first = text.find('zip')
print text.find('zip', first + 1)

#Given a variable, x, that stores the value of any decimal number,
#write Python code that prints out the nearest whole number to x.
#You can assume x is not negative.

# x = 3.14159 -> 3 (not 3.0)
# x = 27.63 -> 28 (not 28.0)
x = 3.14159
x = x + 0.5
decimal = str(x).find('.')
print str(x)[:decimal]