#The code below will help us navigate or move around the html relative to something which we have selected, we can go to the parent, parent of parent or the siblings of the selected alias
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
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")#we have passed the html string in to the beautifulsoup(what we have recieved is not an object or dictionary, it's a string) , html-parser is specified because it supports xml(another markup laguage) also
el = soup.select(".special")[0]
data = soup.body.contents[1]#give the entire content of body in the form of list and every tag is separated by'\n' also the first element is '\n' therefore it starts with 1 and not 0
print(data)
#siblings are the one which are in the same hierarchy level in the avove code div and ol are in the same hierarchy
x = soup.body.contents[1].next_sibling.next_sibling#the first content of the body od div, it's next sibling is \n further its next sibling is ol 
print(x)
y = soup.find(class_="super-special").parent
print(y)
z=soup.find(id="first").find_next_sibling()#instead of using next_sibling if we use find_next_sibling then instead of \n it will give directly give the next sibling
print(z)