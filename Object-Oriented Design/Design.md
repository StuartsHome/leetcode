# Use cases
- Who will use
- When will use
- How many will use
- How use (usage patterns)

# Estimations
- Throughput (QPS for read and write queries)
- Latency expected from system (read and write queries)
- Read/Write ratio
- Traffic Eastimates:
    - Write (QPS, Volume of data)
    - Read (QPS, Volume of data)
- Storage Estimates
- Memory Estimates
    - If using cache, what kind of data stored in cache
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
    - Application Layer Scaling (Microservices, Service Discovery)
    - CAP
        - Consistency: All reads receive the most recent write or an error
        - Availability: All reads contain data, but it might not be the most recent
        - Partition Tolerance: The system continues to operate despite network failures
    - DB (RDMS, NoSQL):
        - RDMS -> CA (Strict Consistency)
        - NoSQL -> AP (Eventual Consistency), CP ()
        - RDMS
            - Master-slave, Master-master, Federation, Sharding, Denormalization, SQL Tuning, Idempotence
        - NoSQL
            - Key-Value, Wide-Column, Graph, Document
                Fast Lookups:
                -------------
                - RAM [Bounded size] -> Redis, Memcached
                - AP [Unbounded size] -> Cassandra, Voldemort
                - CP [Unbounded size] -> MongoDB, Couchbase, DynamoDB, Redis

            - Cassandra: Wide Column Store: Availability and Partition tolerance more important 
                - "writes never fail"
                - Fault Tolerant, Replication
                - Scalability
            - 
        - Wide Column Store:
        - Document Store:
        - Key-Value Store:
        - Graph Store: 

To Do:
- CDN: Push vs Pull
- SQL use cases: e.g. for availability or consistency, which is best for what?
- NoSQL - when to use Key-Value, Wide-Column, Graph, Document
- Load Balancers (Active-Passive, Active-Active, Layer 4, Layer 7)
- Application Layer Scaling (Microservices, Service Discovery)
- How to implement Fault Tolerance
- Better understanding of eventual consistency
- Strict consistence - Strict consistency is the strongest consistency model. Under this model, a write to a variable by any processor needs to be seen instantaneously by all processors.

Scenarios:
- Take one design e.g. a book store:
    - Alter design for CP, AP
    - Scale
    - ?