import string
import random

str1 = string.ascii_letters + string.digits
str = "验证码：" + ''.join(random.sample(str1, 6))
print(str)