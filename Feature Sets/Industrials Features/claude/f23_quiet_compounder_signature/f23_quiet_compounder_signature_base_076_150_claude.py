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
def _f23_low_vol_signal(closeadj, w):
    rets = closeadj.pct_change()
    vol = rets.rolling(w, min_periods=max(1, w // 2)).std()
    return -vol


def _f23_steady_earnings_growth(netinc, w):
    growth = netinc.pct_change(periods=w)
    mu = growth.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = growth.rolling(w, min_periods=max(1, w // 2)).std()
    return mu - sd


def _f23_compounder_composite(closeadj, netinc, w):
    lv = _f23_low_vol_signal(closeadj, w)
    se = _f23_steady_earnings_growth(netinc, w)
    return lv + se


_FEATURES = []


def _add(fn):
    _FEATURES.append(fn)
    return fn


# Use varied scaling, time horizons, and primitives.
@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_xclose2_base_v076_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_xclose2_base_v077_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_xclose2_base_v078_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = base * closeadj * closeadj / 100.0
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_sqrt_base_v079_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_sqrt_base_v080_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_sqrt_base_v081_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_abs_base_v082_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_abs_base_v083_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_abs_base_v084_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63).abs()
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_streak_pos_base_v085_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    pos = (base > base.rolling(252, min_periods=63).median()).astype(float)
    streak = pos.rolling(252, min_periods=63).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_streak_pos_base_v086_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    pos = (base > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_streak_pos_base_v087_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    pos = (base > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_w21_base_v088_signal(closeadj):
    base = _mean(_f23_low_vol_signal(closeadj, 63), 21) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w63_w21_base_v089_signal(netinc, closeadj):
    base = _mean(_f23_steady_earnings_growth(netinc, 63), 21) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w63_w21_base_v090_signal(closeadj, netinc):
    base = _mean(_f23_compounder_composite(closeadj, netinc, 63), 21) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_demean_base_v091_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_demean_base_v092_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_demean_base_v093_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = (base - _mean(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w42_base_v094_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w42_base_v095_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w42_base_v096_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w189_base_v097_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 189) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w189_base_v098_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 189) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w189_base_v099_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 189) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_z63_base_v100_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_z63_base_v101_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_z63_base_v102_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_z126_base_v103_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_z126_base_v104_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_z126_base_v105_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_std_63d_base_v106_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_std_63d_base_v107_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_std_63d_base_v108_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_std_126d_base_v109_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_std_126d_base_v110_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_std_126d_base_v111_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = _std(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_ema_252d_base_v112_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_ema_252d_base_v113_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_ema_252d_base_v114_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_cv_252d_base_v115_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_cv_252d_base_v116_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_cv_252d_base_v117_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_x_steady_w252_base_v118_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 252)
    se = _f23_steady_earnings_growth(netinc, 252)
    result = lv * se * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_triple_product_base_v119_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    c = _f23_compounder_composite(closeadj, netinc, 63)
    result = lv * se * c * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_triple_sum_base_v120_signal(closeadj, netinc):
    lv = _f23_low_vol_signal(closeadj, 63)
    se = _f23_steady_earnings_growth(netinc, 63)
    c = _f23_compounder_composite(closeadj, netinc, 63)
    result = (lv + se + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_regime_base_v121_signal(closeadj):
    a = _f23_low_vol_signal(closeadj, 63)
    b = _f23_low_vol_signal(closeadj, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_regime_base_v122_signal(netinc, closeadj):
    a = _f23_steady_earnings_growth(netinc, 63)
    b = _f23_steady_earnings_growth(netinc, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_regime_base_v123_signal(closeadj, netinc):
    a = _f23_compounder_composite(closeadj, netinc, 63)
    b = _f23_compounder_composite(closeadj, netinc, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_x_eps_base_v124_signal(closeadj, eps):
    base = _f23_low_vol_signal(closeadj, 63)
    pg = eps / (eps.rolling(252, min_periods=63).mean().replace(0, np.nan).abs() + 1e-9)
    result = base * pg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_x_eps_base_v125_signal(netinc, eps, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    pg = eps / (eps.rolling(252, min_periods=63).mean().replace(0, np.nan).abs() + 1e-9)
    result = base * pg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_x_eps_base_v126_signal(closeadj, netinc, eps):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    pg = eps / (eps.rolling(252, min_periods=63).mean().replace(0, np.nan).abs() + 1e-9)
    result = base * pg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_x_ebitda_base_v127_signal(closeadj, ebitda):
    base = _f23_low_vol_signal(closeadj, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_x_ebitda_base_v128_signal(netinc, ebitda, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_x_ebitda_base_v129_signal(closeadj, netinc, ebitda):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    eg = ebitda / (ebitda.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * eg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_log_base_v130_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63).abs() + 1e-9
    result = np.log(base + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w_42_z252_base_v131_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 42)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w_42_z252_base_v132_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 42)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w_42_z252_base_v133_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 42)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w_252_w_42_base_v134_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 252)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w_252_w_42_base_v135_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 252)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w_252_w_42_base_v136_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 252)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w_252_w_126_base_v137_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w_252_w_126_base_v138_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w_252_w_126_base_v139_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w_504_w_63_base_v140_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_w_504_w_63_base_v141_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w_504_w_63_base_v142_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 504)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_min_252d_base_v143_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_min_252d_base_v144_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    result = base.rolling(252, min_periods=63).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_max_252d_base_v145_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    result = base.rolling(252, min_periods=63).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_x_close_base_v146_signal(closeadj):
    base = _f23_low_vol_signal(closeadj, 63)
    cl = closeadj / closeadj.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base * cl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_steady_x_close_base_v147_signal(netinc, closeadj):
    base = _f23_steady_earnings_growth(netinc, 63)
    cl = closeadj / closeadj.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base * cl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_x_close_base_v148_signal(closeadj, netinc):
    base = _f23_compounder_composite(closeadj, netinc, 63)
    cl = closeadj / closeadj.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base * cl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_lowvol_w63_w63_base_v149_signal(closeadj):
    base = _mean(_f23_low_vol_signal(closeadj, 63), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f23qcs_f23_quiet_compounder_signature_composite_w_w63_base_v150_signal(closeadj, netinc):
    base = _mean(_f23_compounder_composite(closeadj, netinc, 63), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_QUIET_COMPOUNDER_SIGNATURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")

    cols = {"closeadj": closeadj, "netinc": netinc, "ebitda": ebitda, "eps": eps}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f23_low_vol_signal", "_f23_steady_earnings_growth", "_f23_compounder_composite")
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
    print(f"OK f23_quiet_compounder_signature_base_076_150_claude: {n_features} features pass")
