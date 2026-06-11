"""37_range_estimators_family d1 features 226-300 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _wilder_smooth(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()

def _dm_components(high: pd.Series, low: pd.Series):
    up_move = high.diff()
    down_move = -low.diff()
    plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0.0)
    minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0.0)
    return (pd.Series(plus_dm, index=high.index), pd.Series(minus_dm, index=high.index))

def _adx(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    pdm, mdm = _dm_components(high, low)
    tr = _true_range(high, low, close)
    pdi = 100.0 * _safe_div(_wilder_smooth(pdm, n), _wilder_smooth(tr, n))
    mdi = 100.0 * _safe_div(_wilder_smooth(mdm, n), _wilder_smooth(tr, n))
    dx = 100.0 * _safe_div((pdi - mdi).abs(), pdi + mdi)
    return _wilder_smooth(dx, n)

def _vortex(high: pd.Series, low: pd.Series, close: pd.Series, n: int):
    vmp = (high - low.shift(1)).abs()
    vmn = (low - high.shift(1)).abs()
    tr = _true_range(high, low, close)
    vip = _safe_div(vmp.rolling(n, min_periods=max(n // 2, 2)).sum(), tr.rolling(n, min_periods=max(n // 2, 2)).sum())
    vin = _safe_div(vmn.rolling(n, min_periods=max(n // 2, 2)).sum(), tr.rolling(n, min_periods=max(n // 2, 2)).sum())
    return (vip, vin)

def _rwi_high(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    atr = _atr(high, low, close, n=n)
    return _safe_div(high - low.shift(n), atr * np.sqrt(float(n)))

def _rwi_low(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    atr = _atr(high, low, close, n=n)
    return _safe_div(high.shift(n) - low, atr * np.sqrt(float(n)))

def _wvf(close: pd.Series, low: pd.Series, n: int=22) -> pd.Series:
    rmax = close.rolling(n, min_periods=max(n // 2, 2)).max()
    return _safe_div(rmax - low, rmax) * 100.0

def _bb_kc_squeeze(close: pd.Series, high: pd.Series, low: pd.Series, n: int=20, bb_k: float=2.0, kc_k: float=1.5) -> pd.Series:
    m = close.rolling(n, min_periods=max(n // 2, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 2, 2)).std()
    bb_up = m + bb_k * sd
    bb_dn = m - bb_k * sd
    atr = _atr(high, low, close, n=n)
    kc_up = m + kc_k * atr
    kc_dn = m - kc_k * atr
    return ((bb_up < kc_up) & (bb_dn > kc_dn)).astype(float).where(bb_up.notna() & kc_up.notna(), np.nan)

def _cusum_max_abs(s: pd.Series, n: int, mp: int) -> pd.Series:

    def _cm(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        c = np.cumsum(v - v.mean())
        return float(np.max(np.abs(c)))
    return s.rolling(n, min_periods=mp).apply(_cm, raw=True)

def _ttm_dur_series(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sq = _bb_kc_squeeze(close, high, low, 20, 2.0, 1.5).values
    n = len(sq)
    out = np.full(n, np.nan)
    streak = 0
    for i in range(n):
        if np.isnan(sq[i]):
            out[i] = np.nan
            streak = 0
        else:
            streak = streak + 1 if sq[i] == 1.0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=close.index)

def f37_rges_226_adx_14d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder smoothed ADX(14) — canonical trend-strength indicator. >25 = trending."""
    return _adx(high, low, close, 14).diff()

def f37_rges_227_adx_28d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wilder smoothed ADX(28) — longer-horizon trend strength."""
    return _adx(high, low, close, 28).diff()

def f37_rges_228_adx_above_25_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADX(14) > 25 — trending-regime flag (Wilder's classic threshold)."""
    a = _adx(high, low, close, 14)
    return (a > 25.0).astype(float).where(a.notna(), np.nan).diff()

def f37_rges_229_adx_rising_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADX(14) - ADX(14)_{t-5} > 0 — trend strength accelerating."""
    a = _adx(high, low, close, 14)
    return (a - a.shift(WDAYS) > 0).astype(float).where(a.notna() & a.shift(WDAYS).notna(), np.nan).diff()

def f37_rges_230_adx_zscore_in_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of ADX(14) in trailing 252d distribution — extremity of current trend strength."""
    a = _adx(high, low, close, 14)
    return _rolling_zscore(a, YDAYS, min_periods=QDAYS).diff()

def f37_rges_231_adx_slope_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of ADX(14) — direction & magnitude of trend-strength change."""
    a = _adx(high, low, close, 14)
    return _rolling_slope(a, MDAYS).diff()

def f37_rges_232_vortex_plus_14d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex Indicator VI+(14) — positive-trend strength via (H_t - L_{t-1}) ratios."""
    vip, _ = _vortex(high, low, close, 14)
    return vip.diff()

def f37_rges_233_vortex_minus_14d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Vortex Indicator VI-(14) — negative-trend strength via (L_t - H_{t-1}) ratios."""
    _, vin = _vortex(high, low, close, 14)
    return vin.diff()

def f37_rges_234_vortex_diff_14d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(14) - VI-(14) — directional Vortex bias; >0 = up-trend, <0 = down-trend."""
    vip, vin = _vortex(high, low, close, 14)
    return (vip - vin).diff()

def f37_rges_235_vortex_diff_28d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(28) - VI-(28) — longer-horizon directional Vortex bias."""
    vip, vin = _vortex(high, low, close, 28)
    return (vip - vin).diff()

def f37_rges_236_vortex_crossover_down_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: VI+(14) crossed BELOW VI-(14) today (bearish Vortex crossover)."""
    vip, vin = _vortex(high, low, close, 14)
    today_below = vip < vin
    prev_above = vip.shift(1) >= vin.shift(1)
    return (today_below & prev_above).astype(float).where(vip.notna() & vin.notna(), np.nan).diff()

def f37_rges_237_vortex_minus_above_plus_streak_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where VI-(14) > VI+(14) — sustained bearish-Vortex state."""
    vip, vin = _vortex(high, low, close, 14)
    flag = (vin > vip).values
    n = len(flag)
    out = np.full(n, np.nan)
    streak = 0
    for i in range(n):
        if np.isnan(vip.iat[i]) or np.isnan(vin.iat[i]):
            out[i] = np.nan
            streak = 0
        else:
            streak = streak + 1 if flag[i] else 0
            out[i] = float(streak)
    return pd.Series(out, index=high.index).diff()

def f37_rges_238_rwi_high_14d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Random Walk Index High(14) — strength of upward move relative to random walk; >1 indicates uptrend."""
    return _rwi_high(high, low, close, 14).diff()

def f37_rges_239_rwi_low_14d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Random Walk Index Low(14) — strength of downward move; >1 indicates downtrend."""
    return _rwi_low(high, low, close, 14).diff()

def f37_rges_240_rwi_diff_14d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RWI_High(14) - RWI_Low(14) — directional RWI bias."""
    return (_rwi_high(high, low, close, 14) - _rwi_low(high, low, close, 14)).diff()

def f37_rges_241_rwi_high_28d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RWI_High(28) — monthly-horizon up-trend strength."""
    return _rwi_high(high, low, close, 28).diff()

def f37_rges_242_rwi_max_14d_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: max(RWI_High(14), RWI_Low(14)) > 1 — non-random-walk regime active."""
    hi = _rwi_high(high, low, close, 14)
    lo = _rwi_low(high, low, close, 14)
    return (pd.concat([hi, lo], axis=1).max(axis=1) > 1.0).astype(float).where(hi.notna() & lo.notna(), np.nan).diff()

def f37_rges_243_wvf_22d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """Williams VIX Fix (22d): (max(C)_22 - L) / max(C)_22 * 100 — VIX-like fear gauge from price only."""
    return _wvf(close, low, 22).diff()

def f37_rges_244_wvf_zscore_in_252d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of WVF(22) in 252d distribution — current fear-gauge extremity."""
    w = _wvf(close, low, 22)
    return _rolling_zscore(w, YDAYS, min_periods=QDAYS).diff()

def f37_rges_245_wvf_percentile_rank_252d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of WVF(22) in trailing 252d — bounded fear-gauge regime measure."""
    w = _wvf(close, low, 22)
    return w.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f37_rges_246_wvf_above_p80_indicator_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: WVF(22) > 80th percentile of trailing 252d — elevated-fear state."""
    w = _wvf(close, low, 22)
    p80 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    return (w > p80).astype(float).where(p80.notna() & w.notna(), np.nan).diff()

def f37_rges_247_wvf_smoothed_bb_pro_22d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """WVF Pro: (WVF - SMA20(WVF)) / std20(WVF) — Bollinger-Band-normalized WVF (Williams Pro variant)."""
    w = _wvf(close, low, 22)
    m = w.rolling(20, min_periods=5).mean()
    s = w.rolling(20, min_periods=5).std()
    return _safe_div(w - m, s).diff()

def f37_rges_248_ttm_squeeze_indicator_20d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TTM Squeeze: indicator that BB(20,2) fits inside KC(20,1.5) — Carter's volatility-compression flag."""
    return _bb_kc_squeeze(close, high, low, 20, 2.0, 1.5).diff()

def f37_rges_249_ttm_squeeze_release_count_21d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of squeeze-releases (squeeze flag flips from 1 -> 0) in trailing 21d — breakout-pulse cadence."""
    sq = _bb_kc_squeeze(close, high, low, 20, 2.0, 1.5)
    rel = (sq.shift(1) == 1.0) & (sq == 0.0)
    return rel.astype(float).where(sq.notna() & sq.shift(1).notna(), np.nan).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f37_rges_250_ttm_squeeze_bars_since_last_release_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since last TTM-squeeze release — staleness of last compression-breakout."""
    sq = _bb_kc_squeeze(close, high, low, 20, 2.0, 1.5)
    rel = ((sq.shift(1) == 1.0) & (sq == 0.0)).values
    n = len(rel)
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if not np.isnan(sq.iat[i]):
            if rel[i]:
                last = i
            if last >= 0:
                out[i] = float(i - last)
    return pd.Series(out, index=close.index).diff()

def f37_rges_251_ttm_squeeze_current_duration_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive-bar streak in TTM-squeeze state — compression-duration counter."""
    sq = _bb_kc_squeeze(close, high, low, 20, 2.0, 1.5).values
    n = len(sq)
    out = np.full(n, np.nan)
    streak = 0
    for i in range(n):
        if np.isnan(sq[i]):
            out[i] = np.nan
            streak = 0
        else:
            streak = streak + 1 if sq[i] == 1.0 else 0
            out[i] = float(streak)
    return pd.Series(out, index=close.index).diff()

def f37_rges_252_ttm_squeeze_pro_1x_atr_20d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Squeeze Pro: BB(20,2) inside KC(20,1.0) — tighter (1.0 ATR) Keltner; rarer & stronger compression."""
    return _bb_kc_squeeze(close, high, low, 20, 2.0, 1.0).diff()

def f37_rges_253_close_minus_daily_pp_normalized_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - daily PP) / close — close vs prior-bar pivot point, scale-free."""
    pp = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    return _safe_div(close - pp, close).diff()

def f37_rges_254_close_minus_daily_r1_normalized_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - daily R1) / close — close vs resistance-1; positive = above R1."""
    pp = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * pp - low.shift(1)
    return _safe_div(close - r1, close).diff()

def f37_rges_255_close_minus_daily_s1_normalized_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - daily S1) / close — close vs support-1; negative = below S1."""
    pp = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s1 = 2.0 * pp - high.shift(1)
    return _safe_div(close - s1, close).diff()

def f37_rges_256_close_minus_camarilla_r3_normalized_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - Camarilla R3) / close — Camarilla resistance-3 (overbought level)."""
    r3 = close.shift(1) + 1.1 * (high.shift(1) - low.shift(1)) / 4.0
    return _safe_div(close - r3, close).diff()

def f37_rges_257_close_minus_camarilla_s3_normalized_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - Camarilla S3) / close — Camarilla support-3 (oversold level)."""
    s3 = close.shift(1) - 1.1 * (high.shift(1) - low.shift(1)) / 4.0
    return _safe_div(close - s3, close).diff()

def f37_rges_258_close_minus_weekly_pp_normalized_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - weekly PP) / close — weekly pivot of trailing 5d.
    Use 5d-trailing OHLC of *prior* week as PP basis (shift by 5)."""
    hh = high.rolling(WDAYS, min_periods=WDAYS).max().shift(WDAYS)
    ll = low.rolling(WDAYS, min_periods=WDAYS).min().shift(WDAYS)
    cc = close.shift(WDAYS)
    pp = (hh + ll + cc) / 3.0
    return _safe_div(close - pp, close).diff()

def f37_rges_259_pivot_range_r1_minus_s1_normalized_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(R1 - S1) / close — pivot-range width; wide = volatile session expected."""
    pp = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    r1 = 2.0 * pp - low.shift(1)
    s1 = 2.0 * pp - high.shift(1)
    return _safe_div(r1 - s1, close).diff()

def f37_rges_260_log_hl_slope_21d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """21d slope of log(H/L) — short-horizon range velocity."""
    return _rolling_slope(np.log(_safe_div(high, low)), MDAYS).diff()

def f37_rges_261_log_hl_slope_63d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """63d slope of log(H/L) — quarterly range velocity."""
    return _rolling_slope(np.log(_safe_div(high, low)), QDAYS).diff()

def f37_rges_262_log_hl_acceleration_21d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of (21d slope of log(H/L)) over 21d — range acceleration."""
    s = _rolling_slope(np.log(_safe_div(high, low)), MDAYS)
    return _rolling_slope(s, MDAYS).diff()

def f37_rges_263_atr_slope_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d slope of ATR(21) — direct ATR velocity."""
    return _rolling_slope(_atr(high, low, close, n=MDAYS), MDAYS).diff()

def f37_rges_264_atr_acceleration_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of (21d slope of ATR(21)) over 21d — ATR acceleration."""
    s = _rolling_slope(_atr(high, low, close, n=MDAYS), MDAYS)
    return _rolling_slope(s, MDAYS).diff()

def f37_rges_265_breakaway_gap_up_indicator_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today opens > 1.5 * ATR(21) above prior close — breakaway-gap-up candidate."""
    pc = close.shift(1)
    atr21 = _atr(high, low, close, n=MDAYS).shift(1)
    return (open_ - pc > 1.5 * atr21).astype(float).where(atr21.notna() & pc.notna(), np.nan).diff()

def f37_rges_266_breakaway_gap_down_indicator_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today opens > 1.5 * ATR(21) below prior close — breakaway-gap-down candidate."""
    pc = close.shift(1)
    atr21 = _atr(high, low, close, n=MDAYS).shift(1)
    return (pc - open_ > 1.5 * atr21).astype(float).where(atr21.notna() & pc.notna(), np.nan).diff()

def f37_rges_267_runaway_gap_up_indicator_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: gap-up >1 ATR AND prior 5d return > 0 — runaway-gap-up (gap in same direction as trend)."""
    pc = close.shift(1)
    atr21 = _atr(high, low, close, n=MDAYS).shift(1)
    gap_up = open_ - pc > atr21
    trend_up = close.shift(1) > close.shift(WDAYS + 1)
    return (gap_up & trend_up).astype(float).where(atr21.notna() & trend_up.notna(), np.nan).diff()

def f37_rges_268_runaway_gap_down_indicator_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: gap-down >1 ATR AND prior 5d return < 0 — runaway-gap-down."""
    pc = close.shift(1)
    atr21 = _atr(high, low, close, n=MDAYS).shift(1)
    gap_down = pc - open_ > atr21
    trend_dn = close.shift(1) < close.shift(WDAYS + 1)
    return (gap_down & trend_dn).astype(float).where(atr21.notna() & trend_dn.notna(), np.nan).diff()

def f37_rges_269_exhaustion_gap_up_indicator_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: gap-up >1.5 ATR AND today's close < open — exhaustion-gap-up (reversal candle on big up gap)."""
    pc = close.shift(1)
    atr21 = _atr(high, low, close, n=MDAYS).shift(1)
    gap_up = open_ - pc > 1.5 * atr21
    bear_close = close < open_
    return (gap_up & bear_close).astype(float).where(atr21.notna() & pc.notna(), np.nan).diff()

def f37_rges_270_gap_count_above_1atr_in_21d_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in trailing 21d where |open - prior close| > ATR(21) — gap-cluster intensity."""
    pc = close.shift(1)
    atr21 = _atr(high, low, close, n=MDAYS).shift(1)
    flag = ((open_ - pc).abs() > atr21).astype(float).where(atr21.notna() & pc.notna(), np.nan)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f37_rges_271_largest_signed_gap_in_252d_d1(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Largest signed gap (open / prior_close - 1) in trailing 252d by absolute magnitude — biggest gap event."""
    pc = close.shift(1)
    gap = _safe_div(open_, pc) - 1.0

    def _max_abs(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        return float(v[np.argmax(np.abs(v))])
    return gap.rolling(YDAYS, min_periods=QDAYS).apply(_max_abs, raw=True).diff()

def f37_rges_272_range_cusum_max_abs_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """CUSUM (max absolute) of centered log(H/L) over 252d — structural-break severity in range process."""
    return _cusum_max_abs(np.log(_safe_div(high, low)), YDAYS, QDAYS).diff()

def f37_rges_273_range_cusum_breakpoint_loc_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Location (fraction of window) of CUSUM peak of log(H/L) over 252d — *when* the break happened."""

    def _loc(w):
        v = w[~np.isnan(w)]
        if v.size < 21:
            return np.nan
        c = np.cumsum(v - v.mean())
        return float(np.argmax(np.abs(c)) / v.size)
    return np.log(_safe_div(high, low)).rolling(YDAYS, min_periods=QDAYS).apply(_loc, raw=True).diff()

def f37_rges_274_range_regime_shift_indicator_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: CUSUM max-abs > 2 * sqrt(N) * std(log H/L) — significant structural break in range process."""
    log_hl = np.log(_safe_div(high, low))
    cm = _cusum_max_abs(log_hl, YDAYS, QDAYS)
    sd = log_hl.rolling(YDAYS, min_periods=QDAYS).std()
    threshold = 2.0 * np.sqrt(YDAYS) * sd
    return (cm > threshold).astype(float).where(cm.notna() & threshold.notna(), np.nan).diff()

def f37_rges_275_range_regime_change_count_504d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of bars in trailing 504d where range-regime indicator turned on (regime shift events)."""
    log_hl = np.log(_safe_div(high, low))
    cm = _cusum_max_abs(log_hl, YDAYS, QDAYS)
    sd = log_hl.rolling(YDAYS, min_periods=QDAYS).std()
    threshold = 2.0 * np.sqrt(YDAYS) * sd
    flag = (cm > threshold).astype(float).where(cm.notna() & threshold.notna(), np.nan)
    on = (flag == 1.0) & (flag.shift(1) == 0.0)
    return on.astype(float).where(flag.notna() & flag.shift(1).notna(), np.nan).rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f37_rges_276_bars_since_last_range_regime_shift_504d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since the last range-regime shift event — staleness of last structural break."""
    log_hl = np.log(_safe_div(high, low))
    cm = _cusum_max_abs(log_hl, YDAYS, QDAYS)
    sd = log_hl.rolling(YDAYS, min_periods=QDAYS).std()
    threshold = 2.0 * np.sqrt(YDAYS) * sd
    flag = (cm > threshold).astype(float)
    on = (flag == 1.0) & (flag.shift(1) == 0.0)
    arr = on.values
    n = len(arr)
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if not np.isnan(cm.iat[i]) and (not np.isnan(threshold.iat[i])):
            if arr[i]:
                last = i
            if last >= 0:
                out[i] = float(i - last)
    return pd.Series(out, index=high.index).diff()

def f37_rges_277_log_hl_mean_reversion_speed_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """OU mean-reversion speed kappa for log(H/L): kappa ~ -ln(AR1 coef of log H/L) — range mean-reversion speed."""
    log_hl = np.log(_safe_div(high, low))

    def _ac1(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[:-1]
        b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    ac1 = log_hl.rolling(YDAYS, min_periods=QDAYS).apply(_ac1, raw=True)
    return (-np.log(ac1.where((ac1 > 0) & (ac1 < 1)))).diff()

def f37_rges_278_log_hl_half_life_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Half-life (bars) of log(H/L) mean reversion — speed of range-shock decay."""
    log_hl = np.log(_safe_div(high, low))

    def _ac1(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[:-1]
        b = v[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    ac1 = log_hl.rolling(YDAYS, min_periods=QDAYS).apply(_ac1, raw=True)
    return (-np.log(2.0) / np.log(ac1.where((ac1 > 0) & (ac1 < 1)))).diff()

def f37_rges_279_log_hl_high_pass_filter_63d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """log(H/L) minus 63d EMA — Ehlers-style high-pass filter; isolates range cycle component."""
    log_hl = np.log(_safe_div(high, low))
    return (log_hl - log_hl.ewm(span=QDAYS, adjust=False, min_periods=MDAYS).mean()).diff()

def f37_rges_280_range_cycle_amplitude_63d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of (log(H/L) - 63d EMA) over 63d — cycle amplitude of range process."""
    log_hl = np.log(_safe_div(high, low))
    hp = log_hl - log_hl.ewm(span=QDAYS, adjust=False, min_periods=MDAYS).mean()
    return hp.rolling(QDAYS, min_periods=MDAYS).std().diff()

def f37_rges_281_log_hl_overshoot_ratio_21_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean log(H/L)_21d / mean log(H/L)_252d — short-vs-long range overshoot."""
    log_hl = np.log(_safe_div(high, low))
    m21 = log_hl.rolling(MDAYS, min_periods=WDAYS).mean()
    m252 = log_hl.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(m21, m252).diff()

def f37_rges_282_trend_strength_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-blend of ADX(14) + |VI diff(14)| + |RWI diff(14)| — overall trend-strength composite."""
    adx = _adx(high, low, close, 14)
    vip, vin = _vortex(high, low, close, 14)
    rwd = _rwi_high(high, low, close, 14) - _rwi_low(high, low, close, 14)
    z_a = _rolling_zscore(adx, YDAYS, min_periods=QDAYS)
    z_v = _rolling_zscore((vip - vin).abs(), YDAYS, min_periods=QDAYS)
    z_r = _rolling_zscore(rwd.abs(), YDAYS, min_periods=QDAYS)
    return ((z_a + z_v + z_r) / 3.0).diff()

def f37_rges_283_bearish_trend_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-blend of ADX + (-)VI_diff + (-)RWI_diff — bearish-trend severity (high when down-trend is strong)."""
    adx = _adx(high, low, close, 14)
    vip, vin = _vortex(high, low, close, 14)
    rwd = _rwi_high(high, low, close, 14) - _rwi_low(high, low, close, 14)
    z_a = _rolling_zscore(adx, YDAYS, min_periods=QDAYS)
    z_v = _rolling_zscore(-(vip - vin), YDAYS, min_periods=QDAYS)
    z_r = _rolling_zscore(-rwd, YDAYS, min_periods=QDAYS)
    return ((z_a + z_v + z_r) / 3.0).diff()

def f37_rges_284_panic_indicator_composite_252d_d1(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Z-blend of WVF + range expansion + |daily return| — sharp-decline panic composite."""
    w = _wvf(close, low, 22)
    log_hl = np.log(_safe_div(high, low))
    exp_ratio = _safe_div(log_hl, log_hl.rolling(YDAYS, min_periods=QDAYS).mean())
    daily_ret = _safe_log(close).diff().abs()
    z_w = _rolling_zscore(w, YDAYS, min_periods=QDAYS)
    z_e = _rolling_zscore(exp_ratio, YDAYS, min_periods=QDAYS)
    z_d = _rolling_zscore(daily_ret, YDAYS, min_periods=QDAYS)
    return ((z_w + z_e + z_d) / 3.0).diff()

def f37_rges_285_compression_composite_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-blend of (-)TTM squeeze duration + (-)log(H/L) overshoot 21/252 + (-)ATR slope — coiling composite."""
    sq_dur = _ttm_dur_series(close, high, low)
    log_hl = np.log(_safe_div(high, low))
    overshoot = _safe_div(log_hl.rolling(MDAYS, min_periods=WDAYS).mean(), log_hl.rolling(YDAYS, min_periods=QDAYS).mean())
    atr_slope = _rolling_slope(_atr(high, low, close, n=MDAYS), MDAYS)
    z_s = _rolling_zscore(sq_dur, YDAYS, min_periods=QDAYS)
    z_o = _rolling_zscore(-overshoot, YDAYS, min_periods=QDAYS)
    z_a = _rolling_zscore(-atr_slope, YDAYS, min_periods=QDAYS)
    return ((z_s + z_o + z_a) / 3.0).diff()

def f37_rges_286_range_at_recent_peak_indicator_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: within 5% of trailing 252d high AND log(H/L) > 80th-pct of 252d — wide-range AT peak (climax)."""
    log_hl = np.log(_safe_div(high, low))
    p80 = log_hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    wide_range = log_hl > p80
    return (near_peak & wide_range).astype(float).where(p80.notna() & peak.notna(), np.nan).diff()

def f37_rges_287_post_peak_range_expansion_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of log(H/L) over 63d evaluated only on bars within 60d after a 252d-high — range ramping after peak."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    is_new_high = close >= rmax
    arr = is_new_high.values
    n = len(arr)
    bsp = np.full(n, np.nan)
    last_peak = -1
    for i in range(n):
        if not np.isnan(close.iat[i]) and arr[i]:
            last_peak = i
        if last_peak >= 0:
            bsp[i] = float(i - last_peak)
    bsp_s = pd.Series(bsp, index=close.index)
    slope = _rolling_slope(np.log(_safe_div(high, low)), QDAYS)
    return slope.where(bsp_s < 60, np.nan).diff()

def f37_rges_288_range_momentum_divergence_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: 21d return < 0 AND 21d slope of log(H/L) > 0 — price falling while range expanding (divergence)."""
    r21 = _safe_log(close).diff(MDAYS)
    rng_slope = _rolling_slope(np.log(_safe_div(high, low)), MDAYS)
    return ((r21 < 0) & (rng_slope > 0)).astype(float).where(r21.notna() & rng_slope.notna(), np.nan).diff()

def f37_rges_289_gap_cluster_severity_composite_252d_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-blend of gap_count_above_1atr_21d + |largest_signed_gap_252d| + exhaustion-gap-count_252d.
    Components averaged with skipna so composite is defined when ANY component is."""
    pc = close.shift(1)
    atr21 = _atr(high, low, close, n=MDAYS).shift(1)
    gap = _safe_div(open_, pc) - 1.0
    abs_gap = ((open_ - pc).abs() > atr21).astype(float).where(atr21.notna() & pc.notna(), np.nan)
    cnt = abs_gap.rolling(MDAYS, min_periods=WDAYS).sum()

    def _max_abs(w):
        v = w[~np.isnan(w)]
        if v.size < 5:
            return np.nan
        return float(np.max(np.abs(v)))
    big = gap.rolling(YDAYS, min_periods=QDAYS).apply(_max_abs, raw=True)
    exh_up = ((open_ - pc > 1.5 * atr21) & (close < open_)).astype(float).where(atr21.notna(), np.nan)
    exh_cnt = exh_up.rolling(YDAYS, min_periods=QDAYS).sum()
    z_c = _rolling_zscore(cnt, YDAYS, min_periods=QDAYS)
    z_b = _rolling_zscore(big, YDAYS, min_periods=QDAYS)
    z_e = _rolling_zscore(exh_cnt, YDAYS, min_periods=QDAYS)
    pieces = pd.concat([z_c.rename('c'), z_b.rename('b'), z_e.rename('e')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()

def f37_rges_290_trend_exhaustion_composite_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-blend of ADX peaking (delta-ADX negative after high ADX) + range exhaustion (slope of H/L negative) — exhaustion signal."""
    adx = _adx(high, low, close, 14)
    delta_adx = adx.diff(WDAYS)
    high_adx = adx > 25.0
    adx_peaking = (delta_adx < 0) & high_adx
    rng_slope = _rolling_slope(np.log(_safe_div(high, low)), MDAYS)
    rng_exhausting = rng_slope < 0
    score = adx_peaking.astype(float) + rng_exhausting.astype(float)
    z_s = _rolling_zscore(score, YDAYS, min_periods=QDAYS)
    z_adx = _rolling_zscore(adx, YDAYS, min_periods=QDAYS)
    return ((z_s + z_adx) / 2.0).diff()

def f37_rges_291_multi_horizon_range_expansion_composite_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of z-scored slopes of log(H/L) at horizons {5, 21, 63, 252} — broad-horizon range-expansion score."""
    log_hl = np.log(_safe_div(high, low))
    s5 = _rolling_slope(log_hl, WDAYS)
    s21 = _rolling_slope(log_hl, MDAYS)
    s63 = _rolling_slope(log_hl, QDAYS)
    s252 = _rolling_slope(log_hl, YDAYS)
    return ((_rolling_zscore(s5, YDAYS, min_periods=QDAYS) + _rolling_zscore(s21, YDAYS, min_periods=QDAYS) + _rolling_zscore(s63, YDAYS, min_periods=QDAYS) + _rolling_zscore(s252, YDAYS, min_periods=QDAYS)) / 4.0).diff()

def f37_rges_292_pivot_breakdown_severity_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of (close - daily S1) / close over trailing 252d, restricted to bars where close < S1 — sustained pivot breakdown depth."""
    pp = (high.shift(1) + low.shift(1) + close.shift(1)) / 3.0
    s1 = 2.0 * pp - high.shift(1)
    below = close < s1
    depth = _safe_div(close - s1, close).where(below)
    return depth.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f37_rges_293_wvf_at_peak_indicator_252d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """Indicator: WVF > 80th-pct AND within 5% of 252d close-high — fear gauge spiking near recent peak."""
    w = _wvf(close, low, 22)
    p80 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    return ((w > p80) & near_peak).astype(float).where(p80.notna() & peak.notna(), np.nan).diff()

def f37_rges_294_squeeze_to_panic_composite_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars-since-last-squeeze-release < 5 AND WVF > p80 — coiled-then-broken into panic (short-side trigger)."""
    sq = _bb_kc_squeeze(close, high, low, 20, 2.0, 1.5)
    rel = ((sq.shift(1) == 1.0) & (sq == 0.0)).values
    n = len(rel)
    bsr = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if not np.isnan(sq.iat[i]):
            if rel[i]:
                last = i
            if last >= 0:
                bsr[i] = float(i - last)
    bsr_s = pd.Series(bsr, index=close.index)
    w = _wvf(close, low, 22)
    p80 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.8)
    return ((bsr_s < WDAYS) & (w > p80)).astype(float).where(bsr_s.notna() & p80.notna(), np.nan).diff()

def f37_rges_295_adx_falling_from_extreme_indicator_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ADX was > 40 in last 21 bars AND now falling for 5 bars — strong-trend-rolling-over flag."""
    adx = _adx(high, low, close, 14)
    was_extreme = (adx > 40.0).rolling(MDAYS, min_periods=WDAYS).max() > 0
    falling = adx.diff(WDAYS) < 0
    return (was_extreme & falling).astype(float).where(adx.notna(), np.nan).diff()

def f37_rges_296_range_expansion_z_score_at_peak_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of log(H/L) in 252d distribution evaluated only at near-peak bars — range extremity at peak."""
    log_hl = np.log(_safe_div(high, low))
    z = _rolling_zscore(log_hl, YDAYS, min_periods=QDAYS)
    peak = close.rolling(YDAYS, min_periods=QDAYS).max()
    near_peak = close >= 0.95 * peak
    return z.where(near_peak, np.nan).diff()

def f37_rges_297_vortex_bearish_persistence_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d where VI-(14) > VI+(14) — sustained-bearish-Vortex regime share."""
    vip, vin = _vortex(high, low, close, 14)
    flag = (vin > vip).astype(float).where(vip.notna() & vin.notna(), np.nan)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f37_rges_298_compression_to_breakdown_composite_504d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-blend of (1 - ttm_squeeze_duration) + range_regime_shift_count + ADX_zscore — multi-step
    compression-then-breakdown profile evaluated over biennial window."""
    sq_dur = _ttm_dur_series(close, high, low)
    log_hl = np.log(_safe_div(high, low))
    cm = _cusum_max_abs(log_hl, YDAYS, QDAYS)
    sd = log_hl.rolling(YDAYS, min_periods=QDAYS).std()
    threshold = 2.0 * np.sqrt(YDAYS) * sd
    flag = (cm > threshold).astype(float)
    on = (flag == 1.0) & (flag.shift(1) == 0.0)
    rc = on.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    adx = _adx(high, low, close, 14)
    z_sq = _rolling_zscore(-sq_dur, DDAYS_2Y, min_periods=YDAYS)
    z_rc = _rolling_zscore(rc, DDAYS_2Y, min_periods=YDAYS)
    z_adx = _rolling_zscore(adx, DDAYS_2Y, min_periods=YDAYS)
    return ((z_sq + z_rc + z_adx) / 3.0).diff()

def f37_rges_299_panic_with_trend_strength_252d_d1(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Z-blend of WVF + ADX — high when fear (WVF) AND trend strength (ADX) are both elevated."""
    w = _wvf(close, low, 22)
    adx = _adx(high, low, close, 14)
    z_w = _rolling_zscore(w, YDAYS, min_periods=QDAYS)
    z_a = _rolling_zscore(adx, YDAYS, min_periods=QDAYS)
    return ((z_w + z_a) / 2.0).diff()

def f37_rges_300_final_stuck_peak_range_composite_504d_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Master composite for short-side stuck-peak detection from range/trend domain:
    bearish_trend + panic + range_regime_shift + ADX falling-from-extreme.
    Each piece z-scored over full series, then averaged. Defined whenever any
    underlying z-score is defined (uses .mean(axis=1) over the 4 components)."""
    adx = _adx(high, low, close, 14)
    vip, vin = _vortex(high, low, close, 14)
    rwd = _rwi_high(high, low, close, 14) - _rwi_low(high, low, close, 14)
    z_adx = _rolling_zscore(adx, DDAYS_2Y, min_periods=QDAYS)
    z_vor = _rolling_zscore(-(vip - vin), DDAYS_2Y, min_periods=QDAYS)
    z_rwi = _rolling_zscore(-rwd, DDAYS_2Y, min_periods=QDAYS)
    w = _wvf(close, low, 22)
    z_w = _rolling_zscore(w, DDAYS_2Y, min_periods=QDAYS)
    log_hl = np.log(_safe_div(high, low))
    cm = _cusum_max_abs(log_hl, YDAYS, QDAYS)
    sd = log_hl.rolling(YDAYS, min_periods=QDAYS).std()
    threshold = 2.0 * np.sqrt(YDAYS) * sd
    flag = (cm > threshold).astype(float)
    on = (flag == 1.0) & (flag.shift(1) == 0.0)
    rc = on.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    z_rc = _rolling_zscore(rc, DDAYS_2Y, min_periods=QDAYS)
    delta_adx = adx.diff(WDAYS)
    z_dadx_neg = _rolling_zscore(-delta_adx, DDAYS_2Y, min_periods=QDAYS)
    pieces = pd.concat([z_adx.rename('a'), z_vor.rename('v'), z_rwi.rename('r'), z_w.rename('w'), z_rc.rename('c'), z_dadx_neg.rename('d')], axis=1)
    return pieces.mean(axis=1, skipna=True).diff()
RANGE_ESTIMATORS_FAMILY_D1_REGISTRY_226_300 = {'f37_rges_226_adx_14d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_226_adx_14d_d1}, 'f37_rges_227_adx_28d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_227_adx_28d_d1}, 'f37_rges_228_adx_above_25_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_228_adx_above_25_indicator_d1}, 'f37_rges_229_adx_rising_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_229_adx_rising_indicator_d1}, 'f37_rges_230_adx_zscore_in_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_230_adx_zscore_in_252d_d1}, 'f37_rges_231_adx_slope_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_231_adx_slope_21d_d1}, 'f37_rges_232_vortex_plus_14d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_232_vortex_plus_14d_d1}, 'f37_rges_233_vortex_minus_14d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_233_vortex_minus_14d_d1}, 'f37_rges_234_vortex_diff_14d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_234_vortex_diff_14d_d1}, 'f37_rges_235_vortex_diff_28d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_235_vortex_diff_28d_d1}, 'f37_rges_236_vortex_crossover_down_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_236_vortex_crossover_down_indicator_d1}, 'f37_rges_237_vortex_minus_above_plus_streak_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_237_vortex_minus_above_plus_streak_d1}, 'f37_rges_238_rwi_high_14d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_238_rwi_high_14d_d1}, 'f37_rges_239_rwi_low_14d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_239_rwi_low_14d_d1}, 'f37_rges_240_rwi_diff_14d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_240_rwi_diff_14d_d1}, 'f37_rges_241_rwi_high_28d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_241_rwi_high_28d_d1}, 'f37_rges_242_rwi_max_14d_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_242_rwi_max_14d_indicator_d1}, 'f37_rges_243_wvf_22d_d1': {'inputs': ['close', 'low'], 'func': f37_rges_243_wvf_22d_d1}, 'f37_rges_244_wvf_zscore_in_252d_d1': {'inputs': ['close', 'low'], 'func': f37_rges_244_wvf_zscore_in_252d_d1}, 'f37_rges_245_wvf_percentile_rank_252d_d1': {'inputs': ['close', 'low'], 'func': f37_rges_245_wvf_percentile_rank_252d_d1}, 'f37_rges_246_wvf_above_p80_indicator_d1': {'inputs': ['close', 'low'], 'func': f37_rges_246_wvf_above_p80_indicator_d1}, 'f37_rges_247_wvf_smoothed_bb_pro_22d_d1': {'inputs': ['close', 'low'], 'func': f37_rges_247_wvf_smoothed_bb_pro_22d_d1}, 'f37_rges_248_ttm_squeeze_indicator_20d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_248_ttm_squeeze_indicator_20d_d1}, 'f37_rges_249_ttm_squeeze_release_count_21d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_249_ttm_squeeze_release_count_21d_d1}, 'f37_rges_250_ttm_squeeze_bars_since_last_release_252d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_250_ttm_squeeze_bars_since_last_release_252d_d1}, 'f37_rges_251_ttm_squeeze_current_duration_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_251_ttm_squeeze_current_duration_d1}, 'f37_rges_252_ttm_squeeze_pro_1x_atr_20d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_252_ttm_squeeze_pro_1x_atr_20d_d1}, 'f37_rges_253_close_minus_daily_pp_normalized_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_253_close_minus_daily_pp_normalized_d1}, 'f37_rges_254_close_minus_daily_r1_normalized_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_254_close_minus_daily_r1_normalized_d1}, 'f37_rges_255_close_minus_daily_s1_normalized_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_255_close_minus_daily_s1_normalized_d1}, 'f37_rges_256_close_minus_camarilla_r3_normalized_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_256_close_minus_camarilla_r3_normalized_d1}, 'f37_rges_257_close_minus_camarilla_s3_normalized_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_257_close_minus_camarilla_s3_normalized_d1}, 'f37_rges_258_close_minus_weekly_pp_normalized_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_258_close_minus_weekly_pp_normalized_d1}, 'f37_rges_259_pivot_range_r1_minus_s1_normalized_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_259_pivot_range_r1_minus_s1_normalized_d1}, 'f37_rges_260_log_hl_slope_21d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_260_log_hl_slope_21d_d1}, 'f37_rges_261_log_hl_slope_63d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_261_log_hl_slope_63d_d1}, 'f37_rges_262_log_hl_acceleration_21d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_262_log_hl_acceleration_21d_d1}, 'f37_rges_263_atr_slope_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_263_atr_slope_21d_d1}, 'f37_rges_264_atr_acceleration_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_264_atr_acceleration_21d_d1}, 'f37_rges_265_breakaway_gap_up_indicator_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_265_breakaway_gap_up_indicator_d1}, 'f37_rges_266_breakaway_gap_down_indicator_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_266_breakaway_gap_down_indicator_d1}, 'f37_rges_267_runaway_gap_up_indicator_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_267_runaway_gap_up_indicator_d1}, 'f37_rges_268_runaway_gap_down_indicator_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_268_runaway_gap_down_indicator_d1}, 'f37_rges_269_exhaustion_gap_up_indicator_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_269_exhaustion_gap_up_indicator_d1}, 'f37_rges_270_gap_count_above_1atr_in_21d_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_270_gap_count_above_1atr_in_21d_d1}, 'f37_rges_271_largest_signed_gap_in_252d_d1': {'inputs': ['open', 'close'], 'func': f37_rges_271_largest_signed_gap_in_252d_d1}, 'f37_rges_272_range_cusum_max_abs_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_272_range_cusum_max_abs_252d_d1}, 'f37_rges_273_range_cusum_breakpoint_loc_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_273_range_cusum_breakpoint_loc_252d_d1}, 'f37_rges_274_range_regime_shift_indicator_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_274_range_regime_shift_indicator_252d_d1}, 'f37_rges_275_range_regime_change_count_504d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_275_range_regime_change_count_504d_d1}, 'f37_rges_276_bars_since_last_range_regime_shift_504d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_276_bars_since_last_range_regime_shift_504d_d1}, 'f37_rges_277_log_hl_mean_reversion_speed_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_277_log_hl_mean_reversion_speed_252d_d1}, 'f37_rges_278_log_hl_half_life_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_278_log_hl_half_life_252d_d1}, 'f37_rges_279_log_hl_high_pass_filter_63d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_279_log_hl_high_pass_filter_63d_d1}, 'f37_rges_280_range_cycle_amplitude_63d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_280_range_cycle_amplitude_63d_d1}, 'f37_rges_281_log_hl_overshoot_ratio_21_252d_d1': {'inputs': ['high', 'low'], 'func': f37_rges_281_log_hl_overshoot_ratio_21_252d_d1}, 'f37_rges_282_trend_strength_composite_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_282_trend_strength_composite_252d_d1}, 'f37_rges_283_bearish_trend_composite_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_283_bearish_trend_composite_252d_d1}, 'f37_rges_284_panic_indicator_composite_252d_d1': {'inputs': ['close', 'low', 'high'], 'func': f37_rges_284_panic_indicator_composite_252d_d1}, 'f37_rges_285_compression_composite_252d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_285_compression_composite_252d_d1}, 'f37_rges_286_range_at_recent_peak_indicator_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_286_range_at_recent_peak_indicator_252d_d1}, 'f37_rges_287_post_peak_range_expansion_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_287_post_peak_range_expansion_63d_d1}, 'f37_rges_288_range_momentum_divergence_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_288_range_momentum_divergence_252d_d1}, 'f37_rges_289_gap_cluster_severity_composite_252d_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_289_gap_cluster_severity_composite_252d_d1}, 'f37_rges_290_trend_exhaustion_composite_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_290_trend_exhaustion_composite_252d_d1}, 'f37_rges_291_multi_horizon_range_expansion_composite_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_291_multi_horizon_range_expansion_composite_d1}, 'f37_rges_292_pivot_breakdown_severity_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_292_pivot_breakdown_severity_252d_d1}, 'f37_rges_293_wvf_at_peak_indicator_252d_d1': {'inputs': ['close', 'low'], 'func': f37_rges_293_wvf_at_peak_indicator_252d_d1}, 'f37_rges_294_squeeze_to_panic_composite_252d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_294_squeeze_to_panic_composite_252d_d1}, 'f37_rges_295_adx_falling_from_extreme_indicator_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_295_adx_falling_from_extreme_indicator_252d_d1}, 'f37_rges_296_range_expansion_z_score_at_peak_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_296_range_expansion_z_score_at_peak_252d_d1}, 'f37_rges_297_vortex_bearish_persistence_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f37_rges_297_vortex_bearish_persistence_252d_d1}, 'f37_rges_298_compression_to_breakdown_composite_504d_d1': {'inputs': ['close', 'high', 'low'], 'func': f37_rges_298_compression_to_breakdown_composite_504d_d1}, 'f37_rges_299_panic_with_trend_strength_252d_d1': {'inputs': ['close', 'low', 'high'], 'func': f37_rges_299_panic_with_trend_strength_252d_d1}, 'f37_rges_300_final_stuck_peak_range_composite_504d_d1': {'inputs': ['open', 'high', 'low', 'close'], 'func': f37_rges_300_final_stuck_peak_range_composite_504d_d1}}