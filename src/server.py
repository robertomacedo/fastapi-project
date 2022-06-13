from fastapi import FastAPI, Depends 
from src.schemas.schems import Produto
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorio.repo_produto import RepoProduto


criar_bd()

app = FastAPI()


@app.post('/produtos')
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepoProduto().criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos():
    return {"Msg": "Listagem de produtos"}
