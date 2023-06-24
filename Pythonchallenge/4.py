import urllib.request
import re
start_url ="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579"


for i in range(400):

 #   start_url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
    next_url = ""
    pattern = r'\d+'

    response = urllib.request.urlopen(start_url)

    # Read the response contents
    contents = response.read()

    # Decode the contents if necessary
    decoded_contents = contents.decode('utf-8')  # Assuming the content is encoded in UTF-8

    get_next_nothing = re.findall(pattern, decoded_contents)

    start_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(get_next_nothing[0])
    print(start_url)