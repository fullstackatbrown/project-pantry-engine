const {Client} = require('@elastic/elasticsearch');
const client = new Client({node: 'http://localhost:9200'});

// TODO --> "ground beef" also returns results with ground ___
// TODO --> error handling?

// expects ?ing[]=first&ing[]=second ...
const get_search = async function (req, res, next) {

    let arr = req.url.split('?');
    if (req.url.length > 1 && arr[1] !== ''){
        let ing_arr = req.query.ing
        for (let i = 0; i < ing_arr.length; i++) {
            ing_arr[i] = {'match': {'ingredients': ing_arr[i]}}
        }
        console.log(ing_arr)
        let search_query = {
            index: 'recipe_index',
            body: {
                'query': {
                    'bool': {
                        'should': ing_arr
                    }
                }

            },
            'size': 10
        }


        let resp_arr = [];

        async function sendResponse() {
            const {body} = await client.search(search_query)
            for (let i = 0; i < body.hits.hits.length; i++) {
                resp_arr.push(body.hits.hits[i])
            }
            console.log(resp_arr)
            res.json(resp_arr);
        }

        await sendResponse();
    } else {
        res.send("No params");
    }
}

const get_results = function (req, res, next) {
    // this doesn't have access to resp_arr declared in the function above...
    // see ./app/server/controllers/search_controllers.js
    res.json(resp_arr)
}


module.exports = {
    get_results,
    get_search
}
