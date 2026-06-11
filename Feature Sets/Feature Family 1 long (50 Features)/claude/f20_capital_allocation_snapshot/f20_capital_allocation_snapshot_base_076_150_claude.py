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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


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


# 21d EMA capex/ncfo × close
def f20cas_f20_capital_allocation_snapshot_capexratioema_21d_base_v076_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA capex/ncfo × close
def f20cas_f20_capital_allocation_snapshot_capexratioema_63d_base_v077_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA capex/ncfo × close
def f20cas_f20_capital_allocation_snapshot_capexratioema_252d_base_v078_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA ncff × close
def f20cas_f20_capital_allocation_snapshot_ncffema_21d_base_v079_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 21)
    result = base.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA ncff × close
def f20cas_f20_capital_allocation_snapshot_ncffema_63d_base_v080_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 63)
    result = base.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA ncff × close
def f20cas_f20_capital_allocation_snapshot_ncffema_252d_base_v081_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 252)
    result = base.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/ncfo zscore × close
def f20cas_f20_capital_allocation_snapshot_capexratioz_252d_base_v082_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/ncfo zscore × close
def f20cas_f20_capital_allocation_snapshot_capexratioz_504d_base_v083_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 63)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log capex/ncfo × close
def f20cas_f20_capital_allocation_snapshot_logcapexratio_252d_base_v084_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252)
    result = np.log(base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log capex/ncfo × close
def f20cas_f20_capital_allocation_snapshot_logcapexratio_504d_base_v085_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 504)
    result = np.log(base.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ncfo squared × close (severity)
def f20cas_f20_capital_allocation_snapshot_capexratiosq_252d_base_v086_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity squared × close
def f20cas_f20_capital_allocation_snapshot_capexintsq_252d_base_v087_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 252)
    result = base * base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ncfo × ncff/ncfo composite × close (deployment + financing posture)
def f20cas_f20_capital_allocation_snapshot_compofin_63d_base_v088_signal(capex, ncfo, ncff, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 63)
    b = _f20_capital_alloc_ncff(ncff, 63) / _mean(ncfo, 63).abs().replace(0, np.nan)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite financing × close
def f20cas_f20_capital_allocation_snapshot_compofin_252d_base_v089_signal(capex, ncfo, ncff, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    b = _f20_capital_alloc_ncff(ncff, 252) / _mean(ncfo, 252).abs().replace(0, np.nan)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex per dollar of equity raised (capex/ncff)
def f20cas_f20_capital_allocation_snapshot_capex_ncff_252d_base_v090_signal(capex, ncff, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    b = _f20_capital_alloc_ncff(ncff, 252)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/ncff
def f20cas_f20_capital_allocation_snapshot_capex_ncff_63d_base_v091_signal(capex, ncff, ncfo, closeadj):
    a = _mean(capex.abs(), 63)
    b = _f20_capital_alloc_ncff(ncff, 63)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/ncff
def f20cas_f20_capital_allocation_snapshot_capex_ncff_504d_base_v092_signal(capex, ncff, ncfo, closeadj):
    a = _mean(capex.abs(), 504)
    b = _f20_capital_alloc_ncff(ncff, 504)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex × current price (raw deployment dollars)
def f20cas_f20_capital_allocation_snapshot_capexpx_21d_base_v093_signal(capex, ncfo, closeadj):
    a = _mean(capex.abs(), 21)
    result = a * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex × current price
def f20cas_f20_capital_allocation_snapshot_capexpx_504d_base_v094_signal(capex, ncfo, closeadj):
    a = _mean(capex.abs(), 504)
    result = a * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity × current price (alt)
def f20cas_f20_capital_allocation_snapshot_capintpx_63d_base_v095_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex intensity × current price
def f20cas_f20_capital_allocation_snapshot_capintpx_504d_base_v096_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff × close (ncff dollar deployment)
def f20cas_f20_capital_allocation_snapshot_ncffpx_252d_base_v097_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff × close
def f20cas_f20_capital_allocation_snapshot_ncffpx_504d_base_v098_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retained-earnings rate × close
def f20cas_f20_capital_allocation_snapshot_retearnrate_21d_base_v099_signal(retearn, capex, revenue, closeadj):
    base = retearn.pct_change(21) + _f20_capex_intensity(capex, revenue, 21) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d retained-earnings rate × close
def f20cas_f20_capital_allocation_snapshot_retearnrate_63d_base_v100_signal(retearn, capex, revenue, closeadj):
    base = retearn.pct_change(63) + _f20_capex_intensity(capex, revenue, 63) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retained-earnings rate × close
def f20cas_f20_capital_allocation_snapshot_retearnrate_252d_base_v101_signal(retearn, capex, revenue, closeadj):
    base = retearn.pct_change(252) + _f20_capex_intensity(capex, revenue, 252) * 0.0
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex/equity at 21d × close
def f20cas_f20_capital_allocation_snapshot_capex_equity_21d_base_v102_signal(capex, equity, ncfo, closeadj):
    a = _mean(capex.abs(), 21)
    b = _mean(equity, 21)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/equity at 63d × close
def f20cas_f20_capital_allocation_snapshot_capex_equity_63d_base_v103_signal(capex, equity, ncfo, closeadj):
    a = _mean(capex.abs(), 63)
    b = _mean(equity, 63)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets at 504d × close
def f20cas_f20_capital_allocation_snapshot_capex_assets_504d_base_v104_signal(capex, assets, ncfo, closeadj):
    a = _mean(capex.abs(), 504)
    b = _mean(assets, 504)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/assets at 21d × close
def f20cas_f20_capital_allocation_snapshot_capex_assets_21d_base_v105_signal(capex, assets, ncfo, closeadj):
    a = _mean(capex.abs(), 21)
    b = _mean(assets, 21)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncff × debt (financing structure)
def f20cas_f20_capital_allocation_snapshot_ncffdebt_252d_base_v106_signal(ncff, debt, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 252)
    db = debt.pct_change(252)
    result = a * db * closeadj / a.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncff × debt
def f20cas_f20_capital_allocation_snapshot_ncffdebt_63d_base_v107_signal(ncff, debt, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 63)
    db = debt.pct_change(63)
    result = a * db * closeadj / a.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff × debt
def f20cas_f20_capital_allocation_snapshot_ncffdebt_504d_base_v108_signal(ncff, debt, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 504)
    db = debt.pct_change(504)
    result = a * db * closeadj / a.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# capex × ncfo × close (interaction product)
def f20cas_f20_capital_allocation_snapshot_capexncfo_252d_base_v109_signal(capex, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    b = _mean(ncfo, 252)
    result = a * b * closeadj / a.abs().replace(0, np.nan) + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retained earnings level / equity (retention ratio)
def f20cas_f20_capital_allocation_snapshot_retearn_equity_504d_base_v110_signal(retearn, equity, capex, revenue, closeadj):
    a = _mean(retearn, 504)
    b = _mean(equity, 504)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capex_intensity(capex, revenue, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retained earnings / equity × close
def f20cas_f20_capital_allocation_snapshot_retearn_equity_252d_base_v111_signal(retearn, equity, capex, revenue, closeadj):
    a = _mean(retearn, 252)
    b = _mean(equity, 252)
    result = (a / b.abs().replace(0, np.nan)) * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retained earnings × close
def f20cas_f20_capital_allocation_snapshot_retearnpx_252d_base_v112_signal(retearn, capex, revenue, closeadj):
    a = _mean(retearn, 252)
    result = a * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retained earnings × close
def f20cas_f20_capital_allocation_snapshot_retearnpx_504d_base_v113_signal(retearn, capex, revenue, closeadj):
    a = _mean(retearn, 504)
    result = a * closeadj + _f20_capex_intensity(capex, revenue, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retained earnings × close
def f20cas_f20_capital_allocation_snapshot_retearnpx_21d_base_v114_signal(retearn, capex, revenue, closeadj):
    a = _mean(retearn, 21)
    result = a * closeadj + _f20_capex_intensity(capex, revenue, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d retearn growth × ncff (financing-funded retention)
def f20cas_f20_capital_allocation_snapshot_retearnxncff_252d_base_v115_signal(retearn, ncff, closeadj):
    a = retearn.pct_change(252)
    b = _f20_capital_alloc_ncff(ncff, 252)
    result = a * b * closeadj / b.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/ncfo difference × ncff (interaction)
def f20cas_f20_capital_allocation_snapshot_capexncffinter_252d_base_v116_signal(capex, ncfo, ncff, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    b = _f20_capital_alloc_ncff(ncff, 252)
    result = a * b * closeadj / b.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d log of (capex + |ncff|) × close
def f20cas_f20_capital_allocation_snapshot_logcapdeploy_252d_base_v117_signal(capex, ncfo, ncff, closeadj):
    base = _mean(capex.abs() + ncff.abs(), 252)
    result = np.log(base.replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d log capex deployment
def f20cas_f20_capital_allocation_snapshot_logcapdeploy_504d_base_v118_signal(capex, ncfo, ncff, closeadj):
    base = _mean(capex.abs() + ncff.abs(), 504)
    result = np.log(base.replace(0, np.nan)) * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range of capex/ncfo × close
def f20cas_f20_capital_allocation_snapshot_capexratiorange_252d_base_v119_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    rng = base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d range of capex/ncfo × close
def f20cas_f20_capital_allocation_snapshot_capexratiorange_504d_base_v120_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    rng = base.rolling(504, min_periods=126).max() - base.rolling(504, min_periods=126).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max of capex/ncfo × close
def f20cas_f20_capital_allocation_snapshot_capexratiomax_252d_base_v121_signal(capex, ncfo, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d max capex intensity × close
def f20cas_f20_capital_allocation_snapshot_capexintmax_504d_base_v122_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21)
    result = base.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# capex per asset × debt change × close
def f20cas_f20_capital_allocation_snapshot_capassdebt_252d_base_v123_signal(capex, assets, debt, ncfo, closeadj):
    a = _mean(capex.abs(), 252) / _mean(assets, 252).abs().replace(0, np.nan)
    db = debt.pct_change(252)
    result = a * db * closeadj + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex/ncfo × revenue (scale-weighted)
def f20cas_f20_capital_allocation_snapshot_capexratiorev_21d_base_v124_signal(capex, ncfo, revenue, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    result = base * revenue * closeadj / revenue.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/ncfo × revenue
def f20cas_f20_capital_allocation_snapshot_capexratiorev_252d_base_v125_signal(capex, ncfo, revenue, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252)
    result = base * revenue * closeadj / revenue.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex/ncfo × equity
def f20cas_f20_capital_allocation_snapshot_capexratioequity_504d_base_v126_signal(capex, ncfo, equity, closeadj):
    base = _f20_capital_alloc_ratio(capex, ncfo, 504)
    result = base * equity * closeadj / equity.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex intensity vol-of-vol × close
def f20cas_f20_capital_allocation_snapshot_capexintvolvol_252d_base_v127_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21)
    sd = _std(base, 63)
    result = _std(sd, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex intensity vol-of-vol
def f20cas_f20_capital_allocation_snapshot_capexintvolvol_504d_base_v128_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21)
    sd = _std(base, 252)
    result = _std(sd, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncff × revenue (financing × scale)
def f20cas_f20_capital_allocation_snapshot_ncffrev_252d_base_v129_signal(ncff, revenue, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 252)
    result = a * revenue * closeadj / revenue.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncff × ncfo (interaction)
def f20cas_f20_capital_allocation_snapshot_ncffncfo_63d_base_v130_signal(ncff, ncfo, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 63)
    b = _mean(ncfo, 63)
    result = a * b * closeadj / b.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex intensity skew × close
def f20cas_f20_capital_allocation_snapshot_capexintskew_252d_base_v131_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21)
    result = base.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d capex intensity skew × close
def f20cas_f20_capital_allocation_snapshot_capexintskew_504d_base_v132_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21)
    result = base.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex intensity kurt × close
def f20cas_f20_capital_allocation_snapshot_capexintkurt_252d_base_v133_signal(capex, revenue, closeadj):
    base = _f20_capex_intensity(capex, revenue, 21)
    result = base.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex/ncfo × ATR scale
def f20cas_f20_capital_allocation_snapshot_capexatr_252d_base_v134_signal(capex, ncfo, closeadj, high, low):
    base = _f20_capital_alloc_ratio(capex, ncfo, 252)
    atr = (high - low).rolling(21, min_periods=5).mean()
    result = base * atr * closeadj / atr.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex/ncfo × dollar volume
def f20cas_f20_capital_allocation_snapshot_capexratiodv_21d_base_v135_signal(capex, ncfo, closeadj, volume):
    base = _f20_capital_alloc_ratio(capex, ncfo, 21)
    dv = closeadj * volume
    result = base * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex intensity × dollar volume
def f20cas_f20_capital_allocation_snapshot_capexintdv_252d_base_v136_signal(capex, revenue, closeadj, volume):
    base = _f20_capex_intensity(capex, revenue, 252)
    dv = closeadj * volume
    result = base * dv
    return result.replace([np.inf, -np.inf], np.nan)


# 252d retained earnings vol-of-vol × close
def f20cas_f20_capital_allocation_snapshot_retearnvol_252d_base_v137_signal(retearn, capex, revenue, closeadj):
    base = _mean(retearn, 21)
    sd = _std(base, 252)
    result = sd * closeadj + _f20_capex_intensity(capex, revenue, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d retearn vol × close
def f20cas_f20_capital_allocation_snapshot_retearnvol_504d_base_v138_signal(retearn, capex, revenue, closeadj):
    base = _mean(retearn, 21)
    sd = _std(base, 504)
    result = sd * closeadj + _f20_capex_intensity(capex, revenue, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex/ncfo and capex intensity blend × close
def f20cas_f20_capital_allocation_snapshot_blend_252d_base_v139_signal(capex, ncfo, revenue, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    b = _f20_capex_intensity(capex, revenue, 252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d blend × close
def f20cas_f20_capital_allocation_snapshot_blend_504d_base_v140_signal(capex, ncfo, revenue, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 504)
    b = _f20_capex_intensity(capex, revenue, 504)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d capex/ncfo × retearn growth × close
def f20cas_f20_capital_allocation_snapshot_capexretearn_252d_base_v141_signal(capex, ncfo, retearn, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    re = retearn.pct_change(252)
    result = a * re * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex × revenue ratio (alt encoding)
def f20cas_f20_capital_allocation_snapshot_capexrev_21d_base_v142_signal(capex, revenue, closeadj):
    result = _f20_capex_intensity(capex, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/revenue ratio scaled by retearn level
def f20cas_f20_capital_allocation_snapshot_capxretearn_252d_base_v143_signal(capex, revenue, retearn, closeadj):
    base = _f20_capex_intensity(capex, revenue, 252)
    re = _mean(retearn, 252)
    result = base * re * closeadj / re.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff sign-flip detection × close
def f20cas_f20_capital_allocation_snapshot_ncffsign_252d_base_v144_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 252)
    result = np.sign(base) * np.log(base.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ncff sign × close
def f20cas_f20_capital_allocation_snapshot_ncffsign_504d_base_v145_signal(ncff, closeadj):
    base = _f20_capital_alloc_ncff(ncff, 504)
    result = np.sign(base) * np.log(base.abs().replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex/ncfo × ncff/ncfo product (full deployment intensity)
def f20cas_f20_capital_allocation_snapshot_fulldeploy_252d_base_v146_signal(capex, ncfo, ncff, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    b = _f20_capital_alloc_ncff(ncff, 252) / _mean(ncfo, 252).abs().replace(0, np.nan)
    result = (a + b.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d full-deploy
def f20cas_f20_capital_allocation_snapshot_fulldeploy_504d_base_v147_signal(capex, ncfo, ncff, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 504)
    b = _f20_capital_alloc_ncff(ncff, 504) / _mean(ncfo, 504).abs().replace(0, np.nan)
    result = (a + b.abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncff dollar with retearn rate × close
def f20cas_f20_capital_allocation_snapshot_ncffretearn_252d_base_v148_signal(ncff, retearn, closeadj):
    a = _f20_capital_alloc_ncff(ncff, 252)
    re = retearn.pct_change(252)
    result = a * re * closeadj / a.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex × ncfo gap
def f20cas_f20_capital_allocation_snapshot_capexgap_252d_base_v149_signal(capex, ncfo, closeadj):
    a = _mean(capex.abs(), 252)
    b = _mean(ncfo, 252)
    result = (a - b.abs()) * closeadj / b.abs().replace(0, np.nan) + _f20_capital_alloc_ratio(capex, ncfo, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite snapshot: capex/ncfo + retearn growth
def f20cas_f20_capital_allocation_snapshot_compositesnp_252d_base_v150_signal(capex, ncfo, retearn, closeadj):
    a = _f20_capital_alloc_ratio(capex, ncfo, 252)
    b = retearn.pct_change(252)
    result = (a + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f20cas_f20_capital_allocation_snapshot_capexratioema_21d_base_v076_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioema_63d_base_v077_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioema_252d_base_v078_signal,
    f20cas_f20_capital_allocation_snapshot_ncffema_21d_base_v079_signal,
    f20cas_f20_capital_allocation_snapshot_ncffema_63d_base_v080_signal,
    f20cas_f20_capital_allocation_snapshot_ncffema_252d_base_v081_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioz_252d_base_v082_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioz_504d_base_v083_signal,
    f20cas_f20_capital_allocation_snapshot_logcapexratio_252d_base_v084_signal,
    f20cas_f20_capital_allocation_snapshot_logcapexratio_504d_base_v085_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiosq_252d_base_v086_signal,
    f20cas_f20_capital_allocation_snapshot_capexintsq_252d_base_v087_signal,
    f20cas_f20_capital_allocation_snapshot_compofin_63d_base_v088_signal,
    f20cas_f20_capital_allocation_snapshot_compofin_252d_base_v089_signal,
    f20cas_f20_capital_allocation_snapshot_capex_ncff_252d_base_v090_signal,
    f20cas_f20_capital_allocation_snapshot_capex_ncff_63d_base_v091_signal,
    f20cas_f20_capital_allocation_snapshot_capex_ncff_504d_base_v092_signal,
    f20cas_f20_capital_allocation_snapshot_capexpx_21d_base_v093_signal,
    f20cas_f20_capital_allocation_snapshot_capexpx_504d_base_v094_signal,
    f20cas_f20_capital_allocation_snapshot_capintpx_63d_base_v095_signal,
    f20cas_f20_capital_allocation_snapshot_capintpx_504d_base_v096_signal,
    f20cas_f20_capital_allocation_snapshot_ncffpx_252d_base_v097_signal,
    f20cas_f20_capital_allocation_snapshot_ncffpx_504d_base_v098_signal,
    f20cas_f20_capital_allocation_snapshot_retearnrate_21d_base_v099_signal,
    f20cas_f20_capital_allocation_snapshot_retearnrate_63d_base_v100_signal,
    f20cas_f20_capital_allocation_snapshot_retearnrate_252d_base_v101_signal,
    f20cas_f20_capital_allocation_snapshot_capex_equity_21d_base_v102_signal,
    f20cas_f20_capital_allocation_snapshot_capex_equity_63d_base_v103_signal,
    f20cas_f20_capital_allocation_snapshot_capex_assets_504d_base_v104_signal,
    f20cas_f20_capital_allocation_snapshot_capex_assets_21d_base_v105_signal,
    f20cas_f20_capital_allocation_snapshot_ncffdebt_252d_base_v106_signal,
    f20cas_f20_capital_allocation_snapshot_ncffdebt_63d_base_v107_signal,
    f20cas_f20_capital_allocation_snapshot_ncffdebt_504d_base_v108_signal,
    f20cas_f20_capital_allocation_snapshot_capexncfo_252d_base_v109_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_equity_504d_base_v110_signal,
    f20cas_f20_capital_allocation_snapshot_retearn_equity_252d_base_v111_signal,
    f20cas_f20_capital_allocation_snapshot_retearnpx_252d_base_v112_signal,
    f20cas_f20_capital_allocation_snapshot_retearnpx_504d_base_v113_signal,
    f20cas_f20_capital_allocation_snapshot_retearnpx_21d_base_v114_signal,
    f20cas_f20_capital_allocation_snapshot_retearnxncff_252d_base_v115_signal,
    f20cas_f20_capital_allocation_snapshot_capexncffinter_252d_base_v116_signal,
    f20cas_f20_capital_allocation_snapshot_logcapdeploy_252d_base_v117_signal,
    f20cas_f20_capital_allocation_snapshot_logcapdeploy_504d_base_v118_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiorange_252d_base_v119_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiorange_504d_base_v120_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiomax_252d_base_v121_signal,
    f20cas_f20_capital_allocation_snapshot_capexintmax_504d_base_v122_signal,
    f20cas_f20_capital_allocation_snapshot_capassdebt_252d_base_v123_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiorev_21d_base_v124_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiorev_252d_base_v125_signal,
    f20cas_f20_capital_allocation_snapshot_capexratioequity_504d_base_v126_signal,
    f20cas_f20_capital_allocation_snapshot_capexintvolvol_252d_base_v127_signal,
    f20cas_f20_capital_allocation_snapshot_capexintvolvol_504d_base_v128_signal,
    f20cas_f20_capital_allocation_snapshot_ncffrev_252d_base_v129_signal,
    f20cas_f20_capital_allocation_snapshot_ncffncfo_63d_base_v130_signal,
    f20cas_f20_capital_allocation_snapshot_capexintskew_252d_base_v131_signal,
    f20cas_f20_capital_allocation_snapshot_capexintskew_504d_base_v132_signal,
    f20cas_f20_capital_allocation_snapshot_capexintkurt_252d_base_v133_signal,
    f20cas_f20_capital_allocation_snapshot_capexatr_252d_base_v134_signal,
    f20cas_f20_capital_allocation_snapshot_capexratiodv_21d_base_v135_signal,
    f20cas_f20_capital_allocation_snapshot_capexintdv_252d_base_v136_signal,
    f20cas_f20_capital_allocation_snapshot_retearnvol_252d_base_v137_signal,
    f20cas_f20_capital_allocation_snapshot_retearnvol_504d_base_v138_signal,
    f20cas_f20_capital_allocation_snapshot_blend_252d_base_v139_signal,
    f20cas_f20_capital_allocation_snapshot_blend_504d_base_v140_signal,
    f20cas_f20_capital_allocation_snapshot_capexretearn_252d_base_v141_signal,
    f20cas_f20_capital_allocation_snapshot_capexrev_21d_base_v142_signal,
    f20cas_f20_capital_allocation_snapshot_capxretearn_252d_base_v143_signal,
    f20cas_f20_capital_allocation_snapshot_ncffsign_252d_base_v144_signal,
    f20cas_f20_capital_allocation_snapshot_ncffsign_504d_base_v145_signal,
    f20cas_f20_capital_allocation_snapshot_fulldeploy_252d_base_v146_signal,
    f20cas_f20_capital_allocation_snapshot_fulldeploy_504d_base_v147_signal,
    f20cas_f20_capital_allocation_snapshot_ncffretearn_252d_base_v148_signal,
    f20cas_f20_capital_allocation_snapshot_capexgap_252d_base_v149_signal,
    f20cas_f20_capital_allocation_snapshot_compositesnp_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F20_CAPITAL_ALLOCATION_SNAPSHOT_REGISTRY_076_150 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f20_capital_allocation_snapshot_base_076_150_claude: {n_features} features pass")
