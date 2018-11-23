# Part 2 - Riak

Solutions to this exercise were tested against Riak 2.2.3 with leveldb backend.

## Common query caching
It wasn't entirely clear here whether the results to be cached were the actual documents or just their ids/references.
Assuming the latter (to avoid duplicating document content), the following `curl` requests could be used to populate a cache with the 5 most popular search queries and their ids:

```
curl -XPUT -H "Content-Type: application/json" -d "[0, 1, 2, 3, 4, 5, 6]" http://localhost:8098/buckets/hscicNewsCache/keys/OR-Care-Commission-Quality
curl -XPUT -H "Content-Type: application/json" -d "[9]" http://localhost:8098/buckets/hscicNewsCache/keys/OR-2004-September
curl -XPUT -H "Content-Type: application/json" -d "[6, 8]" http://localhost:8098/buckets/hscicNewsCache/keys/OR-general-generally-population
curl -XPUT -H "Content-Type: application/json" -d "[1]" http://localhost:8098/buckets/hscicNewsCache/keys/AND-Care-Commission-Quality-admission
curl -XPUT -H "Content-Type: application/json" -d "[6]" http://localhost:8098/buckets/hscicNewsCache/keys/AND-Alzheimer-general-population
```

The cache could then be queried via a HTTP GET using the canonical search term, eg.
```
curl http://localhost:8098/buckets/hscicNewsCache/keys/OR-Care-Commission-Quality
```

## Monthly indexes
The following curl requests would populate the repository with the collection of documents indexed by id (key) and year/month (secondary index):

```
curl -XPUT -H "Content-Type: text/plain" -H 'x-riak-index-year_month_int: 201306' -d "June 5 , 2013 : The majority of ..." http://localhost:8098/buckets/hscicNews/keys/RESULT:0
curl -XPUT -H "Content-Type: text/plain" -H 'x-riak-index-year_month_int: 201307' -d "July 9 , 2013 : The HSCIC has ..." http://localhost:8098/buckets/hscicNews/keys/RESULT:1
curl -XPUT -H "Content-Type: text/plain" -H 'x-riak-index-year_month_int: 201306' -d "June 19 , 2013 : New figures from ..." http://localhost:8098/buckets/hscicNews/keys/RESULT:2
curl -XPUT -H "Content-Type: text/plain" -H 'x-riak-index-year_month_int: 201306' -d "June 13 , 2013 : Almost one in ..." http://localhost:8098/buckets/hscicNews/keys/RESULT:3
curl -XPUT -H "Content-Type: text/plain" -H 'x-riak-index-year_month_int: 201306' -d "June 5 , 2013 : The majority of ..." http://localhost:8098/buckets/hscicNews/keys/RESULT:4
curl -XPUT -H "Content-Type: text/plain" -H 'x-riak-index-year_month_int: 201304' -d "April 15 , 2013 Thousands of GP practices ..." http://localhost:8098/buckets/hscicNews/keys/RESULT:5
curl -XPUT -H "Content-Type: text/plain" -H 'x-riak-index-year_month_int: 201302' -d "February 19 , 2013 : Mortality among mental ..." http://localhost:8098/buckets/hscicNews/keys/RESULT:6
curl -XPUT -H "Content-Type: text/plain" -H 'x-riak-index-year_month_int: 201301' -d "January 23 , 2013 : English A and ..." http://localhost:8098/buckets/hscicNews/keys/RESULT:7
curl -XPUT -H "Content-Type: text/plain" -H 'x-riak-index-year_month_int: 201212' -d "December 12 , 2012 : The proportion of ..." http://localhost:8098/buckets/hscicNews/keys/RESULT:8
curl -XPUT -H "Content-Type: text/plain" -H 'x-riak-index-year_month_int: 201209' -d "September 26 , 2012 : Income before tax ..." http://localhost:8098/buckets/hscicNews/keys/RESULT:9
```

Retrieving the keys for documents in June 2013 could then be achieved using the following query:

```
curl http://localhost:8098/buckets/hscicNews/index/year_month_int/201306
```

