# agency_performance_model
agency_performance_model

### Set-up

    virtualenv env
    source env/bin/activate
    pip install requirements.txt
    python setup.py
    python api.py
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 000-000-000


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



### How to add a dataset:

First upload data with script or via AWS GUI.

    python upload_data.py finalapi.csv finalapi
    
Then in models/data.py add the dataset name to DATASETS:

    DATASETS = ['finalapi', 'new_dataset']  # Add your dataset here.


### Deployment


    zappa deploy dev