"""terminal_distribution_composite base features 301-375 — Pipeline 1b-technical.

Liquidity decay + institutional behavior + Stage 4 / death spiral.
75 distinct hypotheses targeting stuck-stock (-80% DD, no recovery > -50% in 5y).

L: liquidity / microstructure decay (Amihud, Roll, Corwin-Schultz, Abdi-Ranaldi).
M: institutional / block-trade proxies (block-day, distribution stick, capitulation).
N: Stage 4 / Weinstein / death spiral terminal regime.
O: range / structural decay (ATR-expansion, gap density post-peak).

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers at module top.
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


def _slope_kernel(w):
    valid = ~np.isnan(w)
    mp = max(len(w) // 3, 2)
    if valid.sum() < mp:
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


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    return s.rolling(n, min_periods=min_periods).apply(_slope_kernel, raw=True)


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _bars_since_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ============================================================
# L — liquidity / microstructure decay (301-315)
# ============================================================

def f50_tdco_301_amihud_illiquidity_proxy_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud: |daily return| / (dollar-volume) averaged over 21 — illiquidity proxy short-horizon."""
    ret = close.pct_change().abs()
    dvol = volume * close
    daily = _safe_div(ret, dvol)
    return daily.rolling(MDAYS, min_periods=WDAYS).mean()


def f50_tdco_302_amihud_illiquidity_proxy_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Amihud illiquidity averaged over 63 — quarterly horizon."""
    ret = close.pct_change().abs()
    dvol = volume * close
    daily = _safe_div(ret, dvol)
    return daily.rolling(QDAYS, min_periods=MDAYS).mean()


def f50_tdco_303_amihud_illiquidity_zscore_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (252d) of Amihud-21 — extreme-illiquidity regime detector."""
    ret = close.pct_change().abs()
    dvol = volume * close
    daily = _safe_div(ret, dvol)
    am21 = daily.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(am21, YDAYS, min_periods=QDAYS)


def f50_tdco_304_amihud_illiquidity_rising_state_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 63d slope of Amihud-21 > 0 — illiquidity trending up (deteriorating liquidity)."""
    ret = close.pct_change().abs()
    dvol = volume * close
    daily = _safe_div(ret, dvol)
    am21 = daily.rolling(MDAYS, min_periods=WDAYS).mean()
    sl = _rolling_slope(am21, QDAYS)
    return (sl > 0).astype(float).where(sl.notna(), np.nan)


def f50_tdco_305_roll_spread_proxy_21(close: pd.Series) -> pd.Series:
    """Roll spread: 2 * sqrt(max(-cov(r_t, r_t-1), 0)) over 21d window — implicit bid-ask spread proxy."""
    ret = close.pct_change()
    ret1 = ret.shift(1)
    cov = ret.rolling(MDAYS, min_periods=WDAYS).cov(ret1)
    neg_cov = (-cov).clip(lower=0)
    return 2.0 * np.sqrt(neg_cov)


def f50_tdco_306_roll_spread_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score (252d) of Roll-spread-21 — extreme implicit-spread regime."""
    ret = close.pct_change()
    ret1 = ret.shift(1)
    cov = ret.rolling(MDAYS, min_periods=WDAYS).cov(ret1)
    rs = 2.0 * np.sqrt((-cov).clip(lower=0))
    return _rolling_zscore(rs, YDAYS, min_periods=QDAYS)


def f50_tdco_307_corwin_schultz_spread_proxy_2bar(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz 2-bar high-low spread estimator (simplified):
    beta = (ln(H_t/L_t))^2 + (ln(H_{t-1}/L_{t-1}))^2;
    gamma = (ln(max(H_t,H_{t-1}) / min(L_t,L_{t-1})))^2;
    alpha = ( sqrt(2*beta) - sqrt(beta) ) / (3 - 2*sqrt(2)) - sqrt( gamma / (3 - 2*sqrt(2)) );
    spread = 2*(exp(alpha)-1)/(1+exp(alpha)).  Averaged over 21d."""
    lh = np.log(high.replace(0, np.nan))
    ll = np.log(low.replace(0, np.nan))
    hl1 = (lh - ll) ** 2
    hl2 = ((lh.shift(1)) - (ll.shift(1))) ** 2
    beta = hl1 + hl2
    H2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    L2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    gamma = (np.log(_safe_div(H2, L2))) ** 2
    denom = 3.0 - 2.0 * np.sqrt(2.0)
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / denom - np.sqrt(gamma / denom)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    spread = spread.replace([np.inf, -np.inf], np.nan)
    return spread.rolling(MDAYS, min_periods=WDAYS).mean()


def f50_tdco_308_corwin_schultz_zscore_252(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score (252d) of Corwin-Schultz spread — implicit-spread regime extreme."""
    lh = np.log(high.replace(0, np.nan))
    ll = np.log(low.replace(0, np.nan))
    hl1 = (lh - ll) ** 2
    hl2 = ((lh.shift(1)) - (ll.shift(1))) ** 2
    beta = hl1 + hl2
    H2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    L2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    gamma = (np.log(_safe_div(H2, L2))) ** 2
    denom = 3.0 - 2.0 * np.sqrt(2.0)
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / denom - np.sqrt(gamma / denom)
    spread = (2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))).replace([np.inf, -np.inf], np.nan)
    smooth = spread.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(smooth, YDAYS, min_periods=QDAYS)


def f50_tdco_309_abdi_ranaldi_spread_proxy_2bar(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Abdi-Ranaldi 2-bar high-low spread estimator (simplified):
    s_t = sqrt( max(4 * (ln(C_t) - 0.5*(ln(H_t) + ln(L_t))) * (ln(C_{t-1}) - 0.5*(ln(H_{t-1}) + ln(L_{t-1}))) * (-1), 0) )
    averaged over 21 — improved high-low spread proxy."""
    lc = np.log(close.replace(0, np.nan))
    lh = np.log(high.replace(0, np.nan))
    ll = np.log(low.replace(0, np.nan))
    mid = 0.5 * (lh + ll)
    a = (lc - mid)
    b = (lc.shift(1) - mid.shift(1))
    raw = -4.0 * a * b
    s = np.sqrt(raw.clip(lower=0))
    return s.rolling(MDAYS, min_periods=WDAYS).mean()


def f50_tdco_310_high_low_range_volume_ratio_decay_63(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of (H-L)/volume — rising = illiquidity proxy decay (price moves on lighter volume)."""
    rng = high - low
    illiq = _safe_div(rng, volume)
    return _rolling_slope(illiq, QDAYS)


def f50_tdco_311_turnover_decay_post_peak_63(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Turnover proxy (volume) decay since 252d peak: (volume EMA63 / volume EMA63 at peak).
    Computed as ratio of current EMA63 vol to EMA63 vol N bars ago where N = bars since peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    vol_ema = _ema(volume, QDAYS)
    bs_int = bs.fillna(0).astype(int)
    arr = vol_ema.to_numpy()
    out = np.full(arr.shape, np.nan)
    for i in range(arr.size):
        k = int(bs_int.iloc[i]) if not np.isnan(bs.iloc[i]) else 0
        j = i - k
        if j >= 0 and not np.isnan(arr[i]) and not np.isnan(arr[j]) and arr[j] != 0:
            out[i] = arr[i] / arr[j]
    return pd.Series(out, index=volume.index)


def f50_tdco_312_volume_volatility_ratio_decay_63(volume: pd.Series) -> pd.Series:
    """Vol-of-volume rising: 21d std-of-volume / 63d-mean-volume — liquidity stress indicator."""
    vstd = volume.rolling(MDAYS, min_periods=WDAYS).std()
    vmean = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(vstd, vmean)


def f50_tdco_313_dollar_volume_decay_velocity_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of dollar-volume (close * volume) — negative slope = liquidity decay."""
    dv = close * volume
    return _rolling_slope(dv, QDAYS)


def f50_tdco_314_dollar_volume_zscore_below_q25_state(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if current dollar-volume < 25th percentile over past 252 — depressed-liquidity state."""
    dv = close * volume
    q25 = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (dv < q25).astype(float).where(q25.notna(), np.nan)


def f50_tdco_315_effective_tick_size_proxy_21(close: pd.Series) -> pd.Series:
    """Holden-2009 effective-tick proxy (simplified): fraction of past 21 close prices ending in
    rounded cents (e.g., last digit-of-cent in {0,5}) — price clustering = wider effective tick."""
    cents = (close * 100.0).round()
    last_digit = cents % 10
    clust = ((last_digit == 0) | (last_digit == 5)).astype(float)
    return clust.rolling(MDAYS, min_periods=WDAYS).mean().where(close.notna(), np.nan)


# ============================================================
# M — institutional / block-trade proxies (316-330)
# ============================================================

def f50_tdco_316_block_volume_day_indicator(volume: pd.Series) -> pd.Series:
    """1 if today's volume > 3x prior 50d avg — block-trade day (institutional flow proxy)."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    return (volume > 3.0 * vavg).astype(float).where(vavg.notna(), np.nan)


def f50_tdco_317_block_volume_day_count_252(volume: pd.Series) -> pd.Series:
    """Count of block-volume days in past 252 — yearly institutional-flow event count."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ev = (volume > 3.0 * vavg).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(vavg.notna(), np.nan)


def f50_tdco_318_block_volume_day_at_252h_indicator(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if block-volume day occurred WHILE price within 5% of 252d-high — institutional activity at top."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = high >= 0.95 * top
    return ((volume > 3.0 * vavg) & at_top).astype(float).where(vavg.notna() & top.notna(), np.nan)


def f50_tdco_319_block_volume_day_at_252h_count_252(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of block-volume-at-top days in past 252 — institutional-activity-at-peak count."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_top = high >= 0.95 * top
    ev = ((volume > 3.0 * vavg) & at_top).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(vavg.notna() & top.notna(), np.nan)


def f50_tdco_320_distribution_stick_day_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if open ~ low (open within 25% of range above low) AND wide range > 1.5x ATR(21) AND vol > 2x avg
    — classical distribution stick (institution selling into strength)."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    rng = high - low
    atr = _atr(high, low, close, MDAYS)
    open_near_low = (open <= low + 0.25 * rng)
    wide = rng > 1.5 * atr
    heavy = volume > 2.0 * vavg
    return (open_near_low & wide & heavy).astype(float).where(vavg.notna() & atr.notna(), np.nan)


def f50_tdco_321_distribution_stick_count_post_peak_63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution-stick days in 63 bars conditioned on being post-peak (within 252 of 252d high)."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    rng = high - low
    atr = _atr(high, low, close, MDAYS)
    open_near_low = (open <= low + 0.25 * rng)
    wide = rng > 1.5 * atr
    heavy = volume > 2.0 * vavg
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post_peak = (bs > 0) & (bs <= YDAYS)
    ev = (open_near_low & wide & heavy).astype(float).where(post_peak, np.nan)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f50_tdco_322_institutional_support_failure_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if close < SMA50 AND vol > 2x prior 50d avg — institutional-support failure (heavy break of trend)."""
    s50 = _sma(close, 50)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    return ((close < s50) & (volume > 2.0 * vavg)).astype(float).where(s50.notna() & vavg.notna(), np.nan)


def f50_tdco_323_institutional_support_failure_count_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of institutional-support-failure days in past 252."""
    s50 = _sma(close, 50)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ev = ((close < s50) & (volume > 2.0 * vavg)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(s50.notna() & vavg.notna(), np.nan)


def f50_tdco_324_quiet_selling_pattern_indicator(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if today's close < prior bar's low AND volume < 0.8x prior 50d avg — silent (low-vol) distribution.
    Sellers picking off bids without obvious distribution."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    lower_low = close < low.shift(1)
    quiet = volume < 0.8 * vavg
    return (lower_low & quiet).astype(float).where(vavg.notna(), np.nan)


def f50_tdco_325_quiet_selling_count_63(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of quiet-selling days in past 63 bars — silent-distribution density."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    lower_low = close < low.shift(1)
    quiet = volume < 0.8 * vavg
    ev = (lower_low & quiet).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(vavg.notna(), np.nan)


def f50_tdco_326_stealth_distribution_score_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Score over 63 bars: count of down-close days where vol within ±20% of prior-50d avg
    (no obvious distribution flag) BUT close < SMA21 — stealth-distribution density."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    s21 = _sma(close, MDAYS)
    down = close.diff() < 0
    normal_vol = (volume >= 0.8 * vavg) & (volume <= 1.2 * vavg)
    below_short_ma = close < s21
    ev = (down & normal_vol & below_short_ma).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(vavg.notna() & s21.notna(), np.nan)


def f50_tdco_327_absorption_failure_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if today's close < 21d-low AND it is the 3rd or later such test in past 63 bars
    — repeated support test that ultimately failed (absorption failure)."""
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    test = (close <= 1.02 * ll21).astype(float)
    test_count = test.rolling(QDAYS, min_periods=MDAYS).sum()
    fail = (close < ll21) & (test_count >= 3.0)
    return fail.astype(float).where(ll21.notna(), np.nan)


def f50_tdco_328_institutional_capitulation_proxy(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if vol > 5x prior 50d avg AND today's return < -5% AND close < SMA200
    — heavy-vol cascade down through major trend (institutional puke)."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ret = close.pct_change()
    s200 = _sma(close, 200)
    return ((volume > 5.0 * vavg) & (ret < -0.05) & (close < s200)).astype(float).where(vavg.notna() & s200.notna(), np.nan)


def f50_tdco_329_capitulation_count_post_peak_252(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of institutional-capitulation days in past 252 conditioned on being post-peak."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ret = close.pct_change()
    s200 = _sma(close, 200)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post_peak = (bs > 0) & (bs <= YDAYS)
    ev = ((volume > 5.0 * vavg) & (ret < -0.05) & (close < s200)).astype(float).where(post_peak, np.nan)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f50_tdco_330_weak_institutional_support_score_63(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Score over 63 bars: count of support tests (close <= 1.02 * 21d-low) that occurred on
    BELOW-average volume — weak buyer interest at support."""
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    test = (close <= 1.02 * ll21) & (close >= 0.98 * ll21)
    weak = volume < vavg
    ev = (test & weak).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum().where(vavg.notna() & ll21.notna(), np.nan)


# ============================================================
# N — Stage 4 / Weinstein death spiral (331-355)
# ============================================================

def f50_tdco_331_weinstein_stage_4_indicator(close: pd.Series) -> pd.Series:
    """Weinstein Stage 4: close < SMA30 AND SMA30 declining (SMA30 < SMA30 30d ago)
    — confirmed downtrend phase."""
    s30 = _sma(close, 30)
    return ((close < s30) & (s30 < s30.shift(30))).astype(float).where(s30.notna(), np.nan)


def f50_tdco_332_weinstein_stage_3_topping_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stage 3 topping: 63d high-low range tight (rel range < 15%), price near 63d high,
    AND flat SMA30 (|SMA30 slope|/close < 0.0005) — sideways consolidation near top before stage 4 breakdown."""
    s30 = _sma(close, 30)
    sl30 = _rolling_slope(s30, MDAYS)
    flat = (sl30.abs() / close) < 0.0005
    hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    rel_rng = _safe_div(hh - ll, close)
    near_top = close >= 0.9 * hh
    return (flat & (rel_rng < 0.15) & near_top).astype(float).where(s30.notna(), np.nan)


def f50_tdco_333_weinstein_stage_4_age_252(close: pd.Series) -> pd.Series:
    """Bars since most-recent ENTRY into Stage 4 (first bar where stage 4 became true after being false)."""
    s30 = _sma(close, 30)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    entry = stage4 & ~stage4.shift(1).fillna(False)
    return _bars_since_true(entry)


def f50_tdco_334_weinstein_stage_4_persistence_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars in Stage 4 — persistence of bearish regime."""
    s30 = _sma(close, 30)
    stage4 = ((close < s30) & (s30 < s30.shift(30))).astype(float)
    return stage4.rolling(YDAYS, min_periods=QDAYS).mean().where(s30.notna(), np.nan)


def f50_tdco_335_death_spiral_indicator_v1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if drawdown accelerating (63d-slope of drawdown > 0), vol expanding (|ret|-21 / |ret|-63 > 1.2),
    AND down-vol > up-vol over past 21 — death-spiral signature."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    dd_sl = _rolling_slope(dd, QDAYS)
    abs_ret = close.pct_change().abs()
    short_v = abs_ret.rolling(MDAYS, min_periods=WDAYS).mean()
    long_v = abs_ret.rolling(QDAYS, min_periods=MDAYS).mean()
    vol_exp = _safe_div(short_v, long_v) > 1.2
    diff = close.diff()
    dv = volume.where(diff < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    uv = volume.where(diff > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_dom = dv > uv
    return ((dd_sl > 0) & vol_exp & dn_dom).astype(float).where(rmax.notna(), np.nan)


def f50_tdco_336_death_spiral_count_252(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of death-spiral bars in past 252 — death-spiral persistence."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    dd_sl = _rolling_slope(dd, QDAYS)
    abs_ret = close.pct_change().abs()
    short_v = abs_ret.rolling(MDAYS, min_periods=WDAYS).mean()
    long_v = abs_ret.rolling(QDAYS, min_periods=MDAYS).mean()
    vol_exp = _safe_div(short_v, long_v) > 1.2
    diff = close.diff()
    dv = volume.where(diff < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    uv = volume.where(diff > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn_dom = dv > uv
    ev = ((dd_sl > 0) & vol_exp & dn_dom).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(rmax.notna(), np.nan)


def f50_tdco_337_death_spiral_intensity_score_63(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of 3 normalized components over 63 bars:
    drawdown level + (vol-expansion ratio - 1) + (down-vol fraction - 0.5) * 2."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    abs_ret = close.pct_change().abs()
    short_v = abs_ret.rolling(MDAYS, min_periods=WDAYS).mean()
    long_v = abs_ret.rolling(QDAYS, min_periods=MDAYS).mean()
    vol_exp = (_safe_div(short_v, long_v) - 1.0).clip(lower=0)
    diff = close.diff()
    dv = volume.where(diff < 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    uv = volume.where(diff > 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    dn_frac = _safe_div(dv, dv + uv)
    dn_term = (dn_frac - 0.5).clip(lower=0) * 2.0
    return (dd.fillna(0) + vol_exp.fillna(0) + dn_term.fillna(0)).rolling(QDAYS, min_periods=MDAYS).mean()


def f50_tdco_338_broken_bull_signature_v1(close: pd.Series) -> pd.Series:
    """1 if close < SMA200 AND SMA50 < SMA200 AND SMA50 declining (vs 50d ago) AND SMA200 declining
    — fully broken bull market signature."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    s50_decl = s50 < s50.shift(50)
    s200_decl = s200 < s200.shift(50)
    return ((close < s200) & (s50 < s200) & s50_decl & s200_decl).astype(float).where(s200.notna(), np.nan)


def f50_tdco_339_broken_bull_age_252(close: pd.Series) -> pd.Series:
    """Bars since most-recent entry into broken-bull signature."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    s50_decl = s50 < s50.shift(50)
    s200_decl = s200 < s200.shift(50)
    sig = (close < s200) & (s50 < s200) & s50_decl & s200_decl
    entry = sig & ~sig.shift(1).fillna(False)
    return _bars_since_true(entry)


def f50_tdco_340_broken_bull_persistence_252(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars in broken-bull state."""
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    s50_decl = s50 < s50.shift(50)
    s200_decl = s200 < s200.shift(50)
    sig = ((close < s200) & (s50 < s200) & s50_decl & s200_decl).astype(float)
    return sig.rolling(YDAYS, min_periods=QDAYS).mean().where(s200.notna(), np.nan)


def f50_tdco_341_markdown_phase_indicator_v2(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Markdown phase v2: 21d lower-low count >= 7 AND SMA50 declining AND down-vol > up-vol over 21d
    — Wyckoff markdown phase characterized by relentless lower-lows on heavier-down-vol."""
    l5 = low.rolling(WDAYS, min_periods=2).min()
    ll_count = (l5 < l5.shift(WDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    s50 = _sma(close, 50)
    s50_decl = s50 < s50.shift(MDAYS)
    diff = close.diff()
    dv = volume.where(diff < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    uv = volume.where(diff > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((ll_count >= 7.0) & s50_decl & (dv > uv)).astype(float).where(s50.notna(), np.nan)


def f50_tdco_342_markdown_phase_acceleration_v2(low: pd.Series, close: pd.Series) -> pd.Series:
    """Acceleration of markdown: 21d slope of (lower-low count over 21d) — increasing means decline accelerating."""
    l5 = low.rolling(WDAYS, min_periods=2).min()
    ll_count = (l5 < l5.shift(WDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_slope(ll_count, MDAYS)


def f50_tdco_343_stage_4_with_volume_confirmation_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if Stage-4 AND past 21d net-volume bias (down-up)/(down+up) > 0.2 — volume-confirmed Stage 4."""
    s30 = _sma(close, 30)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    diff = close.diff()
    dv = volume.where(diff < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    uv = volume.where(diff > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    bias = _safe_div(dv - uv, dv + uv)
    return (stage4 & (bias > 0.2)).astype(float).where(s30.notna(), np.nan)


def f50_tdco_344_stage_4_capitulation_count_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count in past 252 of (Stage-4 AND vol > 3x avg AND return < -5%) — Stage-4 capitulation events."""
    s30 = _sma(close, 30)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ret = close.pct_change()
    ev = (stage4 & (volume > 3.0 * vavg) & (ret < -0.05)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(s30.notna() & vavg.notna(), np.nan)


def f50_tdco_345_stage_4_recovery_failure_count_252(close: pd.Series) -> pd.Series:
    """Count of recovery attempts (close > SMA30 for at least 5 bars) that immediately re-entered Stage 4
    within 21 bars — recovery-failure during Stage 4."""
    s30 = _sma(close, 30)
    above = (close > s30).astype(float)
    above5 = above.rolling(WDAYS, min_periods=2).min()  # 5 consec days above
    re_below = (close < s30).astype(float)
    re_below21 = re_below.rolling(MDAYS, min_periods=WDAYS).max()
    # event: was above for 5 consec, then within 21 bars re-broke below
    ev = ((above5.shift(MDAYS).fillna(0) > 0) & (re_below21 > 0)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(s30.notna(), np.nan)


def f50_tdco_346_broken_bull_recovery_attempt_failure_rate_63(close: pd.Series) -> pd.Series:
    """Past 63 bars: PIT-clean failure rate of recovery attempts above SMA200.
    Attempt = bar where close crossed above SMA200. Failure-now = there was an attempt in past 10 bars
    AND we are currently back below SMA200. Rate = failures-now-count / attempts-count."""
    s200 = _sma(close, 200)
    cross_above = (close.shift(1) < s200.shift(1)) & (close > s200)
    attempt_past = cross_above.astype(float).rolling(10, min_periods=1).sum()
    failed_now = (attempt_past > 0) & (close < s200)
    attempts = cross_above.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    fails = failed_now.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(fails, attempts)


def f50_tdco_347_stage_4_pre_capitulation_score_63(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Score = stage-4 persistence(63) + (1 - vol_z63) (vol drying up) + drawdown depth — pre-capitulation setup."""
    s30 = _sma(close, 30)
    stage4 = ((close < s30) & (s30 < s30.shift(30))).astype(float)
    persistence = stage4.rolling(QDAYS, min_periods=MDAYS).mean()
    vol_z = _rolling_zscore(volume, QDAYS, min_periods=MDAYS)
    vol_dry = (-vol_z).clip(lower=0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax).clip(lower=0)
    return (persistence + 0.3 * vol_dry + dd).where(s30.notna(), np.nan)


def f50_tdco_348_stage_4_terminal_acceleration_proxy(low: pd.Series, close: pd.Series) -> pd.Series:
    """In Stage 4: 21d return / (21d return 21 bars ago) — ratio > 1 in magnitude indicates accelerating decline."""
    s30 = _sma(close, 30)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    r21 = close.pct_change(MDAYS)
    accel = _safe_div(r21.abs(), r21.shift(MDAYS).abs())
    sign = np.where(r21 < 0, 1.0, -1.0)
    out = (pd.Series(sign, index=close.index) * accel).where(stage4, np.nan)
    return out


def f50_tdco_349_stage_4_volume_pattern_distribution_dominant(close: pd.Series, volume: pd.Series) -> pd.Series:
    """In Stage 4: fraction of past 63 bars where down-vol > up-vol — distribution-dominance in markdown."""
    s30 = _sma(close, 30)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    diff = close.diff()
    dv = volume.where(diff < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    uv = volume.where(diff > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    dom = (dv > uv).astype(float).where(stage4, np.nan)
    return dom.rolling(QDAYS, min_periods=MDAYS).mean()


def f50_tdco_350_stage_4_basket_signal_count(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Stage-4-related signals currently active:
    {stage4, close<SMA200, SMA50<SMA200, persistence>0.5, down-vol-dom-21}."""
    s30 = _sma(close, 30)
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    stage4 = (close < s30) & (s30 < s30.shift(30))
    pers = stage4.astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    diff = close.diff()
    dv = volume.where(diff < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    uv = volume.where(diff > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    dom = dv > uv
    cnt = (stage4.astype(float).fillna(0)
           + (close < s200).astype(float).fillna(0)
           + (s50 < s200).astype(float).fillna(0)
           + (pers > 0.5).astype(float).fillna(0)
           + dom.astype(float).fillna(0))
    return cnt.where(s200.notna(), np.nan)


def f50_tdco_351_catastrophic_decline_signature_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    """1 if drawdown from 252d peak > 50% achieved within 63 bars of peak AND still declining (sl<0)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    dd = _safe_div(rmax - close, rmax)
    sl = _rolling_slope(close, MDAYS)
    return ((dd > 0.5) & (bs <= QDAYS) & (sl < 0)).astype(float).where(rmax.notna(), np.nan)


def f50_tdco_352_secular_bear_market_proxy_indicator(close: pd.Series) -> pd.Series:
    """Multi-quarter decline: close < SMA200 AND SMA200 declining over each of past 4 quarters
    (SMA200 < SMA200.shift(63) for current and 3 lagged checkpoints)."""
    s200 = _sma(close, 200)
    cond = (close < s200)
    for k in (0, QDAYS, 2 * QDAYS, 3 * QDAYS):
        cond = cond & (s200.shift(k) < s200.shift(k + QDAYS))
    return cond.astype(float).where(s200.notna(), np.nan)


def f50_tdco_353_trend_exhaustion_terminal_score_v3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of: drawdown_252 >= 0.3, bars_since_peak > 126, lower-low-streak >= 5, close < SMA200, SMA50<SMA200."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    dd = _safe_div(rmax - close, rmax)
    l5 = low.rolling(WDAYS, min_periods=2).min()
    ll_streak = _streak_true(l5 < l5.shift(WDAYS))
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    return ((dd >= 0.3).astype(float).fillna(0)
            + (bs > 126).astype(float).fillna(0)
            + (ll_streak >= 5).astype(float).fillna(0)
            + (close < s200).astype(float).fillna(0)
            + (s50 < s200).astype(float).fillna(0)).where(s200.notna(), np.nan)


def f50_tdco_354_broken_trend_reflexive_decline_indicator(close: pd.Series) -> pd.Series:
    """1 if 5d return < -8% AND close just broke below SMA200 within past 21 bars AND has been below it since.
    Reflexive cascade after major trend break."""
    s200 = _sma(close, 200)
    cross_below = (close.shift(1) >= s200.shift(1)) & (close < s200)
    crossed_recent = cross_below.rolling(MDAYS, min_periods=1).sum() > 0
    below_since = (close < s200).rolling(MDAYS, min_periods=1).min() > 0
    fast_drop = close.pct_change(WDAYS) < -0.08
    return (fast_drop & crossed_recent & below_since).astype(float).where(s200.notna(), np.nan)


def f50_tdco_355_cascade_failure_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if all of: close broke 21d low, 63d low, and 252d low within past 21 bars (in sequence) — cascade of broken supports."""
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    ll252 = low.shift(1).rolling(YDAYS, min_periods=QDAYS).min()
    br21 = (close < ll21).astype(float).rolling(MDAYS, min_periods=1).max()
    br63 = (close < ll63).astype(float).rolling(MDAYS, min_periods=1).max()
    br252 = (close < ll252).astype(float).rolling(MDAYS, min_periods=1).max()
    return ((br21 > 0) & (br63 > 0) & (br252 > 0)).astype(float).where(ll252.notna(), np.nan)


# ============================================================
# O — range / structural decay (356-375)
# ============================================================

def f50_tdco_356_atr_expansion_ratio_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / mean(ATR(21), 252d) — vol expansion vs annual baseline."""
    atr = _atr(high, low, close, MDAYS)
    return _safe_div(atr, atr.rolling(YDAYS, min_periods=QDAYS).mean())


def f50_tdco_357_atr_expansion_persistence_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars where ATR-expansion-ratio-252 > 1.2 — persistent vol expansion."""
    atr = _atr(high, low, close, MDAYS)
    ratio = _safe_div(atr, atr.rolling(YDAYS, min_periods=QDAYS).mean())
    return (ratio > 1.2).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(atr.notna(), np.nan)


def f50_tdco_358_range_of_range_63(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of daily ranges (H-L) over 63 — variability of daily-range itself (vol-of-range)."""
    rng = high - low
    return rng.rolling(QDAYS, min_periods=MDAYS).std()


def f50_tdco_359_range_of_range_zscore_252(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score (252d) of range-of-range-63 — extreme regime in range variability."""
    rng = high - low
    ror = rng.rolling(QDAYS, min_periods=MDAYS).std()
    return _rolling_zscore(ror, YDAYS, min_periods=QDAYS)


def f50_tdco_360_gap_density_at_top_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in past 63 where |open-prior close|/prior close > 2% AND price within 2% of 252d-high.
    Gap density at the top — distribution turbulence near peak.
    Uses (high-prior close) and (prior close - high.shift)-like proxy via close-to-close gap > 2%."""
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = high >= 0.98 * top
    gap = (close - close.shift(1)).abs() / close.shift(1)
    big_gap = gap > 0.02
    return (big_gap & near_top).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(top.notna(), np.nan)


def f50_tdco_361_gap_density_post_peak_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past 63 bars with |return| > 2% conditioned on being post-peak (bars-since-252h > 0)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post_peak = (bs > 0) & (bs <= YDAYS)
    gap = close.pct_change().abs() > 0.02
    return gap.astype(float).where(post_peak, np.nan).rolling(QDAYS, min_periods=MDAYS).sum()


def f50_tdco_362_gap_down_density_post_peak_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of past 63 bars with return < -2% conditioned on post-peak — gap-down clustering after peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post_peak = (bs > 0) & (bs <= YDAYS)
    gap_dn = close.pct_change() < -0.02
    return gap_dn.astype(float).where(post_peak, np.nan).rolling(QDAYS, min_periods=MDAYS).sum()


def f50_tdco_363_lower_low_frequency_acceleration_63(low: pd.Series) -> pd.Series:
    """63d slope of (rolling-21 fraction of lower-low days) — accelerating lower-low frequency."""
    l5 = low.rolling(WDAYS, min_periods=2).min()
    ll = (l5 < l5.shift(WDAYS)).astype(float)
    freq = ll.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_slope(freq, QDAYS)


def f50_tdco_364_lower_low_clustering_score_63(low: pd.Series) -> pd.Series:
    """Score: max-consecutive lower-low run in past 63 / 63 — clustering of LL events."""
    l5 = low.rolling(WDAYS, min_periods=2).min()
    ll = l5 < l5.shift(WDAYS)
    max_streak = _streak_true(ll).rolling(QDAYS, min_periods=MDAYS).max()
    return max_streak / float(QDAYS)


def f50_tdco_365_average_true_range_pct_close_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of (ATR-21 / close) — extreme vol-pct regime."""
    atr_pct = _safe_div(_atr(high, low, close, MDAYS), close)
    return _rolling_zscore(atr_pct, YDAYS, min_periods=QDAYS)


def f50_tdco_366_range_to_atr_ratio_at_top_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At bars within 5% of 252d-high in past 63: average (daily range / ATR21) — outlier-bar prevalence at top."""
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = high >= 0.95 * top
    rng = high - low
    atr = _atr(high, low, close, MDAYS)
    r = _safe_div(rng, atr).where(near_top, np.nan)
    return r.rolling(QDAYS, min_periods=MDAYS).mean()


def f50_tdco_367_widerange_red_bar_density_post_peak_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count in past 63 of bars where (H-L) > 1.5x ATR21 AND close < open(prev_close proxy) AND post-peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post_peak = (bs > 0) & (bs <= YDAYS)
    rng = high - low
    atr = _atr(high, low, close, MDAYS)
    wide = rng > 1.5 * atr
    red = close < close.shift(1)
    ev = (wide & red).astype(float).where(post_peak, np.nan)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f50_tdco_368_narrow_range_consolidation_at_top_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of narrow-range bars (range < 0.5x ATR21) WHILE price within 5% of 252d-high in past 63."""
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    near_top = high >= 0.95 * top
    rng = high - low
    atr = _atr(high, low, close, MDAYS)
    narrow = rng < 0.5 * atr
    return (narrow & near_top).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(top.notna(), np.nan)


def f50_tdco_369_narrow_range_then_widerange_breakdown_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (today's range > 2x ATR21) AND (mean range over prior 5 bars < 0.7x ATR21) AND today is down
    — coil-then-break pattern."""
    rng = high - low
    atr = _atr(high, low, close, MDAYS)
    today_wide = rng > 2.0 * atr
    prior5_narrow = rng.shift(1).rolling(WDAYS, min_periods=2).mean() < 0.7 * atr
    down = close < close.shift(1)
    return (today_wide & prior5_narrow & down).astype(float).where(atr.notna(), np.nan)


def f50_tdco_370_expansion_contraction_ratio_63(high: pd.Series, low: pd.Series) -> pd.Series:
    """(mean of top-50% daily ranges in 63) / (mean of bottom-50% daily ranges in 63) — vol-asymmetry magnitude."""
    rng = high - low
    med = rng.rolling(QDAYS, min_periods=MDAYS).median()
    top_mean = rng.where(rng >= med).rolling(QDAYS, min_periods=MDAYS).mean()
    bot_mean = rng.where(rng < med).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(top_mean, bot_mean)


def f50_tdco_371_volatility_regime_shift_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score (252d) of (std of returns over 21) / (std of returns over 252) — vol-regime shift indicator."""
    ret = close.pct_change()
    s21 = ret.rolling(MDAYS, min_periods=WDAYS).std()
    s252 = ret.rolling(YDAYS, min_periods=QDAYS).std()
    ratio = _safe_div(s21, s252)
    return _rolling_zscore(ratio, YDAYS, min_periods=QDAYS)


def f50_tdco_372_vol_skew_post_peak_decay_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """In post-peak window: 63d rolling skew of returns — negative & growing-more-negative = down-vol dominant."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post_peak = (bs > 0) & (bs <= YDAYS)
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).skew()
    return sk.where(post_peak, np.nan)


def f50_tdco_373_close_to_close_distance_decay_63(close: pd.Series) -> pd.Series:
    """63d slope of mean(|close - close.shift(1)|) — rising = larger close-to-close moves (decay of orderly trend)."""
    abs_move = (close - close.shift(1)).abs()
    smooth = abs_move.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_slope(smooth, QDAYS)


def f50_tdco_374_high_to_low_distance_decay_63(high: pd.Series, low: pd.Series) -> pd.Series:
    """63d slope of mean daily range (H-L) — rising = expanding ranges, structural decay."""
    rng = high - low
    smooth = rng.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_slope(smooth, QDAYS)


def f50_tdco_375_daily_range_dispersion_post_peak_63(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std-of-ranges over past 63 conditioned on being post-peak — increased range dispersion = post-peak chaos.
    Computed always; gating done by post-peak mask: NaN if not post-peak."""
    bs_proxy = _bars_since_true(high == high.rolling(YDAYS, min_periods=QDAYS).max())
    post_peak = (bs_proxy > 0) & (bs_proxy <= YDAYS)
    rng = high - low
    disp = rng.rolling(QDAYS, min_periods=MDAYS).std()
    return disp.where(post_peak, np.nan)


# ============================================================
#                         REGISTRY 301-375
# ============================================================

TERMINAL_DISTRIBUTION_COMPOSITE_BASE_REGISTRY_301_375 = {
    "f50_tdco_301_amihud_illiquidity_proxy_21": {"inputs": ["close", "volume"], "func": f50_tdco_301_amihud_illiquidity_proxy_21},
    "f50_tdco_302_amihud_illiquidity_proxy_63": {"inputs": ["close", "volume"], "func": f50_tdco_302_amihud_illiquidity_proxy_63},
    "f50_tdco_303_amihud_illiquidity_zscore_252": {"inputs": ["close", "volume"], "func": f50_tdco_303_amihud_illiquidity_zscore_252},
    "f50_tdco_304_amihud_illiquidity_rising_state_63": {"inputs": ["close", "volume"], "func": f50_tdco_304_amihud_illiquidity_rising_state_63},
    "f50_tdco_305_roll_spread_proxy_21": {"inputs": ["close"], "func": f50_tdco_305_roll_spread_proxy_21},
    "f50_tdco_306_roll_spread_zscore_252": {"inputs": ["close"], "func": f50_tdco_306_roll_spread_zscore_252},
    "f50_tdco_307_corwin_schultz_spread_proxy_2bar": {"inputs": ["high", "low"], "func": f50_tdco_307_corwin_schultz_spread_proxy_2bar},
    "f50_tdco_308_corwin_schultz_zscore_252": {"inputs": ["high", "low"], "func": f50_tdco_308_corwin_schultz_zscore_252},
    "f50_tdco_309_abdi_ranaldi_spread_proxy_2bar": {"inputs": ["high", "low", "close"], "func": f50_tdco_309_abdi_ranaldi_spread_proxy_2bar},
    "f50_tdco_310_high_low_range_volume_ratio_decay_63": {"inputs": ["high", "low", "volume"], "func": f50_tdco_310_high_low_range_volume_ratio_decay_63},
    "f50_tdco_311_turnover_decay_post_peak_63": {"inputs": ["high", "volume"], "func": f50_tdco_311_turnover_decay_post_peak_63},
    "f50_tdco_312_volume_volatility_ratio_decay_63": {"inputs": ["volume"], "func": f50_tdco_312_volume_volatility_ratio_decay_63},
    "f50_tdco_313_dollar_volume_decay_velocity_63": {"inputs": ["close", "volume"], "func": f50_tdco_313_dollar_volume_decay_velocity_63},
    "f50_tdco_314_dollar_volume_zscore_below_q25_state": {"inputs": ["close", "volume"], "func": f50_tdco_314_dollar_volume_zscore_below_q25_state},
    "f50_tdco_315_effective_tick_size_proxy_21": {"inputs": ["close"], "func": f50_tdco_315_effective_tick_size_proxy_21},
    "f50_tdco_316_block_volume_day_indicator": {"inputs": ["volume"], "func": f50_tdco_316_block_volume_day_indicator},
    "f50_tdco_317_block_volume_day_count_252": {"inputs": ["volume"], "func": f50_tdco_317_block_volume_day_count_252},
    "f50_tdco_318_block_volume_day_at_252h_indicator": {"inputs": ["high", "volume"], "func": f50_tdco_318_block_volume_day_at_252h_indicator},
    "f50_tdco_319_block_volume_day_at_252h_count_252": {"inputs": ["high", "volume"], "func": f50_tdco_319_block_volume_day_at_252h_count_252},
    "f50_tdco_320_distribution_stick_day_indicator": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_320_distribution_stick_day_indicator},
    "f50_tdco_321_distribution_stick_count_post_peak_63": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_321_distribution_stick_count_post_peak_63},
    "f50_tdco_322_institutional_support_failure_indicator": {"inputs": ["close", "volume"], "func": f50_tdco_322_institutional_support_failure_indicator},
    "f50_tdco_323_institutional_support_failure_count_252": {"inputs": ["close", "volume"], "func": f50_tdco_323_institutional_support_failure_count_252},
    "f50_tdco_324_quiet_selling_pattern_indicator": {"inputs": ["low", "close", "volume"], "func": f50_tdco_324_quiet_selling_pattern_indicator},
    "f50_tdco_325_quiet_selling_count_63": {"inputs": ["low", "close", "volume"], "func": f50_tdco_325_quiet_selling_count_63},
    "f50_tdco_326_stealth_distribution_score_63": {"inputs": ["close", "volume"], "func": f50_tdco_326_stealth_distribution_score_63},
    "f50_tdco_327_absorption_failure_indicator": {"inputs": ["low", "close"], "func": f50_tdco_327_absorption_failure_indicator},
    "f50_tdco_328_institutional_capitulation_proxy": {"inputs": ["close", "volume"], "func": f50_tdco_328_institutional_capitulation_proxy},
    "f50_tdco_329_capitulation_count_post_peak_252": {"inputs": ["high", "close", "volume"], "func": f50_tdco_329_capitulation_count_post_peak_252},
    "f50_tdco_330_weak_institutional_support_score_63": {"inputs": ["low", "close", "volume"], "func": f50_tdco_330_weak_institutional_support_score_63},
    "f50_tdco_331_weinstein_stage_4_indicator": {"inputs": ["close"], "func": f50_tdco_331_weinstein_stage_4_indicator},
    "f50_tdco_332_weinstein_stage_3_topping_indicator": {"inputs": ["high", "low", "close"], "func": f50_tdco_332_weinstein_stage_3_topping_indicator},
    "f50_tdco_333_weinstein_stage_4_age_252": {"inputs": ["close"], "func": f50_tdco_333_weinstein_stage_4_age_252},
    "f50_tdco_334_weinstein_stage_4_persistence_252": {"inputs": ["close"], "func": f50_tdco_334_weinstein_stage_4_persistence_252},
    "f50_tdco_335_death_spiral_indicator_v1": {"inputs": ["high", "close", "volume"], "func": f50_tdco_335_death_spiral_indicator_v1},
    "f50_tdco_336_death_spiral_count_252": {"inputs": ["high", "close", "volume"], "func": f50_tdco_336_death_spiral_count_252},
    "f50_tdco_337_death_spiral_intensity_score_63": {"inputs": ["high", "close", "volume"], "func": f50_tdco_337_death_spiral_intensity_score_63},
    "f50_tdco_338_broken_bull_signature_v1": {"inputs": ["close"], "func": f50_tdco_338_broken_bull_signature_v1},
    "f50_tdco_339_broken_bull_age_252": {"inputs": ["close"], "func": f50_tdco_339_broken_bull_age_252},
    "f50_tdco_340_broken_bull_persistence_252": {"inputs": ["close"], "func": f50_tdco_340_broken_bull_persistence_252},
    "f50_tdco_341_markdown_phase_indicator_v2": {"inputs": ["low", "close", "volume"], "func": f50_tdco_341_markdown_phase_indicator_v2},
    "f50_tdco_342_markdown_phase_acceleration_v2": {"inputs": ["low", "close"], "func": f50_tdco_342_markdown_phase_acceleration_v2},
    "f50_tdco_343_stage_4_with_volume_confirmation_indicator": {"inputs": ["close", "volume"], "func": f50_tdco_343_stage_4_with_volume_confirmation_indicator},
    "f50_tdco_344_stage_4_capitulation_count_252": {"inputs": ["close", "volume"], "func": f50_tdco_344_stage_4_capitulation_count_252},
    "f50_tdco_345_stage_4_recovery_failure_count_252": {"inputs": ["close"], "func": f50_tdco_345_stage_4_recovery_failure_count_252},
    "f50_tdco_346_broken_bull_recovery_attempt_failure_rate_63": {"inputs": ["close"], "func": f50_tdco_346_broken_bull_recovery_attempt_failure_rate_63},
    "f50_tdco_347_stage_4_pre_capitulation_score_63": {"inputs": ["high", "close", "volume"], "func": f50_tdco_347_stage_4_pre_capitulation_score_63},
    "f50_tdco_348_stage_4_terminal_acceleration_proxy": {"inputs": ["low", "close"], "func": f50_tdco_348_stage_4_terminal_acceleration_proxy},
    "f50_tdco_349_stage_4_volume_pattern_distribution_dominant": {"inputs": ["close", "volume"], "func": f50_tdco_349_stage_4_volume_pattern_distribution_dominant},
    "f50_tdco_350_stage_4_basket_signal_count": {"inputs": ["close", "volume"], "func": f50_tdco_350_stage_4_basket_signal_count},
    "f50_tdco_351_catastrophic_decline_signature_indicator": {"inputs": ["high", "close"], "func": f50_tdco_351_catastrophic_decline_signature_indicator},
    "f50_tdco_352_secular_bear_market_proxy_indicator": {"inputs": ["close"], "func": f50_tdco_352_secular_bear_market_proxy_indicator},
    "f50_tdco_353_trend_exhaustion_terminal_score_v3": {"inputs": ["high", "low", "close"], "func": f50_tdco_353_trend_exhaustion_terminal_score_v3},
    "f50_tdco_354_broken_trend_reflexive_decline_indicator": {"inputs": ["close"], "func": f50_tdco_354_broken_trend_reflexive_decline_indicator},
    "f50_tdco_355_cascade_failure_indicator": {"inputs": ["low", "close"], "func": f50_tdco_355_cascade_failure_indicator},
    "f50_tdco_356_atr_expansion_ratio_252": {"inputs": ["high", "low", "close"], "func": f50_tdco_356_atr_expansion_ratio_252},
    "f50_tdco_357_atr_expansion_persistence_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_357_atr_expansion_persistence_63},
    "f50_tdco_358_range_of_range_63": {"inputs": ["high", "low"], "func": f50_tdco_358_range_of_range_63},
    "f50_tdco_359_range_of_range_zscore_252": {"inputs": ["high", "low"], "func": f50_tdco_359_range_of_range_zscore_252},
    "f50_tdco_360_gap_density_at_top_63": {"inputs": ["high", "close"], "func": f50_tdco_360_gap_density_at_top_63},
    "f50_tdco_361_gap_density_post_peak_63": {"inputs": ["high", "close"], "func": f50_tdco_361_gap_density_post_peak_63},
    "f50_tdco_362_gap_down_density_post_peak_63": {"inputs": ["high", "close"], "func": f50_tdco_362_gap_down_density_post_peak_63},
    "f50_tdco_363_lower_low_frequency_acceleration_63": {"inputs": ["low"], "func": f50_tdco_363_lower_low_frequency_acceleration_63},
    "f50_tdco_364_lower_low_clustering_score_63": {"inputs": ["low"], "func": f50_tdco_364_lower_low_clustering_score_63},
    "f50_tdco_365_average_true_range_pct_close_zscore_252": {"inputs": ["high", "low", "close"], "func": f50_tdco_365_average_true_range_pct_close_zscore_252},
    "f50_tdco_366_range_to_atr_ratio_at_top_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_366_range_to_atr_ratio_at_top_63},
    "f50_tdco_367_widerange_red_bar_density_post_peak_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_367_widerange_red_bar_density_post_peak_63},
    "f50_tdco_368_narrow_range_consolidation_at_top_count_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_368_narrow_range_consolidation_at_top_count_63},
    "f50_tdco_369_narrow_range_then_widerange_breakdown_indicator": {"inputs": ["high", "low", "close"], "func": f50_tdco_369_narrow_range_then_widerange_breakdown_indicator},
    "f50_tdco_370_expansion_contraction_ratio_63": {"inputs": ["high", "low"], "func": f50_tdco_370_expansion_contraction_ratio_63},
    "f50_tdco_371_volatility_regime_shift_zscore_252": {"inputs": ["close"], "func": f50_tdco_371_volatility_regime_shift_zscore_252},
    "f50_tdco_372_vol_skew_post_peak_decay_63": {"inputs": ["high", "close"], "func": f50_tdco_372_vol_skew_post_peak_decay_63},
    "f50_tdco_373_close_to_close_distance_decay_63": {"inputs": ["close"], "func": f50_tdco_373_close_to_close_distance_decay_63},
    "f50_tdco_374_high_to_low_distance_decay_63": {"inputs": ["high", "low"], "func": f50_tdco_374_high_to_low_distance_decay_63},
    "f50_tdco_375_daily_range_dispersion_post_peak_63": {"inputs": ["high", "low"], "func": f50_tdco_375_daily_range_dispersion_post_peak_63},
}
