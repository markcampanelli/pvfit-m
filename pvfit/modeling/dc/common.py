"""
PVfit: Common items for DC modeling.

Copyright 2023 Intelligent Measurement Systems LLC
"""

from enum import Enum
from typing import TypedDict

import numpy
import scipy.constants


from pvfit.common import k_B_J_per_K, q_C
from pvfit.types import FloatArray, FloatBroadcastable, IntBroadcastable

# Reference values, including Standard Test Condition (STC).

# Temperature.

# STC temperature in degrees Celsius.
T_degC_stc = 25.0

# STC temperature in Kelvin.
T_K_stc = scipy.constants.convert_temperature(T_degC_stc, "Celsius", "Kelvin")

# Total irradiance.

# Hemispherical irradiance at STC (includes specified sun orientation,
# plane orientation, spectrum, etc.).
G_hemi_W_per_m2_stc = 1000.0


class Material(Enum):
    """Photovoltaic materials recognized by PVfit."""

    CIGS = "CIGS"  # Copper Indium Gallium Selenide (CIGS).
    CIS = "CIS"  # Copper Indium diSelenide (CIS).
    CdTe = "CdTe"  # Cadmium Telluride (CdTe).
    GaAs = "GaAs"  # Gallium Arsenide (GaAs).
    monoSi = "mono-Si"  # Mono-crystalline Silicon (mono-Si).
    multiSi = "multi-Si"  # Multi-crystalline Silicon (multi-Si).
    polySi = "poly-Si"  # Poly-crystalline Silicon (poly-Si).
    xSi = "x-Si"  # Crystalline Silicon (x-Si).


class MaterialsInfo(TypedDict):
    """Information for photovoltaic materials recognized by PVfit."""

    E_g_eV_stc: float


# Materials information.
MATERIALS_INFO = {
    Material.CIGS: MaterialsInfo(
        # De Soto et al. 2006.
        E_g_eV_stc=1.15,
    ),
    Material.CIS: MaterialsInfo(
        # De Soto et al. 2006.
        E_g_eV_stc=1.010,
    ),
    Material.CdTe: MaterialsInfo(
        # De Soto et al. 2006.
        E_g_eV_stc=1.475,
    ),
    Material.GaAs: MaterialsInfo(
        # At 300 K, Kittel, C., Intro. to Solid State Physics, 6th ed. 1986, p 185.
        E_g_eV_stc=1.43,
    ),
    Material.monoSi: MaterialsInfo(
        # De Soto et al. 2006.
        E_g_eV_stc=1.121,
    ),
    Material.multiSi: MaterialsInfo(
        # De Soto et al. 2006.
        E_g_eV_stc=1.121,
    ),
    Material.polySi: MaterialsInfo(
        # De Soto et al. 2006.
        E_g_eV_stc=1.121,
    ),
    Material.xSi: MaterialsInfo(
        # De Soto et al. 2006.
        E_g_eV_stc=1.121,
    ),
}

# Limits on ideality factor on first diode.
N_IC_MIN = 1.0
N_IC_MAX = 2.0


def get_scaled_thermal_voltage(
    N_s: IntBroadcastable, T_degC: FloatBroadcastable
) -> FloatArray:
    """
    Compute thermal voltage [V], scaled by the number of cells in series in each
    parallel string.
    """
    return numpy.array(
        N_s
        * (
            k_B_J_per_K
            * scipy.constants.convert_temperature(T_degC, "Celsius", "Kelvin")
            / q_C
        )
    )
