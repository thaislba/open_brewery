### About open_brewery
This project is  work-in-progress ETL of the public [Open Brewery DB API](https://www.openbrewerydb.org/documentation).
The goal is to extract the data, transform it and then load the data in an analytical environment. The proposal is to follow a Medallion architecture where data in the **raw** layer will be persisted in its native format, **curated** layer data in a columnar storage format partitioned by brewery location and **enriched** with agreggated views.

### Architecture proposed (goal)

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
- [Java SDK]([https://www.java.com/en/download/](https://www.oracle.com/java/technologies/downloads/#jdk20-linux))

### Setup [in review]
#### Locally
- After cloning this repo and installing the requirements above, follow the steps: 
    - Navigate to the folder /open_brewery and run the commands:
    - ````source .venv/bin/activate```` -> activates the environment in which there's google cloud's necessary packages
    - ````gcloud auth application-default login```` -> grants access to your Google account
    - ````export GCP_KEY_PATH=~/.config/gcloud/application_default_credentials.json```` -> creates an environment variable that will be used in the container for authentication
- Check if the variable is correct by typing ````env````in the terminal, it's expected to print the full path to the folder in your machine
- Navigate to the folder /open_brewery/airflow  and build the image
- ````docker build -t open_brewery:latest . ````
- Execute the container: 
    - ````docker-compose -f docker-compose.yaml up````
- Open your [localhost](http://localhost:8080/)

#### Access to GCP open_brewery project 

To access this project you need to send me your gmail so I can add you in it with the proper permissions or you can create your own artifacts in GCP and reuse the code available here.

### Execution

#### Extraction and Load
After you completed the setup of the environment and opened up the localhost, find the dag named ````open_brewery_pipeline.py````.
This DAG has two tasks: 
    - extraction: it is responsible for calling the API, creating a file with the jsons returned and formatted to [NDJSON](http://ndjson.org/).
    - load: it is responsible for loading the data into a GCS bucket in GCP using your ADC(Application Default Credentials).
Execute the dag, if your access to the project in GCP is correct and your ADC credentials is working, a file should be loaded in the GCS bucket.

#### Transformations
(TBD)
The transformations will happen in the local environment using Airflow to orchestrate Spark jobs to promote data from raw to curated and then from curated to enriched.
    - raw: this layer was created using an external table from GCS to BQ
    - curated: dag named ````curated_open_brewery.py````will orchestrate a spark job named ````transform_to_curated.py````. This job is responsible from consuming raw data, transforming it and loading it to a table in the curated dataset.

Filter these dags by typing open_brewery in the Airflow's filter bar. 

#### Important things to acknowledge
    - If there's already a file in Cloud Storage bucket and the load DAG is executed again, it will throw an error. Make sure that you delete the file in the GCS bucket. This problem will be addressed in the future.
    - The codification of other languages still needs to be done at processing time.
    - The folder's tree can and will be improved.
   
   
