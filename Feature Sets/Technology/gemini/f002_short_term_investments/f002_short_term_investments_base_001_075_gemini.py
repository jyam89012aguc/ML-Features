import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

def _get_liq(cashneq, investmentsc): return cashneq + investmentsc

# core00-09: mean 4q
def cg_f002_short_term_investments_core00_mean_4q_v001_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(investmentsc, 4))
def cg_f002_short_term_investments_core01_mean_4q_v002_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_get_liq(cashneq, investmentsc), 4))
def cg_f002_short_term_investments_core02_mean_4q_v003_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), assets), 4))
def cg_f002_short_term_investments_core03_mean_4q_v004_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 4))
def cg_f002_short_term_investments_core04_mean_4q_v005_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), revenue), 4))
def cg_f002_short_term_investments_core05_mean_4q_v006_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 4))
def cg_f002_short_term_investments_core06_mean_4q_v007_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), debt), 4))
def cg_f002_short_term_investments_core07_mean_4q_v008_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(investmentsc, cashneq + 1.0), 4))
def cg_f002_short_term_investments_core08_mean_4q_v009_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 4))
def cg_f002_short_term_investments_core09_mean_4q_v010_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 4))

# core10-19: mean 8q
def cg_f002_short_term_investments_core10_mean_8q_v011_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(investmentsc, 8))
# ... (Continuing same 10 logics through mean 8q, z 8q, z 20q, rank 12q, rank 20q, pct 1q)
def cg_f002_short_term_investments_core11_mean_8q_v012_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_get_liq(cashneq, investmentsc), 8))
def cg_f002_short_term_investments_core12_mean_8q_v013_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), assets), 8))
def cg_f002_short_term_investments_core13_mean_8q_v014_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 8))
def cg_f002_short_term_investments_core14_mean_8q_v015_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), revenue), 8))
def cg_f002_short_term_investments_core15_mean_8q_v016_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 8))
def cg_f002_short_term_investments_core16_mean_8q_v017_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), debt), 8))
def cg_f002_short_term_investments_core17_mean_8q_v018_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(investmentsc, cashneq + 1.0), 8))
def cg_f002_short_term_investments_core18_mean_8q_v019_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 8))
def cg_f002_short_term_investments_core19_mean_8q_v020_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_mean(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 8))

# core20-29: z 8q
def cg_f002_short_term_investments_core20_z8q_v021_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(investmentsc, 8))
# ... (Continuing)
def cg_f002_short_term_investments_core21_z8q_v022_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_get_liq(cashneq, investmentsc), 8))
def cg_f002_short_term_investments_core22_z8q_v023_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), assets), 8))
def cg_f002_short_term_investments_core23_z8q_v024_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 8))
def cg_f002_short_term_investments_core24_z8q_v025_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), revenue), 8))
def cg_f002_short_term_investments_core25_z8q_v026_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 8))
def cg_f002_short_term_investments_core26_z8q_v027_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), debt), 8))
def cg_f002_short_term_investments_core27_z8q_v028_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(investmentsc, cashneq + 1.0), 8))
def cg_f002_short_term_investments_core28_z8q_v029_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 8))
def cg_f002_short_term_investments_core29_z8q_v030_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 8))

# core30-39: z 20q
def cg_f002_short_term_investments_core30_z20q_v031_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(investmentsc, 20))
def cg_f002_short_term_investments_core31_z20q_v032_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_get_liq(cashneq, investmentsc), 20))
def cg_f002_short_term_investments_core32_z20q_v033_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), assets), 20))
def cg_f002_short_term_investments_core33_z20q_v034_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 20))
def cg_f002_short_term_investments_core34_z20q_v035_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), revenue), 20))
def cg_f002_short_term_investments_core35_z20q_v036_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 20))
def cg_f002_short_term_investments_core36_z20q_v037_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), debt), 20))
def cg_f002_short_term_investments_core37_z20q_v038_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(investmentsc, cashneq + 1.0), 20))
def cg_f002_short_term_investments_core38_z20q_v039_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 20))
def cg_f002_short_term_investments_core39_z20q_v040_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_z(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 20))

# core40-49: rank 12q
def cg_f002_short_term_investments_core40_rank12q_v041_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(investmentsc, 12))
def cg_f002_short_term_investments_core41_rank12q_v042_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_get_liq(cashneq, investmentsc), 12))
def cg_f002_short_term_investments_core42_rank12q_v043_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), assets), 12))
def cg_f002_short_term_investments_core43_rank12q_v044_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 12))
def cg_f002_short_term_investments_core44_rank12q_v045_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), revenue), 12))
def cg_f002_short_term_investments_core45_rank12q_v046_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 12))
def cg_f002_short_term_investments_core46_rank12q_v047_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), debt), 12))
def cg_f002_short_term_investments_core47_rank12q_v048_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(investmentsc, cashneq + 1.0), 12))
def cg_f002_short_term_investments_core48_rank12q_v049_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 12))
def cg_f002_short_term_investments_core49_rank12q_v050_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 12))

# core50-59: rank 20q
def cg_f002_short_term_investments_core50_rank20q_v051_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(investmentsc, 20))
def cg_f002_short_term_investments_core51_rank20q_v052_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_get_liq(cashneq, investmentsc), 20))
def cg_f002_short_term_investments_core52_rank20q_v053_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), assets), 20))
def cg_f002_short_term_investments_core53_rank20q_v054_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 20))
def cg_f002_short_term_investments_core54_rank20q_v055_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), revenue), 20))
def cg_f002_short_term_investments_core55_rank20q_v056_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 20))
def cg_f002_short_term_investments_core56_rank20q_v057_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), debt), 20))
def cg_f002_short_term_investments_core57_rank20q_v058_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(investmentsc, cashneq + 1.0), 20))
def cg_f002_short_term_investments_core58_rank20q_v059_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 20))
def cg_f002_short_term_investments_core59_rank20q_v060_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_rank(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 20))

# core60-69: pct 1q
def cg_f002_short_term_investments_core60_pct1q_v061_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(investmentsc, 1))
def cg_f002_short_term_investments_core61_pct1q_v062_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_get_liq(cashneq, investmentsc), 1))
def cg_f002_short_term_investments_core62_pct1q_v063_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), assets), 1))
def cg_f002_short_term_investments_core63_pct1q_v064_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 1))
def cg_f002_short_term_investments_core64_pct1q_v065_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), revenue), 1))
def cg_f002_short_term_investments_core65_pct1q_v066_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), liabilities), 1))
def cg_f002_short_term_investments_core66_pct1q_v067_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), debt), 1))
def cg_f002_short_term_investments_core67_pct1q_v068_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(investmentsc, cashneq + 1.0), 1))
def cg_f002_short_term_investments_core68_pct1q_v069_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), opex.abs() + 1.0), 1))
def cg_f002_short_term_investments_core69_pct1q_v070_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), capex.abs() + rnd.abs() + 1.0), 1))

# core70-74: pct 4q
def cg_f002_short_term_investments_core70_pct4q_v071_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(investmentsc, 4))
def cg_f002_short_term_investments_core71_pct4q_v072_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_get_liq(cashneq, investmentsc), 4))
def cg_f002_short_term_investments_core72_pct4q_v073_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), assets), 4))
def cg_f002_short_term_investments_core73_pct4q_v074_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), marketcap), 4))
def cg_f002_short_term_investments_core74_pct4q_v075_signal(investmentsc, cashneq, assets, marketcap, revenue, liabilities, debt, capex, rnd, opex):
    return _clean(_pct_change(_safe_div(_get_liq(cashneq, investmentsc), revenue), 4))
