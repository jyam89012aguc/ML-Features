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


# 63d z-score of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_z_63d_base_v076_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_z_126d_base_v077_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_z_252d_base_v078_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_z_504d_base_v079_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_z_63d_base_v080_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_z_126d_base_v081_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_z_252d_base_v082_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_z_504d_base_v083_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_z_63d_base_v084_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_z_126d_base_v085_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_z_252d_base_v086_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_z_504d_base_v087_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ni_signflip
def f077rch_f077_regime_change_ni_signflip_z_63d_base_v088_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ni_signflip
def f077rch_f077_regime_change_ni_signflip_z_126d_base_v089_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ni_signflip
def f077rch_f077_regime_change_ni_signflip_z_252d_base_v090_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ni_signflip
def f077rch_f077_regime_change_ni_signflip_z_504d_base_v091_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_z_63d_base_v092_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_z_126d_base_v093_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_z_252d_base_v094_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_z_504d_base_v095_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_z_63d_base_v096_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_z_126d_base_v097_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_z_252d_base_v098_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_z_504d_base_v099_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of regime_score
def f077rch_f077_regime_change_regime_score_z_63d_base_v100_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of regime_score
def f077rch_f077_regime_change_regime_score_z_126d_base_v101_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of regime_score
def f077rch_f077_regime_change_regime_score_z_252d_base_v102_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of regime_score
def f077rch_f077_regime_change_regime_score_z_504d_base_v103_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_distmax_252d_base_v104_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_distmax_504d_base_v105_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_distmax_252d_base_v106_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_distmax_504d_base_v107_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_distmax_252d_base_v108_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_distmax_504d_base_v109_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ni_signflip
def f077rch_f077_regime_change_ni_signflip_distmax_252d_base_v110_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ni_signflip
def f077rch_f077_regime_change_ni_signflip_distmax_504d_base_v111_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_distmax_252d_base_v112_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_distmax_504d_base_v113_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_distmax_252d_base_v114_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_distmax_504d_base_v115_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of regime_score
def f077rch_f077_regime_change_regime_score_distmax_252d_base_v116_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of regime_score
def f077rch_f077_regime_change_regime_score_distmax_504d_base_v117_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_distmed_126d_base_v118_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_distmed_252d_base_v119_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_distmed_504d_base_v120_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_distmed_126d_base_v121_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_distmed_252d_base_v122_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_distmed_504d_base_v123_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_distmed_126d_base_v124_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_distmed_252d_base_v125_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_distmed_504d_base_v126_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ni_signflip
def f077rch_f077_regime_change_ni_signflip_distmed_126d_base_v127_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ni_signflip
def f077rch_f077_regime_change_ni_signflip_distmed_252d_base_v128_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ni_signflip
def f077rch_f077_regime_change_ni_signflip_distmed_504d_base_v129_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_distmed_126d_base_v130_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_distmed_252d_base_v131_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_distmed_504d_base_v132_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_distmed_126d_base_v133_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_distmed_252d_base_v134_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_distmed_504d_base_v135_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of regime_score
def f077rch_f077_regime_change_regime_score_distmed_126d_base_v136_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of regime_score
def f077rch_f077_regime_change_regime_score_distmed_252d_base_v137_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of regime_score
def f077rch_f077_regime_change_regime_score_distmed_504d_base_v138_signal(ncfo, fcf, netinc, closeadj):
    base = ((ncfo > 0).astype(float) + (fcf > 0).astype(float) + (netinc > 0).astype(float))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_chg_63d_base_v139_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rev_growth_signflip
def f077rch_f077_regime_change_rev_growth_signflip_chg_252d_base_v140_signal(revenue, closeadj):
    base = _f077_signflip(revenue.pct_change(periods=252), 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_chg_63d_base_v141_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ocf_signflip
def f077rch_f077_regime_change_ocf_signflip_chg_252d_base_v142_signal(ncfo, closeadj):
    base = _f077_signflip(ncfo, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_chg_63d_base_v143_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in fcf_signflip
def f077rch_f077_regime_change_fcf_signflip_chg_252d_base_v144_signal(fcf, closeadj):
    base = _f077_signflip(fcf, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ni_signflip
def f077rch_f077_regime_change_ni_signflip_chg_63d_base_v145_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ni_signflip
def f077rch_f077_regime_change_ni_signflip_chg_252d_base_v146_signal(netinc, closeadj):
    base = _f077_signflip(netinc, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_chg_63d_base_v147_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in opinc_signflip
def f077rch_f077_regime_change_opinc_signflip_chg_252d_base_v148_signal(opinc, closeadj):
    base = _f077_signflip(opinc, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_chg_63d_base_v149_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in rnd_step_change
def f077rch_f077_regime_change_rnd_step_change_chg_252d_base_v150_signal(rnd, closeadj):
    base = (rnd.pct_change(periods=63).abs() > 0.5).astype(float)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

