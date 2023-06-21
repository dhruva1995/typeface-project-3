# How to run

1. Ensure you have python and pip installed in your system
2. Clone this repository.
3. install dependencies by running `pip install -r requirements.txt`.
4. Start the server by running `python app`. It runs a flask server on port 5000.
5. You can access the api via
   1. cURL `curl --location 'localhost:5000/api/v1/query?query=count%20of%20female%20passengerswho%20have%20siblings%20%3F&use_openai=true' `
   2. Or refer request.http file in this repository.

# What it does ?

1. The API takes 2 request parameters
   1. query -> The english text you want to query.
   2. use_openai -> if a value of true is provided as input the api queries openai's text to sql api, or else uses eversql api for converting the provided text to SQL.
2. Curretly the api tries to return the json array of result(records in the cursor).
3. On a whole this python server, delegates text to sql conversion to either openai or eversql and post getting the sql statement, it execute the query on the local database and provides the result.

# My Learnings:

1. For the first time I created a flask server.
2. Used an ai tool in an app for the first time.
3. Initial developed the api using openai's text to sql converter, later got rate limited so figured out another api provider eversql who also provides text to sql converter.
4. Though I haven't used [ln2sql](https://github.com/FerreroJeremy/ln2sql) for this project, Got an oppurtunity to understand how these ai tools work under the hood is a micro scale.
