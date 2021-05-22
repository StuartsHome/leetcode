

File vs Blob
Blob - binary large object
    varchar 255 is too small to store images
    blob allows this


DB:

- Mutability: Do we need to change the image? No
- Transaction guarantees (atomic operation)? Required? No
- Indexes (Improve search)? Key value lookup contents of file?
- Access Control


Files:
- Cheaper
- Faster storing large objects
- Static so able to use CDN for fast access