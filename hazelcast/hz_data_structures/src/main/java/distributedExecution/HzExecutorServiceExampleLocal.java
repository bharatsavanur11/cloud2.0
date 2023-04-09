package distributedExecution;

import com.hazelcast.client.HazelcastClient;
import com.hazelcast.client.config.ClientConfig;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.core.IExecutorService;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

public class HzExecutorServiceExampleLocal {

 public static void main(String []args) throws ExecutionException, InterruptedException {

        ClientConfig clientConfig = new ClientConfig();
        HazelcastInstance hazelcastInstance = HazelcastClient.newHazelcastClient(clientConfig);
        IExecutorService executor = hazelcastInstance.getExecutorService("executor");
        List<Integer> mulList = new ArrayList<>();
        mulList.add(10);
        mulList.add(20);
        mulList.add(30);
        SimpleMultiplierWithoutList mul1 = new SimpleMultiplierWithoutList(mulList,0);
        SimpleMultiplierWithoutList mul2 = new SimpleMultiplierWithoutList(mulList,1);
        SimpleMultiplierWithoutList mul3 = new SimpleMultiplierWithoutList(mulList,2);
        Future<Integer> future = executor.submit(mul1);
        Future<Integer> future1 = executor.submit(mul2);
        Future<Integer> future2 = executor.submit(mul3);
        System.out.println("Getting the multiplication Factor" + future.get());
        System.out.println("Getting the multiplication Factor" + future1.get());
        System.out.println("Getting the multiplication Factor" + future2.get());
    }
}
