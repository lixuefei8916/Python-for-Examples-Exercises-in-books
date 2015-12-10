#-*- coding: utf-8 -*-
'''
# ===========================================================
# from Python »   Documentation » The Python Standard Library » 25. Development Tools »

import unittest

class TestStringMethods(unittest.TestCase):
	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(),['hello','world'])
		with self.assertRaises(TypeError):
			s.split(2)

if __name__ == '__main__':
	unittest.main()
'''
# ===========================================================
'''
# 测试 def
 test.py
def sum(x,y):
	return x+y

def sub(x,y):
	return x-y

import unittest
import myclass
class Test(unittest.TestCase):
  	def setUp(self): 			##初始化工作 
		pass
  	def tearDown(self): 		#退出清理工作
  		pass

  	# 具体的测试用例，一定要以test开头
	def testsum(self):
		self.assertEqual(myclass.sum(2,3),5)
	def testsub(self):
		self.assertEqual(myclass.sub(3,2),2,'False 3-2=1 !!!')

if __name__ == '__main__':
	unittest.main()

'''
# ===========================================================
'''
# 测试 class
class Myclass(object):
	def __init__(self):
		pass
	def sum(self,x,y):
		return x+y
	def sub(self,x,y):
		return x-y

import unittest
import myclass

class Test(unittest.TestCase):
	def setUp(self):
		self.tclass = myclass.Myclass()
	def testsum(self):
		self.assertEqual(self.tclass.sum(1,3),4)
	def testsub(self):
		self.assertEqual(self.tclass.sub(3,1),2)
if __name__ == '__main__':
	unittest.main()

'''
# ===========================================================
'''
加载测试套件
from http://www.jb51.net/article/65856.htm

>>import unittest 
>>dir(unittest) 
>>memblist = ['FunctionTestCase', 'TestCase', 'TestLoader', 'TestProgram', 'TestResult',\ 
'TestSuite','TextTestRunner', 'defaultTestLoader','findTestCases', 'getTestCaseNames', \ 
'main', 'makeSuite'] 
>>for memb in memblist: 
.. cur = getattr(unittest, memb) 
.. print help(cur)


'FunctionTestCase':函数测试用例，即给一个函数作为参数，返回一个testcase实例，可选参数有set-up，tear-down方法
'TestCase'：所有测试用例的基本类，给一个测试方法的名字，返回一个测试用例实例
'TestLoader'：测试用例加载器，其包括多个加载测试用例的方法。返回一个测试套件
loadTestsFromModule(self, module)--根据给定的模块实例来获取测试用例套件
loadTestsFromName(self, name, module=None)
--根据给定的字符串来获取测试用例套件，字符串可以是模块名，测试类名，测试类中的测试方法名，或者一个可调用的是实例对象
这个实例对象返回一个测试用例或一个测试套件
loadTestsFromNames(self, names, module=None) --和上面功能相同，只不过接受的是字符串列表
loadTestsFromTestCase(self, testCaseClass)--根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
'TestProgram'：命令行进行单元测试的调用方法，作用是执行一个测试用例。其实unittest.main()方法执行的就是这个命令，
而这个类实例时默认加载当前执行的作为测试对象，
原型为 __init__(self, module='__main__', defaultTest=None, argv=None, testRunner=xx, testLoader=xx)
其中module='__main__'就是默认加载自身
'TestResult'：测试用例的结果保存实例，通常有测试框架调用
'TestSuite'：组织测试用例的实例，支持测试用例的添加和删除，最终将传递给testRunner进行测试执行
'TextTestRunner'：进行测试用例执行的实例，其中Text的意思是以文本形式显示测试结果。显示测试名称，即完成的测试结果，其过同执行单元测试脚本时添加-v参数
'defaultTestLoader':其实就是TestLoader
'findTestCases', 'getTestCaseNames'：这个2个就不用解释了
'main': 其实就是TestProgram
'makeSuite'：通常是由单元测试框架调用的，用于生产testsuite对象的实例




整个单元测试框架
分三步走： testloader --> makesuite组装成testsuite --> testrunner执行
详解：第一步testloader根据传入的参数获得相应的测试用例，即对应具体的测试方法，
然后makesuite在把所有的测试用例组装成testsuite，最后把testsiute传给testrunner进行执行

【测试用例文件必须为test开头，如：testxxx.py, 当然这个文件本身是一个单元测试的文件】

import unittest
import myclass
import re,os,sys

def testAllinCurrent():
  	path = os.path.abspath(os.path.dirname(sys.argv[0]))
  	files = os.listdir(path)
  	test = re.compile("test\.py{1}quot;", re.IGNORECASE)
  	files = filter(test.search, files)
  	filenameToModuleName = lambda f: os.path.splitext(f)[0]
  	moduleNames = map(filenameToModuleName, files)
  	modules = map(__import__, moduleNames)
  	load = unittest.defaultTestLoader.loadTestsFromModule
  	return unittest.TestSuite(map(load, modules))
if __name__ == "__main__":
	unittest.main(defaultTest="regressionTest")
'''
# ===========================================================
'''
Python之自动单元测试之一（unittest使用实例）
from http://www.tuicool.com/articles/263m22

myclass.py文件
class Widget():
	def __init__(self,size=(40,40)):
		self._size = size
	def getSize(self):
		return self._size
	def resize(self,width,height):
		if width < 0 or height < 0:
			raise ValueError,'illegal size'
		self._size = (width,height)

from myclass import Widget
import unittest

class WidgetTestCase(unittest.TestCase):
	def setUp(self):
		self.lxf = Widget()
	def tearDown(self):
        self.lxf.dispose()
        self.lxf = None
	def testSize(self):
		self.assertEqual(self.lxf.getSize(),(40,40))
		# 对Widget类中getSize()方法的返回值和预期值进行比较，确保两者是相等的
    def testResize(self):
        self.lxf.resize(100, 100)
        self.assertEqual(self.lxf.getSize(), (100, 100))

def suite():
	suite = unittest.TestSuite()
	suite.addTest(WidgetTestCase("testSize"))
	suite.addTest(WidgetTestCase("testResize"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = 'suite')



#-------------------------------------
TestSuit 测试用例集
from http://www.tuicool.com/articles/263m22

完整的单元测试很少只执行一个测试用例，开发人员通常都需要编写多个测试用例才能对某一软件功能进行比较完整的测试，这些相关的测试用例称为一个测试用例集，在PyUnit中是用TestSuite类来表示的。
在创建了一些TestCase子类的实例作为测试用例之后，下一步要做的工作就是用TestSuit类来组织它们。PyUnit测试框架允许Python程序员在单元测试代码中定义一个名为suite()的全局函数，并将其作为整个单元测试的入口，PyUnit通过调用它来完成整个测试过程。

'''
from myclass import Widget
import unittest

class WidgetTestCase(unittest.TestCase):
	#def __init__(self):
	#	unittest.TestSuite.__init__(self,map(WidgetTestCase,("testSize","testResize")))
	
	def setUp(self):
		self.lxf = Widget()
	def tearDown(self):
		pass
		#self.lxf.dispose()
		#self.lxf = None
	def testSize(self):
		self.assertEqual(self.lxf.getSize(),(40,40))

	def testResize(self):
		self.lxf.resize(100, 100)
		self.assertEqual(self.lxf.getSize(), (100, 100))

if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(WidgetTestCase("testSize"))
	suite.addTest(WidgetTestCase("testResize"))

	runner = unittest.TextTestRunner()
	runner.run(suite)


如果Python程序员能够按照约定（以test开头）来命名所有的测试方法，那就只需要在测试模块的最后加入如下几行代码即可：
if __name__ == "__main__":
    unittest.main()

图形界面测试脚本unittestgui.py
将其复制到当前目录后，可以执行下面的命令来启动该测试工具，对main_runner.py脚本中的所有测试用例进行测试：
python unittestgui.py main_runner

# ===========================================================
# ===========================================================
# ===========================================================
# ===========================================================
# ===========================================================
# ===========================================================
# ===========================================================
# ===========================================================
# ===========================================================
# ===========================================================





