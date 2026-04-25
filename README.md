# BlogApp

English | [中文版](./README_CN.md)

A simple Flask-based blog application with user authentication and todo management.

## Features

- User login and logout
- Create, view, edit, and delete todo items
- Database management with SQLite
- CSRF protection
- Responsive UI with Bootstrap

## Requirements

- Python 3.6+
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/onesingle/blogapp.git
   cd blogapp
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python3 blogapp.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000`

## Configuration

Edit `config.cfg` to change settings:

- `SQLALCHEMY_DATABASE_URI`: Database URI (default: SQLite)
- `SECRET_KEY`: Secret key for sessions
- `DEBUG`: Debug mode (set to False in production)

## Usage

- **Login**: Use username `admin` and password `blog`
- **Home**: View all todos
- **New Todo**: Create a new todo item
- **View/Edit**: Click on a todo ID to view or edit
- **Delete**: Use the delete button on the view page

## Project Structure

- `blogapp.py`: Main application file
- `view.py`: Route handlers
- `data.py`: Database models (currently empty, models moved to blogapp.py)
- `config.cfg`: Configuration file
- `templates/`: HTML templates
- `static/`: CSS and JS files
- `requirements.txt`: Python dependencies

## License

This project is open source.