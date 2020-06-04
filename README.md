### Purpose

This is a POC showing how you can use Jenkins and MLflow with Machine Learning.

### Data

The data used is pulled from yahoo finance. 



### ML

The Machine Learning in this project is just used as an example. It is a clustering algorith called Gaussian mixture models implimenmted using sklearn.

### Setup

1. Docker:

2. Jenkins:
sudo docker exec -it -u root <contianerid> bash
apt-get update
apt install python3-pip python3
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
curl https://pyenv.run | bash
export PATH="$HOME/.pyenv/bin:$PATH" && \
eval "$(pyenv init -)" && \
eval "$(pyenv virtualenv-init -)"&& \
pyenv install 3.7.4 && \
pyenv virtualenv 3.7.4 app && \
pyenv activate app
pyenv virtualenvs
pyenv activate <name>
pip3 install -r mlpipeline_jenkins/app/requirements.txt
pip3 install pandas yfinance psycopg2-binary pytest sklearn mlflow boto3
pyenv deactivate
pyenv virtualenv-delete my-virtual-env

3. AWS:

