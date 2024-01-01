import requests

API_URL = API_URL = "https://api-inference.huggingface.co/models/marcus2000/TextRank_Longformer"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


### We need to generate few shot prompting techniques  from existing test data. This is different from
## instruction fine tuning of all the data.
prompt = ""

"""
Please generate a summary based on below revenue data:

| Product         | Year_2023 | Year_2022 | Year_2021 | Year_2020 |
|-----------------|-----------|-----------|-----------|-----------|
| Cash Equities   | 100       | 89        | 92        | 75        |
| Prime Brokerage | 88        | 99        | 95        | 72        |
| WM              | 23        | 34        | 25        | 23        | 

Summary:
 Cash Equities had good business compared to previous years.  Prime Brokerage has been volatile but compared
 to pre-covid period the revenue looks good. WM is performing a little less than expected. Need to focus on the real reason
 as to which product is not performing well.

"""

prompt += """
Please generate a summary based on below revenue data:

| Product         | Year_2023 | Year_2022 | Year_2021 | Year_2020 |
|-----------------|-----------|-----------|-----------|-----------|
| Cash Equities   | 100       | 89        | 92        | 75        |
| Prime Brokerage | 88        | 99        | 95        | 72        |
| WM              | 23        | 34        | 25        | 23        | 

Summary: """

output = query({
    "inputs": prompt
})

print(output)
