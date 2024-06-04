# Afto-chatbot

cd frontend 

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

streamlit run frontend/app.py

cd flask_app 

python3 -m venv .flaskenv

source .flaskenv/bin/activate

pip install -r requirements.txt

flask run

pip freeze > requirements.txt

