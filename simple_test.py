import allure
from selene.support import by
from selene.support.conditions import be, have
from selene import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity

@allure.severity(Severity.CRITICAL)
def test_github_selene():
    browser.open("https://github.com")
    s('.js-site-search-focus').click()
    s('.js-site-search-focus').send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()
    browser.all('#issue_81_link').element_by(have.exact_text('issue_to_test_allure_report'))

def test_dynamic_steps():

    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозитория"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем название Issue с номером 81"):
        browser.all('#issue_81_link').element_by(have.exact_text('issue_to_test_allure_report'))


def test_decorator_steps():
    allure.dynamic.tag("web тест проверка названиея issue")
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#81")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()

@allure.severity(Severity.CRITICAL)
@allure.step("Проверяем название Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.all(f'#issue_{number}_link').element_by(have.exact_text('issue_to_test_allure_report'))
