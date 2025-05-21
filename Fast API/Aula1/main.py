from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return{'message':'Hello World'}

@app.get('/nomes/{nome}')
async def nomes(nome):
    return {'message': f'Ola {nome}'}