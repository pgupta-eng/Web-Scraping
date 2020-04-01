#in the selection code we learnt to select a particular part of the html code but if we want to access just the text/data of the html code then following changes will be made
from bs4 import BeautifulSoup
#html is the variable wherein we have passed the html *** we will suppose that we have recieved the below html file after making a request.
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")#we have passed the html string in to the beautifulsoup(what we have recieved is not an object or dictionary, it's a string) , html-parser is specified because it supports xml(another markup laguage) also
el = soup.select(".special")[0]
print(el.get_text())#get_text function retrieves the inner text from that object
for el in soup.select(".special"):
  print(el.get_text())#this will display all the inner text having a class named special
  #print(el.name())#returns the name of the tag of the class named special
attr = soup.find("div")["id"]#get the attribute name of the class named special
print(attr)