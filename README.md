# late-show


The **Late Show** is a RESTful API that allows you to manage episodes, guests, and their appearances on the show. It provides endpoints for retrieving episodes and guests, and for creating new appearances by associating guests with episodes.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Endpoints](#endpoints)
    - [GET /episodes](#get-episodes)
    - [GET /episodes/:id](#get-episodesid)
    - [GET /guests](#get-guests)
    - [POST /appearances](#post-appearances)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Retrieve a list of episodes.
- Retrieve details about a specific episode, including its guest appearances.
- Retrieve a list of guests.
- Create new guest appearances by associating a guest with an episode.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/lateshow-api.git

2. **Navigate to the project directory**:

   ```bash
cd lateshow

3. **Install the required dependencies**: Make sure you have ***Python*** installed and then install the required libraries:

   ```bash
   pip install -r requirements.txt

4. **Set up the database**: Use the provided seed script to populate the database with some initial data:

    ```bash
    python seed.py

5. **Run the Flask app**:

   ```bash
    flask run

**The app will be available at http://localhost:5000.**


**Usage**
Once the application is running, you can interact with the API using tools like Postman or curl.

**Endpoints**
**GET /episodes**
- Returns a list of all episodes.

- URL: /episodes
- Method: GET
- Response:
 ```json

[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  }
]

GET /episodes/
Returns details of a specific episode, including guest appearances.

- URL: /episodes/:id

- Method: GET

- Response (if the episode exists):

  ```json
Copy code
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      },
      "guest_id": 1,
      "id": 1,
      "rating": 4
    }
  ]
}

- Response (if the episode does not exist):

  ```json

{
  "error": "Episode not found"
}


**GET /guests**
Returns a list of all guests.

- URL: /guests
- Method: GET
- Response:

   ```json 

[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  },
  {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
]


**POST /appearances**
Creates a new appearance that links an existing guest to an episode.

- URL: /appearances

- Method : POST

- Request Body :

  ```json

{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 1
}
Response (if created successfully):

  ```json

{
  "id": 162,
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1,
  "episode": {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  "guest": {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  }
}

**Response (if validation fails)**:

   ```json

{
  "errors": ["validation errors"]
}

**Technologies**
- Python
- Flask (for the web framework)
- SQLite (for the database)
- Postman (for testing the API)

**Contributing**
Contributions are welcome! Feel free to submit a pull request or open an issue if you find bugs or want to suggest improvements.

**License**
This project is licensed under the MIT ***License***. See the LICENSE file for more details.