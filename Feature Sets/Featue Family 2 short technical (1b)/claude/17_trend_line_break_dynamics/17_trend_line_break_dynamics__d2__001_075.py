"""trend_line_break_dynamics d2 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d2__076_150.py. Each
feature encodes a different concept in the trendline-fit / break-event / retest-failure /
durability / support-resistance-flip / breakdown-asymmetry theme.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


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


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


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


def _rolling_lr_endpoint(s, n, min_periods=None):
    """Last-point value of OLS y = a + b*x fit on rolling window (the fitted trendline value)."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        xm = x.mean(); ym = yv.mean()
        den = float(((x - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = float(((x - xm) * (yv - ym)).sum() / den)
        a = ym - b * xm
        return float(a + b * (len(w) - 1))
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_resid_std(s, n, min_periods=None):
    """Std of residuals from OLS fit on rolling window."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        xm = x.mean(); ym = yv.mean()
        den = float(((x - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = float(((x - xm) * (yv - ym)).sum() / den)
        a = ym - b * xm
        r = yv - (a + b * x)
        if r.size < 2:
            return np.nan
        return float(np.std(r, ddof=1))
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _rolling_r2(s, n, min_periods=None):
    """R² of OLS y vs x on rolling window."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _f(w):
        valid = ~np.isnan(w)
        nv = int(valid.sum())
        if nv < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        yv = w
        if not valid.all():
            x = x[valid]; yv = w[valid]
        xm = x.mean(); ym = yv.mean()
        tss = float(((yv - ym) ** 2).sum())
        if tss <= 0:
            return np.nan
        den = float(((x - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        b = float(((x - xm) * (yv - ym)).sum() / den)
        a = ym - b * xm
        yhat = a + b * x
        rss = float(((yv - yhat) ** 2).sum())
        return 1.0 - rss / tss
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def _theil_sen_slope(w):
    """Median-of-pairs slope (Theil-Sen) on a 1D window array. NaN-safe."""
    valid = ~np.isnan(w)
    nv = int(valid.sum())
    if nv < 5:
        return np.nan
    x = np.arange(len(w), dtype=float)
    if not valid.all():
        x = x[valid]; w = w[valid]
    n = w.size
    # subsample if too long, keep deterministic stride
    if n > 50:
        step = max(1, n // 50)
        idx = np.arange(0, n, step)
        x = x[idx]; w = w[idx]
        n = w.size
    slopes = []
    for i in range(n - 1):
        dx = x[i+1:] - x[i]
        dy = w[i+1:] - w[i]
        mask = dx != 0
        if mask.any():
            slopes.extend((dy[mask] / dx[mask]).tolist())
    if not slopes:
        return np.nan
    return float(np.median(slopes))


def _bars_since_true(b: pd.Series) -> pd.Series:
    """For each bar, bars since the most-recent True in boolean series b (NaN before first True)."""
    arr = b.fillna(False).astype(bool).values
    n = arr.size
    out = np.full(n, np.nan, dtype=float)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=b.index)


def f17_tlbk_001_ols_slope_logclose_21d_d2(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 21, min_periods=7)
    return out.diff().diff()


def f17_tlbk_002_ols_slope_logclose_63d_d2(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 63, min_periods=21)
    return out.diff().diff()


def f17_tlbk_003_ols_slope_logclose_126d_d2(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 126, min_periods=42)
    return out.diff().diff()


def f17_tlbk_004_ols_slope_logclose_252d_d2(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 252, min_periods=84)
    return out.diff().diff()


def f17_tlbk_005_ols_slope_logclose_504d_d2(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 504, min_periods=168)
    return out.diff().diff()


def f17_tlbk_006_ols_slope_loghigh_63d_d2(high: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(high), 63, min_periods=21)
    return out.diff().diff()


def f17_tlbk_007_ols_slope_loghigh_252d_d2(high: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(high), 252, min_periods=84)
    return out.diff().diff()


def f17_tlbk_008_ols_slope_loghigh_504d_d2(high: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(high), 504, min_periods=168)
    return out.diff().diff()


def f17_tlbk_009_ols_slope_loglow_63d_d2(low: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(low), 63, min_periods=21)
    return out.diff().diff()


def f17_tlbk_010_ols_slope_loglow_252d_d2(low: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(low), 252, min_periods=84)
    return out.diff().diff()


def f17_tlbk_011_ols_slope_loglow_504d_d2(low: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(low), 504, min_periods=168)
    return out.diff().diff()


def f17_tlbk_012_atr_norm_close_slope_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _rolling_slope(close, 252, min_periods=84)
    out = _safe_div(sl, _atr(high, low, close, n=21))
    return out.diff().diff()


def f17_tlbk_013_high_minus_low_slope_252d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(high), 252, min_periods=84) - _rolling_slope(_safe_log(low), 252, min_periods=84)
    return out.diff().diff()


def f17_tlbk_014_theil_sen_slope_logclose_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    out = lc.rolling(63, min_periods=21).apply(_theil_sen_slope, raw=True)
    return out.diff().diff()


def f17_tlbk_015_theil_sen_slope_logclose_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    out = lc.rolling(252, min_periods=84).apply(_theil_sen_slope, raw=True)
    return out.diff().diff()


def f17_tlbk_016_slope_sign_flip_event_21d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 21, min_periods=7)
    sgn = np.sign(sl)
    flip = (sgn != sgn.shift(1)).astype(float)
    out = flip.where(sl.notna() & sl.shift(1).notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_017_slope_sign_flip_event_63d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sgn = np.sign(sl)
    flip = (sgn != sgn.shift(1)).astype(float)
    out = flip.where(sl.notna() & sl.shift(1).notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_018_slope_sign_flip_event_252d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 252, min_periods=84)
    sgn = np.sign(sl)
    flip = (sgn != sgn.shift(1)).astype(float)
    out = flip.where(sl.notna() & sl.shift(1).notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_019_slope_flip_count_21d_in_252d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 21, min_periods=7)
    sgn = np.sign(sl)
    flip = ((sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna()).astype(float)
    out = flip.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f17_tlbk_020_slope_flip_count_63d_in_252d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sgn = np.sign(sl)
    flip = ((sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna()).astype(float)
    out = flip.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f17_tlbk_021_bars_since_last_slope_flip_63d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sgn = np.sign(sl)
    flip = (sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna()
    out = _bars_since_true(flip)
    return out.diff().diff()


def f17_tlbk_022_bars_since_last_slope_flip_252d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 252, min_periods=84)
    sgn = np.sign(sl)
    flip = (sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna()
    out = _bars_since_true(flip)
    return out.diff().diff()


def f17_tlbk_023_longest_pos_slope_streak_252d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    pos = (sl > 0).astype(float)
    def _ms(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        best = 0; cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    out = pos.rolling(252, min_periods=63).apply(_ms, raw=True)
    return out.diff().diff()


def f17_tlbk_024_longest_neg_slope_streak_252d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    neg = (sl < 0).astype(float)
    def _ms(w):
        if w.size == 0 or np.isnan(w).all():
            return np.nan
        best = 0; cur = 0
        for v in w:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    out = neg.rolling(252, min_periods=63).apply(_ms, raw=True)
    return out.diff().diff()


def f17_tlbk_025_current_pos_slope_regime_duration_63d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    sgn = np.sign(sl)
    block = (sgn != sgn.shift(1)).fillna(False).cumsum()
    dur = sl.groupby(block).cumcount().astype(float)
    out = dur.where(sgn > 0, np.nan)
    return out.diff().diff()


def f17_tlbk_026_frac_time_pos_slope_252d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21)
    pos = (sl > 0).astype(float).where(sl.notna(), np.nan)
    out = pos.rolling(252, min_periods=84).mean()
    return out.diff().diff()


def f17_tlbk_027_slope_zero_crossing_density_252d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 21, min_periods=7)
    sgn = np.sign(sl)
    flip = ((sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna()).astype(float)
    out = flip.rolling(252, min_periods=84).mean()
    return out.diff().diff()


def f17_tlbk_028_slope_magnitude_zscore_252d_d2(close: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(close), 63, min_periods=21).abs()
    out = _rolling_zscore(sl, 252, min_periods=84)
    return out.diff().diff()


def f17_tlbk_029_slope_21_vs_63_sign_agreement_d2(close: pd.Series) -> pd.Series:
    s21 = np.sign(_rolling_slope(_safe_log(close), 21, min_periods=7))
    s63 = np.sign(_rolling_slope(_safe_log(close), 63, min_periods=21))
    out = (s21 == s63).astype(float).where(s21.notna() & s63.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_030_slope_21_63_252_unanimous_d2(close: pd.Series) -> pd.Series:
    s21 = np.sign(_rolling_slope(_safe_log(close), 21, min_periods=7))
    s63 = np.sign(_rolling_slope(_safe_log(close), 63, min_periods=21))
    s252 = np.sign(_rolling_slope(_safe_log(close), 252, min_periods=84))
    unan = ((s21 == s63) & (s63 == s252)).astype(float)
    out = unan.where(s21.notna() & s63.notna() & s252.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_031_close_below_trendline_63d_d2(close: pd.Series) -> pd.Series:
    tl = _rolling_lr_endpoint(_safe_log(close), 63, min_periods=21)
    out = (_safe_log(close) < tl).astype(float).where(tl.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_032_close_below_trendline_252d_d2(close: pd.Series) -> pd.Series:
    tl = _rolling_lr_endpoint(_safe_log(close), 252, min_periods=84)
    out = (_safe_log(close) < tl).astype(float).where(tl.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_033_trendline_break_event_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    break_e = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float)
    out = break_e.where(tl.notna() & tl.shift(1).notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_034_trendline_break_event_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    above = (lc >= tl).astype(float)
    break_e = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float)
    out = break_e.where(tl.notna() & tl.shift(1).notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_035_trendline_break_count_63d_in_126d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float).where(tl.notna() & tl.shift(1).notna(), np.nan)
    out = be.rolling(126, min_periods=42).sum()
    return out.diff().diff()


def f17_tlbk_036_trendline_break_count_252d_in_504d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float).where(tl.notna() & tl.shift(1).notna(), np.nan)
    out = be.rolling(504, min_periods=168).sum()
    return out.diff().diff()


def f17_tlbk_037_bars_since_last_trendline_break_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)) & tl.notna() & tl.shift(1).notna()
    out = _bars_since_true(be)
    return out.diff().diff()


def f17_tlbk_038_bars_since_last_trendline_break_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)) & tl.notna() & tl.shift(1).notna()
    out = _bars_since_true(be)
    return out.diff().diff()


def f17_tlbk_039_break_magnitude_log_below_trendline_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    below = (lc - tl).where(lc < tl, np.nan)
    out = below
    return out.diff().diff()


def f17_tlbk_040_break_magnitude_atr_below_trendline_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    lc_lvl = np.exp(tl)
    atr = _atr(high, low, close, n=21)
    resid = close - lc_lvl
    out = _safe_div(resid, atr).where(resid < 0, np.nan)
    return out.diff().diff()


def f17_tlbk_041_break_magnitude_sigma_below_trendline_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    rs = _rolling_resid_std(lc, 252, min_periods=84)
    resid = lc - tl
    out = _safe_div(resid, rs).where(resid < 0, np.nan)
    return out.diff().diff()


def f17_tlbk_042_first_break_after_63d_hold_indicator_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float).where(tl.notna() & tl.shift(1).notna(), np.nan)
    held = (above.rolling(63, min_periods=21).sum() >= 60).astype(float)
    out = (be * held.shift(1)).where(be.notna() & held.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_043_break_no_recovery_21d_indicator_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float).where(tl.notna() & tl.shift(1).notna(), np.nan)
    stays_below = (above.rolling(21, min_periods=10).max() < 0.5).astype(float)
    out = (be.shift(21) * stays_below).where(be.shift(21).notna() & stays_below.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_044_break_velocity_5bar_log_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    gap = lc - tl
    out = gap - gap.shift(5)
    return out.diff().diff()


def f17_tlbk_045_distance_at_break_event_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)) & tl.notna() & tl.shift(1).notna()
    out = (lc - tl).where(be, np.nan)
    return out.diff().diff()


def f17_tlbk_046_retest_event_within_0p5sigma_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    broken_recently = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    close_to_line = ((lc - tl).abs() <= 0.5 * rs).astype(float)
    out = (close_to_line * (broken_recently > 0).astype(float)).where(rs.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_047_retest_then_fail_indicator_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    broken_recently = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    close_to_line = ((lc - tl).abs() <= 0.5 * rs).astype(float)
    retest = (close_to_line * (broken_recently > 0).astype(float))
    fail_next = (above.rolling(5, min_periods=2).min() < 0.5).astype(float).shift(-0)
    # fail_next as: in next 5 bars after retest, closed below — use rolling on lagged signal
    # instead: was-retest 5 bars ago AND now below
    out = (retest.shift(5) * (lc < tl).astype(float)).where(rs.notna() & retest.shift(5).notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_048_retest_event_within_0p5sigma_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    rs = _rolling_resid_std(lc, 252, min_periods=84)
    above = (lc >= tl).astype(float)
    broken_recently = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(63, min_periods=21).sum()
    close_to_line = ((lc - tl).abs() <= 0.5 * rs).astype(float)
    out = (close_to_line * (broken_recently > 0).astype(float)).where(rs.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_049_retest_event_count_63d_in_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    broken_recently = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    close_to_line = ((lc - tl).abs() <= 0.5 * rs).astype(float)
    retest = (close_to_line * (broken_recently > 0).astype(float)).where(rs.notna(), np.nan)
    out = retest.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f17_tlbk_050_retest_failure_max_drop_10d_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    close_to_line = ((lc - tl).abs() <= 0.5 * rs).astype(float)
    above = (lc >= tl).astype(float)
    broken_recently = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    retest = (close_to_line * (broken_recently > 0).astype(float)).where(rs.notna(), np.nan)
    min_lc_10 = lc.rolling(10, min_periods=3).min()
    drop = lc - min_lc_10
    out = (drop * (retest.shift(10) > 0.5).astype(float)).where(retest.shift(10).notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_051_bars_since_last_retest_event_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    broken_recently = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    retest_event = (((lc - tl).abs() <= 0.5 * rs) & (broken_recently > 0)) & rs.notna()
    out = _bars_since_true(retest_event)
    return out.diff().diff()


def f17_tlbk_052_retest_dwell_bars_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    broken_recently = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(63, min_periods=21).sum()
    near = (((lc - tl).abs() <= 0.5 * rs) & (broken_recently > 0)).astype(float)
    out = near.rolling(63, min_periods=21).sum().where(rs.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_053_retest_with_bearish_close_indicator_63d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    lo = _safe_log(open)
    # proxy retest by close ~ rolling 21d midpoint of log-close (since we can't import tl here cleanly)
    m21 = lc.rolling(21, min_periods=7).mean()
    retest_proxy = ((lc - m21).abs() < lc.rolling(63, min_periods=21).std() * 0.3).astype(float)
    bearish = ((lc < lo) & (lc < m21)).astype(float)
    out = (retest_proxy * bearish).where(m21.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_054_false_retest_pierce_then_back_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    pierce = ((above.shift(1) < 0.5) & (above > 0.5) & ((lc - tl) < 0.25 * rs)).astype(float)
    close_back = (above.shift(-0) < 0.5).astype(float)
    # proper PIT: at bar t, look at previous-bar pierce + current-bar back-below
    back = ((above.shift(1) > 0.5) & (above < 0.5) & ((tl - lc) < 0.25 * rs)).astype(float)
    out = (pierce.shift(1).fillna(0) * back).where(rs.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_055_break_minus_hold_score_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    breaks = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).where(tl.notna() & tl.shift(1).notna(), np.nan)
    recoveries = (((above.shift(1) < 0.5) & (above > 0.5)).astype(float)).where(tl.notna() & tl.shift(1).notna(), np.nan)
    out = breaks.rolling(252, min_periods=84).sum() - recoveries.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f17_tlbk_056_retest_failure_rate_63d_in_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    br = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    retest = (((lc - tl).abs() <= 0.5 * rs) & (br > 0)).astype(float)
    failed = (retest.shift(5) * (lc < tl).astype(float)).where(retest.shift(5).notna(), np.nan)
    out = _safe_div(failed.rolling(252, min_periods=84).sum(), retest.rolling(252, min_periods=84).sum())
    return out.diff().diff()


def f17_tlbk_057_max_post_break_upside_21d_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    gap = lc - tl
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float).where(tl.notna() & tl.shift(1).notna(), np.nan)
    max_gap_21 = gap.rolling(21, min_periods=5).max()
    out = (max_gap_21 * (be.shift(21).fillna(0))).where(be.shift(21).notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_058_lower_high_after_break_indicator_63d_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    lh = _safe_log(high)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    be = ((above.shift(1) > 0.5) & (above < 0.5)).astype(float).where(tl.notna() & tl.shift(1).notna(), np.nan)
    prior_max = lh.shift(21).rolling(63, min_periods=21).max()
    post_max = lh.rolling(21, min_periods=5).max()
    lhi = ((post_max < prior_max).astype(float)) * (be.shift(21).fillna(0))
    out = lhi.where(be.shift(21).notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_059_retest_cluster_density_63d_in_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    br = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    retest = (((lc - tl).abs() <= 0.5 * rs) & (br > 0)).astype(float)
    cnt = retest.rolling(252, min_periods=84).sum()
    out = cnt / 252.0
    return out.diff().diff()


def f17_tlbk_060_retest_then_slope_flip_neg_indicator_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    above = (lc >= tl).astype(float)
    br = (((above.shift(1) > 0.5) & (above < 0.5)).astype(float)).rolling(21, min_periods=5).sum()
    retest = (((lc - tl).abs() <= 0.5 * rs) & (br > 0)).astype(float)
    sl = _rolling_slope(lc, 63, min_periods=21)
    slope_neg_now = (sl < 0).astype(float)
    slope_pos_prior = (sl.shift(21) >= 0).astype(float)
    flip = slope_neg_now * slope_pos_prior
    out = (retest.shift(0) * flip).where(rs.notna() & sl.shift(21).notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_061_channel_width_2sigma_63d_d2(close: pd.Series) -> pd.Series:
    out = 2.0 * _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    return out.diff().diff()


def f17_tlbk_062_channel_width_2sigma_252d_d2(close: pd.Series) -> pd.Series:
    out = 2.0 * _rolling_resid_std(_safe_log(close), 252, min_periods=84)
    return out.diff().diff()


def f17_tlbk_063_channel_width_2sigma_504d_d2(close: pd.Series) -> pd.Series:
    out = 2.0 * _rolling_resid_std(_safe_log(close), 504, min_periods=168)
    return out.diff().diff()


def f17_tlbk_064_channel_width_atr_units_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    w = 2.0 * _rolling_resid_std(close, 63, min_periods=21)
    out = _safe_div(w, _atr(high, low, close, n=21))
    return out.diff().diff()


def f17_tlbk_065_channel_snr_slope_over_width_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    wd = _rolling_resid_std(lc, 63, min_periods=21)
    out = _safe_div(sl * 63.0, wd)
    return out.diff().diff()


def f17_tlbk_066_channel_snr_slope_over_width_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 252, min_periods=84)
    wd = _rolling_resid_std(lc, 252, min_periods=84)
    out = _safe_div(sl * 252.0, wd)
    return out.diff().diff()


def f17_tlbk_067_frac_time_upper_half_channel_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    upper = (lc > tl).astype(float).where(tl.notna(), np.nan)
    out = upper.rolling(252, min_periods=84).mean()
    return out.diff().diff()


def f17_tlbk_068_frac_time_lower_half_channel_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    lower = (lc < tl).astype(float).where(tl.notna(), np.nan)
    out = lower.rolling(252, min_periods=84).mean()
    return out.diff().diff()


def f17_tlbk_069_channel_width_vs_252d_median_63d_d2(close: pd.Series) -> pd.Series:
    w = 2.0 * _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    med = w.rolling(252, min_periods=84).median()
    out = _safe_div(w, med)
    return out.diff().diff()


def f17_tlbk_070_channel_width_compression_indicator_63d_d2(close: pd.Series) -> pd.Series:
    w = 2.0 * _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    med = w.rolling(252, min_periods=84).median()
    out = (w < 0.5 * med).astype(float).where(med.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_071_channel_width_expansion_indicator_63d_d2(close: pd.Series) -> pd.Series:
    w = 2.0 * _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    med = w.rolling(252, min_periods=84).median()
    out = (w > 2.0 * med).astype(float).where(med.notna(), np.nan)
    return out.diff().diff()


def f17_tlbk_072_channel_width_zscore_63d_in_252d_d2(close: pd.Series) -> pd.Series:
    w = 2.0 * _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    out = _rolling_zscore(w, 252, min_periods=84)
    return out.diff().diff()


def f17_tlbk_073_upper_band_touch_count_63d_in_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    up = tl + 2.0 * rs
    touch = (lc >= up).astype(float).where(rs.notna(), np.nan)
    out = touch.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f17_tlbk_074_lower_band_touch_count_63d_in_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    lo = tl - 2.0 * rs
    touch = (lc <= lo).astype(float).where(rs.notna(), np.nan)
    out = touch.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f17_tlbk_075_upper_vs_lower_touch_asym_63d_in_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    up = tl + 2.0 * rs
    dn = tl - 2.0 * rs
    ut = (lc >= up).astype(float).where(rs.notna(), np.nan).rolling(252, min_periods=84).sum()
    lt = (lc <= dn).astype(float).where(rs.notna(), np.nan).rolling(252, min_periods=84).sum()
    out = ut - lt
    return out.diff().diff()


# ============================================================
#                         REGISTRY 001_075 (d2)
# ============================================================

TREND_LINE_BREAK_DYNAMICS_D2_REGISTRY_001_075 = {
    "f17_tlbk_001_ols_slope_logclose_21d_d2": {"inputs": ["close"], "func": f17_tlbk_001_ols_slope_logclose_21d_d2},
    "f17_tlbk_002_ols_slope_logclose_63d_d2": {"inputs": ["close"], "func": f17_tlbk_002_ols_slope_logclose_63d_d2},
    "f17_tlbk_003_ols_slope_logclose_126d_d2": {"inputs": ["close"], "func": f17_tlbk_003_ols_slope_logclose_126d_d2},
    "f17_tlbk_004_ols_slope_logclose_252d_d2": {"inputs": ["close"], "func": f17_tlbk_004_ols_slope_logclose_252d_d2},
    "f17_tlbk_005_ols_slope_logclose_504d_d2": {"inputs": ["close"], "func": f17_tlbk_005_ols_slope_logclose_504d_d2},
    "f17_tlbk_006_ols_slope_loghigh_63d_d2": {"inputs": ["high"], "func": f17_tlbk_006_ols_slope_loghigh_63d_d2},
    "f17_tlbk_007_ols_slope_loghigh_252d_d2": {"inputs": ["high"], "func": f17_tlbk_007_ols_slope_loghigh_252d_d2},
    "f17_tlbk_008_ols_slope_loghigh_504d_d2": {"inputs": ["high"], "func": f17_tlbk_008_ols_slope_loghigh_504d_d2},
    "f17_tlbk_009_ols_slope_loglow_63d_d2": {"inputs": ["low"], "func": f17_tlbk_009_ols_slope_loglow_63d_d2},
    "f17_tlbk_010_ols_slope_loglow_252d_d2": {"inputs": ["low"], "func": f17_tlbk_010_ols_slope_loglow_252d_d2},
    "f17_tlbk_011_ols_slope_loglow_504d_d2": {"inputs": ["low"], "func": f17_tlbk_011_ols_slope_loglow_504d_d2},
    "f17_tlbk_012_atr_norm_close_slope_252d_d2": {"inputs": ["high", "low", "close"], "func": f17_tlbk_012_atr_norm_close_slope_252d_d2},
    "f17_tlbk_013_high_minus_low_slope_252d_d2": {"inputs": ["high", "low"], "func": f17_tlbk_013_high_minus_low_slope_252d_d2},
    "f17_tlbk_014_theil_sen_slope_logclose_63d_d2": {"inputs": ["close"], "func": f17_tlbk_014_theil_sen_slope_logclose_63d_d2},
    "f17_tlbk_015_theil_sen_slope_logclose_252d_d2": {"inputs": ["close"], "func": f17_tlbk_015_theil_sen_slope_logclose_252d_d2},
    "f17_tlbk_016_slope_sign_flip_event_21d_d2": {"inputs": ["close"], "func": f17_tlbk_016_slope_sign_flip_event_21d_d2},
    "f17_tlbk_017_slope_sign_flip_event_63d_d2": {"inputs": ["close"], "func": f17_tlbk_017_slope_sign_flip_event_63d_d2},
    "f17_tlbk_018_slope_sign_flip_event_252d_d2": {"inputs": ["close"], "func": f17_tlbk_018_slope_sign_flip_event_252d_d2},
    "f17_tlbk_019_slope_flip_count_21d_in_252d_d2": {"inputs": ["close"], "func": f17_tlbk_019_slope_flip_count_21d_in_252d_d2},
    "f17_tlbk_020_slope_flip_count_63d_in_252d_d2": {"inputs": ["close"], "func": f17_tlbk_020_slope_flip_count_63d_in_252d_d2},
    "f17_tlbk_021_bars_since_last_slope_flip_63d_d2": {"inputs": ["close"], "func": f17_tlbk_021_bars_since_last_slope_flip_63d_d2},
    "f17_tlbk_022_bars_since_last_slope_flip_252d_d2": {"inputs": ["close"], "func": f17_tlbk_022_bars_since_last_slope_flip_252d_d2},
    "f17_tlbk_023_longest_pos_slope_streak_252d_d2": {"inputs": ["close"], "func": f17_tlbk_023_longest_pos_slope_streak_252d_d2},
    "f17_tlbk_024_longest_neg_slope_streak_252d_d2": {"inputs": ["close"], "func": f17_tlbk_024_longest_neg_slope_streak_252d_d2},
    "f17_tlbk_025_current_pos_slope_regime_duration_63d_d2": {"inputs": ["close"], "func": f17_tlbk_025_current_pos_slope_regime_duration_63d_d2},
    "f17_tlbk_026_frac_time_pos_slope_252d_d2": {"inputs": ["close"], "func": f17_tlbk_026_frac_time_pos_slope_252d_d2},
    "f17_tlbk_027_slope_zero_crossing_density_252d_d2": {"inputs": ["close"], "func": f17_tlbk_027_slope_zero_crossing_density_252d_d2},
    "f17_tlbk_028_slope_magnitude_zscore_252d_d2": {"inputs": ["close"], "func": f17_tlbk_028_slope_magnitude_zscore_252d_d2},
    "f17_tlbk_029_slope_21_vs_63_sign_agreement_d2": {"inputs": ["close"], "func": f17_tlbk_029_slope_21_vs_63_sign_agreement_d2},
    "f17_tlbk_030_slope_21_63_252_unanimous_d2": {"inputs": ["close"], "func": f17_tlbk_030_slope_21_63_252_unanimous_d2},
    "f17_tlbk_031_close_below_trendline_63d_d2": {"inputs": ["close"], "func": f17_tlbk_031_close_below_trendline_63d_d2},
    "f17_tlbk_032_close_below_trendline_252d_d2": {"inputs": ["close"], "func": f17_tlbk_032_close_below_trendline_252d_d2},
    "f17_tlbk_033_trendline_break_event_63d_d2": {"inputs": ["close"], "func": f17_tlbk_033_trendline_break_event_63d_d2},
    "f17_tlbk_034_trendline_break_event_252d_d2": {"inputs": ["close"], "func": f17_tlbk_034_trendline_break_event_252d_d2},
    "f17_tlbk_035_trendline_break_count_63d_in_126d_d2": {"inputs": ["close"], "func": f17_tlbk_035_trendline_break_count_63d_in_126d_d2},
    "f17_tlbk_036_trendline_break_count_252d_in_504d_d2": {"inputs": ["close"], "func": f17_tlbk_036_trendline_break_count_252d_in_504d_d2},
    "f17_tlbk_037_bars_since_last_trendline_break_63d_d2": {"inputs": ["close"], "func": f17_tlbk_037_bars_since_last_trendline_break_63d_d2},
    "f17_tlbk_038_bars_since_last_trendline_break_252d_d2": {"inputs": ["close"], "func": f17_tlbk_038_bars_since_last_trendline_break_252d_d2},
    "f17_tlbk_039_break_magnitude_log_below_trendline_63d_d2": {"inputs": ["close"], "func": f17_tlbk_039_break_magnitude_log_below_trendline_63d_d2},
    "f17_tlbk_040_break_magnitude_atr_below_trendline_63d_d2": {"inputs": ["high", "low", "close"], "func": f17_tlbk_040_break_magnitude_atr_below_trendline_63d_d2},
    "f17_tlbk_041_break_magnitude_sigma_below_trendline_252d_d2": {"inputs": ["close"], "func": f17_tlbk_041_break_magnitude_sigma_below_trendline_252d_d2},
    "f17_tlbk_042_first_break_after_63d_hold_indicator_252d_d2": {"inputs": ["close"], "func": f17_tlbk_042_first_break_after_63d_hold_indicator_252d_d2},
    "f17_tlbk_043_break_no_recovery_21d_indicator_63d_d2": {"inputs": ["close"], "func": f17_tlbk_043_break_no_recovery_21d_indicator_63d_d2},
    "f17_tlbk_044_break_velocity_5bar_log_63d_d2": {"inputs": ["close"], "func": f17_tlbk_044_break_velocity_5bar_log_63d_d2},
    "f17_tlbk_045_distance_at_break_event_63d_d2": {"inputs": ["close"], "func": f17_tlbk_045_distance_at_break_event_63d_d2},
    "f17_tlbk_046_retest_event_within_0p5sigma_63d_d2": {"inputs": ["close"], "func": f17_tlbk_046_retest_event_within_0p5sigma_63d_d2},
    "f17_tlbk_047_retest_then_fail_indicator_63d_d2": {"inputs": ["close"], "func": f17_tlbk_047_retest_then_fail_indicator_63d_d2},
    "f17_tlbk_048_retest_event_within_0p5sigma_252d_d2": {"inputs": ["close"], "func": f17_tlbk_048_retest_event_within_0p5sigma_252d_d2},
    "f17_tlbk_049_retest_event_count_63d_in_252d_d2": {"inputs": ["close"], "func": f17_tlbk_049_retest_event_count_63d_in_252d_d2},
    "f17_tlbk_050_retest_failure_max_drop_10d_63d_d2": {"inputs": ["close"], "func": f17_tlbk_050_retest_failure_max_drop_10d_63d_d2},
    "f17_tlbk_051_bars_since_last_retest_event_63d_d2": {"inputs": ["close"], "func": f17_tlbk_051_bars_since_last_retest_event_63d_d2},
    "f17_tlbk_052_retest_dwell_bars_63d_d2": {"inputs": ["close"], "func": f17_tlbk_052_retest_dwell_bars_63d_d2},
    "f17_tlbk_053_retest_with_bearish_close_indicator_63d_d2": {"inputs": ["open", "close"], "func": f17_tlbk_053_retest_with_bearish_close_indicator_63d_d2},
    "f17_tlbk_054_false_retest_pierce_then_back_63d_d2": {"inputs": ["close"], "func": f17_tlbk_054_false_retest_pierce_then_back_63d_d2},
    "f17_tlbk_055_break_minus_hold_score_252d_d2": {"inputs": ["close"], "func": f17_tlbk_055_break_minus_hold_score_252d_d2},
    "f17_tlbk_056_retest_failure_rate_63d_in_252d_d2": {"inputs": ["close"], "func": f17_tlbk_056_retest_failure_rate_63d_in_252d_d2},
    "f17_tlbk_057_max_post_break_upside_21d_63d_d2": {"inputs": ["close"], "func": f17_tlbk_057_max_post_break_upside_21d_63d_d2},
    "f17_tlbk_058_lower_high_after_break_indicator_63d_d2": {"inputs": ["high", "close"], "func": f17_tlbk_058_lower_high_after_break_indicator_63d_d2},
    "f17_tlbk_059_retest_cluster_density_63d_in_252d_d2": {"inputs": ["close"], "func": f17_tlbk_059_retest_cluster_density_63d_in_252d_d2},
    "f17_tlbk_060_retest_then_slope_flip_neg_indicator_63d_d2": {"inputs": ["close"], "func": f17_tlbk_060_retest_then_slope_flip_neg_indicator_63d_d2},
    "f17_tlbk_061_channel_width_2sigma_63d_d2": {"inputs": ["close"], "func": f17_tlbk_061_channel_width_2sigma_63d_d2},
    "f17_tlbk_062_channel_width_2sigma_252d_d2": {"inputs": ["close"], "func": f17_tlbk_062_channel_width_2sigma_252d_d2},
    "f17_tlbk_063_channel_width_2sigma_504d_d2": {"inputs": ["close"], "func": f17_tlbk_063_channel_width_2sigma_504d_d2},
    "f17_tlbk_064_channel_width_atr_units_63d_d2": {"inputs": ["high", "low", "close"], "func": f17_tlbk_064_channel_width_atr_units_63d_d2},
    "f17_tlbk_065_channel_snr_slope_over_width_63d_d2": {"inputs": ["close"], "func": f17_tlbk_065_channel_snr_slope_over_width_63d_d2},
    "f17_tlbk_066_channel_snr_slope_over_width_252d_d2": {"inputs": ["close"], "func": f17_tlbk_066_channel_snr_slope_over_width_252d_d2},
    "f17_tlbk_067_frac_time_upper_half_channel_252d_d2": {"inputs": ["close"], "func": f17_tlbk_067_frac_time_upper_half_channel_252d_d2},
    "f17_tlbk_068_frac_time_lower_half_channel_252d_d2": {"inputs": ["close"], "func": f17_tlbk_068_frac_time_lower_half_channel_252d_d2},
    "f17_tlbk_069_channel_width_vs_252d_median_63d_d2": {"inputs": ["close"], "func": f17_tlbk_069_channel_width_vs_252d_median_63d_d2},
    "f17_tlbk_070_channel_width_compression_indicator_63d_d2": {"inputs": ["close"], "func": f17_tlbk_070_channel_width_compression_indicator_63d_d2},
    "f17_tlbk_071_channel_width_expansion_indicator_63d_d2": {"inputs": ["close"], "func": f17_tlbk_071_channel_width_expansion_indicator_63d_d2},
    "f17_tlbk_072_channel_width_zscore_63d_in_252d_d2": {"inputs": ["close"], "func": f17_tlbk_072_channel_width_zscore_63d_in_252d_d2},
    "f17_tlbk_073_upper_band_touch_count_63d_in_252d_d2": {"inputs": ["close"], "func": f17_tlbk_073_upper_band_touch_count_63d_in_252d_d2},
    "f17_tlbk_074_lower_band_touch_count_63d_in_252d_d2": {"inputs": ["close"], "func": f17_tlbk_074_lower_band_touch_count_63d_in_252d_d2},
    "f17_tlbk_075_upper_vs_lower_touch_asym_63d_in_252d_d2": {"inputs": ["close"], "func": f17_tlbk_075_upper_vs_lower_touch_asym_63d_in_252d_d2},
}
