import time
import urllib.request
from anticaptchaofficial.imagecaptcha import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import email.message
import imaplib
import default_functions

def yandex_registration(idx):
    login = 'letintrigy' + idx
    name = 'Alex'
    surname = 'Nevskyi'
    password = 'parolnesloshniy12345A!@'
    secret_ans = 'thisisnotsecretanswer'

    #driver = webdriver.Chrome('C:\\chromedriver.exe')
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    driver.get('https://passport.yandex.ru/auth?mode=add-user')
    time.sleep(5)
    search_box = driver.find_elements_by_tag_name('a')[4]
    search_box.click()
    search_box = driver.find_elements_by_class_name('Textinput-Control')
    search_box[0].send_keys(name)
    search_box[1].send_keys(surname)
    search_box[3].send_keys(login)
    search_box[4].send_keys(password)
    search_box[5].send_keys(password)
    time.sleep(1)
    x = driver.find_elements_by_tag_name('span')[20]
    x.click()
    time.sleep(5)
    search_box = driver.find_elements_by_class_name('Textinput-Control')
    search_box[6].send_keys(secret_ans)
    img_link = driver.find_elements_by_tag_name('img')[-1]
    src = img_link.get_attribute('src')
    urllib.request.urlretrieve(src, "captcha.png")
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key("bc78856197a34979b57c6f89d85f2c6a")
    captcha_text = solver.solve_and_return_solution("captcha.png")
    if captcha_text != 0:
        captcha_text = captcha_text
    else:
        driver.close()
        yandex_registration(idx)
        return 0

    search_box[7].send_keys(captcha_text)
    time.sleep(1)
    driver.find_elements_by_tag_name('button')[-1].click()
    time.sleep(3)
    driver.get('https://mail.yandex.ru/?uid=#setup/client')
    time.sleep(5)
    try:
        search_box = driver.find_elements_by_tag_name('span')[59]
    except Exception:
        print("CAPTCHA NOT RIGHT SOLVE!")
        exit(0)
    search_box.click()
    search_box = driver.find_elements_by_tag_name('span')[72]
    search_box.click()
    search_box = driver.find_elements_by_tag_name('span')[116]
    search_box.click()
    driver.quit()
    return 0


def instagram_registration(idx):
    login = 'letintrigy' + idx
    name = 'Alex'
    surname = 'Nevskyi'
    password = 'parolnesloshniy12345A!@'
    secret_ans = 'thisisnotsecretanswer'
    dd, mm, yyyy = '13', '1', '2001'
    driver = webdriver.Chrome('C:\\chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get('https://www.instagram.com/accounts/emailsignup/?hl=ru')
    time.sleep(5)  # Let the user actually see something!
    search_box = driver.find_elements_by_tag_name('input')
    search_box[0].send_keys(login + '@ya.ru')
    search_box[1].send_keys(name + ' ' + surname)
    search_box[2].send_keys(login.replace('-', ''))
    search_box[3].send_keys(password)
    search_box = driver.find_elements_by_tag_name('button')
    search_box[-1].click()
    time.sleep(5)
    select = Select(driver.find_elements_by_tag_name('select')[0])
    select.select_by_value(mm)
    select = Select(driver.find_elements_by_tag_name('select')[1])
    select.select_by_value(dd)
    select = Select(driver.find_elements_by_tag_name('select')[2])
    select.select_by_value(yyyy)
    search_box = driver.find_elements_by_tag_name('button')[-2]
    search_box.click()
    while True:
        time.sleep(60)
        message = get_mail_main(idx)
        if message != 0:
            break#https://www.instagram.com/accounts/emailsignup/?hl=ru
    print(message)

    search_box = driver.find_elements_by_tag_name('input')[-1]
    search_box.send_keys(message)
    search_box = driver.find_elements_by_tag_name('button')[-2]
    search_box.click()
    time.sleep(10)
    if 'challenge' in driver.current_url:
        captcha = default_functions.AntiCaptcha('6LebnxwUAAAAAGm3yH06pfqQtcMH0AYDwlsXnh-u', driver.current_url, 'bc78856197a34979b57c6f89d85f2c6a')



def get_mostnew_email(messages):
    ids = messages[0]
    id_list = ids.split()
    latest_ten_email_id = id_list[-5:]
    keys = map(int, latest_ten_email_id)
    news_keys = sorted(keys, reverse=True)
    str_keys = [str(e) for e in news_keys]
    return str_keys


def get_mail_main(idx):
    try:
        M = imaplib.IMAP4_SSL('imap.yandex.ru')
        user = f'letintrigy{idx}@ya.ru'
        password = 'parolnesloshniy12345A!@'
        M.login(user, password)
        M.select("INBOX")
        (retcode, messages) =M.search(None, 'ALL')
        news_mail = get_mostnew_email(messages)
        for i in news_mail:
            data = M.fetch(i, '(RFC822)')
            msg = email.message_from_bytes(data[1][0][1])
            return (msg['Subject'].split()[0])
    except Exception:
        return 0


def main():
    idx = '5557'
    yandex_registration(idx)
    instagram_registration(idx)

main()
