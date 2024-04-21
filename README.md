# API de Contagem de Vogais e Ordenação de Palavras

<div>
  <a href="https://pilar-case-28a56b588b23.herokuapp.com/health_check/">
    <img src="https://img.shields.io/badge/API-Heroku-430098?style=for-the-badge&logo=heroku" alt="Heroku">
  </a>
</div>

<div>
  <a href="https://pilar-case-28a56b588b23.herokuapp.com/docs">
    <img src="https://img.shields.io/badge/Documentação-API-blue" alt="Documentação">
  </a>
  <img src="https://img.shields.io/badge/coverage-100%25-brightgreen" alt="Coverage">
</div>

## Esta API fornece dois endpoints para manipulação de palavras:

1. **Contagem de Vogais**

   - Endpoint: `/count-vowels`
   - Método: `POST`
   - Descrição: Este endpoint conta o número de vogais em cada palavra fornecida na lista.
   - Corpo da Requisição:
     ```json
     {
       "words": ["batman", "robin", "coringa"]
     }
     ```
   - Exemplo de Uso:

     ```bash
     curl --request POST \
       --url http://localhost:8000/count-vowels \
       --header 'Content-Type: application/json' \
       --data '{
         "words": [
           "batman",
           "robin",
           "coringa"
         ]
       }'
     ```

   - Resposta Esperada:

   ```json
   {
     "batman": 2,
     "robin": 2,
     "coringa": 3
   }
   ```

2. **Ordenação de Palavras**

   - Endpoint: `/sort-words`
   - Método: `POST`
   - Descrição: Este endpoint ordena as palavras fornecidas em ordem alfabética, ascendente ou descendente, conforme especificado.
   - Corpo da Requisição:
     ```json
     {
       "words": ["batman", "robin", "coringa"],
       "order": "desc"
     }
     ```
   - Exemplo de Uso:

     ```bash
     curl --request POST \
       --url http://localhost:8000/sort-words \
       --header 'Content-Type: application/json' \
       --data '{
         "words": [
           "batman",
           "robin",
           "coringa"
         ],
         "order": "desc"
       }'
     ```

   - Resposta Esperada:

   ```json
   ["robin", "coringa", "batman"]
   ```

Certifique-se de fornecer um corpo de requisição válido com as palavras e a ordem desejada para a rota `/sort-words`.
