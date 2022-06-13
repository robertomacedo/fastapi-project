from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    my_produtos: List[Produto]
    my_vendas: List[Pedido]
    my_pedidos: List[Pedido]


class Produto(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    nome: str
    detalhe: str
    preco: float
    disponivel: bool = False


class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    local: str
    obs: Optional[str] = 'Sem observações'
