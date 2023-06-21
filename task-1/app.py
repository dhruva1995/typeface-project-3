from flask import Flask, request
import openai
from dotenv import dotenv_values
from sqlalchemy import create_engine, text
from requests import get
import logging


app = Flask(__name__)
env_variables = dotenv_values()

openai.api_key = env_variables["KEY"]

prompt_prefix = """
#MySQL Table
#CREATE TABLE passengers(id int,survived boolean,seat_class int,name text,gender enum('male','female'),age double,siblings int,ticket text,fare double,cabin text,embarked enum('Q','S','C'))
#A query to """

schema = """
CREATE TABLE `passengers` (
    `passenger_id` int NOT NULL,
    `survived` boolean DEFAULT NULL,
    `seat_class` int DEFAULT NULL,
    `name` varchar(255) DEFAULT NULL,
    `gender` ENUM('male', 'female'),
    `age` double DEFAULT NULL,
    `siblings` int DEFAULT NULL,
    `Parch` int DEFAULT NULL,
    `ticket` varchar(255) DEFAULT NULL,
    `fare` double DEFAULT NULL,
    `cabin` varchar(255) DEFAULT NULL,
    `embarked` ENUM('Q', 'S', 'C'),
    PRIMARY KEY (`passenger_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""


@app.route("/api/v1/query", methods=["GET"])
def index():
    query = request.args.get("query")
    use_openai = request.args.get("use_openai")
    if use_openai == "true":
        return get_result_from_openai(query)
    else:
        return get_result_from_eversql(query)


def get_result_from_openai(query):
    prompt = prompt_prefix + query + "\nSELECT"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["#", ";"],
        )

        sql = "SELECT " + response["choices"][0]["text"]
        # sql = "SELECT count(*) FROM passengers WHERE gender = 'female'"
        return execute_query(sql)
    except Exception as e:
        return "Encounted err: " + str(e)


def get_result_from_eversql(text):
    query_params = {"schema": schema, "prompt": text}
    try:
        response = get("https://www.eversql.com/api/generateSQLFromText", query_params)
        if response.status_code == 200:
            query = response.json()
            return execute_query(query)
        else:
            app.logger.error(
                f"Request to eversql failed with status code {response.status_code}"
                + str(response.text)
            )
            return f"Request to eversql failed with status code {response.status_code} {str(response.text)}"
    except Exception as e:
        return "Encountered err: " + str(e)


def execute_query(query):
    app.logger.info(f"Quering for: {query}")
    try:
        database = create_engine("mysql://sa:password@localhost:3306/titanic_db")
        with database.connect() as connection:
            response = connection.execute(text(query))
            results = response.all()
            results = [tuple(row) for row in results]
            return results
    except Exception as e:
        app.logger.error("Error while quering database", e)
        return "Encountered err:" + str(e)


if __name__ == "__main__":
    app.run(debug=True)
    # Set the log level and format
    app.logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Create a file handler to log to a file
    file_handler = logging.FileHandler("app.log")
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
