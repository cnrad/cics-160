import unittest
from primes import prime_decomposition

class TestLabFour(unittest.TestCase):
    def test_primeDecompositionCorrectForOne(self):
        self.assertEqual([], prime_decomposition(1))

    def test_primeDecompositionCorrectForDistinctPrimes(self):
        self.assertEqual([2,5], prime_decomposition(10))

    def test_primeDecompositionCorrectForSingularPrime(self):
        self.assertEqual([11], prime_decomposition(11))

    def test_primeDecompositionCorrectForRepeatedPrimes(self):
        self.assertEqual([3, 3, 5], prime_decomposition(45))

if __name__ == "__main__":
    unittest.main()