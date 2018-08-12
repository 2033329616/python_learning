# 1. 待测试部分，自定义一个字典
class Dict(dict):
    def __init__(self, **kw):    # 子类的初始化函数
        super().__init__(**kw)   # 继承中使用super代表使用父类的方法，使用父类的初始化
    def __getattr__(self, key):  # 获取字典的key对应的value
        try:
            return self[key]
        except KeyError:         # 如果没有该key，则出现KeyError错误
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value