acc_key = '15dee06ae84b849620cf2b423c20bd05'

#pip3 install anticaptchaofficial

from anticaptchaofficial.imagecaptcha import *

solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key(acc_key)

captcha_text = solver.solve_and_return_solution("captcha.png")
if captcha_text != 0:
    print("captcha text "+captcha_text)
else:
    print("task finished with error "+solver.error_code)