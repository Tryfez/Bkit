import unittest
import RK2

class RK_Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(RK2.e1(), [('компьютер Acer', 'Zoom'), ('компьютер Samsung', 'Photoshop')])
    def test2(self):    
        self.assertEqual(RK2.e2(), [('Imac', 129.0), ('компютер Lenovo', 224.0), ('компьютер Acer', 289.0), ('компьютер Samsung', 2048.0)])
    def test3(self):    
        self.assertEqual(RK2.e3(), [('PyCharm', 'компьютер Acer'), ('Photoshop', 'компьютер Samsung'), ('PyCharm', 'Imac')])
if __name__ == '__main__':
    unittest.main()