
from dataclasses import dataclass
import datetime
from enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    current_address: str
    permanent_address: str
    gender: Gender
    phone_number: str
    birth_date: datetime.date
    subject: str
    hobby: Hobby
    file: str
    state: str
    city: str


student = User(
    first_name='Johann',
    last_name='Bach',
    email='Johann@Bach.com',
    current_address='Sophienstraße 41, 99817 Eisenach, Germany',
    permanent_address='Earth',
    gender=Gender.male.value,
    phone_number='4931031680',
    birth_date=datetime.date(1900, 1, 18),
    subject='Arts',
    hobby=Hobby.music.value,
    file='organ.jpeg',
    state='NCR',
    city='Delhi'
)

admin = User(
    first_name='Admin Johann',
    last_name='Admin Bach',
    email='adminJohann@Bach.com',
    current_address='Admin Sophienstraße 41, 99817 Eisenach, Germany',
    permanent_address='AdminEarth',
    gender=Gender.male.value,
    phone_number='4931031680',
    birth_date=datetime.date(1900, 1, 1),
    subject='Arts',
    hobby=Hobby.music.value,
    file='organ.jpeg',
    state='NCR',
    city='Delhi'
)
