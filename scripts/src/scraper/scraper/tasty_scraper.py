from selenium import webdriver
from .base_scraper import Scraper, Recipe
from typing import Iterable, Optional
import re

class TastyScraper(Scraper):
  """Scraper for tasty.co
  """
  
  HOME_URL = "https://tasty.co/"
  
  def _is_compilation(self, url : str) -> bool:
    return self.HOME_URL + "compilation/" in url
  
  def _process_compilation(self, url : str) -> str:
    self.driver.execute_script(f"window.open('{url}');")
    self.driver.switch_to.window(self.driver.window_handles[-1])
    
    compilation_containers = self.driver.find_elements_by_class_name("compilation-recipes")
    for compilation_container in compilation_containers:
      feed_items = compilation_container.find_elements_by_class_name("feed-item")
      for feed_item in feed_items:
        yield feed_item.get_attribute("href")
        
    self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[-1])
    
  def recipe_links(self) -> Iterable[str]:
    self.driver.get(self.HOME_URL)
    
    next_container_id = 0
    
    while True:
      feed_containers = self.driver.find_elements_by_class_name("feed__container")
      for feed_container in feed_containers[next_container_id:]:
        feed_items = feed_container.find_elements_by_class_name("feed-item")
        for feed_item in feed_items:
          url = feed_item.get_attribute("href")
          if self._is_compilation(url):
            yield from self._process_compilation(url)
          else:
            yield url 
        next_container_id += 1
      
      try:  
        more_button = self.driver.find_element_by_xpath("//*[text()='Show more']")
      except:
        break
      
      more_button.click()
      
    self.driver.close()

  def _get_image(self):
    results = self.driver.find_elements_by_class_name("vjs-poster")
    if len(results) > 0:
      poster = results[0]
      style = poster.get_attribute("style")
      img_url = re.search(r"url\(\"(.*)\"\)", style).group(1)
      return img_url[:img_url.find("?")]

    results = self.driver.find_elements_by_css_selector(".non-video img")
    if len(results) > 0:
      img = results[0]
      img_url = img.get_attribute("src")
      return img_url[:img_url.find("?")]

    return None

  def parse_recipe(self, url: str, image_url : Optional[str] = None) -> Recipe:
    self.driver.execute_script(f"window.open('{url}');")
    self.driver.switch_to.window(self.driver.window_handles[-1])
    
    title = self.driver.find_element_by_class_name("recipe-name").text
    
    ingredient_names = []
    ingredients = self.driver.find_elements_by_class_name("ingredient")
    for ingredient in ingredients:
      ingredient_names.append(ingredient.text)

    img_url = self._get_image()
    self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[-1])
    
    return Recipe(url, title, ingredient_names, img_url)