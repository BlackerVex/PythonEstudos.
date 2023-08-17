from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        return self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get("Vencimento", None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs["vencimento"] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        try:
            # Possível IndexError
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao == descricao][0]
        except IndexError as e:
            raise TarefaNaoEncontrada(str(e))

    def __str__(self):
        return f"{self.nome} ({len(self.pendentes())}) tarefas(s) pendente(s)"


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append("(Concluída)")
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append("(Vencida)")
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f"(Vence em {dias} dias)")

        return f"{self.descricao} " + " ".join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto("Tarefas de Casa")
    casa += TarefaRecorrente("Passar Roupa",
                             datetime.now() + timedelta(days=1, minutes=2))
    casa.add(TarefaRecorrente("Lavar Prato",
             datetime.now() + timedelta(days=3, minutes=12)))
    casa.add("Passar Pano", datetime.now() + timedelta(days=1, minutes=1))
    casa.add(TarefaRecorrente("Trocar lençois", datetime.now(), 7))
    casa.add(casa.procurar("Trocar lençois").concluir())

    mercado = Projeto("Compras do Mercado")
    mercado.add(TarefaRecorrente("Frutas secas",
                datetime.now() + timedelta(days=3)))
    mercado.add("Carne")
    mercado.add(TarefaRecorrente("Tomate", datetime.now() + timedelta(days=3)))

    print("Compras do Mercado")
    comprar_carne = mercado.procurar("Carne")
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f"- {tarefa}")
    print(mercado)
    print(" ")
    print("Tarefas de Casa")

    try:
        casa.procurar("Lavar Prato - ERRO").concluir()
    except TarefaNaoEncontrada as e:
        print(f'A causa foi "{str(e)}"!')
    finally:
        print("Item não encontrado")
    
    
    casa.procurar("Passar Pano").concluir()
    for tarefa in casa:
        print(f"- {tarefa}")
    print(casa)


if __name__ == "__main__":
    main()
