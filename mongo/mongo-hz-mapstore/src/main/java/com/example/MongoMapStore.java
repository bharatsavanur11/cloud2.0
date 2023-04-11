package com.example;

import com.example.business.Quote;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.map.MapLoaderLifecycleSupport;
import com.hazelcast.map.MapStore;
import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.ServerApi;
import com.mongodb.ServerApiVersion;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import org.bson.Document;
import org.springframework.data.mongodb.core.MongoTemplate;

import java.util.Collection;
import java.util.Map;
import java.util.Properties;


public class MongoMapStore implements MapStore<String, Quote> , MapLoaderLifecycleSupport {

    private MongoTemplate mongoTemplate;

    private MongoClient mongoClient;

    private MongoCollection collection;

    @Override
    public void init(HazelcastInstance hazelcastInstance, Properties properties, String s) {
        String mongoUrl = (String) properties.get("mongo.url");
        String dbName = (String) properties.get("mongo.db");
        String collectionName = (String) properties.get("mongo.collection");
        ConnectionString connectionString = new ConnectionString(mongoUrl);
        MongoClientSettings mongoClientSettings = MongoClientSettings.builder()
                .applyConnectionString(connectionString)
                .serverApi(ServerApi.builder()
                        .version(ServerApiVersion.V1)
                        .build())
                .build();
        this.mongoClient = MongoClients.create(mongoClientSettings);
        this.collection = mongoClient.getDatabase(dbName).getCollection(collectionName);
    }

    @Override
    public void store(String s, Quote quote) {
        Document doc = new Document("book", quote.getBook()).append("content", quote.getContent()).append("_id", quote.getId());
        this.collection.insertOne(doc);
    }

    @Override
    public void storeAll(Map<String, Quote> map) {
        map.forEach((key,quote)->{
            Document doc = new Document("book", quote.getBook()).append("content", quote.getContent()).append("_id", quote.getId());
            this.collection.insertOne(doc);
        });
    }

    @Override
    public void delete(String s) {

    }

    @Override
    public void deleteAll(Collection<String> collection) {

    }

    @Override
    public Quote load(String s) {
        return null;
    }

    @Override
    public Map<String, Quote> loadAll(Collection<String> collection) {
        return null;
    }

    @Override
    public Iterable<String> loadAllKeys() {
        return null;
    }



    @Override
    public void destroy() {

    }
}
