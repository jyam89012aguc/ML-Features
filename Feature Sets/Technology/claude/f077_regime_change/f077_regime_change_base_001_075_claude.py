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
def _f077_signflip(s, n):
    return (np.sign(s) != np.sign(s.shift(n))).astype(float)


# 21d mean of rev_growth_signflip scaled by closeadj
def f077rch_f077_regime_change_rev_growth_signflip_mean_21d_base_v001_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rev_growth_signflip scaled by closeadj
def f077rch_f077_regime_change_rev_growth_signflip_mean_63d_base_v002_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rev_growth_signflip scaled by closeadj
def f077rch_f077_regime_change_rev_growth_signflip_mean_126d_base_v003_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rev_growth_signflip scaled by closeadj
def f077rch_f077_regime_change_rev_growth_signflip_mean_252d_base_v004_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rev_growth_signflip scaled by closeadj
def f077rch_f077_regime_change_rev_growth_signflip_mean_504d_base_v005_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ocf_signflip scaled by closeadj
def f077rch_f077_regime_change_ocf_signflip_mean_21d_base_v006_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ocf_signflip scaled by closeadj
def f077rch_f077_regime_change_ocf_signflip_mean_63d_base_v007_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ocf_signflip scaled by closeadj
def f077rch_f077_regime_change_ocf_signflip_mean_126d_base_v008_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ocf_signflip scaled by closeadj
def f077rch_f077_regime_change_ocf_signflip_mean_252d_base_v009_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ocf_signflip scaled by closeadj
def f077rch_f077_regime_change_ocf_signflip_mean_504d_base_v010_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of fcf_signflip scaled by closeadj
def f077rch_f077_regime_change_fcf_signflip_mean_21d_base_v011_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of fcf_signflip scaled by closeadj
def f077rch_f077_regime_change_fcf_signflip_mean_63d_base_v012_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of fcf_signflip scaled by closeadj
def f077rch_f077_regime_change_fcf_signflip_mean_126d_base_v013_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of fcf_signflip scaled by closeadj
def f077rch_f077_regime_change_fcf_signflip_mean_252d_base_v014_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of fcf_signflip scaled by closeadj
def f077rch_f077_regime_change_fcf_signflip_mean_504d_base_v015_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of ni_signflip scaled by closeadj
def f077rch_f077_regime_change_ni_signflip_mean_21d_base_v016_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of ni_signflip scaled by closeadj
def f077rch_f077_regime_change_ni_signflip_mean_63d_base_v017_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of ni_signflip scaled by closeadj
def f077rch_f077_regime_change_ni_signflip_mean_126d_base_v018_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of ni_signflip scaled by closeadj
def f077rch_f077_regime_change_ni_signflip_mean_252d_base_v019_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of ni_signflip scaled by closeadj
def f077rch_f077_regime_change_ni_signflip_mean_504d_base_v020_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of opinc_signflip scaled by closeadj
def f077rch_f077_regime_change_opinc_signflip_mean_21d_base_v021_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of opinc_signflip scaled by closeadj
def f077rch_f077_regime_change_opinc_signflip_mean_63d_base_v022_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of opinc_signflip scaled by closeadj
def f077rch_f077_regime_change_opinc_signflip_mean_126d_base_v023_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of opinc_signflip scaled by closeadj
def f077rch_f077_regime_change_opinc_signflip_mean_252d_base_v024_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of opinc_signflip scaled by closeadj
def f077rch_f077_regime_change_opinc_signflip_mean_504d_base_v025_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rnd_step_change scaled by closeadj
def f077rch_f077_regime_change_rnd_step_change_mean_21d_base_v026_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rnd_step_change scaled by closeadj
def f077rch_f077_regime_change_rnd_step_change_mean_63d_base_v027_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rnd_step_change scaled by closeadj
def f077rch_f077_regime_change_rnd_step_change_mean_126d_base_v028_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rnd_step_change scaled by closeadj
def f077rch_f077_regime_change_rnd_step_change_mean_252d_base_v029_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rnd_step_change scaled by closeadj
def f077rch_f077_regime_change_rnd_step_change_mean_504d_base_v030_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of regime_score scaled by closeadj
def f077rch_f077_regime_change_regime_score_mean_21d_base_v031_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of regime_score scaled by closeadj
def f077rch_f077_regime_change_regime_score_mean_63d_base_v032_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of regime_score scaled by closeadj
def f077rch_f077_regime_change_regime_score_mean_126d_base_v033_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of regime_score scaled by closeadj
def f077rch_f077_regime_change_regime_score_mean_252d_base_v034_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of regime_score scaled by closeadj
def f077rch_f077_regime_change_regime_score_mean_504d_base_v035_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_median_63d_base_v036_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_median_252d_base_v037_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_median_504d_base_v038_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_median_63d_base_v039_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_median_252d_base_v040_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_median_504d_base_v041_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_median_63d_base_v042_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_median_252d_base_v043_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_median_504d_base_v044_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of ni_signflip
def f077rch_f077_regime_change_ni_signflip_median_63d_base_v045_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of ni_signflip
def f077rch_f077_regime_change_ni_signflip_median_252d_base_v046_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of ni_signflip
def f077rch_f077_regime_change_ni_signflip_median_504d_base_v047_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_median_63d_base_v048_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_median_252d_base_v049_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_median_504d_base_v050_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_median_63d_base_v051_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_median_252d_base_v052_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_median_504d_base_v053_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of regime_score
def f077rch_f077_regime_change_regime_score_median_63d_base_v054_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of regime_score
def f077rch_f077_regime_change_regime_score_median_252d_base_v055_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of regime_score
def f077rch_f077_regime_change_regime_score_median_504d_base_v056_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_rmax_252d_base_v057_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_rmax_504d_base_v058_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_rmax_252d_base_v059_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_rmax_504d_base_v060_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_rmax_252d_base_v061_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_rmax_504d_base_v062_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of ni_signflip
def f077rch_f077_regime_change_ni_signflip_rmax_252d_base_v063_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of ni_signflip
def f077rch_f077_regime_change_ni_signflip_rmax_504d_base_v064_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_rmax_252d_base_v065_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_rmax_504d_base_v066_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_rmax_252d_base_v067_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_rmax_504d_base_v068_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of regime_score
def f077rch_f077_regime_change_regime_score_rmax_252d_base_v069_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of regime_score
def f077rch_f077_regime_change_regime_score_rmax_504d_base_v070_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_rmin_252d_base_v071_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_rmin_504d_base_v072_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_rmin_252d_base_v073_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_rmin_504d_base_v074_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_rmin_252d_base_v075_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

