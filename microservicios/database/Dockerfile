FROM python:3.10-slim
WORKDIR /microservicios
COPY db.py .
RUN pip install fastapi uvicorn pydantic mysql-connector-python
CMD ["uvicorn", "db:app", "--host", "0.0.0.0", "--port", "8000"]