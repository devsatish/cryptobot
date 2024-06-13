from api.rest import Rest
from typing import Self

class AbstractModel(Rest):
    resource_name = ''

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def clone(self: Self) -> Self:
        """Creates a clone of the current instance."""
        return self.__class__(**self.__dict__)

    def handle_exceptions(self) -> None:
        try:
            # Some code that might raise multiple exceptions
            pass
        except* (ValueError, TypeError) as e:
            print(f"Handled exceptions: {e}")