package com.example.business;

import com.example.MongoConfig;
import com.example.model.Person;
import com.hazelcast.com.google.common.collect.Lists;
import com.hazelcast.core.HazelcastInstance;
import com.hazelcast.map.IMap;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Indexes;
import com.mongodb.client.model.TextSearchOptions;
import io.micrometer.core.instrument.LongTaskTimer;
import io.micrometer.core.instrument.simple.SimpleMeterRegistry;
import org.bson.Document;
import org.bson.conversions.Bson;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.TextCriteria;
import org.springframework.data.mongodb.core.query.TextQuery;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Logger;

import static com.mongodb.client.model.Aggregates.match;


@Component
public class MongoService {


    private static final Logger log = Logger.getLogger("QuoteController");

    private static long DELAY_BY_TIME = 1000;

    @Qualifier("testDb")
    @Autowired
    private MongoTemplate mongoTemplate;

    @Qualifier("airBnbDb")
    @Autowired
    private MongoTemplate mongoTemplateAirBnb;


    public List<Quote> findAllQuotes() {
        return mongoTemplate.findAll(Quote.class, "quotes");
    }

    public List<String> getAirBnbData() {
        System.out.print("Fetching Air BnB Data");
        return mongoTemplateAirBnb.findAll(String.class, "listingsAndReviews");
    }

    public List<String> getAirBnbDataFullTextSearch() {
        System.out.print("Fetching Air BnB Data");
        return mongoTemplateAirBnb.findAll(String.class, "listingsAndReviews");
    }

    public List<String> fetchMatchingSearchByFilterCriteria(String field, String searchText, String collectionName) {
        Query searchFreeTextQuery = new Query();
        searchFreeTextQuery.addCriteria(Criteria.where(field).regex(searchText));
        SimpleMeterRegistry registry = new SimpleMeterRegistry();
        LongTaskTimer longTaskTimer = LongTaskTimer.builder("3rdPartyService").register(registry);
        LongTaskTimer.Sample currentTaskId = longTaskTimer.start();
        List<String> returnData = mongoTemplateAirBnb.find(searchFreeTextQuery, String.class, collectionName);
        long timeElapsed = currentTaskId.stop();
        System.out.println("Time Elapsed in milliseconds" + timeElapsed / ((int) 1e6));
        //System.out.print("Data Returned"+returnData);
        return returnData;
    }

    public void saveQuotes(List<Quote> quotes) {
        mongoTemplate.insert(quotes, "quotes");
    }

    public List<String> fetchSearchTextData(String text) {
        MongoCollection personCollection =  mongoTemplate.getCollection("person");
        String resultCreateIndex = personCollection.createIndex(Indexes.text("fullName"));
        TextSearchOptions options = new TextSearchOptions().caseSensitive(false);
        System.out.println(String.format("Index created: %s", resultCreateIndex));
        Bson filter = Filters.text("John", options);
        personCollection.find(filter).forEach(doc->System.out.println(doc));
        return Lists.newArrayList();
    }

    public List<String> performFullTextSearchOnPersonCollection(String text) {
        // $search is the criteria used for querying the full text search and
        // there is no known Spring Data template API that provides a full
        // text search.
        // We first have to create a search index on all the fields in the document
        // then mention this specific index in document filter to
        // use it. Underlying technology is Apache Lucene.
        List<Document> filterCriteria = Arrays.asList(new Document("$search",
                new Document("index", "default")
                       .append("text",
                                new Document("query", text).append("path", new Document("wildcard","*"))
                                        )));

        MongoCollection personCollection =  mongoTemplate.getCollection("person");
        List<String> documents = Lists.newArrayList();
        personCollection.aggregate(filterCriteria).forEach(result->{
            documents.add(result.toString());
        });
    return documents;
    }
}
