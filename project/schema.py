from dataclasses import dataclass
from typing import Union
import marshmallow_dataclass


@dataclass
class Requests:
    cmd1: str
    value1: Union[str, int]
    cmd2: str
    value2: Union[str, int]


RequestsSchema = marshmallow_dataclass.class_schema(Requests)  # type: ignore
