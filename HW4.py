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
    with open("email.txt", mode="w") as file:
        file.write(raw_data.strip())
except Exception as e:
    print(f"Помилка створення початкового файлу: {e}")


# try:
#     with (
#         open("email.txt", mode="r") as file_in,
#         open("gmail.txt", mode="w") as file_out,
#     ):
#         for line in file_in:
#             parts = line.strip().split()
#             email = parts[1].lower()
#             if email.endswith("gmail.com"):
#                 file_out.write(email + "\n")
# except Exception as e:
#     print(f"Помилка при обробці файлу: {e}")

# from collections.abc import Generator


# def gmail_only_gen(file_path: str) -> Generator[str, None, None]:
#     with open(file_path, mode="r") as file:
#         for line in file:
#             parts = line.strip().split()
#             if len(parts) == 2 and parts[1].lower().endswith("gmail.com"):
#                 yield parts[1]


# try:
#     with open("gmail_only.txt", mode="w") as file_out:
#         file_out.writelines(f"{email}\n" for email in gmail_only_gen("email.txt"))
#         # for email in gmail_only_gen("email.txt"):
#         #     file_out.write(f"{email}\n")
#         print("alles gut")
# except Exception as e:
#     print(f"Помилка: {e}")


try:
    with (
        open("email.txt", "r") as file_in,
        open("gmail.txt", "w") as file_out,
    ):
        for line in file_in:
            match line.strip().split():
                case [hash, email] if email.lower().endswith("gmail.com"):
                    file_out.write(email + "\n")
                case _:
                    pass
    print("alles gut")
except Exception as e:
    print(f"Fehler: {e}")
