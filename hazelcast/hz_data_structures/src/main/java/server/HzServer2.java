package server;

import com.hazelcast.core.Hazelcast;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.core.IList;
import com.hazelcast.core.IMap;

/**|
 *
 * This class demonstrates the capability of distributed collection of the hazelcast instance.
 * Run it as many times as you want to start hazelcast instance.
 *
 *
 */
public class HzServer2 {

      public static void main(String []args) {
          HazelcastInstance hz1 = Hazelcast.newHazelcastInstance();
          IList<String> hzList = hz1.getList("distributedList");
          IMap<String,String> hz1Map = hz1.getMap("distributedMap");
          hzList.add("Item1");
          hzList.add("Item2");
          hzList.add("Item3");
          hz1Map.put("1","Item1");
          hz1Map.put("2","Item2");
          hz1Map.put("3","Item3");
      }
}
