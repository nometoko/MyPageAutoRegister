import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mypage_utils import (
    click_input_by_label_text,
    click_label_by_text,
    complete_form,
    go_next,
    select_dropdown_by_value,
)

brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
json_path = "./myProfile.json"
f_json = open(json_path)

options = Options()
options.binary_location = brave_path
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

url = sys.argv[1]
driver.get(url)

# 新規登録
sign_up_button = wait.until(EC.presence_of_element_located((By.ID, "first_access")))
sign_up_button.click()

# 同意
accept_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "同意する")))
accept_button.click()

# mypage 1
json = json.load(f_json)

myProfile = json["MyProfile"]
complete_form(driver, wait, myProfile)

go_next(wait)

if "GraduateSchool" in json:
    grad_school_info = json["GraduateSchool"]
    checkbox_contents = grad_school_info["CheckBox"]
    check_by_text = checkbox_contents["ByText"]

    # mypage 2
    click_label_by_text(wait, check_by_text["SchoolClassification"])
    click_label_by_text(wait, check_by_text["initial"])
    click_label_by_text(wait, check_by_text["location"])
    go_next(wait)

    # mypage 3
    click_label_by_text(wait, check_by_text["name"])
    go_next(wait)

    # mypage 4
    click_input_by_label_text(wait, check_by_text["faculty"])
    go_next(wait)

    # mypage 5
    click_input_by_label_text(wait, check_by_text["MajorClassification"])
    go_next(wait)

# mypage 6
if "University" in json:
    univ_info = json["University"]
    checkbox_contents = univ_info["CheckBox"]
    check_by_text = checkbox_contents["ByText"]

    click_label_by_text(wait, check_by_text["classification"])
    click_label_by_text(wait, check_by_text["initial"])
    click_label_by_text(wait, check_by_text["location"])
    go_next(wait)

    # mypage 7
    click_label_by_text(wait, check_by_text["name"])
    go_next(wait)

    # mypage 8
    click_input_by_label_text(wait, check_by_text["faculty"])
    go_next(wait)

    # mypage 9
    click_input_by_label_text(wait, check_by_text["department"])

    select_content = univ_info["Select"]
    select_by_value = select_content["ByValue"]

    for key, value in select_by_value.items():
        select_dropdown_by_value(driver, wait, key, value)

    go_next(wait)

# アンケート
# title_element = wait.until(
#     (EC.presence_of_element_located((By.CSS_SELECTOR, "h3.heading_l1")))
# )
# title_text = title_element.text.strip()
# print(title_text)
#
# if title_text == "アンケート":
#     questionnaire = json["Questionnaire"]
#     complete_form(driver, wait, questionnaire)
