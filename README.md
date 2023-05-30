# Anonymous Twitter App with Weather Backend

This project aims to build the backend for an anonymous Twitter-like app that also displays current weather information. The backend is implemented using the Flask framework and PostgreSQL as the database. It follows the MVC (Model-View-Controller) architecture pattern and utilizes Flask blueprints for modularity and organization.

## Backend Architecture

The backend architecture is structured as follows:

- app/
- ├── posts/
- | ├── init.py
- | ├── models.py
- | ├── controller.py
- | └── routes.py
- ├── weather/
- | ├── init.py
- | ├── models.py
- | ├── controller.py
- | └── routes.py
- ├── utils/
- ├── init.py
- └── run.py


- The `posts` directory contains the implementation related to handling posts, including models, controllers, and routes.
- The `weather` directory contains the implementation related to handling weather information, including models, controllers, and routes.
- The `utils` directory contains utility functions that can be shared across different components of the backend.
- The `run.py` file is the entry point of the application.

## API Requirements

### Post Text Message API

- Endpoint: `/api/posts/create`
- Method: POST
- Description: Create a new post with a text message and user location.
- Parameters:
  - `text`: The text message of the post.
  - `lat`: Latitude of the user's location.
  - `lon`: Longitude of the user's location.
- Response: Success or failure message.

### Get Nearby Recent Posts API

- Endpoint: `/api/posts/nearby`
- Method: GET
- Description: Retrieve nearby recent posts based on the current location.
- Query Parameters:
  - `lat`: Latitude of the current location.
  - `lon`: Longitude of the current location.
  - `page`: Page number for pagination (default is 1).
- Response: List of nearby recent posts with a pretty timestamp, paginated with ten posts per page.

### Get Current Weather API

- Endpoint: `/api/weather/current`
- Method: GET
- Description: Retrieve the current weather information for a given location.
- Query Parameters:
  - `lat`: Latitude of the location.
  - `lon`: Longitude of the location.
- Response: Current weather information from the integrated third-party weather API.

## Installation and Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies from `requirements.txt`.
4. Configure the PostgreSQL database settings in `config.py`.
5. Run the database migrations using `python manage.py db upgrade`.
6. Start the application server with `python run.py`.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
