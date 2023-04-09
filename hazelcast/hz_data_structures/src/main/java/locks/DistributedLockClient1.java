package locks;

import com.hazelcast.client.HazelcastClient;
import com.hazelcast.client.config.ClientConfig;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.core.ILock;
import com.hazelcast.core.IQueue;

public class DistributedLockClient1 {

    public static  void main(String []args) throws InterruptedException {
        ClientConfig clientConfig = new ClientConfig();
        HazelcastInstance hazelcastInstance = HazelcastClient.newHazelcastClient(clientConfig);
        ILock lock = hazelcastInstance.getLock("distributedLock");
        lock.lock();
        Thread.sleep(5000);
    }
}
