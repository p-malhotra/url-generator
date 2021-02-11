# url-generator

This branch has code to  run a webservice for url generator.
This is just a testing code to know, how to create webservice and shorten url. It already has 2 hardcoded values.
This code will save generated urls in in-memory dict object, ideally should be in DB
This urls are generated using sequenece generator and will restart from begining when webservice restarts, so not production ready.
There are no validations and other parameters in payload.
At large scale, we will need unique "api-key"can be use to validate user and also time for how long the service is needed.

This service has two methods
https://poomalhotra.poojamalhotra.repl.co/api/v1/links/generator (POST)
Payload:
{"name":"youtube.com"}

https://poomalhotra.poojamalhotra.repl.co/api/v1/links/search-tiny?id=g2KJp.ly (GET)
Query param with shortened vallue to return main key


This is very basic version
No Validations
No authantication
Only in-memory persistence, which goes away with user restart
Sequence generator for shortened url, which will restart from begining with service restart.
this is default python sequence generator, can't be used for production purpose
It is just abstract api.

Very basic idea of REST GET/POST. 
