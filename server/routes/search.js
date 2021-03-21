const {Client} = require('@elastic/elasticsearch')
const client = new Client({ node: 'http://localhost:9200'})

// What we have in pantry (ingredients)
// What we need to make it --> how to make the difference

// issues: better method of searching several values than 'terms'
//      --> 'should' clauses pop up a lot, but how would I avoid hard coding?

var should_a = {
    'bool': {
        "should": create_ingredients_json(['beef', 'soy sauce'])
    }
}

// array(string) --> array(JSON)
function create_ingredients_json(ing_arr){
    for (let i = 0; i<ing_arr.length; i++){
        ing_arr[i] = {"match": {"ingredients": ing_arr[i]}}
    }
    return ing_arr
}

// string, string --> JSON
async function query (index_name, body_json){
    let search_result = await client.search({
        index: index_name,
        body: {
            "query": body_json,
            "size": 15
        }
    }).then(function(response){
        return response
    }, function(err){
        console.trace(err.message)
    });

    return search_result
}

(async function() {
    let results = await query('recipe_index', should_a)
    console.log (results.body.hits.hits)
})();
