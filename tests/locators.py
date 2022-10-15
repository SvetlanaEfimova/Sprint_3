name = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input[@name = 'name']"  # поле имя

email_registration = "//label[text()='Email']/following-sibling::input"  # поле email

password_registration = "//label[text()='Пароль']/following-sibling::input"  # поле пароль

register_button = "//*[@id='root']/div/main/div/form/button[text() = 'Зарегистрироваться']"  # кнопка регистрации

invalid_password_error = "//*[@id='root']/div/main/div/form/fieldset[3]/div/p[text()]"  #
# ошибка некорректного пароля
login_button = "//*[@id='root']/div/main/section[2]/div/button[text() = 'Войти в аккаунт']"  # кнопка 'Войти в
# аккаунт' на главной странице

sign_in_button = "//*[@id='root']/div/main/div/form/button[text() = 'Войти']"  # кнопка 'Войти' на странице входа

main_page_title = "//h1[text() = 'Соберите бургер']"  # текст на главной странице

personal_account_button = "//a[@href = '/account']"  # кнопка: Личный кабинет

button_in_the_registration_form = "//a[@href = '/login']"  # кнопка: Войти на странице регистрации

button_in_the_registration = "//a[text() = 'Восстановить пароль']"

button_profile = "//a[text() = 'Профиль']"  # кнопка перехода в профиль в личном кабинете

button_constructor = "//p[text() = 'Конструктор']/parent::a"  # кнопка: Конструктор

logo = "//*[@id='root']/div/header/nav/div/a"  # логотип сайта

button_log_out = "//button[text()='Выход']"  # кнопка выхода из аккаунта

bread_section = "//span[text() = 'Булки']"  # раздел Булки

sauces_section = "//span[text() = 'Соусы']"  # раздел Соусы

fillings_section = "//span[text() = 'Начинки']"  # раздел Начинки

bread = "//p[text() = 'Флюоресцентная булка R2-D3']"  # название булки

sauce = "//p[text() = 'Соус Spicy-X']"  # название соуса

filling = "//p[text() = 'Мясо бессмертных моллюсков Protostomia']"  # название начинки

