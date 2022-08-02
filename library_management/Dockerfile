FROM python:3.8

RUN pip install --upgrade pip

WORKDIR /library_management

COPY  requirements.txt /library_management/

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /

ENTRYPOINT [ "sh","/entrypoint.sh" ]