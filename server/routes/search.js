const { Client } = require('@elastic/elasticsearch')
const client = new Client({ node: 'http://localhost:9200'})

// What we have in pantry (ingredients)
// What we need to make it --> how to make the difference

function query_match_all (index_, body_json){
    JSON.parse(body_json).catch(error => console.log(error))

    let search_result = client.search({
        index: index_,
        body: {
            "query": {
                body_json
            },
            "size": 15
        }
    }).then(response => console.log(response))
        .catch(error => console.log(error))

    return search_result.catch(error => console.log(error))
}