"""multi_condition_blowoff_detectors base 001-075 - 1b-technical."""
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


def f57_mcbd_001_at252h_close_lower30_vol_2x(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At 252d high AND close <30% range AND vol>2x avg."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pos = (close - low) / (high - low).replace(0, np.nan)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    rsi = _rsi(close, 14)
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close)
    zatr = _rolling_zscore(atr_n, YDAYS)
    return (((high >= rmax - 1e-12) & (pos < 0.30) & (volume > 2.0 * v_avg)).astype(float).where(v_avg.notna() & pos.notna(), np.nan))

def f57_mcbd_002_at252h_close_below_open_higher_high_vol_above_avg(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At 252d high AND close<open AND high>prev high AND vol>avg."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pos = (close - low) / (high - low).replace(0, np.nan)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    rsi = _rsi(close, 14)
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close)
    zatr = _rolling_zscore(atr_n, YDAYS)
    return (((high >= rmax - 1e-12) & (close < open) & (high > high.shift(1)) & (volume > v_avg)).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_003_at252h_atr_top_decile_rsi_above_70(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At 252d high AND ATR-N in top decile AND RSI>70."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close)
    p90 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rsi = _rsi(close, 14)
    return (((close >= rmax - 1e-12) & (atr_n > p90) & (rsi > 70.0)).astype(float).where(p90.notna() & rsi.notna(), np.nan))

def f57_mcbd_004_at252h_rsi_above_75_close_pos_top_quintile(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At 252d high AND RSI>75 AND close-pos>80% (overdrive bar)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pos = (close - low) / (high - low).replace(0, np.nan)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    rsi = _rsi(close, 14)
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close)
    zatr = _rolling_zscore(atr_n, YDAYS)
    return (((high >= rmax - 1e-12) & (rsi > 75.0) & (pos > 0.8)).astype(float).where(rsi.notna() & pos.notna(), np.nan))

def f57_mcbd_005_at252h_range_above_2atr_close_bottom_half(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At 252d high AND day range>2*ATR AND close in bottom half."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, MDAYS)
    rng = high - low
    pos = (close - low) / rng.replace(0, np.nan)
    return (((high >= rmax - 1e-12) & (rng > 2.0 * atr) & (pos < 0.5)).astype(float).where(atr.notna() & pos.notna(), np.nan))

def f57_mcbd_006_at252h_open_top_quintile_close_bottom_quintile(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At 252d high AND open in top 20% range AND close in bottom 20% (full reversal bar)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rng = (high - low).replace(0, np.nan)
    op = (open - low) / rng; cp = (close - low) / rng
    return (((high >= rmax - 1e-12) & (op > 0.8) & (cp < 0.2)).astype(float).where(op.notna() & cp.notna(), np.nan))

def f57_mcbd_007_at252h_log_ret_below_neg3pct_vol_above_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """At 252d high AND single-bar log-return<-3% AND vol>avg."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    r = _log_ret(close)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    return (((close >= rmax - 1e-12) & (r < -0.03) & (volume > v_avg)).astype(float).where(v_avg.notna() & r.notna(), np.nan))

def f57_mcbd_008_at252h_above_bb_upper_close_below_open(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At 252d high AND high>BB upper AND close<open (rejection at BB)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ma = _sma(close, 20); sd = close.rolling(20, min_periods=10).std()
    bb = ma + 2.0 * sd
    return (((high >= rmax - 1e-12) & (high > bb) & (close < open)).astype(float).where(bb.notna(), np.nan))

def f57_mcbd_009_at252h_doji_vol_above_avg(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At 252d high AND doji bar (body<10% range) AND vol>avg."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    return (((high >= rmax - 1e-12) & (body < 0.10) & (volume > v_avg)).astype(float).where(body.notna() & v_avg.notna(), np.nan))

def f57_mcbd_010_at252h_inside_bar_with_lower_close_lag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inside bar (prior) at 252d high AND current close < prior close."""
    rmax = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    inside = (high.shift(1) <= high.shift(2)) & (low.shift(1) >= low.shift(2))
    pah = (high.shift(1) >= rmax - 1e-12)
    return ((inside & pah & (close < close.shift(1))).astype(float).where(inside.notna(), np.nan))

def f57_mcbd_011_at252h_gap_up_then_close_below_prev_close(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """At 252d high AND open>prev close AND close<prev close (failed gap)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((high >= rmax - 1e-12) & (open > close.shift(1)) & (close < close.shift(1))).astype(float).where(rmax.notna(), np.nan))

def f57_mcbd_012_at252h_gap_above_prev_high_then_close_below_prev_high(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """At 252d high AND open>prev high AND close<prev high (true gap fail)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((high >= rmax - 1e-12) & (open > high.shift(1)) & (close < high.shift(1))).astype(float).where(rmax.notna(), np.nan))

def f57_mcbd_013_at252h_volume_dryup_new_high(high: pd.Series, volume: pd.Series) -> pd.Series:
    """High at 252d max AND vol<0.7*avg (no-demand new high)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    return (((high >= rmax - 1e-12) & (volume < 0.7 * v_avg)).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_014_at252h_atr_compression_close_below_open(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At 252d high AND ATR-N in bottom-q25 AND close<open."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close)
    q25 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (((high >= rmax - 1e-12) & (atr_n < q25) & (close < open)).astype(float).where(q25.notna(), np.nan))

def f57_mcbd_015_recent252h_close_below_sma20_vol_above_avg(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Close<SMA20 AND high at 252d max within 5 bars AND vol>avg (breakdown at high)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rh = (high >= rmax - 1e-12).rolling(WDAYS, min_periods=1).max()
    sma20 = _sma(close, 20)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    return (((rh > 0.5) & (close < sma20) & (volume > v_avg)).astype(float).where(sma20.notna() & v_avg.notna(), np.nan))

def f57_mcbd_016_climax_vol_then_inside_at_high(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Bar t-1: vol>2x avg at 252d high; Bar t: inside."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    climax = (volume.shift(1) > 2.0 * v_avg.shift(1)) & (high.shift(1) >= rmax.shift(1) - 1e-12)
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return ((climax & inside).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_017_shooting_star_at_high_then_lower_close(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shooting star at 252d high (bar t-1), lower close at t."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng
    uw = (high - pd.concat([open, close], axis=1).max(axis=1)) / rng
    shoot = (close < open) & (body < 0.30) & (uw > 0.60) & (high >= rmax - 1e-12)
    return ((shoot.shift(1) & (close < close.shift(1))).astype(float).where(rmax.notna(), np.nan))

def f57_mcbd_018_gap_up_at_high_then_gap_down_next_day(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Gap up at 252d high (t-1); gap down next day (t)."""
    rmax = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    g1 = (open.shift(1) > high.shift(2)) & (high.shift(1) >= rmax - 1e-12)
    gd = open < low.shift(1)
    return ((g1 & gd).astype(float).where(rmax.notna(), np.nan))

def f57_mcbd_019_bearish_engulf_at_252h_with_volume(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish engulf at 252d high AND vol>avg."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pup = close.shift(1) > open.shift(1); cdn = close < open
    engulf = (open >= close.shift(1)) & (close <= open.shift(1))
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    return ((pup & cdn & engulf & (high.shift(1) >= rmax.shift(1) - 1e-12) & (volume > v_avg)).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_020_two_lower_closes_after_252h(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bar t-2 at 252d high AND t-1 close<t-2 AND t close<t-1."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ah = (high.shift(2) >= rmax.shift(2) - 1e-12)
    return ((ah & (close.shift(1) < close.shift(2)) & (close < close.shift(1))).astype(float).where(rmax.notna(), np.nan))

def f57_mcbd_021_three_lower_highs_after_252h(high: pd.Series) -> pd.Series:
    """Bar t-3 at 252d high then t-2,t-1,t all lower highs."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    ah = (high.shift(3) >= rmax.shift(3) - 1e-12)
    return ((ah & (high.shift(2) < high.shift(3)) & (high.shift(1) < high.shift(2)) & (high < high.shift(1))).astype(float).where(rmax.notna(), np.nan))

def f57_mcbd_022_upthrust_after_distribution_2bar(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bar t-1 distribution (open top close bottom); bar t makes 21d-high AND closes below midrange."""
    rp = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    pop = (open.shift(1) - low.shift(1)) / rp; pcl = (close.shift(1) - low.shift(1)) / rp
    dist = (pop > 0.7) & (pcl < 0.3)
    h21 = high.rolling(MDAYS, min_periods=10).max()
    rng = (high - low).replace(0, np.nan); cp = (close - low) / rng
    return ((dist & (high >= h21 - 1e-12) & (cp < 0.5)).astype(float).where(rp.notna() & rng.notna(), np.nan))

def f57_mcbd_023_climax_vol_then_bearish_engulf_at_high(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bar t-1: vol>2x avg at 252d high; bar t: bearish engulf."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    climax = (volume.shift(1) > 2.0 * v_avg.shift(1)) & (high.shift(1) >= rmax.shift(1) - 1e-12)
    engulf = (close < open) & (open >= close.shift(1)) & (close <= open.shift(1))
    return ((climax & engulf).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_024_hanging_man_at_252h_with_volume(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Hanging man (small body, long lower wick, body in upper half) at 252d high AND vol>avg."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng
    lw = (pd.concat([open, close], axis=1).min(axis=1) - low) / rng
    bt = pd.concat([open, close], axis=1).max(axis=1); bp = (bt - low) / rng
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    return (((high >= rmax - 1e-12) & (body < 0.30) & (lw > 0.60) & (bp > 0.7) & (volume > v_avg)).astype(float).where(v_avg.notna() & rng.notna(), np.nan))

def f57_mcbd_025_three_white_soldiers_then_red_engulf(open: pd.Series, close: pd.Series) -> pd.Series:
    """3 up bars then bearish-engulf at t."""
    up3 = (close.shift(3) > open.shift(3)) & (close.shift(2) > open.shift(2)) & (close.shift(1) > open.shift(1))
    eg = (close < open) & (open >= close.shift(1)) & (close <= open.shift(1))
    return ((up3 & eg).astype(float).where(open.notna() & close.notna(), np.nan))

def f57_mcbd_026_evening_star_at_252h(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Evening star at 252d high: up/small/down sequence erasing 1st-bar gains."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    b1u = close.shift(2) > open.shift(2)
    r2 = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    b2s = (close.shift(1) - open.shift(1)).abs() < 0.3 * r2
    b3d = close < open
    er = close < (open.shift(2) + close.shift(2)) / 2.0
    ah = high.shift(2) >= rmax.shift(2) - 1e-12
    return ((b1u & b2s & b3d & er & ah).astype(float).where(r2.notna(), np.nan))

def f57_mcbd_027_dark_cloud_cover_at_252h(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Dark cloud cover at 252d high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pu = close.shift(1) > open.shift(1); oa = open > close.shift(1)
    mid = (open.shift(1) + close.shift(1)) / 2.0
    cbm = close < mid; su = close > open.shift(1)
    return ((pu & oa & cbm & su & (high >= rmax - 1e-12)).astype(float).where(rmax.notna(), np.nan))

def f57_mcbd_028_three_black_crows_at_252h(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """3 down bars (close<open) each with lower close than prev, at 252d-high context."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    d1 = (close.shift(2) < open.shift(2)); d2 = (close.shift(1) < open.shift(1)) & (close.shift(1) < close.shift(2))
    d3 = (close < open) & (close < close.shift(1))
    ah = high.shift(3) >= 0.95 * rmax.shift(3)
    return ((d1 & d2 & d3 & ah).astype(float).where(rmax.notna(), np.nan))

def f57_mcbd_029_bearish_island_reversal_at_252h(open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar t-3 gap up at 252d high; bar t-1 gap down isolating t-2 as island top."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    gu = (low.shift(3) > high.shift(4)) & (high.shift(3) >= rmax.shift(3) - 1e-12)
    gd = high.shift(1) < low.shift(2)
    return ((gu & gd).astype(float).where(rmax.notna(), np.nan))

def f57_mcbd_030_morning_doji_star_at_low_failure(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bar t-2 down at 252d low; bar t-1 doji; bar t up; bar t+1 reverses."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    b1d = close.shift(3) < open.shift(3)
    r2 = (high.shift(2) - low.shift(2)).replace(0, np.nan)
    b2dj = (close.shift(2) - open.shift(2)).abs() < 0.1 * r2
    b3u = close.shift(1) > open.shift(1)
    at_l = low.shift(3) <= rmin.shift(3) + 1e-12
    fail = close < open.shift(1)
    return ((b1d & b2dj & b3u & at_l & fail).astype(float).where(r2.notna(), np.nan))

def f57_mcbd_031_dry_vol_new_high_3_bars(high: pd.Series, volume: pd.Series) -> pd.Series:
    """3 bars: each makes new 21d-high AND vol<0.7*avg."""
    h21 = high.rolling(MDAYS, min_periods=10).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    nd = ((high >= h21 - 1e-12) & (volume < 0.7 * v_avg)).astype(float)
    return (((nd.shift(2) > 0.5) & (nd.shift(1) > 0.5) & (nd > 0.5)).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_032_vol_climax_narrow_range_breakdown(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bar t-2: vol>3x avg at 252d high. Bar t-1: range<0.5*ATR. Bar t: close<prev low."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    atr = _atr(high, low, close, MDAYS)
    c2 = (volume.shift(2) > 3.0 * v_avg.shift(2)) & (high.shift(2) >= rmax.shift(2) - 1e-12)
    n1 = (high.shift(1) - low.shift(1)) < 0.5 * atr.shift(1)
    bd = close < low.shift(1)
    return ((c2 & n1 & bd).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_033_up_close_low_vol_streak_5_at_high(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """5 bars up-close AND vol<avg AND at 252d high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    nd = ((close > close.shift(1)) & (volume < v_avg) & (high >= rmax - 1e-12)).astype(float)
    return (((nd.shift(4) > 0.5) & (nd.shift(3) > 0.5) & (nd.shift(2) > 0.5) & (nd.shift(1) > 0.5) & (nd > 0.5)).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_034_wide_range_distribution_3bars_at_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """3 bars: range>1.5*ATR AND close in bottom half AND at 252d high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, MDAYS)
    rng = high - low; pos = (close - low) / rng.replace(0, np.nan)
    d = ((rng > 1.5 * atr) & (pos < 0.5) & (high >= rmax - 1e-12)).astype(float)
    return (((d.shift(2) > 0.5) & (d.shift(1) > 0.5) & (d > 0.5)).astype(float).where(atr.notna(), np.nan))

def f57_mcbd_035_effort_no_result_at_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol>2x avg AND range<21d-avg-range AND at 252d high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    rng = high - low; ra = rng.rolling(MDAYS, min_periods=10).mean()
    return (((volume > 2.0 * v_avg) & (rng < ra) & (high >= rmax - 1e-12)).astype(float).where(v_avg.notna() & ra.notna(), np.nan))

def f57_mcbd_036_vol_above_avg_close_bottom_30_no_new_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol>avg AND close-pos<30% AND high did NOT make 21d-high (distribution day)."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=10).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    pos = (close - low) / (high - low).replace(0, np.nan)
    return (((volume > v_avg) & (pos < 0.30) & (high <= h21 - 1e-12)).astype(float).where(v_avg.notna() & pos.notna(), np.nan))

def f57_mcbd_037_low_vol_high_close_no_new_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol<avg AND close-pos>70% AND no new 21d high (no demand at would-be breakout)."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=10).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    pos = (close - low) / (high - low).replace(0, np.nan)
    return (((volume < v_avg) & (pos > 0.70) & (high <= h21 - 1e-12)).astype(float).where(v_avg.notna() & pos.notna(), np.nan))

def f57_mcbd_038_vol_3x_no_followthrough_3bars(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Bar t-3 vol>3x at 252d high; t-2,t-1,t no new 252d-high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    c3 = (volume.shift(3) > 3.0 * v_avg.shift(3)) & (high.shift(3) >= rmax.shift(3) - 1e-12)
    nn = (high.shift(2) < rmax.shift(2) - 1e-12) & (high.shift(1) < rmax.shift(1) - 1e-12) & (high < rmax - 1e-12)
    return ((c3 & nn).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_039_doji_top_decile_atr_vol_above_avg(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Doji AND ATR-N top decile AND vol>avg."""
    rng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close)
    p90 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    return (((body < 0.10) & (atr_n > p90) & (volume > v_avg)).astype(float).where(body.notna() & p90.notna() & v_avg.notna(), np.nan))

def f57_mcbd_040_vol_top_decile_close_pos_below_20_at_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol top decile 252d AND close-pos<20% AND high=252d max (selling climax at top)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    vp90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    pos = (close - low) / (high - low).replace(0, np.nan)
    return (((volume > vp90) & (pos < 0.20) & (high >= rmax - 1e-12)).astype(float).where(vp90.notna() & pos.notna(), np.nan))

def f57_mcbd_041_vol_top_range_top_close_below_open(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol top-decile AND range top-decile AND close<open (wide-range high-vol down bar = distribution)."""
    vp90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rng = high - low; rp90 = rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (((volume > vp90) & (rng > rp90) & (close < open)).astype(float).where(vp90.notna() & rp90.notna(), np.nan))

def f57_mcbd_042_vol_climax_then_2_inside_bars(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Bar t-2 vol>3x avg; bars t-1, t both inside."""
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    c = volume.shift(2) > 3.0 * v_avg.shift(2)
    i1 = (high.shift(1) < high.shift(2)) & (low.shift(1) > low.shift(2))
    i0 = (high < high.shift(1)) & (low > low.shift(1))
    return ((c & i1 & i0).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_043_vol_anomaly_then_gap_down(high: pd.Series, low: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol>3x avg at 252d high; next bar gaps down (open<prev low)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    c = (volume.shift(1) > 3.0 * v_avg.shift(1)) & (high.shift(1) >= rmax.shift(1) - 1e-12)
    return ((c & (open < low.shift(1))).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_044_two_day_vol_burst_lower_2nd_close(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """Bar t-1 vol>2x up-close at high; bar t vol>2x close<prev close."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    c1 = (volume.shift(1) > 2.0 * v_avg.shift(1)) & (close.shift(1) > close.shift(2)) & (high.shift(1) >= rmax.shift(1) - 1e-12)
    c0 = (volume > 2.0 * v_avg) & (close < close.shift(1))
    return ((c1 & c0).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_045_hawkes_vol_spike_then_dryup(volume: pd.Series, high: pd.Series) -> pd.Series:
    """Vol z>3 at 252d high (t-1); vol z<-1 next bar (t)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), QDAYS)
    sp = (vz.shift(1) > 3.0) & (high.shift(1) >= rmax.shift(1) - 1e-12)
    dr = vz < -1.0
    return ((sp & dr).astype(float).where(vz.notna(), np.nan))

def f57_mcbd_046_rsi_above_80_at_252h_atr_z_above_1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RSI>80 AND close=252d max AND ATR-z>1."""
    rsi = _rsi(close, 14); rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)
    return (((rsi > 80.0) & (close >= rmax - 1e-12) & (zatr > 1.0)).astype(float).where(rsi.notna() & zatr.notna(), np.nan))

def f57_mcbd_047_rsi_overbought_5_consecutive_at_high(close: pd.Series) -> pd.Series:
    """5 bars: RSI>70 AND close near 252d max (within 2%)."""
    rsi = _rsi(close, 14); rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    ob = ((rsi > 70.0) & (close / rmax > 0.98)).astype(float)
    return (((ob.shift(4) > 0.5) & (ob.shift(3) > 0.5) & (ob.shift(2) > 0.5) & (ob.shift(1) > 0.5) & (ob > 0.5)).astype(float).where(rsi.notna(), np.nan))

def f57_mcbd_048_rsi_exit_above_70_close_down_vol_above_avg(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI crosses from>=70 to<70 AND close<open AND vol>avg."""
    rsi = _rsi(close, 14)
    eo = (rsi < 70.0) & (rsi.shift(1) >= 70.0)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    return ((eo & (close < open) & (volume > v_avg)).astype(float).where(rsi.notna() & v_avg.notna(), np.nan))

def f57_mcbd_049_rsi_above_75_with_3_lower_highs(close: pd.Series, high: pd.Series) -> pd.Series:
    """RSI>75 AND 3 consecutive lower highs."""
    rsi = _rsi(close, 14)
    return (((rsi > 75.0) & (high < high.shift(1)) & (high.shift(1) < high.shift(2))).astype(float).where(rsi.notna(), np.nan))

def f57_mcbd_050_rsi_above_70_close_pos_below_50_at_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RSI>70 AND close-pos<50% AND high=252d max (OB reversal candle)."""
    rsi = _rsi(close, 14); rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pos = (close - low) / (high - low).replace(0, np.nan)
    return (((rsi > 70.0) & (pos < 0.5) & (high >= rmax - 1e-12)).astype(float).where(rsi.notna() & pos.notna(), np.nan))

def f57_mcbd_051_rsi_above_80_vol_3x_intraday_reversal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI>80 AND vol>3x AND close<midrange (parabolic exhaustion)."""
    rsi = _rsi(close, 14); v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    mid = (high + low) / 2.0
    return (((rsi > 80.0) & (volume > 3.0 * v_avg) & (close < mid)).astype(float).where(rsi.notna() & v_avg.notna(), np.nan))

def f57_mcbd_052_atr_top_decile_close_pos_below_30_at_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-N top decile AND close-pos<30% AND high=252d max."""
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close); p90 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    pos = (close - low) / (high - low).replace(0, np.nan)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((atr_n > p90) & (pos < 0.30) & (high >= rmax - 1e-12)).astype(float).where(p90.notna() & pos.notna(), np.nan))

def f57_mcbd_053_atr_compression_then_2x_expansion_at_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bar t-1 ATR-N in bottom decile; bar t ATR-N>1.5x prev; at 252d high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close); p10 = atr_n.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    c1 = atr_n.shift(1) < p10.shift(1); ex = atr_n > 1.5 * atr_n.shift(1); ah = high >= rmax - 1e-12
    return ((c1 & ex & ah).astype(float).where(p10.notna(), np.nan))

def f57_mcbd_054_vol_z_above_2_rsi_above_70_at_252h(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol z>2 AND RSI>70 AND high=252d max."""
    vz = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS)
    rsi = _rsi(close, 14)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((vz > 2.0) & (rsi > 70.0) & (high >= rmax - 1e-12)).astype(float).where(vz.notna() & rsi.notna(), np.nan))

def f57_mcbd_055_dollar_vol_above_p90_close_bottom_quartile_at_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol>252d p90 AND close-pos<25% AND high=252d max."""
    dv = close * volume; p90 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    pos = (close - low) / (high - low).replace(0, np.nan)
    return (((dv > p90) & (pos < 0.25) & (high >= rmax - 1e-12)).astype(float).where(p90.notna() & pos.notna(), np.nan))

def f57_mcbd_056_rsi_above_70_macd_below_sig_at_high(close: pd.Series, high: pd.Series) -> pd.Series:
    """RSI>70 AND MACD<sig AND close=252d max."""
    rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    return (((rsi > 70.0) & (macd < sig) & (close >= rmax - 1e-12)).astype(float).where(rsi.notna() & sig.notna(), np.nan))

def f57_mcbd_057_above_bb_upper_rsi_70_close_below_open(open: pd.Series, close: pd.Series) -> pd.Series:
    """Close>BB upper AND RSI>70 AND close<open."""
    rsi = _rsi(close, 14); ma = _sma(close, 20); sd = close.rolling(20, min_periods=10).std()
    bbu = ma + 2.0 * sd
    return (((close > bbu) & (rsi > 70.0) & (close < open)).astype(float).where(bbu.notna() & rsi.notna(), np.nan))

def f57_mcbd_058_mayer_above_2_rsi_70_close_below_open(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mayer>2 AND RSI>70 AND close<open."""
    rsi = _rsi(close, 14); sma200 = _sma(close, 200); mayer = _safe_div(close, sma200)
    return (((mayer > 2.0) & (rsi > 70.0) & (close < open)).astype(float).where(mayer.notna() & rsi.notna(), np.nan))

def f57_mcbd_059_close_sma50_extension_above_15pct_rsi_75(close: pd.Series) -> pd.Series:
    """Close/SMA50-1>15% AND RSI>75 (parabolic + extreme OB)."""
    rsi = _rsi(close, 14); sma50 = _sma(close, 50); ext = _safe_div(close - sma50, sma50)
    return (((ext > 0.15) & (rsi > 75.0)).astype(float).where(ext.notna() & rsi.notna(), np.nan))

def f57_mcbd_060_rsi_70_close_below_5d_low_252h_within_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """RSI>70 AND close<5d-low AND 252d-high within 5 bars (immediate breakdown)."""
    rsi = _rsi(close, 14); l5 = low.shift(1).rolling(WDAYS, min_periods=1).min()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rh = (high >= rmax - 1e-12).shift(WDAYS).rolling(WDAYS, min_periods=1).max()
    return (((rsi > 70.0) & (close < l5) & (rh > 0.5)).astype(float).where(rsi.notna() & l5.notna(), np.nan))

def f57_mcbd_061_hindenburg_self_proxy_252d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Self-Hindenburg: new 252d-high AND new 252d-low within 21 bars AND vol>avg."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    nh21 = ((high >= rmax - 1e-12).rolling(MDAYS, min_periods=10).max() > 0.5)
    nl21 = ((low <= rmin + 1e-12).rolling(MDAYS, min_periods=10).max() > 0.5)
    v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    return ((nh21 & nl21 & (volume > v_avg)).astype(float).where(v_avg.notna(), np.nan))

def f57_mcbd_062_composite_warning_3of5_topping_count(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count >=3 of 5: RSI>70, MACD<sig, close=252d max, ATR-z>1, close-pos<50%."""
    rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)
    pos = (close - low) / (high - low).replace(0, np.nan)
    cnt = ((rsi > 70.0).astype(float) + (macd < sig).astype(float) + (close >= rmax - 1e-12).astype(float) + (zatr > 1.0).astype(float) + (pos < 0.5).astype(float))
    return ((cnt >= 3).astype(float).where(rsi.notna() & sig.notna() & zatr.notna() & pos.notna(), np.nan))

def f57_mcbd_063_topping_density_3of5_persistence_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63d with 3-of-5 topping count >=3."""
    rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)
    pos = (close - low) / (high - low).replace(0, np.nan)
    cnt = ((rsi > 70.0).astype(float) + (macd < sig).astype(float) + (close >= rmax - 1e-12).astype(float) + (zatr > 1.0).astype(float) + (pos < 0.5).astype(float))
    return ((cnt >= 3).astype(float).rolling(QDAYS, min_periods=MDAYS).mean())

def f57_mcbd_064_five_of_five_topping_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """All 5 topping conditions simultaneously."""
    rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close); zatr = _rolling_zscore(atr_n, YDAYS)
    pos = (close - low) / (high - low).replace(0, np.nan)
    return (((rsi > 70.0) & (macd < sig) & (close >= rmax - 1e-12) & (zatr > 1.0) & (pos < 0.5)).astype(float).where(rsi.notna() & sig.notna(), np.nan))

def f57_mcbd_065_quadruple_warning_indicator(open: pd.Series, close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """RSI>75 AND vol>2x AND close<open AND at 252d max."""
    rsi = _rsi(close, 14); v_avg = volume.rolling(MDAYS, min_periods=10).mean()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((rsi > 75.0) & (volume > 2.0 * v_avg) & (close < open) & (high >= rmax - 1e-12)).astype(float).where(v_avg.notna() & rsi.notna(), np.nan))

def f57_mcbd_066_five_factor_pre_crash_z_composite(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """z(RSI) + z(vol) + z(atr) + z(close_ext_sma50) + z(MACD-sig) over 252d."""
    rsi = _rsi(close, 14); macd = _macd(close); sig = macd.ewm(span=9, adjust=False, min_periods=3).mean()
    atr_n = _safe_div(_atr(high, low, close, MDAYS), close)
    sma50 = _sma(close, 50); ext = _safe_div(close - sma50, sma50)
    z1 = _rolling_zscore(rsi, YDAYS); z2 = _rolling_zscore(_safe_log(volume.replace(0, np.nan)), YDAYS); z3 = _rolling_zscore(atr_n, YDAYS); z4 = _rolling_zscore(ext, YDAYS); z5 = _rolling_zscore(macd - sig, YDAYS)
    return (z1.fillna(0) + z2.fillna(0) + z3.fillna(0) + z4.fillna(0) - z5.fillna(0))

def f57_mcbd_067_vol_climax_atr_compression_later(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bar t-5 to t-2 vol climax (>3x avg) AND today ATR<0.5*ATR at climax."""
    v_avg = volume.rolling(MDAYS, min_periods=10).mean(); atr = _atr(high, low, close, MDAYS)
    climax = (volume > 3.0 * v_avg).astype(float)
    cr = climax.shift(2).rolling(4, min_periods=1).max()
    ac = (atr.shift(2) * climax.shift(2)).rolling(4, min_periods=1).max()
    comp = (atr < 0.5 * ac)
    return ((cr > 0.5).astype(float) * comp.astype(float))

def f57_mcbd_068_multi_oscillator_3of3_ob_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 63d bars with RSI>70 AND Stoch%K>80 AND Williams%R>-20."""
    rsi = _rsi(close, 14)
    hh = high.rolling(14, min_periods=5).max(); ll = low.rolling(14, min_periods=5).min()
    stk = 100.0 * (close - ll) / (hh - ll).replace(0, np.nan)
    wr = -100.0 * (hh - close) / (hh - ll).replace(0, np.nan)
    all3 = ((rsi > 70.0) & (stk > 80.0) & (wr > -20.0)).astype(float).where(rsi.notna(), np.nan)
    return (all3.rolling(QDAYS, min_periods=MDAYS).sum())

def f57_mcbd_069_multi_oscillator_ob_decay_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """All 3 OB at t-1 but NOT all 3 OB at t (decay)."""
    rsi = _rsi(close, 14)
    hh = high.rolling(14, min_periods=5).max(); ll = low.rolling(14, min_periods=5).min()
    stk = 100.0 * (close - ll) / (hh - ll).replace(0, np.nan)
    wr = -100.0 * (hh - close) / (hh - ll).replace(0, np.nan)
    all3 = ((rsi > 70.0) & (stk > 80.0) & (wr > -20.0)).astype(float)
    return ((all3.shift(1) > 0.5).astype(float) * (all3 < 0.5).astype(float))

def f57_mcbd_070_close_top_decile_rsi_below_50_at_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close in top 10% of 252d range BUT RSI<50 (extreme price/momentum disagreement)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pr = _safe_div(close - rmin, rmax - rmin); rsi = _rsi(close, 14)
    return (((pr > 0.9) & (rsi < 50.0)).astype(float).where(pr.notna() & rsi.notna(), np.nan))

def f57_mcbd_071_close_top_decile_macd_negative_at_high(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close top 10% AND MACD<0 AND close=252d max (extreme bearish momentum at top)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max(); rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pr = _safe_div(close - rmin, rmax - rmin); macd = _macd(close)
    return (((pr > 0.9) & (macd < 0) & (close >= rmax - 1e-12)).astype(float).where(pr.notna() & macd.notna(), np.nan))

def f57_mcbd_072_close_sma200_ext_30pct_obv_falling(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close/SMA200>1.3 AND OBV-slope 21d<0 (parabolic + falling OBV)."""
    sma200 = _sma(close, 200); ext = _safe_div(close - sma200, sma200)
    obv = _obv(close, volume); os = _rolling_slope(obv, MDAYS)
    return (((ext > 0.30) & (os < 0)).astype(float).where(ext.notna() & os.notna(), np.nan))

def f57_mcbd_073_five_consecutive_doji_at_high(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5 consecutive doji (body/range<15%) at near 252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rng = (high - low).replace(0, np.nan); body = (close - open).abs() / rng
    dj = ((body < 0.15) & (high >= 0.98 * rmax)).astype(float)
    return (((dj.shift(4) > 0.5) & (dj.shift(3) > 0.5) & (dj.shift(2) > 0.5) & (dj.shift(1) > 0.5) & (dj > 0.5)).astype(float).where(rng.notna(), np.nan))

def f57_mcbd_074_price_z_above_2_dollar_vol_z_below_neg1_at_high(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """z(close)>2 AND z($-vol)<-1 AND at 252d high (parabolic + low participation)."""
    zc = _rolling_zscore(_safe_log(close), YDAYS); zdv = _rolling_zscore(_safe_log((close * volume).replace(0, np.nan)), YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (((zc > 2.0) & (zdv < -1.0) & (high >= rmax - 1e-12)).astype(float).where(zc.notna() & zdv.notna(), np.nan))

def f57_mcbd_075_parabolic_5_up_closes_above_1_5pct(close: pd.Series) -> pd.Series:
    """5 consecutive bars with log_ret>1.5% (parabolic acceleration)."""
    r = _log_ret(close)
    return (((r.shift(4) > 0.015) & (r.shift(3) > 0.015) & (r.shift(2) > 0.015) & (r.shift(1) > 0.015) & (r > 0.015)).astype(float).where(r.notna(), np.nan))


MULTI_CONDITION_BLOWOFF_DETECTORS_BASE_REGISTRY_001_075 = {
    "f57_mcbd_001_at252h_close_lower30_vol_2x": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_001_at252h_close_lower30_vol_2x},
    "f57_mcbd_002_at252h_close_below_open_higher_high_vol_above_avg": {"inputs": ["open", "high", "low", "close", "volume"], "func": f57_mcbd_002_at252h_close_below_open_higher_high_vol_above_avg},
    "f57_mcbd_003_at252h_atr_top_decile_rsi_above_70": {"inputs": ["high", "low", "close"], "func": f57_mcbd_003_at252h_atr_top_decile_rsi_above_70},
    "f57_mcbd_004_at252h_rsi_above_75_close_pos_top_quintile": {"inputs": ["high", "low", "close"], "func": f57_mcbd_004_at252h_rsi_above_75_close_pos_top_quintile},
    "f57_mcbd_005_at252h_range_above_2atr_close_bottom_half": {"inputs": ["high", "low", "close"], "func": f57_mcbd_005_at252h_range_above_2atr_close_bottom_half},
    "f57_mcbd_006_at252h_open_top_quintile_close_bottom_quintile": {"inputs": ["open", "high", "low", "close"], "func": f57_mcbd_006_at252h_open_top_quintile_close_bottom_quintile},
    "f57_mcbd_007_at252h_log_ret_below_neg3pct_vol_above_avg": {"inputs": ["close", "volume"], "func": f57_mcbd_007_at252h_log_ret_below_neg3pct_vol_above_avg},
    "f57_mcbd_008_at252h_above_bb_upper_close_below_open": {"inputs": ["open", "high", "low", "close"], "func": f57_mcbd_008_at252h_above_bb_upper_close_below_open},
    "f57_mcbd_009_at252h_doji_vol_above_avg": {"inputs": ["open", "high", "low", "close", "volume"], "func": f57_mcbd_009_at252h_doji_vol_above_avg},
    "f57_mcbd_010_at252h_inside_bar_with_lower_close_lag": {"inputs": ["high", "low", "close"], "func": f57_mcbd_010_at252h_inside_bar_with_lower_close_lag},
    "f57_mcbd_011_at252h_gap_up_then_close_below_prev_close": {"inputs": ["open", "high", "close"], "func": f57_mcbd_011_at252h_gap_up_then_close_below_prev_close},
    "f57_mcbd_012_at252h_gap_above_prev_high_then_close_below_prev_high": {"inputs": ["open", "high", "close"], "func": f57_mcbd_012_at252h_gap_above_prev_high_then_close_below_prev_high},
    "f57_mcbd_013_at252h_volume_dryup_new_high": {"inputs": ["high", "volume"], "func": f57_mcbd_013_at252h_volume_dryup_new_high},
    "f57_mcbd_014_at252h_atr_compression_close_below_open": {"inputs": ["open", "high", "low", "close"], "func": f57_mcbd_014_at252h_atr_compression_close_below_open},
    "f57_mcbd_015_recent252h_close_below_sma20_vol_above_avg": {"inputs": ["close", "high", "volume"], "func": f57_mcbd_015_recent252h_close_below_sma20_vol_above_avg},
    "f57_mcbd_016_climax_vol_then_inside_at_high": {"inputs": ["high", "low", "volume"], "func": f57_mcbd_016_climax_vol_then_inside_at_high},
    "f57_mcbd_017_shooting_star_at_high_then_lower_close": {"inputs": ["open", "high", "low", "close"], "func": f57_mcbd_017_shooting_star_at_high_then_lower_close},
    "f57_mcbd_018_gap_up_at_high_then_gap_down_next_day": {"inputs": ["open", "high", "low"], "func": f57_mcbd_018_gap_up_at_high_then_gap_down_next_day},
    "f57_mcbd_019_bearish_engulf_at_252h_with_volume": {"inputs": ["open", "high", "low", "close", "volume"], "func": f57_mcbd_019_bearish_engulf_at_252h_with_volume},
    "f57_mcbd_020_two_lower_closes_after_252h": {"inputs": ["close", "high"], "func": f57_mcbd_020_two_lower_closes_after_252h},
    "f57_mcbd_021_three_lower_highs_after_252h": {"inputs": ["high"], "func": f57_mcbd_021_three_lower_highs_after_252h},
    "f57_mcbd_022_upthrust_after_distribution_2bar": {"inputs": ["open", "high", "low", "close"], "func": f57_mcbd_022_upthrust_after_distribution_2bar},
    "f57_mcbd_023_climax_vol_then_bearish_engulf_at_high": {"inputs": ["open", "high", "low", "close", "volume"], "func": f57_mcbd_023_climax_vol_then_bearish_engulf_at_high},
    "f57_mcbd_024_hanging_man_at_252h_with_volume": {"inputs": ["open", "high", "low", "close", "volume"], "func": f57_mcbd_024_hanging_man_at_252h_with_volume},
    "f57_mcbd_025_three_white_soldiers_then_red_engulf": {"inputs": ["open", "close"], "func": f57_mcbd_025_three_white_soldiers_then_red_engulf},
    "f57_mcbd_026_evening_star_at_252h": {"inputs": ["open", "high", "low", "close"], "func": f57_mcbd_026_evening_star_at_252h},
    "f57_mcbd_027_dark_cloud_cover_at_252h": {"inputs": ["open", "high", "low", "close"], "func": f57_mcbd_027_dark_cloud_cover_at_252h},
    "f57_mcbd_028_three_black_crows_at_252h": {"inputs": ["open", "close", "high"], "func": f57_mcbd_028_three_black_crows_at_252h},
    "f57_mcbd_029_bearish_island_reversal_at_252h": {"inputs": ["open", "high", "low"], "func": f57_mcbd_029_bearish_island_reversal_at_252h},
    "f57_mcbd_030_morning_doji_star_at_low_failure": {"inputs": ["open", "high", "low", "close"], "func": f57_mcbd_030_morning_doji_star_at_low_failure},
    "f57_mcbd_031_dry_vol_new_high_3_bars": {"inputs": ["high", "volume"], "func": f57_mcbd_031_dry_vol_new_high_3_bars},
    "f57_mcbd_032_vol_climax_narrow_range_breakdown": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_032_vol_climax_narrow_range_breakdown},
    "f57_mcbd_033_up_close_low_vol_streak_5_at_high": {"inputs": ["close", "volume", "high"], "func": f57_mcbd_033_up_close_low_vol_streak_5_at_high},
    "f57_mcbd_034_wide_range_distribution_3bars_at_high": {"inputs": ["high", "low", "close"], "func": f57_mcbd_034_wide_range_distribution_3bars_at_high},
    "f57_mcbd_035_effort_no_result_at_high": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_035_effort_no_result_at_high},
    "f57_mcbd_036_vol_above_avg_close_bottom_30_no_new_high": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_036_vol_above_avg_close_bottom_30_no_new_high},
    "f57_mcbd_037_low_vol_high_close_no_new_high": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_037_low_vol_high_close_no_new_high},
    "f57_mcbd_038_vol_3x_no_followthrough_3bars": {"inputs": ["high", "volume"], "func": f57_mcbd_038_vol_3x_no_followthrough_3bars},
    "f57_mcbd_039_doji_top_decile_atr_vol_above_avg": {"inputs": ["open", "high", "low", "close", "volume"], "func": f57_mcbd_039_doji_top_decile_atr_vol_above_avg},
    "f57_mcbd_040_vol_top_decile_close_pos_below_20_at_high": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_040_vol_top_decile_close_pos_below_20_at_high},
    "f57_mcbd_041_vol_top_range_top_close_below_open": {"inputs": ["open", "high", "low", "close", "volume"], "func": f57_mcbd_041_vol_top_range_top_close_below_open},
    "f57_mcbd_042_vol_climax_then_2_inside_bars": {"inputs": ["high", "low", "volume"], "func": f57_mcbd_042_vol_climax_then_2_inside_bars},
    "f57_mcbd_043_vol_anomaly_then_gap_down": {"inputs": ["high", "low", "open", "volume"], "func": f57_mcbd_043_vol_anomaly_then_gap_down},
    "f57_mcbd_044_two_day_vol_burst_lower_2nd_close": {"inputs": ["close", "volume", "high"], "func": f57_mcbd_044_two_day_vol_burst_lower_2nd_close},
    "f57_mcbd_045_hawkes_vol_spike_then_dryup": {"inputs": ["volume", "high"], "func": f57_mcbd_045_hawkes_vol_spike_then_dryup},
    "f57_mcbd_046_rsi_above_80_at_252h_atr_z_above_1": {"inputs": ["high", "low", "close"], "func": f57_mcbd_046_rsi_above_80_at_252h_atr_z_above_1},
    "f57_mcbd_047_rsi_overbought_5_consecutive_at_high": {"inputs": ["close"], "func": f57_mcbd_047_rsi_overbought_5_consecutive_at_high},
    "f57_mcbd_048_rsi_exit_above_70_close_down_vol_above_avg": {"inputs": ["open", "close", "volume"], "func": f57_mcbd_048_rsi_exit_above_70_close_down_vol_above_avg},
    "f57_mcbd_049_rsi_above_75_with_3_lower_highs": {"inputs": ["close", "high"], "func": f57_mcbd_049_rsi_above_75_with_3_lower_highs},
    "f57_mcbd_050_rsi_above_70_close_pos_below_50_at_high": {"inputs": ["high", "low", "close"], "func": f57_mcbd_050_rsi_above_70_close_pos_below_50_at_high},
    "f57_mcbd_051_rsi_above_80_vol_3x_intraday_reversal": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_051_rsi_above_80_vol_3x_intraday_reversal},
    "f57_mcbd_052_atr_top_decile_close_pos_below_30_at_high": {"inputs": ["high", "low", "close"], "func": f57_mcbd_052_atr_top_decile_close_pos_below_30_at_high},
    "f57_mcbd_053_atr_compression_then_2x_expansion_at_high": {"inputs": ["high", "low", "close"], "func": f57_mcbd_053_atr_compression_then_2x_expansion_at_high},
    "f57_mcbd_054_vol_z_above_2_rsi_above_70_at_252h": {"inputs": ["high", "close", "volume"], "func": f57_mcbd_054_vol_z_above_2_rsi_above_70_at_252h},
    "f57_mcbd_055_dollar_vol_above_p90_close_bottom_quartile_at_high": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_055_dollar_vol_above_p90_close_bottom_quartile_at_high},
    "f57_mcbd_056_rsi_above_70_macd_below_sig_at_high": {"inputs": ["close", "high"], "func": f57_mcbd_056_rsi_above_70_macd_below_sig_at_high},
    "f57_mcbd_057_above_bb_upper_rsi_70_close_below_open": {"inputs": ["open", "close"], "func": f57_mcbd_057_above_bb_upper_rsi_70_close_below_open},
    "f57_mcbd_058_mayer_above_2_rsi_70_close_below_open": {"inputs": ["open", "close"], "func": f57_mcbd_058_mayer_above_2_rsi_70_close_below_open},
    "f57_mcbd_059_close_sma50_extension_above_15pct_rsi_75": {"inputs": ["close"], "func": f57_mcbd_059_close_sma50_extension_above_15pct_rsi_75},
    "f57_mcbd_060_rsi_70_close_below_5d_low_252h_within_5d": {"inputs": ["close", "high", "low"], "func": f57_mcbd_060_rsi_70_close_below_5d_low_252h_within_5d},
    "f57_mcbd_061_hindenburg_self_proxy_252d": {"inputs": ["high", "low", "volume"], "func": f57_mcbd_061_hindenburg_self_proxy_252d},
    "f57_mcbd_062_composite_warning_3of5_topping_count": {"inputs": ["high", "low", "close"], "func": f57_mcbd_062_composite_warning_3of5_topping_count},
    "f57_mcbd_063_topping_density_3of5_persistence_63d": {"inputs": ["high", "low", "close"], "func": f57_mcbd_063_topping_density_3of5_persistence_63d},
    "f57_mcbd_064_five_of_five_topping_indicator": {"inputs": ["high", "low", "close"], "func": f57_mcbd_064_five_of_five_topping_indicator},
    "f57_mcbd_065_quadruple_warning_indicator": {"inputs": ["open", "close", "volume", "high"], "func": f57_mcbd_065_quadruple_warning_indicator},
    "f57_mcbd_066_five_factor_pre_crash_z_composite": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_066_five_factor_pre_crash_z_composite},
    "f57_mcbd_067_vol_climax_atr_compression_later": {"inputs": ["high", "low", "close", "volume"], "func": f57_mcbd_067_vol_climax_atr_compression_later},
    "f57_mcbd_068_multi_oscillator_3of3_ob_count_63d": {"inputs": ["high", "low", "close"], "func": f57_mcbd_068_multi_oscillator_3of3_ob_count_63d},
    "f57_mcbd_069_multi_oscillator_ob_decay_indicator": {"inputs": ["high", "low", "close"], "func": f57_mcbd_069_multi_oscillator_ob_decay_indicator},
    "f57_mcbd_070_close_top_decile_rsi_below_50_at_high": {"inputs": ["high", "low", "close"], "func": f57_mcbd_070_close_top_decile_rsi_below_50_at_high},
    "f57_mcbd_071_close_top_decile_macd_negative_at_high": {"inputs": ["high", "low", "close"], "func": f57_mcbd_071_close_top_decile_macd_negative_at_high},
    "f57_mcbd_072_close_sma200_ext_30pct_obv_falling": {"inputs": ["close", "volume"], "func": f57_mcbd_072_close_sma200_ext_30pct_obv_falling},
    "f57_mcbd_073_five_consecutive_doji_at_high": {"inputs": ["open", "high", "low", "close"], "func": f57_mcbd_073_five_consecutive_doji_at_high},
    "f57_mcbd_074_price_z_above_2_dollar_vol_z_below_neg1_at_high": {"inputs": ["close", "volume", "high"], "func": f57_mcbd_074_price_z_above_2_dollar_vol_z_below_neg1_at_high},
    "f57_mcbd_075_parabolic_5_up_closes_above_1_5pct": {"inputs": ["close"], "func": f57_mcbd_075_parabolic_5_up_closes_above_1_5pct},
}
