from sqlalchemy import Column, Integer, String, Boolean
from src.infra.sqlalchemy.config.database import Base 


class Produto(Base):

    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhe = Column(String)
    preco = Column(Integer)
    disponivel = Column(Boolean)
