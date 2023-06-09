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
#### Extraction and Load
- After cloning this repo and installing the requirements above, follow the steps: 
    - Navigate to the folder /open_brewery and run the commands:
    - ````source .venv/bin/activate````
    - ````gcloud auth application-default login```` - > grants access to your Google account
    - ````export GCP_KEY_PATH=~/.config/gcloud/application_default_credentials.json```` -> creates an environment variable that will be used in the container for authentication
- Check if the variable is correct by typing ````env````in the terminal, it's expected to print the full path to the folder in your machine.
- Navigate to the folder /open_brewery/airflow  and build the image
- ````docker build -t open_brewery:latest . ````
- after that run the container: 
    - ````docker-compose -f docker-compose.yaml up````
- Open your [localhost](http://localhost:8080/)

#### Access to GCP open_brewery project 


### Execution

#### Extraction and Load
After you completed the setup of the environment and opened up the localhost, find the dag named ````open_brewery_pipeline`````.
This DAG has two tasks: 
    - extraction: it is responsible for calling the API, creating a file with the jsons returned and formatted to [NDJSON](http://ndjson.org/).
    - load: it is responsible for loading the data into a GCS bucket in GCP using your ADC(Application Default Credentials).
    
#### Transformations
The transformations will happen in the Cloud environment, using Cloud Composer(Airflow) to orchestrate Spark jobs to promote data from raw to curated and then from curated to enriched.
