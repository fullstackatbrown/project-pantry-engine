# Server (Elasticsearch Client)

Please use yarn package manager.

To install dependencies: `yarn install`

To add new dependency: `yarn add <dependency>`

To run (port 5000 by default): `yarn start`

______________________

Query testing was done with `npm`, but `yarn` works as well.
1. Run elasticsearch, e.g., with `elasticsearch`, and the Node app with `yarn start` or `npm start`
2. Yarn will accept over 5000 and 3000, but npm will only accept over 3000
3. URL formats as such: `http://localhost:3000/?ing[]=ingredient1&ing[]=ingredient2`

Have not built out error handling, so bad req's should cause the app to exit. Bad URL's should return a 404 "page"

Correct URL with params will yield exactly what elasticsearch returns from that query, metadata and all. 