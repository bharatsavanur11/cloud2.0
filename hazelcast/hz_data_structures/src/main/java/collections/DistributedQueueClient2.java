package collections;

import com.hazelcast.client.HazelcastClient;
import com.hazelcast.client.config.ClientConfig;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.core.IQueue;

public class DistributedQueueClient2 {
    public static void main(String []args) throws InterruptedException {
        ClientConfig clientConfig = new ClientConfig();
        HazelcastInstance hazelcastInstance = HazelcastClient.newHazelcastClient(clientConfig);
        IQueue<String> queue = hazelcastInstance.getQueue("distributedQueue");
        String item1 = queue.poll();
        System.out.println(item1);
        Thread.sleep(5000);
        String item2 = queue.poll();
        System.out.println(item2);
    }
}
