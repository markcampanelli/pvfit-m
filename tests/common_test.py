"""
PVfit testing: Common items.

Copyright 2023 Intelligent Measurement Systems LLC
"""

import pvfit.common as common


def test_q_C():
    assert isinstance(common.q_C, float)
    assert common.q_C == 1.602176634e-19


def test_k_B_J_per_K():
    assert isinstance(common.k_B_J_per_K, float)
    assert common.k_B_J_per_K == 1.380649e-23


def test_k_B_eV_per_K():
    assert isinstance(common.k_B_eV_per_K, float)
    assert common.k_B_eV_per_K == 8.617333262e-05


def test_c_m_per_s():
    assert common.c_m_per_s == 299792458.0


def test_h_J_s():
    assert common.h_J_s == 6.62607015e-34
