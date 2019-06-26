# Python curator test



## Getting started

* This repository requires you to configure AWS account in the environment where it will run, for more
information on that visit https://aws.amazon.com/cli/

* It also depends on these environment variables

```
AWS_ES_HOST_URL
AWS_REGION
```

Where `AWS_ES_HOST_URL` is the URL provided by AWS for your elasticsearch cluster and `AWS_REGION` is the region where it exists

* To install this repository dependencies use

```bash
$ pip install -r requirements.txt
```

### Using this repository

**TODO**

## Development
To freeze the requirements of this repository 

```
pip freeze > requirements.txt
```