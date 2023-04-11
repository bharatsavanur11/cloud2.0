package com.example;

import com.hazelcast.config.Config;
import com.hazelcast.config.MapConfig;
import com.hazelcast.config.MapStoreConfig;
import com.hazelcast.core.HazelcastInstance;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

import static com.hazelcast.core.Hazelcast.newHazelcastInstance;

@Configuration
public class HazelcastConfig {

    @Bean(name="hazelcastInstance")
    public HazelcastInstance getHazelcastInstance() {
        String connectionUri = null;
        try {
            connectionUri = "mongodb+srv://"+ URLEncoder.encode("hellobharat","UTF-8") +":"+ URLEncoder.encode("hellobharat","UTF-8") +"@sandbox.daamc.mongodb.net/?retryWrites=true&w=majority";
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }
        System.out.println(connectionUri);
        Config config = new Config();
        final MapConfig supplementsMapConfig = config.getMapConfig("quotes");
        final MapStoreConfig mapStoreConfig = supplementsMapConfig.getMapStoreConfig();
        mapStoreConfig
                .setEnabled(true)
                .setClassName("com.example.MongoMapStore")
                .setProperty("mongo.url", connectionUri)
                .setProperty("mongo.db","test")
                .setProperty("mongo.collection","quotes");

        final HazelcastInstance hazelcastInstance = newHazelcastInstance(config);

        return hazelcastInstance;

    }

}
