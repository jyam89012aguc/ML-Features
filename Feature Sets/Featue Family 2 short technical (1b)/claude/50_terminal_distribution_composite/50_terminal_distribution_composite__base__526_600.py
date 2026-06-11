"""terminal_distribution_composite base features 526-600 — Pipeline 1b-technical.

ML-engineered residuals + ensemble-of-ensembles + cross-pattern v4 + spectral + v4 masters.
75 hypotheses for stuck-stock (-80% DD, no recovery > -50% in 5y).
PIT-clean. ALL helpers at module top, NO nested defs. Composites use _h_* helpers only.
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


# ---------------------------- standard helpers ----------------------------

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


# ---------------------------- domain helpers (module-level) ----------------------------

def _h_drawdown(high, close, n):
    rmax = high.rolling(n, min_periods=max(n // 3, 5)).max()
    return _safe_div(rmax - close, rmax)


def _h_dist_day_count(close, volume, window=25):
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = ((ret < -0.002) & (volume > vavg)).astype(float)
    return dd.rolling(window, min_periods=max(window // 3, 5)).sum()


def _h_stage4_mask(close):
    s30 = _sma(close, 30)
    return (close < s30) & (s30 < s30.shift(30))


def _h_breakdown_21(low, close):
    ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    return close < ll21


def _h_breakdown_63(low, close):
    ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    return close < ll63


def _h_breakdown_252(low, close):
    ll252 = low.shift(1).rolling(YDAYS, min_periods=QDAYS).min()
    return close < ll252


def _h_lh_streak(high, n=WDAYS):
    h_n = high.rolling(n, min_periods=2).max()
    return _streak_true(h_n < h_n.shift(n))


def _h_ll_streak(low, n=WDAYS):
    l_n = low.rolling(n, min_periods=2).min()
    return _streak_true(l_n < l_n.shift(n))


def _h_wyckoff_upthrust(high, low, close):
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return (high > h21) & (close < h21)


def _h_wyckoff_upthrust_count_63(high, low, close):
    return _h_wyckoff_upthrust(high, low, close).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def _h_corwin_schultz(high, low):
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    beta_t = np.log(_safe_div(high, low).clip(lower=1e-9)) ** 2
    beta_t1 = np.log(_safe_div(high.shift(1), low.shift(1)).clip(lower=1e-9)) ** 2
    beta = beta_t + beta_t1
    gamma = np.log(_safe_div(h2, l2).clip(lower=1e-9)) ** 2
    a_sqrt2 = np.sqrt(2.0)
    alpha = (np.sqrt(beta.clip(lower=0)) * (a_sqrt2 - 1.0) - np.sqrt(gamma.clip(lower=0))) / (3.0 - 2.0 * a_sqrt2)
    spread = 2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))
    return spread.clip(lower=0)


def _h_amihud(close, volume, n):
    ret = close.pct_change().abs()
    dv = (close * volume).replace(0, np.nan)
    return (ret / dv).rolling(n, min_periods=max(n // 3, 5)).mean()


def _h_skew_kernel(w):
    if np.isnan(w).any() or len(w) < 4:
        return np.nan
    sd = np.std(w)
    if sd == 0 or np.isnan(sd):
        return np.nan
    return float(np.mean(((w - np.mean(w)) / sd) ** 3))


def _h_kurt_kernel(w):
    if np.isnan(w).any() or len(w) < 4:
        return np.nan
    sd = np.std(w)
    if sd == 0 or np.isnan(sd):
        return np.nan
    return float(np.mean(((w - np.mean(w)) / sd) ** 4) - 3.0)


def _h_rolling_pct_rank(s, window, min_periods=None):
    """Rank-based percentile of last value within rolling window."""
    if min_periods is None:
        min_periods = max(window // 3, 5)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


def _h_winsorize_zscore(s, window=YDAYS, pct=0.05):
    """Winsorize at given pct then z-score over window."""
    lo = s.rolling(window, min_periods=max(window // 3, 5)).quantile(pct)
    hi = s.rolling(window, min_periods=max(window // 3, 5)).quantile(1.0 - pct)
    s_w = s.clip(lower=lo, upper=hi)
    return _rolling_zscore(s_w, window)


def _h_residualize_via_slope(target, regressor, window):
    """Compute residual = target - (intercept + slope * regressor) using rolling-window OLS.
    Approximate via: slope = cov(target, regressor)/var(regressor); intercept = mean(target) - slope*mean(regressor).
    """
    mp = max(window // 3, 5)
    mt = target.rolling(window, min_periods=mp).mean()
    mr = regressor.rolling(window, min_periods=mp).mean()
    vr = regressor.rolling(window, min_periods=mp).var()
    cv = target.rolling(window, min_periods=mp).cov(regressor)
    slope = _safe_div(cv, vr)
    intercept = mt - slope * mr
    pred = intercept + slope * regressor
    return target - pred


def _h_basket_dist_breakdown(close, volume):
    """Distribution-basket ensemble: sum of dist-25 + dist-50 + heavy-down-day-count-25 / 3 — broad dist basket."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ddm = ((ret < -0.002) & (volume > vavg)).astype(float)
    d25 = ddm.rolling(25, min_periods=10).sum()
    d50 = ddm.rolling(50, min_periods=15).sum()
    heavy = ((ret < -0.01) & (volume > 1.5 * vavg)).astype(float).rolling(25, min_periods=10).sum()
    return (d25 + d50 / 2.0 + heavy) / 3.0


def _h_basket_wyckoff(high, low, close, volume):
    """Wyckoff basket: upthrust count + no-demand count + climactic-action count over 63 — normalized."""
    upth = _h_wyckoff_upthrust(high, low, close).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    rng = high - low
    rng_med = rng.rolling(MDAYS, min_periods=WDAYS).median()
    nd = ((rng < 0.7 * rng_med) & (volume < 0.8 * vavg) & (close > close.shift(1))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    cli = ((rng > 2.0 * rng_med) & (volume > 2.0 * vavg)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return (upth + nd + cli) / 3.0


def _h_basket_candle(open, high, low, close):
    """Candle basket: count of bearish candle patterns (engulf, shooting-star, dark-cloud) over 63."""
    body = (close - open).abs()
    upper = high - pd.concat([open.rename("a"), close.rename("b")], axis=1).max(axis=1)
    engulf = ((close < open) & (open >= close.shift(1)) & (close < open.shift(1))).astype(float)
    ss = ((close < open) & (upper > 2.0 * body) & (body > 0)).astype(float)
    dc = ((open > close.shift(1)) & (close < (open.shift(1) + close.shift(1)) / 2.0) & (close < open)).astype(float)
    en63 = engulf.rolling(QDAYS, min_periods=MDAYS).sum()
    ss63 = ss.rolling(QDAYS, min_periods=MDAYS).sum()
    dc63 = dc.rolling(QDAYS, min_periods=MDAYS).sum()
    return (en63 + ss63 + dc63) / 3.0


def _h_basket_multi_bar(high, low, close):
    """Multi-bar pattern basket: 3-bar lower-low count + 3-bar lower-high count + lh-streak — over 63."""
    h_lh = ((high < high.shift(1)) & (high.shift(1) < high.shift(2))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    l_ll = ((low < low.shift(1)) & (low.shift(1) < low.shift(2))).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    lh_st = _h_lh_streak(high)
    return (h_lh / 10.0 + l_ll / 10.0 + lh_st / 30.0)


def _h_basket_drawdown(high, close):
    """Drawdown basket: dd_21 + dd_63 + dd_252 summed (multi-scale drawdown magnitude)."""
    dd21 = _h_drawdown(high, close, MDAYS).clip(lower=0)
    dd63 = _h_drawdown(high, close, QDAYS).clip(lower=0)
    dd252 = _h_drawdown(high, close, YDAYS).clip(lower=0)
    return dd21.fillna(0) + dd63.fillna(0) + dd252.fillna(0)


def _h_basket_breakdown(low, close):
    """Breakdown basket: count over 63 of breakdowns of 21/63/252 lows, summed."""
    b21 = _h_breakdown_21(low, close).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    b63 = _h_breakdown_63(low, close).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    b252 = _h_breakdown_252(low, close).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return b21.fillna(0) + b63.fillna(0) + b252.fillna(0)


def _h_basket_microstructure(high, low, close, volume):
    """Microstructure decay basket: amihud(63) + corwin-schultz + (volume / atr_21 decay)."""
    am = _h_amihud(close, volume, QDAYS)
    cs = _h_corwin_schultz(high, low)
    atr21 = _atr(high, low, close, MDAYS)
    vpa = _safe_div(volume, atr21).rolling(MDAYS, min_periods=WDAYS).mean()
    vpa_decay = -_rolling_slope(vpa, QDAYS)  # negative slope of vpa = positive decay
    am_z = _rolling_zscore(am, YDAYS).fillna(0)
    cs_z = _rolling_zscore(cs, YDAYS).fillna(0)
    vd_z = _rolling_zscore(vpa_decay, YDAYS).fillna(0)
    return (am_z + cs_z + vd_z) / 3.0


def _h_basket_institutional(close, volume):
    """Institutional basket: stealth-distribution count + block-volume-day count + chronic-weakness fraction."""
    s21 = _sma(close, MDAYS)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    down = close.diff() < 0
    normal_vol = (volume >= 0.8 * vavg) & (volume <= 1.2 * vavg)
    stealth = (down & normal_vol & (close < s21)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    block = (volume > 3.0 * vavg).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    s50 = _sma(close, 50)
    weak = (close < s50).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return (stealth / 10.0 + block / 10.0 + weak)


def _h_basket_stage4(close, volume):
    """Stage-4 basket: stage-4 state + stage-4 age normalized + close < SMA200 fraction."""
    stg4 = _h_stage4_mask(close).astype(float)
    entry = stg4.diff().fillna(0) > 0
    age = _bars_since_true(entry) / float(YDAYS)
    s200 = _sma(close, 200)
    below_200 = (close < s200).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return stg4.fillna(0) + age.fillna(0).clip(upper=2.0) + below_200.fillna(0)


def _h_basket_cycle_phase(high, low, close, volume):
    """Cycle-phase basket: late-cycle indicator + cycle-end count / 50 + cycle-terminal indicator."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    pos = bs_min / float(YDAYS)
    late = (pos > 0.85).astype(float)
    s50 = _sma(close, 50)
    cyc_end = ((pos > 0.8) & (close < s50)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum() / 50.0
    dd = _h_drawdown(high, close, YDAYS)
    s200 = _sma(close, 200)
    cyc_term = ((pos > 0.85) & (dd > 0.30) & (close < s200)).astype(float)
    return late.fillna(0) + cyc_end.fillna(0) + cyc_term.fillna(0)




def f50_tdco_526_distribution_signal_residual_after_removing_trend_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    dist = _h_dist_day_count(close, volume, 25)
    trend = _rolling_slope(close, QDAYS)
    return _h_residualize_via_slope(dist, trend, YDAYS)


def f50_tdco_527_breakdown_signal_residual_after_removing_drawdown_63(low: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    bcount = _h_breakdown_63(low, close).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    dd = _h_drawdown(high, close, YDAYS)
    return _h_residualize_via_slope(bcount, dd, YDAYS)


def f50_tdco_528_wyckoff_signal_residual_after_removing_distribution_day_63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    wy = _h_wyckoff_upthrust_count_63(high, low, close)
    dist = _h_dist_day_count(close, volume, 25)
    return _h_residualize_via_slope(wy, dist, YDAYS)


def f50_tdco_529_candle_pattern_residual_after_removing_volume_63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    cand_basket = _h_basket_candle(open, high, low, close)
    vol_z = _rolling_zscore(volume, YDAYS)
    return _h_residualize_via_slope(cand_basket, vol_z, YDAYS)


def f50_tdco_530_multi_bar_pattern_residual_after_removing_atr_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mb = _h_basket_multi_bar(high, low, close)
    atr21 = _atr(high, low, close, MDAYS)
    return _h_residualize_via_slope(mb, atr21, YDAYS)


def f50_tdco_531_stage_4_signal_residual_after_removing_market_regime_63(close: pd.Series) -> pd.Series:
    stg4 = _h_stage4_mask(close).astype(float)
    r63 = close.pct_change(QDAYS)
    return _h_residualize_via_slope(stg4, r63, YDAYS)


def f50_tdco_532_cross_pattern_signal_residual_after_removing_basket_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    wy = _h_basket_wyckoff(high, low, close, volume)
    dd_b = _h_basket_drawdown(high, close)
    return _h_residualize_via_slope(wy, dd_b, YDAYS)


def f50_tdco_533_universe_signal_residual_after_removing_first_pc_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    all_b = (_h_basket_dist_breakdown(close, volume).fillna(0)
             + _h_basket_wyckoff(high, low, close, volume).fillna(0)
             + _h_basket_breakdown(low, close).fillna(0))
    dd = _h_drawdown(high, close, YDAYS)
    return _h_residualize_via_slope(all_b, dd, YDAYS)


def f50_tdco_534_distribution_signal_double_orthogonalized_63(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dist = _h_dist_day_count(close, volume, 25)
    trend = _rolling_slope(close, QDAYS)
    r1 = _h_residualize_via_slope(dist, trend, YDAYS)
    dd = _h_drawdown(high, close, YDAYS)
    return _h_residualize_via_slope(r1, dd, YDAYS)


def f50_tdco_535_breakdown_signal_quantile_normalized_252(low: pd.Series, close: pd.Series) -> pd.Series:
    bcount = _h_breakdown_63(low, close).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _h_rolling_pct_rank(bcount, YDAYS)


def f50_tdco_536_pattern_signal_rolling_zscore_504(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mb = _h_basket_multi_bar(high, low, close)
    return _rolling_zscore(mb, DDAYS_2Y)


def f50_tdco_537_universe_signal_winsorized_5pct_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    agg = (_h_drawdown(high, close, YDAYS).fillna(0).clip(lower=0)
           + _h_basket_breakdown(low, close).fillna(0) / 10.0
           + _h_basket_wyckoff(high, low, close, volume).fillna(0) / 5.0)
    return _h_winsorize_zscore(agg, YDAYS, 0.05)


def f50_tdco_538_distribution_signal_rank_within_own_504(close: pd.Series, volume: pd.Series) -> pd.Series:
    dist = _h_dist_day_count(close, volume, 25)
    return _h_rolling_pct_rank(dist, DDAYS_2Y)


def f50_tdco_539_cross_pattern_signal_pct_rank_within_1260(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    cp = (_h_basket_wyckoff(high, low, close, volume).fillna(0)
          + _h_basket_dist_breakdown(close, volume).fillna(0)
          + _h_basket_breakdown(low, close).fillna(0))
    return _h_rolling_pct_rank(cp, DDAYS_5Y)


def f50_tdco_540_multi_resolution_signal_normalized_504(high: pd.Series, close: pd.Series) -> pd.Series:
    dd_b = _h_basket_drawdown(high, close)
    mx = dd_b.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return _safe_div(dd_b, mx)




def f50_tdco_541_wyckoff_basket_ensemble_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    return _h_basket_wyckoff(high, low, close, volume)


def f50_tdco_542_candle_basket_ensemble_score(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _h_basket_candle(open, high, low, close)


def f50_tdco_543_multi_bar_pattern_basket_ensemble_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _h_basket_multi_bar(high, low, close)


def f50_tdco_544_drawdown_basket_ensemble_score(high: pd.Series, close: pd.Series) -> pd.Series:
    return _h_basket_drawdown(high, close)


def f50_tdco_545_breakdown_basket_ensemble_score(low: pd.Series, close: pd.Series) -> pd.Series:
    return _h_basket_breakdown(low, close)


def f50_tdco_546_microstructure_basket_ensemble_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    return _h_basket_microstructure(high, low, close, volume)


def f50_tdco_547_institutional_signal_basket_ensemble_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    return _h_basket_institutional(close, volume)


def f50_tdco_548_stage_4_basket_ensemble_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    return _h_basket_stage4(close, volume)


def f50_tdco_549_cycle_phase_basket_ensemble_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    return _h_basket_cycle_phase(high, low, close, volume)


def f50_tdco_550_cross_ensemble_consensus_score(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    b1 = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    b2 = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    b3 = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    b4 = _rolling_zscore(_h_basket_drawdown(high, close), YDAYS)
    b5 = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    b6 = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    b7 = _rolling_zscore(_h_basket_stage4(close, volume), YDAYS)
    cnt = ((b1 > 1).astype(float).fillna(0)
           + (b2 > 1).astype(float).fillna(0)
           + (b3 > 1).astype(float).fillna(0)
           + (b4 > 1).astype(float).fillna(0)
           + (b5 > 1).astype(float).fillna(0)
           + (b6 > 1).astype(float).fillna(0)
           + (b7 > 1).astype(float).fillna(0))
    return cnt.where(close.notna(), np.nan)


def f50_tdco_551_cross_ensemble_dispersion_score(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    b1 = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    b2 = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    b3 = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    b4 = _rolling_zscore(_h_basket_drawdown(high, close), YDAYS)
    b5 = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    b6 = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    b7 = _rolling_zscore(_h_basket_stage4(close, volume), YDAYS)
    df = pd.concat([b1.rename("b1"), b2.rename("b2"), b3.rename("b3"), b4.rename("b4"),
                    b5.rename("b5"), b6.rename("b6"), b7.rename("b7")], axis=1)
    return df.std(axis=1)


def f50_tdco_552_cross_ensemble_alignment_score(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    b1 = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    b2 = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    b3 = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    b4 = _rolling_zscore(_h_basket_drawdown(high, close), YDAYS)
    b5 = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    b6 = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    b7 = _rolling_zscore(_h_basket_stage4(close, volume), YDAYS)
    return (b1.fillna(0) + b2.fillna(0) + b3.fillna(0) + b4.fillna(0)
            + b5.fillna(0) + b6.fillna(0) + b7.fillna(0)).where(close.notna(), np.nan)


def f50_tdco_553_ensemble_correlation_breakdown_indicator_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dd_b = _h_basket_drawdown(high, close)
    wy_b = _h_basket_wyckoff(high, low, close, volume)
    corr = dd_b.rolling(QDAYS, min_periods=MDAYS).corr(wy_b)
    was_high = corr.shift(QDAYS) > 0.5
    now_low = corr < 0.2
    return (was_high & now_low).astype(float).where(corr.notna(), np.nan)


def f50_tdco_554_ensemble_lag_lead_difference_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dd_z = _rolling_zscore(_h_basket_drawdown(high, close), YDAYS)
    wy_z = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    return dd_z - wy_z.shift(MDAYS)


def f50_tdco_555_ensemble_max_min_score_range_252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    b1 = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    b2 = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    b3 = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    b4 = _rolling_zscore(_h_basket_drawdown(high, close), YDAYS)
    b5 = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    df = pd.concat([b1.rename("a"), b2.rename("b"), b3.rename("c"), b4.rename("d"), b5.rename("e")], axis=1)
    return df.max(axis=1) - df.min(axis=1)




def f50_tdco_556_wyckoff_plus_microstructure_alignment_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    wy_z = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    ms_z = _rolling_zscore(_h_basket_microstructure(high, low, close, volume), YDAYS)
    return ((wy_z > 1) & (ms_z > 1)).astype(float).where(wy_z.notna() & ms_z.notna(), np.nan)


def f50_tdco_557_candle_plus_institutional_alignment_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    c_z = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    in_z = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    return ((c_z > 1) & (in_z > 1)).astype(float).where(c_z.notna() & in_z.notna(), np.nan)


def f50_tdco_558_multi_bar_plus_stage_4_alignment_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mb_z = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    stg4 = _h_stage4_mask(close)
    return ((mb_z > 1) & stg4).astype(float).where(mb_z.notna(), np.nan)


def f50_tdco_559_drawdown_plus_recovery_failure_alignment_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    dd = _h_drawdown(high, close, YDAYS)
    h63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h63)
    b_cnt = bounce.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    f_cnt = failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    fail_frac = _safe_div(f_cnt, b_cnt)
    return ((dd > 0.25) & (fail_frac > 0.5)).astype(float).where(dd.notna(), np.nan)


def f50_tdco_560_breakdown_plus_volume_alignment_signal(low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    brk = _h_breakdown_63(low, close)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    return (brk & (volume > 2.0 * vavg)).astype(float).where(vavg.notna(), np.nan)


def f50_tdco_561_stage_4_plus_microstructure_decay_alignment(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    stg4 = _h_stage4_mask(close)
    ms_z = _rolling_zscore(_h_basket_microstructure(high, low, close, volume), YDAYS)
    return (stg4 & (ms_z > 1)).astype(float).where(ms_z.notna(), np.nan)


def f50_tdco_562_wyckoff_plus_drawdown_plus_breakdown_triple_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    wy_z = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    dd = _h_drawdown(high, close, YDAYS)
    brk = _h_breakdown_63(low, close)
    return ((wy_z > 1) & (dd > 0.20) & brk).astype(float).where(wy_z.notna(), np.nan)


def f50_tdco_563_candle_plus_volume_plus_drawdown_triple(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    c_z = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd = _h_drawdown(high, close, YDAYS)
    return ((c_z > 1) & (volume > 1.5 * vavg) & (dd > 0.20)).astype(float).where(c_z.notna() & vavg.notna(), np.nan)


def f50_tdco_564_multi_bar_plus_stage_4_plus_microstructure_triple(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mb_z = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    stg4 = _h_stage4_mask(close)
    ms_z = _rolling_zscore(_h_basket_microstructure(high, low, close, volume), YDAYS)
    return ((mb_z > 1) & stg4 & (ms_z > 1)).astype(float).where(mb_z.notna() & ms_z.notna(), np.nan)


def f50_tdco_565_distribution_plus_breakdown_plus_recovery_failure_triple(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dist = _h_dist_day_count(close, volume, 25)
    brk = _h_breakdown_63(low, close)
    h63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h63)
    b_cnt = bounce.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    f_cnt = failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    fail_frac = _safe_div(f_cnt, b_cnt)
    return ((dist >= 4) & brk & (fail_frac > 0.5)).astype(float).where(dist.notna(), np.nan)


def f50_tdco_566_universe_alignment_at_252h_v4(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs_peak = _bars_since_true(high == rmax)
    near_peak = (bs_peak <= MDAYS)
    b1 = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    b2 = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    b3 = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    b4 = _rolling_zscore(_h_basket_drawdown(high, close), YDAYS)
    b5 = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    b6 = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    b7 = _rolling_zscore(_h_basket_stage4(close, volume), YDAYS)
    cnt = ((b1 > 1).astype(float).fillna(0)
           + (b2 > 1).astype(float).fillna(0)
           + (b3 > 1).astype(float).fillna(0)
           + (b4 > 1).astype(float).fillna(0)
           + (b5 > 1).astype(float).fillna(0)
           + (b6 > 1).astype(float).fillna(0)
           + (b7 > 1).astype(float).fillna(0))
    return cnt.where(near_peak & close.notna(), np.nan)


def f50_tdco_567_universe_alignment_in_drawdown_v4(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dd = _h_drawdown(high, close, YDAYS)
    in_dd = dd > 0.25
    b1 = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    b2 = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    b3 = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    b5 = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    b6 = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    b7 = _rolling_zscore(_h_basket_stage4(close, volume), YDAYS)
    cnt = ((b1 > 1).astype(float).fillna(0)
           + (b2 > 1).astype(float).fillna(0)
           + (b3 > 1).astype(float).fillna(0)
           + (b5 > 1).astype(float).fillna(0)
           + (b6 > 1).astype(float).fillna(0)
           + (b7 > 1).astype(float).fillna(0))
    return cnt.where(in_dd & close.notna(), np.nan)


def f50_tdco_568_universe_alignment_in_recovery_failure_v4(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    h63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h63)
    b_cnt = bounce.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    f_cnt = failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    fail_frac = _safe_div(f_cnt, b_cnt)
    in_fail = fail_frac > 0.5
    b1 = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    b3 = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    b4 = _rolling_zscore(_h_basket_drawdown(high, close), YDAYS)
    b5 = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    b7 = _rolling_zscore(_h_basket_stage4(close, volume), YDAYS)
    cnt = ((b1 > 1).astype(float).fillna(0)
           + (b3 > 1).astype(float).fillna(0)
           + (b4 > 1).astype(float).fillna(0)
           + (b5 > 1).astype(float).fillna(0)
           + (b7 > 1).astype(float).fillna(0))
    return cnt.where(in_fail & close.notna(), np.nan)


def f50_tdco_569_universe_alignment_in_stage_4_v4(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    stg4 = _h_stage4_mask(close)
    b1 = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    b2 = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    b3 = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    b4 = _rolling_zscore(_h_basket_drawdown(high, close), YDAYS)
    b5 = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    b6 = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    cnt = ((b1 > 1).astype(float).fillna(0)
           + (b2 > 1).astype(float).fillna(0)
           + (b3 > 1).astype(float).fillna(0)
           + (b4 > 1).astype(float).fillna(0)
           + (b5 > 1).astype(float).fillna(0)
           + (b6 > 1).astype(float).fillna(0))
    return cnt.where(stg4 & close.notna(), np.nan)


def f50_tdco_570_universe_alignment_in_terminal_phase_v4(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dd = _h_drawdown(high, close, YDAYS)
    stg4 = _h_stage4_mask(close)
    term = (dd > 0.50) & stg4
    b1 = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    b2 = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    b3 = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    b5 = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    b6 = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    b7 = _rolling_zscore(_h_basket_stage4(close, volume), YDAYS)
    cnt = ((b1 > 1).astype(float).fillna(0)
           + (b2 > 1).astype(float).fillna(0)
           + (b3 > 1).astype(float).fillna(0)
           + (b5 > 1).astype(float).fillna(0)
           + (b6 > 1).astype(float).fillna(0)
           + (b7 > 1).astype(float).fillna(0))
    return cnt.where(term & close.notna(), np.nan)




def _h_dominant_period_kernel(w):
    """FFT-proxy dominant period: return index (period in samples) of largest magnitude FFT bin, excluding DC."""
    if np.isnan(w).any() or len(w) < 16:
        return np.nan
    n = len(w)
    f = np.fft.rfft(w - np.mean(w))
    mags = np.abs(f)
    if len(mags) < 2:
        return np.nan
    idx = int(np.argmax(mags[1:])) + 1
    if idx == 0:
        return np.nan
    return float(n / idx)


def _h_dominant_amplitude_kernel(w):
    """FFT-proxy dominant cycle amplitude: max magnitude / n."""
    if np.isnan(w).any() or len(w) < 16:
        return np.nan
    n = len(w)
    f = np.fft.rfft(w - np.mean(w))
    mags = np.abs(f)
    if len(mags) < 2:
        return np.nan
    return float(np.max(mags[1:]) / n)


def _h_spectral_entropy_kernel(w):
    """Spectral entropy of returns: normalized entropy of FFT power spectrum (excluding DC)."""
    if np.isnan(w).any() or len(w) < 8:
        return np.nan
    f = np.fft.rfft(w - np.mean(w))
    p = np.abs(f) ** 2
    if len(p) < 2:
        return np.nan
    p = p[1:]
    ps = p.sum()
    if ps == 0:
        return np.nan
    p = p / ps
    p = p[p > 0]
    if len(p) == 0:
        return np.nan
    h = -np.sum(p * np.log(p))
    return float(h / np.log(len(p)) if len(p) > 1 else h)


def _h_spectral_flatness_kernel(w):
    """Spectral flatness: geometric-mean / arithmetic-mean of power spectrum (Wiener entropy)."""
    if np.isnan(w).any() or len(w) < 8:
        return np.nan
    f = np.fft.rfft(w - np.mean(w))
    p = np.abs(f) ** 2
    if len(p) < 2:
        return np.nan
    p = p[1:]
    p = p[p > 0]
    if len(p) == 0:
        return np.nan
    gm = np.exp(np.mean(np.log(p)))
    am = np.mean(p)
    if am == 0:
        return np.nan
    return float(gm / am)


def _h_power_ratio_short_long_kernel(w):
    """Ratio of power in upper-half FFT bins (short cycles) to lower-half (long cycles)."""
    if np.isnan(w).any() or len(w) < 8:
        return np.nan
    f = np.fft.rfft(w - np.mean(w))
    p = np.abs(f) ** 2
    if len(p) < 3:
        return np.nan
    p = p[1:]
    half = len(p) // 2
    short = p[half:].sum()
    long_ = p[:half].sum()
    if long_ == 0:
        return np.nan
    return float(short / long_)


def _h_frequency_centroid_kernel(w):
    """Spectral centroid: weighted-avg frequency-bin index, normalized by total power."""
    if np.isnan(w).any() or len(w) < 8:
        return np.nan
    f = np.fft.rfft(w - np.mean(w))
    p = np.abs(f) ** 2
    if len(p) < 2:
        return np.nan
    bins = np.arange(len(p))
    if p.sum() == 0:
        return np.nan
    return float((bins * p).sum() / p.sum())


def f50_tdco_571_close_dominant_period_zscore_252(close: pd.Series) -> pd.Series:
    dp = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dominant_period_kernel, raw=True)
    return _rolling_zscore(dp, YDAYS)


def f50_tdco_572_close_cycle_amplitude_zscore_252(close: pd.Series) -> pd.Series:
    amp = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dominant_amplitude_kernel, raw=True)
    return _rolling_zscore(amp, YDAYS)


def f50_tdco_573_close_spectral_entropy_decay_63(close: pd.Series) -> pd.Series:
    se = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_spectral_entropy_kernel, raw=True)
    return se - se.shift(QDAYS)


def f50_tdco_574_close_spectral_flatness_post_peak_63(close: pd.Series) -> pd.Series:
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_h_spectral_flatness_kernel, raw=True)


def f50_tdco_575_close_power_ratio_short_long_post_peak_63(close: pd.Series) -> pd.Series:
    return close.rolling(QDAYS, min_periods=MDAYS).apply(_h_power_ratio_short_long_kernel, raw=True)


def f50_tdco_576_close_frequency_centroid_decay_63(close: pd.Series) -> pd.Series:
    fc = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_frequency_centroid_kernel, raw=True)
    return fc - fc.shift(QDAYS)


def f50_tdco_577_close_dominant_cycle_phase_post_peak_indicator(high: pd.Series, close: pd.Series) -> pd.Series:
    dp = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dominant_period_kernel, raw=True)
    return (dp < dp.shift(MDAYS)).astype(float).where(dp.notna(), np.nan)


def f50_tdco_578_close_cycle_phase_persistence_post_peak_63(close: pd.Series) -> pd.Series:
    dp = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_dominant_period_kernel, raw=True)
    return (dp < 21).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(dp.notna(), np.nan)


def f50_tdco_579_close_cycle_completion_pct_252(close: pd.Series) -> pd.Series:
    dp = close.rolling(YDAYS, min_periods=QDAYS).apply(_h_dominant_period_kernel, raw=True)
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(close == rmin)
    return _safe_div(bs_min, dp)


def f50_tdco_580_close_cycle_terminal_score_252(close: pd.Series) -> pd.Series:
    dp = close.rolling(YDAYS, min_periods=QDAYS).apply(_h_dominant_period_kernel, raw=True)
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(close == rmin)
    comp = _safe_div(bs_min, dp)
    return comp.clip(upper=2.0)




def f50_tdco_581_stuck_probability_master_v4_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dd = _h_drawdown(high, close, YDAYS).clip(lower=0).fillna(0)
    db = _h_basket_dist_breakdown(close, volume).fillna(0) / 5.0
    bb = _h_basket_breakdown(low, close).fillna(0) / 10.0
    sb = _h_basket_stage4(close, volume).fillna(0) / 3.0
    ib = _h_basket_institutional(close, volume).fillna(0) / 2.0
    mb = _h_basket_microstructure(high, low, close, volume).fillna(0)
    return (2.0 * dd + db + bb + sb + ib + mb).where(close.notna() & volume.notna(), np.nan)


def f50_tdco_582_terminal_distribution_master_v4_orthogonal_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    return (_rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_drawdown(high, close), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_breakdown(low, close), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_institutional(close, volume), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_stage4(close, volume), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_microstructure(high, low, close, volume), YDAYS).fillna(0))


def f50_tdco_583_absolute_terminal_stuck_master_v4_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dd = _h_drawdown(high, close, YDAYS)
    wy = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    db = _rolling_zscore(_h_basket_drawdown(high, close), YDAYS)
    bb = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    ib = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    sb = _rolling_zscore(_h_basket_stage4(close, volume), YDAYS)
    mb = _rolling_zscore(_h_basket_microstructure(high, low, close, volume), YDAYS)
    stg4 = _h_stage4_mask(close)
    return ((dd > 0.60) & (wy > 1) & (db > 1) & (bb > 1) & (ib > 1) & (sb > 1) & (mb > 1.5) & stg4).astype(float).where(wy.notna() & mb.notna(), np.nan)


def f50_tdco_584_cross_pattern_terminal_v4_aggregate(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    return (_rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_drawdown(high, close), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_breakdown(low, close), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_institutional(close, volume), YDAYS).fillna(0)
            + _rolling_zscore(_h_basket_stage4(close, volume), YDAYS).fillna(0))


def f50_tdco_585_multi_resolution_stuck_v4_aggregate(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    s = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS, DDAYS_2Y, DDAYS_5Y):
        ddn = _h_drawdown(high, close, n).clip(lower=0).fillna(0)
        s = s + ddn
    return s.where(close.notna(), np.nan)


def f50_tdco_586_final_distribution_master_v4_score(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ddm = ((ret < -0.002) & (volume > vavg)).astype(float)
    d25 = ddm.rolling(25, min_periods=10).sum()
    d50 = ddm.rolling(50, min_periods=15).sum()
    d100 = ddm.rolling(100, min_periods=30).sum()
    density = d25 / 25.0
    down_mask = (ret < -0.002).astype(float)
    vol_down = (volume * down_mask).rolling(QDAYS, min_periods=MDAYS).sum()
    vol_all = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    vol_down_z = _rolling_zscore(_safe_div(vol_down, vol_all), YDAYS)
    return (d25 / 10.0 + d50 / 15.0 + d100 / 30.0 + density + vol_down_z.fillna(0))


def f50_tdco_587_final_breakdown_master_v4_score(low: pd.Series, close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    b21 = _h_breakdown_21(low, close).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().fillna(0)
    b63 = _h_breakdown_63(low, close).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().fillna(0)
    b252 = _h_breakdown_252(low, close).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    heavy_brk = (_h_breakdown_63(low, close) & (volume > 1.5 * vavg)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().fillna(0)
    return (b21 / 5.0 + b63 / 10.0 + b252 / 20.0 + heavy_brk / 5.0)


def f50_tdco_588_final_blowoff_collapse_master_v4_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    r63 = close.pct_change(QDAYS)
    parabolic = (r63 > 0.5).astype(float)  # >50% in 63d
    drop21 = close.pct_change(MDAYS)
    drop_post = (drop21 < -0.20).astype(float)  # -20% in 21d
    atr21 = _atr(high, low, close, MDAYS)
    atr_z = _rolling_zscore(atr21, YDAYS)
    return parabolic.fillna(0) + drop_post.fillna(0) + atr_z.fillna(0).clip(lower=0)


def f50_tdco_589_final_failure_to_recover_master_v4_score(high: pd.Series, close: pd.Series) -> pd.Series:
    h63 = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h63)
    b_cnt = bounce.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    f_cnt = failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    fail_frac = _safe_div(f_cnt, b_cnt).fillna(0)
    dd = _h_drawdown(high, close, YDAYS).fillna(0)
    s200 = _sma(close, 200)
    below_200 = _streak_true(close < s200) / float(YDAYS)
    return fail_frac + dd + below_200.fillna(0).clip(upper=2.0)


def f50_tdco_590_final_chronic_weakness_master_v4_score(close: pd.Series) -> pd.Series:
    s50 = _sma(close, 50)
    s200 = _sma(close, 200)
    f50 = (close < s50).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    f200 = (close < s200).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    s50_decl = s50 < s50.shift(MDAYS)
    streak_decl = _streak_true(s50_decl) / float(YDAYS)
    return (f50.fillna(0) + f200.fillna(0) + streak_decl.fillna(0).clip(upper=2.0))


def f50_tdco_591_final_capitulation_master_v4_score(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    ret = close.pct_change()
    cap = (volume > 3.0 * vavg) & (ret < -0.05)
    cap_cnt = cap.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    max_drop = ret.rolling(QDAYS, min_periods=MDAYS).min().abs().fillna(0)
    return cap_cnt / 5.0 + max_drop * 10.0


def f50_tdco_592_final_stage_4_master_v4_score(close: pd.Series) -> pd.Series:
    stg4 = _h_stage4_mask(close)
    state = stg4.astype(float).fillna(0)
    frac = stg4.astype(float).rolling(YDAYS, min_periods=QDAYS).mean().fillna(0)
    streak = _streak_true(stg4).fillna(0) / 100.0
    s200 = _sma(close, 200)
    streak_below_200 = _streak_true(close < s200).fillna(0) / float(YDAYS)
    return state + frac + streak.clip(upper=2.0) + streak_below_200.clip(upper=2.0)


def f50_tdco_593_final_microstructure_decay_master_v4_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    am = _h_amihud(close, volume, QDAYS)
    cs = _h_corwin_schultz(high, low)
    atr21 = _atr(high, low, close, MDAYS)
    vpa = _safe_div(volume, atr21).rolling(MDAYS, min_periods=WDAYS).mean()
    vpa_decay = -_rolling_slope(vpa, QDAYS)
    return (_rolling_zscore(am, YDAYS).fillna(0)
            + _rolling_zscore(cs, YDAYS).fillna(0)
            + _rolling_zscore(vpa_decay, YDAYS).fillna(0))


def f50_tdco_594_final_institutional_distribution_master_v4_score(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    s21 = _sma(close, MDAYS)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    down = close.diff() < 0
    normal_vol = (volume >= 0.8 * vavg) & (volume <= 1.2 * vavg)
    stealth = (down & normal_vol & (close < s21)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    block = (volume > 3.0 * vavg).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    # quiet selling: low close, low volume, vs avg
    quiet = (down & (close < low.shift(1)) & (volume < 0.8 * vavg)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    s50 = _sma(close, 50)
    weak = (close < s50).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return (stealth.fillna(0) / 10.0 + block.fillna(0) / 10.0
            + quiet.fillna(0) / 10.0 + weak.fillna(0))


def f50_tdco_595_final_recovery_failure_master_v4_score(high: pd.Series, close: pd.Series) -> pd.Series:
    s = pd.Series(0.0, index=close.index)
    for n in (MDAYS, QDAYS, YDAYS):
        hN = high.shift(1).rolling(n, min_periods=max(n // 3, 5)).max()
        bounce = close.pct_change(WDAYS) > 0.05
        failed = bounce & (high < hN)
        b_cnt = bounce.astype(float).rolling(n, min_periods=max(n // 3, 5)).sum()
        f_cnt = failed.astype(float).rolling(n, min_periods=max(n // 3, 5)).sum()
        s = s + _safe_div(f_cnt, b_cnt).fillna(0)
    return s.where(close.notna(), np.nan)


def f50_tdco_596_final_cycle_terminal_master_v4_score(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    bs_min = _bars_since_true(low == rmin)
    pos = bs_min / float(YDAYS)
    late = (pos > 0.85).astype(float)
    dp = close.rolling(YDAYS, min_periods=QDAYS).apply(_h_dominant_period_kernel, raw=True)
    comp = _safe_div(bs_min, dp).clip(upper=2.0)
    dp_z = _rolling_zscore(dp, YDAYS).fillna(0)
    sf = close.rolling(QDAYS, min_periods=MDAYS).apply(_h_spectral_flatness_kernel, raw=True)
    return late.fillna(0) + comp.fillna(0) + dp_z + sf.fillna(0)


def f50_tdco_597_cross_batch_alignment_v4_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dd = _h_drawdown(high, close, YDAYS)
    wy = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    ms = _rolling_zscore(_h_basket_microstructure(high, low, close, volume), YDAYS)
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    sk_shift = sk - sk.shift(QDAYS)
    return ((dd > 0.20).astype(float).fillna(0)
            + (wy > 0).astype(float).fillna(0)
            + (ms > 0).astype(float).fillna(0)
            + (sk_shift < 0).astype(float).fillna(0)).where(close.notna(), np.nan)


def f50_tdco_598_universe_recall_optimized_v4_master_score(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dd = _h_drawdown(high, close, YDAYS)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    brk = _h_breakdown_21(low, close)
    s50 = _sma(close, 50)
    cs = _h_corwin_schultz(high, low)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    cs_widen = cs - cs.where(high == rmax).ffill()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    pos = _bars_since_true(low == low.rolling(YDAYS, min_periods=QDAYS).min()) / float(YDAYS)
    stg4 = _h_stage4_mask(close)
    mb_z = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    in_z = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    s30 = _sma(close, 30)
    return ((dd > 0.10).astype(float).fillna(0)
            + (dd25 >= 2).astype(float).fillna(0)
            + (close < s50).astype(float).fillna(0)
            + brk.astype(float).fillna(0)
            + (cs_widen > 0).astype(float).fillna(0)
            + (sk < 0).astype(float).fillna(0)
            + (pos > 0.6).astype(float).fillna(0)
            + stg4.astype(float).fillna(0)
            + (mb_z > 0).astype(float).fillna(0)
            + (in_z > 0).astype(float).fillna(0)).where(s30.notna() & vavg.notna(), np.nan)


def f50_tdco_599_universe_precision_optimized_v4_master_score(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dd = _h_drawdown(high, close, YDAYS)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd25 = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    stg4 = _h_stage4_mask(close)
    ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    brk_recent = (close < ll63).astype(float).rolling(MDAYS, min_periods=WDAYS).max()
    cs = _h_corwin_schultz(high, low)
    cs_z = _rolling_zscore(cs, YDAYS)
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    kt = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_kurt_kernel, raw=True)
    s200 = _sma(close, 200)
    streak_below_200 = _streak_true(close < s200)
    return ((dd > 0.50) & (dd25 >= 6) & stg4 & (brk_recent > 0) & (cs_z > 1.5)
            & (sk < -0.5) & (kt > 3) & (streak_below_200 > 63)).astype(float).where(s200.notna() & sk.notna(), np.nan)


def f50_tdco_600_absolute_terminal_stuck_universe_v4_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    dd = _h_drawdown(high, close, YDAYS)
    stg4 = _h_stage4_mask(close)
    b1 = _rolling_zscore(_h_basket_wyckoff(high, low, close, volume), YDAYS)
    b2 = _rolling_zscore(_h_basket_candle(open, high, low, close), YDAYS)
    b3 = _rolling_zscore(_h_basket_multi_bar(high, low, close), YDAYS)
    b4 = _rolling_zscore(_h_basket_drawdown(high, close), YDAYS)
    b5 = _rolling_zscore(_h_basket_breakdown(low, close), YDAYS)
    b6 = _rolling_zscore(_h_basket_institutional(close, volume), YDAYS)
    b7 = _rolling_zscore(_h_basket_stage4(close, volume), YDAYS)
    all_baskets = (b1 > 1) & (b2 > 1) & (b3 > 1) & (b4 > 1) & (b5 > 1) & (b6 > 1) & (b7 > 1)
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _bars_since_true(low == rmin) / float(YDAYS)
    ret = close.pct_change()
    sk = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_skew_kernel, raw=True)
    kt = ret.rolling(QDAYS, min_periods=MDAYS).apply(_h_kurt_kernel, raw=True)
    tu20 = (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    brk_recent = _h_breakdown_63(low, close).astype(float).rolling(MDAYS, min_periods=WDAYS).max()
    return ((dd > 0.60) & stg4 & all_baskets & (pos > 0.85) & (sk < -0.5)
            & (kt > 3.0) & (tu20 > 0.5) & (brk_recent > 0)).astype(float).where(sk.notna() & kt.notna(), np.nan)



TERMINAL_DISTRIBUTION_COMPOSITE_BASE_REGISTRY_526_600 = {
    "f50_tdco_526_distribution_signal_residual_after_removing_trend_63": {"inputs": ["close", "volume"], "func": f50_tdco_526_distribution_signal_residual_after_removing_trend_63},
    "f50_tdco_527_breakdown_signal_residual_after_removing_drawdown_63": {"inputs": ["low", "close", "high"], "func": f50_tdco_527_breakdown_signal_residual_after_removing_drawdown_63},
    "f50_tdco_528_wyckoff_signal_residual_after_removing_distribution_day_63": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_528_wyckoff_signal_residual_after_removing_distribution_day_63},
    "f50_tdco_529_candle_pattern_residual_after_removing_volume_63": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_529_candle_pattern_residual_after_removing_volume_63},
    "f50_tdco_530_multi_bar_pattern_residual_after_removing_atr_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_530_multi_bar_pattern_residual_after_removing_atr_63},
    "f50_tdco_531_stage_4_signal_residual_after_removing_market_regime_63": {"inputs": ["close"], "func": f50_tdco_531_stage_4_signal_residual_after_removing_market_regime_63},
    "f50_tdco_532_cross_pattern_signal_residual_after_removing_basket_63": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_532_cross_pattern_signal_residual_after_removing_basket_63},
    "f50_tdco_533_universe_signal_residual_after_removing_first_pc_63": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_533_universe_signal_residual_after_removing_first_pc_63},
    "f50_tdco_534_distribution_signal_double_orthogonalized_63": {"inputs": ["high", "close", "volume"], "func": f50_tdco_534_distribution_signal_double_orthogonalized_63},
    "f50_tdco_535_breakdown_signal_quantile_normalized_252": {"inputs": ["low", "close"], "func": f50_tdco_535_breakdown_signal_quantile_normalized_252},
    "f50_tdco_536_pattern_signal_rolling_zscore_504": {"inputs": ["high", "low", "close"], "func": f50_tdco_536_pattern_signal_rolling_zscore_504},
    "f50_tdco_537_universe_signal_winsorized_5pct_zscore_252": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_537_universe_signal_winsorized_5pct_zscore_252},
    "f50_tdco_538_distribution_signal_rank_within_own_504": {"inputs": ["close", "volume"], "func": f50_tdco_538_distribution_signal_rank_within_own_504},
    "f50_tdco_539_cross_pattern_signal_pct_rank_within_1260": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_539_cross_pattern_signal_pct_rank_within_1260},
    "f50_tdco_540_multi_resolution_signal_normalized_504": {"inputs": ["high", "close"], "func": f50_tdco_540_multi_resolution_signal_normalized_504},
    "f50_tdco_541_wyckoff_basket_ensemble_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_541_wyckoff_basket_ensemble_score},
    "f50_tdco_542_candle_basket_ensemble_score": {"inputs": ["open", "high", "low", "close"], "func": f50_tdco_542_candle_basket_ensemble_score},
    "f50_tdco_543_multi_bar_pattern_basket_ensemble_score": {"inputs": ["high", "low", "close"], "func": f50_tdco_543_multi_bar_pattern_basket_ensemble_score},
    "f50_tdco_544_drawdown_basket_ensemble_score": {"inputs": ["high", "close"], "func": f50_tdco_544_drawdown_basket_ensemble_score},
    "f50_tdco_545_breakdown_basket_ensemble_score": {"inputs": ["low", "close"], "func": f50_tdco_545_breakdown_basket_ensemble_score},
    "f50_tdco_546_microstructure_basket_ensemble_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_546_microstructure_basket_ensemble_score},
    "f50_tdco_547_institutional_signal_basket_ensemble_score": {"inputs": ["close", "volume"], "func": f50_tdco_547_institutional_signal_basket_ensemble_score},
    "f50_tdco_548_stage_4_basket_ensemble_score": {"inputs": ["close", "volume"], "func": f50_tdco_548_stage_4_basket_ensemble_score},
    "f50_tdco_549_cycle_phase_basket_ensemble_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_549_cycle_phase_basket_ensemble_score},
    "f50_tdco_550_cross_ensemble_consensus_score": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_550_cross_ensemble_consensus_score},
    "f50_tdco_551_cross_ensemble_dispersion_score": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_551_cross_ensemble_dispersion_score},
    "f50_tdco_552_cross_ensemble_alignment_score": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_552_cross_ensemble_alignment_score},
    "f50_tdco_553_ensemble_correlation_breakdown_indicator_63": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_553_ensemble_correlation_breakdown_indicator_63},
    "f50_tdco_554_ensemble_lag_lead_difference_21": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_554_ensemble_lag_lead_difference_21},
    "f50_tdco_555_ensemble_max_min_score_range_252": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_555_ensemble_max_min_score_range_252},
    "f50_tdco_556_wyckoff_plus_microstructure_alignment_signal": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_556_wyckoff_plus_microstructure_alignment_signal},
    "f50_tdco_557_candle_plus_institutional_alignment_signal": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_557_candle_plus_institutional_alignment_signal},
    "f50_tdco_558_multi_bar_plus_stage_4_alignment_signal": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_558_multi_bar_plus_stage_4_alignment_signal},
    "f50_tdco_559_drawdown_plus_recovery_failure_alignment_signal": {"inputs": ["high", "close"], "func": f50_tdco_559_drawdown_plus_recovery_failure_alignment_signal},
    "f50_tdco_560_breakdown_plus_volume_alignment_signal": {"inputs": ["low", "close", "volume"], "func": f50_tdco_560_breakdown_plus_volume_alignment_signal},
    "f50_tdco_561_stage_4_plus_microstructure_decay_alignment": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_561_stage_4_plus_microstructure_decay_alignment},
    "f50_tdco_562_wyckoff_plus_drawdown_plus_breakdown_triple_signal": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_562_wyckoff_plus_drawdown_plus_breakdown_triple_signal},
    "f50_tdco_563_candle_plus_volume_plus_drawdown_triple": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_563_candle_plus_volume_plus_drawdown_triple},
    "f50_tdco_564_multi_bar_plus_stage_4_plus_microstructure_triple": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_564_multi_bar_plus_stage_4_plus_microstructure_triple},
    "f50_tdco_565_distribution_plus_breakdown_plus_recovery_failure_triple": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_565_distribution_plus_breakdown_plus_recovery_failure_triple},
    "f50_tdco_566_universe_alignment_at_252h_v4": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_566_universe_alignment_at_252h_v4},
    "f50_tdco_567_universe_alignment_in_drawdown_v4": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_567_universe_alignment_in_drawdown_v4},
    "f50_tdco_568_universe_alignment_in_recovery_failure_v4": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_568_universe_alignment_in_recovery_failure_v4},
    "f50_tdco_569_universe_alignment_in_stage_4_v4": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_569_universe_alignment_in_stage_4_v4},
    "f50_tdco_570_universe_alignment_in_terminal_phase_v4": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_570_universe_alignment_in_terminal_phase_v4},
    "f50_tdco_571_close_dominant_period_zscore_252": {"inputs": ["close"], "func": f50_tdco_571_close_dominant_period_zscore_252},
    "f50_tdco_572_close_cycle_amplitude_zscore_252": {"inputs": ["close"], "func": f50_tdco_572_close_cycle_amplitude_zscore_252},
    "f50_tdco_573_close_spectral_entropy_decay_63": {"inputs": ["close"], "func": f50_tdco_573_close_spectral_entropy_decay_63},
    "f50_tdco_574_close_spectral_flatness_post_peak_63": {"inputs": ["close"], "func": f50_tdco_574_close_spectral_flatness_post_peak_63},
    "f50_tdco_575_close_power_ratio_short_long_post_peak_63": {"inputs": ["close"], "func": f50_tdco_575_close_power_ratio_short_long_post_peak_63},
    "f50_tdco_576_close_frequency_centroid_decay_63": {"inputs": ["close"], "func": f50_tdco_576_close_frequency_centroid_decay_63},
    "f50_tdco_577_close_dominant_cycle_phase_post_peak_indicator": {"inputs": ["high", "close"], "func": f50_tdco_577_close_dominant_cycle_phase_post_peak_indicator},
    "f50_tdco_578_close_cycle_phase_persistence_post_peak_63": {"inputs": ["close"], "func": f50_tdco_578_close_cycle_phase_persistence_post_peak_63},
    "f50_tdco_579_close_cycle_completion_pct_252": {"inputs": ["close"], "func": f50_tdco_579_close_cycle_completion_pct_252},
    "f50_tdco_580_close_cycle_terminal_score_252": {"inputs": ["close"], "func": f50_tdco_580_close_cycle_terminal_score_252},
    "f50_tdco_581_stuck_probability_master_v4_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_581_stuck_probability_master_v4_score},
    "f50_tdco_582_terminal_distribution_master_v4_orthogonal_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_582_terminal_distribution_master_v4_orthogonal_score},
    "f50_tdco_583_absolute_terminal_stuck_master_v4_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_583_absolute_terminal_stuck_master_v4_indicator},
    "f50_tdco_584_cross_pattern_terminal_v4_aggregate": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_584_cross_pattern_terminal_v4_aggregate},
    "f50_tdco_585_multi_resolution_stuck_v4_aggregate": {"inputs": ["high", "low", "close"], "func": f50_tdco_585_multi_resolution_stuck_v4_aggregate},
    "f50_tdco_586_final_distribution_master_v4_score": {"inputs": ["close", "volume", "high"], "func": f50_tdco_586_final_distribution_master_v4_score},
    "f50_tdco_587_final_breakdown_master_v4_score": {"inputs": ["low", "close", "high", "volume"], "func": f50_tdco_587_final_breakdown_master_v4_score},
    "f50_tdco_588_final_blowoff_collapse_master_v4_score": {"inputs": ["high", "low", "close"], "func": f50_tdco_588_final_blowoff_collapse_master_v4_score},
    "f50_tdco_589_final_failure_to_recover_master_v4_score": {"inputs": ["high", "close"], "func": f50_tdco_589_final_failure_to_recover_master_v4_score},
    "f50_tdco_590_final_chronic_weakness_master_v4_score": {"inputs": ["close"], "func": f50_tdco_590_final_chronic_weakness_master_v4_score},
    "f50_tdco_591_final_capitulation_master_v4_score": {"inputs": ["high", "close", "volume"], "func": f50_tdco_591_final_capitulation_master_v4_score},
    "f50_tdco_592_final_stage_4_master_v4_score": {"inputs": ["close"], "func": f50_tdco_592_final_stage_4_master_v4_score},
    "f50_tdco_593_final_microstructure_decay_master_v4_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_593_final_microstructure_decay_master_v4_score},
    "f50_tdco_594_final_institutional_distribution_master_v4_score": {"inputs": ["close", "volume", "low"], "func": f50_tdco_594_final_institutional_distribution_master_v4_score},
    "f50_tdco_595_final_recovery_failure_master_v4_score": {"inputs": ["high", "close"], "func": f50_tdco_595_final_recovery_failure_master_v4_score},
    "f50_tdco_596_final_cycle_terminal_master_v4_score": {"inputs": ["close", "low", "high"], "func": f50_tdco_596_final_cycle_terminal_master_v4_score},
    "f50_tdco_597_cross_batch_alignment_v4_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_597_cross_batch_alignment_v4_score},
    "f50_tdco_598_universe_recall_optimized_v4_master_score": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_598_universe_recall_optimized_v4_master_score},
    "f50_tdco_599_universe_precision_optimized_v4_master_score": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_599_universe_precision_optimized_v4_master_score},
    "f50_tdco_600_absolute_terminal_stuck_universe_v4_indicator": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_600_absolute_terminal_stuck_universe_v4_indicator},
}
