"""terminal_distribution_composite base features 226-300 — Pipeline 1b-technical.

Extends 151-225 with 75 distinct hypotheses across:
P: Drawdown-shape characteristics (skew, kurt, autocorr, pareto tail, underwater curve).
Q: Recovery-failure metrics (amplitude decay, recovery streaks, consistency).
R: Structural age / cycle position (uptrend age, downtrend age, dominant cycle).
S: Volume-price profile / range distribution (skew/kurt of close & volume).
T: Cross-confirmation with momentum (MA distance at peak / decay / alignment).
U: Cross-validation with prior history (504d regime change, historical extremes).
V: Aggregate terminal-distribution composites v2.

Inputs: SEP OHLCV. PIT-clean (right-anchored rolling, no centered, no shift(-N)).
Self-contained helpers — no cross-family imports.
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


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


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
# Bucket P — Drawdown-shape characteristics (226-235)
# ============================================================

def f50_tdco_226_max_drawdown_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Max value of running drawdown over past 252 — worst peak-to-trough decline of 252d window."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return dd.rolling(YDAYS, min_periods=QDAYS).max()


def f50_tdco_227_drawdown_skew_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of the drawdown series over 252 — asymmetry of underwater distribution."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return dd.rolling(YDAYS, min_periods=QDAYS).skew()


def f50_tdco_228_drawdown_kurtosis_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Kurtosis of drawdown series over 252 — fat-tailed drawdown distribution."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return dd.rolling(YDAYS, min_periods=QDAYS).kurt()


def f50_tdco_229_drawdown_autocorrelation_lag1_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of drawdown over 63 bars — persistence of underwater state."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return dd.rolling(QDAYS, min_periods=MDAYS).corr(dd.shift(1))


def f50_tdco_230_drawdown_pareto_alpha_proxy_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Pareto tail index proxy of drawdown over 252: 1 / mean(log(dd / dd_min)) on top-10% drawdowns.
    Smaller alpha = heavier tail."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    def _alpha(w):
        v = w[~np.isnan(w)]
        v = v[v > 0]
        if v.size < 30:
            return np.nan
        thr = np.quantile(v, 0.90)
        tail = v[v >= thr]
        if tail.size < 3 or thr <= 0:
            return np.nan
        denom = float(np.mean(np.log(tail / thr)))
        if denom <= 0:
            return np.nan
        return 1.0 / denom
    return dd.rolling(YDAYS, min_periods=QDAYS).apply(_alpha, raw=True)


def f50_tdco_231_drawdown_avg_duration_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Average duration (bars) of drawdown episodes (dd > 5%) in past 252."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    under = (dd > 0.05).astype(float)
    streak = _streak_true(under > 0.5)
    # episode end = streak transitions from >0 to 0
    end = (streak.shift(1) > 0) & (streak == 0)
    ep_len = streak.shift(1).where(end, 0)
    avg = _safe_div(ep_len.rolling(YDAYS, min_periods=QDAYS).sum(),
                    end.astype(float).rolling(YDAYS, min_periods=QDAYS).sum())
    return avg.where(rmax.notna(), np.nan)


def f50_tdco_232_drawdown_max_duration_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Max duration (bars) of any drawdown (dd > 5%) episode in past 252."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    streak = _streak_true(dd > 0.05)
    return streak.rolling(YDAYS, min_periods=QDAYS).max().where(rmax.notna(), np.nan)


def f50_tdco_233_underwater_curve_area_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Integral (sum) of drawdown over past 252 — total underwater area (depth × duration product)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return dd.rolling(YDAYS, min_periods=QDAYS).sum()


def f50_tdco_234_drawdown_to_atr_ratio_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(63d drawdown from 63d max) / (ATR(21) / close) — drawdown in vol-normalized units."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    atr_pct = _safe_div(_atr(high, low, close, MDAYS), close)
    return _safe_div(dd, atr_pct)


def f50_tdco_235_drawdown_velocity_skew_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of drawdown daily changes over 63 — asymmetry of drawdown rate (negative = sharp drops dominate recovery rebounds)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    return dd.diff().rolling(QDAYS, min_periods=MDAYS).skew()


# ============================================================
# Bucket Q — Recovery-failure metrics (236-245)
# ============================================================

def f50_tdco_236_recovery_attempt_amplitude_decay_63(close: pd.Series) -> pd.Series:
    """Each rally smaller than the last: 63d slope of rolling 21d max(close) - rolling 21d min(close) sequence.
    Negative slope = each rally amplitude decaying."""
    amp = close.rolling(MDAYS, min_periods=WDAYS).max() - close.rolling(MDAYS, min_periods=WDAYS).min()
    return _rolling_slope(amp, QDAYS)


def f50_tdco_237_recovery_time_to_amplitude_ratio_63(close: pd.Series) -> pd.Series:
    """(63d count of bounces) / (63d avg-bounce-amplitude) — many small failed bounces = high ratio."""
    bounce = (close.pct_change(WDAYS) > 0.05).astype(float)
    cnt = bounce.rolling(QDAYS, min_periods=MDAYS).sum()
    amp = close.pct_change(WDAYS).where(bounce > 0, np.nan).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(cnt, amp)


def f50_tdco_238_expected_recovery_failure_probability_proxy_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Proxy for P(failure | recovery attempt) = failed-bounces / total-bounces in 63 — empirical failure rate."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h21)
    return _safe_div(failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum(),
                     bounce.astype(float).rolling(QDAYS, min_periods=MDAYS).sum())


def f50_tdco_239_partial_recovery_failure_count_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bounces (5d return > 5%) in 63 where high recovered 30-70% of prior drawdown but failed beyond — partial fails."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    # recovery fraction = (current close - 63d min) / (63d max - 63d min)
    pos = _safe_div(close - close.rolling(QDAYS, min_periods=MDAYS).min(),
                    rmax - close.rolling(QDAYS, min_periods=MDAYS).min())
    partial = bounce & (pos > 0.30) & (pos < 0.70)
    return partial.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(rmax.notna(), np.nan)


def f50_tdco_240_fully_failed_recovery_count_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bounces in 63 where recovery fraction < 30% — fully-failed recoveries."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    pos = _safe_div(close - close.rolling(QDAYS, min_periods=MDAYS).min(),
                    rmax - close.rolling(QDAYS, min_periods=MDAYS).min())
    fully_failed = bounce & (pos < 0.30)
    return fully_failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(rmax.notna(), np.nan)


def f50_tdco_241_mean_recovery_attempt_size_63(close: pd.Series) -> pd.Series:
    """Average size of bounce attempts (mean of positive 5d returns > 5%) in past 63 bars."""
    r5 = close.pct_change(WDAYS)
    bounce_size = r5.where(r5 > 0.05, np.nan)
    return bounce_size.rolling(QDAYS, min_periods=MDAYS).mean()


def f50_tdco_242_max_recovery_attempt_size_63(close: pd.Series) -> pd.Series:
    """Maximum bounce size in past 63 bars (max of 5d returns)."""
    return close.pct_change(WDAYS).rolling(QDAYS, min_periods=MDAYS).max()


def f50_tdco_243_recovery_amplitude_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of 21d-range (close-max - close-min) over 252 — extreme recovery amplitude vs history."""
    amp = close.rolling(MDAYS, min_periods=WDAYS).max() - close.rolling(MDAYS, min_periods=WDAYS).min()
    return _rolling_zscore(amp, YDAYS, min_periods=QDAYS)


def f50_tdco_244_recovery_consistency_score_63(close: pd.Series) -> pd.Series:
    """Std of bounce sizes (positive 5d returns > 5%) over 63 / mean — coefficient of variation of recoveries.
    Lower = more consistent; higher = erratic/unreliable recoveries."""
    r5 = close.pct_change(WDAYS)
    b = r5.where(r5 > 0.05, np.nan)
    sd = b.rolling(QDAYS, min_periods=MDAYS).std()
    m = b.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(sd, m)


def f50_tdco_245_recovery_streak_failure_breakdown_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if recent up-streak (3+ consecutive up-close bars) was immediately followed by close < 21d low.
    PIT-clean: today close < prior 21d low AND yesterday's streak was >=3."""
    streak_up = _streak_true(close.diff() > 0)
    streak_y = streak_up.shift(1)
    prior_ll = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    brk_today = close < prior_ll
    ev = (streak_y >= 3) & brk_today
    return ev.astype(float).where(prior_ll.notna(), np.nan)


# ============================================================
# Bucket R — Structural age / cycle position (246-255)
# ============================================================

def f50_tdco_246_age_current_uptrend_252(close: pd.Series) -> pd.Series:
    """Bars since the last cross above SMA200 — live age of current uptrend (NaN if currently below)."""
    s = _sma(close, 200)
    cross_up = (close.shift(1) <= s.shift(1)) & (close > s)
    bs = _bars_since_true(cross_up)
    return bs.where(close > s, np.nan)


def f50_tdco_247_age_current_downtrend_252(close: pd.Series) -> pd.Series:
    """Bars since the last cross below SMA200 — live age of current downtrend (NaN if currently above)."""
    s = _sma(close, 200)
    cross_dn = (close.shift(1) >= s.shift(1)) & (close < s)
    bs = _bars_since_true(cross_dn)
    return bs.where(close < s, np.nan)


def f50_tdco_248_age_above_50ma_continuous_252(close: pd.Series) -> pd.Series:
    """Consecutive bars where close >= SMA50 (live streak)."""
    s = _sma(close, 50)
    return _streak_true(close >= s).where(s.notna(), np.nan)


def f50_tdco_249_age_at_252_high_relative_to_history(high: pd.Series) -> pd.Series:
    """bars-since-252h / 252d-mean(bars-since-252h) — current peak age relative to typical."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    avg_bs = bs.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(bs, avg_bs)


def f50_tdco_250_cycle_completion_estimate_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cycle phase progress estimate: position of current close in (252d-min .. 252d-max .. current).
    Defined as: if making new 252d high, phase 1; if dropping from peak by <20%, phase 2;
    if 20-50% drawdown, phase 3; if >50%, phase 4. Returns phase as float."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    bs_peak = _bars_since_true(high == rmax)
    phase = pd.Series(np.nan, index=close.index)
    phase = phase.mask(bs_peak == 0, 1.0)
    phase = phase.mask((bs_peak > 0) & (dd < 0.20), 2.0)
    phase = phase.mask((dd >= 0.20) & (dd < 0.50), 3.0)
    phase = phase.mask(dd >= 0.50, 4.0)
    return phase


def f50_tdco_251_dominant_cycle_phase_indicator_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Uptrend/distribution/markdown/accumulation proxy from 63d slope of close and 63d top-dwell:
    1=uptrend (slope>0, dwell<0.3), 2=distribution (slope~0, dwell>0.3),
    3=markdown (slope<0, dd>20%), 4=accumulation (slope~0, dd<5% after deep dd)."""
    sl = _rolling_slope(close, QDAYS)
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    dwell = (high >= 0.99 * top).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    dd = _safe_div(top - close, top)
    sd_close = close.rolling(QDAYS, min_periods=MDAYS).std()
    sl_norm = _safe_div(sl * float(QDAYS), sd_close.replace(0, np.nan))
    phase = pd.Series(np.nan, index=close.index)
    phase = phase.mask((sl_norm > 1.0) & (dwell < 0.3), 1.0)
    phase = phase.mask((sl_norm.abs() <= 1.0) & (dwell > 0.3), 2.0)
    phase = phase.mask((sl_norm < -1.0) & (dd > 0.20), 3.0)
    phase = phase.mask((sl_norm.abs() <= 1.0) & (dd < 0.05), 4.0)
    return phase


def f50_tdco_252_dominant_cycle_period_proxy_252(close: pd.Series) -> pd.Series:
    """Autocorrelation peak period: rolling 252d window, find lag k in [10..63] with max autocorr of returns.
    Returns the lag (in bars) — proxy for dominant cycle period."""
    r = close.pct_change()
    def _peak_lag(w):
        valid = ~np.isnan(w)
        if valid.sum() < 100:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 100:
            return np.nan
        vm = v - v.mean()
        den = float((vm * vm).sum())
        if den == 0:
            return np.nan
        best_lag = np.nan
        best_acf = -np.inf
        for k in range(10, 64):
            if k >= v.size:
                break
            acf = float((vm[k:] * vm[:-k]).sum() / den)
            if acf > best_acf:
                best_acf = acf
                best_lag = float(k)
        return best_lag
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_peak_lag, raw=True)


def f50_tdco_253_cycle_age_to_period_ratio(high: pd.Series, close: pd.Series) -> pd.Series:
    """(bars-since-252d-high) / (dominant cycle period proxy). Higher = more cycle-end stress."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    r = close.pct_change()
    def _peak_lag(w):
        valid = ~np.isnan(w)
        if valid.sum() < 100:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 100:
            return np.nan
        vm = v - v.mean()
        den = float((vm * vm).sum())
        if den == 0:
            return np.nan
        best_lag = np.nan
        best_acf = -np.inf
        for k in range(10, 64):
            if k >= v.size:
                break
            acf = float((vm[k:] * vm[:-k]).sum() / den)
            if acf > best_acf:
                best_acf = acf
                best_lag = float(k)
        return best_lag
    period = r.rolling(YDAYS, min_periods=QDAYS).apply(_peak_lag, raw=True)
    return _safe_div(bs, period)


def f50_tdco_254_cycle_terminal_indicator_score(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cycle terminal indicator: sum of {phase>=3, dd>0.20, age>252, 63d-slope<0} (each binary)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    bs_peak = _bars_since_true(high == rmax)
    sl = _rolling_slope(close, QDAYS)
    phase = pd.Series(np.nan, index=close.index)
    phase = phase.mask(bs_peak == 0, 1.0)
    phase = phase.mask((bs_peak > 0) & (dd < 0.20), 2.0)
    phase = phase.mask((dd >= 0.20) & (dd < 0.50), 3.0)
    phase = phase.mask(dd >= 0.50, 4.0)
    score = ((phase >= 3.0).astype(float).fillna(0)
             + (dd > 0.20).astype(float).fillna(0)
             + (bs_peak > YDAYS).astype(float).fillna(0)
             + (sl < 0).astype(float).fillna(0))
    return score.where(rmax.notna() & sl.notna(), np.nan)


def f50_tdco_255_cycle_lead_lag_to_history_avg(high: pd.Series) -> pd.Series:
    """(current bars-since-252d-high) - (504d average bars-since-252d-high) — current cycle position vs typical.
    Positive = cycle has run longer than typical (late stage)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    avg = bs.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return bs - avg


# ============================================================
# Bucket S — Volume-price profile / range distribution (256-265)
# ============================================================

def f50_tdco_256_close_distribution_skew_252(close: pd.Series) -> pd.Series:
    """252d skew of close — asymmetry of price distribution."""
    return close.rolling(YDAYS, min_periods=QDAYS).skew()


def f50_tdco_257_close_distribution_kurtosis_252(close: pd.Series) -> pd.Series:
    """252d kurtosis of close — fat-tailed price clustering."""
    return close.rolling(YDAYS, min_periods=QDAYS).kurt()


def f50_tdco_258_volume_distribution_skew_252(volume: pd.Series) -> pd.Series:
    """252d skew of volume — high positive = concentrated volume spikes."""
    return volume.rolling(YDAYS, min_periods=QDAYS).skew()


def f50_tdco_259_close_at_high_concentration_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where close within 1% of 252d high — high-zone concentration."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (close >= 0.99 * rmax).astype(float)
    return near.rolling(YDAYS, min_periods=QDAYS).mean().where(rmax.notna(), np.nan)


def f50_tdco_260_volume_concentration_at_high_252(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 252d total volume that occurred while close within 1% of 252d high."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = close >= 0.99 * rmax
    v_near = volume.where(near, 0).rolling(YDAYS, min_periods=QDAYS).sum()
    v_tot = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(v_near, v_tot).where(rmax.notna(), np.nan)


def f50_tdco_261_mode_of_close_position_in_252_range_band(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mode band of (close - 252min)/(252max - 252min) bucketed into 10 bands over past 252 — most frequent band index (0..9)."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    def _mode_band(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        bands = np.clip((v * 10).astype(int), 0, 9)
        return float(np.argmax(np.bincount(bands, minlength=10)))
    return pos.rolling(YDAYS, min_periods=QDAYS).apply(_mode_band, raw=True)


def f50_tdco_262_close_position_dispersion_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of close-position-in-252-range over 252 — dispersion of price location."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    return pos.rolling(YDAYS, min_periods=QDAYS).std()


def f50_tdco_263_volume_to_atr_ratio_at_high_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(volume / ATR(21)) averaged over past 63 bars where close near 252d-high (>=95%). Else NaN."""
    atr = _atr(high, low, close, MDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = close >= 0.95 * rmax
    ratio = _safe_div(volume, atr).where(near, np.nan)
    return ratio.rolling(QDAYS, min_periods=MDAYS).mean()


def f50_tdco_264_high_volume_high_close_count_252(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of past 252 bars where both volume in top 10% AND close in top 10% of 252d range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    vq = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    ev = ((pos > 0.9) & (volume >= vq)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(vq.notna(), np.nan)


def f50_tdco_265_low_volume_high_close_count_252(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of past 252 bars where close in top 10% of 252d range AND volume in bottom 50% — bearish high-on-low-vol."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    vmed = volume.rolling(YDAYS, min_periods=QDAYS).median()
    ev = ((pos > 0.9) & (volume < vmed)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum().where(vmed.notna(), np.nan)


# ============================================================
# Bucket T — Cross-confirmation with momentum (266-275)
# ============================================================

def f50_tdco_266_ma_distance_pct_at_peak(high: pd.Series, close: pd.Series) -> pd.Series:
    """At bars where high == 252d max: average of (close/SMA50 - 1) and (close/SMA200 - 1). Else ffilled.
    Captures MA-distance regime at peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    at_peak = high >= rmax
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    avg = ((_safe_div(close, s50) - 1.0) + (_safe_div(close, s200) - 1.0)) / 2.0
    return avg.where(at_peak, np.nan).ffill()


def f50_tdco_267_ma_distance_decay_post_peak_63(high: pd.Series, close: pd.Series) -> pd.Series:
    """Post-peak: 63d slope of ((close/SMA50)+(close/SMA200))/2 - 1. Conditioned on post-peak. NaN otherwise."""
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    avg = ((_safe_div(close, s50) - 1.0) + (_safe_div(close, s200) - 1.0)) / 2.0
    sl = _rolling_slope(avg, QDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post = (bs > 0) & (bs <= YDAYS)
    return sl.where(post, np.nan)


def f50_tdco_268_ma_alignment_at_breakdown(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close just broke 21d-low AND all of SMA20/50/100/200 are declining (21d slope < 0). Else 0/NaN."""
    prior_ll = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    brk = close < prior_ll
    sl20 = _rolling_slope(_sma(close, 20), MDAYS)
    sl50 = _rolling_slope(_sma(close, 50), MDAYS)
    sl100 = _rolling_slope(_sma(close, 100), MDAYS)
    sl200 = _rolling_slope(_sma(close, 200), MDAYS)
    aligned = (sl20 < 0) & (sl50 < 0) & (sl100 < 0) & (sl200 < 0)
    ev = brk & aligned
    return ev.astype(float).where(prior_ll.notna() & sl200.notna(), np.nan)


def f50_tdco_269_ma_break_with_volume_count_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of past 252 bars with MA50 break-down AND volume > 1.3x prior 50d avg — confirmed MA breakdown."""
    s50 = _sma(close, 50)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    brk = (close.shift(1) >= s50.shift(1)) & (close < s50) & (volume > 1.3 * vavg)
    return brk.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(s50.notna() & vavg.notna(), np.nan)


def f50_tdco_270_ma_break_recovery_failure_count_252(close: pd.Series) -> pd.Series:
    """Count of past 252 where close briefly recovered above SMA50 then fell back: today close < SMA50 AND yesterday close >= SMA50
    AND day-before-yesterday close < SMA50 — recovery failure after MA break."""
    s50 = _sma(close, 50)
    today_below = close < s50
    yest_above = close.shift(1) >= s50.shift(1)
    dby_below = close.shift(2) < s50.shift(2)
    ev = today_below & yest_above & dby_below
    return ev.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(s50.notna(), np.nan)


def f50_tdco_271_ma_distance_zscore_post_peak_252(high: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (over 252d) of (close - SMA50)/SMA50 conditioned on post-peak. Negative = below typical MA-distance."""
    s50 = _sma(close, 50)
    dist = _safe_div(close - s50, s50)
    z = _rolling_zscore(dist, YDAYS, min_periods=QDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    bs = _bars_since_true(high == rmax)
    post = (bs > 0) & (bs <= YDAYS)
    return z.where(post, np.nan)


def f50_tdco_272_ma_consensus_bearish_indicator(close: pd.Series) -> pd.Series:
    """1 if ALL of {close < SMA20, close < SMA50, close < SMA100, close < SMA200} AND each MA has negative 21d slope.
    Consensus bearish state."""
    s20 = _sma(close, 20); s50 = _sma(close, 50); s100 = _sma(close, 100); s200 = _sma(close, 200)
    below = (close < s20) & (close < s50) & (close < s100) & (close < s200)
    sl20 = _rolling_slope(s20, MDAYS)
    sl50 = _rolling_slope(s50, MDAYS)
    sl100 = _rolling_slope(s100, MDAYS)
    sl200 = _rolling_slope(s200, MDAYS)
    declining = (sl20 < 0) & (sl50 < 0) & (sl100 < 0) & (sl200 < 0)
    return (below & declining).astype(float).where(s200.notna() & sl200.notna(), np.nan)


def f50_tdco_273_ma_persistence_below_count_252(close: pd.Series) -> pd.Series:
    """Count of past 252 bars where close < SMA200 — persistent-below-MA200 count."""
    s200 = _sma(close, 200)
    return (close < s200).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(s200.notna(), np.nan)


def f50_tdco_274_ma_violation_acceleration_63(close: pd.Series) -> pd.Series:
    """63d slope of (count-of-MAs-below): rising count = accelerating breakdown breadth."""
    s20 = _sma(close, 20); s50 = _sma(close, 50); s100 = _sma(close, 100); s200 = _sma(close, 200)
    cnt = ((close < s20).astype(float) + (close < s50).astype(float)
           + (close < s100).astype(float) + (close < s200).astype(float))
    return _rolling_slope(cnt, QDAYS).where(s200.notna(), np.nan)


def f50_tdco_275_ma_terminal_failure_score(close: pd.Series) -> pd.Series:
    """Composite: sum of {count-MAs-below >=3, MA-consensus bearish (all declining), MA50 break-with-vol count >=2 in 21,
    persistence below 200 > 30 days}."""
    s20 = _sma(close, 20); s50 = _sma(close, 50); s100 = _sma(close, 100); s200 = _sma(close, 200)
    cnt = ((close < s20).astype(float) + (close < s50).astype(float)
           + (close < s100).astype(float) + (close < s200).astype(float))
    sl20 = _rolling_slope(s20, MDAYS)
    sl50 = _rolling_slope(s50, MDAYS)
    sl100 = _rolling_slope(s100, MDAYS)
    sl200 = _rolling_slope(s200, MDAYS)
    bearish_consensus = ((close < s200) & (sl20 < 0) & (sl50 < 0) & (sl100 < 0) & (sl200 < 0))
    brk_50_recent = ((close.shift(1) >= s50.shift(1)) & (close < s50)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    persist = (close < s200).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    score = ((cnt >= 3.0).astype(float).fillna(0)
             + bearish_consensus.astype(float).fillna(0)
             + (brk_50_recent >= 2.0).astype(float).fillna(0)
             + (persist >= 15.0).astype(float).fillna(0))
    return score.where(s200.notna(), np.nan)


# ============================================================
# Bucket U — Cross-validation with prior history (276-285)
# ============================================================

def f50_tdco_276_has_been_at_2y_high_in_252d_state(high: pd.Series) -> pd.Series:
    """1 if any bar in past 252 saw high == 504d max — has touched 2y-high recently."""
    rmax_2y = high.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    at_2y_max = (high >= rmax_2y).astype(float)
    return (at_2y_max.rolling(YDAYS, min_periods=QDAYS).sum() > 0).astype(float).where(rmax_2y.notna(), np.nan)


def f50_tdco_277_first_time_252h_in_504d_indicator(high: pd.Series) -> pd.Series:
    """1 if today high == 252d max AND the prior 504d had NO 252d-max touch — extreme rare new high."""
    rmax_252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    today_new = (high >= rmax_252)
    prior_touched = today_new.shift(1).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    ev = today_new & (prior_touched == 0)
    return ev.astype(float).where(rmax_252.notna() & (prior_touched.notna()), np.nan)


def f50_tdco_278_historical_drawdown_max_252_vs_504(high: pd.Series, close: pd.Series) -> pd.Series:
    """(252d max-drawdown) / (504d max-drawdown) — recent dd severity vs 2y dd severity."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    dd_252 = dd.rolling(YDAYS, min_periods=QDAYS).max()
    dd_504 = dd.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return _safe_div(dd_252, dd_504)


def f50_tdco_279_historical_volatility_regime_change_504(close: pd.Series) -> pd.Series:
    """(63d std-of-returns) / (504d-mean of 63d std-of-returns) — current vol vs historical regime."""
    rv = close.pct_change().rolling(QDAYS, min_periods=MDAYS).std()
    avg = rv.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return _safe_div(rv, avg)


def f50_tdco_280_historical_distribution_intensity_avg_252_to_504_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(252d sum of distribution-intensity) / (504d avg of 252d-sum) — recent vs historical distribution intensity."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    vratio = _safe_div(volume, vavg)
    w = (ret.where(ret < 0, 0).abs() * vratio).where(vavg.notna(), np.nan)
    cur = w.rolling(YDAYS, min_periods=QDAYS).sum()
    hist = cur.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return _safe_div(cur, hist)


def f50_tdco_281_first_break_below_252_low_in_504d_indicator(low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if today close < prior 252d low AND prior 504d had no such break — first major-low break in 2y."""
    prev_ll252 = low.shift(1).rolling(YDAYS, min_periods=QDAYS).min()
    brk_today = (close < prev_ll252)
    prior_brk = brk_today.shift(1).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    ev = brk_today & (prior_brk == 0)
    return ev.astype(float).where(prev_ll252.notna() & prior_brk.notna(), np.nan)


def f50_tdco_282_historical_recovery_failure_rate_504(high: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative recovery-failure rate over past 504 bars — long-horizon failure rate of bounces."""
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h21)
    return _safe_div(failed.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum(),
                     bounce.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum())


def f50_tdco_283_historical_late_cycle_indicator_504(low: pd.Series) -> pd.Series:
    """504d-relative cycle age: (bars-since-504d-low) / 504 — long-horizon cycle position."""
    rmin = low.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    bs = _bars_since_true(low == rmin)
    return bs / float(DDAYS_2Y)


def f50_tdco_284_historical_terminal_pattern_avg_score_504(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """504d average of pre-breakdown topping-score-style binary (distribution+lower-high+drawdown) — historical norm of pattern strength."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = (h5 < h5.shift(WDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    s = ((dd_count >= 3.0).astype(float).fillna(0)
         + (lh >= 3.0).astype(float).fillna(0)
         + (dd > 0.10).astype(float).fillna(0))
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f50_tdco_285_historical_pattern_acceleration_504(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(63d-avg pattern-score) - (504d-avg pattern-score) — pattern acceleration vs long history."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = (h5 < h5.shift(WDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    s = ((dd_count >= 3.0).astype(float).fillna(0)
         + (lh >= 3.0).astype(float).fillna(0)
         + (dd > 0.10).astype(float).fillna(0))
    return s.rolling(QDAYS, min_periods=MDAYS).mean() - s.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


# ============================================================
# Bucket V — Aggregate terminal-distribution composites v2 (286-300)
# ============================================================

def f50_tdco_286_extended_terminal_distribution_master_score_v2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master v2 = sum of {dd_count>=5, lower-high count >=10, drawdown >0.10, close<SMA50, close<SMA200,
    drawdown-skew<0, cycle phase>=3, drawdown duration >30 days, recovery failure rate>0.5}."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = (h5 < h5.shift(WDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    dd_skew = dd.rolling(YDAYS, min_periods=QDAYS).skew()
    bs_peak = _bars_since_true(high == rmax)
    phase = pd.Series(np.nan, index=close.index)
    phase = phase.mask(bs_peak == 0, 1.0)
    phase = phase.mask((bs_peak > 0) & (dd < 0.20), 2.0)
    phase = phase.mask((dd >= 0.20) & (dd < 0.50), 3.0)
    phase = phase.mask(dd >= 0.50, 4.0)
    dur = _streak_true(dd > 0.05)
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h21)
    fr = _safe_div(failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum(),
                   bounce.astype(float).rolling(QDAYS, min_periods=MDAYS).sum())
    score = ((dd_count >= 5.0).astype(float).fillna(0)
             + (lh >= 10.0).astype(float).fillna(0)
             + (dd > 0.10).astype(float).fillna(0)
             + (close < s50).astype(float).fillna(0)
             + (close < s200).astype(float).fillna(0)
             + (dd_skew < 0).astype(float).fillna(0)
             + (phase >= 3.0).astype(float).fillna(0)
             + (dur > 30.0).astype(float).fillna(0)
             + (fr > 0.5).astype(float).fillna(0))
    return score.where(s200.notna() & vavg.notna(), np.nan)


def f50_tdco_287_extended_stuck_probability_proxy_v2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Extended stuck proxy: drawdown × time-underwater(>20%) × (504d-max-dd / 252d-max-dd)
    — depth × duration × historical extremes."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    tu = (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    dd_252 = dd.rolling(YDAYS, min_periods=QDAYS).max()
    dd_504 = dd.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    hist_ratio = _safe_div(dd_504, dd_252)
    return (dd * tu * hist_ratio).where(rmax.notna(), np.nan)


def f50_tdco_288_extended_composite_breakdown_severity_v2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Extends 148: count of distinct breakdown events {21d-low, 63d-low, 252d-low, SMA50, SMA200, death-cross,
    high-vol-break, MA-recovery-failure} in past 252."""
    prev_ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    prev_ll63 = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    prev_ll252 = low.shift(1).rolling(YDAYS, min_periods=QDAYS).min()
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    e1 = (close < prev_ll21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e2 = (close < prev_ll63).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e3 = (close < prev_ll252).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e4 = ((close.shift(1) >= s50.shift(1)) & (close < s50)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e5 = ((close.shift(1) >= s200.shift(1)) & (close < s200)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    d = s50 - s200
    e6 = ((d.shift(1) >= 0) & (d < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e7 = ((close < prev_ll63) & (volume > 1.5 * vavg)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    e8 = ((close < s50) & (close.shift(1) >= s50.shift(1)) & (close.shift(2) < s50.shift(2))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = (e1.fillna(0) + e2.fillna(0) + e3.fillna(0) + e4.fillna(0)
           + e5.fillna(0) + e6.fillna(0) + e7.fillna(0) + e8.fillna(0))
    return tot.where(s200.notna() & vavg.notna(), np.nan)


def f50_tdco_289_extended_multi_signal_topping_aggregate_v2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At bars near 252d high: sum of {distribution-at-top, lower-high streak >=3, dwell>0.5, candle cluster >=2,
    upthrust, climactic action, blow-off proxy > 2}. Else NaN."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.95 * rmax)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dist_at_top = ((ret < -0.002) & (volume > vavg) & near).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh_streak = _streak_true(h5 < h5.shift(WDAYS))
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - ll, hh - ll)
    dwell = (pos > 0.9).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    rng = (high - low).replace(0, np.nan)
    body = (close - open).abs()
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    lower = pd.concat([close, open], axis=1).min(axis=1) - low
    ss = (upper >= 2.0 * body) & (body <= 0.3 * rng) & (lower < 0.2 * rng)
    gd = (body <= 0.10 * rng) & (lower <= 0.10 * rng) & (upper >= 0.6 * rng)
    candle_cluster = (ss.astype(float).fillna(0) + gd.astype(float).fillna(0)).rolling(MDAYS, min_periods=WDAYS).sum()
    prior_h = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    mid = (high + low) / 2.0
    upthrust = ((high > prior_h) & (close < open) & (close < mid)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    atr = _atr(high, low, close, MDAYS)
    climax = ((rng > 2.0 * atr) & (volume > 2.0 * vavg) & (high >= rmax)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    r21 = close.pct_change(MDAYS)
    atr_pct = _safe_div(atr, close)
    blow_off = (_safe_div(r21, atr_pct) > 2.0).astype(float)
    score = ((dist_at_top >= 3.0).astype(float).fillna(0)
             + (lh_streak >= 3.0).astype(float).fillna(0)
             + (dwell > 0.5).astype(float).fillna(0)
             + (candle_cluster >= 2.0).astype(float).fillna(0)
             + (upthrust >= 1.0).astype(float).fillna(0)
             + (climax >= 1.0).astype(float).fillna(0)
             + blow_off.fillna(0))
    return score.where(near, np.nan)


def f50_tdco_290_extended_pre_breakdown_topping_score_v2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At bars within 21 bars of a 63d-low break: sum of {top-dwell>0.3, lower-high count>=3, dd_count>=3,
    drawdown_q>0.05, MA20 break-recent, recovery-failure rate>0.5}."""
    top = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high >= 0.99 * top).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = (h5 < h5.shift(WDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    rmax_q = high.rolling(QDAYS, min_periods=MDAYS).max()
    dd_q = _safe_div(rmax_q - close, rmax_q)
    s20 = _sma(close, 20)
    ma_brk = ((close.shift(1) >= s20.shift(1)) & (close < s20)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h21)
    fr = _safe_div(failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum(),
                   bounce.astype(float).rolling(QDAYS, min_periods=MDAYS).sum())
    score = ((near > 0.3).astype(float).fillna(0)
             + (lh >= 3.0).astype(float).fillna(0)
             + (dd_count >= 3.0).astype(float).fillna(0)
             + (dd_q > 0.05).astype(float).fillna(0)
             + (ma_brk >= 1.0).astype(float).fillna(0)
             + (fr > 0.5).astype(float).fillna(0))
    prev_ll = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    brk_recent = (close < prev_ll).astype(float).rolling(MDAYS, min_periods=1).sum() > 0
    return score.where(brk_recent, np.nan)


def f50_tdco_291_modern_indicator_basket_score(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of indicator counts in past 21: Wyckoff (upthrust+no-demand+stopping-vol) + candle (shooting-star+gravestone+bear-engulf)
    + multi-bar (double-top+three-drives) — count basket."""
    prior_h = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    mid = (high + low) / 2.0
    upthrust = ((high > prior_h) & (close < open) & (close < mid)).astype(float)
    atr = _atr(high, low, close, MDAYS)
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    rng = (high - low).replace(0, np.nan)
    no_demand = ((close > close.shift(1)) & ((high - low) < 0.5 * atr) & (volume < vavg)).astype(float)
    pos = _safe_div(close - low, rng)
    stopping_vol = ((volume > 2.0 * vavg) & (close < close.shift(1)) & (pos < 0.25)).astype(float)
    body = (close - open).abs()
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    lower = pd.concat([close, open], axis=1).min(axis=1) - low
    ss = ((upper >= 2.0 * body) & (body <= 0.3 * rng) & (lower < 0.2 * rng)).astype(float)
    gd = ((body <= 0.10 * rng) & (lower <= 0.10 * rng) & (upper >= 0.6 * rng)).astype(float)
    be = ((close < open) & (close.shift(1) > open.shift(1)) & (open > close.shift(1)) & (close < open.shift(1))).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    h_rec = high.rolling(32, min_periods=10).max()
    h_pr = high.shift(32).rolling(32, min_periods=10).max()
    dt = ((_safe_div(pd.concat([h_rec, h_pr], axis=1).min(axis=1), pd.concat([h_rec, h_pr], axis=1).max(axis=1)) >= 0.99)
          & (pd.concat([h_rec, h_pr], axis=1).max(axis=1) >= 0.90 * rmax)).astype(float)
    h_now = high.rolling(WDAYS, min_periods=2).max()
    three_drives = ((h_now > h_now.shift(21)) & (h_now.shift(21) > h_now.shift(42))
                    & ((h_now - h_now.shift(21)) < (h_now.shift(21) - h_now.shift(42)))).astype(float)
    tot = (upthrust + no_demand + stopping_vol + ss + gd + be + dt + three_drives).rolling(MDAYS, min_periods=WDAYS).sum()
    return tot.where(rmax.notna() & vavg.notna() & atr.notna(), np.nan)


def f50_tdco_292_cross_oscillator_distribution_consensus(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-vs-price proxy consensus: 1 if (down-volume dominance over 21d > 0.6) AND (down-day count in 25 >= 12)
    AND (21d return < -3%) — multi-axis distribution consensus."""
    diff = close.diff()
    dv = volume.where(diff < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    tv = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    dv_frac = _safe_div(dv, tv)
    down_cnt = (diff < 0).astype(float).rolling(25, min_periods=10).sum()
    r21 = close.pct_change(MDAYS)
    ev = (dv_frac > 0.6) & (down_cnt >= 12.0) & (r21 < -0.03)
    return ev.astype(float).where(r21.notna(), np.nan)


def f50_tdco_293_final_terminal_distribution_aggregate_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Aggregate score: master_v2 + breakdown_severity normalized + stuck_proxy normalized — combined signal."""
    # master v2 (simplified inline)
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    master = ((dd_count >= 5.0).astype(float).fillna(0)
              + (dd > 0.10).astype(float).fillna(0)
              + (close < s50).astype(float).fillna(0)
              + (close < s200).astype(float).fillna(0))
    # breakdown severity normalized to [0,1] by /10
    prev_ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    e1 = (close < prev_ll21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    sev = (e1 / 10.0).clip(upper=1.0)
    # stuck proxy
    tu = (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    stuck = (dd * tu).fillna(0)
    return (master + sev + stuck).where(s200.notna() & vavg.notna(), np.nan)


def f50_tdco_294_pattern_universe_breadth_indicator_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of past 252 bars where any of {dist-day, lower-high, MA50-break, drawdown>10%, candle-bear} fired —
    breadth of distribution-pattern activity."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_day = ((ret < -0.002) & (volume > vavg))
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = (h5 < h5.shift(WDAYS))
    s50 = _sma(close, 50)
    ma_brk = (close.shift(1) >= s50.shift(1)) & (close < s50)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd_big = (_safe_div(rmax - close, rmax) > 0.10)
    body = (close.diff().abs())  # crude proxy
    bear_cand = (close < close.shift(1)) & (body > body.rolling(MDAYS, min_periods=WDAYS).mean())
    any_pattern = (dd_day | lh | ma_brk | dd_big | bear_cand).astype(float)
    return any_pattern.rolling(YDAYS, min_periods=QDAYS).sum().where(vavg.notna(), np.nan)


def f50_tdco_295_pattern_universe_persistence_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Persistence: max consecutive run of pattern-active bars in past 252."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_day = ((ret < -0.002) & (volume > vavg))
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = (h5 < h5.shift(WDAYS))
    s50 = _sma(close, 50)
    ma_brk = (close.shift(1) >= s50.shift(1)) & (close < s50)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd_big = (_safe_div(rmax - close, rmax) > 0.10)
    any_pattern = (dd_day | lh | ma_brk | dd_big)
    streak = _streak_true(any_pattern)
    return streak.rolling(YDAYS, min_periods=QDAYS).max().where(vavg.notna(), np.nan)


def f50_tdco_296_pattern_universe_decay_velocity_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of pattern-breadth (sum of dist-day + lh + ma-brk + dd-big indicators per bar) — rising = decay/intensifying."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_day = ((ret < -0.002) & (volume > vavg)).astype(float)
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = (h5 < h5.shift(WDAYS)).astype(float)
    s50 = _sma(close, 50)
    ma_brk = ((close.shift(1) >= s50.shift(1)) & (close < s50)).astype(float)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd_big = (_safe_div(rmax - close, rmax) > 0.10).astype(float)
    breadth = dd_day.fillna(0) + lh.fillna(0) + ma_brk.fillna(0) + dd_big.fillna(0)
    return _rolling_slope(breadth, QDAYS)


def f50_tdco_297_final_stuck_score_with_normalization_v2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Final stuck score: (drawdown × time-underwater >20%) / (252d realized vol of returns × 504d-mean-drawdown).
    Normalized depth × duration / (vol × historical-norm)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    tu = (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    rv = close.pct_change().rolling(YDAYS, min_periods=QDAYS).std()
    dd_mean_504 = dd.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return _safe_div(dd * tu, rv * dd_mean_504)


def f50_tdco_298_universe_late_cycle_consensus_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if ALL of {cycle phase>=3, age-at-252h > 252, 252d-dd-max > 0.30, close < SMA200, 504d-cycle-age > 0.5} hold."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    bs_peak = _bars_since_true(high == rmax)
    phase = pd.Series(np.nan, index=close.index)
    phase = phase.mask(bs_peak == 0, 1.0)
    phase = phase.mask((bs_peak > 0) & (dd < 0.20), 2.0)
    phase = phase.mask((dd >= 0.20) & (dd < 0.50), 3.0)
    phase = phase.mask(dd >= 0.50, 4.0)
    age_p = bs_peak > YDAYS
    dd_max = dd.rolling(YDAYS, min_periods=QDAYS).max() > 0.30
    s200 = _sma(close, 200)
    below_200 = close < s200
    rmin_2y = low.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    bs_min = _bars_since_true(low == rmin_2y)
    cycle_age = (bs_min / float(DDAYS_2Y)) > 0.5
    ev = (phase >= 3.0) & age_p & dd_max & below_200 & cycle_age
    return ev.astype(float).where(s200.notna() & rmin_2y.notna(), np.nan)


def f50_tdco_299_absolute_terminal_pattern_indicator(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary high-confidence stuck signal: 1 if ALL of {drawdown>0.30, time-underwater>0.5, close<SMA200,
    breakdown count >= 5 in 252, recovery-failure rate > 0.7}."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    tu = (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    s200 = _sma(close, 200)
    prev_ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    brk_cnt = (close < prev_ll21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    h21 = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    bounce = close.pct_change(WDAYS) > 0.05
    failed = bounce & (high < h21)
    fr = _safe_div(failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum(),
                   bounce.astype(float).rolling(QDAYS, min_periods=MDAYS).sum())
    ev = (dd > 0.30) & (tu > 0.5) & (close < s200) & (brk_cnt >= 5.0) & (fr > 0.7)
    return ev.astype(float).where(s200.notna() & rmax.notna(), np.nan)


def f50_tdco_300_master_extended_composite_score(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master extended composite: sum of {master-v2 components} + {pattern breadth in 252 >=50} + {stuck-proxy normalized > median}
    + {breakdown severity > 10} + {cycle-terminal score >=3}. Returns final aggregate composite (0..many)."""
    ret = close.pct_change()
    vavg = volume.shift(1).rolling(50, min_periods=10).mean()
    dd_count = ((ret < -0.002) & (volume > vavg)).astype(float).rolling(25, min_periods=10).sum()
    h5 = high.rolling(WDAYS, min_periods=2).max()
    lh = (h5 < h5.shift(WDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(rmax - close, rmax)
    s50 = _sma(close, 50); s200 = _sma(close, 200)
    master = ((dd_count >= 5.0).astype(float).fillna(0)
              + (lh >= 10.0).astype(float).fillna(0)
              + (dd > 0.10).astype(float).fillna(0)
              + (close < s50).astype(float).fillna(0)
              + (close < s200).astype(float).fillna(0))
    # pattern breadth
    dd_day = ((ret < -0.002) & (volume > vavg)).astype(float)
    lh_b = (h5 < h5.shift(WDAYS)).astype(float)
    ma_brk = ((close.shift(1) >= s50.shift(1)) & (close < s50)).astype(float)
    dd_big = (dd > 0.10).astype(float)
    any_p = (dd_day.fillna(0) + lh_b.fillna(0) + ma_brk.fillna(0) + dd_big.fillna(0))
    breadth = any_p.rolling(YDAYS, min_periods=QDAYS).sum()
    breadth_term = (breadth >= 50.0).astype(float).fillna(0)
    # stuck proxy > rolling median
    tu = (dd > 0.20).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    stuck = (dd * tu)
    stuck_med = stuck.rolling(YDAYS, min_periods=QDAYS).median()
    stuck_term = (stuck > stuck_med).astype(float).fillna(0)
    # breakdown severity > 10
    prev_ll21 = low.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    sev = (close < prev_ll21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    sev_term = (sev > 10.0).astype(float).fillna(0)
    # cycle terminal score >=3
    bs_peak = _bars_since_true(high == rmax)
    phase = pd.Series(np.nan, index=close.index)
    phase = phase.mask(bs_peak == 0, 1.0)
    phase = phase.mask((bs_peak > 0) & (dd < 0.20), 2.0)
    phase = phase.mask((dd >= 0.20) & (dd < 0.50), 3.0)
    phase = phase.mask(dd >= 0.50, 4.0)
    sl = _rolling_slope(close, QDAYS)
    cycle_term = ((phase >= 3.0).astype(float).fillna(0)
                  + (dd > 0.20).astype(float).fillna(0)
                  + (bs_peak > YDAYS).astype(float).fillna(0)
                  + (sl < 0).astype(float).fillna(0))
    cycle_pass = (cycle_term >= 3.0).astype(float).fillna(0)
    return (master + breadth_term + stuck_term + sev_term + cycle_pass).where(s200.notna() & vavg.notna(), np.nan)


# ============================================================
#                         REGISTRY 226-300
# ============================================================

TERMINAL_DISTRIBUTION_COMPOSITE_BASE_REGISTRY_226_300 = {
    "f50_tdco_226_max_drawdown_252": {"inputs": ["high", "close"], "func": f50_tdco_226_max_drawdown_252},
    "f50_tdco_227_drawdown_skew_252": {"inputs": ["high", "close"], "func": f50_tdco_227_drawdown_skew_252},
    "f50_tdco_228_drawdown_kurtosis_252": {"inputs": ["high", "close"], "func": f50_tdco_228_drawdown_kurtosis_252},
    "f50_tdco_229_drawdown_autocorrelation_lag1_63": {"inputs": ["high", "close"], "func": f50_tdco_229_drawdown_autocorrelation_lag1_63},
    "f50_tdco_230_drawdown_pareto_alpha_proxy_252": {"inputs": ["high", "close"], "func": f50_tdco_230_drawdown_pareto_alpha_proxy_252},
    "f50_tdco_231_drawdown_avg_duration_252": {"inputs": ["high", "close"], "func": f50_tdco_231_drawdown_avg_duration_252},
    "f50_tdco_232_drawdown_max_duration_252": {"inputs": ["high", "close"], "func": f50_tdco_232_drawdown_max_duration_252},
    "f50_tdco_233_underwater_curve_area_252": {"inputs": ["high", "close"], "func": f50_tdco_233_underwater_curve_area_252},
    "f50_tdco_234_drawdown_to_atr_ratio_63": {"inputs": ["high", "low", "close"], "func": f50_tdco_234_drawdown_to_atr_ratio_63},
    "f50_tdco_235_drawdown_velocity_skew_63": {"inputs": ["high", "close"], "func": f50_tdco_235_drawdown_velocity_skew_63},
    "f50_tdco_236_recovery_attempt_amplitude_decay_63": {"inputs": ["close"], "func": f50_tdco_236_recovery_attempt_amplitude_decay_63},
    "f50_tdco_237_recovery_time_to_amplitude_ratio_63": {"inputs": ["close"], "func": f50_tdco_237_recovery_time_to_amplitude_ratio_63},
    "f50_tdco_238_expected_recovery_failure_probability_proxy_63": {"inputs": ["high", "close"], "func": f50_tdco_238_expected_recovery_failure_probability_proxy_63},
    "f50_tdco_239_partial_recovery_failure_count_63": {"inputs": ["high", "close"], "func": f50_tdco_239_partial_recovery_failure_count_63},
    "f50_tdco_240_fully_failed_recovery_count_63": {"inputs": ["high", "close"], "func": f50_tdco_240_fully_failed_recovery_count_63},
    "f50_tdco_241_mean_recovery_attempt_size_63": {"inputs": ["close"], "func": f50_tdco_241_mean_recovery_attempt_size_63},
    "f50_tdco_242_max_recovery_attempt_size_63": {"inputs": ["close"], "func": f50_tdco_242_max_recovery_attempt_size_63},
    "f50_tdco_243_recovery_amplitude_zscore_252": {"inputs": ["close"], "func": f50_tdco_243_recovery_amplitude_zscore_252},
    "f50_tdco_244_recovery_consistency_score_63": {"inputs": ["close"], "func": f50_tdco_244_recovery_consistency_score_63},
    "f50_tdco_245_recovery_streak_failure_breakdown_indicator": {"inputs": ["low", "close"], "func": f50_tdco_245_recovery_streak_failure_breakdown_indicator},
    "f50_tdco_246_age_current_uptrend_252": {"inputs": ["close"], "func": f50_tdco_246_age_current_uptrend_252},
    "f50_tdco_247_age_current_downtrend_252": {"inputs": ["close"], "func": f50_tdco_247_age_current_downtrend_252},
    "f50_tdco_248_age_above_50ma_continuous_252": {"inputs": ["close"], "func": f50_tdco_248_age_above_50ma_continuous_252},
    "f50_tdco_249_age_at_252_high_relative_to_history": {"inputs": ["high"], "func": f50_tdco_249_age_at_252_high_relative_to_history},
    "f50_tdco_250_cycle_completion_estimate_252": {"inputs": ["high", "low", "close"], "func": f50_tdco_250_cycle_completion_estimate_252},
    "f50_tdco_251_dominant_cycle_phase_indicator_63": {"inputs": ["high", "close"], "func": f50_tdco_251_dominant_cycle_phase_indicator_63},
    "f50_tdco_252_dominant_cycle_period_proxy_252": {"inputs": ["close"], "func": f50_tdco_252_dominant_cycle_period_proxy_252},
    "f50_tdco_253_cycle_age_to_period_ratio": {"inputs": ["high", "close"], "func": f50_tdco_253_cycle_age_to_period_ratio},
    "f50_tdco_254_cycle_terminal_indicator_score": {"inputs": ["high", "low", "close"], "func": f50_tdco_254_cycle_terminal_indicator_score},
    "f50_tdco_255_cycle_lead_lag_to_history_avg": {"inputs": ["high"], "func": f50_tdco_255_cycle_lead_lag_to_history_avg},
    "f50_tdco_256_close_distribution_skew_252": {"inputs": ["close"], "func": f50_tdco_256_close_distribution_skew_252},
    "f50_tdco_257_close_distribution_kurtosis_252": {"inputs": ["close"], "func": f50_tdco_257_close_distribution_kurtosis_252},
    "f50_tdco_258_volume_distribution_skew_252": {"inputs": ["volume"], "func": f50_tdco_258_volume_distribution_skew_252},
    "f50_tdco_259_close_at_high_concentration_252": {"inputs": ["high", "close"], "func": f50_tdco_259_close_at_high_concentration_252},
    "f50_tdco_260_volume_concentration_at_high_252": {"inputs": ["high", "close", "volume"], "func": f50_tdco_260_volume_concentration_at_high_252},
    "f50_tdco_261_mode_of_close_position_in_252_range_band": {"inputs": ["high", "low", "close"], "func": f50_tdco_261_mode_of_close_position_in_252_range_band},
    "f50_tdco_262_close_position_dispersion_252": {"inputs": ["high", "low", "close"], "func": f50_tdco_262_close_position_dispersion_252},
    "f50_tdco_263_volume_to_atr_ratio_at_high_63": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_263_volume_to_atr_ratio_at_high_63},
    "f50_tdco_264_high_volume_high_close_count_252": {"inputs": ["high", "close", "volume"], "func": f50_tdco_264_high_volume_high_close_count_252},
    "f50_tdco_265_low_volume_high_close_count_252": {"inputs": ["high", "close", "volume"], "func": f50_tdco_265_low_volume_high_close_count_252},
    "f50_tdco_266_ma_distance_pct_at_peak": {"inputs": ["high", "close"], "func": f50_tdco_266_ma_distance_pct_at_peak},
    "f50_tdco_267_ma_distance_decay_post_peak_63": {"inputs": ["high", "close"], "func": f50_tdco_267_ma_distance_decay_post_peak_63},
    "f50_tdco_268_ma_alignment_at_breakdown": {"inputs": ["low", "close"], "func": f50_tdco_268_ma_alignment_at_breakdown},
    "f50_tdco_269_ma_break_with_volume_count_252": {"inputs": ["close", "volume"], "func": f50_tdco_269_ma_break_with_volume_count_252},
    "f50_tdco_270_ma_break_recovery_failure_count_252": {"inputs": ["close"], "func": f50_tdco_270_ma_break_recovery_failure_count_252},
    "f50_tdco_271_ma_distance_zscore_post_peak_252": {"inputs": ["high", "close"], "func": f50_tdco_271_ma_distance_zscore_post_peak_252},
    "f50_tdco_272_ma_consensus_bearish_indicator": {"inputs": ["close"], "func": f50_tdco_272_ma_consensus_bearish_indicator},
    "f50_tdco_273_ma_persistence_below_count_252": {"inputs": ["close"], "func": f50_tdco_273_ma_persistence_below_count_252},
    "f50_tdco_274_ma_violation_acceleration_63": {"inputs": ["close"], "func": f50_tdco_274_ma_violation_acceleration_63},
    "f50_tdco_275_ma_terminal_failure_score": {"inputs": ["close"], "func": f50_tdco_275_ma_terminal_failure_score},
    "f50_tdco_276_has_been_at_2y_high_in_252d_state": {"inputs": ["high"], "func": f50_tdco_276_has_been_at_2y_high_in_252d_state},
    "f50_tdco_277_first_time_252h_in_504d_indicator": {"inputs": ["high"], "func": f50_tdco_277_first_time_252h_in_504d_indicator},
    "f50_tdco_278_historical_drawdown_max_252_vs_504": {"inputs": ["high", "close"], "func": f50_tdco_278_historical_drawdown_max_252_vs_504},
    "f50_tdco_279_historical_volatility_regime_change_504": {"inputs": ["close"], "func": f50_tdco_279_historical_volatility_regime_change_504},
    "f50_tdco_280_historical_distribution_intensity_avg_252_to_504_ratio": {"inputs": ["close", "volume"], "func": f50_tdco_280_historical_distribution_intensity_avg_252_to_504_ratio},
    "f50_tdco_281_first_break_below_252_low_in_504d_indicator": {"inputs": ["low", "close"], "func": f50_tdco_281_first_break_below_252_low_in_504d_indicator},
    "f50_tdco_282_historical_recovery_failure_rate_504": {"inputs": ["high", "close"], "func": f50_tdco_282_historical_recovery_failure_rate_504},
    "f50_tdco_283_historical_late_cycle_indicator_504": {"inputs": ["low"], "func": f50_tdco_283_historical_late_cycle_indicator_504},
    "f50_tdco_284_historical_terminal_pattern_avg_score_504": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_284_historical_terminal_pattern_avg_score_504},
    "f50_tdco_285_historical_pattern_acceleration_504": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_285_historical_pattern_acceleration_504},
    "f50_tdco_286_extended_terminal_distribution_master_score_v2": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_286_extended_terminal_distribution_master_score_v2},
    "f50_tdco_287_extended_stuck_probability_proxy_v2": {"inputs": ["high", "close"], "func": f50_tdco_287_extended_stuck_probability_proxy_v2},
    "f50_tdco_288_extended_composite_breakdown_severity_v2": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_288_extended_composite_breakdown_severity_v2},
    "f50_tdco_289_extended_multi_signal_topping_aggregate_v2": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_289_extended_multi_signal_topping_aggregate_v2},
    "f50_tdco_290_extended_pre_breakdown_topping_score_v2": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_290_extended_pre_breakdown_topping_score_v2},
    "f50_tdco_291_modern_indicator_basket_score": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_291_modern_indicator_basket_score},
    "f50_tdco_292_cross_oscillator_distribution_consensus": {"inputs": ["close", "volume"], "func": f50_tdco_292_cross_oscillator_distribution_consensus},
    "f50_tdco_293_final_terminal_distribution_aggregate_score": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_293_final_terminal_distribution_aggregate_score},
    "f50_tdco_294_pattern_universe_breadth_indicator_252": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_294_pattern_universe_breadth_indicator_252},
    "f50_tdco_295_pattern_universe_persistence_252": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_295_pattern_universe_persistence_252},
    "f50_tdco_296_pattern_universe_decay_velocity_63": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_296_pattern_universe_decay_velocity_63},
    "f50_tdco_297_final_stuck_score_with_normalization_v2": {"inputs": ["high", "close"], "func": f50_tdco_297_final_stuck_score_with_normalization_v2},
    "f50_tdco_298_universe_late_cycle_consensus_indicator": {"inputs": ["high", "low", "close"], "func": f50_tdco_298_universe_late_cycle_consensus_indicator},
    "f50_tdco_299_absolute_terminal_pattern_indicator": {"inputs": ["high", "low", "close", "volume"], "func": f50_tdco_299_absolute_terminal_pattern_indicator},
    "f50_tdco_300_master_extended_composite_score": {"inputs": ["open", "high", "low", "close", "volume"], "func": f50_tdco_300_master_extended_composite_score},
}
