FROM python:3
COPY . .
RUN pip install pytest
RUN pip install allure-pytest
RUN pip install requests
CMD python3 main.py


