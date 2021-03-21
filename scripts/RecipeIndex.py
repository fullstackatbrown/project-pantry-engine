import elasticsearch as es
from src.scraper.scraper.base_scraper import Recipe

class RecipeIndex:
    client = es.Elasticsearch()  # http://localhost:9200

    try:
        print(client.indices.create("recipe_index"))
    except es.exceptions.RequestError:
        print("\'recipe_index\' already exists.")

    def insert_recipe(self, recipe: Recipe):
        t_doc_recipe = {
            'url': recipe.url,
            'title': recipe.name,
            'ingredients': recipe.ingredients,
            'img_url': recipe.img_url
        }

        self.client.index('recipe_index', body=t_doc_recipe, id=recipe.url)

    def delete_recipe(self, url: str):
        self.client.delete_by_query(index='recipe_index', body={'query': {'match_all': {'url': url}}})
