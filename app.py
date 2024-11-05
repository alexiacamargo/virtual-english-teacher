import os
import openai
from flask import Flask, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)

# Carrega a chave da API de uma variável de ambiente
load_dotenv("key.env")  # Carrega variáveis do arquivo .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um professor de inglês."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Erro ao se comunicar com a API: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        prompt = f"Aluno: {user_input}\nProfessor de Inglês:"
        response = chat_gpt(prompt)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True, port=5500)
