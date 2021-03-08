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

print("Clearing recipe_index")
client.delete_by_query(index="recipe_index", body=query)
client.indices.delete("recipe_index")
print("Done")