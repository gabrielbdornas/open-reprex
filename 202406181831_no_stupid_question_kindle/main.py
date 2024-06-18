from bs4 import BeautifulSoup
import requests
from markdownify import MarkdownConverter
from markdown_pdf import MarkdownPdf
from markdown_pdf import Section

def webpage_to_markdown(url):
  """
  This function takes a url of a webpage as input and returns the markdown format of the webpage content.

  Args:
    url: The url of the webpage to convert.

  Returns:
    A string containing the markdown format of the webpage content.
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  podcast_div = soup.find(class_="podcast")
  if podcast_div:
    return podcast_div
  else:
    return "Podcast content not found."

# Example usage
url = "https://freakonomics.com/podcast/whats-the-difference-between-sympathy-and-empathy/"
markdown_content = webpage_to_markdown(url)
content = MarkdownConverter().convert_soup(markdown_content)
with open('teste.md', 'w') as file:
    file.write(content)
# import ipdb; ipdb.set_trace(context=10)
pdf = MarkdownPdf(toc_level=2)
pdf.add_section(
   Section(content, toc=False),
   user_css="body {text-align:justify;}",
   )
pdf.save('teste.pdf')
