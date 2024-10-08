#!/usr/bin/env python3
"""This module implements a type-annotated function"""
from typing import Any, Sequence, Union, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]
                     ) -> Union[Any, T]:
    """Safely gets a value from a dictionary with a default if
    key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
