package com.example.business;

import com.hazelcast.core.HazelcastInstance;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class HazelcastService {

    private HazelcastInstance hazelcastInstance;

    @Autowired
    public HazelcastService(HazelcastInstance hazelcastInstance) {
        this.hazelcastInstance = hazelcastInstance;
    }

    public void saveQuotes(List<Quote> quotes) {
        quotes.forEach(quote-> hazelcastInstance.getMap("quotes").put(quote.getId(),quote));

    }
}
