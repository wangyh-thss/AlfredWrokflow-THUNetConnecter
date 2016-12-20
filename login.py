#! encoding=utf-8

import requests
import hashlib
import time
import sys


USER_NAME = ''
PASSWORD = ''
url = 'http://net.tsinghua.edu.cn/do_login.php'

def try_login():
    try:
        m = hashlib.md5()
        m.update(PASSWORD)
        post_data = {
            'action': 'login',
            'username': USER_NAME,
            'password': '{MD5_HEX}' + m.hexdigest(),
            'ac_id': 1
        }
        res = requests.post(url, post_data)
        return res.content
    except:
        return None

def main():
    for try_times in xrange(1, 10):
        res = try_login()
        if res is not None and 'successful' in res:
            print res
            sys.exit()
        else:
            time.sleep(1);
    print 'Login failed'

if __name__ == '__main__':
    main()

