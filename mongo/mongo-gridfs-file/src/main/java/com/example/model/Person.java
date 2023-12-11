package com.example.model;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.mongodb.core.index.TextIndexed;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.TextScore;

@Data
@Getter
@Setter
@Document(collection="person")
public class Person {

    @TextIndexed(weight=5)
    private String firstName;
    private String lastName;
    private String fullName;
    private String address;
    private Double salary;
    private Integer age;
    private String summary;
    private String companyName;
    private String position;
    private String bookName;
    private String favouriteAnimal;
    private String favouriteArtist;
    private String favouriteSport;

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {

        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public void setCompanyName(String companyName) {
        this.companyName = companyName;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public void setBookName(String bookName) {
        this.bookName = bookName;
    }

    public void setFavouriteAnimal(String favouriteAnimal) {
        this.favouriteAnimal = favouriteAnimal;
    }

    public void setFavouriteArtist(String favouriteArtist) {
        this.favouriteArtist = favouriteArtist;
    }

    public void setFavouriteSport(String favouriteSport) {
        this.favouriteSport = favouriteSport;
    }

    public String getLastName() {
        return lastName;
    }

    public String getFullName() {
        return fullName;
    }

    public String getAddress() {
        return address;
    }

    public Double getSalary() {
        return salary;
    }

    public Integer getAge() {
        return age;
    }

    public String getSummary() {
        return summary;
    }

    public String getCompanyName() {
        return companyName;
    }

    public String getPosition() {
        return position;
    }

    public String getBookName() {
        return bookName;
    }

    public String getFavouriteAnimal() {
        return favouriteAnimal;
    }

    public String getFavouriteArtist() {
        return favouriteArtist;
    }

    public String getFavouriteSport() {
        return favouriteSport;
    }
}
