import random

NAME = "Верховний Генерал Качковський"
STYLE = "смішний"

GREETINGS = [
    "Привіт-привіт! Мені приємно!",
    "Нарешті ти тута братанчик, без розмови було скучнооо.",
    "Вітаю! Допомога вже до тебе летить.",
]

MOTIVATION = [
    "Кожна качка колись була людиною. Ти вже на шляху",
    "Помилка — це не провал, а підказка. Спробуй ще раз",
    "Маленький крок щодня — і за місяць ти побачиш у собі качку Pro.",
]

JOKES = [
    "Баг — це не помилка, а фішка!",
    "Заходить качка в аптеку і питає: «У вас є бальзам для губ? Тільки запишіть на мій дзьоб».",
]

ADVICE = [
    "Не відкладай на завтра те, що можна закрякати сьогодні!",
    "Якщо код не працює — випий водички, покрякай і перевір відступи.",
]

SONGS = [
    "Кря-кря-кря, капрали качки йдуть у бій! 🦆🎵",
    "Увімкни щось енергійне, щоб аж пір'я дибом стало!",
]

MOVIES = [
    "Раджу подивитися «Качині історії» — класика для справжніх фанатів генералів!",
    "Глянь «Шрек» або «Кунг-фу Панда», там гумор на висоті.",
]


def get_response(user_text):
    text = user_text.lower()

    if "привіт друже" in text:
        return random.choice(GREETINGS)
    elif "шо ти голова?" in text:
        return "Займаюся важливими справами. А в тебе як?"
    elif "мотивуй мене" in text:
        return random.choice(MOTIVATION)
    elif "розсміши мене" in text:
        return random.choice(JOKES)
    elif "порада" in text:
        return random.choice(ADVICE)
    elif "пісня" in text:
        return random.choice(SONGS)
    elif "кіно" in text:
        return random.choice(MOVIES)
    else:
        return "Такої фігні я ще не чув, але завдяки твоїм словам я щось вивчу!"


def main():
    print(f"{NAME}: Привіт! Я твій {STYLE} помічник.")
    print("(напиши «вихід», щоб завершити)")

    while True:
        user_text = input("Ти: ").lower()

        if user_text == "вихід":
            print(f"{NAME}: Бувай друже!")
            break

        print(f"{NAME}: {get_response(user_text)}")


if __name__ == "__main__":
    main()
