from selenium import webdriver

class TastyScraper:
  """Scraper for tasty.co
  """
  
  HOME_URL = "https://tasty.co/"
  
  def __init__(self):
    self.driver = webdriver.Chrome()
  
  def _is_compilation(self, url):
    return self.HOME_URL + "compilation/" in url
  
  def _process_compilation(self, url):
    self.driver.execute_script(f"window.open('{url}');")
    self.driver.switch_to.window(self.driver.window_handles[-1])
    
    compilation_containers = self.driver.find_elements_by_class_name("compilation-recipes")
    for compilation_container in compilation_containers:
      feed_items = compilation_container.find_elements_by_class_name("feed-item")
      for feed_item in feed_items:
        yield feed_item.get_attribute("href")
        
    self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[0])
    
  def recipe_links(self):
    self.driver.get(self.HOME_URL)
    print(self.driver.current_window_handle)
    
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