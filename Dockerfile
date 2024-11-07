#
FROM python:3.10
#
WORKDIR /banking_integration
#
COPY ./requirements.txt /banking_integration/requirements.txt
#
RUN pip install --no-cache-dir --upgrade -r /banking_integration/requirements.txt
#
COPY ./.env /banking_integration/.env
COPY api/models /banking_integration/models
COPY api/common /banking_integration/common
COPY api/routers /banking_integration/routers
COPY api/serializers /banking_integration/serializers
COPY api/services /banking_integration/services
COPY ./README.md /banking_integration/README.md
COPY ./.gitignore /banking_integration/.gitignore
COPY ./init.sh /banking_integration/init.sh
COPY ./be /banking_integration/be
COPY ./main.py /banking_integration/main.py
#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]