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


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f39_seasonal_inv_pattern(inventory, w):
    # Detrended inventory: deviation from rolling mean
    return (inventory - _mean(inventory, w)) / _mean(inventory, w).replace(0, np.nan)


def _f39_revenue_inv_sync(revenue, inventory, w):
    # Rolling correlation of revenue & inventory growth
    rg = revenue.pct_change()
    ig = inventory.pct_change()
    return rg.rolling(w, min_periods=max(1, w // 2)).corr(ig)


def _f39_seasonality_quality(revenue, inventory, w):
    # High sync + low residual => good seasonal management
    rg = revenue.pct_change()
    ig = inventory.pct_change()
    corr = rg.rolling(w, min_periods=max(1, w // 2)).corr(ig)
    resid_std = _std(ig - rg, w)
    return corr / resid_std.replace(0, np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinvg_5d_base_v076_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 5)
    result = d * inventory.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinvg_10d_base_v077_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 10)
    result = d * inventory.pct_change(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinvg_21d_base_v078_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 21)
    result = d * inventory.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinvg_42d_base_v079_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 42)
    result = d * inventory.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinvg_63d_base_v080_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d * inventory.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinvg_126d_base_v081_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 126)
    result = d * inventory.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinvg_189d_base_v082_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 189)
    result = d * inventory.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinvg_252d_base_v083_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 252)
    result = d * inventory.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinvg_378d_base_v084_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 378)
    result = d * inventory.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinvg_504d_base_v085_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 504)
    result = d * inventory.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_21d_base_v086_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = d * revenue.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_42d_base_v087_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 42)
    result = d * revenue.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_63d_base_v088_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = d * revenue.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_126d_base_v089_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 126)
    result = d * revenue.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_189d_base_v090_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 189)
    result = d * revenue.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_252d_base_v091_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 252)
    result = d * revenue.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_378d_base_v092_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 378)
    result = d * revenue.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_504d_base_v093_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 504)
    result = d * revenue.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_100d_base_v094_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 100)
    result = d * revenue.pct_change(100) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_150d_base_v095_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 150)
    result = d * revenue.pct_change(150) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxrev_21d_base_v096_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 21)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxrev_42d_base_v097_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 42)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxrev_63d_base_v098_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxrev_126d_base_v099_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 126)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxrev_189d_base_v100_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 189)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxrev_252d_base_v101_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 252)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxrev_378d_base_v102_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 378)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxrev_504d_base_v103_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 504)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxrev_100d_base_v104_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 100)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxrev_150d_base_v105_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 150)
    result = d * (revenue / 1e9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvdiff_21d_base_v106_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvdiff_42d_base_v107_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvdiff_63d_base_v108_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvdiff_126d_base_v109_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvdiff_189d_base_v110_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvdiff_252d_base_v111_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvdiff_378d_base_v112_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_21d_base_v113_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = d.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_42d_base_v114_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = d.diff(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_63d_base_v115_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_126d_base_v116_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = d.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_189d_base_v117_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = d.diff(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_252d_base_v118_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = d.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_378d_base_v119_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 63)
    result = d.diff(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualz_42d_base_v120_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _z(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualz_63d_base_v121_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualz_126d_base_v122_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualz_189d_base_v123_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _z(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualz_252d_base_v124_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualz_378d_base_v125_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _z(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualz_504d_base_v126_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 63)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrevd_21d_base_v127_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 21)
    result = d * revenue.diff(21) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrevd_42d_base_v128_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 42)
    result = d * revenue.diff(42) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrevd_63d_base_v129_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 63)
    result = d * revenue.diff(63) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrevd_126d_base_v130_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 126)
    result = d * revenue.diff(126) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrevd_189d_base_v131_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 189)
    result = d * revenue.diff(189) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrevd_252d_base_v132_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 252)
    result = d * revenue.diff(252) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxrevd_378d_base_v133_signal(revenue, inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 378)
    result = d * revenue.diff(378) / 1e9 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncema2_10d_base_v134_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncema2_21d_base_v135_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncema2_42d_base_v136_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _ema(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncema2_63d_base_v137_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncema2_126d_base_v138_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncema2_252d_base_v139_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncema2_378d_base_v140_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 21)
    result = _ema(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema2_10d_base_v141_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 21)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema2_21d_base_v142_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 21)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema2_42d_base_v143_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 21)
    result = _ema(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema2_63d_base_v144_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 21)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema2_126d_base_v145_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 21)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema2_252d_base_v146_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 21)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualema2_378d_base_v147_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 21)
    result = _ema(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasinvxinv_252d_base_v148_signal(inventory, closeadj):
    d = _f39_seasonal_inv_pattern(inventory, 252)
    result = d * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_revinvsyncxinv2_252d_base_v149_signal(revenue, inventory, closeadj):
    d = _f39_revenue_inv_sync(revenue, inventory, 252)
    result = d * inventory.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f39asq_f39_apparel_seasonality_quality_seasqualxinv_252d_base_v150_signal(revenue, inventory, closeadj):
    d = _f39_seasonality_quality(revenue, inventory, 252)
    result = d * (inventory / 1e8) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39asq_f39_apparel_seasonality_quality_seasinvxinvg_5d_base_v076_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxinvg_10d_base_v077_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxinvg_21d_base_v078_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxinvg_42d_base_v079_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxinvg_63d_base_v080_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxinvg_126d_base_v081_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxinvg_189d_base_v082_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxinvg_252d_base_v083_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxinvg_378d_base_v084_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxinvg_504d_base_v085_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_21d_base_v086_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_42d_base_v087_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_63d_base_v088_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_126d_base_v089_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_189d_base_v090_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_252d_base_v091_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_378d_base_v092_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_504d_base_v093_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_100d_base_v094_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxrg_150d_base_v095_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxrev_21d_base_v096_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxrev_42d_base_v097_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxrev_63d_base_v098_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxrev_126d_base_v099_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxrev_189d_base_v100_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxrev_252d_base_v101_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxrev_378d_base_v102_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxrev_504d_base_v103_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxrev_100d_base_v104_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxrev_150d_base_v105_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvdiff_21d_base_v106_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvdiff_42d_base_v107_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvdiff_63d_base_v108_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvdiff_126d_base_v109_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvdiff_189d_base_v110_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvdiff_252d_base_v111_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvdiff_378d_base_v112_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_21d_base_v113_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_42d_base_v114_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_63d_base_v115_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_126d_base_v116_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_189d_base_v117_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_252d_base_v118_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncdiff_378d_base_v119_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualz_42d_base_v120_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualz_63d_base_v121_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualz_126d_base_v122_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualz_189d_base_v123_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualz_252d_base_v124_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualz_378d_base_v125_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualz_504d_base_v126_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrevd_21d_base_v127_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrevd_42d_base_v128_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrevd_63d_base_v129_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrevd_126d_base_v130_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrevd_189d_base_v131_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrevd_252d_base_v132_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxrevd_378d_base_v133_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncema2_10d_base_v134_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncema2_21d_base_v135_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncema2_42d_base_v136_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncema2_63d_base_v137_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncema2_126d_base_v138_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncema2_252d_base_v139_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncema2_378d_base_v140_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema2_10d_base_v141_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema2_21d_base_v142_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema2_42d_base_v143_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema2_63d_base_v144_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema2_126d_base_v145_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema2_252d_base_v146_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualema2_378d_base_v147_signal,
    f39asq_f39_apparel_seasonality_quality_seasinvxinv_252d_base_v148_signal,
    f39asq_f39_apparel_seasonality_quality_revinvsyncxinv2_252d_base_v149_signal,
    f39asq_f39_apparel_seasonality_quality_seasqualxinv_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_APPAREL_SEASONALITY_QUALITY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "cor": cor, "inventory": inventory,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f39_seasonal_inv_pattern", "_f39_revenue_inv_sync", "_f39_seasonality_quality",)
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
    print(f"OK f39_apparel_seasonality_quality_076_150_claude: {n_features} features pass")
