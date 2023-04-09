package server;

import com.hazelcast.core.*;
import com.hazelcast.instance.HazelcastInstanceFactory;
import listeners.events.ClusterMemberListener;
import listeners.object.ItemListeners;

/**
 *
 * This class demonstrates the capability of distributed collection of the hazelcast instance.
 * Run it as many times as you want to start hazelcast instance.
 *
 */
public class HzServer1 {

      public static void main(String []args) {
          HazelcastInstance hz1 = Hazelcast.newHazelcastInstance();
          //Sets the cluster membership
          hz1.getCluster().addMembershipListener(new ClusterMemberListener());
          IList<String> hzList = hz1.getList("distributedList");
          hzList.addItemListener(new ItemListeners(),true);
          IMap<String,String> hz1Map = hz1.getMap("distributedMap");
          IList<Integer> integerList = hz1.getList("distributedIntegerSet");
          IQueue<String> map = hz1.getQueue("distributedQueue");
          // Adding Element to the List.
          integerList.add(10);
          integerList.add(11);
          integerList.add(12);
          //Adding items to Queue.
          map.add("Item-1");
          map.add("Item-2");
          map.add("Item-3");
          map.add("Item-4");
      }
}
