This repo is inspired by this [tutorial](https://youtu.be/tloKxFgom58?si=Mb-AheSQJLU1AHkD)
Actually, it's practical guide for it

There are three main sections in this README:</br>
1. How to contribute</br>
2. How to clone this repo and work with it</br>
3. Tutorial Content (Tutorial Practical Walkthrough)</br>
4. Repo Specification</br>

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

#### Pagination:
* The first type of pagiantion we should know about is \~ `offset pagination` \~
<ins>url</ins>: http://127.0.0.1:8000/analytics/events_offset_paginated/?page=1</br>
<ins>view</ins>: analytics/views -> events_offset_paginated

#### N+1 problem
* we have to avoid N+1 problem when querying data from a table that has relationships like M2M, Foreign-Key and O2O with other tables.</br>
You can read more about N+1 problem from [here]().</br>
select_related and prefetch_related: django docs [here]() and [here]().</br>
<ins>view</ins>: analytics\
<ins>url</ins>: analytics\

## Repo Specification
- Database: PostgreSQL
- Django version: 4.2 (L.T.S)
- Python version: 3.11
- Caching: Redis
- psycopg 3
