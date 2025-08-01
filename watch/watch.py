# Week 7 Regular Expressions Problem Set 7 Watch on YouTube watch.py
#
# In a file called watch.py, implement a function called parse that expects a str of HTML as input,
# extracts any YouTube URL that’s the value of a src attribute of an iframe element therein,
# and returns its shorter, shareable youtu.be equivalent as a str.
# Expect that any such URL will be in one of the formats below.
# Assume that the value of src will be surrounded by double quotes.
# And assume that the input will contain no more than one such URL.
# If the input does not contain any such URL at all, return None.
#
# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0
# Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
# but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
#
# import re
# import sys
#
# def main():
#     print(parse(input("HTML: ")))
#
#
# def parse(s):
#     ...
#
# if __name__ == "__main__":
#     main()
#
# Hints
# Recall that the re module comes with quite a few functions, per docs.python.org/3/library/re.html, including search.
# Recall that regular expressions support quite a few special characters, per docs.python.org/3/library/re.html#regular-expression-syntax.
# Because backslashes in regular expressions could be mistaken for escape sequences (like \n),
# best to use Python’s raw string notation for regular expression patterns. Just as format strings are prefixed with f,
# so are raw strings prefixed with r. For instance, instead of "harvard\.edu", use r"harvard\.edu".
# Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a “match object,” per
# docs.python.org/3/library/re.html#match-objects, wherein matches are 1-indexed, which you can access individually with group,
# per docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, per docs.python.org/3/library/re.html#re.Match.groups.
# Note that * and + are “greedy,” insofar as “they match as much text as possible,”
# per docs.python.org/3/library/re.html#regular-expression-syntax.
# Adding ? immediately after either, a la *? or +?, “makes it perform the match in non-greedy or minimal fashion;
# as few characters as possible will be matched.”
#
# How to Test
# Here’s how to test your code manually:
#
# Run your program with python watch.py. Ensure your program prompts you for HTML, then copy/paste the below:
# <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# Press enter and your program should output https://youtu.be/xvFZjo5PgG0.
# Notice how, though the src attribute is prefixed with http://www.youtube.com/embed/,
# the resulting link is prefixed with https://youtu.be/.
#
# Run your program with python watch.py. Ensure your program prompts you for HTML, then copy/paste the below:
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# Press enter and your program should still output https://youtu.be/xvFZjo5PgG0.

# Run your program with python watch.py. Ensure your program prompts you for HTML, then copy/paste the below:
# <iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>
# Press enter and your program should output None. Notice how the src attribute doesn’t point to a YouTube link!
#
import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # test regex online with <iframe(.)*><\/iframe> at https://regex101.com/
    if re.search(r"<iframe(.)*><\/iframe>", s):
        # test regex online with (http)(s)*:\/\/(www\.)*youtube\.com\/embed\/([a-z_A-Z_0-9]+) at https://regex101.com/
        url_pattern = re.search(r"(http)(s)*:\/\/(www\.)*youtube\.com\/embed\/([a-z_A-Z_0-9]+)", s)
        if url_pattern:
            split_url = url_pattern.groups()
            # updated return to give correct format
            return "https://youtu.be/" + split_url[3]

if __name__ == "__main__":
    main()
