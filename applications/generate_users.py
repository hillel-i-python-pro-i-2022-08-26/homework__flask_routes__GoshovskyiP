import random
from typing import NamedTuple, Iterator

from faker import Faker

fake = Faker()


class User(NamedTuple):
    name: str
    age: int


def generate_user() -> User:
    return User(name=fake.name(), age=random.randint(10, 100))


def generate_users(amount: int = 100) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
