const {Client} = require('@elastic/elasticsearch')
const client = new Client({ node: 'http://localhost:9200'})

// array(string) --> array(JSON)
function createIngredientsJson(ing_arr){
    for (let i = 0; i<ing_arr.length; i++){
        ing_arr[i] = {'match': {'ingredients': ing_arr[i]}}
    }
    return ing_arr
}

// string, string --> JSON
async function query (index_name, ing_arr){
    let search_result = await client.search({
        index: index_name,
        body: {
            'query': {
                'bool':{
                    'should': createIngredientsJson(ing_arr)
                }
            },
            'size': 15
        }
    }).then(function(response){
        return response
    }, function(err){
        console.trace(err.message)
    });

    return search_result
}

exports.query = query;
