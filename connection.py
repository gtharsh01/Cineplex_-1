import pymysql


def Connect():
    conn = pymysql.connect(
        host='localhost',  # 127.0.0.1
        user='root',
        password='system',
        #database='project_aug',
        #port=3308
        port=3306,
        database='project_aug'
    )
    print("successfull")
    return conn



def verifyMobile(mobile):
    if len(mobile) == 10 and str(mobile).isdigit() and mobile[0] in '9876':
        return True
    else:
        return False


def verifyEmail(mail):
    if '@' in mail and '.' in mail:
        return True
    else:
        return False
