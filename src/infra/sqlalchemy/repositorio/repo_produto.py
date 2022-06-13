from sqlalchemy.orm import Session 
from src.schemas import schems
from src.infra.sqlalchemy.models import models

class RepoProduto():
    def __init__(self, db: Session):
        self.db = db


    def criar(self, produto: schems.Produto):
        db_produto = models.Produto(nome=produto.nome,
                                    detalhe=produto.detalhe,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel)
        self.db.add(db_produto) 
        self.db.commint()
        self.db.refresh(db_produto)
        return db_produto


    def lestar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos


    def obter(self):
        pass 


    def remover(self):
        pass
