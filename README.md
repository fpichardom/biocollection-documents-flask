# Flask APP with TailwindCSS template

## Start

Have Python and NodeJS installed
- `python3 -m venv venv`:create venv in top folder
- install packages with npm to create package.json file
  - `npm install -D tailwindcss`
  - `npm install flowbite`
- Build watch tailwindcss
  - `npx tailwindcss init`
  - `npx tailwindcss -i ./app/static/src/input.css -o ./app/static/dist/css/output.css --watch`

Required Python packages

- `flask`
- `flask-sqlalchemy`
- `flask-wtf`
- `flask-migrate`
- `flask-login`
- `pymysql`
- `python-dotenv`

## Requirement list

When installing more python packages remember:
- `pip freeze > requirements.txt`: save current list of installed packages with pip to the requirements.txt file