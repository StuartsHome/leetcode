# Use cases
- Who will use
- When will use
- How many will use
- How use (usage patterns)

# Estimations
- Throughput (QPS for read and write queries)
- Latency expected from system (read and write queries)
    - Polling, Server Send Events, Web-sockets
    - SSE for server to client, one connection is used for all messages
    - Web Sockets for 2-way
- Read/Write ratio
- Traffic Eastimates:
    - Write (QPS, Volume of data)
    - Read (QPS, Volume of data)
- Storage Estimates
- Memory Estimates
    - If using cache, what kind of data stored in cache
        - How to handle cache missies?
            - Policy (FIFO, LIFO, LRU)
    - How much RAM and how many machine to achieve this?
    - How much data to store on disk/ssd

# Design Goals
- Latency and Throughput requirements
- Consistency vs Availability
    - Weak/strong/eventual: Consistency | Failover/Replication: Availability
Database Attributes:
- Fault Tolerance
- Scalability
    - Design for read and write throughput to increase linearly as new machines are added
    with aim of no downtime or interruption to applications.
Distributed
- Every node in the cluster has the same role. There is no single point of failure.
Data is distributed across the cluster (so each node contains different data), but there is no master
as every node can service any request.

# High Level Design

# Deep Dive
- Scaling the Algorithm
- Scaling individual components
    - Availability, Consistency and Scale for each component
    - Consistency and Availability patterns
- Fault Tolerance (Is this the correct place?)
    - Data is automatically replicated to multiple nodes for fault-tolerance
    - Replication across multiple data centers is supported
- Think about the following components, how they would fit in and how it would help:
    - DNS
    - CDN (Push vs Pull)
    - Load Balancers (Active-Passive, Active-Active, Layer 4, Layer 7)
        - Layer 7 more advanced, allows optimisation and changes to content (compression, and encryption)
    - Application Layer Scaling (Microservices, Service Discovery)
    - CAP
        - Consistency: All reads receive the most recent write or an error
        - Availability: All reads contain data, but it might not be the most recent
        - Partition Tolerance: The system continues to operate despite network failures
    - DB (RDMS, NoSQL):
        - Batch or Real-time processing
        - RDMS -> CA (Strict Consistency)
        - NoSQL -> AP (Eventual Consistency), CP ()
        - RDMS
            - Master-slave, Master-master, Federation, Sharding, Denormalization, SQL Tuning, Idempotence
            - Sharding
                - Horizontal partition for efficient data access patterns
                - A shard is a horizontal partition of rows, instead of vertical using columns
                - Increase DB capacity and handle more traffic because load distributed across nodes
                - Each row is assigned a shard key that maps to the logical shard
                - More than one shard can be located on the same physical shard, but logical can't be split between physical shards
                - Create many small shards to prevent hotspots
            - SQL Tune
                - use fixed-length CHAR instead of VARCHAR
                - remove expensive joins (denormalize), improve read performance at the expense of some write performance.
                - store redundant data in multiple tables
            - Index column to speed up querying 
                - Pointer to data in table
                - Quickly access rows, without searching whole table
        - NoSQL
            - Most NoSQL comprimise consistency in favour of availability
            - Lack ACID transactions
            - Key-Value, Wide-Column, Graph, Document
                Fast Lookups:
                -------------
                - RAM [Bounded size] -> Redis, Memcached
                - AP [Unbounded size] -> Cassandra, Voldemort
                - CP [Unbounded size] -> MongoDB, Couchbase, DynamoDB, Redis

            - Cassandra: Wide Column Store: Availability and Partition tolerance more important 
                - Good link: https://cassandra.apache.org/cassandra-basics/
                - "writes never fail"
                - Fault Tolerant, Replication
                - Scalability
                - Cassandra scales horizontally (aka scale-out), because it’s based on nodes not CPU, or RAM
    - Analytics:
        - MapReduce function for NON REALTIME
            - Map: Counts appearance of each word in set of documents (filtering and sorting) and passes to reduce
            - Reduce: Perfoms a summary operation on key
                ```python
                function map(String name, String document):
                    name: document name
                    document: document contents
                    for word in document:
                        yield(word, 1)
                function reduce(String word, Iterator partialCounts):
                    word: a word
                    partialCounts: a list of aggregated partial counts
                    sum = 0
                    for each pc in partialCoutns:
                        sum += pc
                    yield(word, sum)
                ```
Consistency:
- when we talk about consistency we refer to an scenario where different entities (nodes) have their own copy of some data object.
    In any distributed systen there will be multiple copies of any one piece of data
    - Strong:
        - Front-end and backend db are consistent
        - Increased latency
        - Requires constant connection for latest information, if you lose Internet you can't view your balance 
        - Transactions are queued behind each other
    - Eventual:
        - Copies of data don't have to always be identical as long as they are designed to eventually become consistent once all the operations have been processed.
        - Basic reading and writing operations are available as much as possible, but without consistency guarantees
        (the write may not persist after conflicts are reconciled), the read may not get the latest write
        - Eventual Consistency allows for batch processing.
- Conflict resolution
    - When conflicts arise, this can usually be solved by a policy:
        - Last write wins
        - First write wins (used when LWW is unacceptable)
Databases:
NoSQL:
    - Advantages:
    - Disadvantages: 
        - Many NoSQL stores compromise consistency (in the sense of the CAP theorem) in favor of availability, partition tolerance, and speed.
        - Most NoSQL stores lack true ACID transactions, although a few databases have made them central to their designs.
        - Instead, most NoSQL databases offer a concept of "eventual consistency", in which database changes are propagated to all nodes "eventually" (typically within milliseconds), so queries for data might not return updated data immediately or might result in reading data that is not accurate, a problem known as stale reads.
    - Key/Value:
        - Dictionary data structure
        - Each data item has a pointer and a unique key
        - High performance because of integrated hashing feature allows users to store and retrieve data in the shortest time possible
        - Horizontal Scaling
        - No specific schema
        - Suitable for: simple data like caching, storing, user sessions, recommendations.
        - Examples: Redis, Voldemort
    - Wide-Column:
        - Data is stored and grouped into separately stored columns instead of rows
        - Organise information into columns that function similarly to tables in relational databases
        - No pre-defined column names, and are schema-free
        - Rows can have any number of columns unlike tables in relational databases which have a fixed size.
        - Suitable for: high availability, distribute data across multiple servers, store large amounts of data in a single column
        - Examples: Cassandra, Amazon DynamoDB, CosmoDB
    - Document:
        - Data storage system designed for storing, retrieving and managing document-oriented information, also known as semi-structured data
        - Documents in a document store are roughly equivalent to the programming concept of an object.
        - They are not required to adhere to a standard schema, nor will they have all the same sections, slots, parts or keys. 
        - Another defining characteristic of a document-oriented database is that, beyond the simple key-to-document lookup that can be used to retrieve a document, the database offers an API or query language that allows the user to retrieve documents based on content (or metadata). For example, you may want a query that retrieves all the documents with a certain field set to a certain value. 
        - Store data without a schema
        - Suitable for: JSON, XML, managing user profiles
        - Examples: Elasticsearch, MongoDB, CouchDB
    - Graph Store: 
        - Consist of two elements:
            - Nodes (for storing data entities)
            - Edges (for storing the relantionship between entities)
        - Retreive data with one operation
        - Suitable for: social networks
        - Examples: RedisGraph, Neo4j

To Do:
- CDN: Push vs Pull
- SQL use cases: e.g. for availability or consistency, which is best for what?
- NoSQL - when to use Key-Value, Wide-Column, Graph, Document
- Load Balancers (Active-Passive, Active-Active, Layer 4, Layer 7)
    - Layer 4 (Transport Layer, TCP)
        - Look how to distribute requests
        - Involves the source, destination IP addresses and ports in the header
        - No content of the packet
        - Forward network packets to and from the upstream server
    - Layer 7 (Application Layer, APP)
        - Deals predominantly HTTP
        - Routes network traffic in a more sophisticated way than Layer 4
            - Allows optimisation and changes to content (compression, and encryption)
        - Involves the contents of the header, message, and cookies
        - Terminates the network traffic and reads the message within
        - It can make a load-balancing decision based on the content of the message (URL, or Cookie)
        - Then makes a new connection to the upstream server and writes the request to the server
    - Layer 7 more CPU intensive than packet based Layer 4
- Application Layer Scaling (Microservices, Service Discovery)
- How to implement Fault Tolerance
- Better understanding of eventual consistency
- Strict consistence - Strict consistency is the strongest consistency model. Under this model, a write to a variable by any processor needs to be seen instantaneously by all processors.

Scenarios:
- Take one design e.g. a book store:
    - Alter design for CP, AP
    - Scale
    - ?