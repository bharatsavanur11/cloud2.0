package listeners.events;

import com.hazelcast.core.MemberAttributeEvent;
import com.hazelcast.core.MembershipEvent;
import com.hazelcast.core.MembershipListener;

/**
 *
 *  Cluster Member Listener to listen to cluster events.
 *
 */
public class ClusterMemberListener implements MembershipListener {
    @Override
    public void memberAdded(MembershipEvent membershipEvent) {
        System.out.println("Member Added");
    }

    @Override
    public void memberRemoved(MembershipEvent membershipEvent) {
        System.out.println("Member Removed");
    }

    @Override
    public void memberAttributeChanged(MemberAttributeEvent memberAttributeEvent) {
        System.out.println("Member Attributed Changed");
    }
}
