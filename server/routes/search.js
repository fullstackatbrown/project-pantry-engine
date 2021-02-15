const {Client} = require('@elastic/elasticsearch')
const client = new Client({ node: 'http://localhost:9200'}) //what will this change to?

// What we have in pantry (ingredients)
// What we need to make it --> how to make the difference

async function query (index_name, body_json){
    let search_result = await client.search({
        index: index_name,
        body: {
            "query": body_json,
            "size": 15
        }
    }).then(response => console.log(response),
        error => alert(`Error: ${error.message}`));

    return search_result
}

// console.log(query('recipe_index', {"match_all":{}}))
