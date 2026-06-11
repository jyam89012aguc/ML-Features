import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f20_capital_alloc_ratio(capex, ncfo, w):
    a = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    b = ncfo.rolling(w, min_periods=max(1, w // 2)).mean()
    return a.abs() / b.abs().replace(0, np.nan)


def _f20_capex_intensity(capex, revenue, w):
    a = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    b = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return a.abs() / b.abs().replace(0, np.nan)


def _f20_capital_alloc_ncff(ncff, w):
    return ncff.rolling(w, min_periods=max(1, w // 2)).mean()


def _make_capex_ncfo_slope(W, ROC):
    def fn(capex, ncfo, closeadj):
        base = _f20_capital_alloc_ratio(capex, ncfo, W) * closeadj
        result = _slope_diff_norm(base, ROC)
        return result.replace([np.inf, -np.inf], np.nan)
    return fn


# Generated below: fully expanded def blocks (no factories used in module).

# 5d slope of 21d capex/ncfo × close
def f20cas_f20_capital_allocation_snapshot_capexratio_21d_slope_v001_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capex/ncfo × close
def f20cas_f20_capital_allocation_snapshot_capexratio_21d_slope_v002_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capex/ncfo
def f20cas_f20_capital_allocation_snapshot_capexratio_63d_slope_v003_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capex/ncfo
def f20cas_f20_capital_allocation_snapshot_capexratio_63d_slope_v004_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d capex/ncfo
def f20cas_f20_capital_allocation_snapshot_capexratio_126d_slope_v005_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d capex/ncfo
def f20cas_f20_capital_allocation_snapshot_capexratio_252d_slope_v006_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capex/ncfo
def f20cas_f20_capital_allocation_snapshot_capexratio_252d_slope_v007_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d capex/ncfo
def f20cas_f20_capital_allocation_snapshot_capexratio_504d_slope_v008_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d capex/ncfo
def f20cas_f20_capital_allocation_snapshot_capexratio_504d_slope_v009_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d capex intensity
def f20cas_f20_capital_allocation_snapshot_capexint_21d_slope_v010_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d capex intensity
def f20cas_f20_capital_allocation_snapshot_capexint_21d_slope_v011_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capex intensity
def f20cas_f20_capital_allocation_snapshot_capexint_63d_slope_v012_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d capex intensity
def f20cas_f20_capital_allocation_snapshot_capexint_63d_slope_v013_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d capex intensity
def f20cas_f20_capital_allocation_snapshot_capexint_126d_slope_v014_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d capex intensity
def f20cas_f20_capital_allocation_snapshot_capexint_252d_slope_v015_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capex intensity
def f20cas_f20_capital_allocation_snapshot_capexint_252d_slope_v016_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d capex intensity
def f20cas_f20_capital_allocation_snapshot_capexint_504d_slope_v017_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d capex intensity
def f20cas_f20_capital_allocation_snapshot_capexint_504d_slope_v018_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ncff × close
def f20cas_f20_capital_allocation_snapshot_ncff_21d_slope_v019_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ncff
def f20cas_f20_capital_allocation_snapshot_ncff_21d_slope_v020_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ncff
def f20cas_f20_capital_allocation_snapshot_ncff_63d_slope_v021_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ncff
def f20cas_f20_capital_allocation_snapshot_ncff_63d_slope_v022_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ncff
def f20cas_f20_capital_allocation_snapshot_ncff_126d_slope_v023_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ncff
def f20cas_f20_capital_allocation_snapshot_ncff_252d_slope_v024_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ncff
def f20cas_f20_capital_allocation_snapshot_ncff_252d_slope_v025_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ncff
def f20cas_f20_capital_allocation_snapshot_ncff_504d_slope_v026_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ncff
def f20cas_f20_capital_allocation_snapshot_ncff_504d_slope_v027_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d retearn growth × close
def f20cas_f20_capital_allocation_snapshot_retearngrow_21d_slope_v028_signal(retearn, capex, ncfo, closeadj):
    base = retearn.pct_change(21) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d retearn growth
def f20cas_f20_capital_allocation_snapshot_retearngrow_63d_slope_v029_signal(retearn, capex, ncfo, closeadj):
    base = retearn.pct_change(63) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 63) * 0.0
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d retearn growth
def f20cas_f20_capital_allocation_snapshot_retearngrow_252d_slope_v030_signal(retearn, capex, ncfo, closeadj):
    base = retearn.pct_change(252) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d retearn growth
def f20cas_f20_capital_allocation_snapshot_retearngrow_504d_slope_v031_signal(retearn, capex, ncfo, closeadj):
    base = retearn.pct_change(504) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex z 252d
def f20cas_f20_capital_allocation_snapshot_capexz_252d_slope_v032_signal(capex, revenue, closeadj):
    base = _z(_f20_capex_intensity(capex, revenue, 63), 252) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex z 504d
def f20cas_f20_capital_allocation_snapshot_capexz_504d_slope_v033_signal(capex, revenue, closeadj):
    base = _z(_f20_capex_intensity(capex, revenue, 252), 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex level 21d
def f20cas_f20_capital_allocation_snapshot_capexlvl_21d_slope_v034_signal(capex, revenue, closeadj):
    base = _mean(capex.abs(), 21) * closeadj + _f20_capex_intensity(capex, revenue, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex level 63d
def f20cas_f20_capital_allocation_snapshot_capexlvl_63d_slope_v035_signal(capex, revenue, closeadj):
    base = _mean(capex.abs(), 63) * closeadj + _f20_capex_intensity(capex, revenue, 63) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex level 252d
def f20cas_f20_capital_allocation_snapshot_capexlvl_252d_slope_v036_signal(capex, revenue, closeadj):
    base = _mean(capex.abs(), 252) * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex level 504d
def f20cas_f20_capital_allocation_snapshot_capexlvl_504d_slope_v037_signal(capex, revenue, closeadj):
    base = _mean(capex.abs(), 504) * closeadj + _f20_capex_intensity(capex, revenue, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of capex growth 21d
def f20cas_f20_capital_allocation_snapshot_capexgrow_21d_slope_v038_signal(capex, ncfo, closeadj):
    base = capex.abs().pct_change(21) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex growth 63d
def f20cas_f20_capital_allocation_snapshot_capexgrow_63d_slope_v039_signal(capex, ncfo, closeadj):
    base = capex.abs().pct_change(63) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 63) * 0.0
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex growth 252d
def f20cas_f20_capital_allocation_snapshot_capexgrow_252d_slope_v040_signal(capex, ncfo, closeadj):
    base = capex.abs().pct_change(252) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex growth 504d
def f20cas_f20_capital_allocation_snapshot_capexgrow_504d_slope_v041_signal(capex, ncfo, closeadj):
    base = capex.abs().pct_change(504) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ncff growth 21d
def f20cas_f20_capital_allocation_snapshot_ncffgrow_21d_slope_v042_signal(ncff, closeadj):
    base = ncff.pct_change(21) * closeadj + _f20_capital_alloc_ncff(ncff, 21) * 0.0
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ncff growth 63d
def f20cas_f20_capital_allocation_snapshot_ncffgrow_63d_slope_v043_signal(ncff, closeadj):
    base = ncff.pct_change(63) * closeadj + _f20_capital_alloc_ncff(ncff, 63) * 0.0
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff growth 252d
def f20cas_f20_capital_allocation_snapshot_ncffgrow_252d_slope_v044_signal(ncff, closeadj):
    base = ncff.pct_change(252) * closeadj + _f20_capital_alloc_ncff(ncff, 252) * 0.0
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex diff 21m252
def f20cas_f20_capital_allocation_snapshot_capexdiff_21m252_slope_v045_signal(capex, ncfo, closeadj):
    base = (_f20_capital_alloc_ratio(capex, ncfo, 21) - _f20_capital_alloc_ratio(capex, ncfo, 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex diff 63m252
def f20cas_f20_capital_allocation_snapshot_capexdiff_63m252_slope_v046_signal(capex, ncfo, closeadj):
    base = (_f20_capital_alloc_ratio(capex, ncfo, 63) - _f20_capital_alloc_ratio(capex, ncfo, 252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capint diff 63m252
def f20cas_f20_capital_allocation_snapshot_capintdiff_63m252_slope_v047_signal(capex, revenue, closeadj):
    base = (_f20_capex_intensity(capex, revenue, 63) - _f20_capex_intensity(capex, revenue, 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capint diff 21m63
def f20cas_f20_capital_allocation_snapshot_capintdiff_21m63_slope_v048_signal(capex, revenue, closeadj):
    base = (_f20_capex_intensity(capex, revenue, 21) - _f20_capex_intensity(capex, revenue, 63)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capint diff 252m504
def f20cas_f20_capital_allocation_snapshot_capintdiff_252m504_slope_v049_signal(capex, revenue, closeadj):
    base = (_f20_capex_intensity(capex, revenue, 252) - _f20_capex_intensity(capex, revenue, 504)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of ncff/ncfo 21d
def f20cas_f20_capital_allocation_snapshot_ncffncfo_21d_slope_v050_signal(ncff, ncfo, closeadj):
    base = (_f20_capital_alloc_ncff(ncff, 21) / _mean(ncfo, 21).abs().replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ncff/ncfo 63d
def f20cas_f20_capital_allocation_snapshot_ncffncfo_63d_slope_v051_signal(ncff, ncfo, closeadj):
    base = (_f20_capital_alloc_ncff(ncff, 63) / _mean(ncfo, 63).abs().replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff/ncfo 252d
def f20cas_f20_capital_allocation_snapshot_ncffncfo_252d_slope_v052_signal(ncff, ncfo, closeadj):
    base = (_f20_capital_alloc_ncff(ncff, 252) / _mean(ncfo, 252).abs().replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff/ncfo 504d
def f20cas_f20_capital_allocation_snapshot_ncffncfo_504d_slope_v053_signal(ncff, ncfo, closeadj):
    base = (_f20_capital_alloc_ncff(ncff, 504) / _mean(ncfo, 504).abs().replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex std 252d
def f20cas_f20_capital_allocation_snapshot_capexstd_252d_slope_v054_signal(capex, ncfo, closeadj):
    base = _std(_f20_capital_alloc_ratio(capex, ncfo, 21), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex std 504d
def f20cas_f20_capital_allocation_snapshot_capexstd_504d_slope_v055_signal(capex, ncfo, closeadj):
    base = _std(_f20_capital_alloc_ratio(capex, ncfo, 63), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex int EMA 21d
def f20cas_f20_capital_allocation_snapshot_capexintema_21d_slope_v056_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex int EMA 63d
def f20cas_f20_capital_allocation_snapshot_capexintema_63d_slope_v057_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex int EMA 252d
def f20cas_f20_capital_allocation_snapshot_capexintema_252d_slope_v058_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/(ncfo+ncff) 252d
def f20cas_f20_capital_allocation_snapshot_capexcap_252d_slope_v059_signal(capex, ncfo, ncff, closeadj):
    base = (_mean(capex.abs(), 252) / _mean(ncfo + ncff, 252).abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ncff(ncff, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/(ncfo+ncff) 63d
def f20cas_f20_capital_allocation_snapshot_capexcap_63d_slope_v060_signal(capex, ncfo, ncff, closeadj):
    base = (_mean(capex.abs(), 63) / _mean(ncfo + ncff, 63).abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ncff(ncff, 63) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of retearn 21d × close
def f20cas_f20_capital_allocation_snapshot_retearn_21d_slope_v061_signal(retearn, capex, revenue, closeadj):
    base = _mean(retearn, 21) * closeadj + _f20_capex_intensity(capex, revenue, 21) * 0.0
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retearn 63d
def f20cas_f20_capital_allocation_snapshot_retearn_63d_slope_v062_signal(retearn, capex, revenue, closeadj):
    base = _mean(retearn, 63) * closeadj + _f20_capex_intensity(capex, revenue, 63) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn 252d
def f20cas_f20_capital_allocation_snapshot_retearn_252d_slope_v063_signal(retearn, capex, revenue, closeadj):
    base = _mean(retearn, 252) * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn 504d
def f20cas_f20_capital_allocation_snapshot_retearn_504d_slope_v064_signal(retearn, capex, revenue, closeadj):
    base = _mean(retearn, 504) * closeadj + _f20_capex_intensity(capex, revenue, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of capex dollar 21d
def f20cas_f20_capital_allocation_snapshot_capexdollar_21d_slope_v065_signal(capex, ncfo, closeadj):
    base = _mean(capex.abs(), 21) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex dollar 252d
def f20cas_f20_capital_allocation_snapshot_capexdollar_252d_slope_v066_signal(capex, ncfo, closeadj):
    base = _mean(capex.abs(), 252) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/assets 252d
def f20cas_f20_capital_allocation_snapshot_capex_assets_252d_slope_v067_signal(capex, assets, ncfo, closeadj):
    base = (_mean(capex.abs(), 252) / _mean(assets, 252).abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/assets 63d
def f20cas_f20_capital_allocation_snapshot_capex_assets_63d_slope_v068_signal(capex, assets, ncfo, closeadj):
    base = (_mean(capex.abs(), 63) / _mean(assets, 63).abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 63) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/equity 252d
def f20cas_f20_capital_allocation_snapshot_capex_equity_252d_slope_v069_signal(capex, equity, ncfo, closeadj):
    base = (_mean(capex.abs(), 252) / _mean(equity, 252).abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/equity 504d
def f20cas_f20_capital_allocation_snapshot_capex_equity_504d_slope_v070_signal(capex, equity, ncfo, closeadj):
    base = (_mean(capex.abs(), 504) / _mean(equity, 504).abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ncff z 252d
def f20cas_f20_capital_allocation_snapshot_ncffz_252d_slope_v071_signal(ncff, closeadj):
    base = _z(_f20_capital_alloc_ncff(ncff, 21), 252) * closeadj
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff z 504d
def f20cas_f20_capital_allocation_snapshot_ncffz_504d_slope_v072_signal(ncff, closeadj):
    base = _z(_f20_capital_alloc_ncff(ncff, 21), 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ncff std 252d
def f20cas_f20_capital_allocation_snapshot_ncffstd_252d_slope_v073_signal(ncff, closeadj):
    base = _std(_f20_capital_alloc_ncff(ncff, 21), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff std 504d
def f20cas_f20_capital_allocation_snapshot_ncffstd_504d_slope_v074_signal(ncff, closeadj):
    base = _std(_f20_capital_alloc_ncff(ncff, 21), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/rev 63d
def f20cas_f20_capital_allocation_snapshot_capexrev_63d_slope_v075_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex × ncff 252d
def f20cas_f20_capital_allocation_snapshot_capexncff_252d_slope_v076_signal(capex, ncff, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    b = _f20_capital_alloc_ncff(ncff, 252).abs()
    base = a * b * closeadj / a.abs().replace(0, np.nan) + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ncff/ncfo diff 21d
def f20cas_f20_capital_allocation_snapshot_ncffncfodiff_21d_slope_v077_signal(ncff, ncfo, closeadj):
    base = (_f20_capital_alloc_ncff(ncff, 21) - _mean(ncfo, 21)) * closeadj / _mean(ncfo, 21).abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ncff/ncfo diff 63d
def f20cas_f20_capital_allocation_snapshot_ncffncfodiff_63d_slope_v078_signal(ncff, ncfo, closeadj):
    base = (_f20_capital_alloc_ncff(ncff, 63) - _mean(ncfo, 63)) * closeadj / _mean(ncfo, 63).abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff/ncfo diff 252d
def f20cas_f20_capital_allocation_snapshot_ncffncfodiff_252d_slope_v079_signal(ncff, ncfo, closeadj):
    base = (_f20_capital_alloc_ncff(ncff, 252) - _mean(ncfo, 252)) * closeadj / _mean(ncfo, 252).abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex × volz 21d
def f20cas_f20_capital_allocation_snapshot_capexvolz_21d_slope_v080_signal(capex, ncfo, closeadj, volume):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21) * _z(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex × volz 63d
def f20cas_f20_capital_allocation_snapshot_capexvolz_63d_slope_v081_signal(capex, ncfo, closeadj, volume):
    base = _f20_capital_alloc_ratio(capex, ncfo, 63) * _z(volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of log capex int 63d
def f20cas_f20_capital_allocation_snapshot_logcapint_63d_slope_v082_signal(capex, revenue, closeadj):
    base = np.log(_f20_capex_intensity(capex, revenue, 63).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log capex int 252d
def f20cas_f20_capital_allocation_snapshot_logcapint_252d_slope_v083_signal(capex, revenue, closeadj):
    base = np.log(_f20_capex_intensity(capex, revenue, 252).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex × dv 252d
def f20cas_f20_capital_allocation_snapshot_capexdv_252d_slope_v084_signal(capex, ncfo, closeadj, volume):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252) * (closeadj * volume)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex × debt 252d
def f20cas_f20_capital_allocation_snapshot_capexdebt_252d_slope_v085_signal(capex, debt, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    db = debt.pct_change(252)
    base = a * db * closeadj / a.abs().replace(0, np.nan) + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of composite 252d
def f20cas_f20_capital_allocation_snapshot_composite_252d_slope_v086_signal(capex, ncfo, ncff, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    b = _f20_capital_alloc_ncff(ncff, 252) / _mean(ncfo, 252).abs().replace(0, np.nan)
    base = (a + b) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex ratio EMA 21d
def f20cas_f20_capital_allocation_snapshot_capexratioema_21d_slope_v087_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex ratio EMA 63d
def f20cas_f20_capital_allocation_snapshot_capexratioema_63d_slope_v088_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex ratio EMA 252d
def f20cas_f20_capital_allocation_snapshot_capexratioema_252d_slope_v089_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ncff EMA 21d
def f20cas_f20_capital_allocation_snapshot_ncffema_21d_slope_v090_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 21).ewm(span=21, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff EMA 63d
def f20cas_f20_capital_allocation_snapshot_ncffema_63d_slope_v091_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 63).ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff EMA 252d
def f20cas_f20_capital_allocation_snapshot_ncffema_252d_slope_v092_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 252).ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex ratio z 252d
def f20cas_f20_capital_allocation_snapshot_capexratioz_252d_slope_v093_signal(capex, ncfo, closeadj):
    base = _z(_f20_capital_alloc_ratio(capex, ncfo, 21), 252) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex ratio z 504d
def f20cas_f20_capital_allocation_snapshot_capexratioz_504d_slope_v094_signal(capex, ncfo, closeadj):
    base = _z(_f20_capital_alloc_ratio(capex, ncfo, 63), 504) * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log capex ratio 252d
def f20cas_f20_capital_allocation_snapshot_logcapexratio_252d_slope_v095_signal(capex, ncfo, closeadj):
    base = np.log(_f20_capital_alloc_ratio(capex, ncfo, 252).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log capex ratio 504d
def f20cas_f20_capital_allocation_snapshot_logcapexratio_504d_slope_v096_signal(capex, ncfo, closeadj):
    base = np.log(_f20_capital_alloc_ratio(capex, ncfo, 504).replace(0, np.nan)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex ratio sq 252d
def f20cas_f20_capital_allocation_snapshot_capexratiosq_252d_slope_v097_signal(capex, ncfo, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    base = a * a * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex int sq 252d
def f20cas_f20_capital_allocation_snapshot_capexintsq_252d_slope_v098_signal(capex, revenue, closeadj):
    a = _f20_capex_intensity(capex, revenue, 252)
    base = a * a * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of compofin 63d
def f20cas_f20_capital_allocation_snapshot_compofin_63d_slope_v099_signal(capex, ncfo, ncff, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 63)
    b = _f20_capital_alloc_ncff(ncff, 63) / _mean(ncfo, 63).abs().replace(0, np.nan)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of compofin 252d
def f20cas_f20_capital_allocation_snapshot_compofin_252d_slope_v100_signal(capex, ncfo, ncff, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    b = _f20_capital_alloc_ncff(ncff, 252) / _mean(ncfo, 252).abs().replace(0, np.nan)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/ncff 252d
def f20cas_f20_capital_allocation_snapshot_capex_ncff_252d_slope_v101_signal(capex, ncff, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    b = _f20_capital_alloc_ncff(ncff, 252)
    base = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/ncff 63d
def f20cas_f20_capital_allocation_snapshot_capex_ncff_63d_slope_v102_signal(capex, ncff, ncfo, closeadj):
    a = _mean(capex.abs(), 63)
    b = _f20_capital_alloc_ncff(ncff, 63)
    base = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 63) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/ncff 504d
def f20cas_f20_capital_allocation_snapshot_capex_ncff_504d_slope_v103_signal(capex, ncff, ncfo, closeadj):
    a = _mean(capex.abs(), 504)
    b = _f20_capital_alloc_ncff(ncff, 504)
    base = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of capex × close 21d
def f20cas_f20_capital_allocation_snapshot_capexpx_21d_slope_v104_signal(capex, ncfo, closeadj):
    base = _mean(capex.abs(), 21) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex × close 504d
def f20cas_f20_capital_allocation_snapshot_capexpx_504d_slope_v105_signal(capex, ncfo, closeadj):
    base = _mean(capex.abs(), 504) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of cap int × close 63d
def f20cas_f20_capital_allocation_snapshot_capintpx_63d_slope_v106_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of cap int × close 504d
def f20cas_f20_capital_allocation_snapshot_capintpx_504d_slope_v107_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff × close 252d
def f20cas_f20_capital_allocation_snapshot_ncffpx_252d_slope_v108_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff × close 504d
def f20cas_f20_capital_allocation_snapshot_ncffpx_504d_slope_v109_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of retearn rate 21d
def f20cas_f20_capital_allocation_snapshot_retearnrate_21d_slope_v110_signal(retearn, capex, revenue, closeadj):
    base = retearn.pct_change(21) * closeadj + _f20_capex_intensity(capex, revenue, 21) * 0.0
    result = _diff(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of retearn rate 63d
def f20cas_f20_capital_allocation_snapshot_retearnrate_63d_slope_v111_signal(retearn, capex, revenue, closeadj):
    base = retearn.pct_change(63) * closeadj + _f20_capex_intensity(capex, revenue, 63) * 0.0
    result = _diff(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn rate 252d
def f20cas_f20_capital_allocation_snapshot_retearnrate_252d_slope_v112_signal(retearn, capex, revenue, closeadj):
    base = retearn.pct_change(252) * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/equity 21d
def f20cas_f20_capital_allocation_snapshot_capex_equity_21d_slope_v113_signal(capex, equity, ncfo, closeadj):
    base = (_mean(capex.abs(), 21) / _mean(equity, 21).abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/equity 63d
def f20cas_f20_capital_allocation_snapshot_capex_equity_63d_slope_v114_signal(capex, equity, ncfo, closeadj):
    base = (_mean(capex.abs(), 63) / _mean(equity, 63).abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 63) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex/assets 504d
def f20cas_f20_capital_allocation_snapshot_capex_assets_504d_slope_v115_signal(capex, assets, ncfo, closeadj):
    base = (_mean(capex.abs(), 504) / _mean(assets, 504).abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex/assets 21d
def f20cas_f20_capital_allocation_snapshot_capex_assets_21d_slope_v116_signal(capex, assets, ncfo, closeadj):
    base = (_mean(capex.abs(), 21) / _mean(assets, 21).abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff × debt 252d
def f20cas_f20_capital_allocation_snapshot_ncffdebt_252d_slope_v117_signal(ncff, debt, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 252)
    db = debt.pct_change(252)
    base = a * db * closeadj / a.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ncff × debt 63d
def f20cas_f20_capital_allocation_snapshot_ncffdebt_63d_slope_v118_signal(ncff, debt, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 63)
    db = debt.pct_change(63)
    base = a * db * closeadj / a.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff × debt 504d
def f20cas_f20_capital_allocation_snapshot_ncffdebt_504d_slope_v119_signal(ncff, debt, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 504)
    db = debt.pct_change(504)
    base = a * db * closeadj / a.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex × ncfo 252d
def f20cas_f20_capital_allocation_snapshot_capexncfo_252d_slope_v120_signal(capex, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    b = _mean(ncfo, 252)
    base = a * b * closeadj / a.abs().replace(0, np.nan) + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn/equity 504d
def f20cas_f20_capital_allocation_snapshot_retearn_equity_504d_slope_v121_signal(retearn, equity, capex, revenue, closeadj):
    base = (_mean(retearn, 504) / _mean(equity, 504).abs().replace(0, np.nan)) * closeadj + _f20_capex_intensity(capex, revenue, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn/equity 252d
def f20cas_f20_capital_allocation_snapshot_retearn_equity_252d_slope_v122_signal(retearn, equity, capex, revenue, closeadj):
    base = (_mean(retearn, 252) / _mean(equity, 252).abs().replace(0, np.nan)) * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearnpx 252d
def f20cas_f20_capital_allocation_snapshot_retearnpx_252d_slope_v123_signal(retearn, capex, revenue, closeadj):
    base = _mean(retearn, 252) * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearnpx 504d
def f20cas_f20_capital_allocation_snapshot_retearnpx_504d_slope_v124_signal(retearn, capex, revenue, closeadj):
    base = _mean(retearn, 504) * closeadj + _f20_capex_intensity(capex, revenue, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of retearnpx 21d
def f20cas_f20_capital_allocation_snapshot_retearnpx_21d_slope_v125_signal(retearn, capex, revenue, closeadj):
    base = _mean(retearn, 21) * closeadj + _f20_capex_intensity(capex, revenue, 21) * 0.0
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn × ncff 252d
def f20cas_f20_capital_allocation_snapshot_retearnxncff_252d_slope_v126_signal(retearn, ncff, closeadj):
    a = retearn.pct_change(252)
    b = _f20_capital_alloc_ncff(ncff, 252)
    base = a * b * closeadj / b.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex × ncff inter 252d
def f20cas_f20_capital_allocation_snapshot_capexncffinter_252d_slope_v127_signal(capex, ncfo, ncff, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    b = _f20_capital_alloc_ncff(ncff, 252)
    base = a * b * closeadj / b.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log cap deploy 252d
def f20cas_f20_capital_allocation_snapshot_logcapdeploy_252d_slope_v128_signal(capex, ncfo, ncff, closeadj):
    base = np.log(_mean(capex.abs() + ncff.abs(), 252).replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of log cap deploy 504d
def f20cas_f20_capital_allocation_snapshot_logcapdeploy_504d_slope_v129_signal(capex, ncfo, ncff, closeadj):
    base = np.log(_mean(capex.abs() + ncff.abs(), 504).replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex ratio range 252d
def f20cas_f20_capital_allocation_snapshot_capexratiorange_252d_slope_v130_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_diff_norm(rng, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex ratio range 504d
def f20cas_f20_capital_allocation_snapshot_capexratiorange_504d_slope_v131_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    rng = (base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()) * closeadj
    result = _slope_diff_norm(rng, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex ratio max 252d
def f20cas_f20_capital_allocation_snapshot_capexratiomax_252d_slope_v132_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21).rolling(252, min_periods=63).max() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex int max 504d
def f20cas_f20_capital_allocation_snapshot_capexintmax_504d_slope_v133_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21).rolling(504, min_periods=126).max() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of cap×assets×debt 252d
def f20cas_f20_capital_allocation_snapshot_capassdebt_252d_slope_v134_signal(capex, assets, debt, ncfo, closeadj):
    a = _mean(capex.abs(), 252) / _mean(assets, 252).abs().replace(0, np.nan)
    db = debt.pct_change(252)
    base = a * db * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex ratio × revenue 21d
def f20cas_f20_capital_allocation_snapshot_capexratiorev_21d_slope_v135_signal(capex, ncfo, revenue, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21) * revenue * closeadj / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex ratio × revenue 252d
def f20cas_f20_capital_allocation_snapshot_capexratiorev_252d_slope_v136_signal(capex, ncfo, revenue, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252) * revenue * closeadj / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex ratio × equity 504d
def f20cas_f20_capital_allocation_snapshot_capexratioequity_504d_slope_v137_signal(capex, ncfo, equity, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 504) * equity * closeadj / equity.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex int volvol 252d
def f20cas_f20_capital_allocation_snapshot_capexintvolvol_252d_slope_v138_signal(capex, revenue, closeadj):
    base = _std(_std(_f20_capex_intensity(capex, revenue, 21), 63), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex int volvol 504d
def f20cas_f20_capital_allocation_snapshot_capexintvolvol_504d_slope_v139_signal(capex, revenue, closeadj):
    base = _std(_std(_f20_capex_intensity(capex, revenue, 21), 252), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of ncff × revenue 252d
def f20cas_f20_capital_allocation_snapshot_ncffrev_252d_slope_v140_signal(ncff, revenue, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 252) * revenue * closeadj / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of ncff × ncfo 63d
def f20cas_f20_capital_allocation_snapshot_ncffncfo63interactor_slope_v141_signal(ncff, ncfo, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 63)
    b = _mean(ncfo, 63)
    base = a * b * closeadj / b.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex int skew 252d
def f20cas_f20_capital_allocation_snapshot_capexintskew_252d_slope_v142_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21).rolling(252, min_periods=63).skew() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex int skew 504d
def f20cas_f20_capital_allocation_snapshot_capexintskew_504d_slope_v143_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21).rolling(504, min_periods=126).skew() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex int kurt 252d
def f20cas_f20_capital_allocation_snapshot_capexintkurt_252d_slope_v144_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21).rolling(252, min_periods=63).kurt() * closeadj
    result = _diff(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex × atr 252d
def f20cas_f20_capital_allocation_snapshot_capexatr_252d_slope_v145_signal(capex, ncfo, closeadj, high, low):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252)
    atr = (high - low).rolling(21, min_periods=5).mean()
    val = base * atr * closeadj / atr.replace(0, np.nan)
    result = _slope_diff_norm(val, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of capex ratio × dv 21d
def f20cas_f20_capital_allocation_snapshot_capexratiodv_21d_slope_v146_signal(capex, ncfo, closeadj, volume):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21) * (closeadj * volume)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of capex int × dv 252d
def f20cas_f20_capital_allocation_snapshot_capexintdv_252d_slope_v147_signal(capex, revenue, closeadj, volume):
    base = _f20_capex_intensity(capex, revenue, 252) * (closeadj * volume)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn vol 252d
def f20cas_f20_capital_allocation_snapshot_retearnvol_252d_slope_v148_signal(retearn, capex, revenue, closeadj):
    base = _std(_mean(retearn, 21), 252) * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of retearn vol 504d
def f20cas_f20_capital_allocation_snapshot_retearnvol_504d_slope_v149_signal(retearn, capex, revenue, closeadj):
    base = _std(_mean(retearn, 21), 504) * closeadj + _f20_capex_intensity(capex, revenue, 504) * 0.0
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of compositesnp 252d
def f20cas_f20_capital_allocation_snapshot_compositesnp_252d_slope_v150_signal(capex, ncfo, retearn, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    b = retearn.pct_change(252)
    base = (a + b) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20cas_f20_capital_allocation_snapshot_capexratio_21d_slope_v001_signal,
    f20cas_f20_capital_allocation_snapshot_capexratio_21d_slope_v002_signal,
    f20cas_f20_capital_allocation_snapshot_capexratio_63d_slope_v003_signal,
    f20cas_f20_capital_allocation_snapshot_capexratio_63d_slope_v004_signal,
    f20cas_f20_capital_allocation_snapshot_capexratio_126d_slope_v005_signal,
    f20cas_f20_capital_allocation_snapshot_capexratio_252d_slope_v006_signal,
    f20cas_f20_capital_allocation_snapshot_capexratio_252d_slope_v007_signal,
    f20cas_f20_capital_allocation_snapshot_capexratio_504d_slope_v008_signal,
    f20cas_f20_capital_allocation_snapshot_capexratio_504d_slope_v009_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_21d_slope_v010_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_21d_slope_v011_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_63d_slope_v012_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_63d_slope_v013_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_126d_slope_v014_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_252d_slope_v015_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_252d_slope_v016_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_504d_slope_v017_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_504d_slope_v018_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_21d_slope_v019_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_21d_slope_v020_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_63d_slope_v021_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_63d_slope_v022_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_126d_slope_v023_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_252d_slope_v024_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_252d_slope_v025_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_504d_slope_v026_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_504d_slope_v027_signal,
    f20cas_f20_capital_allocation_snapshot_retearngrow_21d_slope_v028_signal,
    f20cas_f20_capital_allocation_snapshot_retearngrow_63d_slope_v029_signal,
    f20cas_f20_capital_allocation_snapshot_retearngrow_252d_slope_v030_signal,
    f20cas_f20_capital_allocation_snapshot_retearngrow_504d_slope_v031_signal,
    f20cas_f20_capital_allocation_snapshot_capexz_252d_slope_v032_signal,
    f20cas_f20_capital_allocation_snapshot_capexz_504d_slope_v033_signal,
    f20cas_f20_capital_allocation_snapshot_capexlvl_21d_slope_v034_signal,
    f20cas_f20_capital_allocation_snapshot_capexlvl_63d_slope_v035_signal,
    f20cas_f20_capital_allocation_snapshot_capexlvl_252d_slope_v036_signal,
    f20cas_f20_capital_allocation_snapshot_capexlvl_504d_slope_v037_signal,
    f20cas_f20_capital_allocation_snapshot_capexgrow_21d_slope_v038_signal,
    f20cas_f20_capital_allocation_snapshot_capexgrow_63d_slope_v039_signal,
    f20cas_f20_capital_allocation_snapshot_capexgrow_252d_slope_v040_signal,
    f20cas_f20_capital_allocation_snapshot_capexgrow_504d_slope_v041_signal,
    f20cas_f20_capital_allocation_snapshot_ncffgrow_21d_slope_v042_signal,
    f20cas_f20_capital_allocation_snapshot_ncffgrow_63d_slope_v043_signal,
    f20cas_f20_capital_allocation_snapshot_ncffgrow_252d_slope_v044_signal,
    f20cas_f20_capital_allocation_snapshot_capexdiff_21m252_slope_v045_signal,
    f20cas_f20_capital_allocation_snapshot_capexdiff_63m252_slope_v046_signal,
    f20cas_f20_capital_allocation_snapshot_capintdiff_63m252_slope_v047_signal,
    f20cas_f20_capital_allocation_snapshot_capintdiff_21m63_slope_v048_signal,
    f20cas_f20_capital_allocation_snapshot_capintdiff_252m504_slope_v049_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfo_21d_slope_v050_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfo_63d_slope_v051_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfo_252d_slope_v052_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfo_504d_slope_v053_signal,
    f20cas_f20_capital_allocation_snapshot_capexstd_252d_slope_v054_signal,
    f20cas_f20_capital_allocation_snapshot_capexstd_504d_slope_v055_signal,
    f20cas_f20_capital_allocation_snapshot_capexintema_21d_slope_v056_signal,
    f20cas_f20_capital_allocation_snapshot_capexintema_63d_slope_v057_signal,
    f20cas_f20_capital_allocation_snapshot_capexintema_252d_slope_v058_signal,
    f20cas_f20_capital_allocation_snapshot_capexcap_252d_slope_v059_signal,
    f20cas_f20_capital_allocation_snapshot_capexcap_63d_slope_v060_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_21d_slope_v061_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_63d_slope_v062_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_252d_slope_v063_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_504d_slope_v064_signal,
    f20cas_f20_capital_allocation_snapshot_capexdollar_21d_slope_v065_signal,
    f20cas_f20_capital_allocation_snapshot_capexdollar_252d_slope_v066_signal,
    f20cas_f20_capital_allocation_snapshot_capex_assets_252d_slope_v067_signal,
    f20cas_f20_capital_allocation_snapshot_capex_assets_63d_slope_v068_signal,
    f20cas_f20_capital_allocation_snapshot_capex_equity_252d_slope_v069_signal,
    f20cas_f20_capital_allocation_snapshot_capex_equity_504d_slope_v070_signal,
    f20cas_f20_capital_allocation_snapshot_ncffz_252d_slope_v071_signal,
    f20cas_f20_capital_allocation_snapshot_ncffz_504d_slope_v072_signal,
    f20cas_f20_capital_allocation_snapshot_ncffstd_252d_slope_v073_signal,
    f20cas_f20_capital_allocation_snapshot_ncffstd_504d_slope_v074_signal,
    f20cas_f20_capital_allocation_snapshot_capexrev_63d_slope_v075_signal,
    f20cas_f20_capital_allocation_snapshot_capexncff_252d_slope_v076_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfodiff_21d_slope_v077_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfodiff_63d_slope_v078_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfodiff_252d_slope_v079_signal,
    f20cas_f20_capital_allocation_snapshot_capexvolz_21d_slope_v080_signal,
    f20cas_f20_capital_allocation_snapshot_capexvolz_63d_slope_v081_signal,
    f20cas_f20_capital_allocation_snapshot_logcapint_63d_slope_v082_signal,
    f20cas_f20_capital_allocation_snapshot_logcapint_252d_slope_v083_signal,
    f20cas_f20_capital_allocation_snapshot_capexdv_252d_slope_v084_signal,
    f20cas_f20_capital_allocation_snapshot_capexdebt_252d_slope_v085_signal,
    f20cas_f20_capital_allocation_snapshot_composite_252d_slope_v086_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioema_21d_slope_v087_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioema_63d_slope_v088_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioema_252d_slope_v089_signal,
    f20cas_f20_capital_allocation_snapshot_ncffema_21d_slope_v090_signal,
    f20cas_f20_capital_allocation_snapshot_ncffema_63d_slope_v091_signal,
    f20cas_f20_capital_allocation_snapshot_ncffema_252d_slope_v092_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioz_252d_slope_v093_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioz_504d_slope_v094_signal,
    f20cas_f20_capital_allocation_snapshot_logcapexratio_252d_slope_v095_signal,
    f20cas_f20_capital_allocation_snapshot_logcapexratio_504d_slope_v096_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiosq_252d_slope_v097_signal,
    f20cas_f20_capital_allocation_snapshot_capexintsq_252d_slope_v098_signal,
    f20cas_f20_capital_allocation_snapshot_compofin_63d_slope_v099_signal,
    f20cas_f20_capital_allocation_snapshot_compofin_252d_slope_v100_signal,
    f20cas_f20_capital_allocation_snapshot_capex_ncff_252d_slope_v101_signal,
    f20cas_f20_capital_allocation_snapshot_capex_ncff_63d_slope_v102_signal,
    f20cas_f20_capital_allocation_snapshot_capex_ncff_504d_slope_v103_signal,
    f20cas_f20_capital_allocation_snapshot_capexpx_21d_slope_v104_signal,
    f20cas_f20_capital_allocation_snapshot_capexpx_504d_slope_v105_signal,
    f20cas_f20_capital_allocation_snapshot_capintpx_63d_slope_v106_signal,
    f20cas_f20_capital_allocation_snapshot_capintpx_504d_slope_v107_signal,
    f20cas_f20_capital_allocation_snapshot_ncffpx_252d_slope_v108_signal,
    f20cas_f20_capital_allocation_snapshot_ncffpx_504d_slope_v109_signal,
    f20cas_f20_capital_allocation_snapshot_retearnrate_21d_slope_v110_signal,
    f20cas_f20_capital_allocation_snapshot_retearnrate_63d_slope_v111_signal,
    f20cas_f20_capital_allocation_snapshot_retearnrate_252d_slope_v112_signal,
    f20cas_f20_capital_allocation_snapshot_capex_equity_21d_slope_v113_signal,
    f20cas_f20_capital_allocation_snapshot_capex_equity_63d_slope_v114_signal,
    f20cas_f20_capital_allocation_snapshot_capex_assets_504d_slope_v115_signal,
    f20cas_f20_capital_allocation_snapshot_capex_assets_21d_slope_v116_signal,
    f20cas_f20_capital_allocation_snapshot_ncffdebt_252d_slope_v117_signal,
    f20cas_f20_capital_allocation_snapshot_ncffdebt_63d_slope_v118_signal,
    f20cas_f20_capital_allocation_snapshot_ncffdebt_504d_slope_v119_signal,
    f20cas_f20_capital_allocation_snapshot_capexncfo_252d_slope_v120_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_equity_504d_slope_v121_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_equity_252d_slope_v122_signal,
    f20cas_f20_capital_allocation_snapshot_retearnpx_252d_slope_v123_signal,
    f20cas_f20_capital_allocation_snapshot_retearnpx_504d_slope_v124_signal,
    f20cas_f20_capital_allocation_snapshot_retearnpx_21d_slope_v125_signal,
    f20cas_f20_capital_allocation_snapshot_retearnxncff_252d_slope_v126_signal,
    f20cas_f20_capital_allocation_snapshot_capexncffinter_252d_slope_v127_signal,
    f20cas_f20_capital_allocation_snapshot_logcapdeploy_252d_slope_v128_signal,
    f20cas_f20_capital_allocation_snapshot_logcapdeploy_504d_slope_v129_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiorange_252d_slope_v130_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiorange_504d_slope_v131_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiomax_252d_slope_v132_signal,
    f20cas_f20_capital_allocation_snapshot_capexintmax_504d_slope_v133_signal,
    f20cas_f20_capital_allocation_snapshot_capassdebt_252d_slope_v134_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiorev_21d_slope_v135_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiorev_252d_slope_v136_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioequity_504d_slope_v137_signal,
    f20cas_f20_capital_allocation_snapshot_capexintvolvol_252d_slope_v138_signal,
    f20cas_f20_capital_allocation_snapshot_capexintvolvol_504d_slope_v139_signal,
    f20cas_f20_capital_allocation_snapshot_ncffrev_252d_slope_v140_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfo63interactor_slope_v141_signal,
    f20cas_f20_capital_allocation_snapshot_capexintskew_252d_slope_v142_signal,
    f20cas_f20_capital_allocation_snapshot_capexintskew_504d_slope_v143_signal,
    f20cas_f20_capital_allocation_snapshot_capexintkurt_252d_slope_v144_signal,
    f20cas_f20_capital_allocation_snapshot_capexatr_252d_slope_v145_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiodv_21d_slope_v146_signal,
    f20cas_f20_capital_allocation_snapshot_capexintdv_252d_slope_v147_signal,
    f20cas_f20_capital_allocation_snapshot_retearnvol_252d_slope_v148_signal,
    f20cas_f20_capital_allocation_snapshot_retearnvol_504d_slope_v149_signal,
    f20cas_f20_capital_allocation_snapshot_compositesnp_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_CAPITAL_ALLOCATION_SNAPSHOT_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    capex = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="capex")
    ncfo = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="ncfo")
    ncff = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.012, n))), name="ncff")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.003, n))), name="assets")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="debt")
    retearn = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="retearn")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {
        "revenue": revenue, "capex": capex, "ncfo": ncfo, "ncff": ncff,
        "assets": assets, "equity": equity, "debt": debt, "retearn": retearn,
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f20_capital_alloc_ratio", "_f20_capex_intensity", "_f20_capital_alloc_ncff")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f20_capital_allocation_snapshot_2nd_derivatives_001_150_claude: {n_features} features pass")
