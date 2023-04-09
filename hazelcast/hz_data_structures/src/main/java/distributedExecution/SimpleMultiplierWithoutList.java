package distributedExecution;

import com.hazelcast.core.IList;

import java.io.Serializable;
import java.util.List;
import java.util.concurrent.Callable;

public class SimpleMultiplierWithoutList implements Callable<Integer>, Serializable {
    private List<Integer> cacheList;
    private Integer listVal;
    public SimpleMultiplierWithoutList(  List<Integer> cacheList) {
        this.cacheList=cacheList;
    }

    public SimpleMultiplierWithoutList(  List<Integer> cacheList, Integer i) {
        this.cacheList=cacheList;
        this.listVal=i;
    }


    @Override
    public Integer call() throws Exception {
        System.out.println("Executing");
        Integer z=0;
        for(int i =0;i<10;i++){
            z=cacheList.get(listVal) *i;
        }
        System.out.println("Result for" + listVal+"==" + z);
        return z;
    }
}
