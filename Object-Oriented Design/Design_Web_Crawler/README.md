https://dev.to/kevincolemaninc/designing-a-distributed-web-crawler-2dp2
https://medium.com/swlh/design-a-proximity-server-like-nearby-or-yelp-part-1-c8fe2951c534

To Do:
- Tidy up System Design structure


# Questions:
- How do we know how many URLs we can safely fetch from one server at a time?
For this, we will need to experiment with timeouts to determine when we are rate limited.
Typically, systems throttle too many connections coming from a single ip address.

To combat - distribute requests to other servers


Assigining each URL to a specific server lets each server manage which URLs need to be fetched
or have already been fetched.
Each server will get its own ID starting from 0 to 99,999.
Hashing each URL and calculating the modulus of the hash with 10,000 can define the ID of the server
we need to fetch the URL from.

In a master/slave design, a single master server could map the server ids to specific ip addresses.
Since the problem asks us to reduce network traffic, we can either pre-configure each server with an ip
addres or rely on a DNS server to map hostnames to ip addresses.

3. Since every URL will be uniquely assigned to a single server number, each server will internally
track which URLs it has already crawled, just like the single server design.
The single server design uses a set, but we could also use a Bloom Filter

4. Each server will need to implement an API to receive a set of URLs that the other servers find in their
pages. We can use JSON and REST to route these requests.

5. The URL attribute should be a unique list of URLs found in the HTML documents that the server found at its
own URLs.
We should avoid sending 1 web request per document because each network request has overhead.
We could collect URLs and send them to the other machines in batches of 100

6. How can you distribute the URLs if a portion of the 10k servers lose power while crawling is happening?

We could use the concept of "consumer groups". Instead of sening the URLs to be fetched to a single machine,
we could divide the 10,000 servers into groups that are collectively responsible for managing URLs assigned to
their group.
One machine would receive the URLs to be fetched using a consistency algorithm to decide within a group
which machine will be fetching the URL.

If an entire group fails, we can use the technique called "Consistent hasing" with log(m) hashing
algorithms to evenly distribute the load, where m is the number of groups.

Consistent hashing:
""
Consistent hashing was designed to avoid the problem of having to change the server assignment of every object when a server is added or removed. The main idea is to use a hash function to randomly map both the objects and the servers to a unit circle.

Each object is then assigned to the next server that appears on the circle in clockwise order. 

provides an even distribution of objects to servers. But, more importantly, if a server fails and is removed from the circle, only the objects that were mapped to the failed server need to be reassigned to the next server in clockwise order. Likewise, if a new server is added, it is added to the unit circle, and only the objects mapped to that server need to be reassigned. Importantly, when a server is added or removed, the vast majority of the objects maintain their prior server assignments.
""

### Code


queue = ["https://wikipedia.org]
seen = set()
while queue:
    URL = queue.pop()
    page = download(URL)
    URLs = extract_URL(page)
    for URL in URLs:
        if not(URL in seen):
            queue.append(URL)

server_num = hash("/wiki/The_Entire_History_of_You") % 1000
- Directly talk to the server
server_ip = num_to_ip_dict[server_num]
- Using a DNS server
server_host = f'http://{server_num}.crawler.company,com'
