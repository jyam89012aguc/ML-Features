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
def _f19_gm_expansion(grossmargin, w):
    return grossmargin - grossmargin.shift(w)


def _f19_software_margin(grossmargin, w):
    base = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return base - 0.30


def _f19_margin_compound(grossmargin, revenue, w):
    expansion = grossmargin - grossmargin.shift(w)
    rev_growth = revenue.pct_change(periods=w)
    return expansion * rev_growth


# ===== features =====
def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v076_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 126).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v077_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 126).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v078_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 126).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v079_signal(grossmargin, closeadj):
    result = (_f19_gm_expansion(grossmargin, 126).rolling(21, min_periods=max(1, 21 // 2)).max() - _f19_gm_expansion(grossmargin, 126).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v080_signal(grossmargin, closeadj):
    result = (_f19_gm_expansion(grossmargin, 126).rolling(63, min_periods=max(1, 63 // 2)).max() - _f19_gm_expansion(grossmargin, 126).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v081_signal(grossmargin, closeadj):
    result = (_f19_gm_expansion(grossmargin, 126).rolling(252, min_periods=max(1, 252 // 2)).max() - _f19_gm_expansion(grossmargin, 126).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v082_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v083_signal(grossmargin, closeadj):
    result = _mean(_f19_gm_expansion(grossmargin, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v084_signal(grossmargin, closeadj):
    result = _mean(_f19_gm_expansion(grossmargin, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v085_signal(grossmargin, closeadj):
    result = _mean(_f19_gm_expansion(grossmargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v086_signal(grossmargin, closeadj):
    result = _std(_f19_gm_expansion(grossmargin, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v087_signal(grossmargin, closeadj):
    result = _std(_f19_gm_expansion(grossmargin, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v088_signal(grossmargin, closeadj):
    result = _std(_f19_gm_expansion(grossmargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v089_signal(grossmargin, closeadj):
    result = _z(_f19_gm_expansion(grossmargin, 252), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v090_signal(grossmargin, closeadj):
    result = _z(_f19_gm_expansion(grossmargin, 252), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v091_signal(grossmargin, closeadj):
    result = _z(_f19_gm_expansion(grossmargin, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v092_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v093_signal(grossmargin, closeadj):
    result = (-_f19_gm_expansion(grossmargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v094_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252) * _f19_gm_expansion(grossmargin, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v095_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v096_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v097_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v098_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v099_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v100_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v101_signal(grossmargin, closeadj):
    result = np.log(_f19_gm_expansion(grossmargin, 252).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v102_signal(grossmargin, closeadj):
    result = np.sign(_f19_gm_expansion(grossmargin, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v103_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v104_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v105_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 252).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v106_signal(grossmargin, closeadj):
    result = (_f19_gm_expansion(grossmargin, 252).rolling(21, min_periods=max(1, 21 // 2)).max() - _f19_gm_expansion(grossmargin, 252).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v107_signal(grossmargin, closeadj):
    result = (_f19_gm_expansion(grossmargin, 252).rolling(63, min_periods=max(1, 63 // 2)).max() - _f19_gm_expansion(grossmargin, 252).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v108_signal(grossmargin, closeadj):
    result = (_f19_gm_expansion(grossmargin, 252).rolling(252, min_periods=max(1, 252 // 2)).max() - _f19_gm_expansion(grossmargin, 252).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v109_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v110_signal(grossmargin, closeadj):
    result = _mean(_f19_gm_expansion(grossmargin, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v111_signal(grossmargin, closeadj):
    result = _mean(_f19_gm_expansion(grossmargin, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v112_signal(grossmargin, closeadj):
    result = _mean(_f19_gm_expansion(grossmargin, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v113_signal(grossmargin, closeadj):
    result = _std(_f19_gm_expansion(grossmargin, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v114_signal(grossmargin, closeadj):
    result = _std(_f19_gm_expansion(grossmargin, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v115_signal(grossmargin, closeadj):
    result = _std(_f19_gm_expansion(grossmargin, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v116_signal(grossmargin, closeadj):
    result = _z(_f19_gm_expansion(grossmargin, 5), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v117_signal(grossmargin, closeadj):
    result = _z(_f19_gm_expansion(grossmargin, 5), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v118_signal(grossmargin, closeadj):
    result = _z(_f19_gm_expansion(grossmargin, 5), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v119_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v120_signal(grossmargin, closeadj):
    result = (-_f19_gm_expansion(grossmargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v121_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5) * _f19_gm_expansion(grossmargin, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v122_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v123_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v124_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5).diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v125_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5).ewm(span=21, min_periods=max(1, 21 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v126_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5).ewm(span=63, min_periods=max(1, 63 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v127_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5).ewm(span=252, min_periods=max(1, 252 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v128_signal(grossmargin, closeadj):
    result = np.log(_f19_gm_expansion(grossmargin, 5).abs().replace(0, np.nan) + 1.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v129_signal(grossmargin, closeadj):
    result = np.sign(_f19_gm_expansion(grossmargin, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v130_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5).rolling(21, min_periods=max(1, 21 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v131_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5).rolling(63, min_periods=max(1, 63 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v132_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 5).rolling(252, min_periods=max(1, 252 // 2)).rank(pct=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v133_signal(grossmargin, closeadj):
    result = (_f19_gm_expansion(grossmargin, 5).rolling(21, min_periods=max(1, 21 // 2)).max() - _f19_gm_expansion(grossmargin, 5).rolling(21, min_periods=max(1, 21 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v134_signal(grossmargin, closeadj):
    result = (_f19_gm_expansion(grossmargin, 5).rolling(63, min_periods=max(1, 63 // 2)).max() - _f19_gm_expansion(grossmargin, 5).rolling(63, min_periods=max(1, 63 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v135_signal(grossmargin, closeadj):
    result = (_f19_gm_expansion(grossmargin, 5).rolling(252, min_periods=max(1, 252 // 2)).max() - _f19_gm_expansion(grossmargin, 5).rolling(252, min_periods=max(1, 252 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v136_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v137_signal(grossmargin, closeadj):
    result = _mean(_f19_gm_expansion(grossmargin, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v138_signal(grossmargin, closeadj):
    result = _mean(_f19_gm_expansion(grossmargin, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v139_signal(grossmargin, closeadj):
    result = _mean(_f19_gm_expansion(grossmargin, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v140_signal(grossmargin, closeadj):
    result = _std(_f19_gm_expansion(grossmargin, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v141_signal(grossmargin, closeadj):
    result = _std(_f19_gm_expansion(grossmargin, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v142_signal(grossmargin, closeadj):
    result = _std(_f19_gm_expansion(grossmargin, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v143_signal(grossmargin, closeadj):
    result = _z(_f19_gm_expansion(grossmargin, 42), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v144_signal(grossmargin, closeadj):
    result = _z(_f19_gm_expansion(grossmargin, 42), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v145_signal(grossmargin, closeadj):
    result = _z(_f19_gm_expansion(grossmargin, 42), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v146_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 42).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v147_signal(grossmargin, closeadj):
    result = (-_f19_gm_expansion(grossmargin, 42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v148_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 42) * _f19_gm_expansion(grossmargin, 42).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v149_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 42).diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v150_signal(grossmargin, closeadj):
    result = _f19_gm_expansion(grossmargin, 42).diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v076_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v077_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v078_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v079_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v080_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_126d_base_v081_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v082_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v083_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v084_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v085_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v086_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v087_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v088_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v089_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v090_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v091_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v092_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v093_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v094_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v095_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v096_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v097_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v098_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v099_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v100_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v101_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v102_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v103_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v104_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v105_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v106_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v107_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_252d_base_v108_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v109_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v110_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v111_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v112_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v113_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v114_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v115_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v116_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v117_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v118_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v119_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v120_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v121_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v122_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v123_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v124_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v125_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v126_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v127_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v128_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v129_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v130_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v131_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v132_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v133_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v134_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_5d_base_v135_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v136_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v137_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v138_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v139_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v140_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v141_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v142_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v143_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v144_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v145_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v146_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v147_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v148_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v149_signal,
    f19hgm_f19_healthit_gross_margin_expansion_gmexpansion_42d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_HEALTHIT_GROSS_MARGIN_EXPANSION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    deferredrev = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "sgna": sgna,
        "opex": opex,
        "deferredrev": deferredrev,
        "grossmargin": grossmargin,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f19_gm_expansion', '_f19_software_margin', '_f19_margin_compound')
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
    print(f"OK f19_healthit_gross_margin_expansion_base_076_150_claude: {n_features} features pass")
