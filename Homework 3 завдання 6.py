def get_user_age_group():

    users_age_groups = {
        "Олександр": "підліток",
        "Марія": "дорослий",
        "Іван": "дитина",
        "Софія": "підліток",
        "Петро": "дорослий"
    }


    name = input("Введіть ім'я користувача: ").strip()


    age_group = users_age_groups.get(name)

    if age_group:
        print(f"Користувач '{name}' належить до вікової групи: {age_group}.")
    else:
        print(f"Помилка: Користувача з ім'ям '{name}' не знайдено у словнику.")


if __name__ == "__main__":
    get_user_age_group()