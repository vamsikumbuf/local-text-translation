FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y bash curl
CMD ["echo", "hello world!!"]

RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN mkdir /home/simple_llm
COPY . /home/simple_llm

WORKDIR /home/simple_llm

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
