const expect = require('chai').expect;
const {Client} = require('@elastic/elasticsearch')
const client = new Client({ node: 'http://localhost:9200'}) //what will this change to?

describe('search es', function() {
    it("exists", function(){
    });
});