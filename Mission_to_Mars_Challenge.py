#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[ ]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


# Set up HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images
# 

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)
browser


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html


# In[ ]:





# In[ ]:





# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[118]:


# 1. Use browser to visit the URL 
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'
browser.visit(url)


# In[119]:


# # Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')

# Find HTML tag that holds all links
tag_box =html_soup.find('div', class_='collapsible results')
tags = tag_box.find_all('div', class_='item')


# In[120]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Iterate through tags 
for tag in tags:
#     tag.html
    # Create an empty dictionary 
    hemispheres = {}
    # Clicking on Hemisphere link
    elem = tag.find('h3').text
    browser.click_link_by_partial_text(elem)
    # Parsing new generated browser
    html = browser.html
    img_soup = soup(html, 'html.parser')
    # Finding url
    url = img_soup.find('div', class_='downloads').find('a').get('href')
    # Adding base url
    img_url = f'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/{url}'
    # Finding title
    title = img_soup.find('h2',class_='title').text
    # Creating Dictionary 
    hemispheres = {'img_url' : img_url,
                   'title': title}
    # Adding dictionary to list 
    hemisphere_image_urls.append(hemispheres)
    # Returning to previous page
    browser.back()


# In[121]:


hemisphere_image_urls


# In[ ]:




