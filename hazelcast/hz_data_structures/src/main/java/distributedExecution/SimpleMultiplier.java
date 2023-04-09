package distributedExecution;

import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.core.HazelcastInstanceAware;
import com.hazelcast.core.IList;

import java.io.Serializable;
import java.util.concurrent.Callable;

public class SimpleMultiplier implements Callable<Integer>, Serializable, HazelcastInstanceAware {

    private Integer val;

    private transient HazelcastInstance hazelcastInstance;

    public SimpleMultiplier(Integer val) {
        this.val= val;
    }

    @Override
    public Integer call() throws Exception {
        Integer z=0;
        IList<Integer> cacheList = hazelcastInstance.getList("distributedIntegerSet");
        for(int i =0;i<10;i++){
            z=cacheList.get(val) *i;
        }
        return z;
    }

    @Override
    public void setHazelcastInstance(HazelcastInstance hazelcastInstance) {
        this.hazelcastInstance = hazelcastInstance;
    }
}
