
# SIMPLE API

### An API that generates ``timestamp`` as key and a ``UUID``(Universal unique identifier) as value in a key-value pair. 

## TO RUN;
- Clone repository
- set up virtual environment
- install requirements --> pip install -r requirements.txt
- run, 
```shell script
python app.py
```
- Then open ``http://127.0.0.1:5000/`` in your browser

#### OUTPUT
```json
{
  "2021-05-26 11:20:36.719414": "addfa544d3ee4d068b3b9004557640eb", 
  "2021-05-26 11:05:55.150258": "f3915f01f4964e4fb82d9f271396e409", 
  "2021-05-26 11:04:22.190809": "03a138b4fcea4fe4918352af9bb167af", 
  "2021-05-26 11:03:19.375524": "1376882aae734a4385af5e095ffada83", 
  "2021-05-26 11:01:49.152717": "deda4d7d35994cbca0257e3d1d78d221", 
  "2021-05-26 11:01:25.572493": "73b9007b919c4155982edf95b3ab925b", 
  "2021-05-26 11:01:10.262273": "36bc086235ca4442b9bbe84a62175dcb", 
  "2021-05-26 11:01:05.739710": "535236796be4486dbb15da113db6947b", 
  "2021-05-26 11:00:52.941019": "6d9fbf246e5e440790cdddc3019106b3", 
  "2021-05-26 09:32:00.667631": "7986901f23f444678593b2e49e4e31e8", 
  "2021-05-26 08:54:56.590200": "79e844f787a445469d76d27605e0de68", 
  "2021-05-26 08:52:27.849270": "6c050fea9b78494293d177fe1761f447", 
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