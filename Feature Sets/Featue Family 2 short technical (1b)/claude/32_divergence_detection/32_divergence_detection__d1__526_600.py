"""32_divergence_detection d1 features 526-600 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()

def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()

def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill

def _slope_div_sign(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    return ((ps > 0) & (osl < 0)).astype(float).where(ps.notna() & osl.notna(), np.nan)

def _vortex_pos(high, low, close, n=14):
    """Vortex VI+(n): sum(|H - prior L|, n) / sum(TR, n)."""
    vm_pos = (high - low.shift(1)).abs()
    tr = _true_range(high, low, close)
    return _safe_div(vm_pos.rolling(n, min_periods=max(n // 3, 2)).sum(), tr.rolling(n, min_periods=max(n // 3, 2)).sum())

def _vortex_neg(high, low, close, n=14):
    """Vortex VI-(n): sum(|L - prior H|, n) / sum(TR, n)."""
    vm_neg = (low - high.shift(1)).abs()
    tr = _true_range(high, low, close)
    return _safe_div(vm_neg.rolling(n, min_periods=max(n // 3, 2)).sum(), tr.rolling(n, min_periods=max(n // 3, 2)).sum())

def _ravi(close, fast=7, slow=65):
    """RAVI (Range Action Verification Index): abs(SMA(fast) - SMA(slow)) / SMA(slow) × 100."""
    return 100.0 * _safe_div((_sma(close, fast) - _sma(close, slow)).abs(), _sma(close, slow))

def _mass_index(high, low, n1=9, n2=25):
    """Mass Index: sum over n2 of (EMA(n1) of range / EMA-EMA(n1) of range). Reversal anticipator."""
    rng = high - low
    e1 = _ema(rng, n1)
    e2 = _ema(e1, n1)
    ratio = _safe_div(e1, e2)
    return ratio.rolling(n2, min_periods=max(n2 // 3, 2)).sum()

def f32_divd_526_wyckoff_effort_zscore_minus_result_zscore_21d_d1(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Effort minus result: z(volume,21) - z(|body|,21). Positive = much vol, little price move (distribution)."""
    effort = _rolling_zscore(volume, MDAYS)
    result = _rolling_zscore((close - open).abs(), MDAYS)
    return (effort - result).diff()

def f32_divd_527_wyckoff_vol_body_ratio_21d_d1(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """volume / (|body| × close) — vol relative to dollar move per share."""
    return _safe_div(volume, (close - open).abs() * close).diff()

def f32_divd_528_wyckoff_wide_vol_narrow_body_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when volume in 252d top decile AND |body| in 252d bottom 30% — classic distribution candle."""
    vol_top = (_pct_rank(volume, YDAYS) >= 0.9).astype(float)
    body_bot = (_pct_rank((close - open).abs(), YDAYS) <= 0.3).astype(float)
    return (vol_top * body_bot).where(vol_top.notna() & body_bot.notna(), np.nan).diff()

def f32_divd_529_wyckoff_climactic_vol_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when volume in 252d top 5% AND close in lower 30% of bar — climactic-vol exhaustion bar."""
    vol_extreme = (_pct_rank(volume, YDAYS) >= 0.95).astype(float)
    close_pos = _safe_div(close - low, high - low)
    close_low = (close_pos < 0.3).astype(float)
    return (vol_extreme * close_low).where(vol_extreme.notna() & close_low.notna(), np.nan).diff()

def f32_divd_530_wyckoff_upthrust_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 on Upthrust bar: high > prior high, close in lower half of bar, vol z(63d) > 1."""
    new_high = (high > high.shift(1)).astype(float)
    close_pos = _safe_div(close - low, high - low)
    weak_close = (close_pos < 0.5).astype(float)
    high_vol = (_rolling_zscore(volume, QDAYS) > 1.0).astype(float)
    return (new_high * weak_close * high_vol).where(new_high.notna() & weak_close.notna() & high_vol.notna(), np.nan).diff()

def f32_divd_531_wyckoff_no_demand_bar_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 on no-demand bar: close > open (up bar) BUT range in bottom 30% AND vol z(63) < -0.5."""
    up_bar = (close > open).astype(float)
    rng = high - low
    narrow = (_pct_rank(rng, YDAYS) <= 0.3).astype(float)
    low_vol = (_rolling_zscore(volume, QDAYS) < -0.5).astype(float)
    return (up_bar * narrow * low_vol).where(up_bar.notna() & narrow.notna() & low_vol.notna(), np.nan).diff()

def f32_divd_532_wyckoff_no_supply_bar_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 on no-supply bar: close < open AND range in bottom 30% AND vol z(63) < -0.5."""
    down_bar = (close < open).astype(float)
    rng = high - low
    narrow = (_pct_rank(rng, YDAYS) <= 0.3).astype(float)
    low_vol = (_rolling_zscore(volume, QDAYS) < -0.5).astype(float)
    return (down_bar * narrow * low_vol).where(down_bar.notna() & narrow.notna() & low_vol.notna(), np.nan).diff()

def f32_divd_533_wyckoff_effort_minus_result_zscore_252d_d1(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (effort - result diff) over 252d."""
    effort = _rolling_zscore(volume, MDAYS)
    result = _rolling_zscore((close - open).abs(), MDAYS)
    return _rolling_zscore(effort - result, YDAYS).diff()

def f32_divd_534_wyckoff_cumulative_vol_div_price_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope-div between cumulative vol (proxy for cumulative effort) and log-close over 252d."""
    cum_vol = volume.cumsum()
    return _slope_div_sign(close, cum_vol, YDAYS).diff()

def f32_divd_535_wyckoff_days_since_last_upthrust_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent Upthrust bar."""
    new_high = (high > high.shift(1)).astype(float)
    close_pos = _safe_div(close - low, high - low)
    weak_close = (close_pos < 0.5).astype(float)
    high_vol = (_rolling_zscore(volume, QDAYS) > 1.0).astype(float)
    flag = new_high * weak_close * high_vol
    return _bars_since_true(flag).diff()

def f32_divd_536_wyckoff_upthrust_count_252d_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Upthrust bars in trailing 252d."""
    new_high = (high > high.shift(1)).astype(float)
    close_pos = _safe_div(close - low, high - low)
    weak_close = (close_pos < 0.5).astype(float)
    high_vol = (_rolling_zscore(volume, QDAYS) > 1.0).astype(float)
    flag = (new_high * weak_close * high_vol).fillna(0)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f32_divd_537_wyckoff_climactic_vol_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when climactic-vol bar AND close within 1% of 252d max (top-distribution event)."""
    vol_extreme = (_pct_rank(volume, YDAYS) >= 0.95).astype(float)
    close_pos = _safe_div(close - low, high - low)
    close_low = (close_pos < 0.3).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (vol_extreme * close_low * near).where(vol_extreme.notna() & close_low.notna() & near.notna(), np.nan).diff()

def f32_divd_538_wyckoff_no_demand_bar_count_252d_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of no-demand bars in trailing 252d."""
    up_bar = (close > open).astype(float)
    rng = high - low
    narrow = (_pct_rank(rng, YDAYS) <= 0.3).astype(float)
    low_vol = (_rolling_zscore(volume, QDAYS) < -0.5).astype(float)
    flag = (up_bar * narrow * low_vol).fillna(0)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f32_divd_539_wyckoff_high_effort_low_result_count_63d_d1(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of trailing 63d bars where vol z(63d) > 1 AND |body|/atr-norm in bottom 30% (effort-result mismatch)."""
    effort = (_rolling_zscore(volume, QDAYS) > 1.0).astype(float)
    body = (close - open).abs()
    body_low = (_pct_rank(body, YDAYS) <= 0.3).astype(float)
    return (effort * body_low).rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f32_divd_540_wyckoff_upthrust_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when Upthrust bar fires AND close near 252d max."""
    new_high = (high > high.shift(1)).astype(float)
    close_pos = _safe_div(close - low, high - low)
    weak_close = (close_pos < 0.5).astype(float)
    high_vol = (_rolling_zscore(volume, QDAYS) > 1.0).astype(float)
    flag = new_high * weak_close * high_vol
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (flag * near).where(flag.notna() & near.notna(), np.nan).diff()

def f32_divd_541_rolling_skew_returns_21d_d1(close: pd.Series) -> pd.Series:
    """Rolling 21d skew of daily log-returns."""
    return _safe_log(close).diff().rolling(MDAYS, min_periods=WDAYS).skew().diff()

def f32_divd_542_rolling_skew_returns_63d_d1(close: pd.Series) -> pd.Series:
    """Rolling 63d skew of daily log-returns."""
    return _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).skew().diff()

def f32_divd_543_rolling_skew_returns_252d_d1(close: pd.Series) -> pd.Series:
    """Rolling 252d skew of daily log-returns."""
    return _safe_log(close).diff().rolling(YDAYS, min_periods=QDAYS).skew().diff()

def f32_divd_544_rolling_kurt_returns_21d_d1(close: pd.Series) -> pd.Series:
    """Rolling 21d excess kurtosis of daily log-returns."""
    return _safe_log(close).diff().rolling(MDAYS, min_periods=WDAYS).kurt().diff()

def f32_divd_545_rolling_kurt_returns_63d_d1(close: pd.Series) -> pd.Series:
    """Rolling 63d excess kurtosis of daily log-returns."""
    return _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).kurt().diff()

def f32_divd_546_rolling_kurt_returns_252d_d1(close: pd.Series) -> pd.Series:
    """Rolling 252d excess kurtosis of daily log-returns."""
    return _safe_log(close).diff().rolling(YDAYS, min_periods=QDAYS).kurt().diff()

def f32_divd_547_skew_returns_change_21d_d1(close: pd.Series) -> pd.Series:
    """21d change in rolling-63d skew — skew shift detection."""
    s = _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).skew()
    return (s - s.shift(MDAYS)).diff()

def f32_divd_548_kurt_returns_change_21d_d1(close: pd.Series) -> pd.Series:
    """21d change in rolling-63d kurtosis — kurt shift detection (tail-thickening event)."""
    k = _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).kurt()
    return (k - k.shift(MDAYS)).diff()

def f32_divd_549_skew_flipped_negative_event_indicator_d1(close: pd.Series) -> pd.Series:
    """+1 on bar where 63d skew flipped from positive to negative (distribution-shape regime flip)."""
    s = _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).skew()
    return ((s.shift(1) > 0) & (s <= 0)).astype(float).where(s.notna() & s.shift(1).notna(), np.nan).diff()

def f32_divd_550_kurt_above_3_indicator_d1(close: pd.Series) -> pd.Series:
    """+1 when 63d excess kurtosis > 3 (very heavy tails)."""
    k = _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).kurt()
    return (k > 3.0).astype(float).where(k.notna(), np.nan).diff()

def f32_divd_551_skew_div_with_price_slope_sign_63d_d1(close: pd.Series) -> pd.Series:
    """Slope-div sign: price slope vs skew(63) slope — bearish if price rising while skew falling."""
    skew = _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).skew()
    return _slope_div_sign(close, skew, QDAYS).diff()

def f32_divd_552_kurt_div_with_price_slope_sign_63d_d1(close: pd.Series) -> pd.Series:
    """Slope-div sign: price slope vs kurt(63) slope — bearish if price rising while kurt rising fast (tail risk)."""
    kurt = _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).kurt()
    return _slope_div_sign(close, kurt, QDAYS).diff()

def f32_divd_553_skew_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """Z-score of 63d skew over 252d."""
    return _rolling_zscore(_safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).skew(), YDAYS).diff()

def f32_divd_554_kurt_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """Z-score of 63d kurt over 252d."""
    return _rolling_zscore(_safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).kurt(), YDAYS).diff()

def f32_divd_555_negative_skew_at_252d_high_indicator_d1(close: pd.Series) -> pd.Series:
    """+1 when 63d skew < -0.5 AND close within 1% of 252d max (negative-skew at top — left-tail risk)."""
    s = _safe_log(close).diff().rolling(QDAYS, min_periods=MDAYS).skew()
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((s < -0.5) & (near == 1)).astype(float).where(s.notna() & near.notna(), np.nan).diff()

def f32_divd_556_vortex_pos_14d_value_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(14) value — positive vortex direction."""
    return _vortex_pos(high, low, close, 14).diff()

def f32_divd_557_vortex_neg_14d_value_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI-(14) value — negative vortex direction."""
    return _vortex_neg(high, low, close, 14).diff()

def f32_divd_558_vortex_gap_pos_minus_neg_14d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """VI+(14) - VI-(14) — signed trend direction (positive = bullish vortex)."""
    return (_vortex_pos(high, low, close, 14) - _vortex_neg(high, low, close, 14)).diff()

def f32_divd_559_vortex_pos_above_neg_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when VI+ > VI- (bullish vortex regime)."""
    vp = _vortex_pos(high, low, close, 14)
    vn = _vortex_neg(high, low, close, 14)
    return (vp > vn).astype(float).where(vp.notna() & vn.notna(), np.nan).diff()

def f32_divd_560_vortex_bearish_cross_event_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 on bar where VI- crosses above VI+ (bearish vortex cross)."""
    vp = _vortex_pos(high, low, close, 14)
    vn = _vortex_neg(high, low, close, 14)
    return ((vp.shift(1) > vn.shift(1)) & (vp <= vn)).astype(float).where(vp.notna() & vn.notna(), np.nan).diff()

def f32_divd_561_days_since_vortex_bearish_cross_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent vortex bearish cross."""
    vp = _vortex_pos(high, low, close, 14)
    vn = _vortex_neg(high, low, close, 14)
    flag = ((vp.shift(1) > vn.shift(1)) & (vp <= vn)).astype(float)
    return _bars_since_true(flag).diff()

def f32_divd_562_vortex_pos_zscore_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of VI+(14) over 252d."""
    return _rolling_zscore(_vortex_pos(high, low, close, 14), YDAYS).diff()

def f32_divd_563_vortex_neg_zscore_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of VI-(14) over 252d."""
    return _rolling_zscore(_vortex_neg(high, low, close, 14), YDAYS).diff()

def f32_divd_564_vortex_cross_count_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of vortex bearish crosses in trailing 252d (regime instability)."""
    vp = _vortex_pos(high, low, close, 14)
    vn = _vortex_neg(high, low, close, 14)
    flag = ((vp.shift(1) > vn.shift(1)) & (vp <= vn)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f32_divd_565_vortex_neg_above_one_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when VI-(14) > 1.0 (strong bearish vortex)."""
    vn = _vortex_neg(high, low, close, 14)
    return (vn > 1.0).astype(float).where(vn.notna(), np.nan).diff()

def f32_divd_566_vortex_pos_below_0_8_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when VI+(14) < 0.8 (weak bullish vortex — fading momentum)."""
    vp = _vortex_pos(high, low, close, 14)
    return (vp < 0.8).astype(float).where(vp.notna(), np.nan).diff()

def f32_divd_567_vortex_bearish_cross_at_252d_high_indicator_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when vortex bearish cross fires AND close within 1% of 252d max."""
    vp = _vortex_pos(high, low, close, 14)
    vn = _vortex_neg(high, low, close, 14)
    flag = ((vp.shift(1) > vn.shift(1)) & (vp <= vn)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (flag * near).where(flag.notna() & near.notna(), np.nan).diff()

def f32_divd_568_vortex_pos_slope_div_sign_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish slope-divergence between log-close and VI+ over 63d."""
    return _slope_div_sign(close, _vortex_pos(high, low, close, 14), QDAYS).diff()

def f32_divd_569_vortex_gap_zscore_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of (VI+ - VI-) over 252d — normalized trend direction strength."""
    return _rolling_zscore(_vortex_pos(high, low, close, 14) - _vortex_neg(high, low, close, 14), YDAYS).diff()

def f32_divd_570_vortex_pos_above_one_persistence_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where VI+(14) > 1.0 (strong bullish vortex persistence)."""
    vp = _vortex_pos(high, low, close, 14)
    return (vp > 1.0).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_571_up_day_pct_21d_d1(close: pd.Series) -> pd.Series:
    """Fraction of trailing 21d bars where close > prior close."""
    return (close > close.shift(1)).astype(float).rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f32_divd_572_up_day_pct_63d_d1(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63d bars where close > prior close."""
    return (close > close.shift(1)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f32_divd_573_up_day_pct_252d_d1(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252d bars where close > prior close."""
    return (close > close.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f32_divd_574_down_day_pct_63d_d1(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63d bars where close < prior close."""
    return (close < close.shift(1)).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f32_divd_575_up_minus_down_day_pct_63d_d1(close: pd.Series) -> pd.Series:
    """Up-day-fraction minus down-day-fraction (63d) — directional asymmetry."""
    return ((close > close.shift(1)).astype(float) - (close < close.shift(1)).astype(float)).rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f32_divd_576_up_day_vol_sum_div_down_day_vol_sum_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum-of-vol-on-up-days / Sum-of-vol-on-down-days, trailing 21d (Wyckoff-style asymmetry)."""
    up_vol = volume.where(close > close.shift(1), 0)
    dn_vol = volume.where(close < close.shift(1), 0)
    return _safe_div(up_vol.rolling(MDAYS, min_periods=WDAYS).sum(), dn_vol.rolling(MDAYS, min_periods=WDAYS).sum()).diff()

def f32_divd_577_up_day_vol_sum_div_down_day_vol_sum_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up-vol / Down-vol ratio over trailing 63d."""
    up_vol = volume.where(close > close.shift(1), 0)
    dn_vol = volume.where(close < close.shift(1), 0)
    return _safe_div(up_vol.rolling(QDAYS, min_periods=MDAYS).sum(), dn_vol.rolling(QDAYS, min_periods=MDAYS).sum()).diff()

def f32_divd_578_up_day_vol_sum_div_down_day_vol_sum_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up-vol / Down-vol ratio over trailing 252d (secular accumulation/distribution)."""
    up_vol = volume.where(close > close.shift(1), 0)
    dn_vol = volume.where(close < close.shift(1), 0)
    return _safe_div(up_vol.rolling(YDAYS, min_periods=QDAYS).sum(), dn_vol.rolling(YDAYS, min_periods=QDAYS).sum()).diff()

def f32_divd_579_down_day_vol_zscore_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (mean down-day vol in trailing 21d) over 252d — distribution-volume regime."""
    dn_vol = volume.where(close < close.shift(1), np.nan)
    mean21 = dn_vol.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(mean21, YDAYS).diff()

def f32_divd_580_up_day_avg_return_63d_d1(close: pd.Series) -> pd.Series:
    """Mean log-return on up-days only, over trailing 63d."""
    ret = _safe_log(close).diff()
    up_ret = ret.where(ret > 0, np.nan)
    return up_ret.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f32_divd_581_down_day_avg_return_63d_d1(close: pd.Series) -> pd.Series:
    """Mean log-return on down-days only, over trailing 63d."""
    ret = _safe_log(close).diff()
    dn_ret = ret.where(ret < 0, np.nan)
    return dn_ret.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f32_divd_582_return_asymmetry_63d_d1(close: pd.Series) -> pd.Series:
    """|up_day_avg_return| - |down_day_avg_return| over trailing 63d — positive = bullish asymmetry."""
    ret = _safe_log(close).diff()
    up_ret = ret.where(ret > 0, np.nan).rolling(QDAYS, min_periods=MDAYS).mean().abs()
    dn_ret = ret.where(ret < 0, np.nan).rolling(QDAYS, min_periods=MDAYS).mean().abs()
    return (up_ret - dn_ret).diff()

def f32_divd_583_up_day_streak_current_d1(close: pd.Series) -> pd.Series:
    """Current consecutive-up-day streak length."""
    flag = (close > close.shift(1)).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff()

def f32_divd_584_down_day_streak_current_d1(close: pd.Series) -> pd.Series:
    """Current consecutive-down-day streak length."""
    flag = (close < close.shift(1)).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff()

def f32_divd_585_up_day_pct_252d_at_252d_high_indicator_d1(close: pd.Series) -> pd.Series:
    """+1 when up-day-pct(252d) > 0.6 AND close within 1% of 252d max (sustained advance into top)."""
    up_pct = (close > close.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((up_pct > 0.6) & (near == 1)).astype(float).where(up_pct.notna() & near.notna(), np.nan).diff()

def f32_divd_586_ravi_value_d1(close: pd.Series) -> pd.Series:
    """RAVI (7, 65) — Range Action Verification Index."""
    return _ravi(close, 7, 65).diff()

def f32_divd_587_ravi_above_3_indicator_d1(close: pd.Series) -> pd.Series:
    """+1 when RAVI > 3 (strong-trend regime per Vitali Apirine)."""
    r = _ravi(close, 7, 65)
    return (r > 3).astype(float).where(r.notna(), np.nan).diff()

def f32_divd_588_ravi_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """Z-score of RAVI over 252d."""
    return _rolling_zscore(_ravi(close, 7, 65), YDAYS).diff()

def f32_divd_589_ravi_slope_21d_d1(close: pd.Series) -> pd.Series:
    """21d slope of RAVI."""
    return _rolling_slope(_ravi(close, 7, 65), MDAYS).diff()

def f32_divd_590_ravi_above_3_persistence_21d_d1(close: pd.Series) -> pd.Series:
    """Count of trailing 21d bars where RAVI > 3."""
    r = _ravi(close, 7, 65)
    return (r > 3).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff()

def f32_divd_591_mass_index_value_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mass Index (9, 25) — range-expansion-based reversal indicator."""
    return _mass_index(high, low, 9, 25).diff()

def f32_divd_592_mass_index_above_27_indicator_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when Mass Index > 27 (Donald's reversal bulge threshold)."""
    mi = _mass_index(high, low, 9, 25)
    return (mi > 27).astype(float).where(mi.notna(), np.nan).diff()

def f32_divd_593_mass_index_slope_21d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """21d slope of Mass Index."""
    return _rolling_slope(_mass_index(high, low, 9, 25), MDAYS).diff()

def f32_divd_594_days_since_mass_index_above_27_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since most recent Mass Index reading above 27."""
    return _bars_since_true((_mass_index(high, low, 9, 25) > 27).astype(float)).diff()

def f32_divd_595_mass_index_above_27_count_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing 252d bars where Mass Index > 27."""
    return (_mass_index(high, low, 9, 25) > 27).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f32_divd_596_average_true_volume_21d_zscore_252d_d1(volume: pd.Series) -> pd.Series:
    """SMA-21 of vol-z(252d) — smoothed average true volume."""
    return _sma(_rolling_zscore(volume, YDAYS), MDAYS).diff()

def f32_divd_597_average_true_volume_slope_21d_d1(volume: pd.Series) -> pd.Series:
    """21d slope of average-true-volume (smoothed vol z-score)."""
    atv = _sma(_rolling_zscore(volume, YDAYS), MDAYS)
    return _rolling_slope(atv, MDAYS).diff()

def f32_divd_598_average_true_volume_at_252d_high_indicator_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when ATV > 1.0 (above-average smoothed vol) AND close near 252d max."""
    atv = _sma(_rolling_zscore(volume, YDAYS), MDAYS)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((atv > 1.0) & (near == 1)).astype(float).where(atv.notna() & near.notna(), np.nan).diff()

def f32_divd_599_average_true_volume_div_with_price_slope_sign_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish slope-divergence between log-close and average-true-volume over 63d."""
    atv = _sma(_rolling_zscore(volume, YDAYS), MDAYS)
    return _slope_div_sign(close, atv, QDAYS).diff()

def f32_divd_600_average_true_volume_decay_event_indicator_d1(volume: pd.Series) -> pd.Series:
    """+1 on bar where ATV crosses from above 1.0 to below 1.0 (vol-decay event)."""
    atv = _sma(_rolling_zscore(volume, YDAYS), MDAYS)
    return ((atv.shift(1) > 1.0) & (atv <= 1.0)).astype(float).where(atv.notna() & atv.shift(1).notna(), np.nan).diff()
DIVERGENCE_DETECTION_D1_REGISTRY_526_600 = {'f32_divd_526_wyckoff_effort_zscore_minus_result_zscore_21d_d1': {'inputs': ['open', 'close', 'volume'], 'func': f32_divd_526_wyckoff_effort_zscore_minus_result_zscore_21d_d1}, 'f32_divd_527_wyckoff_vol_body_ratio_21d_d1': {'inputs': ['open', 'close', 'volume'], 'func': f32_divd_527_wyckoff_vol_body_ratio_21d_d1}, 'f32_divd_528_wyckoff_wide_vol_narrow_body_indicator_d1': {'inputs': ['open', 'close', 'high', 'low', 'volume'], 'func': f32_divd_528_wyckoff_wide_vol_narrow_body_indicator_d1}, 'f32_divd_529_wyckoff_climactic_vol_indicator_d1': {'inputs': ['open', 'close', 'high', 'low', 'volume'], 'func': f32_divd_529_wyckoff_climactic_vol_indicator_d1}, 'f32_divd_530_wyckoff_upthrust_indicator_d1': {'inputs': ['open', 'close', 'high', 'low', 'volume'], 'func': f32_divd_530_wyckoff_upthrust_indicator_d1}, 'f32_divd_531_wyckoff_no_demand_bar_indicator_d1': {'inputs': ['open', 'close', 'high', 'low', 'volume'], 'func': f32_divd_531_wyckoff_no_demand_bar_indicator_d1}, 'f32_divd_532_wyckoff_no_supply_bar_indicator_d1': {'inputs': ['open', 'close', 'high', 'low', 'volume'], 'func': f32_divd_532_wyckoff_no_supply_bar_indicator_d1}, 'f32_divd_533_wyckoff_effort_minus_result_zscore_252d_d1': {'inputs': ['open', 'close', 'volume'], 'func': f32_divd_533_wyckoff_effort_minus_result_zscore_252d_d1}, 'f32_divd_534_wyckoff_cumulative_vol_div_price_252d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_534_wyckoff_cumulative_vol_div_price_252d_d1}, 'f32_divd_535_wyckoff_days_since_last_upthrust_d1': {'inputs': ['open', 'close', 'high', 'low', 'volume'], 'func': f32_divd_535_wyckoff_days_since_last_upthrust_d1}, 'f32_divd_536_wyckoff_upthrust_count_252d_d1': {'inputs': ['open', 'close', 'high', 'low', 'volume'], 'func': f32_divd_536_wyckoff_upthrust_count_252d_d1}, 'f32_divd_537_wyckoff_climactic_vol_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low', 'volume'], 'func': f32_divd_537_wyckoff_climactic_vol_at_252d_high_indicator_d1}, 'f32_divd_538_wyckoff_no_demand_bar_count_252d_d1': {'inputs': ['open', 'close', 'high', 'low', 'volume'], 'func': f32_divd_538_wyckoff_no_demand_bar_count_252d_d1}, 'f32_divd_539_wyckoff_high_effort_low_result_count_63d_d1': {'inputs': ['open', 'close', 'volume'], 'func': f32_divd_539_wyckoff_high_effort_low_result_count_63d_d1}, 'f32_divd_540_wyckoff_upthrust_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low', 'volume'], 'func': f32_divd_540_wyckoff_upthrust_at_252d_high_indicator_d1}, 'f32_divd_541_rolling_skew_returns_21d_d1': {'inputs': ['close'], 'func': f32_divd_541_rolling_skew_returns_21d_d1}, 'f32_divd_542_rolling_skew_returns_63d_d1': {'inputs': ['close'], 'func': f32_divd_542_rolling_skew_returns_63d_d1}, 'f32_divd_543_rolling_skew_returns_252d_d1': {'inputs': ['close'], 'func': f32_divd_543_rolling_skew_returns_252d_d1}, 'f32_divd_544_rolling_kurt_returns_21d_d1': {'inputs': ['close'], 'func': f32_divd_544_rolling_kurt_returns_21d_d1}, 'f32_divd_545_rolling_kurt_returns_63d_d1': {'inputs': ['close'], 'func': f32_divd_545_rolling_kurt_returns_63d_d1}, 'f32_divd_546_rolling_kurt_returns_252d_d1': {'inputs': ['close'], 'func': f32_divd_546_rolling_kurt_returns_252d_d1}, 'f32_divd_547_skew_returns_change_21d_d1': {'inputs': ['close'], 'func': f32_divd_547_skew_returns_change_21d_d1}, 'f32_divd_548_kurt_returns_change_21d_d1': {'inputs': ['close'], 'func': f32_divd_548_kurt_returns_change_21d_d1}, 'f32_divd_549_skew_flipped_negative_event_indicator_d1': {'inputs': ['close'], 'func': f32_divd_549_skew_flipped_negative_event_indicator_d1}, 'f32_divd_550_kurt_above_3_indicator_d1': {'inputs': ['close'], 'func': f32_divd_550_kurt_above_3_indicator_d1}, 'f32_divd_551_skew_div_with_price_slope_sign_63d_d1': {'inputs': ['close'], 'func': f32_divd_551_skew_div_with_price_slope_sign_63d_d1}, 'f32_divd_552_kurt_div_with_price_slope_sign_63d_d1': {'inputs': ['close'], 'func': f32_divd_552_kurt_div_with_price_slope_sign_63d_d1}, 'f32_divd_553_skew_zscore_252d_d1': {'inputs': ['close'], 'func': f32_divd_553_skew_zscore_252d_d1}, 'f32_divd_554_kurt_zscore_252d_d1': {'inputs': ['close'], 'func': f32_divd_554_kurt_zscore_252d_d1}, 'f32_divd_555_negative_skew_at_252d_high_indicator_d1': {'inputs': ['close'], 'func': f32_divd_555_negative_skew_at_252d_high_indicator_d1}, 'f32_divd_556_vortex_pos_14d_value_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_556_vortex_pos_14d_value_d1}, 'f32_divd_557_vortex_neg_14d_value_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_557_vortex_neg_14d_value_d1}, 'f32_divd_558_vortex_gap_pos_minus_neg_14d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_558_vortex_gap_pos_minus_neg_14d_d1}, 'f32_divd_559_vortex_pos_above_neg_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_559_vortex_pos_above_neg_indicator_d1}, 'f32_divd_560_vortex_bearish_cross_event_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_560_vortex_bearish_cross_event_indicator_d1}, 'f32_divd_561_days_since_vortex_bearish_cross_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_561_days_since_vortex_bearish_cross_d1}, 'f32_divd_562_vortex_pos_zscore_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_562_vortex_pos_zscore_252d_d1}, 'f32_divd_563_vortex_neg_zscore_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_563_vortex_neg_zscore_252d_d1}, 'f32_divd_564_vortex_cross_count_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_564_vortex_cross_count_252d_d1}, 'f32_divd_565_vortex_neg_above_one_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_565_vortex_neg_above_one_indicator_d1}, 'f32_divd_566_vortex_pos_below_0_8_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_566_vortex_pos_below_0_8_indicator_d1}, 'f32_divd_567_vortex_bearish_cross_at_252d_high_indicator_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_567_vortex_bearish_cross_at_252d_high_indicator_d1}, 'f32_divd_568_vortex_pos_slope_div_sign_63d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_568_vortex_pos_slope_div_sign_63d_d1}, 'f32_divd_569_vortex_gap_zscore_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_569_vortex_gap_zscore_252d_d1}, 'f32_divd_570_vortex_pos_above_one_persistence_21d_d1': {'inputs': ['high', 'low', 'close'], 'func': f32_divd_570_vortex_pos_above_one_persistence_21d_d1}, 'f32_divd_571_up_day_pct_21d_d1': {'inputs': ['close'], 'func': f32_divd_571_up_day_pct_21d_d1}, 'f32_divd_572_up_day_pct_63d_d1': {'inputs': ['close'], 'func': f32_divd_572_up_day_pct_63d_d1}, 'f32_divd_573_up_day_pct_252d_d1': {'inputs': ['close'], 'func': f32_divd_573_up_day_pct_252d_d1}, 'f32_divd_574_down_day_pct_63d_d1': {'inputs': ['close'], 'func': f32_divd_574_down_day_pct_63d_d1}, 'f32_divd_575_up_minus_down_day_pct_63d_d1': {'inputs': ['close'], 'func': f32_divd_575_up_minus_down_day_pct_63d_d1}, 'f32_divd_576_up_day_vol_sum_div_down_day_vol_sum_21d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_576_up_day_vol_sum_div_down_day_vol_sum_21d_d1}, 'f32_divd_577_up_day_vol_sum_div_down_day_vol_sum_63d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_577_up_day_vol_sum_div_down_day_vol_sum_63d_d1}, 'f32_divd_578_up_day_vol_sum_div_down_day_vol_sum_252d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_578_up_day_vol_sum_div_down_day_vol_sum_252d_d1}, 'f32_divd_579_down_day_vol_zscore_252d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_579_down_day_vol_zscore_252d_d1}, 'f32_divd_580_up_day_avg_return_63d_d1': {'inputs': ['close'], 'func': f32_divd_580_up_day_avg_return_63d_d1}, 'f32_divd_581_down_day_avg_return_63d_d1': {'inputs': ['close'], 'func': f32_divd_581_down_day_avg_return_63d_d1}, 'f32_divd_582_return_asymmetry_63d_d1': {'inputs': ['close'], 'func': f32_divd_582_return_asymmetry_63d_d1}, 'f32_divd_583_up_day_streak_current_d1': {'inputs': ['close'], 'func': f32_divd_583_up_day_streak_current_d1}, 'f32_divd_584_down_day_streak_current_d1': {'inputs': ['close'], 'func': f32_divd_584_down_day_streak_current_d1}, 'f32_divd_585_up_day_pct_252d_at_252d_high_indicator_d1': {'inputs': ['close'], 'func': f32_divd_585_up_day_pct_252d_at_252d_high_indicator_d1}, 'f32_divd_586_ravi_value_d1': {'inputs': ['close'], 'func': f32_divd_586_ravi_value_d1}, 'f32_divd_587_ravi_above_3_indicator_d1': {'inputs': ['close'], 'func': f32_divd_587_ravi_above_3_indicator_d1}, 'f32_divd_588_ravi_zscore_252d_d1': {'inputs': ['close'], 'func': f32_divd_588_ravi_zscore_252d_d1}, 'f32_divd_589_ravi_slope_21d_d1': {'inputs': ['close'], 'func': f32_divd_589_ravi_slope_21d_d1}, 'f32_divd_590_ravi_above_3_persistence_21d_d1': {'inputs': ['close'], 'func': f32_divd_590_ravi_above_3_persistence_21d_d1}, 'f32_divd_591_mass_index_value_d1': {'inputs': ['high', 'low'], 'func': f32_divd_591_mass_index_value_d1}, 'f32_divd_592_mass_index_above_27_indicator_d1': {'inputs': ['high', 'low'], 'func': f32_divd_592_mass_index_above_27_indicator_d1}, 'f32_divd_593_mass_index_slope_21d_d1': {'inputs': ['high', 'low'], 'func': f32_divd_593_mass_index_slope_21d_d1}, 'f32_divd_594_days_since_mass_index_above_27_d1': {'inputs': ['high', 'low'], 'func': f32_divd_594_days_since_mass_index_above_27_d1}, 'f32_divd_595_mass_index_above_27_count_252d_d1': {'inputs': ['high', 'low'], 'func': f32_divd_595_mass_index_above_27_count_252d_d1}, 'f32_divd_596_average_true_volume_21d_zscore_252d_d1': {'inputs': ['volume'], 'func': f32_divd_596_average_true_volume_21d_zscore_252d_d1}, 'f32_divd_597_average_true_volume_slope_21d_d1': {'inputs': ['volume'], 'func': f32_divd_597_average_true_volume_slope_21d_d1}, 'f32_divd_598_average_true_volume_at_252d_high_indicator_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_598_average_true_volume_at_252d_high_indicator_d1}, 'f32_divd_599_average_true_volume_div_with_price_slope_sign_63d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_599_average_true_volume_div_with_price_slope_sign_63d_d1}, 'f32_divd_600_average_true_volume_decay_event_indicator_d1': {'inputs': ['volume'], 'func': f32_divd_600_average_true_volume_decay_event_indicator_d1}}