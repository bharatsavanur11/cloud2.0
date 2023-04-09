package locks;

import com.hazelcast.client.HazelcastClient;
import com.hazelcast.client.config.ClientConfig;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.core.ILock;

public class DistributedLockClient2 {

    public static  void main(String []args) throws InterruptedException {
        ClientConfig clientConfig = new ClientConfig();
        HazelcastInstance hazelcastInstance = HazelcastClient.newHazelcastClient(clientConfig);
        ILock lock = hazelcastInstance.getLock("distributedLock");
        if(lock.tryLock()){
            System.out.println("Got Lock");
        }else{
            System.out.println("Locked by Some on else");
        }
    }
}
