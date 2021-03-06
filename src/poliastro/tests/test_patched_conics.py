# coding: utf-8

from astropy import units as u
from astropy.tests.helper import assert_quantity_allclose

from poliastro.bodies import Sun, Mercury, Venus, Earth, Moon, Mars
from poliastro.bodies import Jupiter, Saturn, Uranus, Neptune, Pluto
from poliastro.patched_conics import compute_soi


def test_compute_soi():
    # Data from Table A.2., Curtis "Orbital Mechanics for Engineering Students"
    data = [
        # body, SOI radius (m)
        (Sun, None),
        (Mercury, 1.12e8),
        (Venus, 6.16e8),
        (Earth, 9.25e8),
        # (Moon, 6.61e7),
        (Mars, 5.77e8),
        (Jupiter, 4.82e10),
        (Saturn, 5.48e10),
        (Uranus, 5.18e10),
        (Neptune, 8.66e10),
        # (Pluto, 3.08e9)
    ]
    for row in data:

        body, expected_r_SOI = row
        if expected_r_SOI is not None:
            expected_r_SOI = expected_r_SOI * u.m
        else:
            continue

        r_SOI = compute_soi(body)

        assert_quantity_allclose(r_SOI, expected_r_SOI, rtol=1e-1)
