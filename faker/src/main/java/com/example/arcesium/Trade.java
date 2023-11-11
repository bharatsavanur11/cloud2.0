package com.example.arcesium;

import java.time.LocalDate;

public class Trade {

    private LocalDate tradeDate;
    private String tickerId;

    private String buySell;

    private Integer quantity;

    private Double price;

    public Trade(LocalDate tradeDate, String tickerId, String buySell, Integer quantity, Double price) {
        this.tradeDate = tradeDate;
        this.tickerId = tickerId;
        this.buySell = buySell;
        this.quantity = quantity;
        this.price = price;
    }

    public LocalDate getTradeDate() {
        return tradeDate;
    }

    public void setTradeDate(LocalDate tradeDate) {
        this.tradeDate = tradeDate;
    }

    public String getTickerId() {
        return tickerId;
    }

    public void setTickerId(String tickerId) {
        this.tickerId = tickerId;
    }

    public String getBuySell() {
        return buySell;
    }

    public void setBuySell(String buySell) {
        this.buySell = buySell;
    }

    public Integer getQuantity() {
        return quantity;
    }

    public void setQuantity(Integer quantity) {
        this.quantity = quantity;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }
}
