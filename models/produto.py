class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
            return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    def formata_moeda_str_float(self: object, valor: float) -> str:
        return f'R$ {valor:,.2f}'

    def __str__(self) -> str:
        return f' Código {self.__codigo};\n Nome {self.__nome};\n Preço {self.formata_moeda_str_float(self.__preco)}'
