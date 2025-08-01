# Week 1 Problem Set 1 File Extensions extensions.py

# In a file called extensions.py, implement a program that prompts the user for the name of a file
# and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif .jpg .png .pdf .txt .zip
# If the file’s name ends with some other suffix or has no suffix at all,
# output application/octet-stream instead, which is a common default.

# Acceptance criteria for input giving output as expected is:
# happy.jpg input image/jpeg output
# document.pdf input application.pdf
# Must apply common MIME types (like application/pdf for .pdf not document/pdf):
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types
# Follow string methods available in Python from hint in https://cs50.harvard.edu/python/2022/psets/1/extensions/ :
# https://docs.python.org/3/library/stdtypes.html#string-methods

file_name = input("File name: ").lower().strip()

if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
