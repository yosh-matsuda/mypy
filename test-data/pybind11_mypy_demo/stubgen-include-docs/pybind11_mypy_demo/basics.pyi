from typing import ClassVar

from typing import overload
PI: float

class Point:
    class AngleUnit:
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        degree: ClassVar[Point.AngleUnit] = ...
        radian: ClassVar[Point.AngleUnit] = ...
        def __init__(self, value: int) -> None:
            """__init__(self: pybind11_mypy_demo.basics.Point.AngleUnit, value: int) -> None"""
        def __eq__(self, other: object) -> bool:
            """__eq__(self: object, other: object) -> bool"""
        def __getstate__(self) -> int:
            """__getstate__(self: object) -> int"""
        def __hash__(self) -> int:
            """__hash__(self: object) -> int"""
        def __index__(self) -> int:
            """__index__(self: pybind11_mypy_demo.basics.Point.AngleUnit) -> int"""
        def __int__(self) -> int:
            """__int__(self: pybind11_mypy_demo.basics.Point.AngleUnit) -> int"""
        def __ne__(self, other: object) -> bool:
            """__ne__(self: object, other: object) -> bool"""
        def __setstate__(self, state: int) -> None:
            """__setstate__(self: pybind11_mypy_demo.basics.Point.AngleUnit, state: int) -> None"""
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...

    class LengthUnit:
        __members__: ClassVar[dict] = ...  # read-only
        __entries: ClassVar[dict] = ...
        inch: ClassVar[Point.LengthUnit] = ...
        mm: ClassVar[Point.LengthUnit] = ...
        pixel: ClassVar[Point.LengthUnit] = ...
        def __init__(self, value: int) -> None:
            """__init__(self: pybind11_mypy_demo.basics.Point.LengthUnit, value: int) -> None"""
        def __eq__(self, other: object) -> bool:
            """__eq__(self: object, other: object) -> bool"""
        def __getstate__(self) -> int:
            """__getstate__(self: object) -> int"""
        def __hash__(self) -> int:
            """__hash__(self: object) -> int"""
        def __index__(self) -> int:
            """__index__(self: pybind11_mypy_demo.basics.Point.LengthUnit) -> int"""
        def __int__(self) -> int:
            """__int__(self: pybind11_mypy_demo.basics.Point.LengthUnit) -> int"""
        def __ne__(self, other: object) -> bool:
            """__ne__(self: object, other: object) -> bool"""
        def __setstate__(self, state: int) -> None:
            """__setstate__(self: pybind11_mypy_demo.basics.Point.LengthUnit, state: int) -> None"""
        @property
        def name(self) -> str: ...
        @property
        def value(self) -> int: ...
    angle_unit: ClassVar[Point.AngleUnit] = ...
    length_unit: ClassVar[Point.LengthUnit] = ...
    x_axis: ClassVar[Point] = ...  # read-only
    y_axis: ClassVar[Point] = ...  # read-only
    origin: ClassVar[Point] = ...
    x: float
    y: float
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.
        
        1. __init__(self: pybind11_mypy_demo.basics.Point) -> None
        
        2. __init__(self: pybind11_mypy_demo.basics.Point, x: float, y: float) -> None"""
    @overload
    def __init__(self, x: float, y: float) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.
        
        1. __init__(self: pybind11_mypy_demo.basics.Point) -> None
        
        2. __init__(self: pybind11_mypy_demo.basics.Point, x: float, y: float) -> None"""
    @overload
    def distance_to(self, x: float, y: float) -> float:
        """distance_to(*args, **kwargs)
        Overloaded function.
        
        1. distance_to(self: pybind11_mypy_demo.basics.Point, x: float, y: float) -> float
        
        2. distance_to(self: pybind11_mypy_demo.basics.Point, other: pybind11_mypy_demo.basics.Point) -> float"""
    @overload
    def distance_to(self, other: Point) -> float:
        """distance_to(*args, **kwargs)
        Overloaded function.
        
        1. distance_to(self: pybind11_mypy_demo.basics.Point, x: float, y: float) -> float
        
        2. distance_to(self: pybind11_mypy_demo.basics.Point, other: pybind11_mypy_demo.basics.Point) -> float"""
    @property
    def length(self) -> float: ...

def answer() -> int:
    '''answer() -> int
    
    answer docstring, with end quote"'''
def midpoint(left: float, right: float) -> float:
    """midpoint(left: float, right: float) -> float"""
def sum(arg0: int, arg1: int) -> int:
    '''sum(arg0: int, arg1: int) -> int
    
    multiline docstring test, edge case quotes """\'\'\''''
def weighted_midpoint(left: float, right: float, alpha: float = ...) -> float:
    """weighted_midpoint(left: float, right: float, alpha: float = 0.5) -> float"""
