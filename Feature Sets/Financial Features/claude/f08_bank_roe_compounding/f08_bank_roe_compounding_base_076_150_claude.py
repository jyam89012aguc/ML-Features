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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _logret(s, w):
    return np.log(s.replace(0, np.nan)).diff(periods=w)


def _f08_roe_trajectory(roe, w):
    return roe.rolling(w, min_periods=max(1, w // 2)).mean()


def _f08_roe_persistence(roe, w):
    m = roe.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = roe.rolling(w, min_periods=max(1, w // 2)).std()
    return m / sd.replace(0, np.nan)


def _f08_roe_quality(roe, roa, w):
    spread = roe - roa
    return spread.rolling(w, min_periods=max(1, w // 2)).mean()


def f08roc_f08_bank_roe_compounding_roequalxpers_126d_base_v076_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    p = _f08_roe_persistence(roe, 126)
    result = q * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxpers_252d_base_v077_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    p = _f08_roe_persistence(roe, 252)
    result = q * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajlog_21d_base_v078_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21).abs()
    result = np.log(tr.replace(0, np.nan)) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajlog_63d_base_v079_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63).abs()
    result = np.log(tr.replace(0, np.nan)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajlog_252d_base_v080_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252).abs()
    result = np.log(tr.replace(0, np.nan)) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roerange_21d_base_v081_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    rng = tr.rolling(21, min_periods=max(1, 21//2)).max() - tr.rolling(21, min_periods=max(1, 21//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roerange_63d_base_v082_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    rng = tr.rolling(63, min_periods=max(1, 63//2)).max() - tr.rolling(63, min_periods=max(1, 63//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roerange_126d_base_v083_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    rng = tr.rolling(126, min_periods=max(1, 126//2)).max() - tr.rolling(126, min_periods=max(1, 126//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roerange_252d_base_v084_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    rng = tr.rolling(252, min_periods=max(1, 252//2)).max() - tr.rolling(252, min_periods=max(1, 252//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajratio_21v63_base_v085_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 21)
    b = _f08_roe_trajectory(roe, 63)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajdiff_21m63_base_v086_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 21)
    b = _f08_roe_trajectory(roe, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajratio_63v252_base_v087_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 63)
    b = _f08_roe_trajectory(roe, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajdiff_63m252_base_v088_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 63)
    b = _f08_roe_trajectory(roe, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajratio_126v504_base_v089_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 126)
    b = _f08_roe_trajectory(roe, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajdiff_126m504_base_v090_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 126)
    b = _f08_roe_trajectory(roe, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajratio_42v189_base_v091_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 42)
    b = _f08_roe_trajectory(roe, 189)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajdiff_42m189_base_v092_signal(roe, closeadj):
    a = _f08_roe_trajectory(roe, 42)
    b = _f08_roe_trajectory(roe, 189)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roedev_21d_base_v093_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    result = (tr - _ema(tr, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roedev_63d_base_v094_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    result = (tr - _ema(tr, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roedev_126d_base_v095_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    result = (tr - _ema(tr, 126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roedev_252d_base_v096_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    result = (tr - _ema(tr, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersratio_63v252_base_v097_signal(roe, closeadj):
    a = _f08_roe_persistence(roe, 63)
    b = _f08_roe_persistence(roe, 252)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersratio_126v504_base_v098_signal(roe, closeadj):
    a = _f08_roe_persistence(roe, 126)
    b = _f08_roe_persistence(roe, 504)
    result = (a / b.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrange_63d_base_v099_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    rng = q.rolling(63, min_periods=max(1, 63//2)).max() - q.rolling(63, min_periods=max(1, 63//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrange_126d_base_v100_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    rng = q.rolling(126, min_periods=max(1, 126//2)).max() - q.rolling(126, min_periods=max(1, 126//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalrange_252d_base_v101_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    rng = q.rolling(252, min_periods=max(1, 252//2)).max() - q.rolling(252, min_periods=max(1, 252//2)).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxequity_21d_base_v102_signal(roe, equity, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    e_chg = equity.pct_change(periods=21)
    result = tr * e_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxequity_63d_base_v103_signal(roe, equity, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    e_chg = equity.pct_change(periods=63)
    result = tr * e_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxequity_126d_base_v104_signal(roe, equity, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    e_chg = equity.pct_change(periods=126)
    result = tr * e_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxequity_252d_base_v105_signal(roe, equity, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    e_chg = equity.pct_change(periods=252)
    result = tr * e_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roetrajxequity_504d_base_v106_signal(roe, equity, closeadj):
    tr = _f08_roe_trajectory(roe, 504)
    e_chg = equity.pct_change(periods=504)
    result = tr * e_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxequity_21d_base_v107_signal(roe, roa, equity, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    e_chg = equity.pct_change(periods=21)
    result = q * e_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxequity_63d_base_v108_signal(roe, roa, equity, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    e_chg = equity.pct_change(periods=63)
    result = q * e_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxequity_126d_base_v109_signal(roe, roa, equity, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    e_chg = equity.pct_change(periods=126)
    result = q * e_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalxequity_252d_base_v110_signal(roe, roa, equity, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    e_chg = equity.pct_change(periods=252)
    result = q * e_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roecompound_63d_base_v111_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    result = (tr - tr.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roecompound_126d_base_v112_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    result = (tr - tr.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roecompound_252d_base_v113_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    result = (tr - tr.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roecompound_504d_base_v114_signal(roe, closeadj):
    tr = _f08_roe_trajectory(roe, 504)
    result = (tr - tr.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersema_10d_base_v115_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 10)
    result = _ema(p, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersema_21d_base_v116_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 21)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersema_63d_base_v117_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 63)
    result = _ema(p, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersema_126d_base_v118_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 126)
    result = _ema(p, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersema_252d_base_v119_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 252)
    result = _ema(p, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roeperschg_5d_base_v120_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 5)
    result = p.diff(periods=5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roeperschg_21d_base_v121_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 21)
    result = p.diff(periods=21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roeperschg_63d_base_v122_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 63)
    result = p.diff(periods=63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roeperschg_126d_base_v123_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 126)
    result = p.diff(periods=126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roeperschg_252d_base_v124_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 252)
    result = p.diff(periods=252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_21d_base_v125_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    ra = _f08_roe_trajectory(roa, 21)
    result = (tr - ra) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_42d_base_v126_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 42)
    ra = _f08_roe_trajectory(roa, 42)
    result = (tr - ra) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_63d_base_v127_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    ra = _f08_roe_trajectory(roa, 63)
    result = (tr - ra) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_126d_base_v128_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    ra = _f08_roe_trajectory(roa, 126)
    result = (tr - ra) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_189d_base_v129_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 189)
    ra = _f08_roe_trajectory(roa, 189)
    result = (tr - ra) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_252d_base_v130_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    ra = _f08_roe_trajectory(roa, 252)
    result = (tr - ra) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_378d_base_v131_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 378)
    ra = _f08_roe_trajectory(roa, 378)
    result = (tr - ra) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroadiff_504d_base_v132_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 504)
    ra = _f08_roe_trajectory(roa, 504)
    result = (tr - ra) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_21d_base_v133_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 21)
    ra = _f08_roe_trajectory(roa, 21)
    result = (tr / ra.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_42d_base_v134_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 42)
    ra = _f08_roe_trajectory(roa, 42)
    result = (tr / ra.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_63d_base_v135_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 63)
    ra = _f08_roe_trajectory(roa, 63)
    result = (tr / ra.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_126d_base_v136_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 126)
    ra = _f08_roe_trajectory(roa, 126)
    result = (tr / ra.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_189d_base_v137_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 189)
    ra = _f08_roe_trajectory(roa, 189)
    result = (tr / ra.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_252d_base_v138_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 252)
    ra = _f08_roe_trajectory(roa, 252)
    result = (tr / ra.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_378d_base_v139_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 378)
    ra = _f08_roe_trajectory(roa, 378)
    result = (tr / ra.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roexroaratio_504d_base_v140_signal(roe, roa, closeadj):
    tr = _f08_roe_trajectory(roe, 504)
    ra = _f08_roe_trajectory(roa, 504)
    result = (tr / ra.replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_21d_base_v141_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 21)
    p = _f08_roe_persistence(roe, 21)
    result = _ema(q, 21) * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_42d_base_v142_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 42)
    p = _f08_roe_persistence(roe, 42)
    result = _ema(q, 42) * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_63d_base_v143_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 63)
    p = _f08_roe_persistence(roe, 63)
    result = _ema(q, 63) * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_126d_base_v144_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 126)
    p = _f08_roe_persistence(roe, 126)
    result = _ema(q, 126) * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_189d_base_v145_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 189)
    p = _f08_roe_persistence(roe, 189)
    result = _ema(q, 189) * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roequalemaxpers_252d_base_v146_signal(roe, roa, closeadj):
    q = _f08_roe_quality(roe, roa, 252)
    p = _f08_roe_persistence(roe, 252)
    result = _ema(q, 252) * p * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersxvol_21d_base_v147_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 21)
    rv = _std(closeadj.pct_change(), 21)
    result = p * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersxvol_42d_base_v148_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 42)
    rv = _std(closeadj.pct_change(), 42)
    result = p * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersxvol_63d_base_v149_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 63)
    rv = _std(closeadj.pct_change(), 63)
    result = p * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f08roc_f08_bank_roe_compounding_roepersxvol_126d_base_v150_signal(roe, closeadj):
    p = _f08_roe_persistence(roe, 126)
    rv = _std(closeadj.pct_change(), 126)
    result = p * rv * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08roc_f08_bank_roe_compounding_roequalxpers_126d_base_v076_signal,
    f08roc_f08_bank_roe_compounding_roequalxpers_252d_base_v077_signal,
    f08roc_f08_bank_roe_compounding_roetrajlog_21d_base_v078_signal,
    f08roc_f08_bank_roe_compounding_roetrajlog_63d_base_v079_signal,
    f08roc_f08_bank_roe_compounding_roetrajlog_252d_base_v080_signal,
    f08roc_f08_bank_roe_compounding_roerange_21d_base_v081_signal,
    f08roc_f08_bank_roe_compounding_roerange_63d_base_v082_signal,
    f08roc_f08_bank_roe_compounding_roerange_126d_base_v083_signal,
    f08roc_f08_bank_roe_compounding_roerange_252d_base_v084_signal,
    f08roc_f08_bank_roe_compounding_roetrajratio_21v63_base_v085_signal,
    f08roc_f08_bank_roe_compounding_roetrajdiff_21m63_base_v086_signal,
    f08roc_f08_bank_roe_compounding_roetrajratio_63v252_base_v087_signal,
    f08roc_f08_bank_roe_compounding_roetrajdiff_63m252_base_v088_signal,
    f08roc_f08_bank_roe_compounding_roetrajratio_126v504_base_v089_signal,
    f08roc_f08_bank_roe_compounding_roetrajdiff_126m504_base_v090_signal,
    f08roc_f08_bank_roe_compounding_roetrajratio_42v189_base_v091_signal,
    f08roc_f08_bank_roe_compounding_roetrajdiff_42m189_base_v092_signal,
    f08roc_f08_bank_roe_compounding_roedev_21d_base_v093_signal,
    f08roc_f08_bank_roe_compounding_roedev_63d_base_v094_signal,
    f08roc_f08_bank_roe_compounding_roedev_126d_base_v095_signal,
    f08roc_f08_bank_roe_compounding_roedev_252d_base_v096_signal,
    f08roc_f08_bank_roe_compounding_roepersratio_63v252_base_v097_signal,
    f08roc_f08_bank_roe_compounding_roepersratio_126v504_base_v098_signal,
    f08roc_f08_bank_roe_compounding_roequalrange_63d_base_v099_signal,
    f08roc_f08_bank_roe_compounding_roequalrange_126d_base_v100_signal,
    f08roc_f08_bank_roe_compounding_roequalrange_252d_base_v101_signal,
    f08roc_f08_bank_roe_compounding_roetrajxequity_21d_base_v102_signal,
    f08roc_f08_bank_roe_compounding_roetrajxequity_63d_base_v103_signal,
    f08roc_f08_bank_roe_compounding_roetrajxequity_126d_base_v104_signal,
    f08roc_f08_bank_roe_compounding_roetrajxequity_252d_base_v105_signal,
    f08roc_f08_bank_roe_compounding_roetrajxequity_504d_base_v106_signal,
    f08roc_f08_bank_roe_compounding_roequalxequity_21d_base_v107_signal,
    f08roc_f08_bank_roe_compounding_roequalxequity_63d_base_v108_signal,
    f08roc_f08_bank_roe_compounding_roequalxequity_126d_base_v109_signal,
    f08roc_f08_bank_roe_compounding_roequalxequity_252d_base_v110_signal,
    f08roc_f08_bank_roe_compounding_roecompound_63d_base_v111_signal,
    f08roc_f08_bank_roe_compounding_roecompound_126d_base_v112_signal,
    f08roc_f08_bank_roe_compounding_roecompound_252d_base_v113_signal,
    f08roc_f08_bank_roe_compounding_roecompound_504d_base_v114_signal,
    f08roc_f08_bank_roe_compounding_roepersema_10d_base_v115_signal,
    f08roc_f08_bank_roe_compounding_roepersema_21d_base_v116_signal,
    f08roc_f08_bank_roe_compounding_roepersema_63d_base_v117_signal,
    f08roc_f08_bank_roe_compounding_roepersema_126d_base_v118_signal,
    f08roc_f08_bank_roe_compounding_roepersema_252d_base_v119_signal,
    f08roc_f08_bank_roe_compounding_roeperschg_5d_base_v120_signal,
    f08roc_f08_bank_roe_compounding_roeperschg_21d_base_v121_signal,
    f08roc_f08_bank_roe_compounding_roeperschg_63d_base_v122_signal,
    f08roc_f08_bank_roe_compounding_roeperschg_126d_base_v123_signal,
    f08roc_f08_bank_roe_compounding_roeperschg_252d_base_v124_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_21d_base_v125_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_42d_base_v126_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_63d_base_v127_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_126d_base_v128_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_189d_base_v129_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_252d_base_v130_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_378d_base_v131_signal,
    f08roc_f08_bank_roe_compounding_roexroadiff_504d_base_v132_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_21d_base_v133_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_42d_base_v134_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_63d_base_v135_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_126d_base_v136_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_189d_base_v137_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_252d_base_v138_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_378d_base_v139_signal,
    f08roc_f08_bank_roe_compounding_roexroaratio_504d_base_v140_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_21d_base_v141_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_42d_base_v142_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_63d_base_v143_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_126d_base_v144_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_189d_base_v145_signal,
    f08roc_f08_bank_roe_compounding_roequalemaxpers_252d_base_v146_signal,
    f08roc_f08_bank_roe_compounding_roepersxvol_21d_base_v147_signal,
    f08roc_f08_bank_roe_compounding_roepersxvol_42d_base_v148_signal,
    f08roc_f08_bank_roe_compounding_roepersxvol_63d_base_v149_signal,
    f08roc_f08_bank_roe_compounding_roepersxvol_126d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_BANK_ROE_COMPOUNDING_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    debt = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    intangibles = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    roa = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    cols = {
        "closeadj": closeadj, "volume": volume, "revenue": revenue,
        "netinc": netinc, "assets": assets, "equity": equity, "debt": debt,
        "intangibles": intangibles, "sharesbas": sharesbas, "roa": roa, "roe": roe,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f08_roe_trajectory', '_f08_roe_persistence', '_f08_roe_quality')
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
    print(f"OK f08_bank_roe_compounding_base_076_150_claude: {n_features} features pass")
