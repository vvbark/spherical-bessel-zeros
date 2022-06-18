# spherical-bessel-zeros

This project solves the calculation problem of Spherical Bessel function
$$
j_n(z) = \sqrt{\frac{\pi}{2z}J_{n+1/2}(z)}
$$

## Usage the class

```python
>>> spherical_bessel = SphericalBesselFunction(100, 100)
>>> spherical_bessel.jn_zero(1, 0)
3.141592653589793
>>> spherical_bessel.jn_zero(1, 4)
8.182561452571242
```