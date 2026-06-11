"""dilution_death_spiral d1 features 001-075 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy(s):
    return s - s.shift(4)


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq(s):
    return s.diff()


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


def _consec_true_streak(b):
    b = b.fillna(False).astype(bool).astype(int)
    grp = (b == 0).cumsum()
    return b.groupby(grp).cumsum()


def _max_consec_true_window(b, window):
    b = b.fillna(False).astype(bool).astype(int)

    def _mx(w):
        best = cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best
    return b.rolling(window, min_periods=1).apply(_mx, raw=True)


def f48_ddsp_001_sharesbas_qoq_pct_d2(sharesbas):
    return _qoq_pct(sharesbas).diff().diff()

def f48_ddsp_002_sharesbas_yoy_pct_d2(sharesbas):
    return _yoy_pct(sharesbas).diff().diff()

def f48_ddsp_003_sharesbas_2y_pct_d2(sharesbas):
    return _safe_div(sharesbas - sharesbas.shift(8), sharesbas.shift(8).abs()).diff().diff()

def f48_ddsp_004_sharesbas_3y_pct_d2(sharesbas):
    return _safe_div(sharesbas - sharesbas.shift(12), sharesbas.shift(12).abs()).diff().diff()

def f48_ddsp_005_shareswa_qoq_pct_d2(shareswa):
    return _qoq_pct(shareswa).diff().diff()

def f48_ddsp_006_shareswa_yoy_pct_d2(shareswa):
    return _yoy_pct(shareswa).diff().diff()

def f48_ddsp_007_shareswadil_qoq_pct_d2(shareswadil):
    return _qoq_pct(shareswadil).diff().diff()

def f48_ddsp_008_shareswadil_yoy_pct_d2(shareswadil):
    return _yoy_pct(shareswadil).diff().diff()

def f48_ddsp_009_dilution_overhang_pct_d2(shareswadil, sharesbas):
    return _safe_div(shareswadil - sharesbas, sharesbas.abs()).diff().diff()

def f48_ddsp_010_dilution_overhang_qoq_change_d2(shareswadil, sharesbas):
    return _safe_div(shareswadil - sharesbas, sharesbas.abs()).diff().diff().diff()

def f48_ddsp_011_log_sharesbas_d2(sharesbas):
    return _safe_log(sharesbas).diff().diff()

def f48_ddsp_012_log_shareswadil_d2(shareswadil):
    return _safe_log(shareswadil).diff().diff()

def f48_ddsp_013_sharesbas_log_8q_slope_d2(sharesbas):
    return _rolling_slope(_safe_log(sharesbas), 8, min_periods=3).diff().diff()

def f48_ddsp_014_shareswa_log_8q_slope_d2(shareswa):
    return _rolling_slope(_safe_log(shareswa), 8, min_periods=3).diff().diff()

def f48_ddsp_015_shareswadil_log_8q_slope_d2(shareswadil):
    return _rolling_slope(_safe_log(shareswadil), 8, min_periods=3).diff().diff()

def f48_ddsp_016_sharesbas_drawup_from_8q_min_d2(sharesbas):
    rmin = sharesbas.rolling(8, min_periods=3).min()
    return (_safe_log(sharesbas) - _safe_log(rmin)).diff().diff()

def f48_ddsp_017_shareswadil_drawup_from_8q_min_d2(shareswadil):
    rmin = shareswadil.rolling(8, min_periods=3).min()
    return (_safe_log(shareswadil) - _safe_log(rmin)).diff().diff()

def f48_ddsp_018_sharesbas_zscore_8q_d2(sharesbas):
    return _rolling_zscore(sharesbas, 8, min_periods=3).diff().diff()

def f48_ddsp_019_shareswadil_zscore_8q_d2(shareswadil):
    return _rolling_zscore(shareswadil, 8, min_periods=3).diff().diff()

def f48_ddsp_020_sharesbas_cumulative_growth_4q_d2(sharesbas):
    return (_safe_div(sharesbas, sharesbas.shift(4)) - 1.0).diff().diff()

def f48_ddsp_021_sharesbas_growth_acceleration_d2(sharesbas):
    return _qoq_pct(sharesbas).diff().diff().diff()

def f48_ddsp_022_shareswa_growth_acceleration_d2(shareswa):
    return _qoq_pct(shareswa).diff().diff().diff()

def f48_ddsp_023_shareswadil_growth_acceleration_d2(shareswadil):
    return _qoq_pct(shareswadil).diff().diff().diff()

def f48_ddsp_024_sharesbas_jerk_d2(sharesbas):
    return _qoq_pct(sharesbas).diff().diff().diff().diff()

def f48_ddsp_025_sharesbas_yoy_acceleration_d2(sharesbas):
    return _yoy_pct(sharesbas).diff().diff().diff()

def f48_ddsp_026_sharesbas_consec_positive_qoq_streak_d2(sharesbas):
    return _consec_true_streak(_qoq_pct(sharesbas) > 0).diff().diff()

def f48_ddsp_027_sharesbas_consec_above_2pct_qoq_streak_d2(sharesbas):
    return _consec_true_streak(_qoq_pct(sharesbas) > 0.02).diff().diff()

def f48_ddsp_028_sharesbas_max_consec_positive_streak_8q_d2(sharesbas):
    return _max_consec_true_window(_qoq_pct(sharesbas) > 0, 8).diff().diff()

def f48_ddsp_029_sharesbas_qoq_above_5pct_count_8q_d2(sharesbas):
    ind = (_qoq_pct(sharesbas) > 0.05).astype(float)
    return ind.rolling(8, min_periods=3).sum().diff().diff()

def f48_ddsp_030_sharesbas_qoq_above_10pct_count_8q_d2(sharesbas):
    ind = (_qoq_pct(sharesbas) > 0.10).astype(float)
    return ind.rolling(8, min_periods=3).sum().diff().diff()

def f48_ddsp_031_sharesbas_yoy_above_20pct_indicator_d2(sharesbas):
    return (_yoy_pct(sharesbas) > 0.20).astype(float).diff().diff()

def f48_ddsp_032_sharesbas_yoy_above_50pct_indicator_d2(sharesbas):
    return (_yoy_pct(sharesbas) > 0.50).astype(float).diff().diff()

def f48_ddsp_033_sharesbas_qoq_pct_volatility_8q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(8, min_periods=3).std().diff().diff()

def f48_ddsp_034_sharesbas_qoq_persistence_positive_8q_d2(sharesbas):
    return (_qoq_pct(sharesbas) > 0).astype(float).rolling(8, min_periods=3).mean().diff().diff()

def f48_ddsp_035_shareswadil_yoy_above_20pct_indicator_d2(shareswadil):
    return (_yoy_pct(shareswadil) > 0.20).astype(float).diff().diff()

def f48_ddsp_036_sharesbas_4q_geomean_growth_d2(sharesbas):
    r = _safe_div(sharesbas, sharesbas.shift(4))
    return (r.where(r > 0, np.nan) ** (1.0 / 4.0) - 1.0).diff().diff()

def f48_ddsp_037_sharesbas_8q_geomean_growth_d2(sharesbas):
    r = _safe_div(sharesbas, sharesbas.shift(8))
    return (r.where(r > 0, np.nan) ** (1.0 / 8.0) - 1.0).diff().diff()

def f48_ddsp_038_sharesbas_4q_vs_8q_geomean_diff_d2(sharesbas):
    r4 = _safe_div(sharesbas, sharesbas.shift(4))
    r8 = _safe_div(sharesbas, sharesbas.shift(8))
    g4 = r4.where(r4 > 0, np.nan) ** (1.0 / 4.0) - 1.0
    g8 = r8.where(r8 > 0, np.nan) ** (1.0 / 8.0) - 1.0
    return (g4 - g8).diff().diff()

def f48_ddsp_039_issuance_step_size_8q_d2(sharesbas):
    return _qoq_pct(sharesbas).rolling(8, min_periods=3).max().diff().diff()

def f48_ddsp_040_issuance_burst_indicator_d2(sharesbas):
    q = _qoq_pct(sharesbas)
    sd = q.rolling(8, min_periods=3).std()
    return (q > 2.0 * sd).astype(float).diff().diff()

def f48_ddsp_041_close_yoy_pct_d2(close):
    return _yoy_pct(close).diff().diff()

def f48_ddsp_042_close_qoq_pct_d2(close):
    return _qoq_pct(close).diff().diff()

def f48_ddsp_043_close_drawdown_from_4q_max_d2(close):
    rmax = close.rolling(4, min_periods=2).max()
    return (_safe_div(close, rmax) - 1.0).diff().diff()

def f48_ddsp_044_close_drawdown_from_8q_max_d2(close):
    rmax = close.rolling(8, min_periods=3).max()
    return (_safe_div(close, rmax) - 1.0).diff().diff()

def f48_ddsp_045_close_drawdown_from_12q_max_d2(close):
    rmax = close.rolling(12, min_periods=4).max()
    return (_safe_div(close, rmax) - 1.0).diff().diff()

def f48_ddsp_046_close_drawdown_from_20q_max_d2(close):
    rmax = close.rolling(20, min_periods=6).max()
    return (_safe_div(close, rmax) - 1.0).diff().diff()

def f48_ddsp_047_close_negative_qoq_streak_d2(close):
    return _consec_true_streak(_qoq_pct(close) < 0).diff().diff()

def f48_ddsp_048_close_max_consec_negative_8q_d2(close):
    return _max_consec_true_window(_qoq_pct(close) < 0, 8).diff().diff()

def f48_ddsp_049_spiral_score_1_d2(sharesbas, close):
    return (_qoq_pct(sharesbas) * (-_qoq_pct(close))).diff().diff()

def f48_ddsp_050_spiral_score_1_8q_sum_d2(sharesbas, close):
    s = _qoq_pct(sharesbas) * (-_qoq_pct(close))
    return s.rolling(8, min_periods=3).sum().diff().diff()

def f48_ddsp_051_spiral_score_1_yoy_change_d2(sharesbas, close):
    s = _qoq_pct(sharesbas) * (-_qoq_pct(close))
    return (s - s.shift(4)).diff().diff()

def f48_ddsp_052_spiral_score_1_zscore_8q_d2(sharesbas, close):
    s = _qoq_pct(sharesbas) * (-_qoq_pct(close))
    return _rolling_zscore(s, 8, min_periods=3).diff().diff()

def f48_ddsp_053_spiral_score_1_consec_positive_streak_d2(sharesbas, close):
    s = _qoq_pct(sharesbas) * (-_qoq_pct(close))
    return _consec_true_streak(s > 0).diff().diff()

def f48_ddsp_054_spiral_score_2_yoy_d2(sharesbas, close):
    return (_yoy_pct(sharesbas) * (-_yoy_pct(close))).diff().diff()

def f48_ddsp_055_spiral_score_2_zscore_8q_d2(sharesbas, close):
    s = _yoy_pct(sharesbas) * (-_yoy_pct(close))
    return _rolling_zscore(s, 8, min_periods=3).diff().diff()

def f48_ddsp_056_issue_when_price_down_indicator_d2(sharesbas, close):
    a = _qoq_pct(sharesbas) > 0.02
    b = _qoq_pct(close) < 0
    return (a.fillna(False) & b.fillna(False)).astype(float).diff().diff()

def f48_ddsp_057_issue_when_price_down_count_8q_d2(sharesbas, close):
    a = _qoq_pct(sharesbas) > 0.02
    b = _qoq_pct(close) < 0
    ind = (a.fillna(False) & b.fillna(False)).astype(float)
    return ind.rolling(8, min_periods=3).sum().diff().diff()

def f48_ddsp_058_issue_when_price_down_count_12q_d2(sharesbas, close):
    a = _qoq_pct(sharesbas) > 0.02
    b = _qoq_pct(close) < 0
    ind = (a.fillna(False) & b.fillna(False)).astype(float)
    return ind.rolling(12, min_periods=4).sum().diff().diff()

def f48_ddsp_059_spiral_persistence_4q_d2(sharesbas, close):
    a = _qoq_pct(sharesbas) > 0.02
    b = _qoq_pct(close) < 0
    ind = (a.fillna(False) & b.fillna(False)).astype(float)
    return (ind.rolling(4, min_periods=4).sum() >= 4).astype(float).diff().diff()

def f48_ddsp_060_spiral_persistence_8q_d2(sharesbas, close):
    a = _qoq_pct(sharesbas) > 0.02
    b = _qoq_pct(close) < 0
    ind = (a.fillna(False) & b.fillna(False)).astype(float)
    return (ind.rolling(8, min_periods=8).sum() >= 8).astype(float).diff().diff()

def f48_ddsp_061_issuance_after_price_decline_lag1_indicator_d2(sharesbas, close):
    a = _qoq_pct(close).shift(1) < 0
    b = _qoq_pct(sharesbas) > 0
    return (a.fillna(False) & b.fillna(False)).astype(float).diff().diff()

def f48_ddsp_062_price_after_issuance_decline_lag1_indicator_d2(sharesbas, close):
    a = _qoq_pct(sharesbas).shift(1) > 0
    b = _qoq_pct(close) < 0
    return (a.fillna(False) & b.fillna(False)).astype(float).diff().diff()

def f48_ddsp_063_cumulative_dilution_during_drawdown_d2(sharesbas, close):
    rmax = close.rolling(8, min_periods=3).max()
    dd = _safe_div(close, rmax) - 1.0
    comp = _safe_log(sharesbas) - _safe_log(sharesbas.shift(8))
    return (comp * (dd < 0).astype(float)).diff().diff()

def f48_ddsp_064_dilution_intensity_per_pct_drop_4q_d2(sharesbas, close):
    num = _safe_div(sharesbas - sharesbas.shift(4), sharesbas.shift(4).abs())
    rmax = close.rolling(4, min_periods=2).max()
    dd = (_safe_div(close, rmax) - 1.0).abs().replace(0, np.nan)
    return _safe_div(num, dd).diff().diff()

def f48_ddsp_065_dilution_intensity_per_pct_drop_8q_d2(sharesbas, close):
    num = _safe_div(sharesbas - sharesbas.shift(8), sharesbas.shift(8).abs())
    rmax = close.rolling(8, min_periods=3).max()
    dd = (_safe_div(close, rmax) - 1.0).abs().replace(0, np.nan)
    return _safe_div(num, dd).diff().diff()

def f48_ddsp_066_correlation_issuance_close_lag1_8q_d2(sharesbas, close):
    a = _qoq_pct(sharesbas)
    b = _qoq_pct(close).shift(1)
    return a.rolling(8, min_periods=4).corr(b).diff().diff()

def f48_ddsp_067_correlation_issuance_close_lag1_12q_d2(sharesbas, close):
    a = _qoq_pct(sharesbas)
    b = _qoq_pct(close).shift(1)
    return a.rolling(12, min_periods=5).corr(b).diff().diff()

def f48_ddsp_068_coincident_decline_count_4q_d2(sharesbas, close):
    a = _qoq_pct(close) < 0
    b = _qoq_pct(sharesbas) > 0
    ind = (a.fillna(False) & b.fillna(False)).astype(float)
    return ind.rolling(4, min_periods=2).sum().diff().diff()

def f48_ddsp_069_coincident_decline_count_8q_d2(sharesbas, close):
    a = _qoq_pct(close) < 0
    b = _qoq_pct(sharesbas) > 0
    ind = (a.fillna(False) & b.fillna(False)).astype(float)
    return ind.rolling(8, min_periods=3).sum().diff().diff()

def f48_ddsp_070_coincident_decline_persistence_streak_d2(sharesbas, close):
    a = _qoq_pct(close) < 0
    b = _qoq_pct(sharesbas) > 0
    ind = (a.fillna(False) & b.fillna(False))
    return _consec_true_streak(ind).diff().diff()

def f48_ddsp_071_marketcap_qoq_pct_d2(marketcap):
    return _qoq_pct(marketcap).diff().diff()

def f48_ddsp_072_marketcap_yoy_pct_d2(marketcap):
    return _yoy_pct(marketcap).diff().diff()

def f48_ddsp_073_marketcap_drawdown_from_8q_max_d2(marketcap):
    rmax = marketcap.rolling(8, min_periods=3).max()
    return (_safe_div(marketcap, rmax) - 1.0).diff().diff()

def f48_ddsp_074_marketcap_drawdown_from_12q_max_d2(marketcap):
    rmax = marketcap.rolling(12, min_periods=4).max()
    return (_safe_div(marketcap, rmax) - 1.0).diff().diff()

def f48_ddsp_075_marketcap_drawdown_from_20q_max_d2(marketcap):
    rmax = marketcap.rolling(20, min_periods=6).max()
    return (_safe_div(marketcap, rmax) - 1.0).diff().diff()


DILUTION_DEATH_SPIRAL_D2_REGISTRY_001_075 = {
    "f48_ddsp_001_sharesbas_qoq_pct_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_001_sharesbas_qoq_pct_d2},
    "f48_ddsp_002_sharesbas_yoy_pct_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_002_sharesbas_yoy_pct_d2},
    "f48_ddsp_003_sharesbas_2y_pct_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_003_sharesbas_2y_pct_d2},
    "f48_ddsp_004_sharesbas_3y_pct_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_004_sharesbas_3y_pct_d2},
    "f48_ddsp_005_shareswa_qoq_pct_d2": {"inputs": ["shareswa"], "func": f48_ddsp_005_shareswa_qoq_pct_d2},
    "f48_ddsp_006_shareswa_yoy_pct_d2": {"inputs": ["shareswa"], "func": f48_ddsp_006_shareswa_yoy_pct_d2},
    "f48_ddsp_007_shareswadil_qoq_pct_d2": {"inputs": ["shareswadil"], "func": f48_ddsp_007_shareswadil_qoq_pct_d2},
    "f48_ddsp_008_shareswadil_yoy_pct_d2": {"inputs": ["shareswadil"], "func": f48_ddsp_008_shareswadil_yoy_pct_d2},
    "f48_ddsp_009_dilution_overhang_pct_d2": {"inputs": ["shareswadil", "sharesbas"], "func": f48_ddsp_009_dilution_overhang_pct_d2},
    "f48_ddsp_010_dilution_overhang_qoq_change_d2": {"inputs": ["shareswadil", "sharesbas"], "func": f48_ddsp_010_dilution_overhang_qoq_change_d2},
    "f48_ddsp_011_log_sharesbas_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_011_log_sharesbas_d2},
    "f48_ddsp_012_log_shareswadil_d2": {"inputs": ["shareswadil"], "func": f48_ddsp_012_log_shareswadil_d2},
    "f48_ddsp_013_sharesbas_log_8q_slope_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_013_sharesbas_log_8q_slope_d2},
    "f48_ddsp_014_shareswa_log_8q_slope_d2": {"inputs": ["shareswa"], "func": f48_ddsp_014_shareswa_log_8q_slope_d2},
    "f48_ddsp_015_shareswadil_log_8q_slope_d2": {"inputs": ["shareswadil"], "func": f48_ddsp_015_shareswadil_log_8q_slope_d2},
    "f48_ddsp_016_sharesbas_drawup_from_8q_min_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_016_sharesbas_drawup_from_8q_min_d2},
    "f48_ddsp_017_shareswadil_drawup_from_8q_min_d2": {"inputs": ["shareswadil"], "func": f48_ddsp_017_shareswadil_drawup_from_8q_min_d2},
    "f48_ddsp_018_sharesbas_zscore_8q_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_018_sharesbas_zscore_8q_d2},
    "f48_ddsp_019_shareswadil_zscore_8q_d2": {"inputs": ["shareswadil"], "func": f48_ddsp_019_shareswadil_zscore_8q_d2},
    "f48_ddsp_020_sharesbas_cumulative_growth_4q_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_020_sharesbas_cumulative_growth_4q_d2},
    "f48_ddsp_021_sharesbas_growth_acceleration_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_021_sharesbas_growth_acceleration_d2},
    "f48_ddsp_022_shareswa_growth_acceleration_d2": {"inputs": ["shareswa"], "func": f48_ddsp_022_shareswa_growth_acceleration_d2},
    "f48_ddsp_023_shareswadil_growth_acceleration_d2": {"inputs": ["shareswadil"], "func": f48_ddsp_023_shareswadil_growth_acceleration_d2},
    "f48_ddsp_024_sharesbas_jerk_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_024_sharesbas_jerk_d2},
    "f48_ddsp_025_sharesbas_yoy_acceleration_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_025_sharesbas_yoy_acceleration_d2},
    "f48_ddsp_026_sharesbas_consec_positive_qoq_streak_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_026_sharesbas_consec_positive_qoq_streak_d2},
    "f48_ddsp_027_sharesbas_consec_above_2pct_qoq_streak_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_027_sharesbas_consec_above_2pct_qoq_streak_d2},
    "f48_ddsp_028_sharesbas_max_consec_positive_streak_8q_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_028_sharesbas_max_consec_positive_streak_8q_d2},
    "f48_ddsp_029_sharesbas_qoq_above_5pct_count_8q_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_029_sharesbas_qoq_above_5pct_count_8q_d2},
    "f48_ddsp_030_sharesbas_qoq_above_10pct_count_8q_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_030_sharesbas_qoq_above_10pct_count_8q_d2},
    "f48_ddsp_031_sharesbas_yoy_above_20pct_indicator_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_031_sharesbas_yoy_above_20pct_indicator_d2},
    "f48_ddsp_032_sharesbas_yoy_above_50pct_indicator_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_032_sharesbas_yoy_above_50pct_indicator_d2},
    "f48_ddsp_033_sharesbas_qoq_pct_volatility_8q_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_033_sharesbas_qoq_pct_volatility_8q_d2},
    "f48_ddsp_034_sharesbas_qoq_persistence_positive_8q_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_034_sharesbas_qoq_persistence_positive_8q_d2},
    "f48_ddsp_035_shareswadil_yoy_above_20pct_indicator_d2": {"inputs": ["shareswadil"], "func": f48_ddsp_035_shareswadil_yoy_above_20pct_indicator_d2},
    "f48_ddsp_036_sharesbas_4q_geomean_growth_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_036_sharesbas_4q_geomean_growth_d2},
    "f48_ddsp_037_sharesbas_8q_geomean_growth_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_037_sharesbas_8q_geomean_growth_d2},
    "f48_ddsp_038_sharesbas_4q_vs_8q_geomean_diff_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_038_sharesbas_4q_vs_8q_geomean_diff_d2},
    "f48_ddsp_039_issuance_step_size_8q_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_039_issuance_step_size_8q_d2},
    "f48_ddsp_040_issuance_burst_indicator_d2": {"inputs": ["sharesbas"], "func": f48_ddsp_040_issuance_burst_indicator_d2},
    "f48_ddsp_041_close_yoy_pct_d2": {"inputs": ["close"], "func": f48_ddsp_041_close_yoy_pct_d2},
    "f48_ddsp_042_close_qoq_pct_d2": {"inputs": ["close"], "func": f48_ddsp_042_close_qoq_pct_d2},
    "f48_ddsp_043_close_drawdown_from_4q_max_d2": {"inputs": ["close"], "func": f48_ddsp_043_close_drawdown_from_4q_max_d2},
    "f48_ddsp_044_close_drawdown_from_8q_max_d2": {"inputs": ["close"], "func": f48_ddsp_044_close_drawdown_from_8q_max_d2},
    "f48_ddsp_045_close_drawdown_from_12q_max_d2": {"inputs": ["close"], "func": f48_ddsp_045_close_drawdown_from_12q_max_d2},
    "f48_ddsp_046_close_drawdown_from_20q_max_d2": {"inputs": ["close"], "func": f48_ddsp_046_close_drawdown_from_20q_max_d2},
    "f48_ddsp_047_close_negative_qoq_streak_d2": {"inputs": ["close"], "func": f48_ddsp_047_close_negative_qoq_streak_d2},
    "f48_ddsp_048_close_max_consec_negative_8q_d2": {"inputs": ["close"], "func": f48_ddsp_048_close_max_consec_negative_8q_d2},
    "f48_ddsp_049_spiral_score_1_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_049_spiral_score_1_d2},
    "f48_ddsp_050_spiral_score_1_8q_sum_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_050_spiral_score_1_8q_sum_d2},
    "f48_ddsp_051_spiral_score_1_yoy_change_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_051_spiral_score_1_yoy_change_d2},
    "f48_ddsp_052_spiral_score_1_zscore_8q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_052_spiral_score_1_zscore_8q_d2},
    "f48_ddsp_053_spiral_score_1_consec_positive_streak_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_053_spiral_score_1_consec_positive_streak_d2},
    "f48_ddsp_054_spiral_score_2_yoy_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_054_spiral_score_2_yoy_d2},
    "f48_ddsp_055_spiral_score_2_zscore_8q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_055_spiral_score_2_zscore_8q_d2},
    "f48_ddsp_056_issue_when_price_down_indicator_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_056_issue_when_price_down_indicator_d2},
    "f48_ddsp_057_issue_when_price_down_count_8q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_057_issue_when_price_down_count_8q_d2},
    "f48_ddsp_058_issue_when_price_down_count_12q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_058_issue_when_price_down_count_12q_d2},
    "f48_ddsp_059_spiral_persistence_4q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_059_spiral_persistence_4q_d2},
    "f48_ddsp_060_spiral_persistence_8q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_060_spiral_persistence_8q_d2},
    "f48_ddsp_061_issuance_after_price_decline_lag1_indicator_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_061_issuance_after_price_decline_lag1_indicator_d2},
    "f48_ddsp_062_price_after_issuance_decline_lag1_indicator_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_062_price_after_issuance_decline_lag1_indicator_d2},
    "f48_ddsp_063_cumulative_dilution_during_drawdown_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_063_cumulative_dilution_during_drawdown_d2},
    "f48_ddsp_064_dilution_intensity_per_pct_drop_4q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_064_dilution_intensity_per_pct_drop_4q_d2},
    "f48_ddsp_065_dilution_intensity_per_pct_drop_8q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_065_dilution_intensity_per_pct_drop_8q_d2},
    "f48_ddsp_066_correlation_issuance_close_lag1_8q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_066_correlation_issuance_close_lag1_8q_d2},
    "f48_ddsp_067_correlation_issuance_close_lag1_12q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_067_correlation_issuance_close_lag1_12q_d2},
    "f48_ddsp_068_coincident_decline_count_4q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_068_coincident_decline_count_4q_d2},
    "f48_ddsp_069_coincident_decline_count_8q_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_069_coincident_decline_count_8q_d2},
    "f48_ddsp_070_coincident_decline_persistence_streak_d2": {"inputs": ["sharesbas", "close"], "func": f48_ddsp_070_coincident_decline_persistence_streak_d2},
    "f48_ddsp_071_marketcap_qoq_pct_d2": {"inputs": ["marketcap"], "func": f48_ddsp_071_marketcap_qoq_pct_d2},
    "f48_ddsp_072_marketcap_yoy_pct_d2": {"inputs": ["marketcap"], "func": f48_ddsp_072_marketcap_yoy_pct_d2},
    "f48_ddsp_073_marketcap_drawdown_from_8q_max_d2": {"inputs": ["marketcap"], "func": f48_ddsp_073_marketcap_drawdown_from_8q_max_d2},
    "f48_ddsp_074_marketcap_drawdown_from_12q_max_d2": {"inputs": ["marketcap"], "func": f48_ddsp_074_marketcap_drawdown_from_12q_max_d2},
    "f48_ddsp_075_marketcap_drawdown_from_20q_max_d2": {"inputs": ["marketcap"], "func": f48_ddsp_075_marketcap_drawdown_from_20q_max_d2},
}
