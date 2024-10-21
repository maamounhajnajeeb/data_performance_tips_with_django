This repo is inspired by this [tutorial](https://youtu.be/tloKxFgom58?si=Mb-AheSQJLU1AHkD)
Actually, it's practical guide for it

There are three main sections in this README:</br>
1. How to contribute</br>
2. How to clone this repo and work with it</br>
3. Tutorial Content (Tutorial Practical Walkthrough)</br>
4. ToDo list</br>
5. Repo Specification</br>

## How to clone this Repo to go through the tutorial
`git clone`</br>
`pip install requirements.txt`</br>
`py manage.py migrate`</br>
`py manage.py loaddata faked_users faked_analytics` (you can see a video of how I build fixture data very fast with mockaroo from [here]())</br>

## Tutorial Content
### Intro
> Time-line: start at: 00:00, end at: 01:30

### Summary of the talk
> Time-line: start at: 1:30, end at: 03:19

General talk about the Django project used in the tutorial and Data performance issues.

### Querying (Pagination, Annotations and Materialized Views)
> Time-line: start at: 03:19, end at: 25:14

### Pagination:
#### Offset Pagination:
* The first type of pagiantion we should know about is \~ `offset pagination` \~</br>
<ins>url</ins>: http://127.0.0.1:8000/analytics/events_offset_paginated/?page=1</br>
<ins>view</ins>: analytics/views -> events_offset_paginated</br>
* In \~ `offset pagination` \~ the database have to load all the data up until the offset specified value (depends on how deep pagination is) which is a problem when working with large data.
* when you work with large number of data you have to work with another type of pagination called \~ `keyset pagination` \~ (also called cursor pagination).

#### Cursor Pagination (Keyset Pagination):
* The way \~ `keyset pagination` \~ works is using cursors, you can see good explanation of how this kind of paginators works from PlanetSacle MySQL tutorial series [here](https://planetscale.com/learn/courses/mysql-for-developers/examples/cursor-pagination?autoplay=1).

### N+1 problem
* we have to avoid N+1 problem when querying data from a table that has relationships like M2M, Foreign-Key and O2O with other tables.</br>
You can read more about N+1 problem from [here]().</br>
select_related and prefetch_related: django docs [here](https://docs.djangoproject.com/en/5.1/ref/models/querysets/#select-related) and [here](https://docs.djangoproject.com/en/5.1/ref/models/querysets/#prefetch-related).</br>
<ins>view</ins>: analytics/views.py -> events_with_related_users</br>
<ins>url</ins>: http://127.0.0.1:8000/analytics/events_with_related_users/?page=2

### Annotations
* Annotations is way to generate summary values for each object in QuerySet.</br>
Django docs [here](https://docs.djangoproject.com/en/5.1/topics/db/aggregation/#generating-aggregates-for-each-item-in-a-queryset)</br>


## ToDo list:
- Generate more data (10000 rows)
- work more on annotations section (build separate repo and work annotation and aggregation section from django docs)
- build cursor pagination
- Add kolo support
- make django version 4.2 L.T.S
- Add N+1 problem resource
- build fake data youtube video

## Repo Specification
- Database: PostgreSQL
- Django version: 4.2 (L.T.S)
- Python version: 3.11
- Caching: Redis
- psycopg 3
