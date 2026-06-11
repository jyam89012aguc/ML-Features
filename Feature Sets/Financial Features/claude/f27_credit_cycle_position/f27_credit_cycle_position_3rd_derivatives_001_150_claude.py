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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


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


def f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v001_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v002_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v003_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v004_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v005_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v006_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v007_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v008_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v009_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v010_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v011_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v012_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v013_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 21)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v014_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v015_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v016_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v017_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v018_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v019_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v020_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v021_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v022_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v023_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v024_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v025_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v026_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v027_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v028_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 63)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v029_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v030_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v031_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v032_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v033_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v034_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v035_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v036_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v037_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v038_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v039_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v040_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v041_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v042_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v043_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 126)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v044_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v045_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v046_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v047_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v048_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v049_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v050_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v051_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v052_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v053_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v054_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v055_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v056_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v057_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v058_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 252)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v059_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v060_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v061_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v062_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v063_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v064_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v065_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v066_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v067_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v068_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v069_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v070_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v071_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v072_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v073_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 21)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v074_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v075_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v076_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v077_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v078_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v079_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v080_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v081_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v082_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v083_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v084_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v085_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v086_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v087_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v088_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 63)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v089_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base.abs()
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v090_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = base * closeadj
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_42d_jerk_v091_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v092_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v093_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_42d_jerk_v094_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaled_42d_jerk_v095_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_42d_jerk_v096_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v097_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v098_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_42d_jerk_v099_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaled_42d_jerk_v100_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_42d_jerk_v101_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v102_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v103_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 126)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_42d_jerk_v104_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    base = base.abs()
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaled_42d_jerk_v105_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    base = base * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_42d_jerk_v106_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v107_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v108_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_42d_jerk_v109_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaled_42d_jerk_v110_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_42d_jerk_v111_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v112_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v113_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_42d_jerk_v114_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaled_42d_jerk_v115_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_42d_jerk_v116_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v117_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v118_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 252)
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_42d_jerk_v119_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    base = base.abs()
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaled_42d_jerk_v120_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    base = base * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_42d_jerk_v121_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v122_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v123_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_42d_jerk_v124_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaled_42d_jerk_v125_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_42d_jerk_v126_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v127_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v128_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_42d_jerk_v129_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaled_42d_jerk_v130_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_42d_jerk_v131_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v132_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v133_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_42d_jerk_v134_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    base = base.abs()
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaled_42d_jerk_v135_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    base = base * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyraw_42d_jerk_v136_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v137_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v138_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyabs_42d_jerk_v139_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_creditproxyscaled_42d_jerk_v140_signal(revenue, netinc, closeadj):
    base = _f27_credit_cycle_proxy(netinc, revenue, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintraw_42d_jerk_v141_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v142_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v143_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintabs_42d_jerk_v144_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_provintscaled_42d_jerk_v145_signal(revenue, netinc, closeadj):
    base = _f27_provision_intensity(revenue, netinc, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreraw_42d_jerk_v146_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v147_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _mean(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v148_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 21)
    base = _z(base, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescoreabs_42d_jerk_v149_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    base = base.abs()
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f27ccp_f27_credit_cycle_position_phasescorescaled_42d_jerk_v150_signal(revenue, netinc, closeadj):
    base = _f27_cycle_phase_score(revenue, netinc, 42)
    base = base * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v001_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v002_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v003_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v004_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v005_signal,
    f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v006_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v007_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v008_signal,
    f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v009_signal,
    f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v010_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v011_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v012_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v013_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v014_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v015_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v016_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v017_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v018_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v019_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v020_signal,
    f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v021_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v022_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v023_signal,
    f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v024_signal,
    f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v025_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v026_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v027_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v028_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v029_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v030_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v031_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v032_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v033_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v034_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v035_signal,
    f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v036_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v037_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v038_signal,
    f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v039_signal,
    f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v040_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v041_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v042_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v043_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v044_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v045_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v046_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v047_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v048_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v049_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v050_signal,
    f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v051_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v052_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v053_signal,
    f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v054_signal,
    f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v055_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v056_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v057_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v058_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v059_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v060_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v061_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v062_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v063_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v064_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v065_signal,
    f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v066_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v067_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v068_signal,
    f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v069_signal,
    f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v070_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v071_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v072_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v073_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v074_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v075_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_21d_jerk_v076_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v077_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v078_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_21d_jerk_v079_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaled_21d_jerk_v080_signal,
    f27ccp_f27_credit_cycle_position_provintraw_21d_jerk_v081_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v082_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v083_signal,
    f27ccp_f27_credit_cycle_position_provintabs_21d_jerk_v084_signal,
    f27ccp_f27_credit_cycle_position_provintscaled_21d_jerk_v085_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_21d_jerk_v086_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v087_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v088_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_21d_jerk_v089_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaled_21d_jerk_v090_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_42d_jerk_v091_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v092_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v093_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_42d_jerk_v094_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaled_42d_jerk_v095_signal,
    f27ccp_f27_credit_cycle_position_provintraw_42d_jerk_v096_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v097_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v098_signal,
    f27ccp_f27_credit_cycle_position_provintabs_42d_jerk_v099_signal,
    f27ccp_f27_credit_cycle_position_provintscaled_42d_jerk_v100_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_42d_jerk_v101_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v102_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v103_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_42d_jerk_v104_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaled_42d_jerk_v105_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_42d_jerk_v106_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v107_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v108_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_42d_jerk_v109_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaled_42d_jerk_v110_signal,
    f27ccp_f27_credit_cycle_position_provintraw_42d_jerk_v111_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v112_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v113_signal,
    f27ccp_f27_credit_cycle_position_provintabs_42d_jerk_v114_signal,
    f27ccp_f27_credit_cycle_position_provintscaled_42d_jerk_v115_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_42d_jerk_v116_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v117_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v118_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_42d_jerk_v119_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaled_42d_jerk_v120_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_42d_jerk_v121_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v122_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v123_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_42d_jerk_v124_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaled_42d_jerk_v125_signal,
    f27ccp_f27_credit_cycle_position_provintraw_42d_jerk_v126_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v127_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v128_signal,
    f27ccp_f27_credit_cycle_position_provintabs_42d_jerk_v129_signal,
    f27ccp_f27_credit_cycle_position_provintscaled_42d_jerk_v130_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_42d_jerk_v131_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v132_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v133_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_42d_jerk_v134_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaled_42d_jerk_v135_signal,
    f27ccp_f27_credit_cycle_position_creditproxyraw_42d_jerk_v136_signal,
    f27ccp_f27_credit_cycle_position_creditproxysm_21d_jerk_v137_signal,
    f27ccp_f27_credit_cycle_position_creditproxyz_21d_jerk_v138_signal,
    f27ccp_f27_credit_cycle_position_creditproxyabs_42d_jerk_v139_signal,
    f27ccp_f27_credit_cycle_position_creditproxyscaled_42d_jerk_v140_signal,
    f27ccp_f27_credit_cycle_position_provintraw_42d_jerk_v141_signal,
    f27ccp_f27_credit_cycle_position_provintsm_21d_jerk_v142_signal,
    f27ccp_f27_credit_cycle_position_provintz_21d_jerk_v143_signal,
    f27ccp_f27_credit_cycle_position_provintabs_42d_jerk_v144_signal,
    f27ccp_f27_credit_cycle_position_provintscaled_42d_jerk_v145_signal,
    f27ccp_f27_credit_cycle_position_phasescoreraw_42d_jerk_v146_signal,
    f27ccp_f27_credit_cycle_position_phasescoresm_21d_jerk_v147_signal,
    f27ccp_f27_credit_cycle_position_phasescorez_21d_jerk_v148_signal,
    f27ccp_f27_credit_cycle_position_phasescoreabs_42d_jerk_v149_signal,
    f27ccp_f27_credit_cycle_position_phasescorescaled_42d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_CREDIT_CYCLE_POSITION_REGISTRY_JERK_001_150 = REGISTRY


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
    print(f"OK f27_credit_cycle_position_3rd_derivatives_001_150_claude: {n_features} features pass")
