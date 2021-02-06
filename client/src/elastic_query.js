const { Client } = require('@elastic/elasticsearch')
// Note that node address depends on local config
const client = new Client({ node: 'httpL//localhost:9200'})

function query_match_all(index_, query_json){
    JSON.parse(query_json).catch(error => console.log(error))

    search_result = client.search({
        index: index_,
        body: {
            "query": {
                query_json
            },
            "from": 0, "size": 10
        }
    }).then(response => console.log(response))
        .catch(error => console.log(error))

    return search_result.catch(error => console.log(error))
}