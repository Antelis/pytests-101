from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error

app = FastAPI()

class EquationResult(BaseModel):
    a: float
    b: float
    c: float
    d: float
    result: float

# Database connection function
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="mysql",  # Using service name from docker-compose
            user="root",
            password="password",
            database="equation_db"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.post("/store_result")
async def store_result(data: EquationResult):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
            INSERT INTO equation_results (a, b, c, d, result)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (data.a, data.b, data.c, data.d, data.result))
            connection.commit()
            return {"message": "Result stored successfully"}
        except Error as e:
            return {"error": str(e)}
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    else:
        return {"error": "Could not connect to database"}

@app.get("/get_results")
async def get_results():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM equation_results")
            results = cursor.fetchall()
            return {"results": results}
        except Error as e:
            return {"error": str(e)}
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    else:
        return {"error": "Could not connect to database"}