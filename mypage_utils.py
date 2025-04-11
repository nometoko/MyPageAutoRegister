from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver


def go_next(wait: WebDriverWait):
    next_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "次へ")))
    next_button.click()
    return None


def click_checkbox_by_id(wait: WebDriverWait, id, enable=True):
    try:
        checkbox = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//label[@for="{id}"]'))
        )
        if checkbox.is_selected() != enable:
            checkbox.click()
    except TimeoutException:
        print(f"error in checkbox by id: {id}")


def click_label_by_text(wait: WebDriverWait, text, enable=True):
    try:
        checkbox = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f'//label[contains(text(), "{text}")]')
            )
        )
        if checkbox.is_selected() != enable:
            checkbox.click()
    except TimeoutException:
        print(f"error in checkbox by text: {text}")


def click_input_by_label_text(wait: WebDriverWait, text, enable=True):
    """
    input が labelと並列に <li>の中にある場合のみ有効
    """
    try:
        checkbox = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//li[label[contains(text(), '{text}')]]/input")
            )
        )
        if checkbox.is_selected() != enable:
            checkbox.click()
    except TimeoutException:
        print(f"error in send text\n\ttext: {text}")


def send_text(wait: WebDriverWait, key, value):
    try:
        textbox = wait.until(EC.presence_of_element_located((By.NAME, key)))
        textbox.send_keys(value)
    except TimeoutException:
        print(f"error in send text\n\tkey: {key}\n\tvalue: {value}")


def select_dropdown_by_value(driver: WebDriver, wait: WebDriverWait, key, value):
    try:
        select = wait.until(EC.presence_of_element_located((By.ID, key)))
        driver.execute_script(
            """
            const select = arguments[0];
            const value = arguments[1];
            select.value = value;
            select.dispatchEvent(new Event('change', { bubbles: true }));
            """,
            select,
            value,
        )
        select = wait.until(EC.presence_of_element_located((By.NAME, key)))

    except TimeoutException:
        print(f"error in select by value:\n\tkey: {key}\n\tvalue: {value}")


def select_dropdown_by_text(driver: WebDriver, wait: WebDriverWait, key, value):
    try:
        select = wait.until(EC.presence_of_element_located((By.ID, key)))
        driver.execute_script(
            """
            const select = arguments[0];
            const visibleText = arguments[1];
            for (let option of select.options) {
                if (option.text === visibleText) {
                    select.value = option.value;
                    select.dispatchEvent(new Event('change', { bubbles: true }));
                    break;
                }
            }
            """,
            select,
            value,
        )

    except TimeoutException:
        print(f"error in select by text:\n\tkey: {key}\n\tvalue: {value}")


def complete_select_dropdown(driver: WebDriver, wait: WebDriverWait, data: dict):
    for data_key, data_value in data.items():
        formbox = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f'//dt[contains(., "{data_key}")]/following-sibling::dd[contains(@class, "formbox02)"]',
                )
            )
        )
        select_by_value = data_value["ByValue"]
        select_by_text = data_value["ByText"]

        for key, value in select_by_value.items():
            select_dropdown_by_value(driver, wait, key, value)


def complete_form(driver: WebDriver, wait: WebDriverWait, data):
    text_contents = data["Text"]
    for key, value in text_contents.items():
        send_text(wait, key, value)

    checkbox_contents = data["CheckBox"]

    check_by_id = checkbox_contents["ById"]
    for key, value in check_by_id.items():
        click_checkbox_by_id(wait, key, value)
    check_by_text = checkbox_contents["ByText"]
    for key, value in check_by_text.items():
        click_label_by_text(wait, value)

    select_content = data["Select"]
    select_by_value = select_content["ByValue"]
    for key, value in select_by_value.items():
        select_dropdown_by_value(driver, wait, key, value)
    select_by_text = select_content["ByText"]
    for key, value in select_by_text.items():
        select_dropdown_by_text(driver, wait, key, value)
