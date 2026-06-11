"""multi_condition_blowoff_detectors d2 076-150 - 1b-technical."""
import numpy as np
import pandas as pd

YDAYS = 252; QDAYS = 63; MDAYS = 21; WDAYS = 5
DDAYS_2Y = 504; DDAYS_3Y = 756; DDAYS_5Y = 1260


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
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum(); den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _sma(s, n, mp=None):
    if mp is None: mp = max(n // 3, 2)
    return s.rolling(n, min_periods=mp).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _log_ret(close):
    return _safe_log(close).diff()


def _rolling_q(s, n, q, min_periods=None):
    if min_periods is None: min_periods = max(n // 3, 10)
    return s.rolling(n, min_periods=min_periods).quantile(q)


def _bars_since_last_event(ind):
    arr = ind.values; nb = len(arr); out = np.full(nb, np.nan, dtype=float); last = -1
    for i in range(nb):
        if not np.isnan(arr[i]) and arr[i] > 0.5:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=ind.index)


def _rsi(close, n=14):
    d = close.diff()
    up = d.clip(lower=0.0); dn = (-d).clip(lower=0.0)
    a = up.ewm(alpha=1.0/n, adjust=False, min_periods=n).mean()
    b = dn.ewm(alpha=1.0/n, adjust=False, min_periods=n).mean().replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + a / b)


def _obv(close, volume):
    return (np.sign(close.diff()).fillna(0.0) * volume).cumsum()


def _macd(close, fast=12, slow=26):
    return _ema(close, fast) - _ema(close, slow)


def f57_mcbd_076_post252h_count_lower_closes_21d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """After 252d high, count of lower-close bars in last 21d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    lower = (close < close.shift(1)).astype(float)
    in_win = (bars_since <= MDAYS).astype(float)
    return ((lower * in_win).rolling(MDAYS, min_periods=10).sum()).diff().diff()

def f57_mcbd_077_post252h_count_down_volume_days_21d_d2(open: pd.Series, close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """After 252d high, count of (close<open, vol>avg) bars in 21d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    dv = ((close < open) & (volume > v_avg)).astype(float)
    iw = (bars_since <= MDAYS).astype(float)
    return ((dv * iw).rolling(MDAYS, min_periods=10).sum()).diff().diff()

def f57_mcbd_078_post252h_max_drawdown_21d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Max drawdown from most recent 252d high within last 21 bars."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    pc = close.where(at_max > 0.5).ffill()
    dd = _safe_div(close - pc, pc)
    iw = (bars_since <= MDAYS).astype(float)
    return ((dd * iw).rolling(MDAYS, min_periods=10).min()).diff().diff()

def f57_mcbd_079_post252h_max_drawdown_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Max drawdown from most recent 252d high within last 63 bars."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    pc = close.where(at_max > 0.5).ffill()
    dd = _safe_div(close - pc, pc)
    return (dd.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff()

def f57_mcbd_080_post252h_vol_z_change_from_high_d2(volume: pd.Series, high: pd.Series) -> pd.Series:
    """Change in vol z from at-high to current."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS)
    vz_h = vz.where(at_max > 0.5).ffill()
    return (vz - vz_h).diff().diff()

def f57_mcbd_081_post252h_atr_z_change_from_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Change in ATR-z from at-high to current."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close); z = _rolling_zscore(atr_n, YDAYS)
    z_h = z.where(at_max > 0.5).ffill()
    return (z - z_h).diff().diff()

def f57_mcbd_082_post252h_rsi_change_from_high_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Change in RSI from at-high bar to current."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    rsi = _rsi(close, 14); rsi_h = rsi.where(at_max > 0.5).ffill()
    return (rsi - rsi_h).diff().diff()

def f57_mcbd_083_post252h_close_below_at_high_close_indicator_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close < close at most-recent 252d high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    ch = close.where(at_max > 0.5).ffill()
    return ((close < ch).astype(float).where(ch.notna(), np.nan)).diff().diff()

def f57_mcbd_084_post252h_5pct_loss_indicator_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars-since-252h>0 AND close < at-high * 0.95."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    ch = close.where(at_max > 0.5).ffill()
    return (((bars_since > 0) & (close < ch * 0.95)).astype(float).where(ch.notna(), np.nan)).diff().diff()

def f57_mcbd_085_post252h_10pct_loss_indicator_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars-since-252h>0 AND close < at-high * 0.90."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    ch = close.where(at_max > 0.5).ffill()
    return (((bars_since > 0) & (close < ch * 0.90)).astype(float).where(ch.notna(), np.nan)).diff().diff()

def f57_mcbd_086_post252h_recovery_failure_21d_indicator_d2(high: pd.Series) -> pd.Series:
    """21d post-252h: max-21d-high < 0.98 * at-high (failed retest)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    hh = high.where(at_max > 0.5).ffill(); h21 = high.rolling(MDAYS, min_periods=10).max()
    return (((bars_since >= MDAYS) & (h21 < hh * 0.98)).astype(float).where(hh.notna(), np.nan)).diff().diff()

def f57_mcbd_087_post252h_recovery_failure_63d_indicator_d2(high: pd.Series) -> pd.Series:
    """63d post-252h: max-63d-high < 0.95 * at-high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    hh = high.where(at_max > 0.5).ffill(); h63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    return (((bars_since >= QDAYS) & (h63 < hh * 0.95)).astype(float).where(hh.notna(), np.nan)).diff().diff()

def f57_mcbd_088_post252h_breakdown_below_sma50_21d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Within 21d post-252h, close<SMA50."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    sma50 = _sma(close, 50)
    return (((bars_since > 0) & (bars_since <= MDAYS) & (close < sma50)).astype(float).where(sma50.notna(), np.nan)).diff().diff()

def f57_mcbd_089_post252h_breakdown_below_sma200_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Within 63d post-252h, close<SMA200."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    sma200 = _sma(close, 200)
    return (((bars_since > 0) & (bars_since <= QDAYS) & (close < sma200)).astype(float).where(sma200.notna(), np.nan)).diff().diff()

def f57_mcbd_090_post252h_first5_avg_lower_close_count_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of lower-close bars in first 5 bars after a 252d high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); at_max = (high >= rmax - 1e-12).astype(float)
    bars_since = _bars_since_last_event(at_max)
    lower = (close < close.shift(1)).astype(float)
    in_win = ((bars_since >= 0) & (bars_since <= WDAYS)).astype(float)
    return ((lower * in_win).rolling(WDAYS, min_periods=1).sum()).diff().diff()

def f57_mcbd_091_close_below_sma50_first_after_252h_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close<SMA50 (cross down) AND most-recent 252h within 21d."""
    sma50 = _sma(close, 50); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    am = (high >= rmax - 1e-12).astype(float); bs = _bars_since_last_event(am)
    cd = (close < sma50) & (close.shift(1) >= sma50.shift(1))
    return ((cd & (bs <= MDAYS)).astype(float).where(sma50.notna(), np.nan)).diff().diff()

def f57_mcbd_092_close_below_sma200_first_after_252h_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close<SMA200 (cross down) within 63d of 252h."""
    sma200 = _sma(close, 200); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    am = (high >= rmax - 1e-12).astype(float); bs = _bars_since_last_event(am)
    cd = (close < sma200) & (close.shift(1) >= sma200.shift(1))
    return ((cd & (bs <= QDAYS)).astype(float).where(sma200.notna(), np.nan)).diff().diff()

def f57_mcbd_093_ema9_below_ema21_at_252h_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """EMA9 crosses below EMA21 AND at 252d high."""
    e9 = _ema(close, 9); e21 = _ema(close, 21); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((e9 < e21) & (e9.shift(1) >= e21.shift(1)) & (high >= rmax - 1e-12)).astype(float).where(e21.notna(), np.nan)).diff().diff()

def f57_mcbd_094_death_cross_sma_within_63d_of_252h_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Death cross (SMA50<SMA200) within 63d after a 252h."""
    sma50 = _sma(close, 50); sma200 = _sma(close, 200)
    d = (sma50 < sma200) & (sma50.shift(1) >= sma200.shift(1))
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    am = (high >= rmax - 1e-12).astype(float); bs = _bars_since_last_event(am)
    return ((d & (bs <= QDAYS)).astype(float).where(sma200.notna() & bs.notna(), np.nan)).diff().diff()

def f57_mcbd_095_below_all_8_sma_ribbon_after_252h_63d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Close below all 8 SMA ribbon MAs (10..200) AND 252h within 63d."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]; mas = pd.concat([_sma(close, n).rename(i) for i, n in enumerate(lens)], axis=1)
    ba = (mas.gt(close, axis=0)).all(axis=1)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); am = (high >= rmax - 1e-12).astype(float); bs = _bars_since_last_event(am)
    return ((ba & (bs <= QDAYS)).astype(float).where(mas.notna().all(axis=1) & bs.notna(), np.nan)).diff().diff()

def f57_mcbd_096_ribbon_compression_then_bearish_expansion_d2(close: pd.Series) -> pd.Series:
    """Bar t-21: 8-SMA width<252d-q10; bar t: width>2x prior AND short<long (fan down)."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]; mas = pd.concat([_sma(close, n).rename(i) for i, n in enumerate(lens)], axis=1)
    w = (mas.max(axis=1) - mas.min(axis=1)) / close.replace(0, np.nan)
    p10 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    c = w.shift(MDAYS) < p10.shift(MDAYS); ex = w > 2.0 * w.shift(MDAYS)
    fd = mas.iloc[:, 0] < mas.iloc[:, -1]
    return ((c & ex & fd).astype(float).where(p10.notna(), np.nan)).diff().diff()

def f57_mcbd_097_ema_full_bearish_stack_9_21_55_200_d2(close: pd.Series) -> pd.Series:
    """EMA9<21<55<200 (full bearish stack)."""
    e9 = _ema(close, 9); e21 = _ema(close, 21); e55 = _ema(close, 55); e200 = _ema(close, 200)
    return (((e9 < e21) & (e21 < e55) & (e55 < e200)).astype(float).where(e200.notna(), np.nan)).diff().diff()

def f57_mcbd_098_bull_to_bear_stack_flip_21d_d2(close: pd.Series) -> pd.Series:
    """21d ago: bullish 8-SMA stack; now: bearish 8-SMA stack."""
    lens = [10, 20, 30, 50, 80, 100, 150, 200]; mas = pd.concat([_sma(close, n).rename(i) for i, n in enumerate(lens)], axis=1)
    di = mas.diff(axis=1).iloc[:, 1:]
    bull = (di.lt(0)).all(axis=1).astype(float); bear = (di.gt(0)).all(axis=1).astype(float)
    return (((bull.shift(MDAYS) > 0.5) & (bear > 0.5)).astype(float).where(di.notna().all(axis=1), np.nan)).diff().diff()

def f57_mcbd_099_close_breaks_atr_trailing_stop_at_high_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close < (max-close-21d - 3*ATR21) AND high made 252h within 5 bars."""
    hh = close.rolling(MDAYS, min_periods=10).max(); atr = _atr(high, low, close, MDAYS)
    stop = hh - 3.0 * atr
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rm = (high >= rmax - 1e-12).rolling(WDAYS, min_periods=1).max()
    return (((close < stop) & (rm > 0.5)).astype(float).where(stop.notna(), np.nan)).diff().diff()

def f57_mcbd_100_close_breaks_donchian20_lower_at_high_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close<20d low AND high was 252h within 5 bars."""
    l20 = low.shift(1).rolling(20, min_periods=10).min(); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rm = (high >= rmax - 1e-12).rolling(WDAYS, min_periods=1).max()
    return (((close < l20) & (rm > 0.5)).astype(float).where(l20.notna(), np.nan)).diff().diff()

def f57_mcbd_101_close_breaks_supertrend_proxy_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close < (mid - 3*ATR10) AND within 5% of 252d max."""
    atr = _atr(high, low, close, 10); med = (high + low) / 2.0; stop = med - 3.0 * atr
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((close < stop) & (close >= 0.95 * rmax)).astype(float).where(stop.notna(), np.nan)).diff().diff()

def f57_mcbd_102_psar_flip_bearish_proxy_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close < (max-high-21d - 2*ATR21) AND was above 1 bar ago."""
    hh = high.rolling(MDAYS, min_periods=10).max(); atr = _atr(high, low, close, MDAYS); stop = hh - 2.0 * atr
    return (((close < stop) & (close.shift(1) >= stop.shift(1))).astype(float).where(stop.notna(), np.nan)).diff().diff()

def f57_mcbd_103_close_below_anchored_vwap_from_252h_d2(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Close < anchored VWAP from most-recent 252d high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); am = (high >= rmax - 1e-12).astype(float)
    tp = (high + low + close) / 3.0; tpv = tp * volume
    aid = am.cumsum()
    num = tpv.groupby(aid).cumsum(); den = volume.groupby(aid).cumsum()
    vwap = num / den.replace(0, np.nan)
    return ((close < vwap).astype(float).where(vwap.notna(), np.nan)).diff().diff()

def f57_mcbd_104_close_below_50pct_fib_retracement_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close < 50% Fib from 252d high to 252d low."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = rmax - 0.5 * (rmax - rmin)
    return ((close < fib).astype(float).where(fib.notna(), np.nan)).diff().diff()

def f57_mcbd_105_close_below_618_fib_retracement_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close < 61.8% Fib retracement (deep retracement = topping confirmed)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    fib = rmax - 0.618 * (rmax - rmin)
    return ((close < fib).astype(float).where(fib.notna(), np.nan)).diff().diff()

def f57_mcbd_106_price_vs_vol_divergence_3bar_at_high_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """3 bars: close>prev close AND vol<prev vol AND at 252h."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ud = ((close > close.shift(1)) & (volume < volume.shift(1)) & (high >= rmax - 1e-12)).astype(float)
    return (((ud.shift(2) > 0.5) & (ud.shift(1) > 0.5) & (ud > 0.5)).astype(float).where(rmax.notna(), np.nan)).diff().diff()

def f57_mcbd_107_close_vs_obv_accel_div_at_high_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """Close-21d-pct>0 AND OBV-21d-pct<0 AND at 252h."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    obv = _obv(close, volume)
    p21 = close.pct_change(MDAYS); o21 = obv.pct_change(MDAYS)
    return (((p21 > 0) & (o21 < 0) & (high >= rmax - 1e-12)).astype(float).where(p21.notna() & o21.notna(), np.nan)).diff().diff()

def f57_mcbd_108_close_inverse_atr_at_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close in 252d top decile AND ATR-N in 252d bottom quartile (complacency at top)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pr = _safe_div(close - rmin, rmax - rmin); atr_n = _safe_div(_atr(high, low, close, MDAYS), close)
    q25 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (((pr > 0.9) & (atr_n < q25)).astype(float).where(pr.notna() & q25.notna(), np.nan)).diff().diff()

def f57_mcbd_109_price_z_div_volume_z_count_252d_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """Count of bars in 252d with close-z>1.5 AND vol-z<-0.5 AND at 252h."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    zc = _rolling_zscore(_safe_log(close), YDAYS); zv = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS)
    ind = ((zc > 1.5) & (zv < -0.5) & (high >= rmax - 1e-12)).astype(float)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f57_mcbd_110_intraday_range_top_decile_close_flat_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range/close top decile 252d AND |close-prev|/close<0.5% (churn at top)."""
    rng_n = (high - low) / close.replace(0, np.nan); p90 = rng_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    flat = (close - close.shift(1)).abs() / close.replace(0, np.nan) < 0.005
    return (((rng_n > p90) & flat).astype(float).where(p90.notna(), np.nan)).diff().diff()

def f57_mcbd_111_multi_modal_z_sum_above_3_count_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 252d bars where (zc-zobv) + (zc-zmacd) > 3."""
    zc = _rolling_zscore(_safe_log(close), YDAYS)
    obv = _obv(close, volume); zo = _rolling_zscore(obv, YDAYS)
    macd = _macd(close); zm = _rolling_zscore(macd, YDAYS)
    gap = (zc - zo) + (zc - zm)
    return ((gap > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f57_mcbd_112_intraday_close_below_open_streak_4_at_high_d2(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """4 consecutive bars close<open AND each at 252h (relentless intraday selling at top)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    da = ((close < open) & (high >= 0.98 * rmax)).astype(float)
    return (((da.shift(3) > 0.5) & (da.shift(2) > 0.5) & (da.shift(1) > 0.5) & (da > 0.5)).astype(float).where(rmax.notna(), np.nan)).diff().diff()

def f57_mcbd_113_intraday_close_pos_below_30_5bar_at_high_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar avg close-pos<30% AND close in 252d top decile (sustained intraday distribution)."""
    pos = (close - low) / (high - low).replace(0, np.nan); a5 = pos.rolling(WDAYS, min_periods=3).mean()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    pr = _safe_div(close - rmin, rmax - rmin)
    return (((a5 < 0.30) & (pr > 0.9)).astype(float).where(a5.notna() & pr.notna(), np.nan)).diff().diff()

def f57_mcbd_114_price_new_high_obv_not_new_high_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close=252d max AND OBV<its 252d max."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); obv = _obv(close, volume); om = obv.rolling(YDAYS, min_periods=QDAYS).max()
    return (((close >= rmax - 1e-12) & (obv < om - 1e-9)).astype(float).where(obv.notna(), np.nan)).diff().diff()

def f57_mcbd_115_price_new_high_rsi_not_new_high_252d_d2(close: pd.Series) -> pd.Series:
    """Close=252d max AND RSI<its 252d max."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); rsi = _rsi(close, 14); rm = rsi.rolling(YDAYS, min_periods=QDAYS).max()
    return (((close >= rmax - 1e-12) & (rsi < rm - 1e-9)).astype(float).where(rsi.notna(), np.nan)).diff().diff()

def f57_mcbd_116_price_new_high_macd_not_new_high_252d_d2(close: pd.Series) -> pd.Series:
    """Close=252d max AND MACD<its 252d max."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); macd = _macd(close); mm = macd.rolling(YDAYS, min_periods=QDAYS).max()
    return (((close >= rmax - 1e-12) & (macd < mm - 1e-9)).astype(float).where(macd.notna(), np.nan)).diff().diff()

def f57_mcbd_117_triple_non_confirmation_at_252h_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close=252d max AND OBV NOT new high AND RSI NOT new high AND MACD NOT new high."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    obv = _obv(close, volume); om = obv.rolling(YDAYS, min_periods=QDAYS).max()
    rsi = _rsi(close, 14); rm = rsi.rolling(YDAYS, min_periods=QDAYS).max()
    macd = _macd(close); mm = macd.rolling(YDAYS, min_periods=QDAYS).max()
    return (((close >= rmax - 1e-12) & (obv < om - 1e-9) & (rsi < rm - 1e-9) & (macd < mm - 1e-9)).astype(float).where(rsi.notna() & macd.notna(), np.nan)).diff().diff()

def f57_mcbd_118_close_2y_high_3of3_extension_d2(close: pd.Series) -> pd.Series:
    """Close=504d max AND close/SMA200>1.5 AND close/SMA50>1.15 AND close/SMA20>1.05."""
    r2 = close.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    r200 = _safe_div(close, _sma(close, 200)); r50 = _safe_div(close, _sma(close, 50)); r20 = _safe_div(close, _sma(close, 20))
    return (((close >= r2 - 1e-12) & (r200 > 1.5) & (r50 > 1.15) & (r20 > 1.05)).astype(float).where(r200.notna() & r50.notna() & r20.notna(), np.nan)).diff().diff()

def f57_mcbd_119_vol_z_3_dollar_vol_z_3_close_below_open_d2(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-z>3 AND $-vol-z>3 AND close<open (huge size distribution day)."""
    vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS); dvz = _rolling_zscore(_safe_log((close * volume).replace(0, np.nan)), YDAYS)
    return (((vz > 3.0) & (dvz > 3.0) & (close < open)).astype(float).where(vz.notna() & dvz.notna(), np.nan)).diff().diff()

def f57_mcbd_120_vol_2x_intraday_recovery_d2(open: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol>2x avg AND (low/open)<-3% AND (close/open)>-0.5% (absorption day)."""
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    il = _safe_div(low - open, open); ic = _safe_div(close - open, open)
    return (((volume > 2.0 * v_avg) & (il < -0.03) & (ic > -0.005)).astype(float).where(v_avg.notna(), np.nan)).diff().diff()

def f57_mcbd_121_vol_compression_then_5sigma_spike_at_high_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """Bar t-21: log-vol z<-1; bar t: z>5; both near 252d max."""
    vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS)
    comp = vz.shift(MDAYS) < -1.0; spike = vz > 5.0
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((comp & spike & (close >= 0.95 * rmax)).astype(float).where(vz.notna(), np.nan)).diff().diff()

def f57_mcbd_122_vol_max_252d_at_252h_d2(volume: pd.Series, high: pd.Series) -> pd.Series:
    """Volume=252d max AND high=252d max."""
    rh = high.rolling(YDAYS, min_periods=QDAYS).max(); rv = volume.rolling(YDAYS, min_periods=QDAYS).max()
    return (((volume >= rv - 1) & (high >= rh - 1e-12)).astype(float).where(rh.notna() & rv.notna(), np.nan)).diff().diff()

def f57_mcbd_123_vol_top_quintile_3of5_at_high_d2(volume: pd.Series, high: pd.Series) -> pd.Series:
    """3 of last 5 bars vol in 252d top quintile AND near 252h."""
    vp80 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.80); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    hv = (volume > vp80).astype(float); rh = (high >= 0.98 * rmax)
    return (((hv.rolling(WDAYS, min_periods=3).sum() >= 3) & rh).astype(float).where(vp80.notna() & rmax.notna(), np.nan)).diff().diff()

def f57_mcbd_124_vol_alternation_high_low_5bars_at_high_d2(volume: pd.Series, high: pd.Series) -> pd.Series:
    """Vol alternation H-L-H-L-H pattern AND near 252h."""
    v_avg = volume.rolling(MDAYS, min_periods=10).mean(); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    hi = (volume > v_avg).astype(float)
    return (((hi.shift(4) > 0.5) & (hi.shift(3) < 0.5) & (hi.shift(2) > 0.5) & (hi.shift(1) < 0.5) & (hi > 0.5) & (high >= 0.95 * rmax)).astype(float).where(v_avg.notna(), np.nan)).diff().diff()

def f57_mcbd_125_vol_skew_above_2_at_252h_d2(volume: pd.Series, high: pd.Series) -> pd.Series:
    """21d skew of log-vol>2 AND at 252h."""
    lv = _safe_log(volume.replace(0, np.nan)); sk = lv.rolling(MDAYS, min_periods=10).skew()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((sk > 2.0) & (high >= rmax - 1e-12)).astype(float).where(sk.notna(), np.nan)).diff().diff()

def f57_mcbd_126_vol_pareto_alpha_below_2_at_252h_d2(volume: pd.Series, high: pd.Series) -> pd.Series:
    """Hill alpha (top 10% vol over 252d)<2 AND at 252h."""
    lv = _safe_log(volume.replace(0, np.nan))
    def _hill(w):
        v = w[~np.isnan(w)]
        if v.size < 30: return np.nan
        v = np.sort(v); k = max(int(0.10 * v.size), 5)
        if k >= v.size: return np.nan
        thr = v[v.size - k - 1]; tail = v[v.size - k:]
        if thr <= 0: return np.nan
        return float(1.0 / np.mean(np.log(tail / thr)))
    alpha = lv.rolling(YDAYS, min_periods=QDAYS).apply(_hill, raw=True)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((alpha < 2.0) & (high >= rmax - 1e-12)).astype(float).where(alpha.notna(), np.nan)).diff().diff()

def f57_mcbd_127_atr_3consecutive_top_decile_at_252h_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """3 consecutive bars ATR-N in 252d top decile AND at 252h."""
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close); p90 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); ha = (atr_n > p90).astype(float)
    return (((ha.shift(2) > 0.5) & (ha.shift(1) > 0.5) & (ha > 0.5) & (high >= 0.95 * rmax)).astype(float).where(p90.notna() & rmax.notna(), np.nan)).diff().diff()

def f57_mcbd_128_realized_skew_negative_atr_compression_at_252h_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d realized skew<0 AND ATR-N bottom quartile AND at 252h."""
    r = _log_ret(close); sk = r.rolling(QDAYS, min_periods=MDAYS).skew()
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close); q25 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((sk < 0) & (atr_n < q25) & (high >= rmax - 1e-12)).astype(float).where(sk.notna() & q25.notna(), np.nan)).diff().diff()

def f57_mcbd_129_realized_kurt_above_5_at_252h_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """63d excess-kurt>5 AND at 252h (heavy-tail at top)."""
    r = _log_ret(close); kt = r.rolling(QDAYS, min_periods=MDAYS).kurt()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((kt > 5.0) & (high >= rmax - 1e-12)).astype(float).where(kt.notna(), np.nan)).diff().diff()

def f57_mcbd_130_var95_exceeded_at_252h_within_5d_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Single-bar loss>252d-VaR95 AND high made 252h within 5 bars."""
    r = _log_ret(close); v95 = -_rolling_q(r, YDAYS, 0.05)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rh = (high >= rmax - 1e-12).rolling(WDAYS, min_periods=1).max()
    return (((-r > v95) & (rh > 0.5)).astype(float).where(v95.notna(), np.nan)).diff().diff()

def f57_mcbd_131_vol_persistence_high_at_252h_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """AR1 of |r| 252d>0.4 AND at 252h (sticky clustering at top)."""
    absr = _log_ret(close).abs()
    def _ac(w):
        x = w[~np.isnan(w)]
        if x.size < 20: return np.nan
        a = x[:-1]; b = x[1:]
        if a.std() == 0 or b.std() == 0: return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    ar1 = absr.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((ar1 > 0.4) & (high >= rmax - 1e-12)).astype(float).where(ar1.notna(), np.nan)).diff().diff()

def f57_mcbd_132_vol_clustering_count_2sigma_3_in_21d_at_252h_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of bars in 21d with |r|>2sigma>=3 AND at 252h."""
    r = _log_ret(close); sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    sh = (r.abs() > 2.0 * sd).astype(float); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((sh.rolling(MDAYS, min_periods=10).sum() >= 3) & (high >= rmax - 1e-12)).astype(float).where(sh.notna(), np.nan)).diff().diff()

def f57_mcbd_133_realized_vol_at_252max_at_close_252max_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """21d realized vol=252d max AND close=252d max."""
    r = _log_ret(close); rv = (r ** 2).rolling(MDAYS, min_periods=10).mean()
    rm = rv.rolling(YDAYS, min_periods=QDAYS).max(); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((rv >= rm - 1e-12) & (close >= rmax - 1e-12)).astype(float).where(rm.notna() & rmax.notna(), np.nan)).diff().diff()

def f57_mcbd_134_overnight_gap_z_above_3_at_252h_d2(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """Overnight gap z>3 AND at 252h."""
    on = _safe_log(open) - _safe_log(close.shift(1)); z = _rolling_zscore(on, YDAYS); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((z > 3.0) & (high >= rmax - 1e-12)).astype(float).where(z.notna(), np.nan)).diff().diff()

def f57_mcbd_135_intraday_swing_above_5pct_at_252h_d2(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(High-low)/open>5% AND high=252d max."""
    sw = (high - low) / open.replace(0, np.nan); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((sw > 0.05) & (high >= rmax - 1e-12)).astype(float).where(sw.notna(), np.nan)).diff().diff()

def f57_mcbd_136_count_3way_warnings_in_252d_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """Count of 252d bars with RSI>70 AND close=252d max AND vol>avg."""
    rsi = _rsi(close, 14); rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    ind = ((rsi > 70.0) & (close >= rmax - 1e-12) & (volume > v_avg)).astype(float)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f57_mcbd_137_count_distribution_days_in_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution days (vol>avg AND close<open AND close bottom 50%) in 252d."""
    v_avg = volume.rolling(MDAYS, min_periods=10).mean(); pos = (close - low) / (high - low).replace(0, np.nan)
    ind = ((volume > v_avg) & (close < open) & (pos < 0.5)).astype(float)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f57_mcbd_138_count_topping_candles_in_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of (shoot-star OR dark-cloud OR bear-engulf) at 252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng
    uw = (high - pd.concat([open, close], axis=1).max(axis=1)) / rng
    shoot = (close < open) & (body < 0.30) & (uw > 0.60)
    egf = (close < open) & (close.shift(1) > open.shift(1)) & (open >= close.shift(1)) & (close <= open.shift(1))
    dc = (close.shift(1) > open.shift(1)) & (open > close.shift(1)) & (close < (open.shift(1) + close.shift(1)) / 2.0)
    top = ((shoot | egf | dc) & (high >= rmax - 1e-12)).astype(float)
    return (top.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f57_mcbd_139_count_bullish_no_demand_in_252d_d2(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """Count of 252d bars with up-close AND vol<0.7avg AND new 21d high."""
    v_avg = volume.rolling(MDAYS, min_periods=10).mean(); h21 = high.rolling(MDAYS, min_periods=10).max()
    ind = ((close > close.shift(1)) & (volume < 0.7 * v_avg) & (high >= h21 - 1e-12)).astype(float)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f57_mcbd_140_count_bearish_high_vol_at_252max_in_252d_d2(open: pd.Series, close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """Count of bars with close<open AND vol>2x avg AND at 252d max in 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    ind = ((close < open) & (volume > 2.0 * v_avg) & (high >= rmax - 1e-12)).astype(float)
    return (ind.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f57_mcbd_141_composite_topping_event_z_score_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(1d-event count across 5 topping conditions) over 252d."""
    rsi = _rsi(close, 14); rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    pos = (close - low) / (high - low).replace(0, np.nan)
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)
    cnt = ((rsi > 70.0).astype(float) + (close >= rmax - 1e-12).astype(float) + (volume > v_avg).astype(float) + (pos < 0.5).astype(float) + (zatr > 1.0).astype(float))
    return (_rolling_zscore(cnt, YDAYS)).diff().diff()

def f57_mcbd_142_days_since_5_topping_conditions_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since last bar with all 5 topping conditions (capped 252)."""
    rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); atr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)
    pos = (close - low) / (high - low).replace(0, np.nan)
    ev = ((rsi > 70.0) & (macd < sig) & (close >= rmax - 1e-12) & (zatr > 1.0) & (pos < 0.5)).astype(float)
    return (_bars_since_last_event(ev).clip(upper=float(YDAYS))).diff().diff()

def f57_mcbd_143_blowoff_signature_cluster_density_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63d with (close top decile AND vol z>1 AND RSI>70)."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max(); rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    pr = _safe_div(close - rmin, rmax - rmin)
    vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS); rsi = _rsi(close, 14)
    ind = ((pr > 0.9) & (vz > 1.0) & (rsi > 70.0)).astype(float).where(pr.notna() & vz.notna() & rsi.notna(), np.nan)
    return (ind.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()

def f57_mcbd_144_count_failed_breakouts_at_252h_in_252d_d2(high: pd.Series) -> pd.Series:
    """Bar t-3 made 252h; bars t-2,t-1,t all made lower highs - PIT-lagged."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ah = (high.shift(3) >= rmax.shift(3) - 1e-12).astype(int)
    fail = ah & (high.shift(2) < high.shift(3)) & (high.shift(1) < high.shift(3)) & (high < high.shift(3))
    return (fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f57_mcbd_145_count_swing_failures_252d_d2(high: pd.Series) -> pd.Series:
    """Count of swing-failure patterns (PIT-lagged) in 252d."""
    h21 = high.rolling(MDAYS, min_periods=10).max()
    mh = (high.shift(WDAYS) >= h21.shift(WDAYS) - 1e-12).astype(int)
    fail = mh & (high.rolling(WDAYS, min_periods=1).max() < high.shift(WDAYS))
    return (fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f57_mcbd_146_triple_top_3_peaks_within_63d_at_similar_d2(high: pd.Series) -> pd.Series:
    """3 distinct pivot-highs within 63d at levels within 1% of each other."""
    p_ph = high.shift(MDAYS // 2).where(high.shift(MDAYS // 2) == high.rolling(MDAYS, min_periods=10).max(), np.nan)
    p_arr = p_ph.values; nb = len(p_arr); out = np.full(nb, np.nan, dtype=float); history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]):
            history.append((t, p_arr[t]))
            recent = [h for h in history if (t - h[0]) <= QDAYS]
            if len(recent) >= 3:
                vals = [h[1] for h in recent[-3:]]
                out[t] = 1.0 if max(vals) - min(vals) < 0.01 * max(vals) else 0.0
            else:
                out[t] = 0.0
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=high.index)
    return (res).diff().diff()

def f57_mcbd_147_rounding_top_signature_252d_d2(close: pd.Series) -> pd.Series:
    """d2(SMA252)<0 AND d1(SMA252)<0 AND price near 252d max."""
    sma = _sma(close, 252); d1 = sma.diff(); d2 = sma.diff().diff()
    return (((d2 < 0) & (d1 < 0) & (close >= 0.95 * close.rolling(YDAYS, min_periods=QDAYS).max())).astype(float).where(d2.notna(), np.nan)).diff().diff()

def f57_mcbd_148_descending_triangle_indicator_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Lower highs 21d AND flat low (range<1%) AND close near flat low."""
    lh = (high < high.shift(WDAYS)) & (high.shift(WDAYS) < high.shift(2 * WDAYS))
    lr = low.rolling(MDAYS, min_periods=10).max() - low.rolling(MDAYS, min_periods=10).min()
    fl = lr / close.replace(0, np.nan) < 0.01
    nl = close < low.rolling(MDAYS, min_periods=10).min() * 1.02
    return ((lh & fl & nl).astype(float).where(fl.notna(), np.nan)).diff().diff()

def f57_mcbd_149_head_shoulders_proxy_3peak_d2(high: pd.Series) -> pd.Series:
    """3 peaks in 63d: middle highest, left/right within 5%."""
    p_ph = high.shift(MDAYS // 2).where(high.shift(MDAYS // 2) == high.rolling(MDAYS, min_periods=10).max(), np.nan)
    p_arr = p_ph.values; nb = len(p_arr); out = np.full(nb, np.nan, dtype=float); history = []
    for t in range(nb):
        if not np.isnan(p_arr[t]):
            history.append((t, p_arr[t]))
            recent = [h for h in history if (t - h[0]) <= QDAYS]
            if len(recent) >= 3:
                l, hp, r = recent[-3][1], recent[-2][1], recent[-1][1]
                out[t] = 1.0 if (hp > l and hp > r and abs(l - r) / max(l, r, 1e-9) < 0.05) else 0.0
            else:
                out[t] = 0.0
        elif t > 0 and not np.isnan(out[t - 1]):
            out[t] = 0.0
    res = pd.Series(out, index=high.index)
    return (res).diff().diff()

def f57_mcbd_150_master_topping_composite_score_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z-sum of: distribution-day-count + non-conf count + bearish-candle count + vol-div days + parabolic-accel days over 252d."""
    v_avg = volume.rolling(MDAYS, min_periods=10).mean(); pos = (close - low) / (high - low).replace(0, np.nan)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = ((volume > v_avg) & (close < open) & (pos < 0.5)).astype(float)
    obv = _obv(close, volume); om = obv.rolling(YDAYS, min_periods=QDAYS).max()
    nc = ((close >= rmax - 1e-12) & (obv < om - 1e-9)).astype(float)
    rng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng
    uw = (high - pd.concat([open, close], axis=1).max(axis=1)) / rng
    ss = ((close < open) & (body < 0.30) & (uw > 0.60) & (high >= rmax - 1e-12)).astype(float)
    vd = ((close > close.shift(1)) & (volume < volume.shift(1)) & (high >= rmax - 1e-12)).astype(float)
    r = _log_ret(close); pa = (r > 0.015).astype(float)
    tot = (dd.rolling(YDAYS, min_periods=QDAYS).sum() + nc.rolling(YDAYS, min_periods=QDAYS).sum() + ss.rolling(YDAYS, min_periods=QDAYS).sum() + vd.rolling(YDAYS, min_periods=QDAYS).sum() + pa.rolling(YDAYS, min_periods=QDAYS).sum())
    return (_rolling_zscore(tot, YDAYS)).diff().diff()


MULTI_CONDITION_BLOWOFF_DETECTORS_D2_REGISTRY_076_150 = {
    "f57_mcbd_076_post252h_count_lower_closes_21d_d2": {"inputs": ["close", "high"], "func": f57_mcbd_076_post252h_count_lower_closes_21d_d2},
    "f57_mcbd_077_post252h_count_down_volume_days_21d_d2": {"inputs": ["open", "close", "volume", "high"], "func": f57_mcbd_077_post252h_count_down_volume_days_21d_d2},
    "f57_mcbd_078_post252h_max_drawdown_21d_d2": {"inputs": ["close", "high"], "func": f57_mcbd_078_post252h_max_drawdown_21d_d2},
    "f57_mcbd_079_post252h_max_drawdown_63d_d2": {"inputs": ["close", "high"], "func": f57_mcbd_079_post252h_max_drawdown_63d_d2},
    "f57_mcbd_080_post252h_vol_z_change_from_high_d2": {"inputs": ["volume", "high"], "func": f57_mcbd_080_post252h_vol_z_change_from_high_d2},
    "f57_mcbd_081_post252h_atr_z_change_from_high_d2": {"inputs": ["high", "low", "close"], "func": f57_mcbd_081_post252h_atr_z_change_from_high_d2},
    "f57_mcbd_082_post252h_rsi_change_from_high_d2": {"inputs": ["close", "high"], "func": f57_mcbd_082_post252h_rsi_change_from_high_d2},
    "f57_mcbd_083_post252h_close_below_at_high_close_indicator_d2": {"inputs": ["close", "high"], "func": f57_mcbd_083_post252h_close_below_at_high_close_indicator_d2},
    "f57_mcbd_084_post252h_5pct_loss_indicator_d2": {"inputs": ["close", "high"], "func": f57_mcbd_084_post252h_5pct_loss_indicator_d2},
    "f57_mcbd_085_post252h_10pct_loss_indicator_d2": {"inputs": ["close", "high"], "func": f57_mcbd_085_post252h_10pct_loss_indicator_d2},
    "f57_mcbd_086_post252h_recovery_failure_21d_indicator_d2": {"inputs": ["high"], "func": f57_mcbd_086_post252h_recovery_failure_21d_indicator_d2},
    "f57_mcbd_087_post252h_recovery_failure_63d_indicator_d2": {"inputs": ["high"], "func": f57_mcbd_087_post252h_recovery_failure_63d_indicator_d2},
    "f57_mcbd_088_post252h_breakdown_below_sma50_21d_d2": {"inputs": ["close", "high"], "func": f57_mcbd_088_post252h_breakdown_below_sma50_21d_d2},
    "f57_mcbd_089_post252h_breakdown_below_sma200_63d_d2": {"inputs": ["close", "high"], "func": f57_mcbd_089_post252h_breakdown_below_sma200_63d_d2},
    "f57_mcbd_090_post252h_first5_avg_lower_close_count_d2": {"inputs": ["close", "high"], "func": f57_mcbd_090_post252h_first5_avg_lower_close_count_d2},
    "f57_mcbd_091_close_below_sma50_first_after_252h_d2": {"inputs": ["close", "high"], "func": f57_mcbd_091_close_below_sma50_first_after_252h_d2},
    "f57_mcbd_092_close_below_sma200_first_after_252h_63d_d2": {"inputs": ["close", "high"], "func": f57_mcbd_092_close_below_sma200_first_after_252h_63d_d2},
    "f57_mcbd_093_ema9_below_ema21_at_252h_d2": {"inputs": ["close", "high"], "func": f57_mcbd_093_ema9_below_ema21_at_252h_d2},
    "f57_mcbd_094_death_cross_sma_within_63d_of_252h_d2": {"inputs": ["close", "high"], "func": f57_mcbd_094_death_cross_sma_within_63d_of_252h_d2},
    "f57_mcbd_095_below_all_8_sma_ribbon_after_252h_63d_d2": {"inputs": ["close", "high"], "func": f57_mcbd_095_below_all_8_sma_ribbon_after_252h_63d_d2},
    "f57_mcbd_096_ribbon_compression_then_bearish_expansion_d2": {"inputs": ["close"], "func": f57_mcbd_096_ribbon_compression_then_bearish_expansion_d2},
    "f57_mcbd_097_ema_full_bearish_stack_9_21_55_200_d2": {"inputs": ["close"], "func": f57_mcbd_097_ema_full_bearish_stack_9_21_55_200_d2},
    "f57_mcbd_098_bull_to_bear_stack_flip_21d_d2": {"inputs": ["close"], "func": f57_mcbd_098_bull_to_bear_stack_flip_21d_d2},
    "f57_mcbd_099_close_breaks_atr_trailing_stop_at_high_d2": {"inputs": ["close", "high", "low"], "func": f57_mcbd_099_close_breaks_atr_trailing_stop_at_high_d2},
    "f57_mcbd_100_close_breaks_donchian20_lower_at_high_d2": {"inputs": ["close", "high", "low"], "func": f57_mcbd_100_close_breaks_donchian20_lower_at_high_d2},
    "f57_mcbd_101_close_breaks_supertrend_proxy_d2": {"inputs": ["close", "high", "low"], "func": f57_mcbd_101_close_breaks_supertrend_proxy_d2},
    "f57_mcbd_102_psar_flip_bearish_proxy_d2": {"inputs": ["close", "high", "low"], "func": f57_mcbd_102_psar_flip_bearish_proxy_d2},
    "f57_mcbd_103_close_below_anchored_vwap_from_252h_d2": {"inputs": ["close", "high", "low", "volume"], "func": f57_mcbd_103_close_below_anchored_vwap_from_252h_d2},
    "f57_mcbd_104_close_below_50pct_fib_retracement_d2": {"inputs": ["close", "high", "low"], "func": f57_mcbd_104_close_below_50pct_fib_retracement_d2},
    "f57_mcbd_105_close_below_618_fib_retracement_d2": {"inputs": ["close", "high", "low"], "func": f57_mcbd_105_close_below_618_fib_retracement_d2},
    "f57_mcbd_106_price_vs_vol_divergence_3bar_at_high_d2": {"inputs": ["close", "volume", "high"], "func": f57_mcbd_106_price_vs_vol_divergence_3bar_at_high_d2},
    "f57_mcbd_107_close_vs_obv_accel_div_at_high_d2": {"inputs": ["close", "volume", "high"], "func": f57_mcbd_107_close_vs_obv_accel_div_at_high_d2},
    "f57_mcbd_108_close_inverse_atr_at_high_d2": {"inputs": ["high", "low", "close"], "func": f57_mcbd_108_close_inverse_atr_at_high_d2},
    "f57_mcbd_109_price_z_div_volume_z_count_252d_d2": {"inputs": ["close", "volume", "high"], "func": f57_mcbd_109_price_z_div_volume_z_count_252d_d2},
    "f57_mcbd_110_intraday_range_top_decile_close_flat_d2": {"inputs": ["high", "low", "close"], "func": f57_mcbd_110_intraday_range_top_decile_close_flat_d2},
    "f57_mcbd_111_multi_modal_z_sum_above_3_count_252d_d2": {"inputs": ["close", "volume"], "func": f57_mcbd_111_multi_modal_z_sum_above_3_count_252d_d2},
    "f57_mcbd_112_intraday_close_below_open_streak_4_at_high_d2": {"inputs": ["open", "close", "high"], "func": f57_mcbd_112_intraday_close_below_open_streak_4_at_high_d2},
    "f57_mcbd_113_intraday_close_pos_below_30_5bar_at_high_d2": {"inputs": ["high", "low", "close"], "func": f57_mcbd_113_intraday_close_pos_below_30_5bar_at_high_d2},
    "f57_mcbd_114_price_new_high_obv_not_new_high_252d_d2": {"inputs": ["close", "volume"], "func": f57_mcbd_114_price_new_high_obv_not_new_high_252d_d2},
    "f57_mcbd_115_price_new_high_rsi_not_new_high_252d_d2": {"inputs": ["close"], "func": f57_mcbd_115_price_new_high_rsi_not_new_high_252d_d2},
    "f57_mcbd_116_price_new_high_macd_not_new_high_252d_d2": {"inputs": ["close"], "func": f57_mcbd_116_price_new_high_macd_not_new_high_252d_d2},
    "f57_mcbd_117_triple_non_confirmation_at_252h_d2": {"inputs": ["close", "volume"], "func": f57_mcbd_117_triple_non_confirmation_at_252h_d2},
    "f57_mcbd_118_close_2y_high_3of3_extension_d2": {"inputs": ["close"], "func": f57_mcbd_118_close_2y_high_3of3_extension_d2},
    "f57_mcbd_119_vol_z_3_dollar_vol_z_3_close_below_open_d2": {"inputs": ["open", "close", "volume"], "func": f57_mcbd_119_vol_z_3_dollar_vol_z_3_close_below_open_d2},
    "f57_mcbd_120_vol_2x_intraday_recovery_d2": {"inputs": ["open", "low", "close", "volume"], "func": f57_mcbd_120_vol_2x_intraday_recovery_d2},
    "f57_mcbd_121_vol_compression_then_5sigma_spike_at_high_d2": {"inputs": ["close", "volume", "high"], "func": f57_mcbd_121_vol_compression_then_5sigma_spike_at_high_d2},
    "f57_mcbd_122_vol_max_252d_at_252h_d2": {"inputs": ["volume", "high"], "func": f57_mcbd_122_vol_max_252d_at_252h_d2},
    "f57_mcbd_123_vol_top_quintile_3of5_at_high_d2": {"inputs": ["volume", "high"], "func": f57_mcbd_123_vol_top_quintile_3of5_at_high_d2},
    "f57_mcbd_124_vol_alternation_high_low_5bars_at_high_d2": {"inputs": ["volume", "high"], "func": f57_mcbd_124_vol_alternation_high_low_5bars_at_high_d2},
    "f57_mcbd_125_vol_skew_above_2_at_252h_d2": {"inputs": ["volume", "high"], "func": f57_mcbd_125_vol_skew_above_2_at_252h_d2},
    "f57_mcbd_126_vol_pareto_alpha_below_2_at_252h_d2": {"inputs": ["volume", "high"], "func": f57_mcbd_126_vol_pareto_alpha_below_2_at_252h_d2},
    "f57_mcbd_127_atr_3consecutive_top_decile_at_252h_d2": {"inputs": ["high", "low", "close"], "func": f57_mcbd_127_atr_3consecutive_top_decile_at_252h_d2},
    "f57_mcbd_128_realized_skew_negative_atr_compression_at_252h_d2": {"inputs": ["high", "low", "close"], "func": f57_mcbd_128_realized_skew_negative_atr_compression_at_252h_d2},
    "f57_mcbd_129_realized_kurt_above_5_at_252h_d2": {"inputs": ["close", "high"], "func": f57_mcbd_129_realized_kurt_above_5_at_252h_d2},
    "f57_mcbd_130_var95_exceeded_at_252h_within_5d_d2": {"inputs": ["close", "high"], "func": f57_mcbd_130_var95_exceeded_at_252h_within_5d_d2},
    "f57_mcbd_131_vol_persistence_high_at_252h_d2": {"inputs": ["close", "high"], "func": f57_mcbd_131_vol_persistence_high_at_252h_d2},
    "f57_mcbd_132_vol_clustering_count_2sigma_3_in_21d_at_252h_d2": {"inputs": ["close", "high"], "func": f57_mcbd_132_vol_clustering_count_2sigma_3_in_21d_at_252h_d2},
    "f57_mcbd_133_realized_vol_at_252max_at_close_252max_d2": {"inputs": ["close", "high"], "func": f57_mcbd_133_realized_vol_at_252max_at_close_252max_d2},
    "f57_mcbd_134_overnight_gap_z_above_3_at_252h_d2": {"inputs": ["open", "close", "high"], "func": f57_mcbd_134_overnight_gap_z_above_3_at_252h_d2},
    "f57_mcbd_135_intraday_swing_above_5pct_at_252h_d2": {"inputs": ["open", "high", "low"], "func": f57_mcbd_135_intraday_swing_above_5pct_at_252h_d2},
    "f57_mcbd_136_count_3way_warnings_in_252d_d2": {"inputs": ["close", "volume", "high"], "func": f57_mcbd_136_count_3way_warnings_in_252d_d2},
    "f57_mcbd_137_count_distribution_days_in_252d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f57_mcbd_137_count_distribution_days_in_252d_d2},
    "f57_mcbd_138_count_topping_candles_in_252d_d2": {"inputs": ["open", "high", "low", "close"], "func": f57_mcbd_138_count_topping_candles_in_252d_d2},
    "f57_mcbd_139_count_bullish_no_demand_in_252d_d2": {"inputs": ["close", "volume", "high"], "func": f57_mcbd_139_count_bullish_no_demand_in_252d_d2},
    "f57_mcbd_140_count_bearish_high_vol_at_252max_in_252d_d2": {"inputs": ["open", "close", "volume", "high"], "func": f57_mcbd_140_count_bearish_high_vol_at_252max_in_252d_d2},
    "f57_mcbd_141_composite_topping_event_z_score_252d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f57_mcbd_141_composite_topping_event_z_score_252d_d2},
    "f57_mcbd_142_days_since_5_topping_conditions_d2": {"inputs": ["high", "low", "close"], "func": f57_mcbd_142_days_since_5_topping_conditions_d2},
    "f57_mcbd_143_blowoff_signature_cluster_density_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_143_blowoff_signature_cluster_density_63d_d2},
    "f57_mcbd_144_count_failed_breakouts_at_252h_in_252d_d2": {"inputs": ["high"], "func": f57_mcbd_144_count_failed_breakouts_at_252h_in_252d_d2},
    "f57_mcbd_145_count_swing_failures_252d_d2": {"inputs": ["high"], "func": f57_mcbd_145_count_swing_failures_252d_d2},
    "f57_mcbd_146_triple_top_3_peaks_within_63d_at_similar_d2": {"inputs": ["high"], "func": f57_mcbd_146_triple_top_3_peaks_within_63d_at_similar_d2},
    "f57_mcbd_147_rounding_top_signature_252d_d2": {"inputs": ["close"], "func": f57_mcbd_147_rounding_top_signature_252d_d2},
    "f57_mcbd_148_descending_triangle_indicator_d2": {"inputs": ["close", "high", "low"], "func": f57_mcbd_148_descending_triangle_indicator_d2},
    "f57_mcbd_149_head_shoulders_proxy_3peak_d2": {"inputs": ["high"], "func": f57_mcbd_149_head_shoulders_proxy_3peak_d2},
    "f57_mcbd_150_master_topping_composite_score_252d_d2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f57_mcbd_150_master_topping_composite_score_252d_d2},
}
