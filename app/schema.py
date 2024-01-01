from typing import List, Optional
from datetime import datetime, date
from enum import Enum
from typing_extensions import Annotated
from pydantic import BaseModel, Field, EmailStr, BeforeValidator


PyObjectId = Annotated[str, BeforeValidator(str)]


class Education(BaseModel):
    college_name: str = Field(...)
    major: str = Field(...)
    graduation_year: int = Field(...)


class AboutMe(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    age: int = Field(...)
    profession: str = Field(...)
    description: str = Field(...)
    language: List[str] = Field(...)
    location: str = Field(...)
    education: Education = Field(...)
    email_id: EmailStr = Field(...)
    last_updated: datetime = Field(...)


class Certificate(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(...)
    description: str = Field(...)
    completion_date: date = Field(...)
    provider: str = Field(...)
    tags: List[str] = Field(...)
    verify_link: str = Field(...)


class Certificates(BaseModel):
    certificates: List[Certificate]


class LeetCode(BaseModel):
    rank: int = Field(...)
    easy: int = Field(...)
    medium: int = Field(...)
    hard: int = Field(...)
    link: str = Field(...)


class CodeWars(BaseModel):
    link: str = Field(...)


class CodeRank(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    leetcode: LeetCode = Field(...)
    codewars: CodeWars = Field(...)


class Experience(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(...)
    company: str = Field(...)
    description: str = Field(...)
    technologies_used: List[str] = Field(...)
    duration: str = Field(...)
    link: str = Field(...)


class Experiences(BaseModel):
    experiences: List[Experience]


class ProjectStatus(Enum):
    ON_GOING = "on_going"
    COMPLETED = "completed"
    PROTOTYPE = "prototype"


class Project(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(...)
    description: str = Field(...)
    screenshots: List[str] = Field(...)
    status: ProjectStatus = Field(...)
    link: str = Field(...)
    tags: List[str] = Field(...)


class Projects(BaseModel):
    projects: List[Project]


class Skills(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    programming_languages: List[str] = Field(...)
    frameworks_or_libraries: List[str] = Field(...)


class Social(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    link: str = Field(...)
    description: str = Field(...)


class Socials(BaseModel):
    socials: List[Social]


class Typing(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    highest_wpm: int = Field(...)
    avg_wpm: int = Field(...)
    link: str = Field(...)


class Typings(BaseModel):
    typing: List[Typing]


class Banner(BaseModel):
    banner_mobile: str = Field(...)
    banner_pc: str = Field(...)
