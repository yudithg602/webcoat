import time, requests, json
from termcolor import colored
import colorama


def eternity_cycle_deep():
    while True:
        input()


def print_col(message, color):
    colorama.init()
    print(colored(message, color))


def AntiCaptcha(site_key, url, key):
    #try:
    if True:
        start = time.time()
        r = requests.post('http://api.anti-captcha.com/createTask', json={"clientKey": key,
                                                                          "task": {"type": "NoCaptchaTaskProxyless",
                                                                                   "websiteURL": url,
                                                                                   "websiteKey": site_key}})
        r = json.loads(r.text)

        taskId = r['taskId']
        for i in range(12):
            time.sleep(10)
            r = requests.post('http://api.anti-captcha.com/getTaskResult', json={"clientKey": key, "taskId": taskId})
            r = json.loads(r.text)
            try:
                if r['status'] == 'ready':
                    delta_time = time.time() - start
                    token = r['solution']['gRecaptchaResponse']

                    print_col(f'Токен найден за {round(delta_time)} сек.', 'magenta')
                    return token
            except Exception:
                pass
        token = None
        return token
    ##except Exception:
      #  print_col('Неверно введен Anticaptcha key или он отсутствует.', 'red')
      #  eternity_cycle_deep()
