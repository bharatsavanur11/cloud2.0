package com.example.faker;

import com.example.business.MongoService;
import com.example.business.Quote;
import com.example.model.Person;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;
import java.util.logging.Logger;

@Controller
@RequestMapping("/fakeData")
@Tag(description = "Faker API", name = "Faker Services")
public class FakerController {

    @Autowired
    private FakerService fakerService;

    private static final Logger log = Logger.getLogger("FakerController");

    @Operation(summary = "Fetch the Quotes for Books", tags = {"User",},
            responses = {
                    @ApiResponse(responseCode = "200",
                            description = "Returns the registered user",
                            content = @Content(mediaType = "application/json",
                                    schema = @Schema(implementation = Quote.class)))
            })
    @GetMapping("/generateFakerPersonData")
    @ResponseBody
    public List<Person> getPersonList(@RequestParam  int count) throws InterruptedException {
        // use slf4k logger for better performance
        log.info("Create {} number of person list using faker"+count);
        return fakerService.getPerson(count);
    }
}
