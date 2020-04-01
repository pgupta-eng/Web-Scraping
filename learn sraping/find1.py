#this is a basic code to understand beautiful soup
#this code demonstaretes : selecting with beautifulsoup: find()
#ways in which we can navigate html: by tag name,.... using find()......css selectors 
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

###########################finding the tags##########################################################################
print(soup)#returns the html string
print(soup.body)#returns the body part of html
print(soup.body.div)#returns the div from the body, there are 2 divs but it will return the first one
print(soup.find("div"))#finds both the divs,this returns the bs4 element, it is not 
print(soup.find_all("div"))#gives the output in the form of list i.e. both the div elements will be obtained in a list
#d = soup.select("[data-example]")
#print(d)
#####################################################################################################################

############################finding the attributes####################################################################### 
p = soup.find(id="first")#attribute of div
z = soup.find_all(class_="special")#the attribute of li class is written as class_ because class is already a keyword in python..more than one elements are found therefore the output is in the form of list
print(z)