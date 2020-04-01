#selecting using css selectors, using select()
#when we use find()- we get the element, when we use find_all we get a list and ehrn we use select() we get the list bach
#this is a basic code to understand beautiful soup

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

##############################selection using the css selector############################################
d= soup.select("#first")#the select keyword gives the output in the form of a list
p= soup.select("#first")[0]#using the index we will no longer get the output in the form of a list we will get the element
print(p)
z= soup.select("[data-example]")# for selecting attribute square brackets are used 
print(z)
m=soup.select(".special")#for selecting the classes . is used this is better s compared to find_all because it's shorter
print(m)
j=soup.select("div")#selection using tag name
################################################################################################################