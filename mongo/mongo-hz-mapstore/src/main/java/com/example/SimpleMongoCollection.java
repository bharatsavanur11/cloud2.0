package com.example;

import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.ServerApi;
import com.mongodb.ServerApiVersion;
import com.mongodb.client.*;

import java.net.URLEncoder;

public class SimpleMongoCollection {

    public static void main(String []args) throws  Exception{
        String connectionUri = "mongodb+srv://"+URLEncoder.encode("hellobharat","UTF-8") +":"+ URLEncoder.encode("hellobharat","UTF-8") +"@sandbox.daamc.mongodb.net/?retryWrites=true&w=majority";
        System.out.println(connectionUri);
        ConnectionString connectionString = new ConnectionString(connectionUri);
        MongoClientSettings settings = MongoClientSettings.builder()
                .applyConnectionString(connectionString)
                .serverApi(ServerApi.builder()
                        .version(ServerApiVersion.V1)
                        .build())
                .build();
        MongoClient mongoClient = MongoClients.create(settings);
        MongoDatabase database = mongoClient.getDatabase("sample_airbnb");
        System.out.println("Printing--"+ database.getCollection("listingsAndReviews"));
        MongoCollection mongoCollection = database.getCollection("listingsAndReviews");

        System.out.println("Count"+"---"+mongoCollection.countDocuments());
        MongoCursor mongoCursor = mongoCollection.find().cursor();
        while(mongoCursor.hasNext()){
            String data = (String) mongoCursor.next();
            System.out.println(data);
            System.out.println("=----");
        }
    }
}
