# Spherical Bessel Function Zeros Python

This project solves the calculation problem of Spherical Bessel function 

<img src="https://latex.codecogs.com/png.image?\dpi{200}j_n(z)%20=%20\sqrt{\frac{\pi}{2z}J_{n+1/2}(z)}" />

## Usage the class

```python
>>> spherical_bessel = SphericalBesselFunction(100, 100)
>>> spherical_bessel.jn_zero(1, 0)
3.141592653589793
>>> spherical_bessel.jn_zero(1, 4)
8.182561452571242
```

The method was realized with approach which was represented [there](https://scipy-cookbook.readthedocs.io/items/SphericalBesselZeros.html)
