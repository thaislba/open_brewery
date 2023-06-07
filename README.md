### About open_brewery
This project is an ETL of the public [Open Brewery DB API](https://www.openbrewerydb.org/documentation).
The goal is to extract the data, transform it and then load the data in an analytical environment. The proposal is to follow a Medallion architecture where data in the **raw** layer will be persisted in its native format, **curated** layer data in a columnar storage format partitioned by brewery location and **enriched** with agreggated views.

### Architecture proposed

![Label](/architecture.drawio.png)

### Data format
The artifacts of the extraction are JSON's and each one of them is supposed to have the following format:
````yaml
{
    "id": "",
    "name": "",
    "brewery_type": "",
    "address_1": "",
    "address_2": null,
    "address_3": null,
    "city": "",
    "state_province": "",
    "postal_code": "",
    "country": "",
    "longitude": "",
    "latitude": "",
    "phone": "",
    "website_url": "",
    "state": "",
    "street": ""
}
````

### Requirements
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

### Setup [in review]
- After cloning this repo and installing the requirements above, follow the steps: 
    - Navigate to the folder /openbrewery/airflow and run the commands:
    - ````gcloud auth application-default login```` - > grants access to your Google account
    - ````export GCP_KEY_PATH=~/.config/gcloud/application_default_credentials.json```` -> creates an environment variable that will be used in the container for authentication
- Check if the varible is correct by typing ````env````in the terminal 
- Run the container 
    - ````docker-compose -f docker-compose.yaml up````
- Open your [localhost](http://localhost:8080/)

### Execution
