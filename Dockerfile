FROM python
COPY . /application
WORKDIR /application
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "application.py"]