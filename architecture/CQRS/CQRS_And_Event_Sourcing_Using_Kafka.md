CQRS using Event Sourcing and Kafka

In the high write and high read systems, the load on the database is usually comes out to be very high. This demands for scalable and highly available database systems. This results in high expenditure but the speed can only be scaled to a certain extent.

One of the approaches to solve the above problem is using CQRS. CQRS stands for Command Query Responsibility Segregation.  As the name suggests,
command - write/update statemenets are executed on a separate database and 
while Query - read statements are executed  on another database.

How it works:

How Kafka is advantageous:

This leads to the writes not blocking your read and vice-versa. Immediately we see so many advantages. Let's list them down:

   1. Design your write database without concerning how it is going to be read.
   2. No table/row level lock needs to be established.
   3. All the writes can occcur in a single transaction without deadlocks.
   4. No complex table joins are required
   5. Support for materialized queries
   6. Design multiple query databases based on requirement
   7. Scale and Query parts optimally 

But there are some drawbacks as well:
   1. Query storage is done asynchronousl, so it is eventually consistent.
   2. May lose some ACID properties
   3. Increase in storage costs.
   4. Debugging becomes cumbersome due to additional hop
   5. Synchronization between write and read databases  become a bottleneck
   6. The read database needs to be written with IDEMPOTENCY of data in     
      place(if the same message is replayed, the effect should be exactly same).

The high level architecture for any CQRS system using Kafka is shown below:


All othe above drawbacks can be handled using standardized coding standards and few retry jobs. The next part of document handles the very same thing.

Let's understand what can go wrong:

   1. There could be an error while putting the message on Kafka.
   2. Once the message is sent, the database update fails on producer.
   3. Once the message is read, the consumer throws an error.
   4. Consumer fails to acknowledge the read message.
   5  The same message is replayed due to offset change/ or some admin error

How to mitigate the above issues:

   1. In the write database, a new additional column to show the cache 
      update status is added.
   2. This column is set to false, every time we make an update to the 
      record.
   3. Once the message is sent to kafka successfully, the record column is 
      updated with successful cache update.
   4. On the reciever side, read the message from MQ.
   5. Update the read store and when successfully done, acknowledge the 
      message.
   6. Add retry logic, if the database update fails and eventually timeout.
   7. If the acknowledgement fails on client side, then the same message is 
      processed and since changes are idempotent, it doesnt effect.
   8. Add an update timestamp to the query database record, so as not to 
      process any out of order records due to kafka partition.
   9. A job on the producer side and consumer side to reconcile both the 
      databases is required.


As it can be seen, when implementing CQRS at scale, certain coding standards need to be followed. A common standard framework , common kafka standards, number of partitions and listeners if implemented at project level becomes extremely important.





