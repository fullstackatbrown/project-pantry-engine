const {Client} = require('@elastic/elasticsearch');
const client = new Client({node: 'http://localhost:9200'});


// array to JSON --> do I need?

// TODO --> array
function createIngredientsJson(ing_arr) {
    for (let i = 0; i < ing_arr.length; i++) {
        ing_arr[i] = {'match': {'ingredients': ing_arr[i]}}
    }
    return ing_arr
}


// TODO --> "ground beef" also returns results with ground ___
async function query(index_name, ing_arrI) {
    console.log(createIngredientsJson(ing_arrI));
    let [search_result] = await Promise.all([client.search({
            index: index_name,
            body: {
                'query': {
                    'bool': {
                        'must': [createIngredientsJson(ing_arrI)]
                    }
                }
            }
            ,
            'size': 10
        }
        ).then(function (response) {
            return response
        }, function (err) {
            console.trace(err.message)
        })
        ])
    ;

    return search_result
}


async function queryT(index_name, ing_arrI) {
    let [search_result] = await Promise.all([client.search({
            index: index_name,
            body: {
                'query': {
                    'bool': {
                        'must':
                            [{'match': {'ingredients': 'ground beef'}}, {'match': {'ingredients': 'salt'}}]
                    }
                }
            }
            ,
            'size': 10
        }
        ).then(function (response) {
            return response
        }, function (err) {
            console.trace(err.message)
        })
        ])
    ;

    return search_result
}

exports.query = query;
exports.queryT = queryT;
