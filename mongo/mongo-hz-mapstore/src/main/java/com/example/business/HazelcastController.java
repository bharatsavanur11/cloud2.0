package com.example.business;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller("/hz")
@Tag(description = "Hazelcast Controller API", name = "Hazelcast Services To Demo Write Through Cache")
public class HazelcastController {

    private HazelcastService hazelcastService;

    @Autowired
    public HazelcastController(HazelcastService hazelcastService) {
        this.hazelcastService = hazelcastService;
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
    public void saveQuote(@RequestBody List<Quote> quotes) throws InterruptedException {
        hazelcastService.saveQuotes(quotes);
    }

}
