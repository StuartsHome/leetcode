- interviewers are looking for your understanding of the nuances of complex problems and your ability to transform the requirements into comprehensible Classes.

- To simplify things, you can take the following approach for any OOD question you encounter:
1. Clarify the requirements
2. Hash out the primary use cases:
    1. Think about, and then talk through, use cases. Make sure you understand all the different functionality your system is expected to have.
3. Identify key Objects
    1. Now, identify all the objects that will play a role in your solution. For example, if you’re designing a parking lot, these will be things like vehicles, parking spots, parking garages, entrances, exits, garage operators, etc.
4. Identify Operations supported by Objects
    1. For example, a car should be able to move, park in a given spot, and hold a license plate. A parking spot should be able to accommodate a two-wheeled vehicle or a four-wheeled vehicle — and so on.
5. Identify Interactions between Objects
    1. Map out the relationships between the different objects that will need to interface with each other. This is where it all comes together. For example, a car should be able to park in a parking spot. Parking garages should be able to fit multiple parking spots, and so on.


## Questions
- Design Amazon / Flipkart (an online shopping platform)
    1. Beyond the basic functionality (signup, login etc.), interviewers will be looking for the following:
    2. Discoverability: How will the buyer discover a product? How will the search surface results?
    3. Cart & Checkout: Users expect the cart and checkout to behave in a certain way. How will the design adhere to such known best practices while also introducing innovative checkout semantics like One-Click-Purchase?
    4. Payment Methods: Users can pay using credit cards, gift cards, etc. How will the payment method work with the checkout process?
    5. Product Reviews & Ratings: When can a user post a review and a rating? How are useful reviews tracked and less useful reviews de-prioritized?
- Design a Movie Ticket Booking System
- Design an ATM
- Design an Airline Management System
- Design Blackjack (a card game)
- Design a Hotel Management System
- Design a Parking Lot
- Design an Online Stock Brokerage System
- Design a Car Rental System
- Design Facebook — a social network

## OOD Structure:
1. Write the damn API highlevel interfaces first
2. Decide on what sort of infra / database distribution to use
3. Describe what sort of business functions u are performing

## Q's
Order:
    - Use case
    - Scale (before high level design)
    - Offer calculations of usage before designing
        - number of users, number of transactions, number of active queries per day, etc
    - Design rough idea, then move into load balancers, caches etc.

First thing - clarifying questions:
    - Ratio of reads to writes
        - Parking garage would be more reads to writes
    - Size of data
    - Keys in database
    - Cloud?
    - Usage
        - Bandwidth
        - How many concurrent connections to a redis instance?
Second - Use cases:
    - How service calculates
    - user views, view categories or products
    - scope
    - 
Third - Start and end point
    - High level design
    - After asking clarifying questions, ask where to start with the design, i.e. at the service? at the database?
    - Start at concrete point
        - e.g. client making call to service(server)
    - Draw arrows or lines conneting things (relationships)
Calculate usage:
    - How much data is being sent to servcer
    - How big are server requests
    - How big are the transactions
    - 40bytes, 40Bil, 40GB transfer to service every month?day? that requires sharding, replication etc.

Databases:
    - If the information is pre-processed, it can be stored and then archived for later use
    - Store in object store, so can archive and send to S3
        - Export the data to archive
        - This allows backup in case something is lost
        - More secure than having in database

### CAP
    - Availability or Consistency
        - Availability
        - Consistency
            - when we talk about consistency we refer to an scenario where different entities (nodes) have their own copy of some data object.
            - If read more than write
                - Read replicas 
            - Strong or eventual consistency?
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

### Database
    SQL or NoSQL
    - SQL
        - Optomised for storage
        - Scale vertically - (schema)
        - Not repeatable queries
    - NOSQL
        - Optomised for compute
        - Scale horizontally
        - Repeatable and consistent queries
        - Distributed request router
            - Parition information of configuration table is cached to stop lookups on config table
        - Partition keys are used to id item
            - enables routing to storage node to service request
            - maintain fast consistent behaviour
            - allows sort key for range
            - partitions are 3-way repllicated
    - Eventual and Strongly consisted
        - Eventual reads are 1/2 cost of strongly consistent read
            - this is because we have more nodes to choose from
            - strongly (read from primary), eventual read from any of 3 replicas
        - With 3 way replication, the primary node to secondary is sub one second
        - By the time you've round tripped to the client the data will have already replicated secondaries 

    - ACID
        - Atomicity, Consistency, Isolation, Durability
        - is a set of properties of database transactions intended to guarantee data validity despite errors, power failures, and other mishaps.
        - A sequence of database operations that satisfies the ACID properties is called a transaction.
    - NoSQL
        - Stores all information in a single instance of DB, every stored object can be different from every other, and uses a hash lookup
        - The difference lies in the way the data is processed; in a key-value store, the data is considered to be inherently opaque to the database, whereas a document-oriented system relies on internal structure in the document in order to extract metadata 
        - Key-value pair or document
            - Key- Value
                - Dynamo, Memcache, Redis
            - Document
                - data storage system designed for storing, retrieving and managing document-oriented information, also known as semi-structured data
                - Documents in a document store are roughly equivalent to the programming concept of an object.
                - They are not required to adhere to a standard schema, nor will they have all the same sections, slots, parts or keys. 
                - Another defining characteristic of a document-oriented database is that, beyond the simple key-to-document lookup that can be used to retrieve a document, the database offers an API or query language that allows the user to retrieve documents based on content (or metadata). For example, you may want a query that retrieves all the documents with a certain field set to a certain value. 
                - MongoDB
    - NoSQL disadvantages
        - Many NoSQL stores compromise consistency (in the sense of the CAP theorem) in favor of availability, partition tolerance, and speed.
        - Most NoSQL stores lack true ACID transactions, although a few databases have made them central to their designs.
        - Instead, most NoSQL databases offer a concept of "eventual consistency", in which database changes are propagated to all nodes "eventually" (typically within milliseconds), so queries for data might not return updated data immediately or might result in reading data that is not accurate, a problem known as stale reads.

    - Batch processing or Real-time processing
        - Allows services to manage large amounts of data efficiently
        - The essential parameters include:
            - Who is submitting the job?
            - Which program will run the job?
            - To location of the inputs and outputs
            - When job run
        - Example:
            - Many companies use batch processing to automate their billing process
            - Think of a credit card transaction that did not show up in your bank account history until several days after you spent your money. This transaction may have been processed in a batch sometime after you made your purchase.
    - Data pre-processing 
        - The step of transforming raw data into an understandable format (information)
        - Steps:
            - Normalisation (into a normalised and generalised format)
        - The phrase "garbage in, garbage out"
        - Used to remove data that is:
            - Out of range
            - unreliable
            - noisy
    - NoSQL
        - You can see that as a 2-dimensional key-value store. The first part of the key is used to distribute the data across servers, the second part of the key lets you quickly find the data on the target server.
    - Replication Factor
        - How many backups of the same DB
        - So Hadoop (HDFS) is fault tolerant
        - If a server fails, there is a copy