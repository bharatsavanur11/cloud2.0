package com.example.business;

import com.example.model.Person;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.logging.Logger;


@Controller
@Tag(description = "Quote API", name = "Quote Services")
public class MongoController {

    @Autowired
    private MongoService mongoService;

    private static final Logger log = Logger.getLogger("QuoteController");

    @Operation(summary = "Fetch the Quotes for Books", tags = {"User",},
            responses = {
                    @ApiResponse(responseCode = "200",
                            description = "Returns the registered user",
                            content = @Content(mediaType = "application/json",
                                    schema = @Schema(implementation = Quote.class)))
            })
    @GetMapping("/getQuotes")
    @ResponseBody
    public List<Quote> getQuote() throws InterruptedException {
        log.info("Calling Normal Flux App");
        return mongoService.findAllQuotes();
    }

    @Operation(summary = "Save the Quotes for Books", tags = {"Quotes",},
            responses = {
                    @ApiResponse(responseCode = "200",
                            description = "Returns the registered user",
                            content = @Content(mediaType = "application/json",
                                    schema = @Schema(implementation = Quote.class)))
            })
    @PostMapping("/saveQuotes")
    @ResponseBody
    public void saveQuote(@RequestBody  List<Quote> quotes) throws InterruptedException {
         mongoService.saveQuotes(quotes);
    }

    @Operation(summary = "Save the Quotes for Books", tags = {"Quotes",},
            responses = {
                    @ApiResponse(responseCode = "200",
                            description = "Returns the registered user",
                            content = @Content(mediaType = "application/json",
                                    schema = @Schema(implementation = Quote.class)))
            })
    @GetMapping("/searchFreeFlowText")
    @ResponseBody
    public List<String> searchFreeFlowText(@RequestParam String field, @RequestParam String searchText) throws InterruptedException {
        return mongoService.fetchMatchingSearchByFilterCriteria(field,searchText,"listingsAndReviews");
    }

    @Operation(summary = "Save the Quotes for Books", tags = {"Quotes",},
            responses = {
                    @ApiResponse(responseCode = "200",
                            description = "Returns the registered user",
                            content = @Content(mediaType = "application/json",
                                    schema = @Schema(implementation = Quote.class)))
            })
    @GetMapping("/performTextSearch")
    @ResponseBody
    public List<String> performTextSearchOnPersonCollection(@RequestParam String textToBeSearched) throws InterruptedException {
        return mongoService.fetchSearchTextData(textToBeSearched);
    }

    @Operation(summary = "Save the Quotes for Books", tags = {"Quotes",},
            responses = {
                    @ApiResponse(responseCode = "200",
                            description = "Returns the registered user",
                            content = @Content(mediaType = "application/json",
                                    schema = @Schema(implementation = Quote.class)))
            })
    @GetMapping("/performFullTextSearch")
    @ResponseBody
    public List<String> performFullTextSearchOnPersonCollection(@RequestParam String textToBeSearched) throws InterruptedException {
        return mongoService.performFullTextSearchOnPersonCollection(textToBeSearched);
    }



    @Operation(summary = "Save the Quotes for Books", tags = {"Quotes",},
            responses = {
                    @ApiResponse(responseCode = "200",
                            description = "Returns the registered user",
                            content = @Content(mediaType = "application/json",
                                    schema = @Schema(implementation = Quote.class)))
            })
    @GetMapping("/getAirBnBData")
    @ResponseBody
    public List<String> fetchAirBnbData() throws InterruptedException {
        return mongoService.getAirBnbData();
    }


}
