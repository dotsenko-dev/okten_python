# ruff: noqa: BLE001
from collections.abc import Iterator

raw_data = """
9d3dc7094d3dcb31ffe2960ad891dd04 34hrap@gmail.com
ec4f2883e9eb74770d02b30f06659a5f tele_nat@mail.i
44ab3c993daee2a9655925d53fbdd7bf telepaev.sn@gmail.com
7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d user123@yahoo.com
a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6 dev_test@gmail.com
f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4 admin@ukr.net
1234567890abcdef1234567890abcdef student_2024@gmail.com
"""

try:
    with open("email.txt", "w") as file:
        file.write(raw_data.strip())
except Exception as e:
    print(f"{e}")


def gen_gmail_only(file_path: str) -> Iterator[str]:
    with open(file_path, "r") as file_in:
        for line in file_in:
            match line.strip().split():
                case [_, email] if email.lower().endswith("gmail.com"):
                    yield email
                case _:
                    pass


try:
    with open("gmail_only.txt", "w") as file_out:
        file_out.writelines(f"{email}\n" for email in gen_gmail_only("email.txt"))
except Exception as e:
    print(f"{e}")
