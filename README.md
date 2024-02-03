## tool poetry dependencies
- python = "^3.11"
- pydantic = "^2.6.0"
- httpx = "^0.26.0"
- fastapi = "^0.109.0"
- uvicorn = "^0.27.0.post1"
- aiohttp = "^3.9.3"

Projeto de conversão de moedas consumindo a API da ExchangeRate-API gratuita.<br>
Ao clonar o projeto não esquecer de criar um <b>.env</b> e utilizar a variavel <b>'EXCHANCE_APIKEY=Your API Key'</b> e colocar sey API KEY da ExchangeRate.

O projeto consta com 2 versões em modelo <b>Asíncrona</b> e <b>Assíncrona</b>, as HTTP Requests dos testes unitarios estão disponíveis na pasta 'Collection-Insomnia'.

Ao modificar o arquivo .env sempre executar o source .env e uvicorn main:app --reload para debugar o projeto.<br>

http://localhost:8000/docs
![image](https://github.com/alexandreribeiro7/FastAPI-project/assets/89461762/e154ea03-728e-4561-af20-1549327db727)
