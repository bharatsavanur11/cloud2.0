package com.example;

import com.hazelcast.config.Config;
import com.hazelcast.config.MapConfig;
import com.hazelcast.config.MapStoreConfig;
import com.hazelcast.core.HazelcastInstance;
import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.ServerApi;
import com.mongodb.ServerApiVersion;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.mongodb.config.AbstractMongoClientConfiguration;
import org.springframework.data.mongodb.core.MongoOperations;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

import java.io.UnsupportedEncodingException;
import java.util.Collection;
import java.util.Collections;
import java.net.URLEncoder;

import static com.hazelcast.core.Hazelcast.newHazelcastInstance;

@EnableMongoRepositories
@Configuration
public class MongoConfig extends AbstractMongoClientConfiguration {

    @Override
    protected String getDatabaseName() {
        return "test";
    }

    /**
     * IN Mongo Atlas free service there could happen thta existing user/name password is not reflecting and hence
     * would need to add a new user and password. This issue is intermittent and can happend sometimes and sometimes doesnt.
     * @return
     */
    @Override
    @Bean
    public MongoClient mongoClient() {
        String connectionUri = null;
        try {
            connectionUri = "mongodb+srv://"+ URLEncoder.encode("hellobharat","UTF-8") +":"+ URLEncoder.encode("hellobharat","UTF-8") +"@sandbox.daamc.mongodb.net/?retryWrites=true&w=majority";
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }
        System.out.println(connectionUri);
        ConnectionString connectionString = new ConnectionString(connectionUri);
        MongoClientSettings mongoClientSettings = MongoClientSettings.builder()
                .applyConnectionString(connectionString)
                .serverApi(ServerApi.builder()
                        .version(ServerApiVersion.V1)
                        .build())
                .build();

        return MongoClients.create(mongoClientSettings);
    }


    @Bean("testDb")
    public MongoTemplate mongoTemplate() throws Exception {
        return new MongoTemplate(mongoClient(), "test");
    }

    @Bean(name="airBnbDb")
    public MongoTemplate mongoTemplateAirBnb() throws Exception {
        return new MongoTemplate(mongoClient(), "sample_airbnb");
    }

    @Override
    public Collection getMappingBasePackages() {
        return Collections.singleton("com.example.business");
    }
}
