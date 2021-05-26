import unittest
print("Please enter your ID num=")
id = input()
def check_id(id):
    if len(id)!=10:
      print('Must have 10 elements!')
      return False
    if not (id[0].isupper()):
        print('First letter must be upper!')
        return False
    if not (id[1] in "12"):
        print('Second letter must be 1 or 2!')
        return False
    for x in id[2:]:
        if not x.isdigit():
            print('3 to 10 cells Must be numbers!')
            return False
    else:
      print('Input correct!')
      return True
check_id(id)


class MTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(len(id),10)
    def test2(self):
        self.assertEqual(True,id[0].isupper())
    def test3(self):
        self.assertEqual(True,id[1] in "12")
    def test4(self):
      for x in id[2:]:
        self.assertEqual(True,x.isdigit())

if __name__ == '__main__':
  unittest.main()