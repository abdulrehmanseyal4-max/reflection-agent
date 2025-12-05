# reflection-agent

Add your description here.

## Project Details
* Name: `reflection-agent`
* Version: `0.1.0`

## Dependencies
* `black>=25.11.0` for code formatting
* `flask>=3.1.2` for web development
* `isort>=7.0.0` for import sorting
* `langchain>=1.1.0` for natural language processing
* `langchain-ollama>=1.0.0` for Ollama model integration
* `langchain-tavily>=0.2.13` for Tavily model integration
* `langgraph>=1.0.4` for graph-based conversation management
* `panel>=1.8.3` for web interface development
* `python-dotenv>=1.2.1` for environment variable management

## Usage
To run the reflection agent, simply execute the following command:

```bash
flask run
```

This will start the Flask development server, and you can access the web interface at `http://localhost:5000`.

### API Endpoints
The reflection agent exposes a single API endpoint for user input:
* `/input`: accepts GET requests with a query parameter `user_input` containing the text to be processed.

## Development
To develop the reflection agent further, clone this repository and install the dependencies using pip:

```bash
pip install -r requirements.txt
```

You can then run the development server using the following command:

```bash
flask run
```

### Testing
The reflection agent includes a suite of unit tests to ensure its functionality. You can run these tests using the following command:

```bash
pytest
```

## Contributing
Contributions are welcome! If you'd like to contribute to the development of this project, please fork this repository and submit a pull request.

### License
This project is licensed under the MIT License. See [LICENSE.txt](LICENSE.txt) for details.