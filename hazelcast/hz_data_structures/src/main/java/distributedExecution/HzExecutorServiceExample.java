package distributedExecution;

import com.hazelcast.client.HazelcastClient;
import com.hazelcast.client.config.ClientConfig;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.core.IExecutorService;
import com.hazelcast.core.IList;
import com.hazelcast.durableexecutor.DurableExecutorService;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

public class HzExecutorServiceExample {

    public static void main(String []args) throws ExecutionException, InterruptedException {
        ClientConfig clientConfig = new ClientConfig();
        HazelcastInstance hazelcastInstance = HazelcastClient.newHazelcastClient(clientConfig);
        DurableExecutorService executor = hazelcastInstance.getDurableExecutorService("executor");
        IList<Integer> list = hazelcastInstance.getList("distributedIntegerSet");
        SimpleMultiplier mul = new SimpleMultiplier(0);
        SimpleMultiplier mul1 = new SimpleMultiplier(1);
        SimpleMultiplier mul2 = new SimpleMultiplier(2);
        mul.setHazelcastInstance(hazelcastInstance);
        Future<Integer> future = executor.submit(mul);
        Future<Integer> future1 = executor.submit(mul1);
        Future<Integer> future2 = executor.submit(mul2);
        System.out.println("Getting the multiplication Factor" + future.get());
        System.out.println("Getting the multiplication Factor" + future1.get());
        System.out.println("Getting the multiplication Factor" + future2.get());

    }
}
