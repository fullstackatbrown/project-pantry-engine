import elasticsearch as es

client = es.Elasticsearch()  # http://localhost:9200

'''
Note the commented lines below. 

The two immediately below will delete the indices themselves (and they will therefore
need to be recreated for the next).

The next two clear out all documents from each

Somewhat a copy of Sami's recipe-browser/RecipeScraper/data_models.py
'''

query = {'query': {'match_all': {}}}

# print(client.indices.delete("recipe_index"))
# print(client.indices.delete("url_index"))

# print(client.delete_by_query(index="recipe_index", body=query))
# print(client.delete_by_query(index="url_index", body=query))

ri_hits = (client.search(body=query, index='recipe_index'))['hits']['hits']
ui_hits = (client.search(body=query, index='url_index'))['hits']['hits']

if len(ri_hits) == 0:
    print('\'recipe_index\' is clear')
if len(ui_hits) == 0:
    print('\'url_index\' is clear')

