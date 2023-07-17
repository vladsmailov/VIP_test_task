import abc


class AbstractRepository(abc.ABC):
    """Абстрактный класс, для реализации паттерна Repository."""

    def __init__(self, session, model) -> None:
        self._session = session
        self._model = model
