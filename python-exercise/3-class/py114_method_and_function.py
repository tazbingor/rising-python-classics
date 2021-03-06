#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/23 下午6:54
# @Author  : Aries
# @Site    : 
# @File    : py114_method_and_function.py
# @Software: PyCharm
'''
13-2 函数和方法的比较. 函数与方法之间的区别
1. 函数(function)是Python中一个可调用对象(callable), 方法(method)是一种特殊的函数。
2. 一个可调用对象是方法和函数，和这个对象无关，仅和这个对象是否与类或实例绑定有关（bound method）。
3. 实例方法，在类中未和类绑定，是函数；在实例中，此实例方法与实例绑定，即变成方法。
4. 静态方法没有和任何类或实例绑定，所以静态方法是个函数。
5. 装饰器不会改变被装饰函数或方法的类型。
6. 类实现__call__方法,其实例也不会变成方法或函数,依旧是类的实例。
7. 使用callalble() 只能判断对象是否可调用,不能判断是不是函数或方法。
8. 判断对象是函数或方法应该使用type(obj)。

同时,可以总结出一条规律
与类以及实例无绑定关系的function都是函数,反之亦然
'''
