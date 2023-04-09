package vo;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@EqualsAndHashCode
public class TradeData {

    private String tradeId;
    private String assetType;
    private Double priceType;
    private String internalCompany;
    private String counterParty;
    private String quoteId;
}
