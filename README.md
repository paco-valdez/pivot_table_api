# Pivot Table API


This app provides a RESTful API and it's meant to run as a serverless app on AWS.
The data most be on a "record" format. The upload_data.py script transforms it to a 2-dimensional pivot tables, although it could easily be modified to support more dimensions. The API Database back-end is schema-agnostic so it can handle any kind of data, although the demo front-end site only supports 2-Dimension pivot tables.  
The pivot tables are defined in the "pivots.json", the sample file is meant to be used with this data: [Agency Perfomance Model](https://www.kaggle.com/moneystore/agencyperformance)
The Data pipeline consists in calculate all the pivot tables defined in the "pivots.json" file, and then upload all the calculated data to the relational data base and then uploads a CSV file for each pivot table to S3. Then the REST api only serves a pre-calculated version of each table.  


[Demo Site](https://s3-us-west-1.amazonaws.com/static-hruncx1gi/index.html)

[Demo API endpoint](https://re291hwt17.execute-api.us-west-1.amazonaws.com/dev/)

### Set-up

    virtualenv /tmp/env
    source /tmp/env/bin/activate
    pip install requirements.txt
    python setup.py
    python upload_data.py record_data_file_name.csv
    python api.py
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 000-000-000

### Data Pipeline:

Define pivots in pivots.json:

    {
      "columns":["STAT_PROFILE_DATE_YEAR", "STAT_PROFILE_DATE_MONTH", "STATE_ABBR"],
      "rows":["PROD_LINE", "AGENCY_ID", "PROD_ABBR", "STATE_ABBR"],
      "values": {
        "sum":["RETENTION_POLY_QTY", "WRTN_PREM_AMT", "LOSS_RATIO"],
        "mean":["RETENTION_POLY_QTY", "WRTN_PREM_AMT", "LOSS_RATIO"]
      },
      "reports": ["AGENCY_ID", "PROD_LINE"]
    }

Upload data with script

    python upload_data.py file_name.csv

## REST API

### Create Users:

    curl -i -X POST -H "Content-Type: application/json" -d '{"username":"demo","password":"demo"}'  http://127.0.0.1:5000/user

Response:

    HTTP/1.0 201 CREATED
    Content-Type: application/json
    Content-Length: 60
    Server: Werkzeug/0.12 Python/2.7.10
    Date: Thu, 14 Dec 2017 00:35:03 GMT
    
    {
        "message": "User created",
        "status": "success"
    }


### Query datasets

Dataset endpoint:  
    
    '/dataset/<string:dataset>'

The dataset key is created by the following pattern 
    
    '{funcion}-{value}-{row}-{column}' 

CURL example:

    curl -u demo:demo -i -X GET http://127.0.0.1:5000/dataset/sum-RETENTION_POLY_QTY-PROD_LINE-STAT_PROFILE_DATE_YEAR
    HTTP/2 200
    content-type: application/json
    content-length: 434
    date: Sun, 17 Dec 2017 18:27:45 GMT
    x-amzn-requestid: f8e55bf9-e357-11e7-8332-49c9e9ac1155
    access-control-allow-origin: *
    access-control-allow-headers: Content-Type,Authorization,X-Requested-With,Access-Control-Request-Headers
    x-amzn-remapped-content-length: 434
    access-control-allow-methods: GET,PUT,POST,DELETE,OPTIONS
    x-amzn-trace-id: sampled=0;root=1-5a36b71f-d8eddd7c43b4e8a037c085f6
    x-cache: Miss from cloudfront
    via: 1.1 3c6cd3705576f791e49d58b73a16e8f0.cloudfront.net (CloudFront)
    x-amz-cf-id: BuFb_jl9X3xyr0o2AqG1bb5n_XXm-XstjcZB6CDD_Z8z6Y8nmxjyFQ==
    
    {"column": "STAT_PROFILE_DATE_YEAR", "data": {"index": [0, 1], "data": [["CL", 169879, 256017, 258091, 258684, 263546, 269332, 267612, 255067, 243525, 241323, 101629], ["PL", 2315892, 3452416, 3429509, 3363486, 3309463, 3226686, 3072411, 2852566, 2690338, 2562238, 981476]], "columns": ["PROD_LINE", 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]}, "func": "sum", "value": "RETENTION_POLY_QTY", "row": "PROD_LINE"}

## Deployment

### Upload AWS lambda function

    zappa deploy dev
    
### Update AWS lambda function

    zappa deploy dev

### Collect Static Files (sync with S3)

    cd static/
    aws s3 sync . s3://bucket-name --acl public-read


### TESTS

Run tests:

    export PYTHONPATH='/path/to/repo/directory/':$PYTHONPATH
    cd resources/tests/
    python test_users.py
    python test_data.py
