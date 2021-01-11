# Pantry Engine

Our stack consists of 3 parts: a React.js user interface, a Node.js server acting as an [Elasticsearch client](https://www.elastic.co/guide/en/elasticsearch/client/javascript-api/current/index.html) (and possibly supporting user accounts in the future), and a collection of Python scripts for Elasticsearch setup, maintenance, and indexing of recipe pages.

Ensure that you have installed and can run the Elasticsearch server locally - this is NOT the same as running the Node.js or Python Elasticsearch clients. Refer to [this article](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-18-04) as a guide to get started.