import pathlib
from dataclasses import dataclass, field
from typing import Optional

from nameparser import HumanName


@dataclass
class Course:
    id: int
    name: str
    course_code: str
    term: str
    alias: Optional[str] = None


@dataclass
class GroupSet:
    id: int
    name: str


@dataclass
class Group:
    id: int
    name: str


@dataclass
class Student:
    id: int
    name: str
    sortable_name: Optional[str] = None
    first_name: str = field(init=False)
    last_name: str = field(init=False)
    notes: Optional[str] = None
    photo: Optional[pathlib.Path] = None

    def __post_init__(self):
        # Parse human names, allowing for underscores to group parts of the name
        name = HumanName(self.name)
        self.first_name = " ".join([name.first, name.middle]).rstrip()
        self.last_name = name.last.replace("_", " ")
        self.name = self.name.replace("_", " ")


@dataclass
class Section:
    id: int
    name: str
    students: list[Student]


@dataclass
class StudentGroup:
    name: str = ""
    students: list[Student] = field(default_factory=list)


@dataclass
class GroupList:
    name: str = ""
    groups: list[StudentGroup] = field(default_factory=list)
