

class LinkException(Exception):
    """
    Classe de exceção base, todas as outras exceções deverão derivar desta
    """


class KeyException(LinkException):
    """
    Exception para capturar keys não mapeadas do teclado
    """

    def __init__(self, key: str, key_map: dict) -> None:
        mapeadas = [f'{key}' for key, _ in key_map.items()]
        self.message = f'''Key {key} não mapeada, abaixo seguem as keys atualmente mapeadas:\n
{mapeadas}
        '''
        
        super().__init__(self.message)


class ExecutionException(LinkException):
    """
    Exception para capturar erros de execução
    """

    def __init__(self, message: str) -> None:
        self.message = message

        super().__init__(self.message)


class EmailException(LinkException):
    """
    Exception para capturar erro no envio de email
    """

    def __init__(self, message: str) -> None:
        self.message = message

        super().__init__(self.message)


class AttachmentException(LinkException):
    """
    Exception para capturar erro nos anexos do email
    """

    def __init__(self, message: str) -> None:
        self.message = message

        super().__init__(self.message)


class PathException(LinkException):
    """
    Exception para capturar caso o path do arquivo não exista
    """

    def __init__(self, message: str) -> None:
        self.message = message

        super().__init__(self.message)
