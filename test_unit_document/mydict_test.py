# 2. 单元测试部分，拿所有可能结果的实例来测试，包括抛出异常
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):            # 继承后的子类
    def test_init(self):                      # 初始化检测
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)              # 相当于判断 d.a == 1 
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))  # 相当于判断 d的类型是dict
    def test_key(self):                       # 测试key值赋值value
        d = Dict()
        d['key'] = 'value'                    # 为什么加单引号？？？？？
        self.assertEqual(d['key'], 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'                      # ???为什么可以这样赋值
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']               # ???
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
if __name__ == '__main__':
    unittest.main()