#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 12:26
# @Author  : taojian
# @Site    : 
# @File    : test1_get_AccessToken.py
# @Software: PyCharm


import unittest,time,json
from Base.runmethod import RunMethod
from Common.AES_CBC_PKCS5 import encrypt,decrypt
from Common.hmacmd5 import hmac_md5
from Common.Html_miaoshu import miaoshu

class Test_get_AccessToken(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.host='http://123.157.219.74:8090/evcs/v1/'
        cls.headers={
            "Content-Type": "application/json; charset=utf-8"}
        cls.times = time.strftime("%Y%m%d%H%M%S", time.localtime())
        cls.DataSecret = 'bed30540c54dda5d'
        cls.SigSecret = 'a77b249029c22ee5'
        cls.text = '{"OperatorID":"MA35PU38X","OperatorSecret":"08083ebe79bc48a9"}'
        cls.encrypt_data = encrypt(cls.DataSecret, cls.text)
        cls.sig = hmac_md5(cls.SigSecret, "MA35PU38X" + cls.encrypt_data + cls.times + "0001")


    def test1_alldata_right(self):
        '''
        检验所有参数正确
        :return:
        '''

        host=self.host
        lujing='query_token'
        data={"OperatorID":"MA35PU38X",
              "Data":"{}".format(self.encrypt_data),
              "TimeStamp":"{}".format(self.times),
              "Seq":"0001",
              "Sig":"{}".format(self.sig)}
        headers=self.headers
        res=RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{'Ret': 0, 'Msg': '请求成功'}", respons=res)
        self.assertTrue(res['Ret'] == 0, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "请求成功", msg="返回msg不正确")

    def test2_sig_error(self):
        '''
        检验签名错误
        :return:
        '''

        host = self.host
        lujing = 'query_token'
        data = {"OperatorID": "MA35PU38X",
                "Data": "{}".format(self.encrypt_data),
                "TimeStamp": "20190619133716",
                "Seq": "0001",
                "Sig": "{}".format(self.sig)}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{'Ret': 4001, 'Msg': '签名错误'}", respons=res)
        self.assertTrue(res['Ret'] == 4001, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "签名错误", msg="返回msg不正确")

    def test3_dataMiSS_OperatorID(self):
        '''
        检验post参数不合法,缺少必须参数OperatorID
        :return:
        '''
        host = self.host
        lujing = 'query_token'
        data = {
                "Data": "{}".format(self.encrypt_data),
                "TimeStamp": "{}".format(self.times),
                "Seq": "0001",
                "Sig": "{}".format(self.sig)}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{'Ret': 4003 'Msg': 'POST参数不合法,缺少必须的示例'}",
                respons=res)
        self.assertTrue(res['Ret'] == 4003, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "POST参数不合法,缺少必须的示例", msg="返回msg不正确")
    def test4_dataMiSS_Data(self):
        '''
        检验post参数不合法,缺少必须参数Data
        :return:
        '''

        host = self.host
        lujing = 'query_token'
        data = {"OperatorID": "MA35PU38X",
                "TimeStamp": "{}".format(self.times),
                "Seg": "0001",
                "Sig": "{}".format(self.sig)}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{'Ret': 4003 'Msg': 'POST参数不合法,缺少必须的示例'}", respons=res)
        self.assertTrue(res['Ret'] == 4003, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "POST参数不合法,缺少必须的示例")

    def test5_dataMiSS_TimeStamp(self):
        '''
        检验post参数不合法,缺少必须参数TimeStamp
        :return:
        '''
        encrypt_data = encrypt(self.DataSecret, self.text)
        sig = hmac_md5(self.SigSecret, "MA35PU38X" + encrypt_data + self.times + "0001")
        host = self.host
        lujing = 'query_token'
        data = {"OperatorID": "MA35PU38X",
                "Data": "{}".format(encrypt_data),
                "Seq": "0001",
                "Sig": "{}".format(sig)}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{'Ret': 4003 'Msg': 'POST参数不合法,缺少必须的示例'}",
                respons=res)
        self.assertTrue(res['Ret'] == 4003, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "POST参数不合法,缺少必须的示例")

    def test6_dataMiSS_Seq(self):
        '''
        检验post参数不合法,缺少必须参数Seq
        :return:
        '''
        host = self.host
        lujing = 'query_token'
        data = {"OperatorID": "MA35PU38X",
                "Data": "{}".format(self.encrypt_data),
                "TimeStamp": "{}".format(self.times),
                "Sig": "{}".format(self.sig)}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{'Ret': 4003 'Msg': 'POST参数不合法,缺少必须的示例'}",
                respons=res)
        self.assertTrue(res['Ret'] == 4003, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "POST参数不合法,缺少必须的示例")

    def test7_dataMiSS_Sig(self):
        '''
        检验post参数不合法,缺少必须参数Sig
        :return:
        '''

        host = self.host
        lujing = 'query_token'
        data = {"OperatorID": "MA35PU38X",
                "Data": "{}".format(self.encrypt_data),
                "TimeStamp": "{}".format(self.times),
                "Seq": "0001",}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{'Ret': 4003 'Msg': 'POST参数不合法,缺少必须的示例'}",
                respons=res)
        self.assertTrue(res['Ret'] == 4003, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "POST参数不合法,缺少必须的示例")

    def test8_datafield_error(self):
        '''
        检验请求的业务参数不合法(字段命名不正确)
        :return:
        '''

        host = self.host
        lujing = 'query_token'
        data = {"ID": "MA35PU38X",
                "data": "{}".format(self.encrypt_data),
                "TimeS": "{}".format(self.times),
                "Seq": "0001",
                "Sig":"{}".format(self.sig)}
        headers = self.headers
        res = RunMethod().run_main('post', host, lujing, data, headers)
        miaoshu(url=host + lujing, method="post", data=data, check="{'Ret': 4004 'Msg': '请求的业务参数不合法，各接口定义自己的必须参数'}",
                respons=res)
        self.assertTrue(res['Ret'] == 4004, msg="状态码不正确")
        self.assertTrue(res['Msg'] == "请求的业务参数不合法，各接口定义自己的必须参数")




if __name__=='__main__':
    unittest.main()
