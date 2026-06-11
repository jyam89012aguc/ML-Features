"""roc_momentum_family base features 301-375 — Pipeline 1b-technical (batch 3).

Third pass, atomic-leaning blowoff/distribution/exhaustion signals.

Buckets in this file:
R (best/worst-N-day extremes in trailing windows), 301-320;
S (bars-since extreme-event), 321-340;
T (single-bar event indicators), 341-355;
U continued (open/close intraday & gap atomic), 356-375.

Inputs: SEP OHLCV (open, high, low, close, volume). PIT-clean: right-anchored
rolling, explicit min_periods, no centered windows, no .shift(N). Self-contained
helpers — no cross-family imports. Atomic-leaning: each function = one single-source
signal the ML can weight independently.
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

def _bars_since_event(flag: pd.Series, window: int, min_periods: int) -> pd.Series:
    """Bars-since the most recent True/1 in flag, within trailing `window`.
    Returns window if no event present in the window."""

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        idxs = np.where(w == 1)[0]
        if len(idxs) == 0:
            return float(len(w))
        return float(len(w) - 1 - idxs[-1])
    return flag.astype(float).rolling(window, min_periods=min_periods).apply(_bs, raw=True)

def f31_rcmf_301_best_1d_return_252d_d3(close: pd.Series) -> pd.Series:
    """Best (max) single-day return over trailing 252d — magnitude of strongest
    single up-day in last year. Atomic blowoff-fingerprint level."""
    r = close.pct_change(1)
    return r.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f31_rcmf_302_best_1d_return_504d_d3(close: pd.Series) -> pd.Series:
    """Best single-day return over trailing 504d (2y) — single biggest up-day in 2y."""
    r = close.pct_change(1)
    return r.rolling(DDAYS_2Y, min_periods=YDAYS).max().diff().diff().diff()

def f31_rcmf_303_best_1d_return_1260d_d3(close: pd.Series) -> pd.Series:
    """Best single-day return over trailing 1260d (5y) — strongest single-day rally in 5y."""
    r = close.pct_change(1)
    return r.rolling(DDAYS_5Y, min_periods=YDAYS).max().diff().diff().diff()

def f31_rcmf_304_worst_1d_return_252d_d3(close: pd.Series) -> pd.Series:
    """Worst (min) single-day return over trailing 252d — deepest single down-day in last year."""
    r = close.pct_change(1)
    return r.rolling(YDAYS, min_periods=QDAYS).min().diff().diff().diff()

def f31_rcmf_305_worst_1d_return_1260d_d3(close: pd.Series) -> pd.Series:
    """Worst single-day return over trailing 1260d — deepest single down-day in 5y."""
    r = close.pct_change(1)
    return r.rolling(DDAYS_5Y, min_periods=YDAYS).min().diff().diff().diff()

def f31_rcmf_306_best_3d_return_252d_d3(close: pd.Series) -> pd.Series:
    """Best trailing 3d return observed within trailing 252d — short-burst maximum."""
    r3 = close.pct_change(3)
    return r3.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f31_rcmf_307_best_5d_return_252d_d3(close: pd.Series) -> pd.Series:
    """Best trailing 5d return observed within trailing 252d."""
    r5 = close.pct_change(WDAYS)
    return r5.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f31_rcmf_308_best_5d_return_1260d_d3(close: pd.Series) -> pd.Series:
    """Best trailing 5d return observed within trailing 1260d — 5y strongest weekly burst."""
    r5 = close.pct_change(WDAYS)
    return r5.rolling(DDAYS_5Y, min_periods=YDAYS).max().diff().diff().diff()

def f31_rcmf_309_best_10d_return_252d_d3(close: pd.Series) -> pd.Series:
    """Best trailing 10d return observed within trailing 252d."""
    r10 = close.pct_change(10)
    return r10.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f31_rcmf_310_best_21d_return_504d_d3(close: pd.Series) -> pd.Series:
    """Best trailing 21d return observed within trailing 504d — strongest 1-month rally in 2y."""
    r21 = close.pct_change(MDAYS)
    return r21.rolling(DDAYS_2Y, min_periods=YDAYS).max().diff().diff().diff()

def f31_rcmf_311_best_21d_return_1260d_d3(close: pd.Series) -> pd.Series:
    """Best trailing 21d return observed within trailing 1260d — strongest 1-month rally in 5y."""
    r21 = close.pct_change(MDAYS)
    return r21.rolling(DDAYS_5Y, min_periods=YDAYS).max().diff().diff().diff()

def f31_rcmf_312_best_63d_return_1260d_d3(close: pd.Series) -> pd.Series:
    """Best trailing 63d return observed within trailing 1260d — strongest quarter in 5y."""
    r63 = close.pct_change(QDAYS)
    return r63.rolling(DDAYS_5Y, min_periods=YDAYS).max().diff().diff().diff()

def f31_rcmf_313_best_minus_worst_1d_in_252d_d3(close: pd.Series) -> pd.Series:
    """Spread between best and worst 1d returns in 252d — extreme-event amplitude."""
    r = close.pct_change(1)
    return (r.rolling(YDAYS, min_periods=QDAYS).max() - r.rolling(YDAYS, min_periods=QDAYS).min()).diff().diff().diff()

def f31_rcmf_314_worst_5d_return_252d_d3(close: pd.Series) -> pd.Series:
    """Worst trailing 5d return in 252d — deepest weekly drawdown."""
    r5 = close.pct_change(WDAYS)
    return r5.rolling(YDAYS, min_periods=QDAYS).min().diff().diff().diff()

def f31_rcmf_315_worst_21d_return_252d_d3(close: pd.Series) -> pd.Series:
    """Worst trailing 21d return in 252d — deepest monthly drop."""
    r21 = close.pct_change(MDAYS)
    return r21.rolling(YDAYS, min_periods=QDAYS).min().diff().diff().diff()

def f31_rcmf_316_worst_63d_return_1260d_d3(close: pd.Series) -> pd.Series:
    """Worst trailing 63d return in 1260d — worst quarter in 5y."""
    r63 = close.pct_change(QDAYS)
    return r63.rolling(DDAYS_5Y, min_periods=YDAYS).min().diff().diff().diff()

def f31_rcmf_317_best_1d_to_mean_abs_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """Best 1d return / mean(|1d returns|) over 252d — ratio of extreme event to typical
    daily magnitude. High = single-bar shock unrepresentative of typical activity."""
    r = close.pct_change(1)
    best = r.rolling(YDAYS, min_periods=QDAYS).max()
    typ = r.abs().rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(best, typ).diff().diff().diff()

def f31_rcmf_318_best_21d_to_mean_abs_21d_ratio_252d_d3(close: pd.Series) -> pd.Series:
    """Best 21d return / mean(|21d returns|) over 252d — month-level extremity vs typical."""
    r21 = close.pct_change(MDAYS)
    best = r21.rolling(YDAYS, min_periods=QDAYS).max()
    typ = r21.abs().rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(best, typ).diff().diff().diff()

def f31_rcmf_319_best_1d_in_252d_rank_in_1260d_d3(close: pd.Series) -> pd.Series:
    """Rank of current best-1d-in-252d statistic within its own trailing 1260d distribution
    — how unusual is today's recent-best-single-day relative to multi-year norms."""
    r = close.pct_change(1)
    best252 = r.rolling(YDAYS, min_periods=QDAYS).max()
    return best252.rolling(DDAYS_5Y, min_periods=YDAYS).rank(pct=True).diff().diff().diff()

def f31_rcmf_320_current_1d_to_trailing_best_1d_252d_d3(close: pd.Series) -> pd.Series:
    """Today's 1d return divided by trailing 252d best-1d return — 0 to ~1, with ~1 meaning
    today is rivalling the prior-year extreme. Equals current-extremity gauge."""
    r = close.pct_change(1)
    best = r.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(r, best).diff().diff().diff()

def f31_rcmf_321_bars_since_best_1d_return_252d_d3(close: pd.Series) -> pd.Series:
    """Bars since the trailing-252d best-1d-return day — age of last single-day blowout."""
    r = close.pct_change(1)
    n = YDAYS

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        wv = np.where(valid, w, -np.inf)
        idx = int(np.argmax(wv))
        return float(len(w) - 1 - idx)
    return r.rolling(n, min_periods=QDAYS).apply(_bs, raw=True).diff().diff().diff()

def f31_rcmf_322_bars_since_best_1d_return_1260d_d3(close: pd.Series) -> pd.Series:
    """Bars since the trailing-1260d best-1d-return day — age of 5y single-day extreme."""
    r = close.pct_change(1)
    n = DDAYS_5Y

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        wv = np.where(valid, w, -np.inf)
        idx = int(np.argmax(wv))
        return float(len(w) - 1 - idx)
    return r.rolling(n, min_periods=YDAYS).apply(_bs, raw=True).diff().diff().diff()

def f31_rcmf_323_bars_since_worst_1d_return_252d_d3(close: pd.Series) -> pd.Series:
    """Bars since the trailing-252d worst-1d-return day — age of biggest down-day."""
    r = close.pct_change(1)
    n = YDAYS

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        wv = np.where(valid, w, np.inf)
        idx = int(np.argmin(wv))
        return float(len(w) - 1 - idx)
    return r.rolling(n, min_periods=QDAYS).apply(_bs, raw=True).diff().diff().diff()

def f31_rcmf_324_bars_since_worst_1d_return_1260d_d3(close: pd.Series) -> pd.Series:
    """Bars since the trailing-1260d worst-1d-return day."""
    r = close.pct_change(1)
    n = DDAYS_5Y

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        wv = np.where(valid, w, np.inf)
        idx = int(np.argmin(wv))
        return float(len(w) - 1 - idx)
    return r.rolling(n, min_periods=YDAYS).apply(_bs, raw=True).diff().diff().diff()

def f31_rcmf_325_bars_since_best_21d_return_252d_d3(close: pd.Series) -> pd.Series:
    """Bars since the trailing-252d best-21d-return ending day — age of biggest monthly rally."""
    r21 = close.pct_change(MDAYS)
    n = YDAYS

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        wv = np.where(valid, w, -np.inf)
        idx = int(np.argmax(wv))
        return float(len(w) - 1 - idx)
    return r21.rolling(n, min_periods=QDAYS).apply(_bs, raw=True).diff().diff().diff()

def f31_rcmf_326_bars_since_best_21d_return_1260d_d3(close: pd.Series) -> pd.Series:
    """Bars since the trailing-1260d best-21d-return ending day."""
    r21 = close.pct_change(MDAYS)
    n = DDAYS_5Y

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        wv = np.where(valid, w, -np.inf)
        idx = int(np.argmax(wv))
        return float(len(w) - 1 - idx)
    return r21.rolling(n, min_periods=YDAYS).apply(_bs, raw=True).diff().diff().diff()

def f31_rcmf_327_bars_since_best_63d_return_1260d_d3(close: pd.Series) -> pd.Series:
    """Bars since the trailing-1260d best-63d-return ending day — age of biggest quarterly rally."""
    r63 = close.pct_change(QDAYS)
    n = DDAYS_5Y

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < YDAYS:
            return np.nan
        wv = np.where(valid, w, -np.inf)
        idx = int(np.argmax(wv))
        return float(len(w) - 1 - idx)
    return r63.rolling(n, min_periods=YDAYS).apply(_bs, raw=True).diff().diff().diff()

def f31_rcmf_328_bars_since_5pct_up_day_252d_d3(close: pd.Series) -> pd.Series:
    """Bars since the most recent +5% single-day return in 252d — recency of strong rally days."""
    r = close.pct_change(1)
    flag = (r >= 0.05) & r.notna()
    return _bars_since_event(flag, YDAYS, QDAYS).diff().diff().diff()

def f31_rcmf_329_bars_since_10pct_up_day_252d_d3(close: pd.Series) -> pd.Series:
    """Bars since the most recent +10% single-day return in 252d — recency of extreme up-days."""
    r = close.pct_change(1)
    flag = (r >= 0.1) & r.notna()
    return _bars_since_event(flag, YDAYS, QDAYS).diff().diff().diff()

def f31_rcmf_330_bars_since_5pct_down_day_252d_d3(close: pd.Series) -> pd.Series:
    """Bars since the most recent −5% single-day return in 252d."""
    r = close.pct_change(1)
    flag = (r <= -0.05) & r.notna()
    return _bars_since_event(flag, YDAYS, QDAYS).diff().diff().diff()

def f31_rcmf_331_bars_since_10pct_down_day_252d_d3(close: pd.Series) -> pd.Series:
    """Bars since the most recent −10% single-day return in 252d — recency of crash days."""
    r = close.pct_change(1)
    flag = (r <= -0.1) & r.notna()
    return _bars_since_event(flag, YDAYS, QDAYS).diff().diff().diff()

def f31_rcmf_332_bars_since_first_negative_after_252d_high_d3(close: pd.Series) -> pd.Series:
    """Bars since the most recent 'first negative 1d return after a new 252d-close-high' event
    within trailing 504d. Stuck-forensic: first hint of buyer absence following each new high."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = (close >= rmax) & rmax.notna()
    r1 = close.pct_change(1)
    flag = at_high.shift(1).fillna(False).astype(bool) & (r1 < 0) & r1.notna()
    return _bars_since_event(flag, DDAYS_2Y, YDAYS).diff().diff().diff()

def f31_rcmf_333_bars_since_first_negative_21d_after_252d_high_d3(close: pd.Series) -> pd.Series:
    """Bars since first negative 21d return following a new 252d-high — stuck-forensic
    medium-horizon: bars since 'distribution started' on monthly horizon."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_high = (close >= rmax) & rmax.notna()
    r21 = close.pct_change(MDAYS)
    flag = at_high.shift(MDAYS).fillna(False).astype(bool) & (r21 < 0) & r21.notna()
    return _bars_since_event(flag, DDAYS_2Y, YDAYS).diff().diff().diff()

def f31_rcmf_334_bars_since_252d_close_high_d3(close: pd.Series) -> pd.Series:
    """Bars since the most recent 252d close-high — pure recency of new-yearly-high event."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    flag = (close >= rmax) & rmax.notna()
    return _bars_since_event(flag, YDAYS, QDAYS).diff().diff().diff()

def f31_rcmf_335_bars_since_1260d_close_high_d3(close: pd.Series) -> pd.Series:
    """Bars since the most recent 1260d (5y) close-high — recency of 5y top."""
    rmax = close.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    flag = (close >= rmax) & rmax.notna()
    return _bars_since_event(flag, DDAYS_5Y, YDAYS).diff().diff().diff()

def f31_rcmf_336_bars_since_21d_return_above_20pct_d3(close: pd.Series) -> pd.Series:
    """Bars since 21d return last exceeded +20% — recency of monthly burst."""
    r21 = close.pct_change(MDAYS)
    flag = (r21 >= 0.2) & r21.notna()
    return _bars_since_event(flag, DDAYS_2Y, YDAYS).diff().diff().diff()

def f31_rcmf_337_bars_since_63d_return_above_50pct_d3(close: pd.Series) -> pd.Series:
    """Bars since 63d return last exceeded +50% — recency of major quarterly rally."""
    r63 = close.pct_change(QDAYS)
    flag = (r63 >= 0.5) & r63.notna()
    return _bars_since_event(flag, DDAYS_2Y, YDAYS).diff().diff().diff()

def f31_rcmf_338_bars_since_1d_above_99th_pct_252d_d3(close: pd.Series) -> pd.Series:
    """Bars since 1d return last exceeded the 99th-percentile of trailing 252d return distribution
    — recency of statistically-extreme up-day. Distinct from existing 293/295 which use 90th/99th
    over different windows — this is 1d return vs 252d 99th-pct event-recency."""
    r = close.pct_change(1)
    q99 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    flag = (r >= q99) & r.notna() & q99.notna()
    return _bars_since_event(flag, YDAYS, QDAYS).diff().diff().diff()

def f31_rcmf_339_bars_since_5d_above_95th_pct_252d_d3(close: pd.Series) -> pd.Series:
    """Bars since 5d return last exceeded the 95th-percentile of trailing 252d 5d distribution."""
    r5 = close.pct_change(WDAYS)
    q95 = r5.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (r5 >= q95) & r5.notna() & q95.notna()
    return _bars_since_event(flag, YDAYS, QDAYS).diff().diff().diff()

def f31_rcmf_340_bars_since_pos_followed_by_5neg_d3(close: pd.Series) -> pd.Series:
    """Bars since the last positive 1d-return immediately followed by 5 consecutive negative
    1d-returns — recency of a 'reversal-day-confirmed-by-week' event."""
    r = close.pct_change(1)
    sign = np.sign(r)
    pos_prev = sign.shift(5) > 0
    neg_streak = (sign.shift(4) < 0) & (sign.shift(3) < 0) & (sign.shift(2) < 0) & (sign.shift(1) < 0) & (sign < 0)
    flag = pos_prev & neg_streak
    return _bars_since_event(flag.fillna(False), YDAYS, QDAYS).diff().diff().diff()

def f31_rcmf_341_ret_1d_above_99th_pct_252d_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator (0/1): today's 1d return exceeds 99th percentile of trailing 252d 1d returns."""
    r = close.pct_change(1)
    q99 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    out = (r >= q99).astype(float)
    return out.where(r.notna() & q99.notna(), np.nan).diff().diff().diff()

def f31_rcmf_342_ret_1d_below_1st_pct_252d_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: today's 1d return below 1st percentile of trailing 252d."""
    r = close.pct_change(1)
    q01 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.01)
    out = (r <= q01).astype(float)
    return out.where(r.notna() & q01.notna(), np.nan).diff().diff().diff()

def f31_rcmf_343_ret_1d_above_10pct_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: today's 1d return > +10% (absolute extreme up-day event)."""
    r = close.pct_change(1)
    out = (r > 0.1).astype(float)
    return out.where(r.notna(), np.nan).diff().diff().diff()

def f31_rcmf_344_ret_1d_below_neg10pct_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: today's 1d return < −10% (absolute extreme down-day event)."""
    r = close.pct_change(1)
    out = (r < -0.1).astype(float)
    return out.where(r.notna(), np.nan).diff().diff().diff()

def f31_rcmf_345_ret_5d_above_25pct_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: trailing 5d return > +25% (weekly vertical-move event)."""
    r5 = close.pct_change(WDAYS)
    out = (r5 > 0.25).astype(float)
    return out.where(r5.notna(), np.nan).diff().diff().diff()

def f31_rcmf_346_four_consecutive_positive_5d_returns_d3(close: pd.Series) -> pd.Series:
    """Indicator: 4 consecutive positive 5d returns sampled every 5 bars
    (4 weeks-up event)."""
    r5 = close.pct_change(WDAYS)
    s = (r5 > 0).astype(float)
    cond = (s.shift(15) > 0) & (s.shift(10) > 0) & (s.shift(5) > 0) & (s > 0)
    return cond.astype(float).where(r5.notna(), np.nan).diff().diff().diff()

def f31_rcmf_347_four_consecutive_negative_5d_returns_d3(close: pd.Series) -> pd.Series:
    """Indicator: 4 consecutive negative 5d returns sampled every 5 bars (4 down-weeks event)."""
    r5 = close.pct_change(WDAYS)
    s = (r5 < 0).astype(float)
    cond = (s.shift(15) > 0) & (s.shift(10) > 0) & (s.shift(5) > 0) & (s > 0)
    return cond.astype(float).where(r5.notna(), np.nan).diff().diff().diff()

def f31_rcmf_348_first_positive_after_5_negative_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: today positive after 5 consecutive prior-day negatives — reversal-up event."""
    r = close.pct_change(1)
    cond = (r > 0) & (r.shift(1) < 0) & (r.shift(2) < 0) & (r.shift(3) < 0) & (r.shift(4) < 0) & (r.shift(5) < 0)
    return cond.astype(float).where(r.notna(), np.nan).diff().diff().diff()

def f31_rcmf_349_first_negative_after_5_positive_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: today negative after 5 consecutive prior-day positives — reversal-down event.
    Classic exhaustion fingerprint at a high."""
    r = close.pct_change(1)
    cond = (r < 0) & (r.shift(1) > 0) & (r.shift(2) > 0) & (r.shift(3) > 0) & (r.shift(4) > 0) & (r.shift(5) > 0)
    return cond.astype(float).where(r.notna(), np.nan).diff().diff().diff()

def f31_rcmf_350_ret_21d_turns_negative_after_above_50pct_d3(close: pd.Series) -> pd.Series:
    """Indicator: ret_21d now < 0 AND any of the prior 21 bars had ret_21d > +50%. Stuck-forensic
    'fast collapse after vertical run' event."""
    r21 = close.pct_change(MDAYS)
    prev_extreme = r21.shift(1).rolling(MDAYS, min_periods=WDAYS).max() > 0.5
    cond = (r21 < 0) & prev_extreme
    return cond.astype(float).where(r21.notna(), np.nan).diff().diff().diff()

def f31_rcmf_351_ret_63d_crosses_zero_from_positive_d3(close: pd.Series) -> pd.Series:
    """Indicator: ret_63d < 0 today but was >= 0 yesterday — quarterly-momentum sign-flip event."""
    r63 = close.pct_change(QDAYS)
    cond = (r63 < 0) & (r63.shift(1) >= 0)
    return cond.astype(float).where(r63.notna() & r63.shift(1).notna(), np.nan).diff().diff().diff()

def f31_rcmf_352_ret_252d_crosses_zero_from_positive_d3(close: pd.Series) -> pd.Series:
    """Indicator: ret_252d < 0 today but >= 0 yesterday — annual sign-flip event (regime change)."""
    r252 = close.pct_change(YDAYS)
    cond = (r252 < 0) & (r252.shift(1) >= 0)
    return cond.astype(float).where(r252.notna() & r252.shift(1).notna(), np.nan).diff().diff().diff()

def f31_rcmf_353_first_10pct_dd_from_252d_high_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator of bar where running drawdown from trailing-252d-max first reaches −10% after
    having been within 2% of a fresh 252d-high in the last 21 bars."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    recent_at_high = (dd >= -0.02).rolling(MDAYS, min_periods=WDAYS).max()
    cond = (dd <= -0.1) & (dd.shift(1) > -0.1) & (recent_at_high.shift(1) > 0)
    return cond.astype(float).where(dd.notna(), np.nan).diff().diff().diff()

def f31_rcmf_354_range_21d_above_30pct_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: (max(close,21d) − min(close,21d)) / close_today > 30% — monthly amplitude
    vertical-move flag."""
    rmax = close.rolling(MDAYS, min_periods=WDAYS).max()
    rmin = close.rolling(MDAYS, min_periods=WDAYS).min()
    amp = _safe_div(rmax - rmin, close)
    cond = amp > 0.3
    return cond.astype(float).where(amp.notna(), np.nan).diff().diff().diff()

def f31_rcmf_355_range_5d_above_15pct_indicator_d3(close: pd.Series) -> pd.Series:
    """Indicator: 5d range / close > 15% — weekly amplitude spike flag."""
    rmax = close.rolling(WDAYS, min_periods=2).max()
    rmin = close.rolling(WDAYS, min_periods=2).min()
    amp = _safe_div(rmax - rmin, close)
    cond = amp > 0.15
    return cond.astype(float).where(amp.notna(), np.nan).diff().diff().diff()

def f31_rcmf_356_gap_return_1d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Today's overnight gap return: open_today / prev_close − 1. Atomic overnight component."""
    return (_safe_div(open_, close.shift(1)) - 1.0).diff().diff().diff()

def f31_rcmf_357_intraday_return_1d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Today's intraday return: close / open − 1. Atomic session-bar component."""
    return (_safe_div(close, open_) - 1.0).diff().diff().diff()

def f31_rcmf_358_mean_gap_return_21d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Mean overnight gap return over trailing 21d."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    return g.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f31_rcmf_359_std_gap_return_21d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Std of overnight gap return over trailing 21d — overnight volatility."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    return g.rolling(MDAYS, min_periods=WDAYS).std().diff().diff().diff()

def f31_rcmf_360_mean_intraday_return_21d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Mean intraday (open-to-close) return over trailing 21d."""
    i = _safe_div(close, open_) - 1.0
    return i.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f31_rcmf_361_std_intraday_return_21d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Std of intraday return over trailing 21d — intraday volatility."""
    i = _safe_div(close, open_) - 1.0
    return i.rolling(MDAYS, min_periods=WDAYS).std().diff().diff().diff()

def f31_rcmf_362_largest_gap_up_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Largest gap-up in trailing 252d (max of gap_return_1d)."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    return g.rolling(YDAYS, min_periods=QDAYS).max().diff().diff().diff()

def f31_rcmf_363_largest_gap_down_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Largest gap-down in trailing 252d (min of gap_return_1d)."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    return g.rolling(YDAYS, min_periods=QDAYS).min().diff().diff().diff()

def f31_rcmf_364_bars_since_largest_gap_up_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the trailing-252d largest gap-up day."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    n = YDAYS

    def _bs(w):
        valid = ~np.isnan(w)
        if valid.sum() < QDAYS:
            return np.nan
        wv = np.where(valid, w, -np.inf)
        return float(len(w) - 1 - int(np.argmax(wv)))
    return g.rolling(n, min_periods=QDAYS).apply(_bs, raw=True).diff().diff().diff()

def f31_rcmf_365_overnight_return_sum_21d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of overnight gap returns over trailing 21d — cumulative overnight contribution."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    return g.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f31_rcmf_366_overnight_return_sum_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of overnight gap returns over trailing 63d — quarterly overnight contribution."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    return g.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f31_rcmf_367_intraday_return_sum_21d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of intraday returns over trailing 21d — cumulative session contribution."""
    i = _safe_div(close, open_) - 1.0
    return i.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff().diff()

def f31_rcmf_368_intraday_return_sum_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of intraday returns over trailing 63d — quarterly session contribution."""
    i = _safe_div(close, open_) - 1.0
    return i.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f31_rcmf_369_overnight_to_intraday_ratio_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Sum_overnight_63d / sum_intraday_63d — relative dominance of overnight vs session.
    Lordhart-style return decomposition signal."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    i = _safe_div(close, open_) - 1.0
    gn = g.rolling(QDAYS, min_periods=MDAYS).sum()
    inn = i.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(gn, inn).diff().diff().diff()

def f31_rcmf_370_fraction_gap_fade_days_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 63d where gap > 0 AND intraday < 0 (gap-fade days)."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    i = _safe_div(close, open_) - 1.0
    fade = ((g > 0) & (i < 0)).astype(float)
    valid = (g.notna() & i.notna()).astype(float)
    return _safe_div(fade.rolling(QDAYS, min_periods=MDAYS).sum(), valid.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f31_rcmf_371_fraction_gap_extend_days_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in trailing 63d where gap > 0 AND intraday > 0 (gap-extend days)."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    i = _safe_div(close, open_) - 1.0
    ext = ((g > 0) & (i > 0)).astype(float)
    valid = (g.notna() & i.notna()).astype(float)
    return _safe_div(ext.rolling(QDAYS, min_periods=MDAYS).sum(), valid.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f31_rcmf_372_fraction_inverted_gap_days_63d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in 63d where gap < 0 AND intraday > 0 (gap-down reversed intraday)."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    i = _safe_div(close, open_) - 1.0
    inv = ((g < 0) & (i > 0)).astype(float)
    valid = (g.notna() & i.notna()).astype(float)
    return _safe_div(inv.rolling(QDAYS, min_periods=MDAYS).sum(), valid.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()

def f31_rcmf_373_cumulative_gap_return_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative (sum) overnight gap return over trailing 252d — annual overnight contribution."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    return g.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f31_rcmf_374_cumulative_intraday_return_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative (sum) intraday return over trailing 252d — annual session contribution."""
    i = _safe_div(close, open_) - 1.0
    return i.rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f31_rcmf_375_overnight_share_of_total_252d_d3(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight share of total move over trailing 252d:
    sum_overnight / (sum_overnight + sum_intraday)."""
    g = _safe_div(open_, close.shift(1)) - 1.0
    i = _safe_div(close, open_) - 1.0
    gn = g.rolling(YDAYS, min_periods=QDAYS).sum()
    inn = i.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(gn, gn + inn).diff().diff().diff()
ROC_MOMENTUM_FAMILY_D3_REGISTRY_301_375 = {'f31_rcmf_301_best_1d_return_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_301_best_1d_return_252d_d3}, 'f31_rcmf_302_best_1d_return_504d_d3': {'inputs': ['close'], 'func': f31_rcmf_302_best_1d_return_504d_d3}, 'f31_rcmf_303_best_1d_return_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_303_best_1d_return_1260d_d3}, 'f31_rcmf_304_worst_1d_return_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_304_worst_1d_return_252d_d3}, 'f31_rcmf_305_worst_1d_return_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_305_worst_1d_return_1260d_d3}, 'f31_rcmf_306_best_3d_return_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_306_best_3d_return_252d_d3}, 'f31_rcmf_307_best_5d_return_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_307_best_5d_return_252d_d3}, 'f31_rcmf_308_best_5d_return_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_308_best_5d_return_1260d_d3}, 'f31_rcmf_309_best_10d_return_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_309_best_10d_return_252d_d3}, 'f31_rcmf_310_best_21d_return_504d_d3': {'inputs': ['close'], 'func': f31_rcmf_310_best_21d_return_504d_d3}, 'f31_rcmf_311_best_21d_return_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_311_best_21d_return_1260d_d3}, 'f31_rcmf_312_best_63d_return_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_312_best_63d_return_1260d_d3}, 'f31_rcmf_313_best_minus_worst_1d_in_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_313_best_minus_worst_1d_in_252d_d3}, 'f31_rcmf_314_worst_5d_return_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_314_worst_5d_return_252d_d3}, 'f31_rcmf_315_worst_21d_return_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_315_worst_21d_return_252d_d3}, 'f31_rcmf_316_worst_63d_return_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_316_worst_63d_return_1260d_d3}, 'f31_rcmf_317_best_1d_to_mean_abs_ratio_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_317_best_1d_to_mean_abs_ratio_252d_d3}, 'f31_rcmf_318_best_21d_to_mean_abs_21d_ratio_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_318_best_21d_to_mean_abs_21d_ratio_252d_d3}, 'f31_rcmf_319_best_1d_in_252d_rank_in_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_319_best_1d_in_252d_rank_in_1260d_d3}, 'f31_rcmf_320_current_1d_to_trailing_best_1d_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_320_current_1d_to_trailing_best_1d_252d_d3}, 'f31_rcmf_321_bars_since_best_1d_return_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_321_bars_since_best_1d_return_252d_d3}, 'f31_rcmf_322_bars_since_best_1d_return_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_322_bars_since_best_1d_return_1260d_d3}, 'f31_rcmf_323_bars_since_worst_1d_return_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_323_bars_since_worst_1d_return_252d_d3}, 'f31_rcmf_324_bars_since_worst_1d_return_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_324_bars_since_worst_1d_return_1260d_d3}, 'f31_rcmf_325_bars_since_best_21d_return_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_325_bars_since_best_21d_return_252d_d3}, 'f31_rcmf_326_bars_since_best_21d_return_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_326_bars_since_best_21d_return_1260d_d3}, 'f31_rcmf_327_bars_since_best_63d_return_1260d_d3': {'inputs': ['close'], 'func': f31_rcmf_327_bars_since_best_63d_return_1260d_d3}, 'f31_rcmf_328_bars_since_5pct_up_day_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_328_bars_since_5pct_up_day_252d_d3}, 'f31_rcmf_329_bars_since_10pct_up_day_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_329_bars_since_10pct_up_day_252d_d3}, 'f31_rcmf_330_bars_since_5pct_down_day_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_330_bars_since_5pct_down_day_252d_d3}, 'f31_rcmf_331_bars_since_10pct_down_day_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_331_bars_since_10pct_down_day_252d_d3}, 'f31_rcmf_332_bars_since_first_negative_after_252d_high_d3': {'inputs': ['close'], 'func': f31_rcmf_332_bars_since_first_negative_after_252d_high_d3}, 'f31_rcmf_333_bars_since_first_negative_21d_after_252d_high_d3': {'inputs': ['close'], 'func': f31_rcmf_333_bars_since_first_negative_21d_after_252d_high_d3}, 'f31_rcmf_334_bars_since_252d_close_high_d3': {'inputs': ['close'], 'func': f31_rcmf_334_bars_since_252d_close_high_d3}, 'f31_rcmf_335_bars_since_1260d_close_high_d3': {'inputs': ['close'], 'func': f31_rcmf_335_bars_since_1260d_close_high_d3}, 'f31_rcmf_336_bars_since_21d_return_above_20pct_d3': {'inputs': ['close'], 'func': f31_rcmf_336_bars_since_21d_return_above_20pct_d3}, 'f31_rcmf_337_bars_since_63d_return_above_50pct_d3': {'inputs': ['close'], 'func': f31_rcmf_337_bars_since_63d_return_above_50pct_d3}, 'f31_rcmf_338_bars_since_1d_above_99th_pct_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_338_bars_since_1d_above_99th_pct_252d_d3}, 'f31_rcmf_339_bars_since_5d_above_95th_pct_252d_d3': {'inputs': ['close'], 'func': f31_rcmf_339_bars_since_5d_above_95th_pct_252d_d3}, 'f31_rcmf_340_bars_since_pos_followed_by_5neg_d3': {'inputs': ['close'], 'func': f31_rcmf_340_bars_since_pos_followed_by_5neg_d3}, 'f31_rcmf_341_ret_1d_above_99th_pct_252d_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_341_ret_1d_above_99th_pct_252d_indicator_d3}, 'f31_rcmf_342_ret_1d_below_1st_pct_252d_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_342_ret_1d_below_1st_pct_252d_indicator_d3}, 'f31_rcmf_343_ret_1d_above_10pct_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_343_ret_1d_above_10pct_indicator_d3}, 'f31_rcmf_344_ret_1d_below_neg10pct_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_344_ret_1d_below_neg10pct_indicator_d3}, 'f31_rcmf_345_ret_5d_above_25pct_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_345_ret_5d_above_25pct_indicator_d3}, 'f31_rcmf_346_four_consecutive_positive_5d_returns_d3': {'inputs': ['close'], 'func': f31_rcmf_346_four_consecutive_positive_5d_returns_d3}, 'f31_rcmf_347_four_consecutive_negative_5d_returns_d3': {'inputs': ['close'], 'func': f31_rcmf_347_four_consecutive_negative_5d_returns_d3}, 'f31_rcmf_348_first_positive_after_5_negative_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_348_first_positive_after_5_negative_indicator_d3}, 'f31_rcmf_349_first_negative_after_5_positive_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_349_first_negative_after_5_positive_indicator_d3}, 'f31_rcmf_350_ret_21d_turns_negative_after_above_50pct_d3': {'inputs': ['close'], 'func': f31_rcmf_350_ret_21d_turns_negative_after_above_50pct_d3}, 'f31_rcmf_351_ret_63d_crosses_zero_from_positive_d3': {'inputs': ['close'], 'func': f31_rcmf_351_ret_63d_crosses_zero_from_positive_d3}, 'f31_rcmf_352_ret_252d_crosses_zero_from_positive_d3': {'inputs': ['close'], 'func': f31_rcmf_352_ret_252d_crosses_zero_from_positive_d3}, 'f31_rcmf_353_first_10pct_dd_from_252d_high_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_353_first_10pct_dd_from_252d_high_indicator_d3}, 'f31_rcmf_354_range_21d_above_30pct_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_354_range_21d_above_30pct_indicator_d3}, 'f31_rcmf_355_range_5d_above_15pct_indicator_d3': {'inputs': ['close'], 'func': f31_rcmf_355_range_5d_above_15pct_indicator_d3}, 'f31_rcmf_356_gap_return_1d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_356_gap_return_1d_d3}, 'f31_rcmf_357_intraday_return_1d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_357_intraday_return_1d_d3}, 'f31_rcmf_358_mean_gap_return_21d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_358_mean_gap_return_21d_d3}, 'f31_rcmf_359_std_gap_return_21d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_359_std_gap_return_21d_d3}, 'f31_rcmf_360_mean_intraday_return_21d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_360_mean_intraday_return_21d_d3}, 'f31_rcmf_361_std_intraday_return_21d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_361_std_intraday_return_21d_d3}, 'f31_rcmf_362_largest_gap_up_252d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_362_largest_gap_up_252d_d3}, 'f31_rcmf_363_largest_gap_down_252d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_363_largest_gap_down_252d_d3}, 'f31_rcmf_364_bars_since_largest_gap_up_252d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_364_bars_since_largest_gap_up_252d_d3}, 'f31_rcmf_365_overnight_return_sum_21d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_365_overnight_return_sum_21d_d3}, 'f31_rcmf_366_overnight_return_sum_63d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_366_overnight_return_sum_63d_d3}, 'f31_rcmf_367_intraday_return_sum_21d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_367_intraday_return_sum_21d_d3}, 'f31_rcmf_368_intraday_return_sum_63d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_368_intraday_return_sum_63d_d3}, 'f31_rcmf_369_overnight_to_intraday_ratio_63d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_369_overnight_to_intraday_ratio_63d_d3}, 'f31_rcmf_370_fraction_gap_fade_days_63d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_370_fraction_gap_fade_days_63d_d3}, 'f31_rcmf_371_fraction_gap_extend_days_63d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_371_fraction_gap_extend_days_63d_d3}, 'f31_rcmf_372_fraction_inverted_gap_days_63d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_372_fraction_inverted_gap_days_63d_d3}, 'f31_rcmf_373_cumulative_gap_return_252d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_373_cumulative_gap_return_252d_d3}, 'f31_rcmf_374_cumulative_intraday_return_252d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_374_cumulative_intraday_return_252d_d3}, 'f31_rcmf_375_overnight_share_of_total_252d_d3': {'inputs': ['open', 'close'], 'func': f31_rcmf_375_overnight_share_of_total_252d_d3}}