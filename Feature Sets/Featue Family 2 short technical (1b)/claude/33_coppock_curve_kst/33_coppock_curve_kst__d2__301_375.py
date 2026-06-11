"""33_coppock_curve_kst d2 features 301-375 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260

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
    idx = num.index if hasattr(num, 'index') else None
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)

def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()

def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()

def _wma(s, n):
    weights = np.arange(1, n + 1, dtype=float)
    wsum = weights.sum()

    def _ww(w):
        if np.isnan(w).any():
            return np.nan
        return float(np.dot(w, weights) / wsum)
    return s.rolling(n, min_periods=n).apply(_ww, raw=True)

def _roc_pct(s, n):
    return s.pct_change(n) * 100.0

def _coppock(close, n_long, n_short, n_wma):
    return _wma(_roc_pct(close, n_long) + _roc_pct(close, n_short), n_wma)

def _coppock_annual(close):
    return _coppock(close, 294, 231, 210)

def _coppock_biennial(close):
    return _coppock(close, DDAYS_2Y, 378, 210)

def _coppock_semi_annual(close):
    return _coppock(close, 126, 84, 42)

def _coppock_quarterly(close):
    return _coppock(close, QDAYS, 42, MDAYS)

def _dpo(close, n):
    return close - _sma(close, n)

def f33_cpkt_301_kst_std_roc10_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """1st KST standard component: SMA-10 of ROC(10). Individual signal — not the sum."""
    return _sma(_roc_pct(close, 10), 10).diff().diff()

def f33_cpkt_302_kst_std_roc15_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """2nd KST standard component: SMA-10 of ROC(15)."""
    return _sma(_roc_pct(close, 15), 10).diff().diff()

def f33_cpkt_303_kst_std_roc20_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """3rd KST standard component: SMA-10 of ROC(20)."""
    return _sma(_roc_pct(close, 20), 10).diff().diff()

def f33_cpkt_304_kst_std_roc30_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """4th KST standard component: SMA-15 of ROC(30)."""
    return _sma(_roc_pct(close, 30), 15).diff().diff()

def f33_cpkt_305_kst_std_roc10_smoothed_slope_21d_d2(close: pd.Series) -> pd.Series:
    """21d slope of the 1st KST standard component."""
    return _rolling_slope(_sma(_roc_pct(close, 10), 10), MDAYS).diff().diff()

def f33_cpkt_306_kst_std_roc15_smoothed_slope_21d_d2(close: pd.Series) -> pd.Series:
    """21d slope of the 2nd KST standard component."""
    return _rolling_slope(_sma(_roc_pct(close, 15), 10), MDAYS).diff().diff()

def f33_cpkt_307_kst_std_roc20_smoothed_slope_21d_d2(close: pd.Series) -> pd.Series:
    """21d slope of the 3rd KST standard component."""
    return _rolling_slope(_sma(_roc_pct(close, 20), 10), MDAYS).diff().diff()

def f33_cpkt_308_kst_std_roc30_smoothed_slope_21d_d2(close: pd.Series) -> pd.Series:
    """21d slope of the 4th KST standard component."""
    return _rolling_slope(_sma(_roc_pct(close, 30), 15), MDAYS).diff().diff()

def f33_cpkt_309_kst_long_roc65_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """1st KST long-term component: SMA-21 of ROC(65) — quarterly secular momentum."""
    return _sma(_roc_pct(close, 65), 21).diff().diff()

def f33_cpkt_310_kst_long_roc130_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """2nd KST long-term component: SMA-21 of ROC(130) — half-year secular momentum."""
    return _sma(_roc_pct(close, 130), 21).diff().diff()

def f33_cpkt_311_kst_long_roc195_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """3rd KST long-term component: SMA-21 of ROC(195) — 3/4-year secular momentum."""
    return _sma(_roc_pct(close, 195), 21).diff().diff()

def f33_cpkt_312_kst_long_roc260_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """4th KST long-term component: SMA-42 of ROC(260) — annual secular momentum."""
    return _sma(_roc_pct(close, 260), 42).diff().diff()

def f33_cpkt_313_kst_long_roc65_smoothed_slope_63d_d2(close: pd.Series) -> pd.Series:
    """63d slope of the 1st KST long-term component."""
    return _rolling_slope(_sma(_roc_pct(close, 65), 21), QDAYS).diff().diff()

def f33_cpkt_314_kst_long_roc130_smoothed_slope_63d_d2(close: pd.Series) -> pd.Series:
    """63d slope of the 2nd KST long-term component."""
    return _rolling_slope(_sma(_roc_pct(close, 130), 21), QDAYS).diff().diff()

def f33_cpkt_315_kst_long_roc195_smoothed_slope_63d_d2(close: pd.Series) -> pd.Series:
    """63d slope of the 3rd KST long-term component."""
    return _rolling_slope(_sma(_roc_pct(close, 195), 21), QDAYS).diff().diff()

def f33_cpkt_316_kst_long_roc260_smoothed_slope_63d_d2(close: pd.Series) -> pd.Series:
    """63d slope of the 4th KST long-term component."""
    return _rolling_slope(_sma(_roc_pct(close, 260), 42), QDAYS).diff().diff()

def f33_cpkt_317_kst_short_roc5_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """1st KST short-term component: SMA-5 of ROC(5) — acute momentum."""
    return _sma(_roc_pct(close, 5), 5).diff().diff()

def f33_cpkt_318_kst_short_roc8_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """2nd KST short-term component: SMA-5 of ROC(8)."""
    return _sma(_roc_pct(close, 8), 5).diff().diff()

def f33_cpkt_319_kst_short_roc12_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """3rd KST short-term component: SMA-5 of ROC(12)."""
    return _sma(_roc_pct(close, 12), 5).diff().diff()

def f33_cpkt_320_kst_short_roc18_smoothed_value_d2(close: pd.Series) -> pd.Series:
    """4th KST short-term component: SMA-8 of ROC(18)."""
    return _sma(_roc_pct(close, 18), 8).diff().diff()

def f33_cpkt_321_kst_short_roc5_smoothed_slope_5d_d2(close: pd.Series) -> pd.Series:
    """5d slope of the 1st KST short-term component."""
    return _rolling_slope(_sma(_roc_pct(close, 5), 5), WDAYS).diff().diff()

def f33_cpkt_322_kst_short_roc8_smoothed_slope_5d_d2(close: pd.Series) -> pd.Series:
    """5d slope of the 2nd KST short-term component."""
    return _rolling_slope(_sma(_roc_pct(close, 8), 5), WDAYS).diff().diff()

def f33_cpkt_323_kst_short_roc12_smoothed_slope_5d_d2(close: pd.Series) -> pd.Series:
    """5d slope of the 3rd KST short-term component."""
    return _rolling_slope(_sma(_roc_pct(close, 12), 5), WDAYS).diff().diff()

def f33_cpkt_324_kst_short_roc18_smoothed_slope_5d_d2(close: pd.Series) -> pd.Series:
    """5d slope of the 4th KST short-term component."""
    return _rolling_slope(_sma(_roc_pct(close, 18), 8), WDAYS).diff().diff()

def f33_cpkt_325_coppock_quarterly_above_zero_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when quarterly Coppock > 0 (short-cycle bullish regime)."""
    c = _coppock_quarterly(close)
    return (c > 0).astype(float).where(c.notna(), np.nan).diff().diff()

def f33_cpkt_326_coppock_semi_annual_above_zero_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when semi-annual Coppock > 0 (intermediate bullish regime)."""
    c = _coppock_semi_annual(close)
    return (c > 0).astype(float).where(c.notna(), np.nan).diff().diff()

def f33_cpkt_327_coppock_biennial_above_zero_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when biennial Coppock > 0 (secular bullish regime)."""
    c = _coppock_biennial(close)
    return (c > 0).astype(float).where(c.notna(), np.nan).diff().diff()

def f33_cpkt_328_coppock_quarterly_days_since_positive_cross_d2(close: pd.Series) -> pd.Series:
    """Bars since last bullish zero-crossing of quarterly Coppock."""
    c = _coppock_quarterly(close)
    flag = ((c.shift(1) < 0) & (c >= 0)).astype(float)
    return _bars_since_true(flag).diff().diff()

def f33_cpkt_329_coppock_semi_annual_days_since_positive_cross_d2(close: pd.Series) -> pd.Series:
    """Bars since last bullish zero-crossing of semi-annual Coppock."""
    c = _coppock_semi_annual(close)
    flag = ((c.shift(1) < 0) & (c >= 0)).astype(float)
    return _bars_since_true(flag).diff().diff()

def f33_cpkt_330_coppock_biennial_days_since_positive_cross_d2(close: pd.Series) -> pd.Series:
    """Bars since last bullish zero-crossing of biennial Coppock."""
    c = _coppock_biennial(close)
    flag = ((c.shift(1) < 0) & (c >= 0)).astype(float)
    return _bars_since_true(flag).diff().diff()

def f33_cpkt_331_coppock_quarterly_days_since_negative_cross_d2(close: pd.Series) -> pd.Series:
    """Bars since last bearish zero-crossing of quarterly Coppock — age of bearish regime."""
    c = _coppock_quarterly(close)
    flag = ((c.shift(1) > 0) & (c <= 0)).astype(float)
    return _bars_since_true(flag).diff().diff()

def f33_cpkt_332_coppock_semi_annual_days_since_negative_cross_d2(close: pd.Series) -> pd.Series:
    """Bars since last bearish zero-crossing of semi-annual Coppock."""
    c = _coppock_semi_annual(close)
    flag = ((c.shift(1) > 0) & (c <= 0)).astype(float)
    return _bars_since_true(flag).diff().diff()

def f33_cpkt_333_coppock_biennial_days_since_negative_cross_d2(close: pd.Series) -> pd.Series:
    """Bars since last bearish zero-crossing of biennial Coppock."""
    c = _coppock_biennial(close)
    flag = ((c.shift(1) > 0) & (c <= 0)).astype(float)
    return _bars_since_true(flag).diff().diff()

def f33_cpkt_334_coppock_quarterly_fraction_positive_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars with quarterly Coppock > 0."""
    c = _coppock_quarterly(close)
    return (c > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f33_cpkt_335_coppock_semi_annual_fraction_positive_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars with semi-annual Coppock > 0."""
    c = _coppock_semi_annual(close)
    return (c > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f33_cpkt_336_coppock_biennial_fraction_positive_252d_d2(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars with biennial Coppock > 0."""
    c = _coppock_biennial(close)
    return (c > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f33_cpkt_337_coppock_quarterly_longest_positive_run_252d_d2(close: pd.Series) -> pd.Series:
    """Longest consecutive-positive run length for quarterly Coppock within trailing 252d."""
    c = _coppock_quarterly(close)
    flag = (c > 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f33_cpkt_338_coppock_semi_annual_longest_positive_run_252d_d2(close: pd.Series) -> pd.Series:
    """Longest consecutive-positive run length for semi-annual Coppock within trailing 252d."""
    c = _coppock_semi_annual(close)
    flag = (c > 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f33_cpkt_339_coppock_biennial_longest_positive_run_252d_d2(close: pd.Series) -> pd.Series:
    """Longest consecutive-positive run length for biennial Coppock within trailing 252d."""
    c = _coppock_biennial(close)
    flag = (c > 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f33_cpkt_340_coppock_quarterly_longest_negative_run_252d_d2(close: pd.Series) -> pd.Series:
    """Longest consecutive-negative run length for quarterly Coppock within trailing 252d."""
    c = _coppock_quarterly(close)
    flag = (c < 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f33_cpkt_341_coppock_semi_annual_longest_negative_run_252d_d2(close: pd.Series) -> pd.Series:
    """Longest consecutive-negative run length for semi-annual Coppock within trailing 252d."""
    c = _coppock_semi_annual(close)
    flag = (c < 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f33_cpkt_342_coppock_biennial_longest_negative_run_252d_d2(close: pd.Series) -> pd.Series:
    """Longest consecutive-negative run length for biennial Coppock within trailing 252d."""
    c = _coppock_biennial(close)
    flag = (c < 0).astype(int)
    grp = (flag == 0).cumsum()
    run = flag.groupby(grp).cumsum().astype(float)
    return run.rolling(YDAYS, min_periods=QDAYS).max().diff().diff()

def f33_cpkt_343_coppock_quarterly_peak_to_current_decay_pct_d2(close: pd.Series) -> pd.Series:
    """% decay of quarterly Coppock from its trailing 252d max."""
    c = _coppock_quarterly(close)
    mx = c.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(c - mx, mx.abs()).diff().diff()

def f33_cpkt_344_coppock_semi_annual_peak_to_current_decay_pct_d2(close: pd.Series) -> pd.Series:
    """% decay of semi-annual Coppock from its trailing 252d max."""
    c = _coppock_semi_annual(close)
    mx = c.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(c - mx, mx.abs()).diff().diff()

def f33_cpkt_345_coppock_biennial_peak_to_current_decay_pct_d2(close: pd.Series) -> pd.Series:
    """% decay of biennial Coppock from its trailing 252d max."""
    c = _coppock_biennial(close)
    mx = c.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(c - mx, mx.abs()).diff().diff()

def f33_cpkt_346_coppock_quarterly_days_since_252d_peak_d2(close: pd.Series) -> pd.Series:
    """Bars since quarterly Coppock printed its trailing 252d maximum."""
    c = _coppock_quarterly(close)
    flag = (c == c.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    return _bars_since_true(flag).diff().diff()

def f33_cpkt_347_coppock_semi_annual_days_since_252d_peak_d2(close: pd.Series) -> pd.Series:
    """Bars since semi-annual Coppock printed its trailing 252d max."""
    c = _coppock_semi_annual(close)
    flag = (c == c.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    return _bars_since_true(flag).diff().diff()

def f33_cpkt_348_coppock_biennial_days_since_252d_peak_d2(close: pd.Series) -> pd.Series:
    """Bars since biennial Coppock printed its trailing 252d max."""
    c = _coppock_biennial(close)
    flag = (c == c.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    return _bars_since_true(flag).diff().diff()

def f33_cpkt_349_coppock_quarterly_d2_21d_d2(close: pd.Series) -> pd.Series:
    """d²(quarterly Coppock) at 21d-of-21d horizon — short-cycle acceleration."""
    c = _coppock_quarterly(close)
    return _rolling_slope(_rolling_slope(c, MDAYS), MDAYS).diff().diff()

def f33_cpkt_350_coppock_semi_annual_d2_21d_d2(close: pd.Series) -> pd.Series:
    """d²(semi-annual Coppock) at 21d horizon."""
    c = _coppock_semi_annual(close)
    return _rolling_slope(_rolling_slope(c, MDAYS), MDAYS).diff().diff()

def f33_cpkt_351_coppock_biennial_d2_21d_d2(close: pd.Series) -> pd.Series:
    """d²(biennial Coppock) at 21d horizon."""
    c = _coppock_biennial(close)
    return _rolling_slope(_rolling_slope(c, MDAYS), MDAYS).diff().diff()

def f33_cpkt_352_coppock_quarterly_d2_63d_d2(close: pd.Series) -> pd.Series:
    """d²(quarterly Coppock) at 63d-of-63d horizon — medium-cycle acceleration."""
    c = _coppock_quarterly(close)
    return _rolling_slope(_rolling_slope(c, QDAYS), QDAYS).diff().diff()

def f33_cpkt_353_coppock_semi_annual_d2_63d_d2(close: pd.Series) -> pd.Series:
    """d²(semi-annual Coppock) at 63d horizon."""
    c = _coppock_semi_annual(close)
    return _rolling_slope(_rolling_slope(c, QDAYS), QDAYS).diff().diff()

def f33_cpkt_354_coppock_biennial_d2_63d_d2(close: pd.Series) -> pd.Series:
    """d²(biennial Coppock) at 63d horizon."""
    c = _coppock_biennial(close)
    return _rolling_slope(_rolling_slope(c, QDAYS), QDAYS).diff().diff()

def f33_cpkt_355_coppock_quarterly_jerk_d3_21d_d2(close: pd.Series) -> pd.Series:
    """d³(quarterly Coppock) — jerk (rate of change of acceleration)."""
    c = _coppock_quarterly(close)
    return _rolling_slope(_rolling_slope(_rolling_slope(c, MDAYS), MDAYS), MDAYS).diff().diff()

def f33_cpkt_356_coppock_semi_annual_jerk_d3_21d_d2(close: pd.Series) -> pd.Series:
    """d³(semi-annual Coppock)."""
    c = _coppock_semi_annual(close)
    return _rolling_slope(_rolling_slope(_rolling_slope(c, MDAYS), MDAYS), MDAYS).diff().diff()

def f33_cpkt_357_coppock_biennial_jerk_d3_21d_d2(close: pd.Series) -> pd.Series:
    """d³(biennial Coppock)."""
    c = _coppock_biennial(close)
    return _rolling_slope(_rolling_slope(_rolling_slope(c, MDAYS), MDAYS), MDAYS).diff().diff()

def f33_cpkt_358_coppock_quarterly_dist_from_252d_max_d2(close: pd.Series) -> pd.Series:
    """Quarterly Coppock minus its trailing 252d max."""
    c = _coppock_quarterly(close)
    return (c - c.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff()

def f33_cpkt_359_coppock_semi_annual_dist_from_252d_max_d2(close: pd.Series) -> pd.Series:
    """Semi-annual Coppock minus its trailing 252d max."""
    c = _coppock_semi_annual(close)
    return (c - c.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff()

def f33_cpkt_360_coppock_biennial_dist_from_252d_max_d2(close: pd.Series) -> pd.Series:
    """Biennial Coppock minus its trailing 252d max."""
    c = _coppock_biennial(close)
    return (c - c.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff()

def f33_cpkt_361_special_k_component_1_sma10_roc10_d2(close: pd.Series) -> pd.Series:
    """Special K component 1 (weight 1): SMA-10 of ROC(10)."""
    return _sma(_roc_pct(close, 10), 10).diff().diff()

def f33_cpkt_362_special_k_component_2_sma10_roc15_d2(close: pd.Series) -> pd.Series:
    """Special K component 2 (weight 2): SMA-10 of ROC(15). (Note: weight applied at composite-build.)"""
    return _sma(_roc_pct(close, 15), 10).diff().diff()

def f33_cpkt_363_special_k_component_3_sma10_roc20_d2(close: pd.Series) -> pd.Series:
    """Special K component 3 (weight 3): SMA-10 of ROC(20)."""
    return _sma(_roc_pct(close, 20), 10).diff().diff()

def f33_cpkt_364_special_k_component_4_sma15_roc30_d2(close: pd.Series) -> pd.Series:
    """Special K component 4 (weight 4): SMA-15 of ROC(30)."""
    return _sma(_roc_pct(close, 30), 15).diff().diff()

def f33_cpkt_365_special_k_component_5_sma50_roc50_d2(close: pd.Series) -> pd.Series:
    """Special K component 5: SMA-50 of ROC(50)."""
    return _sma(_roc_pct(close, 50), 50).diff().diff()

def f33_cpkt_366_special_k_component_6_sma65_roc65_d2(close: pd.Series) -> pd.Series:
    """Special K component 6: SMA-65 of ROC(65)."""
    return _sma(_roc_pct(close, 65), 65).diff().diff()

def f33_cpkt_367_special_k_component_7_sma100_roc100_d2(close: pd.Series) -> pd.Series:
    """Special K component 7: SMA-100 of ROC(100)."""
    return _sma(_roc_pct(close, 100), 100).diff().diff()

def f33_cpkt_368_special_k_component_8_sma130_roc195_d2(close: pd.Series) -> pd.Series:
    """Special K component 8: SMA-130 of ROC(195) — longest-cycle component."""
    return _sma(_roc_pct(close, 195), 130).diff().diff()

def f33_cpkt_369_dpo21_value_d2(close: pd.Series) -> pd.Series:
    """Detrended Price Oscillator at 21d horizon (monthly-cycle isolator)."""
    return _dpo(close, MDAYS).diff().diff()

def f33_cpkt_370_dpo42_value_d2(close: pd.Series) -> pd.Series:
    """DPO at 42d horizon (2-month cycle)."""
    return _dpo(close, 42).diff().diff()

def f33_cpkt_371_dpo504_value_d2(close: pd.Series) -> pd.Series:
    """DPO at 504d horizon (biennial cycle)."""
    return _dpo(close, DDAYS_2Y).diff().diff()

def f33_cpkt_372_dpo21_zscore_252d_d2(close: pd.Series) -> pd.Series:
    """Z-score of DPO(21) over 252d."""
    return _rolling_zscore(_dpo(close, MDAYS), YDAYS).diff().diff()

def f33_cpkt_373_dpo126_zscore_252d_d2(close: pd.Series) -> pd.Series:
    """Z-score of DPO(126) over 252d."""
    return _rolling_zscore(_dpo(close, 126), YDAYS).diff().diff()

def f33_cpkt_374_dpo252_pct_rank_504d_d2(close: pd.Series) -> pd.Series:
    """Percentile rank of DPO(252) in trailing 504d."""
    return _pct_rank(_dpo(close, YDAYS), DDAYS_2Y).diff().diff()

def f33_cpkt_375_dpo504_above_zero_indicator_d2(close: pd.Series) -> pd.Series:
    """+1 when DPO(504) > 0 (secular-cycle positive)."""
    d = _dpo(close, DDAYS_2Y)
    return (d > 0).astype(float).where(d.notna(), np.nan).diff().diff()
COPPOCK_CURVE_KST_D2_REGISTRY_301_375 = {'f33_cpkt_301_kst_std_roc10_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_301_kst_std_roc10_smoothed_value_d2}, 'f33_cpkt_302_kst_std_roc15_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_302_kst_std_roc15_smoothed_value_d2}, 'f33_cpkt_303_kst_std_roc20_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_303_kst_std_roc20_smoothed_value_d2}, 'f33_cpkt_304_kst_std_roc30_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_304_kst_std_roc30_smoothed_value_d2}, 'f33_cpkt_305_kst_std_roc10_smoothed_slope_21d_d2': {'inputs': ['close'], 'func': f33_cpkt_305_kst_std_roc10_smoothed_slope_21d_d2}, 'f33_cpkt_306_kst_std_roc15_smoothed_slope_21d_d2': {'inputs': ['close'], 'func': f33_cpkt_306_kst_std_roc15_smoothed_slope_21d_d2}, 'f33_cpkt_307_kst_std_roc20_smoothed_slope_21d_d2': {'inputs': ['close'], 'func': f33_cpkt_307_kst_std_roc20_smoothed_slope_21d_d2}, 'f33_cpkt_308_kst_std_roc30_smoothed_slope_21d_d2': {'inputs': ['close'], 'func': f33_cpkt_308_kst_std_roc30_smoothed_slope_21d_d2}, 'f33_cpkt_309_kst_long_roc65_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_309_kst_long_roc65_smoothed_value_d2}, 'f33_cpkt_310_kst_long_roc130_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_310_kst_long_roc130_smoothed_value_d2}, 'f33_cpkt_311_kst_long_roc195_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_311_kst_long_roc195_smoothed_value_d2}, 'f33_cpkt_312_kst_long_roc260_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_312_kst_long_roc260_smoothed_value_d2}, 'f33_cpkt_313_kst_long_roc65_smoothed_slope_63d_d2': {'inputs': ['close'], 'func': f33_cpkt_313_kst_long_roc65_smoothed_slope_63d_d2}, 'f33_cpkt_314_kst_long_roc130_smoothed_slope_63d_d2': {'inputs': ['close'], 'func': f33_cpkt_314_kst_long_roc130_smoothed_slope_63d_d2}, 'f33_cpkt_315_kst_long_roc195_smoothed_slope_63d_d2': {'inputs': ['close'], 'func': f33_cpkt_315_kst_long_roc195_smoothed_slope_63d_d2}, 'f33_cpkt_316_kst_long_roc260_smoothed_slope_63d_d2': {'inputs': ['close'], 'func': f33_cpkt_316_kst_long_roc260_smoothed_slope_63d_d2}, 'f33_cpkt_317_kst_short_roc5_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_317_kst_short_roc5_smoothed_value_d2}, 'f33_cpkt_318_kst_short_roc8_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_318_kst_short_roc8_smoothed_value_d2}, 'f33_cpkt_319_kst_short_roc12_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_319_kst_short_roc12_smoothed_value_d2}, 'f33_cpkt_320_kst_short_roc18_smoothed_value_d2': {'inputs': ['close'], 'func': f33_cpkt_320_kst_short_roc18_smoothed_value_d2}, 'f33_cpkt_321_kst_short_roc5_smoothed_slope_5d_d2': {'inputs': ['close'], 'func': f33_cpkt_321_kst_short_roc5_smoothed_slope_5d_d2}, 'f33_cpkt_322_kst_short_roc8_smoothed_slope_5d_d2': {'inputs': ['close'], 'func': f33_cpkt_322_kst_short_roc8_smoothed_slope_5d_d2}, 'f33_cpkt_323_kst_short_roc12_smoothed_slope_5d_d2': {'inputs': ['close'], 'func': f33_cpkt_323_kst_short_roc12_smoothed_slope_5d_d2}, 'f33_cpkt_324_kst_short_roc18_smoothed_slope_5d_d2': {'inputs': ['close'], 'func': f33_cpkt_324_kst_short_roc18_smoothed_slope_5d_d2}, 'f33_cpkt_325_coppock_quarterly_above_zero_indicator_d2': {'inputs': ['close'], 'func': f33_cpkt_325_coppock_quarterly_above_zero_indicator_d2}, 'f33_cpkt_326_coppock_semi_annual_above_zero_indicator_d2': {'inputs': ['close'], 'func': f33_cpkt_326_coppock_semi_annual_above_zero_indicator_d2}, 'f33_cpkt_327_coppock_biennial_above_zero_indicator_d2': {'inputs': ['close'], 'func': f33_cpkt_327_coppock_biennial_above_zero_indicator_d2}, 'f33_cpkt_328_coppock_quarterly_days_since_positive_cross_d2': {'inputs': ['close'], 'func': f33_cpkt_328_coppock_quarterly_days_since_positive_cross_d2}, 'f33_cpkt_329_coppock_semi_annual_days_since_positive_cross_d2': {'inputs': ['close'], 'func': f33_cpkt_329_coppock_semi_annual_days_since_positive_cross_d2}, 'f33_cpkt_330_coppock_biennial_days_since_positive_cross_d2': {'inputs': ['close'], 'func': f33_cpkt_330_coppock_biennial_days_since_positive_cross_d2}, 'f33_cpkt_331_coppock_quarterly_days_since_negative_cross_d2': {'inputs': ['close'], 'func': f33_cpkt_331_coppock_quarterly_days_since_negative_cross_d2}, 'f33_cpkt_332_coppock_semi_annual_days_since_negative_cross_d2': {'inputs': ['close'], 'func': f33_cpkt_332_coppock_semi_annual_days_since_negative_cross_d2}, 'f33_cpkt_333_coppock_biennial_days_since_negative_cross_d2': {'inputs': ['close'], 'func': f33_cpkt_333_coppock_biennial_days_since_negative_cross_d2}, 'f33_cpkt_334_coppock_quarterly_fraction_positive_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_334_coppock_quarterly_fraction_positive_252d_d2}, 'f33_cpkt_335_coppock_semi_annual_fraction_positive_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_335_coppock_semi_annual_fraction_positive_252d_d2}, 'f33_cpkt_336_coppock_biennial_fraction_positive_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_336_coppock_biennial_fraction_positive_252d_d2}, 'f33_cpkt_337_coppock_quarterly_longest_positive_run_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_337_coppock_quarterly_longest_positive_run_252d_d2}, 'f33_cpkt_338_coppock_semi_annual_longest_positive_run_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_338_coppock_semi_annual_longest_positive_run_252d_d2}, 'f33_cpkt_339_coppock_biennial_longest_positive_run_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_339_coppock_biennial_longest_positive_run_252d_d2}, 'f33_cpkt_340_coppock_quarterly_longest_negative_run_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_340_coppock_quarterly_longest_negative_run_252d_d2}, 'f33_cpkt_341_coppock_semi_annual_longest_negative_run_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_341_coppock_semi_annual_longest_negative_run_252d_d2}, 'f33_cpkt_342_coppock_biennial_longest_negative_run_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_342_coppock_biennial_longest_negative_run_252d_d2}, 'f33_cpkt_343_coppock_quarterly_peak_to_current_decay_pct_d2': {'inputs': ['close'], 'func': f33_cpkt_343_coppock_quarterly_peak_to_current_decay_pct_d2}, 'f33_cpkt_344_coppock_semi_annual_peak_to_current_decay_pct_d2': {'inputs': ['close'], 'func': f33_cpkt_344_coppock_semi_annual_peak_to_current_decay_pct_d2}, 'f33_cpkt_345_coppock_biennial_peak_to_current_decay_pct_d2': {'inputs': ['close'], 'func': f33_cpkt_345_coppock_biennial_peak_to_current_decay_pct_d2}, 'f33_cpkt_346_coppock_quarterly_days_since_252d_peak_d2': {'inputs': ['close'], 'func': f33_cpkt_346_coppock_quarterly_days_since_252d_peak_d2}, 'f33_cpkt_347_coppock_semi_annual_days_since_252d_peak_d2': {'inputs': ['close'], 'func': f33_cpkt_347_coppock_semi_annual_days_since_252d_peak_d2}, 'f33_cpkt_348_coppock_biennial_days_since_252d_peak_d2': {'inputs': ['close'], 'func': f33_cpkt_348_coppock_biennial_days_since_252d_peak_d2}, 'f33_cpkt_349_coppock_quarterly_d2_21d_d2': {'inputs': ['close'], 'func': f33_cpkt_349_coppock_quarterly_d2_21d_d2}, 'f33_cpkt_350_coppock_semi_annual_d2_21d_d2': {'inputs': ['close'], 'func': f33_cpkt_350_coppock_semi_annual_d2_21d_d2}, 'f33_cpkt_351_coppock_biennial_d2_21d_d2': {'inputs': ['close'], 'func': f33_cpkt_351_coppock_biennial_d2_21d_d2}, 'f33_cpkt_352_coppock_quarterly_d2_63d_d2': {'inputs': ['close'], 'func': f33_cpkt_352_coppock_quarterly_d2_63d_d2}, 'f33_cpkt_353_coppock_semi_annual_d2_63d_d2': {'inputs': ['close'], 'func': f33_cpkt_353_coppock_semi_annual_d2_63d_d2}, 'f33_cpkt_354_coppock_biennial_d2_63d_d2': {'inputs': ['close'], 'func': f33_cpkt_354_coppock_biennial_d2_63d_d2}, 'f33_cpkt_355_coppock_quarterly_jerk_d3_21d_d2': {'inputs': ['close'], 'func': f33_cpkt_355_coppock_quarterly_jerk_d3_21d_d2}, 'f33_cpkt_356_coppock_semi_annual_jerk_d3_21d_d2': {'inputs': ['close'], 'func': f33_cpkt_356_coppock_semi_annual_jerk_d3_21d_d2}, 'f33_cpkt_357_coppock_biennial_jerk_d3_21d_d2': {'inputs': ['close'], 'func': f33_cpkt_357_coppock_biennial_jerk_d3_21d_d2}, 'f33_cpkt_358_coppock_quarterly_dist_from_252d_max_d2': {'inputs': ['close'], 'func': f33_cpkt_358_coppock_quarterly_dist_from_252d_max_d2}, 'f33_cpkt_359_coppock_semi_annual_dist_from_252d_max_d2': {'inputs': ['close'], 'func': f33_cpkt_359_coppock_semi_annual_dist_from_252d_max_d2}, 'f33_cpkt_360_coppock_biennial_dist_from_252d_max_d2': {'inputs': ['close'], 'func': f33_cpkt_360_coppock_biennial_dist_from_252d_max_d2}, 'f33_cpkt_361_special_k_component_1_sma10_roc10_d2': {'inputs': ['close'], 'func': f33_cpkt_361_special_k_component_1_sma10_roc10_d2}, 'f33_cpkt_362_special_k_component_2_sma10_roc15_d2': {'inputs': ['close'], 'func': f33_cpkt_362_special_k_component_2_sma10_roc15_d2}, 'f33_cpkt_363_special_k_component_3_sma10_roc20_d2': {'inputs': ['close'], 'func': f33_cpkt_363_special_k_component_3_sma10_roc20_d2}, 'f33_cpkt_364_special_k_component_4_sma15_roc30_d2': {'inputs': ['close'], 'func': f33_cpkt_364_special_k_component_4_sma15_roc30_d2}, 'f33_cpkt_365_special_k_component_5_sma50_roc50_d2': {'inputs': ['close'], 'func': f33_cpkt_365_special_k_component_5_sma50_roc50_d2}, 'f33_cpkt_366_special_k_component_6_sma65_roc65_d2': {'inputs': ['close'], 'func': f33_cpkt_366_special_k_component_6_sma65_roc65_d2}, 'f33_cpkt_367_special_k_component_7_sma100_roc100_d2': {'inputs': ['close'], 'func': f33_cpkt_367_special_k_component_7_sma100_roc100_d2}, 'f33_cpkt_368_special_k_component_8_sma130_roc195_d2': {'inputs': ['close'], 'func': f33_cpkt_368_special_k_component_8_sma130_roc195_d2}, 'f33_cpkt_369_dpo21_value_d2': {'inputs': ['close'], 'func': f33_cpkt_369_dpo21_value_d2}, 'f33_cpkt_370_dpo42_value_d2': {'inputs': ['close'], 'func': f33_cpkt_370_dpo42_value_d2}, 'f33_cpkt_371_dpo504_value_d2': {'inputs': ['close'], 'func': f33_cpkt_371_dpo504_value_d2}, 'f33_cpkt_372_dpo21_zscore_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_372_dpo21_zscore_252d_d2}, 'f33_cpkt_373_dpo126_zscore_252d_d2': {'inputs': ['close'], 'func': f33_cpkt_373_dpo126_zscore_252d_d2}, 'f33_cpkt_374_dpo252_pct_rank_504d_d2': {'inputs': ['close'], 'func': f33_cpkt_374_dpo252_pct_rank_504d_d2}, 'f33_cpkt_375_dpo504_above_zero_indicator_d2': {'inputs': ['close'], 'func': f33_cpkt_375_dpo504_above_zero_indicator_d2}}