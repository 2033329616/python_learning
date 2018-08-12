# 1. 待测试部分，自定义一个字典
class Dict(dict):
    """
    Simple dict but alse support access as x.y style
    
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    
    """
    def __init__(self, **kw):    # 子类的初始化函数
        super().__init__(**kw)   # 继承中使用super代表使用父类的方法，使用父类的初始化
    def __getattr__(self, key):  # 获取字典的key对应的value
        try:
            return self[key]
        except KeyError:         # 如果没有该key，则出现KeyError错误
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    
if __name__=='__main__':         
    import doctest
    doctest.testmod()