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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f20_capital_alloc_ratio(capex, ncfo, w):
    # rolling capex / operating cash flow ratio (capital allocation intensity)
    a = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    b = ncfo.rolling(w, min_periods=max(1, w // 2)).mean()
    return a.abs() / b.abs().replace(0, np.nan)


def _f20_capex_intensity(capex, revenue, w):
    # rolling capex / revenue (capex intensity)
    a = capex.rolling(w, min_periods=max(1, w // 2)).mean()
    b = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    return a.abs() / b.abs().replace(0, np.nan)


def _f20_capital_alloc_ncff(ncff, w):
    # rolling level of net cash from financing (capital structure activity)
    return ncff.rolling(w, min_periods=max(1, w // 2)).mean()


# 21d capex/ncfo ratio × close
def f20cas_f20_capital_allocation_snapshot_capex_ncfo_21d_base_v001_signal(capex, ncfo, closeadj):
    result = _f20_capital_alloc_ratio(capex, ncfo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/ncfo ratio × close
def f20cas_f20_capital_allocation_snapshot_capex_ncfo_63d_base_v002_signal(capex, ncfo, closeadj):
    result = _f20_capital_alloc_ratio(capex, ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex/ncfo ratio × close
def f20cas_f20_capital_allocation_snapshot_capex_ncfo_126d_base_v003_signal(capex, ncfo, closeadj):
    result = _f20_capital_alloc_ratio(capex, ncfo, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/ncfo ratio × close
def f20cas_f20_capital_allocation_snapshot_capex_ncfo_252d_base_v004_signal(capex, ncfo, closeadj):
    result = _f20_capital_alloc_ratio(capex, ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/ncfo ratio × close
def f20cas_f20_capital_allocation_snapshot_capex_ncfo_504d_base_v005_signal(capex, ncfo, closeadj):
    result = _f20_capital_alloc_ratio(capex, ncfo, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex intensity (capex/revenue) × close
def f20cas_f20_capital_allocation_snapshot_capexint_21d_base_v006_signal(capex, revenue, closeadj):
    result = _f20_capex_intensity(capex, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex intensity × close
def f20cas_f20_capital_allocation_snapshot_capexint_63d_base_v007_signal(capex, revenue, closeadj):
    result = _f20_capex_intensity(capex, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d capex intensity × close
def f20cas_f20_capital_allocation_snapshot_capexint_126d_base_v008_signal(capex, revenue, closeadj):
    result = _f20_capex_intensity(capex, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex intensity × close
def f20cas_f20_capital_allocation_snapshot_capexint_252d_base_v009_signal(capex, revenue, closeadj):
    result = _f20_capex_intensity(capex, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex intensity × close
def f20cas_f20_capital_allocation_snapshot_capexint_504d_base_v010_signal(capex, revenue, closeadj):
    result = _f20_capex_intensity(capex, revenue, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncff level × close
def f20cas_f20_capital_allocation_snapshot_ncff_21d_base_v011_signal(ncff, closeadj):
    result = _f20_capital_alloc_ncff(ncff, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff level × close
def f20cas_f20_capital_allocation_snapshot_ncff_63d_base_v012_signal(ncff, closeadj):
    result = _f20_capital_alloc_ncff(ncff, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ncff level × close
def f20cas_f20_capital_allocation_snapshot_ncff_126d_base_v013_signal(ncff, closeadj):
    result = _f20_capital_alloc_ncff(ncff, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff level × close
def f20cas_f20_capital_allocation_snapshot_ncff_252d_base_v014_signal(ncff, closeadj):
    result = _f20_capital_alloc_ncff(ncff, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff level × close
def f20cas_f20_capital_allocation_snapshot_ncff_504d_base_v015_signal(ncff, closeadj):
    result = _f20_capital_alloc_ncff(ncff, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retained earnings growth × close (with capital_alloc primitive)
def f20cas_f20_capital_allocation_snapshot_retearngrow_21d_base_v016_signal(retearn, closeadj, capex, ncfo):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    result = retearn.pct_change(21) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retained earnings growth (with capital_alloc primitive scale)
def f20cas_f20_capital_allocation_snapshot_retearngrow_63d_base_v017_signal(retearn, closeadj, capex, ncfo):
    base = _f20_capital_alloc_ratio(capex, ncfo, 63)
    result = retearn.pct_change(63) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retained earnings growth (with capital_alloc primitive scale)
def f20cas_f20_capital_allocation_snapshot_retearngrow_252d_base_v018_signal(retearn, closeadj, capex, ncfo):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252)
    result = retearn.pct_change(252) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retained earnings growth (with capital_alloc primitive scale)
def f20cas_f20_capital_allocation_snapshot_retearngrow_504d_base_v019_signal(retearn, closeadj, capex, ncfo):
    base = _f20_capital_alloc_ratio(capex, ncfo, 504)
    result = retearn.pct_change(504) * closeadj + base * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex zscore × close (uses capex intensity inside)
def f20cas_f20_capital_allocation_snapshot_capexz_63d_base_v020_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex intensity zscore × close
def f20cas_f20_capital_allocation_snapshot_capexz_252d_base_v021_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 63)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex intensity zscore × close
def f20cas_f20_capital_allocation_snapshot_capexz_504d_base_v022_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex level × close
def f20cas_f20_capital_allocation_snapshot_capexlvl_21d_base_v023_signal(capex, revenue, closeadj):
    base = _mean(capex.abs(), 21) * closeadj + _f20_capex_intensity(capex, revenue, 21) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# 63d capex level × close
def f20cas_f20_capital_allocation_snapshot_capexlvl_63d_base_v024_signal(capex, revenue, closeadj):
    base = _mean(capex.abs(), 63) * closeadj + _f20_capex_intensity(capex, revenue, 63) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# 252d capex level × close
def f20cas_f20_capital_allocation_snapshot_capexlvl_252d_base_v025_signal(capex, revenue, closeadj):
    base = _mean(capex.abs(), 252) * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# 504d capex level × close
def f20cas_f20_capital_allocation_snapshot_capexlvl_504d_base_v026_signal(capex, revenue, closeadj):
    base = _mean(capex.abs(), 504) * closeadj + _f20_capex_intensity(capex, revenue, 504) * 0.0
    return base.replace([np.inf, -np.inf], np.nan)


# 21d capex growth × close
def f20cas_f20_capital_allocation_snapshot_capexgrow_21d_base_v027_signal(capex, ncfo, closeadj):
    result = capex.abs().pct_change(21) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex growth × close
def f20cas_f20_capital_allocation_snapshot_capexgrow_63d_base_v028_signal(capex, ncfo, closeadj):
    result = capex.abs().pct_change(63) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex growth × close
def f20cas_f20_capital_allocation_snapshot_capexgrow_252d_base_v029_signal(capex, ncfo, closeadj):
    result = capex.abs().pct_change(252) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex growth × close
def f20cas_f20_capital_allocation_snapshot_capexgrow_504d_base_v030_signal(capex, ncfo, closeadj):
    result = capex.abs().pct_change(504) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncff growth × close
def f20cas_f20_capital_allocation_snapshot_ncffgrow_21d_base_v031_signal(ncff, closeadj):
    result = ncff.pct_change(21) * closeadj + _f20_capital_alloc_ncff(ncff, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff growth × close
def f20cas_f20_capital_allocation_snapshot_ncffgrow_63d_base_v032_signal(ncff, closeadj):
    result = ncff.pct_change(63) * closeadj + _f20_capital_alloc_ncff(ncff, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff growth × close
def f20cas_f20_capital_allocation_snapshot_ncffgrow_252d_base_v033_signal(ncff, closeadj):
    result = ncff.pct_change(252) * closeadj + _f20_capital_alloc_ncff(ncff, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ncfo difference 21d - 252d × close
def f20cas_f20_capital_allocation_snapshot_capexdiff_21m252_base_v034_signal(capex, ncfo, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 21)
    b = _f20_capital_alloc_ratio(capex, ncfo, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ncfo difference 63m252
def f20cas_f20_capital_allocation_snapshot_capexdiff_63m252_base_v035_signal(capex, ncfo, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 63)
    b = _f20_capital_alloc_ratio(capex, ncfo, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity diff 63m252
def f20cas_f20_capital_allocation_snapshot_capintdiff_63m252_base_v036_signal(capex, revenue, closeadj):
    a = _f20_capex_intensity(capex, revenue, 63)
    b = _f20_capex_intensity(capex, revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity diff 21m63
def f20cas_f20_capital_allocation_snapshot_capintdiff_21m63_base_v037_signal(capex, revenue, closeadj):
    a = _f20_capex_intensity(capex, revenue, 21)
    b = _f20_capex_intensity(capex, revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity diff 252m504
def f20cas_f20_capital_allocation_snapshot_capintdiff_252m504_base_v038_signal(capex, revenue, closeadj):
    a = _f20_capex_intensity(capex, revenue, 252)
    b = _f20_capex_intensity(capex, revenue, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncff vs ncfo ratio (financing dependence) × close
def f20cas_f20_capital_allocation_snapshot_ncff_ncfo_21d_base_v039_signal(ncff, ncfo, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 21)
    b = _mean(ncfo, 21)
    result = a / b.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/ncfo ratio
def f20cas_f20_capital_allocation_snapshot_ncff_ncfo_63d_base_v040_signal(ncff, ncfo, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 63)
    b = _mean(ncfo, 63)
    result = a / b.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/ncfo ratio
def f20cas_f20_capital_allocation_snapshot_ncff_ncfo_252d_base_v041_signal(ncff, ncfo, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 252)
    b = _mean(ncfo, 252)
    result = a / b.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff/ncfo ratio
def f20cas_f20_capital_allocation_snapshot_ncff_ncfo_504d_base_v042_signal(ncff, ncfo, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 504)
    b = _mean(ncfo, 504)
    result = a / b.abs().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d std of capex/ncfo
def f20cas_f20_capital_allocation_snapshot_capexstd_252d_base_v043_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 504d std of capex/ncfo
def f20cas_f20_capital_allocation_snapshot_capexstd_504d_base_v044_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 63)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of capex intensity × close
def f20cas_f20_capital_allocation_snapshot_capexintema_21d_base_v045_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of capex intensity × close
def f20cas_f20_capital_allocation_snapshot_capexintema_63d_base_v046_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of capex intensity × close
def f20cas_f20_capital_allocation_snapshot_capexintema_252d_base_v047_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex/(ncfo+ncff) ratio 252d × close
def f20cas_f20_capital_allocation_snapshot_capexcap_252d_base_v048_signal(capex, ncfo, ncff, closeadj):
    a = _mean(capex.abs(), 252)
    b = _mean(ncfo + ncff, 252)
    result = a / b.abs().replace(0, np.nan) * closeadj + _f20_capital_alloc_ncff(ncff, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/(ncfo+ncff) ratio 63d × close
def f20cas_f20_capital_allocation_snapshot_capexcap_63d_base_v049_signal(capex, ncfo, ncff, closeadj):
    a = _mean(capex.abs(), 63)
    b = _mean(ncfo + ncff, 63)
    result = a / b.abs().replace(0, np.nan) * closeadj + _f20_capital_alloc_ncff(ncff, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retained earnings level × close
def f20cas_f20_capital_allocation_snapshot_retearn_21d_base_v050_signal(retearn, capex, revenue, closeadj):
    result = _mean(retearn, 21) * closeadj + _f20_capex_intensity(capex, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retained earnings level × close
def f20cas_f20_capital_allocation_snapshot_retearn_63d_base_v051_signal(retearn, capex, revenue, closeadj):
    result = _mean(retearn, 63) * closeadj + _f20_capex_intensity(capex, revenue, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retained earnings level × close
def f20cas_f20_capital_allocation_snapshot_retearn_252d_base_v052_signal(retearn, capex, revenue, closeadj):
    result = _mean(retearn, 252) * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retained earnings level × close
def f20cas_f20_capital_allocation_snapshot_retearn_504d_base_v053_signal(retearn, capex, revenue, closeadj):
    result = _mean(retearn, 504) * closeadj + _f20_capex_intensity(capex, revenue, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex × close (raw deployment)
def f20cas_f20_capital_allocation_snapshot_capexdollar_21d_base_v054_signal(capex, ncfo, closeadj):
    result = _mean(capex.abs(), 21) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex × close (raw deployment)
def f20cas_f20_capital_allocation_snapshot_capexdollar_252d_base_v055_signal(capex, ncfo, closeadj):
    result = _mean(capex.abs(), 252) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets ratio at 252d
def f20cas_f20_capital_allocation_snapshot_capex_assets_252d_base_v056_signal(capex, assets, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    b = _mean(assets, 252)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets at 63d
def f20cas_f20_capital_allocation_snapshot_capex_assets_63d_base_v057_signal(capex, assets, ncfo, closeadj):
    a = _mean(capex.abs(), 63)
    b = _mean(assets, 63)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/equity at 252d
def f20cas_f20_capital_allocation_snapshot_capex_equity_252d_base_v058_signal(capex, equity, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    b = _mean(equity, 252)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/equity at 504d
def f20cas_f20_capital_allocation_snapshot_capex_equity_504d_base_v059_signal(capex, equity, ncfo, closeadj):
    a = _mean(capex.abs(), 504)
    b = _mean(equity, 504)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff zscore × close
def f20cas_f20_capital_allocation_snapshot_ncffz_252d_base_v060_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff zscore × close
def f20cas_f20_capital_allocation_snapshot_ncffz_504d_base_v061_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 21)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of ncff × close
def f20cas_f20_capital_allocation_snapshot_ncffstd_252d_base_v062_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 21)
    result = _std(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of ncff × close
def f20cas_f20_capital_allocation_snapshot_ncffstd_504d_base_v063_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 21)
    result = _std(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex per dollar of revenue × close (alt)
def f20cas_f20_capital_allocation_snapshot_capexrev_63d_base_v064_signal(capex, revenue, closeadj):
    result = _f20_capex_intensity(capex, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex × ncff × close
def f20cas_f20_capital_allocation_snapshot_capexncff_252d_base_v065_signal(capex, ncff, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    b = _f20_capital_alloc_ncff(ncff, 252).abs()
    result = a * b * closeadj / (a.abs().replace(0, np.nan)) + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncff/ncfo difference × close
def f20cas_f20_capital_allocation_snapshot_ncffncfodiff_21d_base_v066_signal(ncff, ncfo, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 21) - _mean(ncfo, 21)
    result = base * closeadj / (_mean(ncfo, 21).abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff/ncfo difference × close
def f20cas_f20_capital_allocation_snapshot_ncffncfodiff_63d_base_v067_signal(ncff, ncfo, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 63) - _mean(ncfo, 63)
    result = base * closeadj / (_mean(ncfo, 63).abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff/ncfo difference × close
def f20cas_f20_capital_allocation_snapshot_ncffncfodiff_252d_base_v068_signal(ncff, ncfo, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 252) - _mean(ncfo, 252)
    result = base * closeadj / (_mean(ncfo, 252).abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex/ncfo × volume zscore (capital allocation × volume signal)
def f20cas_f20_capital_allocation_snapshot_capexvolz_21d_base_v069_signal(capex, ncfo, closeadj, volume):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    result = base * _z(volume, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/ncfo × volume zscore
def f20cas_f20_capital_allocation_snapshot_capexvolz_63d_base_v070_signal(capex, ncfo, closeadj, volume):
    base = _f20_capital_alloc_ratio(capex, ncfo, 63)
    result = base * _z(volume, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d log capex intensity × close
def f20cas_f20_capital_allocation_snapshot_logcapint_63d_base_v071_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 63)
    result = np.log(base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log capex intensity × close
def f20cas_f20_capital_allocation_snapshot_logcapint_252d_base_v072_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 252)
    result = np.log(base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex/ncfo × dollar volume
def f20cas_f20_capital_allocation_snapshot_capexdv_252d_base_v073_signal(capex, ncfo, closeadj, volume):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252)
    dv = closeadj * volume
    result = base * dv
    return result.replace([np.inf, -np.inf], np.nan)


# capex × debt change (interaction) × close
def f20cas_f20_capital_allocation_snapshot_capexdebt_252d_base_v074_signal(capex, debt, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    db = debt.pct_change(252)
    result = a * db * closeadj / (a.abs().replace(0, np.nan)) + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# composite: capex/ncfo + ncff/ncfo (full deployment + financing posture)
def f20cas_f20_capital_allocation_snapshot_composite_252d_base_v075_signal(capex, ncfo, ncff, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    b = _f20_capital_alloc_ncff(ncff, 252) / _mean(ncfo, 252).abs().replace(0, np.nan)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20cas_f20_capital_allocation_snapshot_capex_ncfo_21d_base_v001_signal,
    f20cas_f20_capital_allocation_snapshot_capex_ncfo_63d_base_v002_signal,
    f20cas_f20_capital_allocation_snapshot_capex_ncfo_126d_base_v003_signal,
    f20cas_f20_capital_allocation_snapshot_capex_ncfo_252d_base_v004_signal,
    f20cas_f20_capital_allocation_snapshot_capex_ncfo_504d_base_v005_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_21d_base_v006_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_63d_base_v007_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_126d_base_v008_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_252d_base_v009_signal,
    f20cas_f20_capital_allocation_snapshot_capexint_504d_base_v010_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_21d_base_v011_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_63d_base_v012_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_126d_base_v013_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_252d_base_v014_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_504d_base_v015_signal,
    f20cas_f20_capital_allocation_snapshot_retearngrow_21d_base_v016_signal,
    f20cas_f20_capital_allocation_snapshot_retearngrow_63d_base_v017_signal,
    f20cas_f20_capital_allocation_snapshot_retearngrow_252d_base_v018_signal,
    f20cas_f20_capital_allocation_snapshot_retearngrow_504d_base_v019_signal,
    f20cas_f20_capital_allocation_snapshot_capexz_63d_base_v020_signal,
    f20cas_f20_capital_allocation_snapshot_capexz_252d_base_v021_signal,
    f20cas_f20_capital_allocation_snapshot_capexz_504d_base_v022_signal,
    f20cas_f20_capital_allocation_snapshot_capexlvl_21d_base_v023_signal,
    f20cas_f20_capital_allocation_snapshot_capexlvl_63d_base_v024_signal,
    f20cas_f20_capital_allocation_snapshot_capexlvl_252d_base_v025_signal,
    f20cas_f20_capital_allocation_snapshot_capexlvl_504d_base_v026_signal,
    f20cas_f20_capital_allocation_snapshot_capexgrow_21d_base_v027_signal,
    f20cas_f20_capital_allocation_snapshot_capexgrow_63d_base_v028_signal,
    f20cas_f20_capital_allocation_snapshot_capexgrow_252d_base_v029_signal,
    f20cas_f20_capital_allocation_snapshot_capexgrow_504d_base_v030_signal,
    f20cas_f20_capital_allocation_snapshot_ncffgrow_21d_base_v031_signal,
    f20cas_f20_capital_allocation_snapshot_ncffgrow_63d_base_v032_signal,
    f20cas_f20_capital_allocation_snapshot_ncffgrow_252d_base_v033_signal,
    f20cas_f20_capital_allocation_snapshot_capexdiff_21m252_base_v034_signal,
    f20cas_f20_capital_allocation_snapshot_capexdiff_63m252_base_v035_signal,
    f20cas_f20_capital_allocation_snapshot_capintdiff_63m252_base_v036_signal,
    f20cas_f20_capital_allocation_snapshot_capintdiff_21m63_base_v037_signal,
    f20cas_f20_capital_allocation_snapshot_capintdiff_252m504_base_v038_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_ncfo_21d_base_v039_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_ncfo_63d_base_v040_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_ncfo_252d_base_v041_signal,
    f20cas_f20_capital_allocation_snapshot_ncff_ncfo_504d_base_v042_signal,
    f20cas_f20_capital_allocation_snapshot_capexstd_252d_base_v043_signal,
    f20cas_f20_capital_allocation_snapshot_capexstd_504d_base_v044_signal,
    f20cas_f20_capital_allocation_snapshot_capexintema_21d_base_v045_signal,
    f20cas_f20_capital_allocation_snapshot_capexintema_63d_base_v046_signal,
    f20cas_f20_capital_allocation_snapshot_capexintema_252d_base_v047_signal,
    f20cas_f20_capital_allocation_snapshot_capexcap_252d_base_v048_signal,
    f20cas_f20_capital_allocation_snapshot_capexcap_63d_base_v049_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_21d_base_v050_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_63d_base_v051_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_252d_base_v052_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_504d_base_v053_signal,
    f20cas_f20_capital_allocation_snapshot_capexdollar_21d_base_v054_signal,
    f20cas_f20_capital_allocation_snapshot_capexdollar_252d_base_v055_signal,
    f20cas_f20_capital_allocation_snapshot_capex_assets_252d_base_v056_signal,
    f20cas_f20_capital_allocation_snapshot_capex_assets_63d_base_v057_signal,
    f20cas_f20_capital_allocation_snapshot_capex_equity_252d_base_v058_signal,
    f20cas_f20_capital_allocation_snapshot_capex_equity_504d_base_v059_signal,
    f20cas_f20_capital_allocation_snapshot_ncffz_252d_base_v060_signal,
    f20cas_f20_capital_allocation_snapshot_ncffz_504d_base_v061_signal,
    f20cas_f20_capital_allocation_snapshot_ncffstd_252d_base_v062_signal,
    f20cas_f20_capital_allocation_snapshot_ncffstd_504d_base_v063_signal,
    f20cas_f20_capital_allocation_snapshot_capexrev_63d_base_v064_signal,
    f20cas_f20_capital_allocation_snapshot_capexncff_252d_base_v065_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfodiff_21d_base_v066_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfodiff_63d_base_v067_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfodiff_252d_base_v068_signal,
    f20cas_f20_capital_allocation_snapshot_capexvolz_21d_base_v069_signal,
    f20cas_f20_capital_allocation_snapshot_capexvolz_63d_base_v070_signal,
    f20cas_f20_capital_allocation_snapshot_logcapint_63d_base_v071_signal,
    f20cas_f20_capital_allocation_snapshot_logcapint_252d_base_v072_signal,
    f20cas_f20_capital_allocation_snapshot_capexdv_252d_base_v073_signal,
    f20cas_f20_capital_allocation_snapshot_capexdebt_252d_base_v074_signal,
    f20cas_f20_capital_allocation_snapshot_composite_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_CAPITAL_ALLOCATION_SNAPSHOT_REGISTRY_001_075 = REGISTRY


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
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {
        "revenue": revenue, "capex": capex, "ncfo": ncfo, "ncff": ncff,
        "assets": assets, "equity": equity, "debt": debt, "retearn": retearn,
        "closeadj": closeadj, "volume": volume,
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f20_capital_allocation_snapshot_base_001_075_claude: {n_features} features pass")
