import numpy as np
from scipy.special import spherical_jn
from scipy.optimize import brentq


class SphericalBesselFunction:
    '''Class for keeping zeros of spherical Bessel function.'''

    def __init__(self, max_quantum_number: int, max_orbital_moment: int):
        '''Initialize the class.
        
        :param max_quantum_number: The count of zeros
        :param max_orbital_moment: The maximum order of Bessel function
        '''
        if max_quantum_number < max_orbital_moment:
            raise Exception('Check the condition of n and l while initialization')
            
        self.zeros_table = self._spherical_bessel_zeros_table(
            max_quantum_number,
            max_orbital_moment,
        )

    @staticmethod
    def _spherical_bessel(z, n):
        return spherical_jn(n, z)

    def _spherical_bessel_zeros_table(self, n, l):
        '''Calculate and save grid of zeros n x (l + 1).'''
        zeros = np.zeros((n + l, l + 1))
        zeros[:, 0] = np.arange(1, zeros.shape[0] + 1) * np.pi
        for i in range(1, l + 1):
            for j in range(n + l - i):
                zeros[j, i] = brentq(
                    self._spherical_bessel,
                    zeros[j, i - 1],
                    zeros[j + 1, i  -1],
                    args=(i),
                )
        return zeros[:-l]

    def jn_zero(self, quantum_number: int, orbital_moment: int) -> float:
        '''Method for extracting zero from calculated grid.'''
        check_condition = (
            quantum_number > self.zeros_table.shape[0] or
            orbital_moment > self.zeros_table.shape[1] - 1
        )
        if check_condition:
            raise IndexError('Check the maximum generated bessel zeros')
        return self.zeros_table[quantum_number - 1, orbital_moment]
