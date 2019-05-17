# !/usr/bin/python
# coding = utf-8
# stack()创建栈
# push()压栈
# pop()弹出栈顶元素
# peek()返回栈顶元素
# is_empty()判空
# size()返回栈的元素个数


class stack(object):
      def __init__(self):
          self._list = []


      def is_empty(self):
          return self._list == []


      def push(self,item):
          self._list.append(item)


      def pop(self):
          return self._list.pop()


      def peek(self):
          if self._list:
             return self._list[-1]
          else:
             return None

      def size(self):
          return len(self._list)


if __name__ == "__main__":
   s = stack()
   s.push(1)
   s.push(2)
   s.push(3)
   print(s.is_empty())
   print(s.peek())
   print(s.size())
