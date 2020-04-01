
#from a website (https://www.rithmschool.com/blog) we will be selecting the anchor tag within which a tag and the contents will selected
import requests
# we will make the request, take the html response back and give it to beautiful soup
# navigate through it get extract the data we want and write it to a file through csv
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
#go to the link provided: inspect the headers we will find that these are enclosed in a tag named <article>
#so the plan is to select all the article tags and then select the h4 tags within it
#print(response.text)# the entire html file is given in the form of a string
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
#print(articles)#returns all the article tags
####################csv file###############################################################################
#we have openes a file named blog_data.csv in write mode
with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title" "link" "date"])
##############################printing the titles, the urls from the site and the date ##############################
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()#returns the content of all the anchor tags, and hence we get the output of all the links  
        url = a_tag['href']
        date = article.find("time")["datetime"]#here we are extracting the time which is available in side the time tag which is further inside article tag the date and time is available inside the attribute datetime which is accessed using the sq brackets
        csv_writer.writerow([title, url, date])#csv writer works in the form of list and we are passing the variables
        #prints all the urls available inside the article tag using square bracket we can access the attributes and hence the url
