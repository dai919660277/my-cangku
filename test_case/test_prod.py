from tools.api import request_tool
from tools.security.md5_tool import md5_passwd

API_URL="http://api.yansl.com:8084"

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

def test_add_prod(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品接口"  # allure报告中一级分类
    story = '新增产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {"token": pub_data["token"]}
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "brand": "荣耀",
  "colors": [
    "天空蓝","魅焰红","酷炫黑"
  ],
  "price": 2500,
  "productCode": "自动生成 字符串 3 数字字母 rongyao",
  "productName": "华为荣耀",
  "sizes": [
    "6寸"
  ],
  "type": "移动设备"
}
    '''

    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    request_tool.request(json_path=json_path,headers=headers,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    print(pub_data)



def test_post_data(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '修改价格'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_2"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU":pub_data["skuCode"],"price":2000}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_post_incrementSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品库存模块"  # allure报告中一级分类
    story = '增量调整单个商品库存'  # allure报告中二级分类
    title = "锁定用户_全字段正常流_3"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"skuCode":"dd9X_魅焰红_6寸","qty":100}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_post_addOrder(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '无签名无加密下单'  # allure报告中二级分类
    title = "无签名无加密下单_全字段正常流_4"  # allure报告中用例名字
    uri = "/order/addOrder"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = {
  "ordeerPrice": 2500,
  "orderLineList": [
    {
      "qty": 1,
      "skuCode": "dd9X_魅焰红_6寸"
    }
  ],
  "receiver": "东东",
  "receiverPhone": "18715891452",
  "receivingAddress": "上海 闵行 浦江镇 红星美凯龙43洞 果芽415",
  "sign": "None",
  "userName": "xukun666"
}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_post_addOrderSignBody(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "订单模块"  # allure报告中一级分类
    story = '签名加密下单'  # allure报告中二级分类
    title = "无签名无加密下单_全字段正常流_5"  # allure报告中用例名字
    uri = "/order/addOrderSignBody"  # 接口地址
    s="receiver=东东&ordeerPrice=2500&receiverPhone=18715891452&key=guoya"
    sign=md5_passwd(s,"")
    pub_data["sign"]=sign
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = {
  "ordeerPrice": 2500,
  "orderLineList": [
    {
      "qty": 1,
      "skuCode": "dd9X_魅焰红_6寸"
    }
  ],
  "receiver": "东东",
  "receiverPhone": "18715891452",
  "receivingAddress": "上海 闵行 浦江镇 红星美凯龙43洞 果芽415",
  "sign": "${sign}",
  "userName": "xukun666"
}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

