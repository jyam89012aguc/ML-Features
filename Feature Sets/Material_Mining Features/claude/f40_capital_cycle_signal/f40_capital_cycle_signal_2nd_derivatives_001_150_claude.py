import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _chg(s, w):
    return s - s.shift(w)


def _capex_intensity(capex, assets):
    return capex / assets.replace(0, np.nan)


def _capex_to_ppne(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan)


def _asset_growth(assets, w):
    return np.log(assets.replace(0, np.nan) / assets.shift(w).replace(0, np.nan))


def _invcap_growth(invcap, w):
    return np.log(invcap.replace(0, np.nan) / invcap.shift(w).replace(0, np.nan))


def _roic_sm(roic, w):
    return roic.rolling(w, min_periods=max(1, w // 2)).mean()


def _roic_below_hurdle(roic, w=504):
    sm = roic.rolling(63, min_periods=21).mean()
    hurdle = roic.rolling(w, min_periods=max(1, w // 2)).median()
    return (hurdle - sm).clip(lower=0)


def _build_minus_return(growth_term, roic, w):
    dr = roic - roic.shift(w)
    return growth_term - dr



def _slope(s, w):
    # 1st math derivative: rate of change over w trading days
    return (s - s.shift(w)) / float(w)



# ========================================================
# 1st math derivative (slope) of capital-cycle build-vs-return bases.
# ROC window matched to base horizon (21/63/126d). Every base couples
# a build/investment term WITH the ROIC/return dimension.

# capex-intensity z minus ROIC z (build-vs-return divergence) (slope of base)
def f40cc_f40_capital_cycle_signal_buildretz_21d_slope_v001_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 252) - _z(roic, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex-intensity z minus ROIC z (build-vs-return divergence) (slope of base)
def f40cc_f40_capital_cycle_signal_buildretz_63d_slope_v002_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 252) - _z(roic, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex-intensity z minus ROIC z (build-vs-return divergence) (slope of base)
def f40cc_f40_capital_cycle_signal_buildretz_126d_slope_v003_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 252) - _z(roic, 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset growth minus ROIC change (core divergence) (slope of base)
def f40cc_f40_capital_cycle_signal_assetgvsret_21d_slope_v004_signal(assets, roic):
    base = _build_minus_return(_asset_growth(assets, 252), roic, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset growth minus ROIC change (core divergence) (slope of base)
def f40cc_f40_capital_cycle_signal_assetgvsret_63d_slope_v005_signal(assets, roic):
    base = _build_minus_return(_asset_growth(assets, 252), roic, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset growth minus ROIC change (core divergence) (slope of base)
def f40cc_f40_capital_cycle_signal_assetgvsret_126d_slope_v006_signal(assets, roic):
    base = _build_minus_return(_asset_growth(assets, 252), roic, 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap growth minus ROIC level (build above return) (slope of base)
def f40cc_f40_capital_cycle_signal_invcapgvsroic_21d_slope_v007_signal(invcap, roic):
    base = _invcap_growth(invcap, 252) - _roic_sm(roic, 63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap growth minus ROIC level (build above return) (slope of base)
def f40cc_f40_capital_cycle_signal_invcapgvsroic_63d_slope_v008_signal(invcap, roic):
    base = _invcap_growth(invcap, 252) - _roic_sm(roic, 63)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap growth minus ROIC level (build above return) (slope of base)
def f40cc_f40_capital_cycle_signal_invcapgvsroic_126d_slope_v009_signal(invcap, roic):
    base = _invcap_growth(invcap, 252) - _roic_sm(roic, 63)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# reinvestment rate minus ROIC level (spend faster than earn) (slope of base)
def f40cc_f40_capital_cycle_signal_reinvminroic_21d_slope_v010_signal(capex, ppnenet, roic):
    base = _capex_to_ppne(capex, ppnenet) - _roic_sm(roic, 63)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# reinvestment rate minus ROIC level (spend faster than earn) (slope of base)
def f40cc_f40_capital_cycle_signal_reinvminroic_63d_slope_v011_signal(capex, ppnenet, roic):
    base = _capex_to_ppne(capex, ppnenet) - _roic_sm(roic, 63)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# reinvestment rate minus ROIC level (spend faster than earn) (slope of base)
def f40cc_f40_capital_cycle_signal_reinvminroic_126d_slope_v012_signal(capex, ppnenet, roic):
    base = _capex_to_ppne(capex, ppnenet) - _roic_sm(roic, 63)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# PP&E growth minus ROIC change (capacity vs return) (slope of base)
def f40cc_f40_capital_cycle_signal_ppnegvsret_21d_slope_v013_signal(ppnenet, roic):
    base = _growth(ppnenet, 252) - _chg(roic, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# PP&E growth minus ROIC change (capacity vs return) (slope of base)
def f40cc_f40_capital_cycle_signal_ppnegvsret_63d_slope_v014_signal(ppnenet, roic):
    base = _growth(ppnenet, 252) - _chg(roic, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# PP&E growth minus ROIC change (capacity vs return) (slope of base)
def f40cc_f40_capital_cycle_signal_ppnegvsret_126d_slope_v015_signal(ppnenet, roic):
    base = _growth(ppnenet, 252) - _chg(roic, 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# high-build x low-return misallocation product (slope of base)
def f40cc_f40_capital_cycle_signal_misalloc_21d_slope_v016_signal(invcap, roic):
    base = _z(_invcap_growth(invcap, 252), 252) * (-_z(roic, 252))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# high-build x low-return misallocation product (slope of base)
def f40cc_f40_capital_cycle_signal_misalloc_63d_slope_v017_signal(invcap, roic):
    base = _z(_invcap_growth(invcap, 252), 252) * (-_z(roic, 252))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# high-build x low-return misallocation product (slope of base)
def f40cc_f40_capital_cycle_signal_misalloc_126d_slope_v018_signal(invcap, roic):
    base = _z(_invcap_growth(invcap, 252), 252) * (-_z(roic, 252))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# over-build trap: capex z x negative ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_overbuildtrap_21d_slope_v019_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 504) * (-_z(roic, 504))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# over-build trap: capex z x negative ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_overbuildtrap_63d_slope_v020_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 504) * (-_z(roic, 504))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# over-build trap: capex z x negative ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_overbuildtrap_126d_slope_v021_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 504) * (-_z(roic, 504))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex starvation x ROIC level (starve + earn) (slope of base)
def f40cc_f40_capital_cycle_signal_starvepayoff_21d_slope_v022_signal(capex, ppnenet, roic):
    base = (-_z(_capex_to_ppne(capex, ppnenet), 504)) * np.tanh(5.0 * _roic_sm(roic, 63))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex starvation x ROIC level (starve + earn) (slope of base)
def f40cc_f40_capital_cycle_signal_starvepayoff_63d_slope_v023_signal(capex, ppnenet, roic):
    base = (-_z(_capex_to_ppne(capex, ppnenet), 504)) * np.tanh(5.0 * _roic_sm(roic, 63))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex starvation x ROIC level (starve + earn) (slope of base)
def f40cc_f40_capital_cycle_signal_starvepayoff_126d_slope_v024_signal(capex, ppnenet, roic):
    base = (-_z(_capex_to_ppne(capex, ppnenet), 504)) * np.tanh(5.0 * _roic_sm(roic, 63))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# marginal ROIC: ROIC change per unit invcap growth (slope of base)
def f40cc_f40_capital_cycle_signal_margroic_21d_slope_v025_signal(invcap, roic):
    base = (_chg(roic, 252)) / (_invcap_growth(invcap, 252)).replace(0, np.nan)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# marginal ROIC: ROIC change per unit invcap growth (slope of base)
def f40cc_f40_capital_cycle_signal_margroic_63d_slope_v026_signal(invcap, roic):
    base = (_chg(roic, 252)) / (_invcap_growth(invcap, 252)).replace(0, np.nan)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# marginal ROIC: ROIC change per unit invcap growth (slope of base)
def f40cc_f40_capital_cycle_signal_margroic_126d_slope_v027_signal(invcap, roic):
    base = (_chg(roic, 252)) / (_invcap_growth(invcap, 252)).replace(0, np.nan)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity per unit of ROIC (cost of return) (slope of base)
def f40cc_f40_capital_cycle_signal_capexperroic_21d_slope_v028_signal(capex, assets, roic):
    r = _roic_sm(roic, 63)
    base = _capex_intensity(capex, assets) / r.where(r.abs() > 0.005)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity per unit of ROIC (cost of return) (slope of base)
def f40cc_f40_capital_cycle_signal_capexperroic_63d_slope_v029_signal(capex, assets, roic):
    r = _roic_sm(roic, 63)
    base = _capex_intensity(capex, assets) / r.where(r.abs() > 0.005)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex intensity per unit of ROIC (cost of return) (slope of base)
def f40cc_f40_capital_cycle_signal_capexperroic_126d_slope_v030_signal(capex, assets, roic):
    r = _roic_sm(roic, 63)
    base = _capex_intensity(capex, assets) / r.where(r.abs() > 0.005)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC per unit of capex intensity (return per build) (slope of base)
def f40cc_f40_capital_cycle_signal_roicperbuild_21d_slope_v031_signal(roic, capex, assets):
    base = _roic_sm(roic, 63) / (_capex_intensity(capex, assets) + 0.01)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC per unit of capex intensity (return per build) (slope of base)
def f40cc_f40_capital_cycle_signal_roicperbuild_63d_slope_v032_signal(roic, capex, assets):
    base = _roic_sm(roic, 63) / (_capex_intensity(capex, assets) + 0.01)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC per unit of capex intensity (return per build) (slope of base)
def f40cc_f40_capital_cycle_signal_roicperbuild_126d_slope_v033_signal(roic, capex, assets):
    base = _roic_sm(roic, 63) / (_capex_intensity(capex, assets) + 0.01)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# bounded over-build minus return divergence (slope of base)
def f40cc_f40_capital_cycle_signal_buildretbounded_21d_slope_v034_signal(capex, assets, roic):
    base = np.tanh(_z(_capex_intensity(capex, assets), 504)) - np.tanh(_z(roic, 504))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# bounded over-build minus return divergence (slope of base)
def f40cc_f40_capital_cycle_signal_buildretbounded_63d_slope_v035_signal(capex, assets, roic):
    base = np.tanh(_z(_capex_intensity(capex, assets), 504)) - np.tanh(_z(roic, 504))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# bounded over-build minus return divergence (slope of base)
def f40cc_f40_capital_cycle_signal_buildretbounded_126d_slope_v036_signal(capex, assets, roic):
    base = np.tanh(_z(_capex_intensity(capex, assets), 504)) - np.tanh(_z(roic, 504))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex growth x ROIC deceleration (warning) (slope of base)
def f40cc_f40_capital_cycle_signal_capexgxroicdec_21d_slope_v037_signal(capex, roic):
    base = np.tanh(4.0 * _growth(capex, 252)) * np.tanh(-4.0 * _chg(roic, 252))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex growth x ROIC deceleration (warning) (slope of base)
def f40cc_f40_capital_cycle_signal_capexgxroicdec_63d_slope_v038_signal(capex, roic):
    base = np.tanh(4.0 * _growth(capex, 252)) * np.tanh(-4.0 * _chg(roic, 252))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex growth x ROIC deceleration (warning) (slope of base)
def f40cc_f40_capital_cycle_signal_capexgxroicdec_126d_slope_v039_signal(capex, roic):
    base = np.tanh(4.0 * _growth(capex, 252)) * np.tanh(-4.0 * _chg(roic, 252))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset-growth z penalised by ROIC below mid-cycle (slope of base)
def f40cc_f40_capital_cycle_signal_overbuildpen_21d_slope_v040_signal(assets, roic):
    base = _z(_asset_growth(assets, 252), 504) * (1.0 + 5.0 * (_mean(roic, 1260) - roic).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset-growth z penalised by ROIC below mid-cycle (slope of base)
def f40cc_f40_capital_cycle_signal_overbuildpen_63d_slope_v041_signal(assets, roic):
    base = _z(_asset_growth(assets, 252), 504) * (1.0 + 5.0 * (_mean(roic, 1260) - roic).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset-growth z penalised by ROIC below mid-cycle (slope of base)
def f40cc_f40_capital_cycle_signal_overbuildpen_126d_slope_v042_signal(assets, roic):
    base = _z(_asset_growth(assets, 252), 504) * (1.0 + 5.0 * (_mean(roic, 1260) - roic).clip(lower=0))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# low capex z + rising ROIC (tightening payoff) (slope of base)
def f40cc_f40_capital_cycle_signal_tighteningpay_21d_slope_v043_signal(capex, assets, roic):
    base = (-_z(_capex_intensity(capex, assets), 504)) + _chg(roic, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# low capex z + rising ROIC (tightening payoff) (slope of base)
def f40cc_f40_capital_cycle_signal_tighteningpay_63d_slope_v044_signal(capex, assets, roic):
    base = (-_z(_capex_intensity(capex, assets), 504)) + _chg(roic, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# low capex z + rising ROIC (tightening payoff) (slope of base)
def f40cc_f40_capital_cycle_signal_tighteningpay_126d_slope_v045_signal(capex, assets, roic):
    base = (-_z(_capex_intensity(capex, assets), 504)) + _chg(roic, 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# blended build minus return cycle score (slope of base)
def f40cc_f40_capital_cycle_signal_cyclescore_21d_slope_v046_signal(capex, assets, invcap, roic):
    base = 0.5 * _z(_capex_intensity(capex, assets), 504) + 0.5 * _z(_invcap_growth(invcap, 252), 504) - _z(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# blended build minus return cycle score (slope of base)
def f40cc_f40_capital_cycle_signal_cyclescore_63d_slope_v047_signal(capex, assets, invcap, roic):
    base = 0.5 * _z(_capex_intensity(capex, assets), 504) + 0.5 * _z(_invcap_growth(invcap, 252), 504) - _z(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# blended build minus return cycle score (slope of base)
def f40cc_f40_capital_cycle_signal_cyclescore_126d_slope_v048_signal(capex, assets, invcap, roic):
    base = 0.5 * _z(_capex_intensity(capex, assets), 504) + 0.5 * _z(_invcap_growth(invcap, 252), 504) - _z(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# reinvestment-rate z minus ROIC z (cycle extreme) (slope of base)
def f40cc_f40_capital_cycle_signal_reinvretz_21d_slope_v049_signal(capex, ppnenet, roic):
    base = _z(_capex_to_ppne(capex, ppnenet), 504) - _z(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# reinvestment-rate z minus ROIC z (cycle extreme) (slope of base)
def f40cc_f40_capital_cycle_signal_reinvretz_63d_slope_v050_signal(capex, ppnenet, roic):
    base = _z(_capex_to_ppne(capex, ppnenet), 504) - _z(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# reinvestment-rate z minus ROIC z (cycle extreme) (slope of base)
def f40cc_f40_capital_cycle_signal_reinvretz_126d_slope_v051_signal(capex, ppnenet, roic):
    base = _z(_capex_to_ppne(capex, ppnenet), 504) - _z(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# PP&E-intensity z minus ROIC z (heaviness vs return) (slope of base)
def f40cc_f40_capital_cycle_signal_ppneintvsroic_21d_slope_v052_signal(ppnenet, invcap, roic):
    base = _z(ppnenet / invcap.replace(0, np.nan), 504) - _z(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# PP&E-intensity z minus ROIC z (heaviness vs return) (slope of base)
def f40cc_f40_capital_cycle_signal_ppneintvsroic_63d_slope_v053_signal(ppnenet, invcap, roic):
    base = _z(ppnenet / invcap.replace(0, np.nan), 504) - _z(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# PP&E-intensity z minus ROIC z (heaviness vs return) (slope of base)
def f40cc_f40_capital_cycle_signal_ppneintvsroic_126d_slope_v054_signal(ppnenet, invcap, roic):
    base = _z(ppnenet / invcap.replace(0, np.nan), 504) - _z(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap-intensity z minus ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_invcapintvsroic_21d_slope_v055_signal(invcap, assets, roic):
    base = _z(invcap / assets.replace(0, np.nan), 504) - _z(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap-intensity z minus ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_invcapintvsroic_63d_slope_v056_signal(invcap, assets, roic):
    base = _z(invcap / assets.replace(0, np.nan), 504) - _z(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap-intensity z minus ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_invcapintvsroic_126d_slope_v057_signal(invcap, assets, roic):
    base = _z(invcap / assets.replace(0, np.nan), 504) - _z(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# smoothed invcap-growth z x negative ROIC trend (slope of base)
def f40cc_f40_capital_cycle_signal_buildretema_21d_slope_v058_signal(invcap, roic):
    g = _invcap_growth(invcap, 63).ewm(span=126, min_periods=63).mean()
    base = _z(g, 252) * np.tanh(-5.0 * _chg(roic, 126))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# smoothed invcap-growth z x negative ROIC trend (slope of base)
def f40cc_f40_capital_cycle_signal_buildretema_63d_slope_v059_signal(invcap, roic):
    g = _invcap_growth(invcap, 63).ewm(span=126, min_periods=63).mean()
    base = _z(g, 252) * np.tanh(-5.0 * _chg(roic, 126))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# smoothed invcap-growth z x negative ROIC trend (slope of base)
def f40cc_f40_capital_cycle_signal_buildretema_126d_slope_v060_signal(invcap, roic):
    g = _invcap_growth(invcap, 63).ewm(span=126, min_periods=63).mean()
    base = _z(g, 252) * np.tanh(-5.0 * _chg(roic, 126))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# favourable starvation: -asset growth + ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_favstarve_21d_slope_v061_signal(assets, roic):
    base = (-_asset_growth(assets, 504)) * 5.0 + _z(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# favourable starvation: -asset growth + ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_favstarve_63d_slope_v062_signal(assets, roic):
    base = (-_asset_growth(assets, 504)) * 5.0 + _z(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# favourable starvation: -asset growth + ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_favstarve_126d_slope_v063_signal(assets, roic):
    base = (-_asset_growth(assets, 504)) * 5.0 + _z(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# tanh(ROIC) signed by invcap-growth direction (slope of base)
def f40cc_f40_capital_cycle_signal_steadybuildret_21d_slope_v064_signal(invcap, roic):
    base = np.tanh(roic.ewm(span=63, min_periods=21).mean() * 4.0) * np.sign(_invcap_growth(invcap, 252))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# tanh(ROIC) signed by invcap-growth direction (slope of base)
def f40cc_f40_capital_cycle_signal_steadybuildret_63d_slope_v065_signal(invcap, roic):
    base = np.tanh(roic.ewm(span=63, min_periods=21).mean() * 4.0) * np.sign(_invcap_growth(invcap, 252))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# tanh(ROIC) signed by invcap-growth direction (slope of base)
def f40cc_f40_capital_cycle_signal_steadybuildret_126d_slope_v066_signal(invcap, roic):
    base = np.tanh(roic.ewm(span=63, min_periods=21).mean() * 4.0) * np.sign(_invcap_growth(invcap, 252))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC gated by whether capital is expanding (slope of base)
def f40cc_f40_capital_cycle_signal_roicwhilebuild_21d_slope_v067_signal(roic, invcap):
    base = _roic_sm(roic, 21) * np.tanh(8.0 * _invcap_growth(invcap, 252))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC gated by whether capital is expanding (slope of base)
def f40cc_f40_capital_cycle_signal_roicwhilebuild_63d_slope_v068_signal(roic, invcap):
    base = _roic_sm(roic, 21) * np.tanh(8.0 * _invcap_growth(invcap, 252))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC gated by whether capital is expanding (slope of base)
def f40cc_f40_capital_cycle_signal_roicwhilebuild_126d_slope_v069_signal(roic, invcap):
    base = _roic_sm(roic, 21) * np.tanh(8.0 * _invcap_growth(invcap, 252))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# starve-and-earn: -invcap-g z + ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_starveearn_21d_slope_v070_signal(invcap, roic):
    base = -_z(_invcap_growth(invcap, 252), 504) + _z(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# starve-and-earn: -invcap-g z + ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_starveearn_63d_slope_v071_signal(invcap, roic):
    base = -_z(_invcap_growth(invcap, 252), 504) + _z(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# starve-and-earn: -invcap-g z + ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_starveearn_126d_slope_v072_signal(invcap, roic):
    base = -_z(_invcap_growth(invcap, 252), 504) + _z(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex-cut depth x ROIC level (slash + hold) (slope of base)
def f40cc_f40_capital_cycle_signal_capexcutxret_21d_slope_v073_signal(capex, roic):
    base = (-(capex / _rmax(capex, 504).replace(0, np.nan) - 1.0)) * np.tanh(5.0 * _roic_sm(roic, 63))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex-cut depth x ROIC level (slash + hold) (slope of base)
def f40cc_f40_capital_cycle_signal_capexcutxret_63d_slope_v074_signal(capex, roic):
    base = (-(capex / _rmax(capex, 504).replace(0, np.nan) - 1.0)) * np.tanh(5.0 * _roic_sm(roic, 63))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex-cut depth x ROIC level (slash + hold) (slope of base)
def f40cc_f40_capital_cycle_signal_capexcutxret_126d_slope_v075_signal(capex, roic):
    base = (-(capex / _rmax(capex, 504).replace(0, np.nan) - 1.0)) * np.tanh(5.0 * _roic_sm(roic, 63))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC-change rank minus capex-growth rank (tightening) (slope of base)
def f40cc_f40_capital_cycle_signal_returnspercut_21d_slope_v076_signal(roic, capex):
    base = _rank(_chg(roic, 252), 504) - _rank(_growth(capex, 252), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC-change rank minus capex-growth rank (tightening) (slope of base)
def f40cc_f40_capital_cycle_signal_returnspercut_63d_slope_v077_signal(roic, capex):
    base = _rank(_chg(roic, 252), 504) - _rank(_growth(capex, 252), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC-change rank minus capex-growth rank (tightening) (slope of base)
def f40cc_f40_capital_cycle_signal_returnspercut_126d_slope_v078_signal(roic, capex):
    base = _rank(_chg(roic, 252), 504) - _rank(_growth(capex, 252), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# PP&E-growth rank minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_ppnevsroic_21d_slope_v079_signal(ppnenet, roic):
    base = _rank(_growth(ppnenet, 252), 504) - _rank(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# PP&E-growth rank minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_ppnevsroic_63d_slope_v080_signal(ppnenet, roic):
    base = _rank(_growth(ppnenet, 252), 504) - _rank(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# PP&E-growth rank minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_ppnevsroic_126d_slope_v081_signal(ppnenet, roic):
    base = _rank(_growth(ppnenet, 252), 504) - _rank(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap growth minus ROIC change (504d) (slope of base)
def f40cc_f40_capital_cycle_signal_invbuildret_21d_slope_v082_signal(invcap, roic):
    base = _build_minus_return(_invcap_growth(invcap, 504), roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap growth minus ROIC change (504d) (slope of base)
def f40cc_f40_capital_cycle_signal_invbuildret_63d_slope_v083_signal(invcap, roic):
    base = _build_minus_return(_invcap_growth(invcap, 504), roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap growth minus ROIC change (504d) (slope of base)
def f40cc_f40_capital_cycle_signal_invbuildret_126d_slope_v084_signal(invcap, roic):
    base = _build_minus_return(_invcap_growth(invcap, 504), roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC drawdown scaled by capex intensity (slope of base)
def f40cc_f40_capital_cycle_signal_roicddxbuild_21d_slope_v085_signal(roic, capex, assets):
    base = (roic - _rmax(roic, 504)) * (1.0 + _z(_capex_intensity(capex, assets), 504).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC drawdown scaled by capex intensity (slope of base)
def f40cc_f40_capital_cycle_signal_roicddxbuild_63d_slope_v086_signal(roic, capex, assets):
    base = (roic - _rmax(roic, 504)) * (1.0 + _z(_capex_intensity(capex, assets), 504).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC drawdown scaled by capex intensity (slope of base)
def f40cc_f40_capital_cycle_signal_roicddxbuild_126d_slope_v087_signal(roic, capex, assets):
    base = (roic - _rmax(roic, 504)) * (1.0 + _z(_capex_intensity(capex, assets), 504).clip(lower=0))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex amplitude gated by ROIC weakness (slope of base)
def f40cc_f40_capital_cycle_signal_capexampxlow_21d_slope_v088_signal(capex, roic):
    amp = (_rmax(capex, 504) - _rmin(capex, 504)) / _mean(capex, 504).replace(0, np.nan)
    base = amp * (1.0 + 4.0 * _roic_below_hurdle(roic))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex amplitude gated by ROIC weakness (slope of base)
def f40cc_f40_capital_cycle_signal_capexampxlow_63d_slope_v089_signal(capex, roic):
    amp = (_rmax(capex, 504) - _rmin(capex, 504)) / _mean(capex, 504).replace(0, np.nan)
    base = amp * (1.0 + 4.0 * _roic_below_hurdle(roic))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex amplitude gated by ROIC weakness (slope of base)
def f40cc_f40_capital_cycle_signal_capexampxlow_126d_slope_v090_signal(capex, roic):
    amp = (_rmax(capex, 504) - _rmin(capex, 504)) / _mean(capex, 504).replace(0, np.nan)
    base = amp * (1.0 + 4.0 * _roic_below_hurdle(roic))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset growth minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_agvsroicrank_21d_slope_v091_signal(assets, roic):
    base = _asset_growth(assets, 252) - _rank(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset growth minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_agvsroicrank_63d_slope_v092_signal(assets, roic):
    base = _asset_growth(assets, 252) - _rank(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset growth minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_agvsroicrank_126d_slope_v093_signal(assets, roic):
    base = _asset_growth(assets, 252) - _rank(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capital-cycle phase angle atan2(capex z, ROIC z) (slope of base)
def f40cc_f40_capital_cycle_signal_capexvsroicrank_21d_slope_v094_signal(capex, assets, roic):
    zci = _z(_capex_intensity(capex, assets), 252)
    base = pd.Series(np.arctan2(zci.values, _z(roic, 252).values), index=zci.index) / np.pi
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capital-cycle phase angle atan2(capex z, ROIC z) (slope of base)
def f40cc_f40_capital_cycle_signal_capexvsroicrank_63d_slope_v095_signal(capex, assets, roic):
    zci = _z(_capex_intensity(capex, assets), 252)
    base = pd.Series(np.arctan2(zci.values, _z(roic, 252).values), index=zci.index) / np.pi
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capital-cycle phase angle atan2(capex z, ROIC z) (slope of base)
def f40cc_f40_capital_cycle_signal_capexvsroicrank_126d_slope_v096_signal(capex, assets, roic):
    zci = _z(_capex_intensity(capex, assets), 252)
    base = pd.Series(np.arctan2(zci.values, _z(roic, 252).values), index=zci.index) / np.pi
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex z x ROIC-below-hurdle distance (slope of base)
def f40cc_f40_capital_cycle_signal_overinvhurdle_21d_slope_v097_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 252) * (1.0 + 8.0 * _roic_below_hurdle(roic))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex z x ROIC-below-hurdle distance (slope of base)
def f40cc_f40_capital_cycle_signal_overinvhurdle_63d_slope_v098_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 252) * (1.0 + 8.0 * _roic_below_hurdle(roic))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex z x ROIC-below-hurdle distance (slope of base)
def f40cc_f40_capital_cycle_signal_overinvhurdle_126d_slope_v099_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 252) * (1.0 + 8.0 * _roic_below_hurdle(roic))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC change per unit of asset growth (slope of base)
def f40cc_f40_capital_cycle_signal_buildpayoff_21d_slope_v100_signal(assets, roic):
    base = _chg(roic, 252) / (_asset_growth(assets, 252).abs() + 0.02)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC change per unit of asset growth (slope of base)
def f40cc_f40_capital_cycle_signal_buildpayoff_63d_slope_v101_signal(assets, roic):
    base = _chg(roic, 252) / (_asset_growth(assets, 252).abs() + 0.02)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC change per unit of asset growth (slope of base)
def f40cc_f40_capital_cycle_signal_buildpayoff_126d_slope_v102_signal(assets, roic):
    base = _chg(roic, 252) / (_asset_growth(assets, 252).abs() + 0.02)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC change minus capex growth (slope of base)
def f40cc_f40_capital_cycle_signal_roicvscapexg_21d_slope_v103_signal(roic, capex):
    base = _chg(roic, 252) - _growth(capex, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC change minus capex growth (slope of base)
def f40cc_f40_capital_cycle_signal_roicvscapexg_63d_slope_v104_signal(roic, capex):
    base = _chg(roic, 252) - _growth(capex, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC change minus capex growth (slope of base)
def f40cc_f40_capital_cycle_signal_roicvscapexg_126d_slope_v105_signal(roic, capex):
    base = _chg(roic, 252) - _growth(capex, 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex growth minus ROIC change (504d) (slope of base)
def f40cc_f40_capital_cycle_signal_capexgvsret_21d_slope_v106_signal(capex, roic):
    base = _growth(capex, 504) - _chg(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex growth minus ROIC change (504d) (slope of base)
def f40cc_f40_capital_cycle_signal_capexgvsret_63d_slope_v107_signal(capex, roic):
    base = _growth(capex, 504) - _chg(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex growth minus ROIC change (504d) (slope of base)
def f40cc_f40_capital_cycle_signal_capexgvsret_126d_slope_v108_signal(capex, roic):
    base = _growth(capex, 504) - _chg(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap-minus-asset build gated by low ROIC (slope of base)
def f40cc_f40_capital_cycle_signal_invcapmixlow_21d_slope_v109_signal(invcap, assets, roic):
    base = (_invcap_growth(invcap, 252) - _asset_growth(assets, 252)) * (1.0 + 4.0 * _roic_below_hurdle(roic))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap-minus-asset build gated by low ROIC (slope of base)
def f40cc_f40_capital_cycle_signal_invcapmixlow_63d_slope_v110_signal(invcap, assets, roic):
    base = (_invcap_growth(invcap, 252) - _asset_growth(assets, 252)) * (1.0 + 4.0 * _roic_below_hurdle(roic))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap-minus-asset build gated by low ROIC (slope of base)
def f40cc_f40_capital_cycle_signal_invcapmixlow_126d_slope_v111_signal(invcap, assets, roic):
    base = (_invcap_growth(invcap, 252) - _asset_growth(assets, 252)) * (1.0 + 4.0 * _roic_below_hurdle(roic))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC mid-cycle gap scaled by build pace (slope of base)
def f40cc_f40_capital_cycle_signal_roicmidgapxbuild_21d_slope_v112_signal(roic, invcap):
    base = (roic - _mean(roic, 1260)) * (1.0 + np.tanh(8.0 * _invcap_growth(invcap, 252)).clip(lower=0))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC mid-cycle gap scaled by build pace (slope of base)
def f40cc_f40_capital_cycle_signal_roicmidgapxbuild_63d_slope_v113_signal(roic, invcap):
    base = (roic - _mean(roic, 1260)) * (1.0 + np.tanh(8.0 * _invcap_growth(invcap, 252)).clip(lower=0))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC mid-cycle gap scaled by build pace (slope of base)
def f40cc_f40_capital_cycle_signal_roicmidgapxbuild_126d_slope_v114_signal(roic, invcap):
    base = (roic - _mean(roic, 1260)) * (1.0 + np.tanh(8.0 * _invcap_growth(invcap, 252)).clip(lower=0))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex/invcap z minus ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_capexinvcapvsret_21d_slope_v115_signal(capex, invcap, roic):
    base = _z(capex / invcap.replace(0, np.nan), 252) - _z(roic, 252)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex/invcap z minus ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_capexinvcapvsret_63d_slope_v116_signal(capex, invcap, roic):
    base = _z(capex / invcap.replace(0, np.nan), 252) - _z(roic, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex/invcap z minus ROIC z (slope of base)
def f40cc_f40_capital_cycle_signal_capexinvcapvsret_126d_slope_v117_signal(capex, invcap, roic):
    base = _z(capex / invcap.replace(0, np.nan), 252) - _z(roic, 252)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# joint extremity: |capex z| x |ROIC z| (slope of base)
def f40cc_f40_capital_cycle_signal_jointextreme_21d_slope_v118_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 504).abs() * _z(roic, 504).abs()
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# joint extremity: |capex z| x |ROIC z| (slope of base)
def f40cc_f40_capital_cycle_signal_jointextreme_63d_slope_v119_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 504).abs() * _z(roic, 504).abs()
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# joint extremity: |capex z| x |ROIC z| (slope of base)
def f40cc_f40_capital_cycle_signal_jointextreme_126d_slope_v120_signal(capex, assets, roic):
    base = _z(_capex_intensity(capex, assets), 504).abs() * _z(roic, 504).abs()
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# build-minus-return divergence ranked (slope of base)
def f40cc_f40_capital_cycle_signal_buildretrank_21d_slope_v121_signal(assets, roic):
    base = _rank(_build_minus_return(_asset_growth(assets, 252), roic, 252), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# build-minus-return divergence ranked (slope of base)
def f40cc_f40_capital_cycle_signal_buildretrank_63d_slope_v122_signal(assets, roic):
    base = _rank(_build_minus_return(_asset_growth(assets, 252), roic, 252), 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# build-minus-return divergence ranked (slope of base)
def f40cc_f40_capital_cycle_signal_buildretrank_126d_slope_v123_signal(assets, roic):
    base = _rank(_build_minus_return(_asset_growth(assets, 252), roic, 252), 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap-growth rank minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_invgvsroicrank_21d_slope_v124_signal(invcap, roic):
    base = _rank(_invcap_growth(invcap, 252), 504) - _rank(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap-growth rank minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_invgvsroicrank_63d_slope_v125_signal(invcap, roic):
    base = _rank(_invcap_growth(invcap, 252), 504) - _rank(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap-growth rank minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_invgvsroicrank_126d_slope_v126_signal(invcap, roic):
    base = _rank(_invcap_growth(invcap, 252), 504) - _rank(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# reinvestment-rate rank minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_reinvvsroicrank_21d_slope_v127_signal(capex, ppnenet, roic):
    base = _rank(_capex_to_ppne(capex, ppnenet), 504) - _rank(roic, 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# reinvestment-rate rank minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_reinvvsroicrank_63d_slope_v128_signal(capex, ppnenet, roic):
    base = _rank(_capex_to_ppne(capex, ppnenet), 504) - _rank(roic, 504)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# reinvestment-rate rank minus ROIC rank (slope of base)
def f40cc_f40_capital_cycle_signal_reinvvsroicrank_126d_slope_v129_signal(capex, ppnenet, roic):
    base = _rank(_capex_to_ppne(capex, ppnenet), 504) - _rank(roic, 504)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex-trend vs ROIC-trend sign co-movement (slope of base)
def f40cc_f40_capital_cycle_signal_capexcotrend_21d_slope_v130_signal(roic, capex, assets):
    ci = _capex_intensity(capex, assets)
    dr = _chg(roic, 252)
    dci = ci - ci.shift(252)
    base = np.sign(dr) * np.sign(dci) * (dr.abs() + dci.abs())
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex-trend vs ROIC-trend sign co-movement (slope of base)
def f40cc_f40_capital_cycle_signal_capexcotrend_63d_slope_v131_signal(roic, capex, assets):
    ci = _capex_intensity(capex, assets)
    dr = _chg(roic, 252)
    dci = ci - ci.shift(252)
    base = np.sign(dr) * np.sign(dci) * (dr.abs() + dci.abs())
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex-trend vs ROIC-trend sign co-movement (slope of base)
def f40cc_f40_capital_cycle_signal_capexcotrend_126d_slope_v132_signal(roic, capex, assets):
    ci = _capex_intensity(capex, assets)
    dr = _chg(roic, 252)
    dci = ci - ci.shift(252)
    base = np.sign(dr) * np.sign(dci) * (dr.abs() + dci.abs())
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex acceleration x ROIC deceleration warning (slope of base)
def f40cc_f40_capital_cycle_signal_warningsign_21d_slope_v133_signal(capex, roic):
    cacc = _growth(capex, 126) - _growth(capex, 126).shift(126)
    base = np.tanh(8.0 * cacc) * np.tanh(-4.0 * _chg(roic, 126))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex acceleration x ROIC deceleration warning (slope of base)
def f40cc_f40_capital_cycle_signal_warningsign_63d_slope_v134_signal(capex, roic):
    cacc = _growth(capex, 126) - _growth(capex, 126).shift(126)
    base = np.tanh(8.0 * cacc) * np.tanh(-4.0 * _chg(roic, 126))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex acceleration x ROIC deceleration warning (slope of base)
def f40cc_f40_capital_cycle_signal_warningsign_126d_slope_v135_signal(capex, roic):
    cacc = _growth(capex, 126) - _growth(capex, 126).shift(126)
    base = np.tanh(8.0 * cacc) * np.tanh(-4.0 * _chg(roic, 126))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset-growth z x tanh ROIC-below-mid-cycle (slope of base)
def f40cc_f40_capital_cycle_signal_misalloc2_21d_slope_v136_signal(assets, roic):
    base = _z(_asset_growth(assets, 252), 504) * np.tanh(6.0 * (_mean(roic, 1260) - roic).clip(lower=-0.05))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset-growth z x tanh ROIC-below-mid-cycle (slope of base)
def f40cc_f40_capital_cycle_signal_misalloc2_63d_slope_v137_signal(assets, roic):
    base = _z(_asset_growth(assets, 252), 504) * np.tanh(6.0 * (_mean(roic, 1260) - roic).clip(lower=-0.05))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# asset-growth z x tanh ROIC-below-mid-cycle (slope of base)
def f40cc_f40_capital_cycle_signal_misalloc2_126d_slope_v138_signal(assets, roic):
    base = _z(_asset_growth(assets, 252), 504) * np.tanh(6.0 * (_mean(roic, 1260) - roic).clip(lower=-0.05))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex cut x rising ROIC (capitulation payoff) (slope of base)
def f40cc_f40_capital_cycle_signal_cutthenpay_21d_slope_v139_signal(capex, roic):
    cut = capex / _rmax(capex, 504).replace(0, np.nan) - 1.0
    base = (-cut) * np.tanh(5.0 * _chg(roic, 126))
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex cut x rising ROIC (capitulation payoff) (slope of base)
def f40cc_f40_capital_cycle_signal_cutthenpay_63d_slope_v140_signal(capex, roic):
    cut = capex / _rmax(capex, 504).replace(0, np.nan) - 1.0
    base = (-cut) * np.tanh(5.0 * _chg(roic, 126))
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex cut x rising ROIC (capitulation payoff) (slope of base)
def f40cc_f40_capital_cycle_signal_cutthenpay_126d_slope_v141_signal(capex, roic):
    cut = capex / _rmax(capex, 504).replace(0, np.nan) - 1.0
    base = (-cut) * np.tanh(5.0 * _chg(roic, 126))
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap phase minus ROIC phase (1260d) (slope of base)
def f40cc_f40_capital_cycle_signal_capvsretphase_21d_slope_v142_signal(invcap, roic):
    ipos = (invcap - _rmin(invcap, 1260)) / (_rmax(invcap, 1260) - _rmin(invcap, 1260)).replace(0, np.nan)
    rpos = (roic - _rmin(roic, 1260)) / (_rmax(roic, 1260) - _rmin(roic, 1260)).replace(0, np.nan)
    base = ipos - rpos
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap phase minus ROIC phase (1260d) (slope of base)
def f40cc_f40_capital_cycle_signal_capvsretphase_63d_slope_v143_signal(invcap, roic):
    ipos = (invcap - _rmin(invcap, 1260)) / (_rmax(invcap, 1260) - _rmin(invcap, 1260)).replace(0, np.nan)
    rpos = (roic - _rmin(roic, 1260)) / (_rmax(roic, 1260) - _rmin(roic, 1260)).replace(0, np.nan)
    base = ipos - rpos
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# invcap phase minus ROIC phase (1260d) (slope of base)
def f40cc_f40_capital_cycle_signal_capvsretphase_126d_slope_v144_signal(invcap, roic):
    ipos = (invcap - _rmin(invcap, 1260)) / (_rmax(invcap, 1260) - _rmin(invcap, 1260)).replace(0, np.nan)
    rpos = (roic - _rmin(roic, 1260)) / (_rmax(roic, 1260) - _rmin(roic, 1260)).replace(0, np.nan)
    base = ipos - rpos
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC mean per capex-intensity mean (slope of base)
def f40cc_f40_capital_cycle_signal_retperbuildlvl_21d_slope_v145_signal(roic, capex, assets):
    base = _mean(roic, 252) / (_mean(_capex_intensity(capex, assets), 252) + 0.005)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC mean per capex-intensity mean (slope of base)
def f40cc_f40_capital_cycle_signal_retperbuildlvl_63d_slope_v146_signal(roic, capex, assets):
    base = _mean(roic, 252) / (_mean(_capex_intensity(capex, assets), 252) + 0.005)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# ROIC mean per capex-intensity mean (slope of base)
def f40cc_f40_capital_cycle_signal_retperbuildlvl_126d_slope_v147_signal(roic, capex, assets):
    base = _mean(roic, 252) / (_mean(_capex_intensity(capex, assets), 252) + 0.005)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex momentum minus ROIC momentum (slope of base)
def f40cc_f40_capital_cycle_signal_capexvsroiccross_21d_slope_v148_signal(capex, assets, roic):
    ci = _capex_intensity(capex, assets)
    cmom = (ci.ewm(span=63, min_periods=21).mean() - ci.ewm(span=252, min_periods=126).mean()) / ci.ewm(span=252, min_periods=126).mean().replace(0, np.nan)
    rmom = roic.ewm(span=63, min_periods=21).mean() - roic.ewm(span=252, min_periods=126).mean()
    base = cmom - np.tanh(5.0 * rmom)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex momentum minus ROIC momentum (slope of base)
def f40cc_f40_capital_cycle_signal_capexvsroiccross_63d_slope_v149_signal(capex, assets, roic):
    ci = _capex_intensity(capex, assets)
    cmom = (ci.ewm(span=63, min_periods=21).mean() - ci.ewm(span=252, min_periods=126).mean()) / ci.ewm(span=252, min_periods=126).mean().replace(0, np.nan)
    rmom = roic.ewm(span=63, min_periods=21).mean() - roic.ewm(span=252, min_periods=126).mean()
    base = cmom - np.tanh(5.0 * rmom)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)

# capex momentum minus ROIC momentum (slope of base)
def f40cc_f40_capital_cycle_signal_capexvsroiccross_126d_slope_v150_signal(capex, assets, roic):
    ci = _capex_intensity(capex, assets)
    cmom = (ci.ewm(span=63, min_periods=21).mean() - ci.ewm(span=252, min_periods=126).mean()) / ci.ewm(span=252, min_periods=126).mean().replace(0, np.nan)
    rmom = roic.ewm(span=63, min_periods=21).mean() - roic.ewm(span=252, min_periods=126).mean()
    base = cmom - np.tanh(5.0 * rmom)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40cc_f40_capital_cycle_signal_buildretz_21d_slope_v001_signal,
    f40cc_f40_capital_cycle_signal_buildretz_63d_slope_v002_signal,
    f40cc_f40_capital_cycle_signal_buildretz_126d_slope_v003_signal,
    f40cc_f40_capital_cycle_signal_assetgvsret_21d_slope_v004_signal,
    f40cc_f40_capital_cycle_signal_assetgvsret_63d_slope_v005_signal,
    f40cc_f40_capital_cycle_signal_assetgvsret_126d_slope_v006_signal,
    f40cc_f40_capital_cycle_signal_invcapgvsroic_21d_slope_v007_signal,
    f40cc_f40_capital_cycle_signal_invcapgvsroic_63d_slope_v008_signal,
    f40cc_f40_capital_cycle_signal_invcapgvsroic_126d_slope_v009_signal,
    f40cc_f40_capital_cycle_signal_reinvminroic_21d_slope_v010_signal,
    f40cc_f40_capital_cycle_signal_reinvminroic_63d_slope_v011_signal,
    f40cc_f40_capital_cycle_signal_reinvminroic_126d_slope_v012_signal,
    f40cc_f40_capital_cycle_signal_ppnegvsret_21d_slope_v013_signal,
    f40cc_f40_capital_cycle_signal_ppnegvsret_63d_slope_v014_signal,
    f40cc_f40_capital_cycle_signal_ppnegvsret_126d_slope_v015_signal,
    f40cc_f40_capital_cycle_signal_misalloc_21d_slope_v016_signal,
    f40cc_f40_capital_cycle_signal_misalloc_63d_slope_v017_signal,
    f40cc_f40_capital_cycle_signal_misalloc_126d_slope_v018_signal,
    f40cc_f40_capital_cycle_signal_overbuildtrap_21d_slope_v019_signal,
    f40cc_f40_capital_cycle_signal_overbuildtrap_63d_slope_v020_signal,
    f40cc_f40_capital_cycle_signal_overbuildtrap_126d_slope_v021_signal,
    f40cc_f40_capital_cycle_signal_starvepayoff_21d_slope_v022_signal,
    f40cc_f40_capital_cycle_signal_starvepayoff_63d_slope_v023_signal,
    f40cc_f40_capital_cycle_signal_starvepayoff_126d_slope_v024_signal,
    f40cc_f40_capital_cycle_signal_margroic_21d_slope_v025_signal,
    f40cc_f40_capital_cycle_signal_margroic_63d_slope_v026_signal,
    f40cc_f40_capital_cycle_signal_margroic_126d_slope_v027_signal,
    f40cc_f40_capital_cycle_signal_capexperroic_21d_slope_v028_signal,
    f40cc_f40_capital_cycle_signal_capexperroic_63d_slope_v029_signal,
    f40cc_f40_capital_cycle_signal_capexperroic_126d_slope_v030_signal,
    f40cc_f40_capital_cycle_signal_roicperbuild_21d_slope_v031_signal,
    f40cc_f40_capital_cycle_signal_roicperbuild_63d_slope_v032_signal,
    f40cc_f40_capital_cycle_signal_roicperbuild_126d_slope_v033_signal,
    f40cc_f40_capital_cycle_signal_buildretbounded_21d_slope_v034_signal,
    f40cc_f40_capital_cycle_signal_buildretbounded_63d_slope_v035_signal,
    f40cc_f40_capital_cycle_signal_buildretbounded_126d_slope_v036_signal,
    f40cc_f40_capital_cycle_signal_capexgxroicdec_21d_slope_v037_signal,
    f40cc_f40_capital_cycle_signal_capexgxroicdec_63d_slope_v038_signal,
    f40cc_f40_capital_cycle_signal_capexgxroicdec_126d_slope_v039_signal,
    f40cc_f40_capital_cycle_signal_overbuildpen_21d_slope_v040_signal,
    f40cc_f40_capital_cycle_signal_overbuildpen_63d_slope_v041_signal,
    f40cc_f40_capital_cycle_signal_overbuildpen_126d_slope_v042_signal,
    f40cc_f40_capital_cycle_signal_tighteningpay_21d_slope_v043_signal,
    f40cc_f40_capital_cycle_signal_tighteningpay_63d_slope_v044_signal,
    f40cc_f40_capital_cycle_signal_tighteningpay_126d_slope_v045_signal,
    f40cc_f40_capital_cycle_signal_cyclescore_21d_slope_v046_signal,
    f40cc_f40_capital_cycle_signal_cyclescore_63d_slope_v047_signal,
    f40cc_f40_capital_cycle_signal_cyclescore_126d_slope_v048_signal,
    f40cc_f40_capital_cycle_signal_reinvretz_21d_slope_v049_signal,
    f40cc_f40_capital_cycle_signal_reinvretz_63d_slope_v050_signal,
    f40cc_f40_capital_cycle_signal_reinvretz_126d_slope_v051_signal,
    f40cc_f40_capital_cycle_signal_ppneintvsroic_21d_slope_v052_signal,
    f40cc_f40_capital_cycle_signal_ppneintvsroic_63d_slope_v053_signal,
    f40cc_f40_capital_cycle_signal_ppneintvsroic_126d_slope_v054_signal,
    f40cc_f40_capital_cycle_signal_invcapintvsroic_21d_slope_v055_signal,
    f40cc_f40_capital_cycle_signal_invcapintvsroic_63d_slope_v056_signal,
    f40cc_f40_capital_cycle_signal_invcapintvsroic_126d_slope_v057_signal,
    f40cc_f40_capital_cycle_signal_buildretema_21d_slope_v058_signal,
    f40cc_f40_capital_cycle_signal_buildretema_63d_slope_v059_signal,
    f40cc_f40_capital_cycle_signal_buildretema_126d_slope_v060_signal,
    f40cc_f40_capital_cycle_signal_favstarve_21d_slope_v061_signal,
    f40cc_f40_capital_cycle_signal_favstarve_63d_slope_v062_signal,
    f40cc_f40_capital_cycle_signal_favstarve_126d_slope_v063_signal,
    f40cc_f40_capital_cycle_signal_steadybuildret_21d_slope_v064_signal,
    f40cc_f40_capital_cycle_signal_steadybuildret_63d_slope_v065_signal,
    f40cc_f40_capital_cycle_signal_steadybuildret_126d_slope_v066_signal,
    f40cc_f40_capital_cycle_signal_roicwhilebuild_21d_slope_v067_signal,
    f40cc_f40_capital_cycle_signal_roicwhilebuild_63d_slope_v068_signal,
    f40cc_f40_capital_cycle_signal_roicwhilebuild_126d_slope_v069_signal,
    f40cc_f40_capital_cycle_signal_starveearn_21d_slope_v070_signal,
    f40cc_f40_capital_cycle_signal_starveearn_63d_slope_v071_signal,
    f40cc_f40_capital_cycle_signal_starveearn_126d_slope_v072_signal,
    f40cc_f40_capital_cycle_signal_capexcutxret_21d_slope_v073_signal,
    f40cc_f40_capital_cycle_signal_capexcutxret_63d_slope_v074_signal,
    f40cc_f40_capital_cycle_signal_capexcutxret_126d_slope_v075_signal,
    f40cc_f40_capital_cycle_signal_returnspercut_21d_slope_v076_signal,
    f40cc_f40_capital_cycle_signal_returnspercut_63d_slope_v077_signal,
    f40cc_f40_capital_cycle_signal_returnspercut_126d_slope_v078_signal,
    f40cc_f40_capital_cycle_signal_ppnevsroic_21d_slope_v079_signal,
    f40cc_f40_capital_cycle_signal_ppnevsroic_63d_slope_v080_signal,
    f40cc_f40_capital_cycle_signal_ppnevsroic_126d_slope_v081_signal,
    f40cc_f40_capital_cycle_signal_invbuildret_21d_slope_v082_signal,
    f40cc_f40_capital_cycle_signal_invbuildret_63d_slope_v083_signal,
    f40cc_f40_capital_cycle_signal_invbuildret_126d_slope_v084_signal,
    f40cc_f40_capital_cycle_signal_roicddxbuild_21d_slope_v085_signal,
    f40cc_f40_capital_cycle_signal_roicddxbuild_63d_slope_v086_signal,
    f40cc_f40_capital_cycle_signal_roicddxbuild_126d_slope_v087_signal,
    f40cc_f40_capital_cycle_signal_capexampxlow_21d_slope_v088_signal,
    f40cc_f40_capital_cycle_signal_capexampxlow_63d_slope_v089_signal,
    f40cc_f40_capital_cycle_signal_capexampxlow_126d_slope_v090_signal,
    f40cc_f40_capital_cycle_signal_agvsroicrank_21d_slope_v091_signal,
    f40cc_f40_capital_cycle_signal_agvsroicrank_63d_slope_v092_signal,
    f40cc_f40_capital_cycle_signal_agvsroicrank_126d_slope_v093_signal,
    f40cc_f40_capital_cycle_signal_capexvsroicrank_21d_slope_v094_signal,
    f40cc_f40_capital_cycle_signal_capexvsroicrank_63d_slope_v095_signal,
    f40cc_f40_capital_cycle_signal_capexvsroicrank_126d_slope_v096_signal,
    f40cc_f40_capital_cycle_signal_overinvhurdle_21d_slope_v097_signal,
    f40cc_f40_capital_cycle_signal_overinvhurdle_63d_slope_v098_signal,
    f40cc_f40_capital_cycle_signal_overinvhurdle_126d_slope_v099_signal,
    f40cc_f40_capital_cycle_signal_buildpayoff_21d_slope_v100_signal,
    f40cc_f40_capital_cycle_signal_buildpayoff_63d_slope_v101_signal,
    f40cc_f40_capital_cycle_signal_buildpayoff_126d_slope_v102_signal,
    f40cc_f40_capital_cycle_signal_roicvscapexg_21d_slope_v103_signal,
    f40cc_f40_capital_cycle_signal_roicvscapexg_63d_slope_v104_signal,
    f40cc_f40_capital_cycle_signal_roicvscapexg_126d_slope_v105_signal,
    f40cc_f40_capital_cycle_signal_capexgvsret_21d_slope_v106_signal,
    f40cc_f40_capital_cycle_signal_capexgvsret_63d_slope_v107_signal,
    f40cc_f40_capital_cycle_signal_capexgvsret_126d_slope_v108_signal,
    f40cc_f40_capital_cycle_signal_invcapmixlow_21d_slope_v109_signal,
    f40cc_f40_capital_cycle_signal_invcapmixlow_63d_slope_v110_signal,
    f40cc_f40_capital_cycle_signal_invcapmixlow_126d_slope_v111_signal,
    f40cc_f40_capital_cycle_signal_roicmidgapxbuild_21d_slope_v112_signal,
    f40cc_f40_capital_cycle_signal_roicmidgapxbuild_63d_slope_v113_signal,
    f40cc_f40_capital_cycle_signal_roicmidgapxbuild_126d_slope_v114_signal,
    f40cc_f40_capital_cycle_signal_capexinvcapvsret_21d_slope_v115_signal,
    f40cc_f40_capital_cycle_signal_capexinvcapvsret_63d_slope_v116_signal,
    f40cc_f40_capital_cycle_signal_capexinvcapvsret_126d_slope_v117_signal,
    f40cc_f40_capital_cycle_signal_jointextreme_21d_slope_v118_signal,
    f40cc_f40_capital_cycle_signal_jointextreme_63d_slope_v119_signal,
    f40cc_f40_capital_cycle_signal_jointextreme_126d_slope_v120_signal,
    f40cc_f40_capital_cycle_signal_buildretrank_21d_slope_v121_signal,
    f40cc_f40_capital_cycle_signal_buildretrank_63d_slope_v122_signal,
    f40cc_f40_capital_cycle_signal_buildretrank_126d_slope_v123_signal,
    f40cc_f40_capital_cycle_signal_invgvsroicrank_21d_slope_v124_signal,
    f40cc_f40_capital_cycle_signal_invgvsroicrank_63d_slope_v125_signal,
    f40cc_f40_capital_cycle_signal_invgvsroicrank_126d_slope_v126_signal,
    f40cc_f40_capital_cycle_signal_reinvvsroicrank_21d_slope_v127_signal,
    f40cc_f40_capital_cycle_signal_reinvvsroicrank_63d_slope_v128_signal,
    f40cc_f40_capital_cycle_signal_reinvvsroicrank_126d_slope_v129_signal,
    f40cc_f40_capital_cycle_signal_capexcotrend_21d_slope_v130_signal,
    f40cc_f40_capital_cycle_signal_capexcotrend_63d_slope_v131_signal,
    f40cc_f40_capital_cycle_signal_capexcotrend_126d_slope_v132_signal,
    f40cc_f40_capital_cycle_signal_warningsign_21d_slope_v133_signal,
    f40cc_f40_capital_cycle_signal_warningsign_63d_slope_v134_signal,
    f40cc_f40_capital_cycle_signal_warningsign_126d_slope_v135_signal,
    f40cc_f40_capital_cycle_signal_misalloc2_21d_slope_v136_signal,
    f40cc_f40_capital_cycle_signal_misalloc2_63d_slope_v137_signal,
    f40cc_f40_capital_cycle_signal_misalloc2_126d_slope_v138_signal,
    f40cc_f40_capital_cycle_signal_cutthenpay_21d_slope_v139_signal,
    f40cc_f40_capital_cycle_signal_cutthenpay_63d_slope_v140_signal,
    f40cc_f40_capital_cycle_signal_cutthenpay_126d_slope_v141_signal,
    f40cc_f40_capital_cycle_signal_capvsretphase_21d_slope_v142_signal,
    f40cc_f40_capital_cycle_signal_capvsretphase_63d_slope_v143_signal,
    f40cc_f40_capital_cycle_signal_capvsretphase_126d_slope_v144_signal,
    f40cc_f40_capital_cycle_signal_retperbuildlvl_21d_slope_v145_signal,
    f40cc_f40_capital_cycle_signal_retperbuildlvl_63d_slope_v146_signal,
    f40cc_f40_capital_cycle_signal_retperbuildlvl_126d_slope_v147_signal,
    f40cc_f40_capital_cycle_signal_capexvsroiccross_21d_slope_v148_signal,
    f40cc_f40_capital_cycle_signal_capexvsroiccross_63d_slope_v149_signal,
    f40cc_f40_capital_cycle_signal_capexvsroiccross_126d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_CAPITAL_CYCLE_SIGNAL_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    capex = _fund(4001, base=9e7, drift=0.010, vol=0.22).rename("capex")
    assets = _fund(4002, base=1.5e9, drift=0.015, vol=0.06).rename("assets")
    ppnenet = _fund(4003, base=7e8, drift=0.018, vol=0.11).rename("ppnenet")
    invcap = _fund(4004, base=1.0e9, drift=0.012, vol=0.08).rename("invcap")
    roic = _fund(4005, base=0.12, drift=-0.004, vol=0.30, allow_neg=True).rename("roic")

    cols = {"capex": capex, "assets": assets, "ppnenet": ppnenet,
            "invcap": invcap, "roic": roic}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        assert any(c in ("capex", "assets", "ppnenet", "roic", "invcap")
                   for c in meta["inputs"]), name
        assert "roic" in meta["inputs"], "%s missing return leg" % name
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx2 = ai.index.intersection(aj.index)
            if len(idx2) < 30:
                continue
            c = ai.loc[idx2].corr(aj.loc[idx2])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f40_capital_cycle_signal_2nd_derivatives_001_150_claude: %d features pass" % n_features)
