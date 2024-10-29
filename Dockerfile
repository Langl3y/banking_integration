#
FROM python:3.8.19
#
WORKDIR /banking_integration
#
COPY ./requirements.txt /banking_integration/requirements.txt
#
RUN pip install --no-cache-dir --upgrade -r /banking_integration/requirements.txt
#
COPY ./.env /banking_integration/.env
COPY ./common /banking_integration/common
COPY ./routers /banking_integration/routers
COPY ./serializers /banking_integration/serializers
COPY ./services /banking_integration/services
COPY ./main.py /banking_integration/main.py
#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]