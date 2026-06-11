"""linear_regression_channel base features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py. Each
feature encodes a different concept in the LR-channel theme:
slope / R² / residual / channel-width / band-touch / multi-horizon disagreement /
SNR / rotation / decay / composite topping.

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


def _rolling_resid_skew(s, n, min_periods=None):
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
        if r.size < 5:
            return np.nan
        sd = float(np.std(r, ddof=1))
        if sd <= 0:
            return np.nan
        return float(np.mean(((r - r.mean()) / sd) ** 3))
    return s.rolling(n, min_periods=min_periods).apply(_f, raw=True)


def f18_lrch_001_lr_slope_logclose_21d(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 21, min_periods=7)
    return out


def f18_lrch_002_lr_slope_logclose_63d(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 63, min_periods=21)
    return out


def f18_lrch_003_lr_slope_logclose_126d(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 126, min_periods=42)
    return out


def f18_lrch_004_lr_slope_logclose_252d(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 252, min_periods=84)
    return out


def f18_lrch_005_lr_slope_logclose_504d(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 504, min_periods=168)
    return out


def f18_lrch_006_lr_slope_close_raw_252d(close: pd.Series) -> pd.Series:
    out = _rolling_slope(close, 252, min_periods=84)
    return out


def f18_lrch_007_lr_slope_log_norm_by_close_63d(close: pd.Series) -> pd.Series:
    out = _safe_div(_rolling_slope(_safe_log(close), 63, min_periods=21), 1.0)
    return out


def f18_lrch_008_lr_slope_atr_norm_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _rolling_slope(close, 63, min_periods=21)
    out = _safe_div(sl, _atr(high, low, close, n=21))
    return out


def f18_lrch_009_lr_slope_atr_norm_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _rolling_slope(close, 252, min_periods=84)
    out = _safe_div(sl, _atr(high, low, close, n=21))
    return out


def f18_lrch_010_lr_slope_high_minus_low_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(high), 252, min_periods=84) - _rolling_slope(_safe_log(low), 252, min_periods=84)
    return out


def f18_lrch_011_lr_slope_ohlc4_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (open + high + low + close) / 4.0
    out = _rolling_slope(_safe_log(tp), 63, min_periods=21)
    return out


def f18_lrch_012_lr_slope_ohlc4_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (open + high + low + close) / 4.0
    out = _rolling_slope(_safe_log(tp), 252, min_periods=84)
    return out


def f18_lrch_013_lr_slope_annualized_63d(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 63, min_periods=21) * (252.0 / 63.0)
    return out


def f18_lrch_014_lr_slope_annualized_252d(close: pd.Series) -> pd.Series:
    out = _rolling_slope(_safe_log(close), 252, min_periods=84) * 1.0
    return out


def f18_lrch_015_lr_slope_hl_mid_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    mid = (high + low) / 2.0
    out = _rolling_slope(_safe_log(mid), 252, min_periods=84)
    return out


def f18_lrch_016_lr_r2_logclose_21d(close: pd.Series) -> pd.Series:
    out = _rolling_r2(_safe_log(close), 21, min_periods=7)
    return out


def f18_lrch_017_lr_r2_logclose_63d(close: pd.Series) -> pd.Series:
    out = _rolling_r2(_safe_log(close), 63, min_periods=21)
    return out


def f18_lrch_018_lr_r2_logclose_252d(close: pd.Series) -> pd.Series:
    out = _rolling_r2(_safe_log(close), 252, min_periods=84)
    return out


def f18_lrch_019_lr_r2_logclose_504d(close: pd.Series) -> pd.Series:
    out = _rolling_r2(_safe_log(close), 504, min_periods=168)
    return out


def f18_lrch_020_lr_r2_close_raw_252d(close: pd.Series) -> pd.Series:
    out = _rolling_r2(close, 252, min_periods=84)
    return out


def f18_lrch_021_lr_high_r2_indicator_63d(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    out = (r2 > 0.7).astype(float).where(r2.notna(), np.nan)
    return out


def f18_lrch_022_frac_high_r2_63d_in_252d(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    hr = (r2 > 0.7).astype(float).where(r2.notna(), np.nan)
    out = hr.rolling(252, min_periods=84).mean()
    return out


def f18_lrch_023_frac_low_r2_63d_in_252d(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    lr = (r2 < 0.3).astype(float).where(r2.notna(), np.nan)
    out = lr.rolling(252, min_periods=84).mean()
    return out


def f18_lrch_024_lr_r2_short_minus_long_63_vs_252(close: pd.Series) -> pd.Series:
    out = _rolling_r2(_safe_log(close), 63, min_periods=21) - _rolling_r2(_safe_log(close), 252, min_periods=84)
    return out


def f18_lrch_025_lr_r2_snr_proxy_63d(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21).clip(0.0, 0.999)
    out = np.sqrt(r2 / (1.0 - r2))
    return out


def f18_lrch_026_lr_r2_snr_proxy_252d(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 252, min_periods=84).clip(0.0, 0.999)
    out = np.sqrt(r2 / (1.0 - r2))
    return out


def f18_lrch_027_lr_r2_high_minus_low_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    out = _rolling_r2(_safe_log(high), 252, min_periods=84) - _rolling_r2(_safe_log(low), 252, min_periods=84)
    return out


def f18_lrch_028_current_high_r2_streak_63d(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    hi = (r2 > 0.5).astype(int)
    block = (hi != hi.shift(1)).fillna(False).cumsum()
    streak = hi.groupby(block).cumcount()
    out = (streak.astype(float) * (hi > 0)).where(r2.notna(), np.nan)
    return out


def f18_lrch_029_lr_r2_pct_rank_63d_in_252d(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    out = r2.rolling(252, min_periods=84).apply(_rk, raw=True)
    return out


def f18_lrch_030_r2_regime_transition_count_252d_63d(close: pd.Series) -> pd.Series:
    r2 = _rolling_r2(_safe_log(close), 63, min_periods=21)
    hi = (r2 > 0.5).astype(float)
    trans = ((hi.shift(1) > 0.5) & (hi < 0.5)).astype(float).where(r2.notna() & r2.shift(1).notna(), np.nan)
    out = trans.rolling(252, min_periods=84).sum()
    return out


def f18_lrch_031_channel_width_log_2sigma_21d(close: pd.Series) -> pd.Series:
    out = 2.0 * _rolling_resid_std(_safe_log(close), 21, min_periods=7)
    return out


def f18_lrch_032_channel_width_log_2sigma_63d(close: pd.Series) -> pd.Series:
    out = 2.0 * _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    return out


def f18_lrch_033_channel_width_log_2sigma_252d(close: pd.Series) -> pd.Series:
    out = 2.0 * _rolling_resid_std(_safe_log(close), 252, min_periods=84)
    return out


def f18_lrch_034_channel_width_log_2sigma_504d(close: pd.Series) -> pd.Series:
    out = 2.0 * _rolling_resid_std(_safe_log(close), 504, min_periods=168)
    return out


def f18_lrch_035_channel_width_raw_2sigma_63d(close: pd.Series) -> pd.Series:
    out = 2.0 * _rolling_resid_std(close, 63, min_periods=21)
    return out


def f18_lrch_036_channel_width_atr_units_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    w = 2.0 * _rolling_resid_std(close, 63, min_periods=21)
    out = _safe_div(w, _atr(high, low, close, n=21))
    return out


def f18_lrch_037_channel_width_atr_units_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    w = 2.0 * _rolling_resid_std(close, 252, min_periods=84)
    out = _safe_div(w, _atr(high, low, close, n=21))
    return out


def f18_lrch_038_channel_width_ratio_63_over_252(close: pd.Series) -> pd.Series:
    w63 = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    w252 = _rolling_resid_std(_safe_log(close), 252, min_periods=84)
    out = _safe_div(w63, w252)
    return out


def f18_lrch_039_channel_width_ratio_21_over_252(close: pd.Series) -> pd.Series:
    w21 = _rolling_resid_std(_safe_log(close), 21, min_periods=7)
    w252 = _rolling_resid_std(_safe_log(close), 252, min_periods=84)
    out = _safe_div(w21, w252)
    return out


def f18_lrch_040_channel_width_zscore_63d_in_252d(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    out = _rolling_zscore(w, 252, min_periods=84)
    return out


def f18_lrch_041_channel_width_zscore_252d_in_504d(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 252, min_periods=84)
    out = _rolling_zscore(w, 504, min_periods=168)
    return out


def f18_lrch_042_channel_width_pct_rank_63d_in_252d(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    def _rk(w_arr):
        if np.isnan(w_arr).all():
            return np.nan
        last = w_arr[-1]
        if np.isnan(last):
            return np.nan
        v = w_arr[~np.isnan(w_arr)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    out = w.rolling(252, min_periods=84).apply(_rk, raw=True)
    return out


def f18_lrch_043_channel_resid_skew_252d(close: pd.Series) -> pd.Series:
    out = _rolling_resid_skew(_safe_log(close), 252, min_periods=84)
    return out


def f18_lrch_044_channel_resid_skew_63d(close: pd.Series) -> pd.Series:
    out = _rolling_resid_skew(_safe_log(close), 63, min_periods=21)
    return out


def f18_lrch_045_channel_width_growth_slope_63d_over_63d(close: pd.Series) -> pd.Series:
    w = _rolling_resid_std(_safe_log(close), 63, min_periods=21)
    out = _rolling_slope(w, 63, min_periods=21)
    return out


def f18_lrch_046_channel_position_zscore_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    out = _safe_div(lc - tl, rs)
    return out


def f18_lrch_047_channel_position_zscore_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    rs = _rolling_resid_std(lc, 252, min_periods=84)
    out = _safe_div(lc - tl, rs)
    return out


def f18_lrch_048_channel_position_zscore_504d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 504, min_periods=168)
    rs = _rolling_resid_std(lc, 504, min_periods=168)
    out = _safe_div(lc - tl, rs)
    return out


def f18_lrch_049_channel_position_normalized_0to1_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    resid = lc - tl
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    out = resid.rolling(63, min_periods=21).apply(_rk, raw=True)
    return out


def f18_lrch_050_close_top_quintile_channel_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    resid = lc - tl
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    rk = resid.rolling(63, min_periods=21).apply(_rk, raw=True)
    out = (rk >= 0.8).astype(float).where(rk.notna(), np.nan)
    return out


def f18_lrch_051_close_bottom_quintile_channel_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    resid = lc - tl
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    rk = resid.rolling(63, min_periods=21).apply(_rk, raw=True)
    out = (rk <= 0.2).astype(float).where(rk.notna(), np.nan)
    return out


def f18_lrch_052_dwell_upper_half_channel_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    up = (lc > tl).astype(float).where(tl.notna(), np.nan)
    out = up.rolling(252, min_periods=84).mean()
    return out


def f18_lrch_053_dwell_upper_quintile_channel_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    in_top = (lc > tl + rs).astype(float).where(rs.notna(), np.nan)
    out = in_top.rolling(252, min_periods=84).mean()
    return out


def f18_lrch_054_bars_since_lower_band_touch_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    lb = tl - 2.0 * rs
    touch = (lc <= lb).fillna(False)
    arr = touch.astype(bool).values
    n = arr.size
    out_arr = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out_arr[i] = float(i - last)
    out = pd.Series(out_arr, index=lc.index)
    return out


def f18_lrch_055_bars_since_upper_band_touch_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 2.0 * rs
    touch = (lc >= ub).fillna(False)
    arr = touch.astype(bool).values
    n = arr.size
    out_arr = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out_arr[i] = float(i - last)
    out = pd.Series(out_arr, index=lc.index)
    return out


def f18_lrch_056_dwell_extreme_bands_density_63d_in_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    z = _safe_div(lc - tl, rs)
    ex = (z.abs() > 1.5).astype(float).where(z.notna(), np.nan)
    out = ex.rolling(252, min_periods=84).mean()
    return out


def f18_lrch_057_channel_position_volatility_21d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    z = _safe_div(lc - tl, rs)
    out = z.rolling(21, min_periods=7).std()
    return out


def f18_lrch_058_current_upper_half_streak_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    up = (lc > tl).astype(int).where(tl.notna(), 0)
    block = (up != up.shift(1)).fillna(False).cumsum()
    streak = up.groupby(block).cumcount().astype(float)
    out = (streak * (up > 0)).where(tl.notna(), np.nan)
    return out


def f18_lrch_059_close_above_upper_band_indicator_252d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    rs = _rolling_resid_std(lc, 252, min_periods=84)
    ub = tl + 2.0 * rs
    out = (lc >= ub).astype(float).where(rs.notna(), np.nan)
    return out


def f18_lrch_060_close_above_3sigma_upper_band_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 3.0 * rs
    out = (lc >= ub).astype(float).where(rs.notna(), np.nan)
    return out


def f18_lrch_061_upper_band_2sigma_touch_count_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 2.0 * rs
    ev = (lc >= ub).astype(float).where(rs.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).sum()
    return out


def f18_lrch_062_lower_band_2sigma_pierce_count_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    lb = tl - 2.0 * rs
    ev = (lc <= lb).astype(float).where(rs.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).sum()
    return out


def f18_lrch_063_band_touch_asymmetry_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 2.0 * rs; lb = tl - 2.0 * rs
    ut = (lc >= ub).astype(float).where(rs.notna(), np.nan).rolling(252, min_periods=84).sum()
    lt = (lc <= lb).astype(float).where(rs.notna(), np.nan).rolling(252, min_periods=84).sum()
    out = ut - lt
    return out


def f18_lrch_064_furthest_upper_pierce_max_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 2.0 * rs
    exc = (lc - ub).clip(lower=0).where(rs.notna(), np.nan)
    out = exc.rolling(252, min_periods=84).max()
    return out


def f18_lrch_065_furthest_lower_pierce_max_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    lb = tl - 2.0 * rs
    exc = (lb - lc).clip(lower=0).where(rs.notna(), np.nan)
    out = exc.rolling(252, min_periods=84).max()
    return out


def f18_lrch_066_mean_upper_pierce_excursion_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 2.0 * rs
    exc = (lc - ub).where(lc > ub, np.nan)
    out = exc.rolling(252, min_periods=84).mean()
    return out


def f18_lrch_067_mean_lower_pierce_excursion_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    lb = tl - 2.0 * rs
    exc = (lb - lc).where(lc < lb, np.nan)
    out = exc.rolling(252, min_periods=84).mean()
    return out


def f18_lrch_068_upper_band_touch_density_252d_channel(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 252, min_periods=84)
    rs = _rolling_resid_std(lc, 252, min_periods=84)
    ub = tl + 2.0 * rs
    ev = (lc >= ub).astype(float).where(rs.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).mean()
    return out


def f18_lrch_069_walking_upper_band_3bars_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 2.0 * rs
    touch = (lc >= ub).astype(float).where(rs.notna(), np.nan)
    out = (touch.rolling(3, min_periods=3).min() > 0.5).astype(float).where(rs.notna(), np.nan)
    return out


def f18_lrch_070_upper_band_cross_event_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 2.0 * rs
    above = (lc >= ub).astype(float).where(rs.notna(), np.nan)
    out = ((above.shift(1) < 0.5) & (above > 0.5)).astype(float).where(rs.notna() & rs.shift(1).notna(), np.nan)
    return out


def f18_lrch_071_mean_inter_upper_touch_gap_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 2.0 * rs
    touch = (lc >= ub).astype(float).where(rs.notna(), np.nan)
    cnt = touch.rolling(252, min_periods=84).sum()
    out = 252.0 / cnt.replace(0, np.nan)
    return out


def f18_lrch_072_lower_band_cross_event_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    lb = tl - 2.0 * rs
    below = (lc <= lb).astype(float).where(rs.notna(), np.nan)
    out = ((below.shift(1) < 0.5) & (below > 0.5)).astype(float).where(rs.notna() & rs.shift(1).notna(), np.nan)
    return out


def f18_lrch_073_both_bands_touched_in_21d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 2.0 * rs; lb = tl - 2.0 * rs
    ut = (lc >= ub).astype(float).where(rs.notna(), np.nan).rolling(21, min_periods=5).max()
    lt = (lc <= lb).astype(float).where(rs.notna(), np.nan).rolling(21, min_periods=5).max()
    out = ((ut > 0.5) & (lt > 0.5)).astype(float).where(ut.notna() & lt.notna(), np.nan)
    return out


def f18_lrch_074_intra_channel_range_pct_21d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    w = 2.0 * _rolling_resid_std(lc, 63, min_periods=21)
    rng = lc.rolling(21, min_periods=7).max() - lc.rolling(21, min_periods=7).min()
    out = _safe_div(rng, w)
    return out


def f18_lrch_075_one_sigma_touch_count_252d_63d(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    tl = _rolling_lr_endpoint(lc, 63, min_periods=21)
    rs = _rolling_resid_std(lc, 63, min_periods=21)
    ub = tl + 1.0 * rs
    ev = (lc >= ub).astype(float).where(rs.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).sum()
    return out


# ============================================================
#                         REGISTRY 001_075 (base)
# ============================================================

LINEAR_REGRESSION_CHANNEL_BASE_REGISTRY_001_075 = {
    "f18_lrch_001_lr_slope_logclose_21d": {"inputs": ["close"], "func": f18_lrch_001_lr_slope_logclose_21d},
    "f18_lrch_002_lr_slope_logclose_63d": {"inputs": ["close"], "func": f18_lrch_002_lr_slope_logclose_63d},
    "f18_lrch_003_lr_slope_logclose_126d": {"inputs": ["close"], "func": f18_lrch_003_lr_slope_logclose_126d},
    "f18_lrch_004_lr_slope_logclose_252d": {"inputs": ["close"], "func": f18_lrch_004_lr_slope_logclose_252d},
    "f18_lrch_005_lr_slope_logclose_504d": {"inputs": ["close"], "func": f18_lrch_005_lr_slope_logclose_504d},
    "f18_lrch_006_lr_slope_close_raw_252d": {"inputs": ["close"], "func": f18_lrch_006_lr_slope_close_raw_252d},
    "f18_lrch_007_lr_slope_log_norm_by_close_63d": {"inputs": ["close"], "func": f18_lrch_007_lr_slope_log_norm_by_close_63d},
    "f18_lrch_008_lr_slope_atr_norm_63d": {"inputs": ["high", "low", "close"], "func": f18_lrch_008_lr_slope_atr_norm_63d},
    "f18_lrch_009_lr_slope_atr_norm_252d": {"inputs": ["high", "low", "close"], "func": f18_lrch_009_lr_slope_atr_norm_252d},
    "f18_lrch_010_lr_slope_high_minus_low_252d": {"inputs": ["high", "low"], "func": f18_lrch_010_lr_slope_high_minus_low_252d},
    "f18_lrch_011_lr_slope_ohlc4_63d": {"inputs": ["open", "high", "low", "close"], "func": f18_lrch_011_lr_slope_ohlc4_63d},
    "f18_lrch_012_lr_slope_ohlc4_252d": {"inputs": ["open", "high", "low", "close"], "func": f18_lrch_012_lr_slope_ohlc4_252d},
    "f18_lrch_013_lr_slope_annualized_63d": {"inputs": ["close"], "func": f18_lrch_013_lr_slope_annualized_63d},
    "f18_lrch_014_lr_slope_annualized_252d": {"inputs": ["close"], "func": f18_lrch_014_lr_slope_annualized_252d},
    "f18_lrch_015_lr_slope_hl_mid_252d": {"inputs": ["high", "low"], "func": f18_lrch_015_lr_slope_hl_mid_252d},
    "f18_lrch_016_lr_r2_logclose_21d": {"inputs": ["close"], "func": f18_lrch_016_lr_r2_logclose_21d},
    "f18_lrch_017_lr_r2_logclose_63d": {"inputs": ["close"], "func": f18_lrch_017_lr_r2_logclose_63d},
    "f18_lrch_018_lr_r2_logclose_252d": {"inputs": ["close"], "func": f18_lrch_018_lr_r2_logclose_252d},
    "f18_lrch_019_lr_r2_logclose_504d": {"inputs": ["close"], "func": f18_lrch_019_lr_r2_logclose_504d},
    "f18_lrch_020_lr_r2_close_raw_252d": {"inputs": ["close"], "func": f18_lrch_020_lr_r2_close_raw_252d},
    "f18_lrch_021_lr_high_r2_indicator_63d": {"inputs": ["close"], "func": f18_lrch_021_lr_high_r2_indicator_63d},
    "f18_lrch_022_frac_high_r2_63d_in_252d": {"inputs": ["close"], "func": f18_lrch_022_frac_high_r2_63d_in_252d},
    "f18_lrch_023_frac_low_r2_63d_in_252d": {"inputs": ["close"], "func": f18_lrch_023_frac_low_r2_63d_in_252d},
    "f18_lrch_024_lr_r2_short_minus_long_63_vs_252": {"inputs": ["close"], "func": f18_lrch_024_lr_r2_short_minus_long_63_vs_252},
    "f18_lrch_025_lr_r2_snr_proxy_63d": {"inputs": ["close"], "func": f18_lrch_025_lr_r2_snr_proxy_63d},
    "f18_lrch_026_lr_r2_snr_proxy_252d": {"inputs": ["close"], "func": f18_lrch_026_lr_r2_snr_proxy_252d},
    "f18_lrch_027_lr_r2_high_minus_low_252d": {"inputs": ["high", "low"], "func": f18_lrch_027_lr_r2_high_minus_low_252d},
    "f18_lrch_028_current_high_r2_streak_63d": {"inputs": ["close"], "func": f18_lrch_028_current_high_r2_streak_63d},
    "f18_lrch_029_lr_r2_pct_rank_63d_in_252d": {"inputs": ["close"], "func": f18_lrch_029_lr_r2_pct_rank_63d_in_252d},
    "f18_lrch_030_r2_regime_transition_count_252d_63d": {"inputs": ["close"], "func": f18_lrch_030_r2_regime_transition_count_252d_63d},
    "f18_lrch_031_channel_width_log_2sigma_21d": {"inputs": ["close"], "func": f18_lrch_031_channel_width_log_2sigma_21d},
    "f18_lrch_032_channel_width_log_2sigma_63d": {"inputs": ["close"], "func": f18_lrch_032_channel_width_log_2sigma_63d},
    "f18_lrch_033_channel_width_log_2sigma_252d": {"inputs": ["close"], "func": f18_lrch_033_channel_width_log_2sigma_252d},
    "f18_lrch_034_channel_width_log_2sigma_504d": {"inputs": ["close"], "func": f18_lrch_034_channel_width_log_2sigma_504d},
    "f18_lrch_035_channel_width_raw_2sigma_63d": {"inputs": ["close"], "func": f18_lrch_035_channel_width_raw_2sigma_63d},
    "f18_lrch_036_channel_width_atr_units_63d": {"inputs": ["high", "low", "close"], "func": f18_lrch_036_channel_width_atr_units_63d},
    "f18_lrch_037_channel_width_atr_units_252d": {"inputs": ["high", "low", "close"], "func": f18_lrch_037_channel_width_atr_units_252d},
    "f18_lrch_038_channel_width_ratio_63_over_252": {"inputs": ["close"], "func": f18_lrch_038_channel_width_ratio_63_over_252},
    "f18_lrch_039_channel_width_ratio_21_over_252": {"inputs": ["close"], "func": f18_lrch_039_channel_width_ratio_21_over_252},
    "f18_lrch_040_channel_width_zscore_63d_in_252d": {"inputs": ["close"], "func": f18_lrch_040_channel_width_zscore_63d_in_252d},
    "f18_lrch_041_channel_width_zscore_252d_in_504d": {"inputs": ["close"], "func": f18_lrch_041_channel_width_zscore_252d_in_504d},
    "f18_lrch_042_channel_width_pct_rank_63d_in_252d": {"inputs": ["close"], "func": f18_lrch_042_channel_width_pct_rank_63d_in_252d},
    "f18_lrch_043_channel_resid_skew_252d": {"inputs": ["close"], "func": f18_lrch_043_channel_resid_skew_252d},
    "f18_lrch_044_channel_resid_skew_63d": {"inputs": ["close"], "func": f18_lrch_044_channel_resid_skew_63d},
    "f18_lrch_045_channel_width_growth_slope_63d_over_63d": {"inputs": ["close"], "func": f18_lrch_045_channel_width_growth_slope_63d_over_63d},
    "f18_lrch_046_channel_position_zscore_63d": {"inputs": ["close"], "func": f18_lrch_046_channel_position_zscore_63d},
    "f18_lrch_047_channel_position_zscore_252d": {"inputs": ["close"], "func": f18_lrch_047_channel_position_zscore_252d},
    "f18_lrch_048_channel_position_zscore_504d": {"inputs": ["close"], "func": f18_lrch_048_channel_position_zscore_504d},
    "f18_lrch_049_channel_position_normalized_0to1_63d": {"inputs": ["close"], "func": f18_lrch_049_channel_position_normalized_0to1_63d},
    "f18_lrch_050_close_top_quintile_channel_63d": {"inputs": ["close"], "func": f18_lrch_050_close_top_quintile_channel_63d},
    "f18_lrch_051_close_bottom_quintile_channel_63d": {"inputs": ["close"], "func": f18_lrch_051_close_bottom_quintile_channel_63d},
    "f18_lrch_052_dwell_upper_half_channel_252d_63d": {"inputs": ["close"], "func": f18_lrch_052_dwell_upper_half_channel_252d_63d},
    "f18_lrch_053_dwell_upper_quintile_channel_252d_63d": {"inputs": ["close"], "func": f18_lrch_053_dwell_upper_quintile_channel_252d_63d},
    "f18_lrch_054_bars_since_lower_band_touch_63d": {"inputs": ["close"], "func": f18_lrch_054_bars_since_lower_band_touch_63d},
    "f18_lrch_055_bars_since_upper_band_touch_63d": {"inputs": ["close"], "func": f18_lrch_055_bars_since_upper_band_touch_63d},
    "f18_lrch_056_dwell_extreme_bands_density_63d_in_252d": {"inputs": ["close"], "func": f18_lrch_056_dwell_extreme_bands_density_63d_in_252d},
    "f18_lrch_057_channel_position_volatility_21d_63d": {"inputs": ["close"], "func": f18_lrch_057_channel_position_volatility_21d_63d},
    "f18_lrch_058_current_upper_half_streak_63d": {"inputs": ["close"], "func": f18_lrch_058_current_upper_half_streak_63d},
    "f18_lrch_059_close_above_upper_band_indicator_252d": {"inputs": ["close"], "func": f18_lrch_059_close_above_upper_band_indicator_252d},
    "f18_lrch_060_close_above_3sigma_upper_band_63d": {"inputs": ["close"], "func": f18_lrch_060_close_above_3sigma_upper_band_63d},
    "f18_lrch_061_upper_band_2sigma_touch_count_252d_63d": {"inputs": ["close"], "func": f18_lrch_061_upper_band_2sigma_touch_count_252d_63d},
    "f18_lrch_062_lower_band_2sigma_pierce_count_252d_63d": {"inputs": ["close"], "func": f18_lrch_062_lower_band_2sigma_pierce_count_252d_63d},
    "f18_lrch_063_band_touch_asymmetry_252d_63d": {"inputs": ["close"], "func": f18_lrch_063_band_touch_asymmetry_252d_63d},
    "f18_lrch_064_furthest_upper_pierce_max_252d_63d": {"inputs": ["close"], "func": f18_lrch_064_furthest_upper_pierce_max_252d_63d},
    "f18_lrch_065_furthest_lower_pierce_max_252d_63d": {"inputs": ["close"], "func": f18_lrch_065_furthest_lower_pierce_max_252d_63d},
    "f18_lrch_066_mean_upper_pierce_excursion_252d_63d": {"inputs": ["close"], "func": f18_lrch_066_mean_upper_pierce_excursion_252d_63d},
    "f18_lrch_067_mean_lower_pierce_excursion_252d_63d": {"inputs": ["close"], "func": f18_lrch_067_mean_lower_pierce_excursion_252d_63d},
    "f18_lrch_068_upper_band_touch_density_252d_channel": {"inputs": ["close"], "func": f18_lrch_068_upper_band_touch_density_252d_channel},
    "f18_lrch_069_walking_upper_band_3bars_63d": {"inputs": ["close"], "func": f18_lrch_069_walking_upper_band_3bars_63d},
    "f18_lrch_070_upper_band_cross_event_63d": {"inputs": ["close"], "func": f18_lrch_070_upper_band_cross_event_63d},
    "f18_lrch_071_mean_inter_upper_touch_gap_252d_63d": {"inputs": ["close"], "func": f18_lrch_071_mean_inter_upper_touch_gap_252d_63d},
    "f18_lrch_072_lower_band_cross_event_63d": {"inputs": ["close"], "func": f18_lrch_072_lower_band_cross_event_63d},
    "f18_lrch_073_both_bands_touched_in_21d_63d": {"inputs": ["close"], "func": f18_lrch_073_both_bands_touched_in_21d_63d},
    "f18_lrch_074_intra_channel_range_pct_21d_63d": {"inputs": ["close"], "func": f18_lrch_074_intra_channel_range_pct_21d_63d},
    "f18_lrch_075_one_sigma_touch_count_252d_63d": {"inputs": ["close"], "func": f18_lrch_075_one_sigma_touch_count_252d_63d},
}
