package com.example.business;

import com.example.MongoConfig;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.map.IMap;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.logging.Logger;


@Component
public class MongoService{


        private static final Logger log = Logger.getLogger("QuoteController");

        private static long DELAY_BY_TIME = 1000;

        @Qualifier("testDb")
        @Autowired
        private  MongoTemplate mongoTemplate;

        @Qualifier("airBnbDb")
        @Autowired
        private  MongoTemplate mongoTemplateAirBnb;



        public List<Quote> findAllQuotes() {
              return mongoTemplate.findAll(Quote.class,"quotes");
        }

        public List<String> getAirBnbData() {
                System.out.print("Fetching Air BnB Data");
                return mongoTemplateAirBnb.findAll(String.class,"listingsAndReviews");
        }

        public void saveQuotes(List<Quote> quotes) {
                mongoTemplate.insert(quotes,"quotes");
        }
}
