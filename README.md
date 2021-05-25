
# SIMPLE API

### An API that generates ``timestamp`` as key and a ``UUID``(Universal unique identifier) as value in a key-value pair. 

## TO RUN;
- Clone repository
- set up virtual environment
- install requirements --> pip install -r requirements.txt
- Then, 
```shell script
python app.py
```

#### OUTPUT
```json
{
  "2021-05-26 00:31:34.576753": "b113fdfac8314dc6a620e3bbcde7773c", 
  "2021-05-26 00:31:31.586216": "f78370f8c51b48958e2dde5cf41d8da3", 
  "2021-05-26 00:31:07.590016": "616c191fff3a4ca0b0441af572bc58f1", 
  "2021-05-26 00:30:56.983472": "487e0a8d01d6465f8a63c21dd91b43d7", 
  "2021-05-26 00:30:41.384636": "00124da9d5e948058c4d7bb1e36d6e6d", 
  "2021-05-26 00:30:37.480628": "6b6829227ce14b36afe4b2df10857a74", 
  "2021-05-26 00:27:32.317173": "837184b0783246abb496879abb735bea", 
  "2021-05-26 00:27:29.379352": "b1d9f110bc464111954cef2f0853c064", 
  "2021-05-26 00:27:26.552479": "a7c8a6c5fc9f485091b8c8e49d94e0b3"
}
```

NB: The implementation uses linked list. This is to ensure that the new uuid and timestamp pair is at the top of the json object returned (when a request is sent to the running server).