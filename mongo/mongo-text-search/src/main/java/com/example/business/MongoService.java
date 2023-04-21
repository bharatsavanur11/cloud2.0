package com.example.business;

import com.example.MongoConfig;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.map.IMap;
import io.micrometer.core.instrument.LongTaskTimer;
import io.micrometer.core.instrument.simple.SimpleMeterRegistry;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
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

        public List<String> fetchMatchingSearchByFilterCriteria(String field, String searchText,String collectionName) {
                Query searchFreeTextQuery = new Query();
                searchFreeTextQuery.addCriteria(Criteria.where(field).regex(searchText));
                SimpleMeterRegistry registry = new SimpleMeterRegistry();
                LongTaskTimer longTaskTimer = LongTaskTimer.builder("3rdPartyService").register(registry);
                LongTaskTimer.Sample currentTaskId = longTaskTimer.start();
                List<String>  returnData =  mongoTemplateAirBnb.find(searchFreeTextQuery,String.class,collectionName);
                long timeElapsed = currentTaskId.stop();
                System.out.println("Time Elapsed in milliseconds" + timeElapsed/((int) 1e6));
                //System.out.print("Data Returned"+returnData);
                return returnData;
        }

        public void saveQuotes(List<Quote> quotes) {
                mongoTemplate.insert(quotes,"quotes");
        }
}
