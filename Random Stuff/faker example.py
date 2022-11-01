# faker example

from random import randint
from faker import Faker

Faker.seed(1)
fake = Faker("en_GB")

[
    print(
        f"{fake.name()} {fake.date_between('-70y','-18y')} {fake.email()} {'07'+''.join([str(randint(0,9)) for j in range(9)])} {fake.date_between('-5M','+5M')}"
    )
    for i in range(5)
]
