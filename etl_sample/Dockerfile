FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# run when the container starts
CMD ["python", "src/sample__etl_pipeline.py", "test.csv", "test.json", "sqlite:///test.db"]
