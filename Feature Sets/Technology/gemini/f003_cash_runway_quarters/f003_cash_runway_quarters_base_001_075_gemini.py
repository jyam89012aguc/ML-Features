import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


def _f003_burn(ncfo):
    return (-ncfo).clip(lower=0)


def _f003_runway(cashneq, investmentsc, ncfo):
    burn = (-ncfo).clip(lower=0)
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / burn.replace(0, np.nan)


def _f003_fcf_runway(cashneq, investmentsc, fcf):
    burn = (-fcf).clip(lower=0)
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / burn.replace(0, np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_mean_21d_base_v001_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_mean_63d_base_v002_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_mean_126d_base_v003_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_mean_252d_base_v004_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_mean_504d_base_v005_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_mean_21d_base_v006_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_mean_63d_base_v007_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_mean_126d_base_v008_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_mean_252d_base_v009_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_mean_504d_base_v010_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_mean_21d_base_v011_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_mean_63d_base_v012_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_mean_126d_base_v013_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_mean_252d_base_v014_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_mean_504d_base_v015_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_asset_mean_21d_base_v016_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_asset_mean_63d_base_v017_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_asset_mean_126d_base_v018_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_asset_mean_252d_base_v019_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_asset_mean_504d_base_v020_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_mcap_mean_21d_base_v021_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_mcap_mean_63d_base_v022_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_mcap_mean_126d_base_v023_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_mcap_mean_252d_base_v024_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_mcap_mean_504d_base_v025_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_cash_mean_21d_base_v026_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_cash_mean_63d_base_v027_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_cash_mean_126d_base_v028_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_cash_mean_252d_base_v029_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_cash_mean_504d_base_v030_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_burn_to_mcap_mean_21d_base_v031_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_burn_to_mcap_mean_63d_base_v032_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_burn_to_mcap_mean_126d_base_v033_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_burn_to_mcap_mean_252d_base_v034_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_burn_to_mcap_mean_504d_base_v035_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_median_63d_base_v036_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_median_252d_base_v037_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_median_504d_base_v038_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_median_63d_base_v039_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_median_252d_base_v040_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_median_504d_base_v041_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_median_63d_base_v042_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_median_252d_base_v043_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_median_504d_base_v044_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_asset_median_63d_base_v045_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_asset_median_252d_base_v046_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_asset_median_504d_base_v047_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_mcap_median_63d_base_v048_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_mcap_median_252d_base_v049_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_mcap_median_504d_base_v050_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_cash_median_63d_base_v051_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_cash_median_252d_base_v052_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_cash_median_504d_base_v053_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_burn_to_mcap_median_63d_base_v054_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_burn_to_mcap_median_252d_base_v055_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_burn_to_mcap_median_504d_base_v056_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_rmax_252d_base_v057_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_rmax_504d_base_v058_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_rmax_252d_base_v059_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_rmax_504d_base_v060_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_rmax_252d_base_v061_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_rmax_504d_base_v062_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_asset_rmax_252d_base_v063_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_asset_rmax_504d_base_v064_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_mcap_rmax_252d_base_v065_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_mcap_rmax_504d_base_v066_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_cash_rmax_252d_base_v067_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_to_cash_rmax_504d_base_v068_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_burn_to_mcap_rmax_252d_base_v069_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_burn_to_mcap_rmax_504d_base_v070_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_rmin_252d_base_v071_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_burn_lvl_rmin_504d_base_v072_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_rmin_252d_base_v073_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_runway_rmin_504d_base_v074_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def cg_f003_cash_runway_quarters_fcf_runway_rmin_252d_base_v075_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

