import unittest
import triangleEngine

class TriangleTestCase(unittest.TestCase):

    ##Aurel Codarcea

    def test_checkLength_6_6_6_And_VerifyStringResultReturn(self):

        ##Arrange
        a = int(6)
        b = int(6)
        c = int(6)

        ##Act
        receive = triangleEngine.define_lenght(a,b,c)

        ##Assert
        self.assertEqual("triangle is equilateral", receive)

    def test_checkLenght_4_5_5_And_VerifyStringResultReturn(self):

        ##Arrange
        a = int(4)
        b = int(5)
        c = int(5)

        ##Act
        receive = triangleEngine.define_lenght(a,b,c)

        ##Assert
        self.assertEqual("triangle is isoscele", receive)

    def test_checkLenght_4_5_3_And_VerifyStringResultReturn(self):

        ##Arrange
        a = int(4)
        b = int(5)
        c = int(3)

        ##Act
        receive = triangleEngine.define_lenght(a,b,c)

        ##Assert
        self.assertEqual("triangle is irregular", receive)
        

if __name__ == '__main__' :
    unittest.main()
