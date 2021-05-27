

###
One : One text

Sent / Delivered / Read checkmarks on messages
- Server sends back ack
- Second connection back to recipient needed for Delivered
- Deliveree then sends an ack back to recipient using a queue

Push notifications
- Google's cloud notification service
- A new service in the system
- Push notification can be delayed because the delivery doesn't have to be as real-time as One : One text.
- Push notifications are fire and forget

Server
- Uses queues for messages
- Do we need a server that stores the history of all messages
Whats'app sends the messages and then removes the history from the server

## Issues
When recipient is offline, messages can be sent out of order
When the user is back online, the servers have queues that send at the same time.
