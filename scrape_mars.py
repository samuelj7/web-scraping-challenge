
from flask import Flask, render_template
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import os
import requests
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    #Visit website
    url = "https://redplanetscience.com/"
    browser.visit(url)
    #time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find_all('div', class_='content_title')
    news_title

    paragraphs =soup.find_all('div', class_='article_teaser_body')
    first_paragraph = paragraphs[0].text

    #Featured Image
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html = browser.html
    soup_v2 = bs(html, 'html.parser')
    img = soup_v2.find('img', class_='headerimage fade-in')['src']
    mars_img = url + img
    mars_img

    #Mars Facts
    url_3 = 'https://galaxyfacts-mars.com/'
    browser.visit(url_3)

    table_string = pd.read_html(url_3)
    table_string
    df= table_string[0]
    df
    df_html = df.to_html()
    df_html
    html_table = df_html.replace('\n', ' ')
    html_table

    #Mars Hemisphere
    #First Hemisphere
    url_4 = 'https://marshemispheres.com/'
    browser.visit(url_4)
    html = browser.html
    soup = bs(html, 'html.parser')
    browser.find_by_text('Cerberus Hemisphere Enhanced').click()
    image = browser.find_by_tag('img')[4]
    image['src']
    title_hemisphere = browser.find_by_tag('h2')
    title_hemisphere.text
    hemisphere_list = []
    hemisphere_image_urls= {}
    hemisphere_image_urls['Title'] = title_hemisphere.text
    hemisphere_image_urls['img_url'] = image['src']
    hemisphere_image_urls
    hemisphere_list.append(hemisphere_image_urls)
    hemisphere_list

    #Hemisphere 2
    browser.back()
    browser.find_by_text('Schiaparelli Hemisphere Enhanced').click()
    image_2 = browser.find_by_tag('img')[4]
    image_2['src']
    title_hemisphere_2 = browser.find_by_tag('h2')[0]
    title_hemisphere_2.text
    hemisphere_image_urls_2 ={}
    hemisphere_image_urls_2['Title'] = title_hemisphere_2.text
    hemisphere_image_urls_2['img_url'] = image_2['src']
    hemisphere_image_urls_2
    hemisphere_list.append(hemisphere_image_urls_2)
    hemisphere_list 

    #Hemisphere 3
    browser.back()
    browser.find_by_text('Syrtis Major Hemisphere Enhanced').click()
    image_3 = browser.find_by_tag('img')[4]
    image_3['src']
    title_hemisphere_3 = browser.find_by_tag('h2')[0]
    title_hemisphere_3.text
    hemisphere_image_urls_3 = {}
    hemisphere_image_urls_3['Title'] = title_hemisphere_3.text
    hemisphere_image_urls_3['img_url'] = image_3['src']
    hemisphere_image_urls_3
    hemisphere_list.append(hemisphere_image_urls_3)
    hemisphere_list

    #Hemisphere 4
    browser.back()
    browser.find_by_text('Valles Marineris Hemisphere Enhanced').click()
    image_4 = browser.find_by_tag('img')[4]
    image_4['src']
    title_hemisphere_4 = browser.find_by_tag('h2')[0]
    title_hemisphere_4.text
    hemisphere_image_urls_4 = {}
    hemisphere_image_urls_4['Title'] = title_hemisphere_4.text
    hemisphere_image_urls_4['img_url'] = image_4['src']
    hemisphere_image_urls_4
    hemisphere_list.append(hemisphere_image_urls_4)
    hemisphere_list

    browser.quit()

    data = {'news_title': news_title,
            'mars_img': mars_img,
            'html_table': html_table,
            'hemisphere_list': hemisphere_list
            }
    print(data)
    return data
    









