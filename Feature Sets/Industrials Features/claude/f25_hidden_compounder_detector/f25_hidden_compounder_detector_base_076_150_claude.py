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


def _f25_quiet_fcf_compound(fcf, w):
    g = fcf.pct_change(periods=w)
    mu = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return mu - sd


def _f25_low_attention_high_growth(closeadj, volume, fcf, w):
    vz = -((volume - volume.rolling(w, min_periods=max(1, w // 2)).mean())
           / volume.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan))
    g = fcf.pct_change(periods=w)
    gm = g.rolling(w, min_periods=max(1, w // 2)).mean()
    return vz + gm


def _f25_compounder_undiscovered(fcf, marketcap, w):
    yield_ = fcf / marketcap.replace(0, np.nan).abs()
    return yield_.rolling(w, min_periods=max(1, w // 2)).mean()


_FEATURES = []


def _add(fn):
    _FEATURES.append(fn)
    return fn


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_w63_base_v076_signal(fcf, closeadj):
    base = _mean(_f25_quiet_fcf_compound(fcf, 63), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_w63_base_v077_signal(closeadj, volume, fcf):
    base = _mean(_f25_low_attention_high_growth(closeadj, volume, fcf, 63), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_w63_base_v078_signal(fcf, marketcap, closeadj):
    base = _mean(_f25_compounder_undiscovered(fcf, marketcap, 63), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w252_w42_base_v079_signal(fcf, closeadj):
    base = _mean(_f25_quiet_fcf_compound(fcf, 252), 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w252_w42_base_v080_signal(closeadj, volume, fcf):
    base = _mean(_f25_low_attention_high_growth(closeadj, volume, fcf, 252), 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w252_w42_base_v081_signal(fcf, marketcap, closeadj):
    base = _mean(_f25_compounder_undiscovered(fcf, marketcap, 252), 42) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w504_w63_base_v082_signal(fcf, closeadj):
    base = _mean(_f25_quiet_fcf_compound(fcf, 504), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w504_w63_base_v083_signal(closeadj, volume, fcf):
    base = _mean(_f25_low_attention_high_growth(closeadj, volume, fcf, 504), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w504_w63_base_v084_signal(fcf, marketcap, closeadj):
    base = _mean(_f25_compounder_undiscovered(fcf, marketcap, 504), 63) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_ema21_base_v085_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_ema21_base_v086_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_ema21_base_v087_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = base.ewm(span=21, min_periods=5).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_ema252_base_v088_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_ema252_base_v089_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_ema252_base_v090_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = base.ewm(span=252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_diff21_base_v091_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_diff21_base_v092_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = (base - base.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_diff63_base_v093_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_streak_pos_base_v094_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    pos = (base > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_streak_pos_base_v095_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    pos = (base > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_streak_high_base_v096_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    high = (base > base.rolling(252, min_periods=63).median()).astype(float)
    streak = high.rolling(252, min_periods=63).sum()
    result = streak * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_above_qt_base_v097_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    qt = base.rolling(252, min_periods=63).quantile(0.5)
    ind = (base > qt).astype(float) * base
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_above_qt_base_v098_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    qt = base.rolling(252, min_periods=63).quantile(0.5)
    ind = (base > qt).astype(float) * base
    result = ind * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w42_w21_base_v099_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 42)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w42_w21_base_v100_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 42)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w42_w21_base_v101_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 42)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w189_w21_base_v102_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w189_w21_base_v103_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w189_w21_base_v104_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 189)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w378_w63_base_v105_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w378_w63_base_v106_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w378_w63_base_v107_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 378)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_w42_base_v108_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_w42_base_v109_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_w42_base_v110_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = _mean(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_w126_base_v111_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_w126_base_v112_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_w126_base_v113_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_xclose_base_v114_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    cl = closeadj / closeadj.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base * cl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_xclose_base_v115_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    cl = closeadj / closeadj.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base * cl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_xclose_base_v116_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    cl = closeadj / closeadj.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = base * cl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_xvolume_base_v117_signal(fcf, volume, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    vg = volume / (volume.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * vg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_xvolume_base_v118_signal(fcf, marketcap, volume, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    vg = volume / (volume.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * vg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_xmcap_base_v119_signal(fcf, marketcap, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    mg = marketcap / (marketcap.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * mg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_xmcap_base_v120_signal(closeadj, volume, fcf, marketcap):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    mg = marketcap / (marketcap.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = base * mg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_z63_base_v121_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_z63_base_v122_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_z63_base_v123_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_std63_base_v124_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_std63_base_v125_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_std63_base_v126_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = _std(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_med504_base_v127_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base.rolling(504, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_med504_base_v128_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base.rolling(504, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_med504_base_v129_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = base.rolling(504, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_min_504d_base_v130_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base.rolling(504, min_periods=126).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_min_504d_base_v131_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base.rolling(504, min_periods=126).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_min_504d_base_v132_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = base.rolling(504, min_periods=126).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_max_504d_base_v133_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    result = base.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_max_504d_base_v134_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    result = base.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_max_504d_base_v135_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    result = base.rolling(504, min_periods=126).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_rank63_base_v136_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    rk = base.rolling(63, min_periods=21).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_rank63_base_v137_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    rk = base.rolling(63, min_periods=21).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_rank63_base_v138_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    rk = base.rolling(63, min_periods=21).rank(pct=True)
    result = rk * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_cv_252d_base_v139_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_cv_252d_base_v140_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_cv_252d_base_v141_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    cv = _safe_div(_std(base, 252), _mean(base, 252).abs() + 1e-9)
    result = cv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w252_diff63_base_v142_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w252_diff63_base_v143_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w252_diff63_base_v144_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 252)
    result = (base - base.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_triple_z252_base_v145_signal(closeadj, volume, fcf, marketcap):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = q + l + u
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_inv_xclose_base_v146_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    cl = closeadj / closeadj.rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = (1.0 / (base.abs() + 1e-6)) * cl * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_inv_xmcap_base_v147_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    mg = marketcap / (marketcap.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = (1.0 / (base.abs() + 1e-6)) * mg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_inv_xvol_base_v148_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    vg = volume / (volume.rolling(252, min_periods=63).mean().replace(0, np.nan))
    result = (1.0 / (base.abs() + 1e-6)) * vg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_sqrt_base_v149_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_sqrt_base_v150_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63).abs()
    result = np.sqrt(base + 1e-9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_HIDDEN_COMPOUNDER_DETECTOR_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    fcf = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")

    cols = {"closeadj": closeadj, "volume": volume, "fcf": fcf, "marketcap": marketcap}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f25_quiet_fcf_compound", "_f25_low_attention_high_growth", "_f25_compounder_undiscovered")
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
    print(f"OK f25_hidden_compounder_detector_base_076_150_claude: {n_features} features pass")
