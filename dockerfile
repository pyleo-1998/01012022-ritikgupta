FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3 -m venv venv 
RUN . ./venv/bin/activate
RUN /usr/local/bin/python -m pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "tail","-f","/dev/null" ]
