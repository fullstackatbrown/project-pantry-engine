import elasticsearch as es

"""
Notably, 'ConnectionRefusedError: Errno 61' probably == make sure Elasticsearch is running 
    (ie, cmd/ terminal --> elasticsearch, or brew services start elasticsearch, etc.)
"""


# Somewhat a copy paste of Sami's recipe-browser/RecipeScraper/RecipeIndexer.py

class RecipeIndex:
    client = es.Elasticsearch()  # http://localhost:9200
    url_index_conf = {

    }
    recipe_index_conf = {

    }
    try:
        print(client.indices.create("recipe_index"))
    except es.exceptions.RequestError:
        print("\'recipe_index\' already exists.")

    try:
        print(client.indices.create("url_index"))
    except es.exceptions.RequestError:
        print("\'url_index\' already exists.")

    # constructor passed for now
    def __init__(self):
        pass

    # Sami had url: str, title: str, and ingredients: [str]
    # makes sense for us to use those standards.
    def insert_recipe(self, url, title, ingredients):
        #type: (str, str, str) -> None
        t_doc_recipe = {
            'url': url,
            'title': title,
            'ingredients': ingredients,
        }

        print(self.client.index('recipe_index', body=t_doc_recipe))

    def delete_recipe(self, url):
        # type: (str) -> None
        print(self.client.delete_by_query(index='recipe_index', body={'query': {'match_all': {'url': url}}))

    # Original method takes url: str, host: str (ie, Tasty, NYT cooking, etc.) and presumably
    # html: str as args. Passed for now
    def insert_url(self, url, host, html):
        # type: (str, str, str) -> None
        t_doc_url = {
            'url': url,
            'host': host,
            'html_string': html,
        }
        print(self.client.index('url_index',body=t_doc_url))


    def delete_url(self, url):
        # type: (str) -> None
        print(self.client.delete_by_query(index='recipe_index', body={'query': {'match_all': {'url': url}}}))

