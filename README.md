  # Teste API 

Este projeto cria uma API com FastAPI que permite buscar operadoras de saúde a partir de um arquivo CSV cadastral da ANS.

## O que o script faz

- Lê e limpa os dados do arquivo CSV
- Substitui valores nulos por string vazia
- Cria um endpoint `/operadoras` para busca por nome
- Retorna os resultados em formato JSON
- Permite consulta via navegador ou ferramentas como Postman

### Rodar servidor: python -m uvicorn ta:app --reload 
### EndPoint: http://localhost:8000/operadoras?busca

<img width="1456" height="824" alt="image" src="https://github.com/user-attachments/assets/967d4c3a-f7c4-4db5-a7d8-d2dbae83894b" />

