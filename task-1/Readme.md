# How to Run

1. Make sure you have Python, Docker, and pip installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
4. Bring up the database by running the command:
   ```
   docker compose up
   ```
5. Start the server by running the command:
   ```
   python app
   ```
   This will launch a Flask server on port 5000.
6. [Optional] If you prefer to run the server within Docker, uncomment the corresponding code section in the `docker-compose.yml` file. Please note that the image creation may take some time initially, so it was commented out to avoid delays during image building and startup.
7. You can access the API using either of the following methods:
   - cURL: Use the following command to send a request:
     ```
     curl --location 'localhost:5000/api/v1/query?query=count%20of%20female%20passengerswho%20have%20siblings%20%3F&use_openai=true'
     ```
   - Refer to the `request.http` file in this repository for example requests.

# What it Does

1. The API accepts two request parameters:
   - `query`: The English text you want to convert into a SQL query.
   - `use_openai`: If set to `true`, the API will use OpenAI's Text to SQL API for conversion; otherwise, it will use the Eversql API.
2. Currently, the API returns a JSON array of results (records in the cursor).
3. In summary, this Python server delegates the text to SQL conversion to either OpenAI or Eversql. After receiving the SQL statement, it executes the query on the local database and provides the result.

# Key Learnings

During the development of this project, I acquired several key learnings:

1. Flask Server: This project marked my first experience in creating a Flask server, providing me with practical exposure to building and running a server using Flask.
2. AI Tool Integration: I integrated an AI tool into the application for the first time, leveraging either OpenAI's Text to SQL API or Eversql for converting text into SQL statements.
3. Adaptation to API Limitations: Initially, I used OpenAI's Text to SQL converter, but encountered rate limitations. As a result, I explored alternative solutions and discovered Eversql as another API provider for text to SQL conversion.
4. Understanding AI Tools: Although I didn't utilize the `ln2sql` library for this project, I gained valuable insights into the workings of AI tools on a smaller scale, further enhancing my understanding of these technologies.

Thank you for considering this project submission. If you have any additional questions or require further information, please don't hesitate to reach out.
