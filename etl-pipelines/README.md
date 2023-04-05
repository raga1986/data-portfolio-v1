## ETL Pipeline

## Introduction
We built an ETL pipeline that carries out the following tasks:
- Extracts transactional data on 400k invoices from a Redshift Database.
- Transforms the data by identifying and removing duplicates
- Transforms the invoice_data field by fixing the data type.
- Loads the transformed data to a s3 bucket.
## Requirements
 The minimum requirements:
- Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/docker-for-mac/install/)
- Docker for Windows: ????

## Instructions
Copy the ``.env.example`` file to `.env` and fill out the environment vars.

Make sure you are executing the code from the etl_pipeline folder. 

To run it locally first build the image.

```bash
  docker image build -t etl-pipeline:0.1 .
```

Then run the job:
```bash
  docker run --env-file .env etl-pipeline:0.1
```

