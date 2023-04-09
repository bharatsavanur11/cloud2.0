package listeners.object;


import com.hazelcast.core.ItemEvent;
import com.hazelcast.core.ItemListener;

public class ItemListeners implements ItemListener<String> {

    @Override
    public void itemAdded(ItemEvent<String> itemEvent) {
        System.out.println("Item Added "+ itemEvent.getItem());
    }

    @Override
    public void itemRemoved(ItemEvent<String> itemEvent) {
        System.out.println("Item Removed");
    }
}
