# Todo App

A simple Todo application built with Django.

## Prerequisites

- Python version: 3.6 or higher
- PostgreSQL database (or your preferred database)

## Installation

1. Clone the repository:

git clone https://github.com/SherazSafdar/ToDo-App-Django


2. Change to the project directory:


3. Create and activate a virtual environment :
python -m venv venv
source venv/bin/activate # On macOS and Linux
.\venv\Scripts\activate # On Windows


4. Install project dependencies from the requirements.txt file:
pip install -r requirements.txt


## Configuration

1. Create a `.env` file in the project directory and configure environment variables such as database credentials:

DATABASE_URL=your_database_connection_url
SECRET_KEY=your_secret_key
DEBUG=True # Change to False in production


2. Apply database migrations:

python manage.py migrate


3. Start the development server:

python manage.py runserver

## Contact

- Sheraz Safdar
- sherazsafdar00@gmail.com

Feel free to reach out if you have any questions or need assistance.


