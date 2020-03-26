#coding:utf-8

from trans_pro import tranEn2Cn


if __name__ == '__main__':
    with open('msg_en.txt', 'r+', encoding='utf-8') as f:
        msg_en_items = f.readlines()
        f.close()
    i = 0 
    with open('msg_cn.txt', 'w+', encoding='utf-8') as f2:
        for x in msg_en_items:
            i += 1
            if not x:
                continue
            _msg = tranEn2Cn(x)
            cn_msg = str(_msg) if _msg else '-'
            f2.write(cn_msg + '\n')
            print( '[{}] '.format(str(i)) +  cn_msg)
        f2.close()
    print('--ok')
