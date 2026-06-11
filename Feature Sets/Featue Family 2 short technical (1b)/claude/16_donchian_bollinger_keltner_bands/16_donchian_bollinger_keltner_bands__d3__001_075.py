"""16_donchian_bollinger_keltner_bands d3 features 001-075 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
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

def _bollinger(close, n, k):
    """Bollinger (upper, mid, lower) with SMA mid, k-sigma bands."""
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return (mid + k * sd, mid, mid - k * sd)

def _keltner(high, low, close, n_ema, n_atr, k):
    """Keltner (upper, mid, lower) with EMA mid (span=n_ema), ATR(n_atr) bands."""
    mid = close.ewm(span=n_ema, adjust=False, min_periods=max(n_ema // 3, 2)).mean()
    atr = _atr(high, low, close, n=n_atr)
    return (mid + k * atr, mid, mid - k * atr)

def _donchian(high, low, n):
    """Donchian (upper, lower) over trailing-n window."""
    mp = max(n // 3, 2)
    return (high.rolling(n, min_periods=mp).max(), low.rolling(n, min_periods=mp).min())

def _band_width_rel(upper, lower, mid):
    """(upper − lower) / mid."""
    return _safe_div(upper - lower, mid)

def _band_position(close, upper, lower):
    """(close − lower) / (upper − lower) — 0=at lower, 1=at upper."""
    return _safe_div(close - lower, upper - lower)

def _bars_since_true(mask):
    arr = mask.values.astype(bool)
    n = len(arr)
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)

def _streak_true(mask):
    arr = mask.values.astype(bool)
    n = len(arr)
    out = np.zeros(n, dtype=float)
    run = 0
    for i in range(n):
        run = run + 1 if arr[i] else 0
        out[i] = float(run)
    return pd.Series(out, index=mask.index)

def _starc(high, low, close, n=15, mult=2.0):
    """STARC bands (Stoller): SMA(close, n) ± mult × ATR(n). Returns (upper, mid, lower)."""
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    atr = _atr(high, low, close, n=n)
    return (mid + mult * atr, mid, mid - mult * atr)

def _acceleration_bands(high, low, close, n=20, factor=2.0):
    """Price Headley's Acceleration Bands. Returns (upper, mid, lower)."""
    ratio = factor * _safe_div(high - low, high + low)
    upper = (high * (1 + ratio)).rolling(n, min_periods=max(n // 3, 2)).mean()
    lower = (low * (1 - ratio)).rolling(n, min_periods=max(n // 3, 2)).mean()
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    return (upper, mid, lower)

def _moving_average_envelope(close, n, pct):
    """Moving Average Envelope: SMA(close, n) ± pct. Returns (upper, mid, lower)."""
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    return (mid * (1 + pct), mid, mid * (1 - pct))

def _choppiness_index(high, low, close, n=14):
    """Choppiness Index (Dreiss): 100 × log10(ΣTR/range) / log10(n). Low=trending, high=ranging."""
    mp = max(n // 3, 2)
    tr = _true_range(high, low, close)
    tr_sum = tr.rolling(n, min_periods=mp).sum()
    max_hi = high.rolling(n, min_periods=mp).max()
    min_lo = low.rolling(n, min_periods=mp).min()
    rng = (max_hi - min_lo).replace(0, np.nan)
    return 100.0 * np.log10(_safe_div(tr_sum, rng)) / np.log10(n)

def _mass_index(high, low, n=25, n_ema=9):
    """Mass Index (Dorsey): Σ(EMA9(HL)/EMA9(EMA9(HL))) over n. Reversal signal: cross >27 then <26.5."""
    hl = high - low
    e1 = hl.ewm(span=n_ema, adjust=False, min_periods=max(n_ema // 3, 2)).mean()
    e2 = e1.ewm(span=n_ema, adjust=False, min_periods=max(n_ema // 3, 2)).mean()
    ratio = _safe_div(e1, e2)
    return ratio.rolling(n, min_periods=max(n // 3, 2)).sum()

def _standard_error_bands(close, n=21, k=2.0):
    """Standard Error Bands: rolling LR line ± k × residual SE over n bars. Returns (upper, mid, lower)."""
    mp = max(n // 3, 3)
    arr = close.values
    nb = len(arr)
    mid_arr = np.full(nb, np.nan)
    se_arr = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - n + 1)
        if i - s + 1 < mp:
            continue
        w = arr[s:i + 1]
        valid = ~np.isnan(w)
        if valid.sum() < mp:
            continue
        w = w[valid]
        if w.size < 3:
            continue
        x = np.arange(w.size, dtype=float)
        xm = x.mean()
        wm = w.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            continue
        sxy = ((x - xm) * (w - wm)).sum()
        b = sxy / sxx
        a = wm - b * xm
        y_pred = a + b * x
        resid = w - y_pred
        mid_arr[i] = float(a + b * x[-1])
        se_arr[i] = float(np.sqrt((resid ** 2).sum() / max(w.size - 2, 1)))
    mid = pd.Series(mid_arr, index=close.index)
    se = pd.Series(se_arr, index=close.index)
    return (mid + k * se, mid, mid - k * se)

def f16_dbkb_001_bollinger_width_20_2_norm_mid_d3(close):
    """Bollinger(20,2) band width / mid — standard width measure."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _band_width_rel(upper, lower, mid).diff().diff().diff()

def f16_dbkb_002_keltner_width_20_10_2_norm_mid_d3(high, low, close):
    """Keltner(EMA20, ATR10, 2) band width / mid — volatility-based band width."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    return _band_width_rel(upper, lower, mid).diff().diff().diff()

def f16_dbkb_003_donchian_width_20_norm_mid_d3(high, low, close):
    """Donchian(20) width / midline ((upper+lower)/2) — range-based width."""
    u, l = _donchian(high, low, 20)
    mid = (u + l) / 2.0
    return _band_width_rel(u, l, mid).diff().diff().diff()

def f16_dbkb_004_donchian_width_55_norm_mid_d3(high, low, close):
    """Donchian(55) width / midline — multi-month range width (turtle horizon)."""
    u, l = _donchian(high, low, 55)
    mid = (u + l) / 2.0
    return _band_width_rel(u, l, mid).diff().diff().diff()

def f16_dbkb_005_bollinger_width_20_2_zscore_252d_d3(close):
    """Z-score of Bollinger(20,2) width in trailing 252d — tail-discriminative for extreme compression/expansion."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _rolling_zscore(_band_width_rel(upper, lower, mid), YDAYS).diff().diff().diff()

def f16_dbkb_006_pctile_rank_bollinger_width_20_in_252d_d3(close):
    """Empirical percentile rank of Bollinger(20,2) width in trailing 252d distribution."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    w = _band_width_rel(upper, lower, mid)

    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        v = arr[~np.isnan(arr)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return w.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True).diff().diff().diff()

def f16_dbkb_007_pctile_rank_keltner_width_20_in_504d_d3(high, low, close):
    """Empirical percentile rank of Keltner(20,10,2) width in trailing 504d."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    w = _band_width_rel(upper, lower, mid)

    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        v = arr[~np.isnan(arr)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return w.rolling(DDAYS_2Y, min_periods=YDAYS).apply(_rk, raw=True).diff().diff().diff()

def f16_dbkb_008_bollinger_width_expansion_rate_vs_63d_baseline_d3(close):
    """Current Bollinger(20,2) width ÷ trailing-63d mean width − 1 — expansion factor (>0=expanding, post-squeeze release)."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    w = _band_width_rel(upper, lower, mid)
    return (_safe_div(w, w.rolling(QDAYS, min_periods=MDAYS).mean()) - 1.0).diff().diff().diff()

def f16_dbkb_009_zscore_bollinger_width_20_in_252d_d3(close):
    """Z-score of Bollinger(20,2) width in trailing 252d."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _rolling_zscore(_band_width_rel(upper, lower, mid), YDAYS).diff().diff().diff()

def f16_dbkb_010_ratio_bollinger_width_20_to_252d_median_d3(close):
    """Current Bollinger(20,2) width / its trailing 252d median — squeeze ratio."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    w = _band_width_rel(upper, lower, mid)
    return _safe_div(w, w.rolling(YDAYS, min_periods=QDAYS).median()).diff().diff().diff()

def f16_dbkb_011_starc_width_15_2_norm_mid_d3(high, low, close):
    """STARC(15,2) band width / mid (Stoller: SMA mid + ATR bands; distinct from EMA-based Keltner)."""
    upper, mid, lower = _starc(high, low, close, n=15, mult=2.0)
    return _band_width_rel(upper, lower, mid).diff().diff().diff()

def f16_dbkb_012_diff_bollinger_width_now_minus_63d_ago_d3(close):
    """Bollinger(20,2) width now − 63d ago — width-expansion velocity."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    w = _band_width_rel(upper, lower, mid)
    return (w - w.shift(QDAYS)).diff().diff().diff()

def f16_dbkb_013_atr_norm_donchian_width_20_d3(high, low, close):
    """Donchian(20) width / ATR(20) — ATR-normalized range width."""
    u, l = _donchian(high, low, 20)
    return _safe_div(u - l, _atr(high, low, close, n=20)).diff().diff().diff()

def f16_dbkb_014_donchian_20_midline_distance_norm_close_d3(high, low, close):
    """(close − Donchian(20) midline) / close — distance from channel center; near zero = mean-reversion target reached."""
    u, l = _donchian(high, low, 20)
    return _safe_div(close - (u + l) / 2.0, close).diff().diff().diff()

def f16_dbkb_015_bollinger_pct_b_20_2_d3(close):
    """Bollinger %B (20,2): (close − lower)/(upper − lower)."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _band_position(close, upper, lower).diff().diff().diff()

def f16_dbkb_016_keltner_pct_position_20_10_2_d3(high, low, close):
    """Keltner %position (20,10,2): (close − lower)/(upper − lower)."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    return _band_position(close, upper, lower).diff().diff().diff()

def f16_dbkb_017_donchian_pct_position_20_d3(high, low, close):
    """Donchian(20) %position: (close − lower)/(upper − lower)."""
    u, l = _donchian(high, low, 20)
    return _band_position(close, u, l).diff().diff().diff()

def f16_dbkb_018_donchian_pct_position_252_d3(high, low, close):
    """Donchian(252) %position — annual range position."""
    u, l = _donchian(high, low, YDAYS)
    return _band_position(close, u, l).diff().diff().diff()

def f16_dbkb_019_zscore_bollinger_pct_b_in_63d_d3(close):
    """Z-score of Bollinger(20,2) %B in trailing 63d."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _rolling_zscore(_band_position(close, upper, lower), QDAYS).diff().diff().diff()

def f16_dbkb_020_consensus_position_avg_3systems_d3(high, low, close):
    """Mean of (Bollinger %B, Keltner %position, Donchian(20) %position) — multi-band consensus."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    p1 = _band_position(close, bu, bl)
    p2 = _band_position(close, ku, kl)
    p3 = _band_position(close, du, dl)
    return ((p1 + p2 + p3) / 3.0).diff().diff().diff()

def f16_dbkb_021_bollinger_pct_b_in_top_decile_d3(close):
    """Indicator: Bollinger %B > 0.9 — close in top decile of Bollinger band."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    pb = _band_position(close, upper, lower)
    return (pb > 0.9).astype(float).where(pb.notna(), np.nan).diff().diff().diff()

def f16_dbkb_022_bbw_to_atr_ratio_20_d3(high, low, close):
    """Bollinger(20,2) width ÷ (ATR(20)/close) — squared-vol band vs absolute-range band; diverges in tail events."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    bbw = _band_width_rel(upper, lower, mid)
    atr_pct = _safe_div(_atr(high, low, close, n=20), close)
    return _safe_div(bbw, atr_pct).diff().diff().diff()

def f16_dbkb_023_pctile_rank_donchian_pct_position_252_in_252d_d3(high, low, close):
    """Empirical percentile rank of Donchian(252) %position in trailing 252d."""
    u, l = _donchian(high, low, YDAYS)
    p = _band_position(close, u, l)

    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        v = arr[~np.isnan(arr)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return p.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True).diff().diff().diff()

def f16_dbkb_024_bollinger_upper_break_count_21d_d3(close):
    """Count of bars in 21d where close > Bollinger(20,2) upper."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    br = (close > upper).astype(float).where(upper.notna(), np.nan)
    return br.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f16_dbkb_025_bollinger_upper_break_count_63d_d3(close):
    """Count of bars in 63d where close > Bollinger(20,2) upper."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    br = (close > upper).astype(float).where(upper.notna(), np.nan)
    return br.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f16_dbkb_026_keltner_upper_break_count_63d_d3(high, low, close):
    """Count of bars in 63d where close > Keltner(20,10,2) upper."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    br = (close > upper).astype(float).where(upper.notna(), np.nan)
    return br.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f16_dbkb_027_donchian_upper_break_count_252d_d3(high, low, close):
    """Count of bars in 252d where high == Donchian(20) upper (new 20d-high prints)."""
    u, l = _donchian(high, low, 20)
    br = (high >= u).astype(float).where(u.notna(), np.nan)
    return br.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f16_dbkb_028_indicator_first_bollinger_upper_break_in_21d_d3(close):
    """Indicator: most recent Bollinger upper break (close > upper) happened in last 21d."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    br = ((close > upper) & upper.notna()).astype(bool)
    bsb = _bars_since_true(br)
    return ((bsb <= MDAYS) & bsb.notna()).astype(float).diff().diff().diff()

def f16_dbkb_029_bars_since_last_bollinger_upper_break_d3(close):
    """Bars since most recent Bollinger(20,2) upper break."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _bars_since_true(((close > upper) & upper.notna()).astype(bool)).diff().diff().diff()

def f16_dbkb_030_bollinger_lower_break_count_63d_d3(close):
    """Count of bars in 63d where close < Bollinger(20,2) lower."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    br = (close < lower).astype(float).where(lower.notna(), np.nan)
    return br.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f16_dbkb_031_donchian_upper_break_252d_count_d3(high, low, close):
    """Count of bars in 252d where high == Donchian(252) upper — new 252d-high prints (Turtle)."""
    u, l = _donchian(high, low, YDAYS)
    br = (high >= u).astype(float).where(u.notna(), np.nan)
    return br.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f16_dbkb_032_starc_pct_position_15_2_d3(high, low, close):
    """STARC(15,2) %position: (close − lower)/(upper − lower) — SMA-anchored ATR-band position."""
    upper, mid, lower = _starc(high, low, close, n=15, mult=2.0)
    return _band_position(close, upper, lower).diff().diff().diff()

def f16_dbkb_033_keltner_upper_break_then_close_below_mid_within_5_d3(high, low, close):
    """Indicator: ≥1 Keltner upper break in last 5d AND today close < Keltner mid (rapid reversal)."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    br = ((close > upper) & upper.notna()).astype(float)
    recent = br.rolling(WDAYS, min_periods=1).sum().fillna(0) > 0
    return (recent & (close < mid)).astype(float).where(mid.notna(), np.nan).diff().diff().diff()

def f16_dbkb_034_bollinger_upper_break_failure_rate_252d_d3(close):
    """In 252d: count of (upper-break then close<mid within 5 bars) divided by count of upper-breaks."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    br = ((close > upper) & upper.notna()).astype(int)
    below_mid_in_5 = (close < mid).astype(int).rolling(WDAYS, min_periods=1).sum().shift(WDAYS - 1).fillna(0)
    past_break = br.shift(WDAYS).fillna(0)
    closed_below_since = (close < mid).rolling(WDAYS, min_periods=1).max().fillna(0)
    fail = (past_break * closed_below_since).rolling(YDAYS, min_periods=QDAYS).sum()
    breaks = br.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(fail, breaks).diff().diff().diff()

def f16_dbkb_035_keltner_break_then_recover_count_252d_d3(high, low, close):
    """Count of bars in 252d where (close > Keltner upper) AND (close < Keltner upper within 5 prior bars)."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    above = ((close > upper) & upper.notna()).astype(int)
    recent_below = ((close < upper) & upper.notna()).astype(int).rolling(WDAYS, min_periods=1).sum().shift(1).fillna(0)
    whip = ((above == 1) & (recent_below > 0)).astype(float)
    return whip.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f16_dbkb_036_donchian_upper_break_then_close_below_within_3_d3(high, low, close):
    """Bars in 252d where high>=Donchian(20)-upper but close<Donchian(20)-upper (intraday-only break)."""
    u, l = _donchian(high, low, 20)
    fb = ((high >= u) & (close < u)).astype(float).where(u.notna(), np.nan)
    return fb.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f16_dbkb_037_max_failed_bollinger_break_extension_252d_d3(close):
    """Max log-extension (close − upper)/upper of failed Bollinger upper-breaks (close<mid within 5d) in 252d."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    ext = _safe_div(close - upper, upper).where(close > upper, np.nan)
    past_break = ((close > upper) & upper.notna()).shift(WDAYS).fillna(False)
    closed_below_since = (close < mid).rolling(WDAYS, min_periods=1).max().fillna(0) > 0
    failed_ext = ext.shift(WDAYS).where(past_break & closed_below_since)
    return failed_ext.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f16_dbkb_038_bollinger_upper_break_then_fail_count_504d_d3(close):
    """In 504d: count of (Bollinger upper-break followed by close<mid within 5d)."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    past_break = ((close > upper) & upper.notna()).shift(WDAYS).fillna(False)
    closed_below_since = (close < mid).rolling(WDAYS, min_periods=1).max().fillna(0) > 0
    fail = (past_break & closed_below_since).astype(float)
    return fail.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f16_dbkb_039_acceleration_bands_width_20_norm_mid_d3(high, low, close):
    """Headley Acceleration Bands(20) width / mid — H×(1+factor·ratio)−L×(1−factor·ratio), distinct vol-band geometry."""
    upper, mid, lower = _acceleration_bands(high, low, close, n=20, factor=2.0)
    return _band_width_rel(upper, lower, mid).diff().diff().diff()

def f16_dbkb_040_standard_error_bands_width_63_2_norm_close_d3(close):
    """Standard Error Bands(63d, k=2) width ÷ close — regression-residual band width (distinct from BB std and Keltner ATR)."""
    upper, mid, lower = _standard_error_bands(close, n=QDAYS, k=2.0)
    return _safe_div(upper - lower, close).diff().diff().diff()

def f16_dbkb_041_ratio_bollinger_failed_breaks_to_total_252d_d3(close):
    """Same as 034 but with 21-bar failure window — different timescale concept."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    br = ((close > upper) & upper.notna()).astype(int)
    past_break = br.shift(MDAYS).fillna(0)
    closed_below_since = (close < mid).rolling(MDAYS, min_periods=1).max().fillna(0)
    fail = (past_break * closed_below_since).rolling(YDAYS, min_periods=QDAYS).sum()
    breaks = br.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(fail, breaks).diff().diff().diff()

def f16_dbkb_042_donchian_55_break_failure_count_252d_d3(high, low, close):
    """Count of Donchian(55)-upper break-failures (high>=upper but close<midline) in 252d."""
    u, l = _donchian(high, low, 55)
    midline = (u + l) / 2.0
    fb = ((high >= u) & (close < midline)).astype(float).where(u.notna() & midline.notna(), np.nan)
    return fb.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f16_dbkb_043_max_failed_break_extension_keltner_252d_d3(high, low, close):
    """Max ATR-normalized extension above Keltner upper for failed-breaks (close<mid within 5d) in 252d."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    atr = _atr(high, low, close, n=MDAYS)
    ext = _safe_div(close - upper, atr).where(close > upper, np.nan)
    past_break = ((close > upper) & upper.notna()).shift(WDAYS).fillna(False)
    closed_below_since = (close < mid).rolling(WDAYS, min_periods=1).max().fillna(0) > 0
    failed_ext = ext.shift(WDAYS).where(past_break & closed_below_since)
    return failed_ext.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f16_dbkb_044_indicator_recent_failed_bollinger_break_d3(close):
    """Indicator: any failed Bollinger upper-break occurred in the trailing 21d."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    past_break = ((close > upper) & upper.notna()).shift(WDAYS).fillna(False)
    closed_below_since = (close < mid).rolling(WDAYS, min_periods=1).max().fillna(0) > 0
    fail = (past_break & closed_below_since).astype(float)
    return (fail.rolling(MDAYS, min_periods=1).sum() > 0).astype(float).diff().diff().diff()

def f16_dbkb_045_frac_close_above_bollinger_upper_21d_d3(close):
    """Fraction of bars in 21d where close > Bollinger(20,2) upper — walking the upper band."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    above = ((close > upper) & upper.notna()).astype(float)
    return above.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f16_dbkb_046_frac_close_within_half_sigma_keltner_upper_63d_d3(high, low, close):
    """Fraction of bars in 63d where close within 0.5 × ATR of Keltner upper — hugging upper Keltner."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    atr = _atr(high, low, close, n=MDAYS)
    near = ((upper - close).abs() < 0.5 * atr).astype(float).where(upper.notna() & atr.notna(), np.nan)
    return near.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f16_dbkb_047_consec_bars_above_donchian_55_upper_d3(high, low, close):
    """Current consecutive-bar streak where high >= Donchian(55) upper (sustained range-top hugging)."""
    u, l = _donchian(high, low, 55)
    return _streak_true((high >= u) & u.notna()).diff().diff().diff()

def f16_dbkb_048_indicator_walking_upper_band_then_fail_d3(close):
    """Indicator: ≥3-of-last-5 bars closed above Bollinger upper AND today close < mid (walk-then-fail)."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    above = ((close > upper) & upper.notna()).astype(int)
    walk = above.rolling(WDAYS, min_periods=WDAYS).sum() >= 3
    return (walk.shift(1).fillna(False) & (close < mid) & mid.notna()).astype(float).diff().diff().diff()

def f16_dbkb_049_frac_above_keltner_upper_21d_d3(high, low, close):
    """Fraction of bars in 21d where close > Keltner upper."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    return ((close > upper) & upper.notna()).astype(float).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f16_dbkb_050_consec_bars_close_above_bollinger_mid_d3(close):
    """Current consecutive-bar streak where close > Bollinger(20,2) mid (sustained over-midline)."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _streak_true((close > mid) & mid.notna()).diff().diff().diff()

def f16_dbkb_051_longest_streak_above_bollinger_upper_252d_d3(close):
    """Longest consecutive-bar streak in 252d where close > Bollinger(20,2) upper."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    above = ((close > upper) & upper.notna()).astype(float)

    def _longest(w):
        run = best = 0
        for v in w:
            if v > 0:
                run += 1
                if run > best:
                    best = run
            else:
                run = 0
        return float(best)
    return above.rolling(YDAYS, min_periods=QDAYS).apply(_longest, raw=True).diff().diff().diff()

def f16_dbkb_052_dwell_time_above_keltner_upper_63d_d3(high, low, close):
    """Fraction of bars in 63d where close > Keltner upper — dwell time in extended-zone."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    return ((close > upper) & upper.notna()).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f16_dbkb_053_persistence_5of5_above_donchian_20_upper_d3(high, low, close):
    """Indicator: 5-of-last-5 bars printed Donchian(20) upper-touch (high>=upper)."""
    u, l = _donchian(high, low, 20)
    touch = ((high >= u) & u.notna()).astype(int)
    return (touch.rolling(WDAYS, min_periods=WDAYS).sum() == WDAYS).astype(float).where(u.notna(), np.nan).diff().diff().diff()

def f16_dbkb_054_indicator_close_above_all_three_upper_bands_d3(high, low, close):
    """Indicator: close > all of (Bollinger upper, Keltner upper, Donchian(20) upper)."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    return ((close > bu) & (close > ku) & (close > du)).astype(float).diff().diff().diff()

def f16_dbkb_055_ttm_squeeze_indicator_d3(high, low, close):
    """TTM Squeeze: Bollinger(20,2) inside Keltner(20,10,1.5)."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    return ((bu < ku) & (bl > kl)).astype(float).where(bu.notna() & ku.notna(), np.nan).diff().diff().diff()

def f16_dbkb_056_ttm_squeeze_duration_d3(high, low, close):
    """Current consecutive-bar duration of TTM squeeze state."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(bool)
    return _streak_true(sq).diff().diff().diff()

def f16_dbkb_057_bars_since_ttm_squeeze_release_d3(high, low, close):
    """Bars since most recent TTM-squeeze release (sq=True → False transition)."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    return _bars_since_true(release).diff().diff().diff()

def f16_dbkb_058_ratio_bollinger_to_keltner_width_d3(high, low, close):
    """Bollinger(20,2) width / Keltner(20,10,2) width — TTM-style ratio (<1 = squeeze)."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    return _safe_div(bu - bl, ku - kl).diff().diff().diff()

def f16_dbkb_059_squeeze_then_expansion_velocity_d3(high, low, close):
    """If bars-since-release ≤ 10: (Bollinger width − width-at-release) / 10 (post-release expansion rate)."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    bsr = _bars_since_true(release)
    bw = bu - bl
    bw_at_release = bw.shift(bsr.fillna(0).astype(int).clip(upper=1260)) if False else None
    bw_v = bw.values
    bs = bsr.values
    n = len(bs)
    out = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(bs[i]) or bs[i] > 10:
            continue
        j = i - int(bs[i])
        if 0 <= j < n and (not np.isnan(bw_v[i])) and (not np.isnan(bw_v[j])):
            out[i] = (bw_v[i] - bw_v[j]) / 10.0
    return pd.Series(out, index=close.index).diff().diff().diff()

def f16_dbkb_060_squeeze_state_persistence_252d_d3(high, low, close):
    """Fraction of bars in 252d in TTM-squeeze state."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    return ((bu < ku) & (bl > kl)).astype(float).where(bu.notna() & ku.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f16_dbkb_061_squeeze_count_252d_d3(high, low, close):
    """Count of distinct TTM-squeeze episodes (entries) in trailing 252d."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    enter = ((sq.shift(1).fillna(0) == 0) & (sq == 1)).astype(float)
    return enter.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f16_dbkb_062_bollinger_band_squeeze_p10_indicator_d3(close):
    """Indicator: Bollinger(20,2) width ≤ 10th-pct of trailing 252d distribution — deep squeeze."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    w = _band_width_rel(upper, lower, mid)
    p10 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    return (w <= p10).astype(float).where(p10.notna(), np.nan).diff().diff().diff()

def f16_dbkb_063_keltner_band_squeeze_p10_indicator_d3(high, low, close):
    """Indicator: Keltner(20,10,2) width ≤ 10th-pct of trailing 252d distribution."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    w = _band_width_rel(upper, lower, mid)
    p10 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    return (w <= p10).astype(float).where(p10.notna(), np.nan).diff().diff().diff()

def f16_dbkb_064_donchian_compression_ratio_20_to_252_d3(high, low, close):
    """Donchian(20) width / Donchian(252) width — short-range compression vs annual range."""
    u20, l20 = _donchian(high, low, 20)
    u252, l252 = _donchian(high, low, YDAYS)
    return _safe_div(u20 - l20, u252 - l252).diff().diff().diff()

def f16_dbkb_065_post_squeeze_direction_sign_close_minus_mid_d3(high, low, close):
    """Sign of (close − Bollinger mid) on the bar of TTM-squeeze release — initial post-release direction."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    sign = np.sign(close - bm).astype(float)
    return sign.where(release, np.nan).diff().diff().diff()

def f16_dbkb_066_post_squeeze_5d_atr_move_magnitude_d3(high, low, close):
    """ATR-normalized 5-bar log return measured 5 bars after most recent TTM-squeeze release."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    bsr = _bars_since_true(release)
    atr = _atr(high, low, close, n=MDAYS)
    arr = close.values
    bs = bsr.values
    av = atr.values
    n = len(arr)
    out = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(bs[i]) or bs[i] < 5 or bs[i] > 100:
            continue
        anchor = i - int(bs[i])
        if anchor + 5 >= n:
            continue
        j = anchor + 5
        if j >= n or np.isnan(arr[j]) or np.isnan(arr[anchor]) or (arr[j] <= 0) or (arr[anchor] <= 0) or np.isnan(av[i]):
            continue
        r = arr[j] - arr[anchor]
        if av[i] != 0:
            out[i] = r / av[i]
    return pd.Series(out, index=close.index).diff().diff().diff()

def f16_dbkb_067_post_release_upper_break_count_in_21d_d3(high, low, close):
    """Count of Bollinger upper-breaks in 21 bars following the most recent TTM-squeeze release."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    bsr = _bars_since_true(release)
    br = ((close > bu) & bu.notna()).astype(int)
    bs = bsr.values
    bv = br.values
    n = len(bs)
    out = np.full(n, np.nan)
    cur_sum = 0
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]) and bs[i] <= MDAYS:
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_sum = 0
            cur_sum += int(bv[i])
            out[i] = float(cur_sum)
    return pd.Series(out, index=close.index).diff().diff().diff()

def f16_dbkb_068_post_release_lower_break_count_in_21d_d3(close):
    """Count of Bollinger lower-breaks in 21 bars following most recent TTM-squeeze release."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    w = _band_width_rel(bu, bl, bm)
    p10 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    squeezed = (w <= p10).astype(int)
    release = ((squeezed.shift(1) == 1) & (squeezed == 0)).astype(bool)
    bsr = _bars_since_true(release)
    br = ((close < bl) & bl.notna()).astype(int)
    bs = bsr.values
    bv = br.values
    n = len(bs)
    out = np.full(n, np.nan)
    cur_sum = 0
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]) and bs[i] <= MDAYS:
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_sum = 0
            cur_sum += int(bv[i])
            out[i] = float(cur_sum)
    return pd.Series(out, index=close.index).diff().diff().diff()

def f16_dbkb_069_acceleration_bands_upper_break_count_21d_d3(high, low, close):
    """Count of bars in 21d where close > Acceleration Bands(20) upper — Headley trend-acceleration signal."""
    upper, mid, lower = _acceleration_bands(high, low, close, n=20, factor=2.0)
    br = (close > upper).astype(float).where(upper.notna(), np.nan)
    return br.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f16_dbkb_070_log_return_first_21d_after_squeeze_release_d3(high, low, close):
    """Log close return measured 21 bars after most recent TTM-squeeze release (cumulative since anchor)."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    bsr = _bars_since_true(release)
    arr = close.values
    bs = bsr.values
    n = len(arr)
    out = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(bs[i]) or bs[i] > MDAYS:
            continue
        anchor = i - int(bs[i])
        if 0 <= anchor < n and arr[anchor] > 0 and (arr[i] > 0):
            out[i] = np.log(arr[i]) - np.log(arr[anchor])
    return pd.Series(out, index=close.index).diff().diff().diff()

def f16_dbkb_071_post_release_max_drawdown_21d_d3(high, low, close):
    """Max drawdown of low vs close-at-release within 21 bars after most recent TTM-squeeze release."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    bsr = _bars_since_true(release)
    arr_c = close.values
    arr_l = low.values
    bs = bsr.values
    n = len(arr_c)
    out = np.full(n, np.nan)
    cur_min_logret = np.nan
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]) and bs[i] <= MDAYS:
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_min_logret = np.nan
            if 0 <= anchor < n and arr_c[anchor] > 0 and (arr_l[i] > 0):
                r = np.log(arr_l[i]) - np.log(arr_c[anchor])
                cur_min_logret = r if np.isnan(cur_min_logret) else min(cur_min_logret, r)
            out[i] = cur_min_logret
    return pd.Series(out, index=close.index).diff().diff().diff()

def f16_dbkb_072_post_release_volume_avg_norm_63d_d3(high, low, close, volume):
    """Mean volume in post-release window (≤21d), normalized by 63d-rolling-avg volume."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    bsr = _bars_since_true(release)
    vavg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    bs = bsr.values
    v = volume.values
    va = vavg.values
    n = len(v)
    out = np.full(n, np.nan)
    cur_sum = 0.0
    cur_n = 0
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]) and bs[i] <= MDAYS:
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_sum = 0.0
                cur_n = 0
            if not np.isnan(v[i]):
                cur_sum += v[i]
                cur_n += 1
            if cur_n > 0 and (not np.isnan(va[i])) and (va[i] > 0):
                out[i] = cur_sum / cur_n / va[i]
    return pd.Series(out, index=close.index).diff().diff().diff()

def f16_dbkb_073_consecutive_failed_squeezes_count_252d_d3(high, low, close):
    """Count of squeezes where post-release return at +21d was negative — 'failed squeezes' in 252d."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    arr = close.values
    rel = release.values
    n = len(arr)
    failed = np.zeros(n, dtype=float)
    for i in range(n - MDAYS):
        if rel[i] and arr[i] > 0 and (arr[i + MDAYS] > 0):
            if arr[i + MDAYS] < arr[i]:
                failed[i + MDAYS] = 1.0
    return pd.Series(failed, index=close.index).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f16_dbkb_074_post_release_atr_normalized_range_21d_d3(high, low, close):
    """Realized H−L range over 21d after most recent release / ATR(21) — expansion-magnitude indicator."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    bsr = _bars_since_true(release)
    atr = _atr(high, low, close, n=MDAYS)
    arr_h = high.values
    arr_l = low.values
    bs = bsr.values
    av = atr.values
    n = len(arr_h)
    out = np.full(n, np.nan)
    cur_hi = np.nan
    cur_lo = np.nan
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]) and bs[i] <= MDAYS:
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_hi = np.nan
                cur_lo = np.nan
            if not np.isnan(arr_h[i]):
                cur_hi = arr_h[i] if np.isnan(cur_hi) else max(cur_hi, arr_h[i])
            if not np.isnan(arr_l[i]):
                cur_lo = arr_l[i] if np.isnan(cur_lo) else min(cur_lo, arr_l[i])
            if not (np.isnan(cur_hi) or np.isnan(cur_lo) or np.isnan(av[i]) or (av[i] == 0)):
                out[i] = (cur_hi - cur_lo) / av[i]
    return pd.Series(out, index=close.index).diff().diff().diff()

def f16_dbkb_075_indicator_post_release_break_failure_d3(high, low, close):
    """Indicator: a Bollinger upper-break-then-fail (close<mid within 5d) occurred within 21d of most recent TTM-release."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(bool)
    bsr = _bars_since_true(release)
    past_break = ((close > bu) & bu.notna()).shift(WDAYS).fillna(False)
    closed_below_since = (close < bm).rolling(WDAYS, min_periods=1).max().fillna(0) > 0
    fail = (past_break & closed_below_since).astype(int)
    bs = bsr.values
    fv = fail.values
    n = len(bs)
    out = np.full(n, np.nan)
    cur_any = 0
    last_anchor = -1
    for i in range(n):
        if not np.isnan(bs[i]) and bs[i] <= MDAYS:
            anchor = i - int(bs[i])
            if anchor != last_anchor:
                last_anchor = anchor
                cur_any = 0
            if fv[i]:
                cur_any = 1
            out[i] = float(cur_any)
    return pd.Series(out, index=close.index).diff().diff().diff()
DONCHIAN_BOLLINGER_KELTNER_BANDS_D3_REGISTRY_001_075 = {'f16_dbkb_001_bollinger_width_20_2_norm_mid_d3': {'inputs': ['close'], 'func': f16_dbkb_001_bollinger_width_20_2_norm_mid_d3}, 'f16_dbkb_002_keltner_width_20_10_2_norm_mid_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_002_keltner_width_20_10_2_norm_mid_d3}, 'f16_dbkb_003_donchian_width_20_norm_mid_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_003_donchian_width_20_norm_mid_d3}, 'f16_dbkb_004_donchian_width_55_norm_mid_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_004_donchian_width_55_norm_mid_d3}, 'f16_dbkb_005_bollinger_width_20_2_zscore_252d_d3': {'inputs': ['close'], 'func': f16_dbkb_005_bollinger_width_20_2_zscore_252d_d3}, 'f16_dbkb_006_pctile_rank_bollinger_width_20_in_252d_d3': {'inputs': ['close'], 'func': f16_dbkb_006_pctile_rank_bollinger_width_20_in_252d_d3}, 'f16_dbkb_007_pctile_rank_keltner_width_20_in_504d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_007_pctile_rank_keltner_width_20_in_504d_d3}, 'f16_dbkb_008_bollinger_width_expansion_rate_vs_63d_baseline_d3': {'inputs': ['close'], 'func': f16_dbkb_008_bollinger_width_expansion_rate_vs_63d_baseline_d3}, 'f16_dbkb_009_zscore_bollinger_width_20_in_252d_d3': {'inputs': ['close'], 'func': f16_dbkb_009_zscore_bollinger_width_20_in_252d_d3}, 'f16_dbkb_010_ratio_bollinger_width_20_to_252d_median_d3': {'inputs': ['close'], 'func': f16_dbkb_010_ratio_bollinger_width_20_to_252d_median_d3}, 'f16_dbkb_011_starc_width_15_2_norm_mid_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_011_starc_width_15_2_norm_mid_d3}, 'f16_dbkb_012_diff_bollinger_width_now_minus_63d_ago_d3': {'inputs': ['close'], 'func': f16_dbkb_012_diff_bollinger_width_now_minus_63d_ago_d3}, 'f16_dbkb_013_atr_norm_donchian_width_20_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_013_atr_norm_donchian_width_20_d3}, 'f16_dbkb_014_donchian_20_midline_distance_norm_close_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_014_donchian_20_midline_distance_norm_close_d3}, 'f16_dbkb_015_bollinger_pct_b_20_2_d3': {'inputs': ['close'], 'func': f16_dbkb_015_bollinger_pct_b_20_2_d3}, 'f16_dbkb_016_keltner_pct_position_20_10_2_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_016_keltner_pct_position_20_10_2_d3}, 'f16_dbkb_017_donchian_pct_position_20_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_017_donchian_pct_position_20_d3}, 'f16_dbkb_018_donchian_pct_position_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_018_donchian_pct_position_252_d3}, 'f16_dbkb_019_zscore_bollinger_pct_b_in_63d_d3': {'inputs': ['close'], 'func': f16_dbkb_019_zscore_bollinger_pct_b_in_63d_d3}, 'f16_dbkb_020_consensus_position_avg_3systems_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_020_consensus_position_avg_3systems_d3}, 'f16_dbkb_021_bollinger_pct_b_in_top_decile_d3': {'inputs': ['close'], 'func': f16_dbkb_021_bollinger_pct_b_in_top_decile_d3}, 'f16_dbkb_022_bbw_to_atr_ratio_20_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_022_bbw_to_atr_ratio_20_d3}, 'f16_dbkb_023_pctile_rank_donchian_pct_position_252_in_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_023_pctile_rank_donchian_pct_position_252_in_252d_d3}, 'f16_dbkb_024_bollinger_upper_break_count_21d_d3': {'inputs': ['close'], 'func': f16_dbkb_024_bollinger_upper_break_count_21d_d3}, 'f16_dbkb_025_bollinger_upper_break_count_63d_d3': {'inputs': ['close'], 'func': f16_dbkb_025_bollinger_upper_break_count_63d_d3}, 'f16_dbkb_026_keltner_upper_break_count_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_026_keltner_upper_break_count_63d_d3}, 'f16_dbkb_027_donchian_upper_break_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_027_donchian_upper_break_count_252d_d3}, 'f16_dbkb_028_indicator_first_bollinger_upper_break_in_21d_d3': {'inputs': ['close'], 'func': f16_dbkb_028_indicator_first_bollinger_upper_break_in_21d_d3}, 'f16_dbkb_029_bars_since_last_bollinger_upper_break_d3': {'inputs': ['close'], 'func': f16_dbkb_029_bars_since_last_bollinger_upper_break_d3}, 'f16_dbkb_030_bollinger_lower_break_count_63d_d3': {'inputs': ['close'], 'func': f16_dbkb_030_bollinger_lower_break_count_63d_d3}, 'f16_dbkb_031_donchian_upper_break_252d_count_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_031_donchian_upper_break_252d_count_d3}, 'f16_dbkb_032_starc_pct_position_15_2_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_032_starc_pct_position_15_2_d3}, 'f16_dbkb_033_keltner_upper_break_then_close_below_mid_within_5_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_033_keltner_upper_break_then_close_below_mid_within_5_d3}, 'f16_dbkb_034_bollinger_upper_break_failure_rate_252d_d3': {'inputs': ['close'], 'func': f16_dbkb_034_bollinger_upper_break_failure_rate_252d_d3}, 'f16_dbkb_035_keltner_break_then_recover_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_035_keltner_break_then_recover_count_252d_d3}, 'f16_dbkb_036_donchian_upper_break_then_close_below_within_3_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_036_donchian_upper_break_then_close_below_within_3_d3}, 'f16_dbkb_037_max_failed_bollinger_break_extension_252d_d3': {'inputs': ['close'], 'func': f16_dbkb_037_max_failed_bollinger_break_extension_252d_d3}, 'f16_dbkb_038_bollinger_upper_break_then_fail_count_504d_d3': {'inputs': ['close'], 'func': f16_dbkb_038_bollinger_upper_break_then_fail_count_504d_d3}, 'f16_dbkb_039_acceleration_bands_width_20_norm_mid_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_039_acceleration_bands_width_20_norm_mid_d3}, 'f16_dbkb_040_standard_error_bands_width_63_2_norm_close_d3': {'inputs': ['close'], 'func': f16_dbkb_040_standard_error_bands_width_63_2_norm_close_d3}, 'f16_dbkb_041_ratio_bollinger_failed_breaks_to_total_252d_d3': {'inputs': ['close'], 'func': f16_dbkb_041_ratio_bollinger_failed_breaks_to_total_252d_d3}, 'f16_dbkb_042_donchian_55_break_failure_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_042_donchian_55_break_failure_count_252d_d3}, 'f16_dbkb_043_max_failed_break_extension_keltner_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_043_max_failed_break_extension_keltner_252d_d3}, 'f16_dbkb_044_indicator_recent_failed_bollinger_break_d3': {'inputs': ['close'], 'func': f16_dbkb_044_indicator_recent_failed_bollinger_break_d3}, 'f16_dbkb_045_frac_close_above_bollinger_upper_21d_d3': {'inputs': ['close'], 'func': f16_dbkb_045_frac_close_above_bollinger_upper_21d_d3}, 'f16_dbkb_046_frac_close_within_half_sigma_keltner_upper_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_046_frac_close_within_half_sigma_keltner_upper_63d_d3}, 'f16_dbkb_047_consec_bars_above_donchian_55_upper_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_047_consec_bars_above_donchian_55_upper_d3}, 'f16_dbkb_048_indicator_walking_upper_band_then_fail_d3': {'inputs': ['close'], 'func': f16_dbkb_048_indicator_walking_upper_band_then_fail_d3}, 'f16_dbkb_049_frac_above_keltner_upper_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_049_frac_above_keltner_upper_21d_d3}, 'f16_dbkb_050_consec_bars_close_above_bollinger_mid_d3': {'inputs': ['close'], 'func': f16_dbkb_050_consec_bars_close_above_bollinger_mid_d3}, 'f16_dbkb_051_longest_streak_above_bollinger_upper_252d_d3': {'inputs': ['close'], 'func': f16_dbkb_051_longest_streak_above_bollinger_upper_252d_d3}, 'f16_dbkb_052_dwell_time_above_keltner_upper_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_052_dwell_time_above_keltner_upper_63d_d3}, 'f16_dbkb_053_persistence_5of5_above_donchian_20_upper_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_053_persistence_5of5_above_donchian_20_upper_d3}, 'f16_dbkb_054_indicator_close_above_all_three_upper_bands_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_054_indicator_close_above_all_three_upper_bands_d3}, 'f16_dbkb_055_ttm_squeeze_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_055_ttm_squeeze_indicator_d3}, 'f16_dbkb_056_ttm_squeeze_duration_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_056_ttm_squeeze_duration_d3}, 'f16_dbkb_057_bars_since_ttm_squeeze_release_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_057_bars_since_ttm_squeeze_release_d3}, 'f16_dbkb_058_ratio_bollinger_to_keltner_width_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_058_ratio_bollinger_to_keltner_width_d3}, 'f16_dbkb_059_squeeze_then_expansion_velocity_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_059_squeeze_then_expansion_velocity_d3}, 'f16_dbkb_060_squeeze_state_persistence_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_060_squeeze_state_persistence_252d_d3}, 'f16_dbkb_061_squeeze_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_061_squeeze_count_252d_d3}, 'f16_dbkb_062_bollinger_band_squeeze_p10_indicator_d3': {'inputs': ['close'], 'func': f16_dbkb_062_bollinger_band_squeeze_p10_indicator_d3}, 'f16_dbkb_063_keltner_band_squeeze_p10_indicator_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_063_keltner_band_squeeze_p10_indicator_d3}, 'f16_dbkb_064_donchian_compression_ratio_20_to_252_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_064_donchian_compression_ratio_20_to_252_d3}, 'f16_dbkb_065_post_squeeze_direction_sign_close_minus_mid_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_065_post_squeeze_direction_sign_close_minus_mid_d3}, 'f16_dbkb_066_post_squeeze_5d_atr_move_magnitude_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_066_post_squeeze_5d_atr_move_magnitude_d3}, 'f16_dbkb_067_post_release_upper_break_count_in_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_067_post_release_upper_break_count_in_21d_d3}, 'f16_dbkb_068_post_release_lower_break_count_in_21d_d3': {'inputs': ['close'], 'func': f16_dbkb_068_post_release_lower_break_count_in_21d_d3}, 'f16_dbkb_069_acceleration_bands_upper_break_count_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_069_acceleration_bands_upper_break_count_21d_d3}, 'f16_dbkb_070_log_return_first_21d_after_squeeze_release_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_070_log_return_first_21d_after_squeeze_release_d3}, 'f16_dbkb_071_post_release_max_drawdown_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_071_post_release_max_drawdown_21d_d3}, 'f16_dbkb_072_post_release_volume_avg_norm_63d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f16_dbkb_072_post_release_volume_avg_norm_63d_d3}, 'f16_dbkb_073_consecutive_failed_squeezes_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_073_consecutive_failed_squeezes_count_252d_d3}, 'f16_dbkb_074_post_release_atr_normalized_range_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_074_post_release_atr_normalized_range_21d_d3}, 'f16_dbkb_075_indicator_post_release_break_failure_d3': {'inputs': ['high', 'low', 'close'], 'func': f16_dbkb_075_indicator_post_release_break_failure_d3}}