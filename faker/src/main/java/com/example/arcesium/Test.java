package com.example.arcesium;

import java.io.File;
import java.io.FileNotFoundException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Test{

    public static void main(String args[]){
        List<Trade> trades  = new ArrayList<>();
        try {
            File myObj = new File("/Users/bharatsavanur/Desktop/projects/personal_git/cloud-2.0/faker/src/main/java/data");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] tokens = data.split(",");
                validate(tokens);
                Trade trade = new Trade(LocalDate.parse(tokens[0]),tokens[1],tokens[2],Integer.parseInt(tokens[3]),Double.parseDouble(tokens[4]));
                trades.add(trade);
                System.out.println(data);
            }

            myReader.close();

            System.out.println("Tax===" + calculateTax(trades));

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    private static Double calculateTax(List<Trade> trades) {
        List<Double> profitLoss  = new ArrayList<>();
        Double totalPnl = 0.0;
        List<Trade> validTrades = trades.stream().filter(trade->trade.getTradeDate().getYear()==2015).toList();
        for(int i=0;i<validTrades.size();i++){
            Trade currentTrade = validTrades.get(i);
            matchTheCurrentTrade(i,validTrades,currentTrade,profitLoss);
        }
        for(int i=0;i<profitLoss.size();i++){
            totalPnl = totalPnl + profitLoss.get(i);

        }
        return totalPnl * .25;
    }

    private static void matchTheCurrentTrade(int index, List<Trade> validTrades,Trade currentTrade,List<Double> profitLoss) {
        if(currentTrade.getBuySell().equals("S")){
            for(int i=0;i<index;i++){
                Trade tradeBeingConsidered = validTrades.get(i);
                if(tradeBeingConsidered.getBuySell().equals("B") &&
                        tradeBeingConsidered.getTickerId().equals(currentTrade.getTickerId()) && tradeBeingConsidered.getQuantity()>0){
                    Integer sellQuantity = currentTrade.getQuantity();
                    Integer buyQuantity = tradeBeingConsidered.getQuantity();
                    if(buyQuantity>sellQuantity){
                        Double pnl = (currentTrade.getQuantity()* currentTrade.getPrice()) - (currentTrade.getQuantity()* tradeBeingConsidered.getPrice());
                        profitLoss.add(pnl);
                        System.out.println("PNL ==="+ pnl);
                        currentTrade.setQuantity(0);
                        tradeBeingConsidered.setQuantity(buyQuantity-sellQuantity);
                    }else{
                        Double pnl = (tradeBeingConsidered.getQuantity()* currentTrade.getPrice()) - (tradeBeingConsidered.getQuantity()* tradeBeingConsidered.getPrice());
                        profitLoss.add(pnl);
                        System.out.println("PNL ==="+ pnl);

                        // reduce the current sell trade to diff
                        currentTrade.setQuantity(sellQuantity-buyQuantity);
                        //set Buy trade to zero
                        tradeBeingConsidered.setQuantity(0);
                    }
                }else{
                    continue;
                }
            }
        }else{
                // when current trade is buy
                for(int i=0;i<index;i++){
                    System.out.println("Val of i==" +index);
                    Trade tradeBeingConsidered = validTrades.get(i);
                    if(tradeBeingConsidered.getBuySell().equals("S") &&
                            tradeBeingConsidered.getTickerId().equals(currentTrade.getTickerId()) && tradeBeingConsidered.getQuantity()>0){
                        Integer buyQuantity = currentTrade.getQuantity();
                        Integer sellQuantity = tradeBeingConsidered.getQuantity();
                        if(buyQuantity>sellQuantity){
                            Double pnl = (tradeBeingConsidered.get  Quantity()* tradeBeingConsidered.getPrice()) - (tradeBeingConsidered.getQuantity()* currentTrade.getPrice());
                            profitLoss.add(pnl);
                            System.out.println("PNL ==="+ pnl);
                            tradeBeingConsidered.setQuantity(0);
                            currentTrade.setQuantity(buyQuantity-sellQuantity);
                        }else{
                            Double pnl = (currentTrade.getQuantity()* tradeBeingConsidered.getPrice()) - (currentTrade.getQuantity()* currentTrade.getPrice());
                            profitLoss.add(pnl);
                            System.out.println("PNL ==="+ pnl);

                            // reduce the current sell trade to diff
                            tradeBeingConsidered.setQuantity(sellQuantity-buyQuantity);
                            //set Buy trade to zero
                            currentTrade.setQuantity(0);
                        }
                    }else{
                        continue;
                    }


                }
            }




    }

    private static void validate(String[] tokens) {
    }
}
