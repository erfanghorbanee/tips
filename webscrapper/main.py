from bs4 import BeautifulSoup
import requests

search = input("Enter search terms: ")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
#print(soup.prettify())
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    item_description = item.find("div", {"class": "b_caption"}).find("p").text
    # item_description = item.find("p").text  --har do item_description kar mikonad.
    
    
    if item_text and item_href and item_description:
        print(item_text)
        print(item_href)
        print(item_description)
        print("------------------------------------------")
        #print("parent:", item.find("a").parent)
        #children = item.find("h2")
        #print("nex sibling of the h2: ", children.next)
        