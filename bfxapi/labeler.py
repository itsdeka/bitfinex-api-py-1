from .exceptions import LabelerSerializerException

from typing import Generic, TypeVar, Iterable, Optional, List, Tuple, Any, cast, Dict, Union

from types import SimpleNamespace

T = TypeVar("T")

class _Serializer(Generic[T]):
    def __init__(self, name: str, labels: List[str], IGNORE: List[str] = [ "_PLACEHOLDER" ]):
        self.name, self.__labels, self.__IGNORE = name, labels, IGNORE

    def _serialize(self, *args: Any, skip: Optional[List[str]] = None) -> Union[Dict, List[Dict]]:
        labels = list(filter(lambda label: label not in (skip or list()), self.__labels))

        if type(args[0]) == list:
            response = []

            for sub_args in args:
                sub_response = {}

                if len(labels) > len(sub_args):
                    raise LabelerSerializerException("<labels> and <*args> arguments should contain the same amount of elements.")

                for index, label in enumerate(labels):
                    if label not in self.__IGNORE:
                        sub_response[label] = sub_args[index]

                response.append(sub_response)
        else:
            response = {}

            if len(labels) > len(args):
                raise LabelerSerializerException("<labels> and <*args> arguments should contain the same amount of elements.")

            for index, label in enumerate(labels):
                if label not in self.__IGNORE:
                    response[label] = args[index]

        return response

    def parse(self, *values: Any, skip: Optional[List[str]] = None) -> T:
        serialized_values = self._serialize(*values, skip=skip)

        if type(serialized_values) == list:
            return [ cast(T, SimpleNamespace(**value)) for value in serialized_values ]
        else:
            return cast(T, SimpleNamespace(**serialized_values))
