class BaseClass(object):
  def __init__():
    """super()函数的参数有两个，第一个参数是当前子类的类对象（即子类本身），第二个参数是当前子类的实例对象。这两个参数都是可选的，如果省略不写，则Python会自动推断出需要的参数。"""
    super(BaseClass, self).__init__() # 在Python 3.x版本中，可以直接写成super().__init__()。

