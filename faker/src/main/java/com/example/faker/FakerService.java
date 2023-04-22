package com.example.faker;

import com.example.model.Person;
import com.github.javafaker.Address;
import com.github.javafaker.Faker;
import com.github.javafaker.Name;
import com.hazelcast.com.google.common.collect.Lists;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Random;
import java.util.random.RandomGenerator;



@Component
public class FakerService {

    @Qualifier("testDb")
    @Autowired
    private MongoTemplate mongoTemplate;


    public List<Person> getPerson(Integer count) {

        List<Person> personList = Lists.newArrayList();
        for (int i = 0; i < count; i++) {
            Faker faker = new Faker();
            Person p = new Person();
            Name fakerName = faker.name();
            Address fakerAddress = faker.address();
            String companyName = faker.company().name();
            String position = faker.job().position();
            p.setFirstName(fakerName.firstName());
            p.setLastName(fakerName.lastName());
            p.setFullName(faker.name().fullName());
            p.setFavouriteArtist(faker.artist().name());
            p.setFavouriteSport(faker.team().sport());
            p.setCompanyName(companyName);
            p.setFavouriteAnimal(faker.animal().name());
            p.setAge(RandomGenerator.getDefault().nextInt(18,60));
            p.setSalary(RandomGenerator.getDefault().nextDouble(450000,100000000));
            p.setPosition(position);
            p.setAddress(fakerAddress.fullAddress());
            p.setBookName(faker.book().author());
            p.setSummary(faker.harryPotter().quote());
            p.setFavouriteAnimal(faker.animal().name());
            p.setCompanyName(faker.company().name());
            personList.add(p);
            System.out.println(i);
            mongoTemplate.save(p);
        }


        return personList;
    }
}
