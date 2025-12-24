import unittest

def square(n):
    '''Принимает число n, возвращает квадрат числа n

            Параметры:
                    n (int/float): число

            Возвращаемое значение:
                    - (int/float): квадрат числа
    '''
    return n**2

def add_binary(a,b):
    '''
    Возвращает сумму двух десятичных чисел в двоичном формате.

            Параметры:
                    a (uint): первое десятичное целое число
                    b (uint): второе десятичное целое число

            Возвращаемое значение:
                    binary_sum (str): двочиная строка a и b
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum

def sqrt(number, n):
    '''Принимает число number и степень n, возвращает корень n-ой степени числа number

            Параметры:
                    number (uint): число
                    n (uint): показатель корня

            Возвращаемое значение:
                    - (float): корень числа n-ой степени
    '''
    return number**(1/n)
   

class OperationsTestCase (unittest.TestCase):
    def test_square(self):
        res = square(2)
        self.assertEqual(res,4)
    def test_square_null(self):
        res = square(0)
        self.assertEqual(res,0)
    def test_square_float(self):
        res = square(1.7)
        self.assertEqual(res,2.89)
    def test_square_neg(self):
        res = square(-3)
        self.assertEqual(res,9)


    def test_bin(self):
        res = add_binary(2,3)
        self.assertEqual(res,"101")
    def test_bin_null(self):
        res = add_binary(0,0)
        self.assertEqual(res,"0")
    def test_bin_float(self):
        with self.assertRaises(TypeError):
            res = add_binary(2,3.4)
    def test_bin_neg(self):
        res = add_binary(-1,-2)
        self.assertEqual(res, "-11")

    def test_sqrt_even(self):
        res = sqrt(4, 2)
        self.assertEqual(res,2)
    def test_sqrt_pdd(self):
        res = sqrt(27,3)
        self.assertEqual(res,3)
    def test_sqrt_num_null(self):
        res = sqrt(0,3)
        self.assertEqual(res,0)
    def test_sqrt_n_null(self):
        with self.assertRaises(ZeroDivisionError):
            res = sqrt(2,0)
    def test_sqrt_num_float(self):
        res = sqrt(0.25,2)
        self.assertEqual(res,0.5)
    def test_sqrt_n_float(self):
        res = sqrt(3, 0.5)
        self.assertEqual(res,9)
    def test_sqrt_num_null(self):
        with self.assertRaises(ValueError):
            res = sqrt(-4, 2)
    def test_sqrt_n_null(self):
        res = sqrt(4, -2)
        self.assertEqual(res, 0.5)
   
        

