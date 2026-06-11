"""short_squeeze_aftermath_technical d1 features 226-300 — Pipeline 1b-technical.

Second gap-fill batch. NSIR percentile/distribution shape & acceleration,
bear structure events (lower-highs/lows + flag/pennant variants), alt-horizon
anchored VWAPs, failed-rally/V-bottom patterns, distribution-day extensions,
terminal vol-structure, joint NSIR+price patterns, and terminal-decline /
final-stage indicators.

Bucket U: NSIR percentile / distribution shape (226-235).
Bucket V: NSIR change rate / acceleration (236-244).
Bucket W: Bear structure events (245-254).
Bucket X: Anchored VWAP from peak — alt horizons (255-262).
Bucket Y: Failed-rally / capitulation-recovery (263-270).
Bucket Z: Distribution-day extensions (271-278).
Bucket AA: Vol-structure terminal phase (279-286).
Bucket BB: Combined NSIR + price patterns (287-294).
Bucket CC: Terminal-decline / final-stage indicators (295-300).

Inputs: SEP OHLCV + NSIR (NaN-stubbed when absent). Self-contained; PIT-clean.
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


def _bars_since_true(mask):
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


def _streak_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _anchored_vwap_from_cummax_high(close, volume, high):
    """Anchored VWAP from all-time-high anchor (cumulative max high bar)."""
    high_arr = high.to_numpy(dtype=float)
    pv = (close * volume).to_numpy(dtype=float)
    vol_arr = volume.to_numpy(dtype=float)
    out = np.full(high_arr.size, np.nan)
    cur_max = -np.inf
    anchor_idx = -1
    sum_pv = 0.0
    sum_v = 0.0
    for t in range(high_arr.size):
        if not np.isnan(high_arr[t]) and high_arr[t] > cur_max:
            cur_max = high_arr[t]
            anchor_idx = t
            sum_pv = 0.0
            sum_v = 0.0
        if anchor_idx >= 0:
            if not np.isnan(pv[t]):
                sum_pv += pv[t]
            if not np.isnan(vol_arr[t]):
                sum_v += vol_arr[t]
            if sum_v > 0:
                out[t] = sum_pv / sum_v
    return pd.Series(out, index=close.index)


def _anchored_vwap_from_rolling_high(close, volume, high, n):
    """Anchored VWAP from max-high in trailing-n window (re-anchors as window slides)."""
    high_arr = high.to_numpy(dtype=float)
    pv = (close * volume).to_numpy(dtype=float)
    vol_arr = volume.to_numpy(dtype=float)
    out = np.full(high_arr.size, np.nan)
    for t in range(high_arr.size):
        lo = max(0, t - n + 1)
        w = high_arr[lo : t + 1]
        if w.size == 0 or np.isnan(w).all():
            continue
        rel = int(np.nanargmax(w))
        k = lo + rel
        sum_pv = np.nansum(pv[k : t + 1])
        sum_v = np.nansum(vol_arr[k : t + 1])
        if sum_v == 0:
            continue
        out[t] = sum_pv / sum_v
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket U — NSIR percentile / distribution shape (226-235)
# ============================================================


def f48_ssat_226_si_pct_rank_504_d1(shortinterest: pd.Series) -> pd.Series:
    """Pct rank of SI vs trailing 504d (2y) distribution."""
    return (shortinterest.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).rank(pct=True)).diff()


def f48_ssat_227_dtc_pct_rank_252_d1(daystocover: pd.Series) -> pd.Series:
    """Pct rank of daystocover vs trailing 252d."""
    return (daystocover.astype(float).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff()


def f48_ssat_228_shortpctfloat_pct_rank_252_d1(shortpctfloat: pd.Series) -> pd.Series:
    """Pct rank of short %-float vs trailing 252d."""
    return (shortpctfloat.astype(float).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff()


def f48_ssat_229_shortpctfloat_at_252d_max_flag_d1(shortpctfloat: pd.Series) -> pd.Series:
    """1 if short %-float equals its trailing 252d max — at-extreme indicator."""
    p = shortpctfloat.astype(float)
    return ((p >= p.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).where(p.notna(), np.nan)).diff()


def f48_ssat_230_shortpctfloat_at_252d_min_flag_d1(shortpctfloat: pd.Series) -> pd.Series:
    """1 if short %-float equals its trailing 252d min — fully-unwound indicator."""
    p = shortpctfloat.astype(float)
    return ((p <= p.rolling(YDAYS, min_periods=QDAYS).min()).astype(float).where(p.notna(), np.nan)).diff()


def f48_ssat_231_dtc_at_252d_max_flag_d1(daystocover: pd.Series) -> pd.Series:
    """1 if daystocover at trailing 252d max — peak-squeeze-risk indicator."""
    d = daystocover.astype(float)
    return ((d >= d.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).where(d.notna(), np.nan)).diff()


def f48_ssat_232_si_std_252_d1(shortinterest: pd.Series) -> pd.Series:
    """Trailing 252d std of short interest — SI volatility."""
    return (shortinterest.astype(float).rolling(YDAYS, min_periods=QDAYS).std()).diff()


def f48_ssat_233_si_range_over_mean_252_d1(shortinterest: pd.Series) -> pd.Series:
    """(252d max SI - 252d min SI) / 252d mean SI — relative SI swing."""
    s = shortinterest.astype(float)
    return (_safe_div(s.rolling(YDAYS, min_periods=QDAYS).max() - s.rolling(YDAYS, min_periods=QDAYS).min(),

                     s.rolling(YDAYS, min_periods=QDAYS).mean())).diff()


def f48_ssat_234_si_entropy_252_d1(shortinterest: pd.Series) -> pd.Series:
    """Normalized Shannon entropy (10 bins) of SI distribution past 252 — concentration measure."""
    def _ent(w):
        arr = w[~np.isnan(w)]
        if arr.size < 30:
            return np.nan
        x = np.log(arr.clip(1.0))
        if x.max() - x.min() == 0:
            return 0.0
        hist, _ = np.histogram(x, bins=10)
        s = hist.sum()
        if s == 0:
            return (np.nan).diff()
        p = hist / s
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(10))
    return shortinterest.astype(float).rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True)


def f48_ssat_235_si_recent_over_annual_avg_d1(shortinterest: pd.Series) -> pd.Series:
    """21d-avg SI / 252d-avg SI — recent-vs-annual SI level ratio."""
    s = shortinterest.astype(float)
    return (_safe_div(s.rolling(MDAYS, min_periods=WDAYS).mean(), s.rolling(YDAYS, min_periods=QDAYS).mean())).diff()


def f48_ssat_236_si_5d_pct_change_d1(shortinterest: pd.Series) -> pd.Series:
    """5-day %-change of SI — short-horizon SI flow direction."""
    return (shortinterest.astype(float).pct_change(WDAYS)).diff()


def f48_ssat_237_dtc_5d_change_d1(daystocover: pd.Series) -> pd.Series:
    """5-day absolute change of daystocover."""
    return (daystocover.astype(float).diff(WDAYS)).diff()


def f48_ssat_238_si_21d_slope_acceleration_d1(shortinterest: pd.Series) -> pd.Series:
    """21d slope of (21d slope of SI) — SI acceleration."""
    sl = _rolling_slope(shortinterest.astype(float), MDAYS)
    return (_rolling_slope(sl, MDAYS)).diff()


def f48_ssat_239_si_weekly_change_zscore_252_d1(shortinterest: pd.Series) -> pd.Series:
    """Z-score (252d) of weekly (5d) SI %-change — extreme weekly SI move detector."""
    return (_rolling_zscore(shortinterest.astype(float).pct_change(WDAYS), YDAYS, min_periods=QDAYS)).diff()


def f48_ssat_240_si_monthly_change_zscore_252_d1(shortinterest: pd.Series) -> pd.Series:
    """Z-score (252d) of monthly (21d) SI %-change."""
    return (_rolling_zscore(shortinterest.astype(float).pct_change(MDAYS), YDAYS, min_periods=QDAYS)).diff()


def f48_ssat_241_si_slope_sign_reversal_count_63_d1(shortinterest: pd.Series) -> pd.Series:
    """Count past 63 of 21d-slope-of-SI sign reversals — SI-trend instability."""
    sl = _rolling_slope(shortinterest.astype(float), MDAYS)
    sgn = np.sign(sl)
    flip = ((sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna()).astype(float)
    return (flip.rolling(QDAYS, min_periods=MDAYS).sum().where(sl.notna(), np.nan)).diff()


def f48_ssat_242_dtc_sign_change_count_63_d1(daystocover: pd.Series) -> pd.Series:
    """Count past 63 of daystocover-direction reversals (21d slope sign flips)."""
    sl = _rolling_slope(daystocover.astype(float), MDAYS)
    sgn = np.sign(sl)
    flip = ((sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna()).astype(float)
    return (flip.rolling(QDAYS, min_periods=MDAYS).sum().where(sl.notna(), np.nan)).diff()


def f48_ssat_243_shortpctfloat_sign_change_count_63_d1(shortpctfloat: pd.Series) -> pd.Series:
    """Count past 63 of short %-float trend reversals (21d slope sign flips)."""
    sl = _rolling_slope(shortpctfloat.astype(float), MDAYS)
    sgn = np.sign(sl)
    flip = ((sgn != sgn.shift(1)) & sl.notna() & sl.shift(1).notna()).astype(float)
    return (flip.rolling(QDAYS, min_periods=MDAYS).sum().where(sl.notna(), np.nan)).diff()


def f48_ssat_244_si_new_252d_low_events_count_252_d1(shortinterest: pd.Series) -> pd.Series:
    """Annual count of bars where SI = trailing 252d min — repeated new-SI-low events."""
    s = shortinterest.astype(float)
    return ((s <= s.rolling(YDAYS, min_periods=QDAYS).min()).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(s.notna(), np.nan)).diff()


def f48_ssat_245_lower_high_count_21_d1(high: pd.Series) -> pd.Series:
    """Lower-high count past 21 — short-horizon variant of 151."""
    rh = high.rolling(WDAYS, min_periods=2).max()
    lh = (rh < rh.shift(WDAYS)).astype(float)
    return (lh.rolling(MDAYS, min_periods=WDAYS).sum().where(rh.notna() & rh.shift(WDAYS).notna(), np.nan)).diff()


def f48_ssat_246_lower_high_count_504_d1(high: pd.Series) -> pd.Series:
    """Lower-high count past 504 (2y) — multi-year cooling structure."""
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    lh = (rh < rh.shift(MDAYS)).astype(float)
    return (lh.rolling(DDAYS_2Y, min_periods=YDAYS).sum().where(rh.notna() & rh.shift(MDAYS).notna(), np.nan)).diff()


def f48_ssat_247_lower_low_count_21_d1(low: pd.Series) -> pd.Series:
    """Lower-low count past 21 — short-horizon variant of 153."""
    rl = low.rolling(WDAYS, min_periods=2).min()
    ll = (rl < rl.shift(WDAYS)).astype(float)
    return (ll.rolling(MDAYS, min_periods=WDAYS).sum().where(rl.notna() & rl.shift(WDAYS).notna(), np.nan)).diff()


def f48_ssat_248_lower_low_count_504_d1(low: pd.Series) -> pd.Series:
    """Lower-low count past 504 — multi-year cascading-lows structure."""
    rl = low.rolling(MDAYS, min_periods=WDAYS).min()
    ll = (rl < rl.shift(MDAYS)).astype(float)
    return (ll.rolling(DDAYS_2Y, min_periods=YDAYS).sum().where(rl.notna() & rl.shift(MDAYS).notna(), np.nan)).diff()


def f48_ssat_249_new_252d_low_event_flag_d1(low: pd.Series) -> pd.Series:
    """1 if low equals trailing 252d min — new-annual-low event."""
    return ((low <= low.rolling(YDAYS, min_periods=QDAYS).min()).astype(float).where(low.notna(), np.nan)).diff()


def f48_ssat_250_new_504d_low_event_flag_d1(low: pd.Series) -> pd.Series:
    """1 if low equals trailing 504d min — 2-year new-low event."""
    return ((low <= low.rolling(DDAYS_2Y, min_periods=YDAYS).min()).astype(float).where(low.notna(), np.nan)).diff()


def f48_ssat_251_bars_since_new_504d_low_d1(low: pd.Series) -> pd.Series:
    """Bars since 2-year low event."""
    return (_bars_since_true(low <= low.rolling(DDAYS_2Y, min_periods=YDAYS).min())).diff()


def f48_ssat_252_bear_flag_count_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of bars satisfying bear-flag conditions (63d slope < -atr/bar AND 21d HL range < 0.5x 63d HL range)."""
    sl = _rolling_slope(close, QDAYS)
    a = _atr(high, low, close, MDAYS)
    rng_21 = (high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min())
    rng_63 = (high.rolling(QDAYS, min_periods=MDAYS).max() - low.rolling(QDAYS, min_periods=MDAYS).min())
    cond = ((sl < -1.0 * a) & (rng_21 < 0.5 * rng_63)).astype(float)
    return (cond.rolling(QDAYS, min_periods=MDAYS).sum().where(sl.notna() & a.notna(), np.nan)).diff()


def f48_ssat_253_log_slope_21d_below_neg_threshold_count_63_d1(close: pd.Series) -> pd.Series:
    """Count past 63 of bars where 21d log-price slope < -0.005 per bar — sustained-decline-bar count."""
    sl = _rolling_slope(_safe_log(close), MDAYS)
    return ((sl < -0.005).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(sl.notna(), np.nan)).diff()


def f48_ssat_254_bear_pennant_count_252_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count past 252 of bars where (high - low) past 21 is in lowest 10% of trailing 63d — sustained-compression count."""
    r = high - low
    r21 = r.rolling(MDAYS, min_periods=WDAYS).mean()
    q10_63 = r21.rolling(QDAYS, min_periods=MDAYS).quantile(0.10)
    cond = (r21 <= q10_63).astype(float)
    return (cond.rolling(YDAYS, min_periods=QDAYS).sum().where(q10_63.notna(), np.nan)).diff()


def f48_ssat_255_dist_aVWAP_from_504d_peak_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - aVWAP-from-504d-peak) / ATR21 — distance from multi-year-peak-anchored VWAP in ATR21."""
    avwap = _anchored_vwap_from_rolling_high(close, volume, high, DDAYS_2Y)
    return (_safe_div(close - avwap, _atr(high, low, close, MDAYS))).diff()


def f48_ssat_256_dist_aVWAP_from_504d_peak_pct_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close / aVWAP-from-504d-peak) - 1 — pct distance from 2y-peak-anchored VWAP."""
    avwap = _anchored_vwap_from_rolling_high(close, volume, high, DDAYS_2Y)
    return (_safe_div(close, avwap) - 1.0).diff()


def f48_ssat_257_dist_aVWAP_from_alltime_peak_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - aVWAP-from-all-time-peak) / ATR21 — distance from cumulative-peak-anchored VWAP."""
    avwap = _anchored_vwap_from_cummax_high(close, volume, high)
    return (_safe_div(close - avwap, _atr(high, low, close, MDAYS))).diff()


def f48_ssat_258_dist_aVWAP_from_alltime_peak_pct_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close / aVWAP-from-all-time-peak) - 1 — pct distance from cumulative-peak-anchored VWAP."""
    avwap = _anchored_vwap_from_cummax_high(close, volume, high)
    return (_safe_div(close, avwap) - 1.0).diff()


def f48_ssat_259_aVWAP_from_peak_slope_21_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of anchored-VWAP-from-peak — VWAP drift since peak (negative = peak-VWAP declining)."""
    avwap = _anchored_vwap_from_rolling_high(close, volume, high, YDAYS)
    return (_rolling_slope(avwap, MDAYS)).diff()


def f48_ssat_260_aVWAP_from_peak_vs_sma200_signed_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """sign(aVWAP-from-peak - SMA200) — which is higher (1 = peak-VWAP, -1 = SMA200, 0 = tied)."""
    avwap = _anchored_vwap_from_rolling_high(close, volume, high, YDAYS)
    sma = _sma(close, 200)
    return (np.sign(avwap - sma)).diff()


def f48_ssat_261_close_below_aVWAP_from_peak_30pct_state_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if (close / aVWAP-from-peak) - 1 <= -0.30 — 30%+ below peak-anchored VWAP."""
    avwap = _anchored_vwap_from_rolling_high(close, volume, high, YDAYS)
    return (((_safe_div(close, avwap) - 1.0) <= -0.30).astype(float).where(avwap.notna(), np.nan)).diff()


def f48_ssat_262_close_below_aVWAP_from_peak_50pct_state_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 50%+ below peak-anchored VWAP — deep underwater state."""
    avwap = _anchored_vwap_from_rolling_high(close, volume, high, YDAYS)
    return (((_safe_div(close, avwap) - 1.0) <= -0.50).astype(float).where(avwap.notna(), np.nan)).diff()


def f48_ssat_263_rally_count_10pct_in_5d_past_63_d1(close: pd.Series) -> pd.Series:
    """Count past 63 of bars where 5d return > 10% — strong-rally count."""
    return ((close.pct_change(WDAYS) > 0.10).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(close.pct_change(WDAYS).notna(), np.nan)).diff()


def f48_ssat_264_failed_rally_below_prelow_count_63_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 of bars where 5d-prior had rally (5d ret >5%) AND today's close < low from 10 bars ago."""
    rally_prior = (close.pct_change(WDAYS).shift(WDAYS) > 0.05)
    below_pre = (close < low.shift(2 * WDAYS))
    return ((rally_prior & below_pre).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(close.shift(2 * WDAYS).notna(), np.nan)).diff()


def f48_ssat_265_v_bottom_count_63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count past 63 of bars where capit-bar 5 bars ago AND 5d cum return now > 10% — V-bottom recovery count."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = (move < -3.0 * a) & (v_ratio > 3.0)
    cond = capit.shift(WDAYS) & (close.pct_change(WDAYS) > 0.10)
    return (cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(a.notna() & v_ratio.notna(), np.nan)).diff()


def f48_ssat_266_failed_v_bottom_count_63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count past 63 of bars where V-bottom occurred 5 bars ago AND today's close < that capit-bar's low."""
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit = (move < -3.0 * a) & (v_ratio > 3.0)
    capit_10_ago = capit.shift(2 * WDAYS)
    vbottom_5_ago = capit.shift(WDAYS) & (close.shift(0) > close.shift(WDAYS)) & (close.pct_change(WDAYS) > 0.05)  # not used directly
    # Simpler implementation: at bar t, if capit at t-10 AND close[t] < low[t-10]
    failed = capit_10_ago & (close < low.shift(2 * WDAYS))
    return (failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(a.notna() & v_ratio.notna(), np.nan)).diff()


def f48_ssat_267_max_5d_return_past_63_d1(close: pd.Series) -> pd.Series:
    """Max 5d return over past 63 — peak rally amplitude (recent)."""
    return (close.pct_change(WDAYS).rolling(QDAYS, min_periods=MDAYS).max()).diff()


def f48_ssat_268_max_5d_return_past_252_d1(close: pd.Series) -> pd.Series:
    """Max 5d return over past 252 — peak rally amplitude (annual)."""
    return (close.pct_change(WDAYS).rolling(YDAYS, min_periods=QDAYS).max()).diff()


def f48_ssat_269_bars_since_max_5d_rally_252_d1(close: pd.Series) -> pd.Series:
    """Bars since the 252d max-5d-return event."""
    r5 = close.pct_change(WDAYS)
    rmax = r5.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(r5 == rmax)).diff()


def f48_ssat_270_rally_then_lower_high_count_252_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 252 of bars where 5d-rally (>5%) occurred 21 bars ago AND today's 21d-rolling-high < 21d-rolling-high of that rally bar."""
    rh = high.rolling(MDAYS, min_periods=WDAYS).max()
    rally_21_ago = (close.pct_change(WDAYS).shift(MDAYS) > 0.05)
    cond = rally_21_ago & (rh < rh.shift(MDAYS))
    return (cond.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(rh.notna() & rh.shift(MDAYS).notna(), np.nan)).diff()


def f48_ssat_271_dist_day_cluster_3_in_5_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 3+ distribution days in past 5 bars — tight-cluster warning."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    cnt = (down & bigvol).astype(float).rolling(WDAYS, min_periods=2).sum()
    return ((cnt >= 3).astype(float).where(close.notna(), np.nan)).diff()


def f48_ssat_272_bars_since_last_distribution_day_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent distribution day."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    return (_bars_since_true(down & bigvol)).diff()


def f48_ssat_273_dist_minus_accum_ratio_63_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(distribution count - accumulation count) / (total volume-event count) past 63 — net institutional pressure ratio."""
    down = close < close.shift(1)
    up = close > close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    dist = (down & bigvol).astype(float)
    accum = (up & bigvol).astype(float)
    num = dist.rolling(QDAYS, min_periods=MDAYS).sum() - accum.rolling(QDAYS, min_periods=MDAYS).sum()
    den = (dist + accum).rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(num, den)).diff()


def f48_ssat_274_heavy_down_day_count_63_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count past 63 of bars with return < -3% AND vol > 1.5x 21d avg — heavy-down-day count."""
    r = close.pct_change()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (r < -0.03) & (volume > 1.5 * v_avg)
    return (cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(v_avg.notna(), np.nan)).diff()


def f48_ssat_275_heavy_down_day_count_252_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual heavy-down-day count."""
    r = close.pct_change()
    v_avg = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    cond = (r < -0.03) & (volume > 1.5 * v_avg)
    return (cond.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(v_avg.notna(), np.nan)).diff()


def f48_ssat_276_largest_down_day_return_past_252_d1(close: pd.Series) -> pd.Series:
    """Most-negative 1-bar return in past 252 — worst single-day shock."""
    return (close.pct_change().rolling(YDAYS, min_periods=QDAYS).min()).diff()


def f48_ssat_277_dist_day_streak_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive distribution-day streak."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    return (_streak_true(down & bigvol)).diff()


def f48_ssat_278_longest_dist_day_streak_252_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Longest dist-day streak in past 252."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    s = _streak_true(down & bigvol)
    return (s.rolling(YDAYS, min_periods=QDAYS).max().where(close.notna(), np.nan)).diff()


def f48_ssat_279_atr_pct_close_lowest_decile_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ATR21/close <= 10th-pct of trailing 252d distribution — % terminal-vol contraction."""
    ratio = _safe_div(_atr(high, low, close, MDAYS), close)
    q = ratio.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return ((ratio <= q).astype(float).where(q.notna(), np.nan)).diff()


def f48_ssat_280_atr_over_avg_vol_21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ATR21 / 21d-avg-volume — price-vol per traded share unit (Amihud-ish in ATR units)."""
    return (_safe_div(_atr(high, low, close, MDAYS), volume.rolling(MDAYS, min_periods=WDAYS).mean())).diff()


def f48_ssat_281_atr5_over_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR5 / ATR21 — vol-shrinkage rate (<1 means short-term vol contracting)."""
    return (_safe_div(_atr(high, low, close, WDAYS), _atr(high, low, close, MDAYS))).diff()


def f48_ssat_282_bars_since_returns_std_252d_max_d1(close: pd.Series) -> pd.Series:
    """Bars since 21d-std-of-returns hit its 252d max — recency of last realized-vol peak."""
    s = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    return (_bars_since_true(s == s.rolling(YDAYS, min_periods=QDAYS).max())).diff()


def f48_ssat_283_hl_range_cv_63_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of HL range past 63 — range-vol volatility (lower = more orderly)."""
    r = high - low
    return (_safe_div(r.rolling(QDAYS, min_periods=MDAYS).std(), r.rolling(QDAYS, min_periods=MDAYS).mean())).diff()


def f48_ssat_284_median_tr_past_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Median TR over past 63 bars — typical-bar-size in the recent regime."""
    return (_true_range(high, low, close).rolling(QDAYS, min_periods=MDAYS).median()).diff()


def f48_ssat_285_log_vol_zscore_252_d1(volume: pd.Series) -> pd.Series:
    """Z-score (252d) of log(volume) — log-scale volume regime."""
    return (_rolling_zscore(_safe_log(volume), YDAYS, min_periods=QDAYS)).diff()


def f48_ssat_286_vol_of_vol_zscore_252_d1(close: pd.Series) -> pd.Series:
    """Z-score (252d) of (21d-std of 21d-std of returns) — vol-of-vol regime."""
    rv = close.pct_change().rolling(MDAYS, min_periods=WDAYS).std()
    vov = rv.rolling(MDAYS, min_periods=WDAYS).std()
    return (_rolling_zscore(vov, YDAYS, min_periods=QDAYS)).diff()


def f48_ssat_287_si_fell_below_sma200_5plus_capit_21_d1(shortinterest: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if SI fell >50% from 252d max AND close < SMA200 AND 5+ capit bars in past 21 — terminal-distress 3-cond."""
    s = shortinterest.astype(float)
    si_unwound = s < 0.5 * s.rolling(YDAYS, min_periods=QDAYS).max()
    sma = _sma(close, 200)
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit_cnt = ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((si_unwound & (close < sma) & (capit_cnt >= 5)).astype(float).where(s.notna() & sma.notna() & a.notna(), np.nan)).diff()


def f48_ssat_288_si_252d_low_and_close_252d_low_d1(shortinterest: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SI at 252d min AND close at 252d min — joint-floor state."""
    s = shortinterest.astype(float)
    return (((s <= s.rolling(YDAYS, min_periods=QDAYS).min()) & (close <= low.rolling(YDAYS, min_periods=QDAYS).min())).astype(float).where(s.notna() & low.rolling(YDAYS, min_periods=QDAYS).min().notna(), np.nan)).diff()


def f48_ssat_289_dtc_252d_low_and_below_sma200_d1(daystocover: pd.Series, close: pd.Series) -> pd.Series:
    """1 if daystocover at 252d min AND close < SMA200."""
    d = daystocover.astype(float)
    sma = _sma(close, 200)
    return (((d <= d.rolling(YDAYS, min_periods=QDAYS).min()) & (close < sma)).astype(float).where(d.notna() & sma.notna(), np.nan)).diff()


def f48_ssat_290_shortpctfloat_below_5_lower_lows_5_in_21_d1(shortpctfloat: pd.Series, low: pd.Series) -> pd.Series:
    """1 if short %-float < 5% AND 5+ lower-lows (21d-low < 21d-low 5 bars ago) in past 21."""
    spf = shortpctfloat.astype(float)
    rl = low.rolling(WDAYS, min_periods=2).min()
    ll = (rl < rl.shift(WDAYS)).astype(float)
    ll_count = ll.rolling(MDAYS, min_periods=WDAYS).sum()
    return (((spf < 5.0) & (ll_count >= 5)).astype(float).where(spf.notna() & rl.notna(), np.nan)).diff()


def f48_ssat_291_shortpctfloat_decline_plus_3_lower_lows_21_d1(shortpctfloat: pd.Series, low: pd.Series) -> pd.Series:
    """1 if short %-float 21d slope < 0 AND 3+ lower-lows in past 21."""
    spf_sl = _rolling_slope(shortpctfloat.astype(float), MDAYS)
    rl = low.rolling(WDAYS, min_periods=2).min()
    ll = (rl < rl.shift(WDAYS)).astype(float)
    ll_count = ll.rolling(MDAYS, min_periods=WDAYS).sum()
    return (((spf_sl < 0) & (ll_count >= 3)).astype(float).where(spf_sl.notna() & rl.notna(), np.nan)).diff()


def f48_ssat_292_si_mean_reverted_plus_below_sma50_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """1 if |SI - 252d mean| < 0.5 std AND close < SMA50 — SI normalized, but price still weak."""
    s = shortinterest.astype(float)
    m = s.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = s.rolling(YDAYS, min_periods=QDAYS).std()
    return ((((s - m).abs() < 0.5 * sd) & (close < _sma(close, 50))).astype(float).where(sd.notna() & _sma(close, 50).notna(), np.nan)).diff()


def f48_ssat_293_extended_aftermath_score_d1(shortinterest: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """SI-decline-pct × |drawdown-pct| × (1 + capit-count-past-63) — extended aftermath intensity."""
    s = shortinterest.astype(float)
    smax = s.rolling(YDAYS, min_periods=QDAYS).max()
    si_dec_pct = _safe_div(smax - s, smax)
    dd = (_safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0).abs()
    a = _atr(high, low, close, MDAYS)
    move = close - close.shift(1)
    v_ratio = _safe_div(volume, volume.rolling(MDAYS, min_periods=WDAYS).mean())
    capit_cnt = ((move < -3.0 * a) & (v_ratio > 3.0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return (si_dec_pct * dd * (1.0 + capit_cnt)).diff()


def f48_ssat_294_si_rising_price_declining_21_d1(shortinterest: pd.Series, close: pd.Series) -> pd.Series:
    """1 if SI 21d slope > 0 AND 21d return < 0 — fresh-shorts building bearish bet."""
    sl_si = _rolling_slope(shortinterest.astype(float), MDAYS)
    r21 = close.pct_change(MDAYS)
    return (((sl_si > 0) & (r21 < 0)).astype(float).where(sl_si.notna() & r21.notna(), np.nan)).diff()


def f48_ssat_295_dwell_below_sma200_past_252_d1(close: pd.Series) -> pd.Series:
    """Fraction past 252 days with close < SMA200 — sustained-breakdown dwell."""
    sma = _sma(close, 200)
    return ((close < sma).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(sma.notna(), np.nan)).diff()


def f48_ssat_296_max_drawdown_past_252_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Min drawdown (most-negative) in past 252 — worst drawdown observed."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return (dd.rolling(YDAYS, min_periods=QDAYS).min()).diff()


def f48_ssat_297_max_drawdown_past_504_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Min drawdown in past 504 — multi-year worst drawdown."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    return (dd.rolling(DDAYS_2Y, min_periods=YDAYS).min()).diff()


def f48_ssat_298_consecutive_dd_below_neg50_streak_252_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    """Longest consecutive-bars-with-drawdown <=-50% streak in past 252."""
    dd = _safe_div(close, high.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0
    s = _streak_true(dd <= -0.5)
    return (s.rolling(YDAYS, min_periods=QDAYS).max().where(dd.notna(), np.nan)).diff()


def f48_ssat_299_rolling_252d_return_d1(close: pd.Series) -> pd.Series:
    """Trailing 252-day return (1-year return) — annual performance (negative = bear regime)."""
    return (close.pct_change(YDAYS)).diff()


def f48_ssat_300_rolling_504d_return_d1(close: pd.Series) -> pd.Series:
    """Trailing 504-day return (2-year return) — multi-year performance."""
    return (close.pct_change(DDAYS_2Y)).diff()


# ============================================================
#                         REGISTRY 226-300 (d1)
# ============================================================

_HC = ["high", "close"]
_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_CV = ["close", "volume"]
_HCV = ["high", "close", "volume"]

SHORT_SQUEEZE_AFTERMATH_TECHNICAL_D1_REGISTRY_226_300 = {
    "f48_ssat_226_si_pct_rank_504_d1": {"inputs": ["shortinterest"], "func": f48_ssat_226_si_pct_rank_504_d1},
    "f48_ssat_227_dtc_pct_rank_252_d1": {"inputs": ["daystocover"], "func": f48_ssat_227_dtc_pct_rank_252_d1},
    "f48_ssat_228_shortpctfloat_pct_rank_252_d1": {"inputs": ["shortpctfloat"], "func": f48_ssat_228_shortpctfloat_pct_rank_252_d1},
    "f48_ssat_229_shortpctfloat_at_252d_max_flag_d1": {"inputs": ["shortpctfloat"], "func": f48_ssat_229_shortpctfloat_at_252d_max_flag_d1},
    "f48_ssat_230_shortpctfloat_at_252d_min_flag_d1": {"inputs": ["shortpctfloat"], "func": f48_ssat_230_shortpctfloat_at_252d_min_flag_d1},
    "f48_ssat_231_dtc_at_252d_max_flag_d1": {"inputs": ["daystocover"], "func": f48_ssat_231_dtc_at_252d_max_flag_d1},
    "f48_ssat_232_si_std_252_d1": {"inputs": ["shortinterest"], "func": f48_ssat_232_si_std_252_d1},
    "f48_ssat_233_si_range_over_mean_252_d1": {"inputs": ["shortinterest"], "func": f48_ssat_233_si_range_over_mean_252_d1},
    "f48_ssat_234_si_entropy_252_d1": {"inputs": ["shortinterest"], "func": f48_ssat_234_si_entropy_252_d1},
    "f48_ssat_235_si_recent_over_annual_avg_d1": {"inputs": ["shortinterest"], "func": f48_ssat_235_si_recent_over_annual_avg_d1},
    "f48_ssat_236_si_5d_pct_change_d1": {"inputs": ["shortinterest"], "func": f48_ssat_236_si_5d_pct_change_d1},
    "f48_ssat_237_dtc_5d_change_d1": {"inputs": ["daystocover"], "func": f48_ssat_237_dtc_5d_change_d1},
    "f48_ssat_238_si_21d_slope_acceleration_d1": {"inputs": ["shortinterest"], "func": f48_ssat_238_si_21d_slope_acceleration_d1},
    "f48_ssat_239_si_weekly_change_zscore_252_d1": {"inputs": ["shortinterest"], "func": f48_ssat_239_si_weekly_change_zscore_252_d1},
    "f48_ssat_240_si_monthly_change_zscore_252_d1": {"inputs": ["shortinterest"], "func": f48_ssat_240_si_monthly_change_zscore_252_d1},
    "f48_ssat_241_si_slope_sign_reversal_count_63_d1": {"inputs": ["shortinterest"], "func": f48_ssat_241_si_slope_sign_reversal_count_63_d1},
    "f48_ssat_242_dtc_sign_change_count_63_d1": {"inputs": ["daystocover"], "func": f48_ssat_242_dtc_sign_change_count_63_d1},
    "f48_ssat_243_shortpctfloat_sign_change_count_63_d1": {"inputs": ["shortpctfloat"], "func": f48_ssat_243_shortpctfloat_sign_change_count_63_d1},
    "f48_ssat_244_si_new_252d_low_events_count_252_d1": {"inputs": ["shortinterest"], "func": f48_ssat_244_si_new_252d_low_events_count_252_d1},
    "f48_ssat_245_lower_high_count_21_d1": {"inputs": ["high"], "func": f48_ssat_245_lower_high_count_21_d1},
    "f48_ssat_246_lower_high_count_504_d1": {"inputs": ["high"], "func": f48_ssat_246_lower_high_count_504_d1},
    "f48_ssat_247_lower_low_count_21_d1": {"inputs": ["low"], "func": f48_ssat_247_lower_low_count_21_d1},
    "f48_ssat_248_lower_low_count_504_d1": {"inputs": ["low"], "func": f48_ssat_248_lower_low_count_504_d1},
    "f48_ssat_249_new_252d_low_event_flag_d1": {"inputs": ["low"], "func": f48_ssat_249_new_252d_low_event_flag_d1},
    "f48_ssat_250_new_504d_low_event_flag_d1": {"inputs": ["low"], "func": f48_ssat_250_new_504d_low_event_flag_d1},
    "f48_ssat_251_bars_since_new_504d_low_d1": {"inputs": ["low"], "func": f48_ssat_251_bars_since_new_504d_low_d1},
    "f48_ssat_252_bear_flag_count_63_d1": {"inputs": _HLC, "func": f48_ssat_252_bear_flag_count_63_d1},
    "f48_ssat_253_log_slope_21d_below_neg_threshold_count_63_d1": {"inputs": ["close"], "func": f48_ssat_253_log_slope_21d_below_neg_threshold_count_63_d1},
    "f48_ssat_254_bear_pennant_count_252_d1": {"inputs": ["high", "low"], "func": f48_ssat_254_bear_pennant_count_252_d1},
    "f48_ssat_255_dist_aVWAP_from_504d_peak_atr21_d1": {"inputs": _HLCV, "func": f48_ssat_255_dist_aVWAP_from_504d_peak_atr21_d1},
    "f48_ssat_256_dist_aVWAP_from_504d_peak_pct_d1": {"inputs": _HCV, "func": f48_ssat_256_dist_aVWAP_from_504d_peak_pct_d1},
    "f48_ssat_257_dist_aVWAP_from_alltime_peak_atr21_d1": {"inputs": _HLCV, "func": f48_ssat_257_dist_aVWAP_from_alltime_peak_atr21_d1},
    "f48_ssat_258_dist_aVWAP_from_alltime_peak_pct_d1": {"inputs": _HCV, "func": f48_ssat_258_dist_aVWAP_from_alltime_peak_pct_d1},
    "f48_ssat_259_aVWAP_from_peak_slope_21_d1": {"inputs": _HCV, "func": f48_ssat_259_aVWAP_from_peak_slope_21_d1},
    "f48_ssat_260_aVWAP_from_peak_vs_sma200_signed_d1": {"inputs": _HCV, "func": f48_ssat_260_aVWAP_from_peak_vs_sma200_signed_d1},
    "f48_ssat_261_close_below_aVWAP_from_peak_30pct_state_d1": {"inputs": _HCV, "func": f48_ssat_261_close_below_aVWAP_from_peak_30pct_state_d1},
    "f48_ssat_262_close_below_aVWAP_from_peak_50pct_state_d1": {"inputs": _HCV, "func": f48_ssat_262_close_below_aVWAP_from_peak_50pct_state_d1},
    "f48_ssat_263_rally_count_10pct_in_5d_past_63_d1": {"inputs": ["close"], "func": f48_ssat_263_rally_count_10pct_in_5d_past_63_d1},
    "f48_ssat_264_failed_rally_below_prelow_count_63_d1": {"inputs": ["low", "close"], "func": f48_ssat_264_failed_rally_below_prelow_count_63_d1},
    "f48_ssat_265_v_bottom_count_63_d1": {"inputs": _HLCV, "func": f48_ssat_265_v_bottom_count_63_d1},
    "f48_ssat_266_failed_v_bottom_count_63_d1": {"inputs": _HLCV, "func": f48_ssat_266_failed_v_bottom_count_63_d1},
    "f48_ssat_267_max_5d_return_past_63_d1": {"inputs": ["close"], "func": f48_ssat_267_max_5d_return_past_63_d1},
    "f48_ssat_268_max_5d_return_past_252_d1": {"inputs": ["close"], "func": f48_ssat_268_max_5d_return_past_252_d1},
    "f48_ssat_269_bars_since_max_5d_rally_252_d1": {"inputs": ["close"], "func": f48_ssat_269_bars_since_max_5d_rally_252_d1},
    "f48_ssat_270_rally_then_lower_high_count_252_d1": {"inputs": _HC, "func": f48_ssat_270_rally_then_lower_high_count_252_d1},
    "f48_ssat_271_dist_day_cluster_3_in_5_d1": {"inputs": _CV, "func": f48_ssat_271_dist_day_cluster_3_in_5_d1},
    "f48_ssat_272_bars_since_last_distribution_day_d1": {"inputs": _CV, "func": f48_ssat_272_bars_since_last_distribution_day_d1},
    "f48_ssat_273_dist_minus_accum_ratio_63_d1": {"inputs": _CV, "func": f48_ssat_273_dist_minus_accum_ratio_63_d1},
    "f48_ssat_274_heavy_down_day_count_63_d1": {"inputs": _CV, "func": f48_ssat_274_heavy_down_day_count_63_d1},
    "f48_ssat_275_heavy_down_day_count_252_d1": {"inputs": _CV, "func": f48_ssat_275_heavy_down_day_count_252_d1},
    "f48_ssat_276_largest_down_day_return_past_252_d1": {"inputs": ["close"], "func": f48_ssat_276_largest_down_day_return_past_252_d1},
    "f48_ssat_277_dist_day_streak_d1": {"inputs": _CV, "func": f48_ssat_277_dist_day_streak_d1},
    "f48_ssat_278_longest_dist_day_streak_252_d1": {"inputs": _CV, "func": f48_ssat_278_longest_dist_day_streak_252_d1},
    "f48_ssat_279_atr_pct_close_lowest_decile_252_d1": {"inputs": _HLC, "func": f48_ssat_279_atr_pct_close_lowest_decile_252_d1},
    "f48_ssat_280_atr_over_avg_vol_21_d1": {"inputs": _HLCV, "func": f48_ssat_280_atr_over_avg_vol_21_d1},
    "f48_ssat_281_atr5_over_atr21_d1": {"inputs": _HLC, "func": f48_ssat_281_atr5_over_atr21_d1},
    "f48_ssat_282_bars_since_returns_std_252d_max_d1": {"inputs": ["close"], "func": f48_ssat_282_bars_since_returns_std_252d_max_d1},
    "f48_ssat_283_hl_range_cv_63_d1": {"inputs": ["high", "low"], "func": f48_ssat_283_hl_range_cv_63_d1},
    "f48_ssat_284_median_tr_past_63_d1": {"inputs": _HLC, "func": f48_ssat_284_median_tr_past_63_d1},
    "f48_ssat_285_log_vol_zscore_252_d1": {"inputs": ["volume"], "func": f48_ssat_285_log_vol_zscore_252_d1},
    "f48_ssat_286_vol_of_vol_zscore_252_d1": {"inputs": ["close"], "func": f48_ssat_286_vol_of_vol_zscore_252_d1},
    "f48_ssat_287_si_fell_below_sma200_5plus_capit_21_d1": {"inputs": ["shortinterest", "high", "low", "close", "volume"], "func": f48_ssat_287_si_fell_below_sma200_5plus_capit_21_d1},
    "f48_ssat_288_si_252d_low_and_close_252d_low_d1": {"inputs": ["shortinterest", "low", "close"], "func": f48_ssat_288_si_252d_low_and_close_252d_low_d1},
    "f48_ssat_289_dtc_252d_low_and_below_sma200_d1": {"inputs": ["daystocover", "close"], "func": f48_ssat_289_dtc_252d_low_and_below_sma200_d1},
    "f48_ssat_290_shortpctfloat_below_5_lower_lows_5_in_21_d1": {"inputs": ["shortpctfloat", "low"], "func": f48_ssat_290_shortpctfloat_below_5_lower_lows_5_in_21_d1},
    "f48_ssat_291_shortpctfloat_decline_plus_3_lower_lows_21_d1": {"inputs": ["shortpctfloat", "low"], "func": f48_ssat_291_shortpctfloat_decline_plus_3_lower_lows_21_d1},
    "f48_ssat_292_si_mean_reverted_plus_below_sma50_d1": {"inputs": ["shortinterest", "close"], "func": f48_ssat_292_si_mean_reverted_plus_below_sma50_d1},
    "f48_ssat_293_extended_aftermath_score_d1": {"inputs": ["shortinterest", "high", "low", "close", "volume"], "func": f48_ssat_293_extended_aftermath_score_d1},
    "f48_ssat_294_si_rising_price_declining_21_d1": {"inputs": ["shortinterest", "close"], "func": f48_ssat_294_si_rising_price_declining_21_d1},
    "f48_ssat_295_dwell_below_sma200_past_252_d1": {"inputs": ["close"], "func": f48_ssat_295_dwell_below_sma200_past_252_d1},
    "f48_ssat_296_max_drawdown_past_252_d1": {"inputs": _HC, "func": f48_ssat_296_max_drawdown_past_252_d1},
    "f48_ssat_297_max_drawdown_past_504_d1": {"inputs": _HC, "func": f48_ssat_297_max_drawdown_past_504_d1},
    "f48_ssat_298_consecutive_dd_below_neg50_streak_252_d1": {"inputs": _HC, "func": f48_ssat_298_consecutive_dd_below_neg50_streak_252_d1},
    "f48_ssat_299_rolling_252d_return_d1": {"inputs": ["close"], "func": f48_ssat_299_rolling_252d_return_d1},
    "f48_ssat_300_rolling_504d_return_d1": {"inputs": ["close"], "func": f48_ssat_300_rolling_504d_return_d1},
}
