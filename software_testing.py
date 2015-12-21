'''
Created on 2015/11/18
@author: Eric Chou
'''
import unittest
from datetime import date
from startup import Calculate
from startup import download_quarter
from startup import removexml

"""
class boundary_value_test(unittest.TestCase):
#Take {-10000000000.00,+10000000000.00} as the bound of Calculate input val1
#Take {-10000000000.00,!=0,+10000000000.00} as the bound of Calculate input val2
    def test_Calculate(self):
        self.assertEqual(Calculate(10000000000,10000000000),'0.00')
        self.assertEqual(Calculate(10000000000,9999999999.9999),'0.00')
        self.assertEqual(Calculate(10000000000,100000.5555),'9999844.45')
        self.assertEqual(Calculate(10000000000,-9999999999.9999),'-200.00')
        self.assertEqual(Calculate(10000000000,-10000000000),'-200.00')
        
        self.assertEqual(Calculate(9999999999.9999,10000000000),'-0.00')
        self.assertEqual(Calculate(9999999999.9999,9999999999.9999),'0.00')
        self.assertEqual(Calculate(9999999999.9999,100000.5555),'9999844.45')
        self.assertEqual(Calculate(9999999999.9999,-9999999999.9999),'-200.00')
        self.assertEqual(Calculate(9999999999.9999,-10000000000),'-200.00')
        
        self.assertEqual(Calculate(100000.5555,10000000000), '-100.00')
        self.assertEqual(Calculate(100000.5555,9999999999.9999), '-100.00')
        self.assertEqual(Calculate(100000.5555,100000.5555), '0.00')
        self.assertEqual(Calculate(100000.5555,-9999999999.9999), '-100.00')
        self.assertEqual(Calculate(100000.5555,-10000000000), '-100.00')
        
        self.assertEqual(Calculate(-9999999999.9999,10000000000),'-200.00')
        self.assertEqual(Calculate(-9999999999.9999,9999999999.9999),'-200.00')
        self.assertEqual(Calculate(-9999999999.9999,100000.5555),'-10000044.45')
        self.assertEqual(Calculate(-9999999999.9999,-9999999999.9999),'0.00')
        self.assertEqual(Calculate(-9999999999.9999,-10000000000),'-0.00')
        
        self.assertEqual(Calculate(-10000000000,10000000000),'-200.00')
        self.assertEqual(Calculate(-10000000000,9999999999.9999),'-200.00')
        self.assertEqual(Calculate(-10000000000,100000.5555),'-10000044.45')
        self.assertEqual(Calculate(-10000000000,-9999999999.9999),'0.00')
        self.assertEqual(Calculate(-10000000000,-10000000000),'0.00')

#Take {1,4} as the bound of download_quarter's 'quarter' input
#Take {102,current_year(ROC year)} as the bound of download_quarter's 'year' input
    def test_download_quarter(self):
        current_year = date.today().year - 1911
        self.assertFalse(download_quarter(1, 102))
        self.assertTrue(download_quarter(1, 103))
        self.assertTrue(download_quarter(1, 104))
        self.assertTrue(download_quarter(1, current_year-1))
        self.assertTrue(download_quarter(1, current_year))
        
        self.assertFalse(download_quarter(2, 102))
        self.assertTrue(download_quarter(2, 103))
        self.assertTrue(download_quarter(2, 104))
        self.assertTrue(download_quarter(2, current_year-1))
        self.assertTrue(download_quarter(2, current_year))
        
        self.assertTrue(download_quarter(3, 102))
        self.assertTrue(download_quarter(3, 103))
        self.assertTrue(download_quarter(3, 104))
        self.assertTrue(download_quarter(3, current_year-1))
        self.assertTrue(download_quarter(3, current_year))
        
        self.assertTrue(download_quarter(4, 102))
        self.assertTrue(download_quarter(4, 103))
        self.assertFalse(download_quarter(4, 104))
        self.assertTrue(download_quarter(4, current_year-1))
        self.assertFalse(download_quarter(4, current_year))
        
        self.assertFalse(download_quarter(5, 102))
        self.assertFalse(download_quarter(5, 103))
        self.assertFalse(download_quarter(5, 104))
        self.assertFalse(download_quarter(5, current_year-1))
        self.assertFalse(download_quarter(5, current_year))

class equivalence_class_test(unittest.TestCase):
#-10000000000<=val1<=10000000000; {va11<-10000000000},{-10000000000<=va12<=-10000000000},{10000000000<va13}
#-10000000000<=val2<0;0<val2<=10000000000; {va21<-10000000000},{-10000000000<=va22<0},{va23==0},{0<va24<=10000000000},{10000000000<va25}
    def test_Calculate(self):
        self.assertEqual(Calculate(20000000000,-7890000),'error')
        self.assertEqual(Calculate(-10000000005,-9999999999.9999),'error')
        self.assertEqual(Calculate(1359002.32,683201.5000),'98.92')
        self.assertEqual(Calculate(1359002.32,0.0),'error')
        self.assertEqual(Calculate(765750,-23505000.20),'-103.26')
        self.assertEqual(Calculate(100099999999900,9999100),'error')
        self.assertEqual(Calculate(-1982027700000,9999999999999999.9999),'error')
      
#1<=quarter<=4; {q1<1},{1<=q2<=4},{4<q3}
#102<=year<=current_year; {y1<102},{102<=y2<=current_year},{current_year<y3}
    def test_download_quarter(self):
        current_year = date.today().year - 1911
        self.assertFalse(download_quarter(0, 101))
        self.assertFalse(download_quarter(2, 100))
        self.assertFalse(download_quarter(6, 99))
        self.assertFalse(download_quarter(0, 102))
        self.assertTrue(download_quarter(3, 103))
        self.assertFalse(download_quarter(5, current_year-1))
        self.assertFalse(download_quarter(-1, current_year+1))
        self.assertFalse(download_quarter(4, current_year+2))
        self.assertFalse(download_quarter(6, current_year+3))
"""
     
class path_coverage_test(unittest.TestCase):
    def test_Calculate(self):
        self.assertEqual(Calculate(20000000000,20000000000),'error')
        self.assertEqual(Calculate(20000000000,-99999999999),'error')
        self.assertEqual(Calculate(20000000000,0),'error')
        self.assertEqual(Calculate(20000000000,12345),'error')
        
        self.assertEqual(Calculate(-10000000005,20000000000),'error')
        self.assertEqual(Calculate(-10000000005,-99999999999),'error')
        self.assertEqual(Calculate(-10000000005,0),'error')
        self.assertEqual(Calculate(-10000000005,12345),'error')
        
        self.assertEqual(Calculate(23560,20000000000),'error')
        self.assertEqual(Calculate(23560,-99999999999),'error')
        self.assertEqual(Calculate(23560,0),'error')
        self.assertEqual(Calculate(23560,12345),'90.85')

    def test_download_quarter(self):
        current_year = date.today().year - 1911
        self.assertFalse(download_quarter(0, current_year+1))
        self.assertFalse(download_quarter(1, current_year+1))
        self.assertFalse(download_quarter(2, current_year+1))
        self.assertFalse(download_quarter(4, current_year+1))
        self.assertFalse(download_quarter(5, current_year+1))
        
        self.assertFalse(download_quarter(0, 102))
        self.assertFalse(download_quarter(1, 102))
        self.assertFalse(download_quarter(2, 102))
        self.assertTrue(download_quarter(4, 102))
        self.assertFalse(download_quarter(5, 102))
        
        self.assertFalse(download_quarter(0, 104))
        self.assertTrue(download_quarter(1, 104))
        self.assertTrue(download_quarter(2, 104))
        self.assertFalse(download_quarter(4, 104))
        self.assertFalse(download_quarter(5, 104))
        
        self.assertFalse(download_quarter(0, 100))
        self.assertFalse(download_quarter(1, 100))
        self.assertFalse(download_quarter(2, 100))
        self.assertFalse(download_quarter(4, 100))
        self.assertFalse(download_quarter(5, 100))

if __name__ == '__main__':
    unittest.main(exit=False)
    removexml()
    print('Test finished')