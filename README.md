### About open_brewery
This project is an ETL of the public [Open Brewery DB API](https://www.openbrewerydb.org/documentation).
The goal is to extract the data, transform it and then load the data in an analytical environment. The proposal is to follow a Medallion architecture where data in the raw layer will be persisted in its native format, curated layer data in a columnar storage format partitioned by brewery location and enriched with agreggated views. 

### Architecture proposed

![Label](/architecture.drawio.png)

### Data format
The artifects of the extraction are JSON's and each one has the following format:
````
{
    "id": "",
    "name": "",
    "brewery_type": "",
    "address_1": "5164 Kennedy Ave",
    "address_2": null,
    "address_3": null,
    "city": "Cincinnati",
    "state_province": "Ohio",
    "postal_code": "45213",
    "country": "United States",
    "longitude": "-84.4137736",
    "latitude": "39.1885752",
    "phone": "5138368733",
    "website_url": "http://www.madtreebrewing.com",
    "state": "Ohio",
    "street": "5164 Kennedy Ave"
}
````
### Execution
