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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f27_credit_cycle_proxy(netinc, revenue, w):
    margin = netinc / revenue.replace(0, np.nan)
    return margin - margin.rolling(w, min_periods=max(1, w // 2)).mean()


def _f27_provision_intensity(revenue, netinc, w):
    gap = (revenue - netinc) / revenue.replace(0, np.nan)
    return gap - gap.rolling(w, min_periods=max(1, w // 2)).mean()


def _f27_cycle_phase_score(revenue, netinc, w):
    rg = revenue.pct_change(periods=w)
    ng = netinc.pct_change(periods=w)
    return ng - rg


def f27ccp_f27_credit_cycle_position_creditproxyrawsdn_21d_slope_v001_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysmsdn_21d_slope_v002_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyzsdn_21d_slope_v003_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabssdn_21d_slope_v004_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaledsdn_21d_slope_v005_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrawpct_21d_slope_v006_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysmpct_21d_slope_v007_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyzpct_21d_slope_v008_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabspct_21d_slope_v009_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaledpct_21d_slope_v010_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrawsdn_21d_slope_v011_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsmsdn_21d_slope_v012_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintzsdn_21d_slope_v013_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabssdn_21d_slope_v014_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaledsdn_21d_slope_v015_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrawpct_21d_slope_v016_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsmpct_21d_slope_v017_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintzpct_21d_slope_v018_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabspct_21d_slope_v019_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaledpct_21d_slope_v020_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerawsdn_21d_slope_v021_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresmsdn_21d_slope_v022_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorezsdn_21d_slope_v023_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabssdn_21d_slope_v024_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaledsdn_21d_slope_v025_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerawpct_21d_slope_v026_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresmpct_21d_slope_v027_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorezpct_21d_slope_v028_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabspct_21d_slope_v029_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaledpct_21d_slope_v030_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrawsdn_21d_slope_v031_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysmsdn_21d_slope_v032_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyzsdn_21d_slope_v033_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabssdn_21d_slope_v034_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaledsdn_21d_slope_v035_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrawpct_21d_slope_v036_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysmpct_21d_slope_v037_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyzpct_21d_slope_v038_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabspct_21d_slope_v039_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaledpct_21d_slope_v040_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrawsdn_21d_slope_v041_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsmsdn_21d_slope_v042_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintzsdn_21d_slope_v043_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabssdn_21d_slope_v044_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaledsdn_21d_slope_v045_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrawpct_21d_slope_v046_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsmpct_21d_slope_v047_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintzpct_21d_slope_v048_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabspct_21d_slope_v049_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaledpct_21d_slope_v050_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerawsdn_21d_slope_v051_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresmsdn_21d_slope_v052_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorezsdn_21d_slope_v053_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabssdn_21d_slope_v054_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaledsdn_21d_slope_v055_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerawpct_21d_slope_v056_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresmpct_21d_slope_v057_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorezpct_21d_slope_v058_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabspct_21d_slope_v059_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaledpct_21d_slope_v060_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrawsdn_21d_slope_v061_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysmsdn_21d_slope_v062_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyzsdn_21d_slope_v063_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabssdn_21d_slope_v064_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaledsdn_21d_slope_v065_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrawpct_21d_slope_v066_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysmpct_21d_slope_v067_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyzpct_21d_slope_v068_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabspct_21d_slope_v069_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaledpct_21d_slope_v070_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrawsdn_21d_slope_v071_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsmsdn_21d_slope_v072_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintzsdn_21d_slope_v073_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabssdn_21d_slope_v074_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaledsdn_21d_slope_v075_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrawpct_21d_slope_v076_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsmpct_21d_slope_v077_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintzpct_21d_slope_v078_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabspct_21d_slope_v079_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaledpct_21d_slope_v080_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerawsdn_21d_slope_v081_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresmsdn_21d_slope_v082_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorezsdn_21d_slope_v083_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabssdn_21d_slope_v084_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaledsdn_21d_slope_v085_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerawpct_21d_slope_v086_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresmpct_21d_slope_v087_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorezpct_21d_slope_v088_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 126)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabspct_21d_slope_v089_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaledpct_21d_slope_v090_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrawsdn_21d_slope_v091_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysmsdn_21d_slope_v092_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyzsdn_21d_slope_v093_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabssdn_21d_slope_v094_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaledsdn_21d_slope_v095_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrawpct_21d_slope_v096_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysmpct_21d_slope_v097_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyzpct_21d_slope_v098_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabspct_21d_slope_v099_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaledpct_21d_slope_v100_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrawsdn_21d_slope_v101_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsmsdn_21d_slope_v102_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintzsdn_21d_slope_v103_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabssdn_21d_slope_v104_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaledsdn_21d_slope_v105_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrawpct_21d_slope_v106_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsmpct_21d_slope_v107_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintzpct_21d_slope_v108_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabspct_21d_slope_v109_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaledpct_21d_slope_v110_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerawsdn_21d_slope_v111_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresmsdn_21d_slope_v112_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorezsdn_21d_slope_v113_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabssdn_21d_slope_v114_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaledsdn_21d_slope_v115_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerawpct_21d_slope_v116_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresmpct_21d_slope_v117_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorezpct_21d_slope_v118_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 252)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabspct_21d_slope_v119_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaledpct_21d_slope_v120_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrawsdn_21d_slope_v121_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysmsdn_21d_slope_v122_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyzsdn_21d_slope_v123_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabssdn_21d_slope_v124_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaledsdn_21d_slope_v125_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyrawpct_21d_slope_v126_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysmpct_21d_slope_v127_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyzpct_21d_slope_v128_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabspct_21d_slope_v129_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaledpct_21d_slope_v130_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrawsdn_21d_slope_v131_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsmsdn_21d_slope_v132_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintzsdn_21d_slope_v133_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabssdn_21d_slope_v134_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaledsdn_21d_slope_v135_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintrawpct_21d_slope_v136_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsmpct_21d_slope_v137_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintzpct_21d_slope_v138_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabspct_21d_slope_v139_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaledpct_21d_slope_v140_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerawsdn_21d_slope_v141_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresmsdn_21d_slope_v142_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorezsdn_21d_slope_v143_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabssdn_21d_slope_v144_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaledsdn_21d_slope_v145_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorerawpct_21d_slope_v146_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresmpct_21d_slope_v147_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorezpct_21d_slope_v148_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 21)
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabspct_21d_slope_v149_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaledpct_21d_slope_v150_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f27ccp_f27_credit_cycle_position_creditproxyrawsdn_21d_slope_v001_signal,
    f27ccp_f27_credit_cycle_position_creditproxysmsdn_21d_slope_v002_signal,
    f27ccp_f27_credit_cycle_position_creditproxyzsdn_21d_slope_v003_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabssdn_21d_slope_v004_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaledsdn_21d_slope_v005_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrawpct_21d_slope_v006_signal,
    f27ccp_f27_credit_cycle_position_creditproxysmpct_21d_slope_v007_signal,
    f27ccp_f27_credit_cycle_position_creditproxyzpct_21d_slope_v008_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabspct_21d_slope_v009_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaledpct_21d_slope_v010_signal,
    f27ccp_f27_credit_cycle_position_provintrawsdn_21d_slope_v011_signal,
    f27ccp_f27_credit_cycle_position_provintsmsdn_21d_slope_v012_signal,
    f27ccp_f27_credit_cycle_position_provintzsdn_21d_slope_v013_signal,
    f27ccp_f27_credit_cycle_position_provintabssdn_21d_slope_v014_signal,
    f27ccp_f27_credit_cycle_position_provintscaledsdn_21d_slope_v015_signal,
    f27ccp_f27_credit_cycle_position_provintrawpct_21d_slope_v016_signal,
    f27ccp_f27_credit_cycle_position_provintsmpct_21d_slope_v017_signal,
    f27ccp_f27_credit_cycle_position_provintzpct_21d_slope_v018_signal,
    f27ccp_f27_credit_cycle_position_provintabspct_21d_slope_v019_signal,
    f27ccp_f27_credit_cycle_position_provintscaledpct_21d_slope_v020_signal,
    f27ccp_f27_credit_cycle_position_phasescorerawsdn_21d_slope_v021_signal,
    f27ccp_f27_credit_cycle_position_phasescoresmsdn_21d_slope_v022_signal,
    f27ccp_f27_credit_cycle_position_phasescorezsdn_21d_slope_v023_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabssdn_21d_slope_v024_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaledsdn_21d_slope_v025_signal,
    f27ccp_f27_credit_cycle_position_phasescorerawpct_21d_slope_v026_signal,
    f27ccp_f27_credit_cycle_position_phasescoresmpct_21d_slope_v027_signal,
    f27ccp_f27_credit_cycle_position_phasescorezpct_21d_slope_v028_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabspct_21d_slope_v029_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaledpct_21d_slope_v030_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrawsdn_21d_slope_v031_signal,
    f27ccp_f27_credit_cycle_position_creditproxysmsdn_21d_slope_v032_signal,
    f27ccp_f27_credit_cycle_position_creditproxyzsdn_21d_slope_v033_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabssdn_21d_slope_v034_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaledsdn_21d_slope_v035_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrawpct_21d_slope_v036_signal,
    f27ccp_f27_credit_cycle_position_creditproxysmpct_21d_slope_v037_signal,
    f27ccp_f27_credit_cycle_position_creditproxyzpct_21d_slope_v038_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabspct_21d_slope_v039_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaledpct_21d_slope_v040_signal,
    f27ccp_f27_credit_cycle_position_provintrawsdn_21d_slope_v041_signal,
    f27ccp_f27_credit_cycle_position_provintsmsdn_21d_slope_v042_signal,
    f27ccp_f27_credit_cycle_position_provintzsdn_21d_slope_v043_signal,
    f27ccp_f27_credit_cycle_position_provintabssdn_21d_slope_v044_signal,
    f27ccp_f27_credit_cycle_position_provintscaledsdn_21d_slope_v045_signal,
    f27ccp_f27_credit_cycle_position_provintrawpct_21d_slope_v046_signal,
    f27ccp_f27_credit_cycle_position_provintsmpct_21d_slope_v047_signal,
    f27ccp_f27_credit_cycle_position_provintzpct_21d_slope_v048_signal,
    f27ccp_f27_credit_cycle_position_provintabspct_21d_slope_v049_signal,
    f27ccp_f27_credit_cycle_position_provintscaledpct_21d_slope_v050_signal,
    f27ccp_f27_credit_cycle_position_phasescorerawsdn_21d_slope_v051_signal,
    f27ccp_f27_credit_cycle_position_phasescoresmsdn_21d_slope_v052_signal,
    f27ccp_f27_credit_cycle_position_phasescorezsdn_21d_slope_v053_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabssdn_21d_slope_v054_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaledsdn_21d_slope_v055_signal,
    f27ccp_f27_credit_cycle_position_phasescorerawpct_21d_slope_v056_signal,
    f27ccp_f27_credit_cycle_position_phasescoresmpct_21d_slope_v057_signal,
    f27ccp_f27_credit_cycle_position_phasescorezpct_21d_slope_v058_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabspct_21d_slope_v059_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaledpct_21d_slope_v060_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrawsdn_21d_slope_v061_signal,
    f27ccp_f27_credit_cycle_position_creditproxysmsdn_21d_slope_v062_signal,
    f27ccp_f27_credit_cycle_position_creditproxyzsdn_21d_slope_v063_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabssdn_21d_slope_v064_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaledsdn_21d_slope_v065_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrawpct_21d_slope_v066_signal,
    f27ccp_f27_credit_cycle_position_creditproxysmpct_21d_slope_v067_signal,
    f27ccp_f27_credit_cycle_position_creditproxyzpct_21d_slope_v068_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabspct_21d_slope_v069_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaledpct_21d_slope_v070_signal,
    f27ccp_f27_credit_cycle_position_provintrawsdn_21d_slope_v071_signal,
    f27ccp_f27_credit_cycle_position_provintsmsdn_21d_slope_v072_signal,
    f27ccp_f27_credit_cycle_position_provintzsdn_21d_slope_v073_signal,
    f27ccp_f27_credit_cycle_position_provintabssdn_21d_slope_v074_signal,
    f27ccp_f27_credit_cycle_position_provintscaledsdn_21d_slope_v075_signal,
    f27ccp_f27_credit_cycle_position_provintrawpct_21d_slope_v076_signal,
    f27ccp_f27_credit_cycle_position_provintsmpct_21d_slope_v077_signal,
    f27ccp_f27_credit_cycle_position_provintzpct_21d_slope_v078_signal,
    f27ccp_f27_credit_cycle_position_provintabspct_21d_slope_v079_signal,
    f27ccp_f27_credit_cycle_position_provintscaledpct_21d_slope_v080_signal,
    f27ccp_f27_credit_cycle_position_phasescorerawsdn_21d_slope_v081_signal,
    f27ccp_f27_credit_cycle_position_phasescoresmsdn_21d_slope_v082_signal,
    f27ccp_f27_credit_cycle_position_phasescorezsdn_21d_slope_v083_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabssdn_21d_slope_v084_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaledsdn_21d_slope_v085_signal,
    f27ccp_f27_credit_cycle_position_phasescorerawpct_21d_slope_v086_signal,
    f27ccp_f27_credit_cycle_position_phasescoresmpct_21d_slope_v087_signal,
    f27ccp_f27_credit_cycle_position_phasescorezpct_21d_slope_v088_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabspct_21d_slope_v089_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaledpct_21d_slope_v090_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrawsdn_21d_slope_v091_signal,
    f27ccp_f27_credit_cycle_position_creditproxysmsdn_21d_slope_v092_signal,
    f27ccp_f27_credit_cycle_position_creditproxyzsdn_21d_slope_v093_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabssdn_21d_slope_v094_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaledsdn_21d_slope_v095_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrawpct_21d_slope_v096_signal,
    f27ccp_f27_credit_cycle_position_creditproxysmpct_21d_slope_v097_signal,
    f27ccp_f27_credit_cycle_position_creditproxyzpct_21d_slope_v098_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabspct_21d_slope_v099_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaledpct_21d_slope_v100_signal,
    f27ccp_f27_credit_cycle_position_provintrawsdn_21d_slope_v101_signal,
    f27ccp_f27_credit_cycle_position_provintsmsdn_21d_slope_v102_signal,
    f27ccp_f27_credit_cycle_position_provintzsdn_21d_slope_v103_signal,
    f27ccp_f27_credit_cycle_position_provintabssdn_21d_slope_v104_signal,
    f27ccp_f27_credit_cycle_position_provintscaledsdn_21d_slope_v105_signal,
    f27ccp_f27_credit_cycle_position_provintrawpct_21d_slope_v106_signal,
    f27ccp_f27_credit_cycle_position_provintsmpct_21d_slope_v107_signal,
    f27ccp_f27_credit_cycle_position_provintzpct_21d_slope_v108_signal,
    f27ccp_f27_credit_cycle_position_provintabspct_21d_slope_v109_signal,
    f27ccp_f27_credit_cycle_position_provintscaledpct_21d_slope_v110_signal,
    f27ccp_f27_credit_cycle_position_phasescorerawsdn_21d_slope_v111_signal,
    f27ccp_f27_credit_cycle_position_phasescoresmsdn_21d_slope_v112_signal,
    f27ccp_f27_credit_cycle_position_phasescorezsdn_21d_slope_v113_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabssdn_21d_slope_v114_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaledsdn_21d_slope_v115_signal,
    f27ccp_f27_credit_cycle_position_phasescorerawpct_21d_slope_v116_signal,
    f27ccp_f27_credit_cycle_position_phasescoresmpct_21d_slope_v117_signal,
    f27ccp_f27_credit_cycle_position_phasescorezpct_21d_slope_v118_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabspct_21d_slope_v119_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaledpct_21d_slope_v120_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrawsdn_21d_slope_v121_signal,
    f27ccp_f27_credit_cycle_position_creditproxysmsdn_21d_slope_v122_signal,
    f27ccp_f27_credit_cycle_position_creditproxyzsdn_21d_slope_v123_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabssdn_21d_slope_v124_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaledsdn_21d_slope_v125_signal,
    f27ccp_f27_credit_cycle_position_creditproxyrawpct_21d_slope_v126_signal,
    f27ccp_f27_credit_cycle_position_creditproxysmpct_21d_slope_v127_signal,
    f27ccp_f27_credit_cycle_position_creditproxyzpct_21d_slope_v128_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabspct_21d_slope_v129_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaledpct_21d_slope_v130_signal,
    f27ccp_f27_credit_cycle_position_provintrawsdn_21d_slope_v131_signal,
    f27ccp_f27_credit_cycle_position_provintsmsdn_21d_slope_v132_signal,
    f27ccp_f27_credit_cycle_position_provintzsdn_21d_slope_v133_signal,
    f27ccp_f27_credit_cycle_position_provintabssdn_21d_slope_v134_signal,
    f27ccp_f27_credit_cycle_position_provintscaledsdn_21d_slope_v135_signal,
    f27ccp_f27_credit_cycle_position_provintrawpct_21d_slope_v136_signal,
    f27ccp_f27_credit_cycle_position_provintsmpct_21d_slope_v137_signal,
    f27ccp_f27_credit_cycle_position_provintzpct_21d_slope_v138_signal,
    f27ccp_f27_credit_cycle_position_provintabspct_21d_slope_v139_signal,
    f27ccp_f27_credit_cycle_position_provintscaledpct_21d_slope_v140_signal,
    f27ccp_f27_credit_cycle_position_phasescorerawsdn_21d_slope_v141_signal,
    f27ccp_f27_credit_cycle_position_phasescoresmsdn_21d_slope_v142_signal,
    f27ccp_f27_credit_cycle_position_phasescorezsdn_21d_slope_v143_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabssdn_21d_slope_v144_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaledsdn_21d_slope_v145_signal,
    f27ccp_f27_credit_cycle_position_phasescorerawpct_21d_slope_v146_signal,
    f27ccp_f27_credit_cycle_position_phasescoresmpct_21d_slope_v147_signal,
    f27ccp_f27_credit_cycle_position_phasescorezpct_21d_slope_v148_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabspct_21d_slope_v149_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaledpct_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CREDIT_CYCLE_POSITION_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")

    cols = {"revenue": revenue, "netinc": netinc, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_credit_cycle_proxy", "_f27_provision_intensity", "_f27_cycle_phase_score")
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
    print(f"OK f27_credit_cycle_position_2nd_derivatives_001_150_claude: {n_features} features pass")
