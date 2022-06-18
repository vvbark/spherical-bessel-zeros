# spherical-bessel-zeros

This project solves the calculation problem of Spherical Bessel function 

<img src="https://latex.codecogs.com/svg.image?j_n(z)%20=%20\sqrt{\frac{\pi}{2z}J_{n+1/2}(z)}" />

## Usage the class

```python
>>> spherical_bessel = SphericalBesselFunction(100, 100)
>>> spherical_bessel.jn_zero(1, 0)
3.141592653589793
>>> spherical_bessel.jn_zero(1, 4)
8.182561452571242
```

Calculus method was realized with approach represented [there](https://scipy-cookbook.readthedocs.io/items/SphericalBesselZeros.html)
