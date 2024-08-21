# Server

## Setup
```shell
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip && pip3 install -r requirements.txt
```

## How to Deploy
1. remove lambda and Terraform apply
```shell
cd terraform
terraform apply
```
2. Push Docker to ECR
```shell
cd src
tar -cJh . | docker build -t app/ecr/mms/prod:latest -
export YOUR_ACCOUNT_ID=000000000
docker tag app/ecr/mms/prod ${YOUR_ACCOUNT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/app/ecr/mms/prod
```
3. Add lambda and Terraform apply
```shell
cd terraform
terraform apply
```

4. Apply lambda
```shell
aws ecr get-login-password --region ap-northeast-1 | docker login  --username AWS --password-stdin ${YOUR_ACCOUNT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com
docker push ${YOUR_ACCOUNT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/app/ecr/mms/prod
```

## Run FastAPI (Local)
```shell
cd src
uvicorn main:app --reload
```