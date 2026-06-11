"""td_sequential_demark d1 features 076-150 — Pipeline 1b-technical.

Extends __base__001_075.py with TD REI (Range Expansion Index), TD Demand/Supply
levels, TD bar-pattern signals (Camouflage, Open, Trap, Differential), TD Combo +
Aggressive composites, time-since-event signals, conjunctions of TD signals with
volume/range, conjunctions of TD signals at multi-year highs, and weighted
DeMark topping-pressure composites.

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers.
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


def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)


def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill


# ---------------------------- TD setup/countdown helpers ----------------------------

def _td_sell_setup_count(close: pd.Series) -> pd.Series:
    qual = (close > close.shift(4)).astype(int)
    qual = qual.where(close.shift(4).notna(), np.nan).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)


def _td_buy_setup_count(close: pd.Series) -> pd.Series:
    qual = (close < close.shift(4)).astype(int)
    qual = qual.where(close.shift(4).notna(), np.nan).fillna(0).astype(int)
    grp = (qual == 0).cumsum()
    return qual.groupby(grp).cumsum().astype(float)


def _td_sell_countdown_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    cl = close.values; hi = high.values
    n = len(close)
    out = np.zeros(n)
    active = False; cnt = 0
    for i in range(n):
        if not active and i >= 8 and sc[i] >= 9:
            active = True; cnt = 0
        if active and i >= 8 and bc[i] >= 9:
            active = False; cnt = 0
        if active:
            if i >= 2 and cl[i] >= hi[i - 2] and cnt < 13:
                cnt += 1
            out[i] = cnt
    return pd.Series(out, index=close.index)


def _td_sell_combo_count(close: pd.Series, high: pd.Series) -> pd.Series:
    """TD Combo: consecutive-bar variant of sell-countdown."""
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    cl = close.values; hi = high.values
    n = len(close)
    out = np.zeros(n)
    active = False; cnt = 0
    for i in range(n):
        if not active and i >= 8 and sc[i] >= 9:
            active = True; cnt = 0
        if active and i >= 8 and bc[i] >= 9:
            active = False; cnt = 0
        if active and i >= 2:
            qual = (cl[i] >= hi[i - 2])
            if qual and cnt < 13:
                cnt += 1
            elif not qual:
                cnt = 0
            out[i] = cnt
    return pd.Series(out, index=close.index)


def _td_perfected_sell_setup_9_event(close: pd.Series, high: pd.Series) -> pd.Series:
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float)
    h6 = high.shift(3); h7 = high.shift(2); h8 = high.shift(1); h9 = high
    bar_max = pd.concat([h6, h7], axis=1).max(axis=1)
    perfected = ((h8 >= bar_max) | (h9 >= bar_max)).astype(float)
    return (fires * perfected).where(sc.notna(), np.nan)


# ---------------------------- TD REI helper ----------------------------

def _td_rei(close: pd.Series, high: pd.Series, low: pd.Series, n: int = 5) -> pd.Series:
    """TD Range Expansion Index: a momentum oscillator -100..+100 that filters certain bar patterns."""
    high_mom = high - high.shift(2)
    low_mom = low - low.shift(2)
    abs_high_mom = high_mom.abs()
    abs_low_mom = low_mom.abs()
    cond1 = (high.shift(2) >= close.shift(7)) | (high.shift(2) >= close.shift(8))
    cond2 = (high >= low.shift(5)) | (high >= low.shift(6))
    cond3 = (low.shift(2) <= close.shift(7)) | (low.shift(2) <= close.shift(8))
    cond4 = (low <= high.shift(5)) | (low <= high.shift(6))
    weight = ((cond1 & cond2) | (cond3 & cond4)).astype(float)
    weighted = (high_mom + low_mom) * weight
    abs_sum = abs_high_mom + abs_low_mom
    num = weighted.rolling(n, min_periods=max(n // 3, 2)).sum()
    den = abs_sum.rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(num, den)


# ---------------------------- TD bar-pattern helpers ----------------------------

def _td_camouflage_event(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish TD Camouflage (mirror of standard bullish): close < prior close AND close >= prior open
    AND true high > prior true high."""
    pc = close.shift(1); po = open_.shift(1)
    pch = pd.concat([high, close.shift(1)], axis=1).max(axis=1)
    p_pch = pch.shift(1)
    flag = ((close < pc) & (close >= po) & (pch > p_pch))
    return flag.astype(float).where(pc.notna() & po.notna() & p_pch.notna(), np.nan)


def _td_open_up_gap_event(open_: pd.Series, high: pd.Series) -> pd.Series:
    """TD Open Up: open > prior high (gap up — exhaustion signal at top)."""
    return (open_ > high.shift(1)).astype(float).where(high.shift(1).notna(), np.nan)


def _td_trap_event(close: pd.Series, high: pd.Series) -> pd.Series:
    """TD Trap (bearish failed breakout): high > prior high BUT close <= prior close."""
    flag = ((high > high.shift(1)) & (close <= close.shift(1)))
    return flag.astype(float).where(high.shift(1).notna() & close.shift(1).notna(), np.nan)


def _td_differential_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish TD Differential: close < prior close AND (close - low) > (prior close - prior low)
    AND (prior high - prior close) > (high - close)."""
    pc = close.shift(1); ph = high.shift(1); pl = low.shift(1)
    cond_a = (close < pc)
    cond_b = ((close - low) > (pc - pl))
    cond_c = ((ph - pc) > (high - close))
    return (cond_a & cond_b & cond_c).astype(float).where(pc.notna() & ph.notna() & pl.notna(), np.nan)


def _td_pressure(open_: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series, n: int = 13) -> pd.Series:
    body = (close - open_)
    rng = (high - low).replace(0, np.nan)
    return _safe_div(body.rolling(n, min_periods=max(n // 3, 2)).sum(),
                     rng.rolling(n, min_periods=max(n // 3, 2)).sum())


# ============================================================
# Bucket H — TD REI (Range Expansion Index) (076-085)
# ============================================================

def f34_tdsq_076_td_rei_value_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD REI value (5d standard window)."""
    return _td_rei(close, high, low, 5)


def f34_tdsq_077_td_rei_overbought_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when TD REI > +60 (canonical overbought threshold)."""
    r = _td_rei(close, high, low, 5)
    return (r > 60).astype(float).where(r.notna(), np.nan)


def f34_tdsq_078_td_rei_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of TD REI in trailing 252d."""
    return _pct_rank(_td_rei(close, high, low, 5), YDAYS)


def f34_tdsq_079_td_rei_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of TD REI over 252d."""
    return _rolling_zscore(_td_rei(close, high, low, 5), YDAYS)


def f34_tdsq_080_td_rei_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21d slope of TD REI."""
    return _rolling_slope(_td_rei(close, high, low, 5), MDAYS)


def f34_tdsq_081_days_since_td_rei_above_60(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since TD REI was last above +60 (overbought trigger age)."""
    r = _td_rei(close, high, low, 5)
    return _bars_since_true((r > 60).astype(float))


def f34_tdsq_082_td_rei_persistence_above_60_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing-21d bars where TD REI > 60."""
    r = _td_rei(close, high, low, 5)
    return (r > 60).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f34_tdsq_083_td_rei_count_above_60_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing-252d bars where TD REI > 60."""
    r = _td_rei(close, high, low, 5)
    return (r > 60).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_084_td_rei_top_to_breakdown_velocity(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5d-slope of TD REI conditional on REI < REI 21d ago — post-peak velocity at top."""
    r = _td_rei(close, high, low, 5)
    s5 = _rolling_slope(r, WDAYS)
    falling_long = (r < r.shift(MDAYS))
    return s5.where(falling_long, 0.0)


def f34_tdsq_085_td_rei_overbought_x_close_at_252d_high_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when TD REI > 60 AND close within 1% of 252d max."""
    r = _td_rei(close, high, low, 5)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((r > 60) & (near == 1)).astype(float).where(r.notna() & near.notna(), np.nan)


# ============================================================
# Bucket I — TD Demand / Supply (086-090)
# ============================================================

def f34_tdsq_086_td_demand_level_last_sell_setup_lowest_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """TD Demand: lowest low during the most recent completed sell setup (forward-fill held)."""
    sc = _td_sell_setup_count(close).values
    lo = low.values
    n = len(close)
    out = np.full(n, np.nan)
    cur_min = np.nan; in_setup = False
    last_demand = np.nan
    for i in range(n):
        if sc[i] == 1:
            in_setup = True; cur_min = lo[i]
        elif in_setup and i > 0 and sc[i] > sc[i - 1]:
            cur_min = min(cur_min, lo[i])
        if in_setup and i > 0 and sc[i] == 0:
            if sc[i - 1] >= 9:
                last_demand = cur_min
            in_setup = False
        out[i] = last_demand
    return pd.Series(out, index=close.index)


def f34_tdsq_087_td_supply_level_last_buy_setup_highest_high(close: pd.Series, high: pd.Series) -> pd.Series:
    """TD Supply: highest high during the most recent completed buy setup (forward-fill held)."""
    bc = _td_buy_setup_count(close).values
    hi = high.values
    n = len(close)
    out = np.full(n, np.nan)
    cur_max = np.nan; in_setup = False
    last_supply = np.nan
    for i in range(n):
        if bc[i] == 1:
            in_setup = True; cur_max = hi[i]
        elif in_setup and i > 0 and bc[i] > bc[i - 1]:
            cur_max = max(cur_max, hi[i])
        if in_setup and i > 0 and bc[i] == 0:
            if bc[i - 1] >= 9:
                last_supply = cur_max
            in_setup = False
        out[i] = last_supply
    return pd.Series(out, index=close.index)


def f34_tdsq_088_close_below_td_demand_indicator(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when close < TD Demand level (breakdown below demand-support)."""
    d = f34_tdsq_086_td_demand_level_last_sell_setup_lowest_low(close, low)
    return (close < d).astype(float).where(d.notna(), np.nan)


def f34_tdsq_089_close_distance_to_td_supply_atr_norm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(TD_supply - close) / ATR21 — distance below supply ceiling."""
    s = f34_tdsq_087_td_supply_level_last_buy_setup_highest_high(close, high)
    return _safe_div(s - close, _atr(high, low, close, MDAYS))


def f34_tdsq_090_close_below_td_demand_event_indicator(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where close newly crosses below TD demand level (breakdown event)."""
    d = f34_tdsq_086_td_demand_level_last_sell_setup_lowest_low(close, low)
    return ((close < d) & (close.shift(1) >= d.shift(1))).astype(float).where(d.notna() & d.shift(1).notna(), np.nan)


# ============================================================
# Bucket J — TD bar patterns: Camouflage / Open / Trap / Differential (091-100)
# ============================================================

def f34_tdsq_091_td_camouflage_bearish_event_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where bearish TD Camouflage condition fires."""
    return _td_camouflage_event(open, close, high, low)


def f34_tdsq_092_td_camouflage_count_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bearish TD Camouflage events in trailing 252d."""
    f = _td_camouflage_event(open, close, high, low)
    return f.fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_093_td_open_up_gap_event_indicator(open: pd.Series, high: pd.Series) -> pd.Series:
    """+1 on bar where open > prior high (TD Open Up gap — exhaustion signal)."""
    return _td_open_up_gap_event(open, high)


def f34_tdsq_094_td_open_up_gap_count_252d(open: pd.Series, high: pd.Series) -> pd.Series:
    """Count of TD Open-Up-Gap events in trailing 252d."""
    f = _td_open_up_gap_event(open, high)
    return f.fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_095_td_trap_event_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 on bar where bearish TD Trap fires (new high, lower-or-equal close)."""
    return _td_trap_event(close, high)


def f34_tdsq_096_td_trap_count_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of bearish TD Trap events in trailing 63d."""
    return _td_trap_event(close, high).fillna(0).rolling(QDAYS, min_periods=MDAYS).sum()


def f34_tdsq_097_td_trap_count_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of bearish TD Trap events in trailing 252d."""
    return _td_trap_event(close, high).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_098_td_differential_bearish_event_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where bearish TD Differential fires."""
    return _td_differential_bearish_event(close, high, low)


def f34_tdsq_099_td_differential_bearish_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bearish TD Differential events in trailing 252d."""
    return _td_differential_bearish_event(close, high, low).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_100_td_bar_pattern_breadth_4indicators_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count (0..4) of bearish TD bar patterns firing TODAY: Camouflage, Open-Up gap, Trap, Differential."""
    a = _td_camouflage_event(open, close, high, low).fillna(0)
    b = _td_open_up_gap_event(open, high).fillna(0)
    c = _td_trap_event(close, high).fillna(0)
    d = _td_differential_bearish_event(close, high, low).fillna(0)
    return a + b + c + d


# ============================================================
# Bucket K — TD Combo & Aggressive composites (101-110)
# ============================================================

def f34_tdsq_101_td_sell_combo_count_current(close: pd.Series, high: pd.Series) -> pd.Series:
    """Current running TD Combo count (consecutive-bar countdown variant)."""
    return _td_sell_combo_count(close, high)


def f34_tdsq_102_td_sell_combo_13_fires_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 on bar where TD Combo count transitions <13 → 13."""
    cb = _td_sell_combo_count(close, high)
    return ((cb == 13) & (cb.shift(1) < 13)).astype(float).where(cb.notna() & cb.shift(1).notna(), np.nan)


def f34_tdsq_103_days_since_td_sell_combo_13(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since most recent TD Combo-13 fire."""
    cb = _td_sell_combo_count(close, high)
    fire = ((cb == 13) & (cb.shift(1) < 13)).astype(float)
    return _bars_since_true(fire)


def f34_tdsq_104_count_td_sell_combo_13_in_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of TD Combo-13 fires in trailing 252d."""
    cb = _td_sell_combo_count(close, high)
    fire = ((cb == 13) & (cb.shift(1) < 13)).astype(float)
    return fire.rolling(YDAYS, min_periods=QDAYS).sum()


def f34_tdsq_105_td_combo_active_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when TD Combo count > 0 AND < 13."""
    cb = _td_sell_combo_count(close, high)
    return ((cb > 0) & (cb < 13)).astype(float).where(cb.notna(), np.nan)


def f34_tdsq_106_td_combo_progress_pct(close: pd.Series, high: pd.Series) -> pd.Series:
    """Current TD Combo count / 13."""
    return _td_sell_combo_count(close, high) / 13.0


def f34_tdsq_107_td_sell_combo_max_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Max TD Combo count over trailing 252d."""
    return _td_sell_combo_count(close, high).rolling(YDAYS, min_periods=QDAYS).max()


def f34_tdsq_108_td_combo_vs_countdown_agreement_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when BOTH TD Combo and standard sell-countdown are currently active."""
    cb_active = ((_td_sell_combo_count(close, high) > 0)).astype(float)
    cd_active = ((_td_sell_countdown_count(close, high, low) > 0)).astype(float)
    return (cb_active * cd_active).where(cb_active.notna() & cd_active.notna(), np.nan)


def f34_tdsq_109_combo_completion_at_252d_high_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when TD Combo-13 fires AND close within 1% of 252d max."""
    cb = _td_sell_combo_count(close, high)
    fire = ((cb == 13) & (cb.shift(1) < 13)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan)


def f34_tdsq_110_aggressive_vs_standard_countdown_gap(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Aggressive-countdown count minus standard sell-countdown count (positive = aggressive ahead)."""
    from_helper_agg_state = _td_aggressive_helper_inline(close, high)
    return from_helper_agg_state - _td_sell_countdown_count(close, high, low)


def _td_aggressive_helper_inline(close: pd.Series, high: pd.Series) -> pd.Series:
    """Aggressive sell countdown (high vs high[t-2]) — inline duplicate of family-001-075's helper."""
    sc = _td_sell_setup_count(close).values
    bc = _td_buy_setup_count(close).values
    hi = high.values
    n = len(close)
    out = np.zeros(n)
    active = False; cnt = 0
    for i in range(n):
        if not active and i >= 8 and sc[i] >= 9:
            active = True; cnt = 0
        if active and i >= 8 and bc[i] >= 9:
            active = False; cnt = 0
        if active:
            if i >= 2 and hi[i] >= hi[i - 2] and cnt < 13:
                cnt += 1
            out[i] = cnt
    return pd.Series(out, index=close.index)


# ============================================================
# Bucket L — Time-since-event composites (111-120)
# ============================================================

def f34_tdsq_111_bars_since_setup_9_normalized_252d(close: pd.Series) -> pd.Series:
    """bars-since-setup-9 / 252 — normalized age (≥1 = older than a year)."""
    fires = (_td_sell_setup_count(close) == 9).astype(float)
    return _bars_since_true(fires) / float(YDAYS)


def f34_tdsq_112_bars_since_combo_13_normalized_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """bars-since-combo-13 / 252."""
    cb = _td_sell_combo_count(close, high)
    fire = ((cb == 13) & (cb.shift(1) < 13)).astype(float)
    return _bars_since_true(fire) / float(YDAYS)


def f34_tdsq_113_bars_since_camouflage_normalized_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """bars-since-camouflage / 252."""
    f = _td_camouflage_event(open, close, high, low)
    return _bars_since_true(f) / float(YDAYS)


def f34_tdsq_114_bars_since_trap_normalized_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """bars-since-trap / 252."""
    return _bars_since_true(_td_trap_event(close, high)) / float(YDAYS)


def f34_tdsq_115_bars_since_open_up_gap_normalized_252d(open: pd.Series, high: pd.Series) -> pd.Series:
    """bars-since-open-up-gap / 252."""
    return _bars_since_true(_td_open_up_gap_event(open, high)) / float(YDAYS)


def f34_tdsq_116_min_bars_since_any_td_signal_5signals(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Minimum across 5 TD signals (setup-9 / combo-13 / camouflage / trap / open-up-gap) of bars-since."""
    s1 = _bars_since_true((_td_sell_setup_count(close) == 9).astype(float))
    cb = _td_sell_combo_count(close, high)
    s2 = _bars_since_true(((cb == 13) & (cb.shift(1) < 13)).astype(float))
    s3 = _bars_since_true(_td_camouflage_event(open, close, high, low))
    s4 = _bars_since_true(_td_trap_event(close, high))
    s5 = _bars_since_true(_td_open_up_gap_event(open, high))
    df = pd.concat([s1.rename("a"), s2.rename("b"), s3.rename("c"), s4.rename("d"), s5.rename("e")], axis=1)
    return df.min(axis=1)


def f34_tdsq_117_max_bars_since_any_td_signal_5signals(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum across same 5 TD signals — staleness of the least-recent signal."""
    s1 = _bars_since_true((_td_sell_setup_count(close) == 9).astype(float))
    cb = _td_sell_combo_count(close, high)
    s2 = _bars_since_true(((cb == 13) & (cb.shift(1) < 13)).astype(float))
    s3 = _bars_since_true(_td_camouflage_event(open, close, high, low))
    s4 = _bars_since_true(_td_trap_event(close, high))
    s5 = _bars_since_true(_td_open_up_gap_event(open, high))
    df = pd.concat([s1.rename("a"), s2.rename("b"), s3.rename("c"), s4.rename("d"), s5.rename("e")], axis=1)
    return df.max(axis=1)


def f34_tdsq_118_count_td_signals_active_within_21d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count (0..5) of 5 TD signals whose last fire is within trailing 21d."""
    s1 = _bars_since_true((_td_sell_setup_count(close) == 9).astype(float))
    cb = _td_sell_combo_count(close, high)
    s2 = _bars_since_true(((cb == 13) & (cb.shift(1) < 13)).astype(float))
    s3 = _bars_since_true(_td_camouflage_event(open, close, high, low))
    s4 = _bars_since_true(_td_trap_event(close, high))
    s5 = _bars_since_true(_td_open_up_gap_event(open, high))
    df = pd.concat([(s1 <= MDAYS).astype(float).rename("a"),
                    (s2 <= MDAYS).astype(float).rename("b"),
                    (s3 <= MDAYS).astype(float).rename("c"),
                    (s4 <= MDAYS).astype(float).rename("d"),
                    (s5 <= MDAYS).astype(float).rename("e")], axis=1)
    return df.sum(axis=1)


def f34_tdsq_119_count_td_signals_active_within_63d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 5 TD signals whose last fire is within trailing 63d."""
    s1 = _bars_since_true((_td_sell_setup_count(close) == 9).astype(float))
    cb = _td_sell_combo_count(close, high)
    s2 = _bars_since_true(((cb == 13) & (cb.shift(1) < 13)).astype(float))
    s3 = _bars_since_true(_td_camouflage_event(open, close, high, low))
    s4 = _bars_since_true(_td_trap_event(close, high))
    s5 = _bars_since_true(_td_open_up_gap_event(open, high))
    df = pd.concat([(s1 <= QDAYS).astype(float).rename("a"),
                    (s2 <= QDAYS).astype(float).rename("b"),
                    (s3 <= QDAYS).astype(float).rename("c"),
                    (s4 <= QDAYS).astype(float).rename("d"),
                    (s5 <= QDAYS).astype(float).rename("e")], axis=1)
    return df.sum(axis=1)


def f34_tdsq_120_td_signal_density_event_count_252d_5signals(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Total raw event count across 5 TD bearish signals in trailing 252d."""
    s1 = (_td_sell_setup_count(close) == 9).astype(float).fillna(0)
    cb = _td_sell_combo_count(close, high)
    s2 = ((cb == 13) & (cb.shift(1) < 13)).astype(float).fillna(0)
    s3 = _td_camouflage_event(open, close, high, low).fillna(0)
    s4 = _td_trap_event(close, high).fillna(0)
    s5 = _td_open_up_gap_event(open, high).fillna(0)
    total = s1 + s2 + s3 + s4 + s5
    return total.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket M — Setup × volume/range conjunctions (121-130)
# ============================================================

def f34_tdsq_121_setup_9_x_high_volume_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 fires AND volume z-score(63) > 1."""
    fire = (_td_sell_setup_count(close) == 9).astype(float)
    vz = _rolling_zscore(volume, QDAYS)
    return ((fire == 1) & (vz > 1.0)).astype(float).where(fire.notna() & vz.notna(), np.nan)


def f34_tdsq_122_setup_9_x_low_volume_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 fires AND volume z-score(63) < -0.5 (suspect failure on no volume)."""
    fire = (_td_sell_setup_count(close) == 9).astype(float)
    vz = _rolling_zscore(volume, QDAYS)
    return ((fire == 1) & (vz < -0.5)).astype(float).where(fire.notna() & vz.notna(), np.nan)


def f34_tdsq_123_setup_9_x_atr_expansion_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 fires AND ATR(21) > 1.5 × ATR(252) (volatility-expansion regime)."""
    fire = (_td_sell_setup_count(close) == 9).astype(float)
    a21 = _atr(high, low, close, MDAYS)
    a252 = _atr(high, low, close, YDAYS)
    expand = (a21 > 1.5 * a252).astype(float)
    return (fire * expand).where(fire.notna() & expand.notna(), np.nan)


def f34_tdsq_124_setup_9_at_wide_range_bar_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 fires AND today's range is in trailing 252d top decile."""
    fire = (_td_sell_setup_count(close) == 9).astype(float)
    rng = high - low
    rng_rank = _pct_rank(rng, YDAYS)
    return ((fire == 1) & (rng_rank >= 0.9)).astype(float).where(fire.notna() & rng_rank.notna(), np.nan)


def f34_tdsq_125_countdown_13_x_high_volume_indicator(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when sell-countdown-13 fires AND volume z(63) > 1."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    vz = _rolling_zscore(volume, QDAYS)
    return ((fire == 1) & (vz > 1.0)).astype(float).where(fire.notna() & vz.notna(), np.nan)


def f34_tdsq_126_setup_9_x_dollar_vol_top_decile_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 fires AND dollar volume in 252d top decile (high-impact setup)."""
    fire = (_td_sell_setup_count(close) == 9).astype(float)
    dvol = close * volume
    dr = _pct_rank(dvol, YDAYS)
    return ((fire == 1) & (dr >= 0.9)).astype(float).where(fire.notna() & dr.notna(), np.nan)


def f34_tdsq_127_perfected_setup_9_x_high_volume_indicator(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when perfected sell-setup-9 AND vol-z(63) > 1."""
    pf = _td_perfected_sell_setup_9_event(close, high)
    vz = _rolling_zscore(volume, QDAYS)
    return ((pf == 1) & (vz > 1.0)).astype(float).where(pf.notna() & vz.notna(), np.nan)


def f34_tdsq_128_setup_9_x_close_in_top_decile_of_5d_range_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 fires AND close in top decile of 5d high-low range — failure-of-thrust ahead."""
    fire = (_td_sell_setup_count(close) == 9).astype(float)
    hh = high.rolling(WDAYS, min_periods=1).max(); ll = low.rolling(WDAYS, min_periods=1).min()
    pos = _safe_div(close - ll, hh - ll)
    return ((fire == 1) & (pos >= 0.9)).astype(float).where(fire.notna() & pos.notna(), np.nan)


def f34_tdsq_129_setup_9_x_atr_ratio_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Magnitude: at setup-9 bar, z-score of ATR21/ATR252 (held forward) — vol-regime at setup."""
    fire = (_td_sell_setup_count(close) == 9).astype(float)
    a21 = _atr(high, low, close, MDAYS); a252 = _atr(high, low, close, YDAYS)
    z = _rolling_zscore(_safe_div(a21, a252), YDAYS)
    return z.where(fire == 1, np.nan).ffill()


def f34_tdsq_130_setup_9_with_recent_3d_volume_surge_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when sell-setup-9 fires AND 3d volume sum > 2× trailing-21d mean."""
    fire = (_td_sell_setup_count(close) == 9).astype(float)
    v3 = volume.rolling(3, min_periods=1).sum()
    v21mean = volume.rolling(MDAYS, min_periods=WDAYS).mean() * 3.0
    surge = (v3 > 2.0 * v21mean).astype(float)
    return (fire * surge).where(fire.notna() & surge.notna(), np.nan)


# ============================================================
# Bucket N — At-multi-year-high TD-signal conjunctions (131-140)
# ============================================================

def f34_tdsq_131_setup_9_x_1260d_high_x_perfected_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when perfected sell-setup-9 AND close within 2% of 1260d max."""
    pf = _td_perfected_sell_setup_9_event(close, high)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (pf * near).where(pf.notna() & near.notna(), np.nan)


def f34_tdsq_132_countdown_13_x_252d_high_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when sell-countdown-13 fires AND close within 1% of 252d max."""
    cd = _td_sell_countdown_count(close, high, low)
    fire = ((cd == 13) & (cd.shift(1) < 13)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan)


def f34_tdsq_133_combo_13_x_252d_high_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when TD Combo-13 fires AND close within 1% of 252d max."""
    cb = _td_sell_combo_count(close, high)
    fire = ((cb == 13) & (cb.shift(1) < 13)).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan)


def f34_tdsq_134_trap_x_252d_high_indicator(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when TD Trap fires AND close within 1% of 252d max."""
    fire = _td_trap_event(close, high)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan)


def f34_tdsq_135_open_up_gap_x_1260d_high_indicator(open: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """+1 when TD Open-Up-Gap fires AND close within 2% of 1260d max (gap-up exhaustion at secular high)."""
    fire = _td_open_up_gap_event(open, high)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan)


def f34_tdsq_136_rei_overbought_x_252d_high_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when TD REI > 60 AND close within 1% of 252d max."""
    r = _td_rei(close, high, low, 5)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((r > 60) & (near == 1)).astype(float).where(r.notna() & near.notna(), np.nan)


def f34_tdsq_137_camouflage_x_252d_high_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when bearish TD Camouflage fires AND close within 1% of 252d max."""
    fire = _td_camouflage_event(open, close, high, low)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan)


def f34_tdsq_138_differential_bearish_x_252d_high_indicator(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when bearish TD Differential fires AND close within 1% of 252d max."""
    fire = _td_differential_bearish_event(close, high, low)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (fire * near).where(fire.notna() & near.notna(), np.nan)


def f34_tdsq_139_count_5_td_signals_at_252d_high_in_21d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 5 TD signals that fired AT a 252d-high bar within last 21d."""
    near_flag = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    s1 = ((_td_sell_setup_count(close) == 9).astype(float) * near_flag).fillna(0)
    cb = _td_sell_combo_count(close, high)
    s2 = (((cb == 13) & (cb.shift(1) < 13)).astype(float) * near_flag).fillna(0)
    s3 = (_td_camouflage_event(open, close, high, low) * near_flag).fillna(0)
    s4 = (_td_trap_event(close, high) * near_flag).fillna(0)
    s5 = (_td_open_up_gap_event(open, high) * near_flag).fillna(0)
    total = s1 + s2 + s3 + s4 + s5
    return total.rolling(MDAYS, min_periods=WDAYS).sum()


def f34_tdsq_140_total_td_bearish_signals_at_high_252d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Total raw TD bearish signal events (5 signals) AT 252d-high bars, in trailing 252d."""
    near_flag = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    s1 = ((_td_sell_setup_count(close) == 9).astype(float) * near_flag).fillna(0)
    cb = _td_sell_combo_count(close, high)
    s2 = (((cb == 13) & (cb.shift(1) < 13)).astype(float) * near_flag).fillna(0)
    s3 = (_td_camouflage_event(open, close, high, low) * near_flag).fillna(0)
    s4 = (_td_trap_event(close, high) * near_flag).fillna(0)
    s5 = (_td_open_up_gap_event(open, high) * near_flag).fillna(0)
    total = s1 + s2 + s3 + s4 + s5
    return total.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket O — TD weighted composites (141-150)
# ============================================================

def f34_tdsq_141_td_topping_score_weighted_composite(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Weighted: 0.30*z(setup-9-count,252) + 0.25*z(combo-13-count,252)
    + 0.25*z(rei-overbought-count,252) + 0.20*close-pct-rank-1260d."""
    s9_cnt = (_td_sell_setup_count(close) == 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    cb = _td_sell_combo_count(close, high)
    c13_cnt = ((cb == 13) & (cb.shift(1) < 13)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    r = _td_rei(close, high, low, 5)
    rei_cnt = (r > 60).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    px_rank = _pct_rank(close, DDAYS_5Y)
    return (0.30 * _rolling_zscore(s9_cnt, YDAYS)
            + 0.25 * _rolling_zscore(c13_cnt, YDAYS)
            + 0.25 * _rolling_zscore(rei_cnt, YDAYS)
            + 0.20 * px_rank)


def f34_tdsq_142_td_topping_score_bar_pattern_weighted(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Weighted: 0.4*camouflage-252d + 0.3*trap-252d + 0.3*differential-252d (all z-scored)."""
    cam = _td_camouflage_event(open, close, high, low).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()
    trp = _td_trap_event(close, high).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()
    dif = _td_differential_bearish_event(close, high, low).fillna(0).rolling(YDAYS, min_periods=QDAYS).sum()
    return (0.4 * _rolling_zscore(cam, YDAYS)
            + 0.3 * _rolling_zscore(trp, YDAYS)
            + 0.3 * _rolling_zscore(dif, YDAYS))


def f34_tdsq_143_td_combined_topping_score_all_signals(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average of f34_tdsq_141 and f34_tdsq_142 — combined sequential+pattern topping score."""
    a = f34_tdsq_141_td_topping_score_weighted_composite(close, high, low)
    b = f34_tdsq_142_td_topping_score_bar_pattern_weighted(open, close, high, low)
    return 0.5 * a + 0.5 * b


def f34_tdsq_144_td_pressure_x_setup_active_composite(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """TD pressure × (sell-setup-count / 9) — pressure-modulated by setup-progress."""
    pr = _td_pressure(open, close, high, low, 13)
    sc = _td_sell_setup_count(close) / 9.0
    return pr * sc


def f34_tdsq_145_td_setup_intensity_index_252d(close: pd.Series) -> pd.Series:
    """Mean of (sell-setup-count / 9) over trailing 252d — secular setup intensity."""
    return (_td_sell_setup_count(close) / 9.0).rolling(YDAYS, min_periods=QDAYS).mean()


def f34_tdsq_146_ratio_setup9_completed_vs_inprogress_504d(close: pd.Series) -> pd.Series:
    """Ratio: trailing-504d sell-setup-9 fires divided by trailing-504d count of bars at count ≥ 5."""
    sc = _td_sell_setup_count(close)
    fires = (sc == 9).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    inprog = (sc >= 5).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()
    return _safe_div(fires, inprog)


def f34_tdsq_147_td_demark_breadth_4signals_active_in_5d_x_at_high_indicator(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when at least 2 of {setup-9, combo-13, trap, camouflage} fired in last 5 bars AND close near 252d high."""
    s1 = ((_td_sell_setup_count(close) == 9).astype(float).rolling(WDAYS, min_periods=1).max())
    cb = _td_sell_combo_count(close, high)
    s2 = (((cb == 13) & (cb.shift(1) < 13)).astype(float).rolling(WDAYS, min_periods=1).max())
    s3 = (_td_trap_event(close, high).fillna(0).rolling(WDAYS, min_periods=1).max())
    s4 = (_td_camouflage_event(open, close, high, low).fillna(0).rolling(WDAYS, min_periods=1).max())
    cnt = (s1.fillna(0) + s2.fillna(0) + s3.fillna(0) + s4.fillna(0))
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((cnt >= 2) & (near == 1)).astype(float).where(cnt.notna() & near.notna(), np.nan)


def f34_tdsq_148_td_signal_correlation_with_252d_high_zscore(close: pd.Series) -> pd.Series:
    """Rolling 252d correlation between sell-setup-count and (close/252d-max) — high = setup count rises with stretch."""
    sc = _td_sell_setup_count(close)
    rel = _safe_div(close, close.rolling(YDAYS, min_periods=QDAYS).max())
    return sc.rolling(YDAYS, min_periods=QDAYS).corr(rel)


def f34_tdsq_149_td_signal_pyramid_score_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Pyramid: 1×setup-9 + 2×combo-13 + 3×countdown-13 events in trailing 252d, normalized by 252.
    Heavier weights on later-stage sequential completions."""
    s9 = (_td_sell_setup_count(close) == 9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    cb = _td_sell_combo_count(close, high)
    c13 = ((cb == 13) & (cb.shift(1) < 13)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    cd = _td_sell_countdown_count(close, high, low)
    cdfire = ((cd == 13) & (cd.shift(1) < 13)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return (1.0 * s9 + 2.0 * c13 + 3.0 * cdfire) / float(YDAYS)


def f34_tdsq_150_td_full_demark_topping_master_index(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Master DeMark topping index: 0.4*f34_tdsq_143 + 0.3*f34_tdsq_144(z) + 0.3*f34_tdsq_149(z)."""
    a = f34_tdsq_143_td_combined_topping_score_all_signals(open, close, high, low)
    b = _rolling_zscore(f34_tdsq_144_td_pressure_x_setup_active_composite(open, close, high, low), YDAYS)
    c = _rolling_zscore(f34_tdsq_149_td_signal_pyramid_score_252d(close, high, low), YDAYS)
    return 0.4 * a + 0.3 * b + 0.3 * c


# ============================================================
# REGISTRY
# ============================================================



def f34_tdsq_076_td_rei_value_5d_d1(close, high, low):
    return f34_tdsq_076_td_rei_value_5d(close, high, low).diff()


def f34_tdsq_077_td_rei_overbought_indicator_d1(close, high, low):
    return f34_tdsq_077_td_rei_overbought_indicator(close, high, low).diff()


def f34_tdsq_078_td_rei_pct_rank_252d_d1(close, high, low):
    return f34_tdsq_078_td_rei_pct_rank_252d(close, high, low).diff()


def f34_tdsq_079_td_rei_zscore_252d_d1(close, high, low):
    return f34_tdsq_079_td_rei_zscore_252d(close, high, low).diff()


def f34_tdsq_080_td_rei_slope_21d_d1(close, high, low):
    return f34_tdsq_080_td_rei_slope_21d(close, high, low).diff()


def f34_tdsq_081_days_since_td_rei_above_60_d1(close, high, low):
    return f34_tdsq_081_days_since_td_rei_above_60(close, high, low).diff()


def f34_tdsq_082_td_rei_persistence_above_60_21d_d1(close, high, low):
    return f34_tdsq_082_td_rei_persistence_above_60_21d(close, high, low).diff()


def f34_tdsq_083_td_rei_count_above_60_252d_d1(close, high, low):
    return f34_tdsq_083_td_rei_count_above_60_252d(close, high, low).diff()


def f34_tdsq_084_td_rei_top_to_breakdown_velocity_d1(close, high, low):
    return f34_tdsq_084_td_rei_top_to_breakdown_velocity(close, high, low).diff()


def f34_tdsq_085_td_rei_overbought_x_close_at_252d_high_indicator_d1(close, high, low):
    return f34_tdsq_085_td_rei_overbought_x_close_at_252d_high_indicator(close, high, low).diff()


def f34_tdsq_086_td_demand_level_last_sell_setup_lowest_low_d1(close, low):
    return f34_tdsq_086_td_demand_level_last_sell_setup_lowest_low(close, low).diff()


def f34_tdsq_087_td_supply_level_last_buy_setup_highest_high_d1(close, high):
    return f34_tdsq_087_td_supply_level_last_buy_setup_highest_high(close, high).diff()


def f34_tdsq_088_close_below_td_demand_indicator_d1(close, low):
    return f34_tdsq_088_close_below_td_demand_indicator(close, low).diff()


def f34_tdsq_089_close_distance_to_td_supply_atr_norm_d1(close, high, low):
    return f34_tdsq_089_close_distance_to_td_supply_atr_norm(close, high, low).diff()


def f34_tdsq_090_close_below_td_demand_event_indicator_d1(close, low):
    return f34_tdsq_090_close_below_td_demand_event_indicator(close, low).diff()


def f34_tdsq_091_td_camouflage_bearish_event_indicator_d1(open, close, high, low):
    return f34_tdsq_091_td_camouflage_bearish_event_indicator(open, close, high, low).diff()


def f34_tdsq_092_td_camouflage_count_252d_d1(open, close, high, low):
    return f34_tdsq_092_td_camouflage_count_252d(open, close, high, low).diff()


def f34_tdsq_093_td_open_up_gap_event_indicator_d1(open, high):
    return f34_tdsq_093_td_open_up_gap_event_indicator(open, high).diff()


def f34_tdsq_094_td_open_up_gap_count_252d_d1(open, high):
    return f34_tdsq_094_td_open_up_gap_count_252d(open, high).diff()


def f34_tdsq_095_td_trap_event_indicator_d1(close, high):
    return f34_tdsq_095_td_trap_event_indicator(close, high).diff()


def f34_tdsq_096_td_trap_count_63d_d1(close, high):
    return f34_tdsq_096_td_trap_count_63d(close, high).diff()


def f34_tdsq_097_td_trap_count_252d_d1(close, high):
    return f34_tdsq_097_td_trap_count_252d(close, high).diff()


def f34_tdsq_098_td_differential_bearish_event_indicator_d1(close, high, low):
    return f34_tdsq_098_td_differential_bearish_event_indicator(close, high, low).diff()


def f34_tdsq_099_td_differential_bearish_count_252d_d1(close, high, low):
    return f34_tdsq_099_td_differential_bearish_count_252d(close, high, low).diff()


def f34_tdsq_100_td_bar_pattern_breadth_4indicators_indicator_d1(open, close, high, low):
    return f34_tdsq_100_td_bar_pattern_breadth_4indicators_indicator(open, close, high, low).diff()


def f34_tdsq_101_td_sell_combo_count_current_d1(close, high):
    return f34_tdsq_101_td_sell_combo_count_current(close, high).diff()


def f34_tdsq_102_td_sell_combo_13_fires_indicator_d1(close, high):
    return f34_tdsq_102_td_sell_combo_13_fires_indicator(close, high).diff()


def f34_tdsq_103_days_since_td_sell_combo_13_d1(close, high):
    return f34_tdsq_103_days_since_td_sell_combo_13(close, high).diff()


def f34_tdsq_104_count_td_sell_combo_13_in_252d_d1(close, high):
    return f34_tdsq_104_count_td_sell_combo_13_in_252d(close, high).diff()


def f34_tdsq_105_td_combo_active_indicator_d1(close, high):
    return f34_tdsq_105_td_combo_active_indicator(close, high).diff()


def f34_tdsq_106_td_combo_progress_pct_d1(close, high):
    return f34_tdsq_106_td_combo_progress_pct(close, high).diff()


def f34_tdsq_107_td_sell_combo_max_252d_d1(close, high):
    return f34_tdsq_107_td_sell_combo_max_252d(close, high).diff()


def f34_tdsq_108_td_combo_vs_countdown_agreement_indicator_d1(close, high, low):
    return f34_tdsq_108_td_combo_vs_countdown_agreement_indicator(close, high, low).diff()


def f34_tdsq_109_combo_completion_at_252d_high_indicator_d1(close, high):
    return f34_tdsq_109_combo_completion_at_252d_high_indicator(close, high).diff()


def f34_tdsq_110_aggressive_vs_standard_countdown_gap_d1(close, high, low):
    return f34_tdsq_110_aggressive_vs_standard_countdown_gap(close, high, low).diff()


def f34_tdsq_111_bars_since_setup_9_normalized_252d_d1(close):
    return f34_tdsq_111_bars_since_setup_9_normalized_252d(close).diff()


def f34_tdsq_112_bars_since_combo_13_normalized_252d_d1(close, high):
    return f34_tdsq_112_bars_since_combo_13_normalized_252d(close, high).diff()


def f34_tdsq_113_bars_since_camouflage_normalized_252d_d1(open, close, high, low):
    return f34_tdsq_113_bars_since_camouflage_normalized_252d(open, close, high, low).diff()


def f34_tdsq_114_bars_since_trap_normalized_252d_d1(close, high):
    return f34_tdsq_114_bars_since_trap_normalized_252d(close, high).diff()


def f34_tdsq_115_bars_since_open_up_gap_normalized_252d_d1(open, high):
    return f34_tdsq_115_bars_since_open_up_gap_normalized_252d(open, high).diff()


def f34_tdsq_116_min_bars_since_any_td_signal_5signals_d1(open, close, high, low):
    return f34_tdsq_116_min_bars_since_any_td_signal_5signals(open, close, high, low).diff()


def f34_tdsq_117_max_bars_since_any_td_signal_5signals_d1(open, close, high, low):
    return f34_tdsq_117_max_bars_since_any_td_signal_5signals(open, close, high, low).diff()


def f34_tdsq_118_count_td_signals_active_within_21d_d1(open, close, high, low):
    return f34_tdsq_118_count_td_signals_active_within_21d(open, close, high, low).diff()


def f34_tdsq_119_count_td_signals_active_within_63d_d1(open, close, high, low):
    return f34_tdsq_119_count_td_signals_active_within_63d(open, close, high, low).diff()


def f34_tdsq_120_td_signal_density_event_count_252d_5signals_d1(open, close, high, low):
    return f34_tdsq_120_td_signal_density_event_count_252d_5signals(open, close, high, low).diff()


def f34_tdsq_121_setup_9_x_high_volume_indicator_d1(close, volume):
    return f34_tdsq_121_setup_9_x_high_volume_indicator(close, volume).diff()


def f34_tdsq_122_setup_9_x_low_volume_indicator_d1(close, volume):
    return f34_tdsq_122_setup_9_x_low_volume_indicator(close, volume).diff()


def f34_tdsq_123_setup_9_x_atr_expansion_indicator_d1(close, high, low):
    return f34_tdsq_123_setup_9_x_atr_expansion_indicator(close, high, low).diff()


def f34_tdsq_124_setup_9_at_wide_range_bar_indicator_d1(close, high, low):
    return f34_tdsq_124_setup_9_at_wide_range_bar_indicator(close, high, low).diff()


def f34_tdsq_125_countdown_13_x_high_volume_indicator_d1(close, high, low, volume):
    return f34_tdsq_125_countdown_13_x_high_volume_indicator(close, high, low, volume).diff()


def f34_tdsq_126_setup_9_x_dollar_vol_top_decile_indicator_d1(close, volume):
    return f34_tdsq_126_setup_9_x_dollar_vol_top_decile_indicator(close, volume).diff()


def f34_tdsq_127_perfected_setup_9_x_high_volume_indicator_d1(close, high, volume):
    return f34_tdsq_127_perfected_setup_9_x_high_volume_indicator(close, high, volume).diff()


def f34_tdsq_128_setup_9_x_close_in_top_decile_of_5d_range_indicator_d1(close, high, low):
    return f34_tdsq_128_setup_9_x_close_in_top_decile_of_5d_range_indicator(close, high, low).diff()


def f34_tdsq_129_setup_9_x_atr_ratio_zscore_252d_d1(close, high, low):
    return f34_tdsq_129_setup_9_x_atr_ratio_zscore_252d(close, high, low).diff()


def f34_tdsq_130_setup_9_with_recent_3d_volume_surge_indicator_d1(close, volume):
    return f34_tdsq_130_setup_9_with_recent_3d_volume_surge_indicator(close, volume).diff()


def f34_tdsq_131_setup_9_x_1260d_high_x_perfected_indicator_d1(close, high):
    return f34_tdsq_131_setup_9_x_1260d_high_x_perfected_indicator(close, high).diff()


def f34_tdsq_132_countdown_13_x_252d_high_indicator_d1(close, high, low):
    return f34_tdsq_132_countdown_13_x_252d_high_indicator(close, high, low).diff()


def f34_tdsq_133_combo_13_x_252d_high_indicator_d1(close, high):
    return f34_tdsq_133_combo_13_x_252d_high_indicator(close, high).diff()


def f34_tdsq_134_trap_x_252d_high_indicator_d1(close, high):
    return f34_tdsq_134_trap_x_252d_high_indicator(close, high).diff()


def f34_tdsq_135_open_up_gap_x_1260d_high_indicator_d1(open, high, close):
    return f34_tdsq_135_open_up_gap_x_1260d_high_indicator(open, high, close).diff()


def f34_tdsq_136_rei_overbought_x_252d_high_indicator_d1(close, high, low):
    return f34_tdsq_136_rei_overbought_x_252d_high_indicator(close, high, low).diff()


def f34_tdsq_137_camouflage_x_252d_high_indicator_d1(open, close, high, low):
    return f34_tdsq_137_camouflage_x_252d_high_indicator(open, close, high, low).diff()


def f34_tdsq_138_differential_bearish_x_252d_high_indicator_d1(close, high, low):
    return f34_tdsq_138_differential_bearish_x_252d_high_indicator(close, high, low).diff()


def f34_tdsq_139_count_5_td_signals_at_252d_high_in_21d_d1(open, close, high, low):
    return f34_tdsq_139_count_5_td_signals_at_252d_high_in_21d(open, close, high, low).diff()


def f34_tdsq_140_total_td_bearish_signals_at_high_252d_d1(open, close, high, low):
    return f34_tdsq_140_total_td_bearish_signals_at_high_252d(open, close, high, low).diff()


def f34_tdsq_141_td_topping_score_weighted_composite_d1(close, high, low):
    return f34_tdsq_141_td_topping_score_weighted_composite(close, high, low).diff()


def f34_tdsq_142_td_topping_score_bar_pattern_weighted_d1(open, close, high, low):
    return f34_tdsq_142_td_topping_score_bar_pattern_weighted(open, close, high, low).diff()


def f34_tdsq_143_td_combined_topping_score_all_signals_d1(open, close, high, low):
    return f34_tdsq_143_td_combined_topping_score_all_signals(open, close, high, low).diff()


def f34_tdsq_144_td_pressure_x_setup_active_composite_d1(open, close, high, low):
    return f34_tdsq_144_td_pressure_x_setup_active_composite(open, close, high, low).diff()


def f34_tdsq_145_td_setup_intensity_index_252d_d1(close):
    return f34_tdsq_145_td_setup_intensity_index_252d(close).diff()


def f34_tdsq_146_ratio_setup9_completed_vs_inprogress_504d_d1(close):
    return f34_tdsq_146_ratio_setup9_completed_vs_inprogress_504d(close).diff()


def f34_tdsq_147_td_demark_breadth_4signals_active_in_5d_x_at_high_indicator_d1(open, close, high, low):
    return f34_tdsq_147_td_demark_breadth_4signals_active_in_5d_x_at_high_indicator(open, close, high, low).diff()


def f34_tdsq_148_td_signal_correlation_with_252d_high_zscore_d1(close):
    return f34_tdsq_148_td_signal_correlation_with_252d_high_zscore(close).diff()


def f34_tdsq_149_td_signal_pyramid_score_252d_d1(close, high, low):
    return f34_tdsq_149_td_signal_pyramid_score_252d(close, high, low).diff()


def f34_tdsq_150_td_full_demark_topping_master_index_d1(open, close, high, low):
    return f34_tdsq_150_td_full_demark_topping_master_index(open, close, high, low).diff()


TD_SEQUENTIAL_DEMARK_D1_REGISTRY_076_150 = {
    "f34_tdsq_076_td_rei_value_5d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_076_td_rei_value_5d_d1},
    "f34_tdsq_077_td_rei_overbought_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_077_td_rei_overbought_indicator_d1},
    "f34_tdsq_078_td_rei_pct_rank_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_078_td_rei_pct_rank_252d_d1},
    "f34_tdsq_079_td_rei_zscore_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_079_td_rei_zscore_252d_d1},
    "f34_tdsq_080_td_rei_slope_21d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_080_td_rei_slope_21d_d1},
    "f34_tdsq_081_days_since_td_rei_above_60_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_081_days_since_td_rei_above_60_d1},
    "f34_tdsq_082_td_rei_persistence_above_60_21d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_082_td_rei_persistence_above_60_21d_d1},
    "f34_tdsq_083_td_rei_count_above_60_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_083_td_rei_count_above_60_252d_d1},
    "f34_tdsq_084_td_rei_top_to_breakdown_velocity_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_084_td_rei_top_to_breakdown_velocity_d1},
    "f34_tdsq_085_td_rei_overbought_x_close_at_252d_high_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_085_td_rei_overbought_x_close_at_252d_high_indicator_d1},
    "f34_tdsq_086_td_demand_level_last_sell_setup_lowest_low_d1": {"inputs": ["close", "low"], "func": f34_tdsq_086_td_demand_level_last_sell_setup_lowest_low_d1},
    "f34_tdsq_087_td_supply_level_last_buy_setup_highest_high_d1": {"inputs": ["close", "high"], "func": f34_tdsq_087_td_supply_level_last_buy_setup_highest_high_d1},
    "f34_tdsq_088_close_below_td_demand_indicator_d1": {"inputs": ["close", "low"], "func": f34_tdsq_088_close_below_td_demand_indicator_d1},
    "f34_tdsq_089_close_distance_to_td_supply_atr_norm_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_089_close_distance_to_td_supply_atr_norm_d1},
    "f34_tdsq_090_close_below_td_demand_event_indicator_d1": {"inputs": ["close", "low"], "func": f34_tdsq_090_close_below_td_demand_event_indicator_d1},
    "f34_tdsq_091_td_camouflage_bearish_event_indicator_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_091_td_camouflage_bearish_event_indicator_d1},
    "f34_tdsq_092_td_camouflage_count_252d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_092_td_camouflage_count_252d_d1},
    "f34_tdsq_093_td_open_up_gap_event_indicator_d1": {"inputs": ["open", "high"], "func": f34_tdsq_093_td_open_up_gap_event_indicator_d1},
    "f34_tdsq_094_td_open_up_gap_count_252d_d1": {"inputs": ["open", "high"], "func": f34_tdsq_094_td_open_up_gap_count_252d_d1},
    "f34_tdsq_095_td_trap_event_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_095_td_trap_event_indicator_d1},
    "f34_tdsq_096_td_trap_count_63d_d1": {"inputs": ["close", "high"], "func": f34_tdsq_096_td_trap_count_63d_d1},
    "f34_tdsq_097_td_trap_count_252d_d1": {"inputs": ["close", "high"], "func": f34_tdsq_097_td_trap_count_252d_d1},
    "f34_tdsq_098_td_differential_bearish_event_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_098_td_differential_bearish_event_indicator_d1},
    "f34_tdsq_099_td_differential_bearish_count_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_099_td_differential_bearish_count_252d_d1},
    "f34_tdsq_100_td_bar_pattern_breadth_4indicators_indicator_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_100_td_bar_pattern_breadth_4indicators_indicator_d1},
    "f34_tdsq_101_td_sell_combo_count_current_d1": {"inputs": ["close", "high"], "func": f34_tdsq_101_td_sell_combo_count_current_d1},
    "f34_tdsq_102_td_sell_combo_13_fires_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_102_td_sell_combo_13_fires_indicator_d1},
    "f34_tdsq_103_days_since_td_sell_combo_13_d1": {"inputs": ["close", "high"], "func": f34_tdsq_103_days_since_td_sell_combo_13_d1},
    "f34_tdsq_104_count_td_sell_combo_13_in_252d_d1": {"inputs": ["close", "high"], "func": f34_tdsq_104_count_td_sell_combo_13_in_252d_d1},
    "f34_tdsq_105_td_combo_active_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_105_td_combo_active_indicator_d1},
    "f34_tdsq_106_td_combo_progress_pct_d1": {"inputs": ["close", "high"], "func": f34_tdsq_106_td_combo_progress_pct_d1},
    "f34_tdsq_107_td_sell_combo_max_252d_d1": {"inputs": ["close", "high"], "func": f34_tdsq_107_td_sell_combo_max_252d_d1},
    "f34_tdsq_108_td_combo_vs_countdown_agreement_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_108_td_combo_vs_countdown_agreement_indicator_d1},
    "f34_tdsq_109_combo_completion_at_252d_high_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_109_combo_completion_at_252d_high_indicator_d1},
    "f34_tdsq_110_aggressive_vs_standard_countdown_gap_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_110_aggressive_vs_standard_countdown_gap_d1},
    "f34_tdsq_111_bars_since_setup_9_normalized_252d_d1": {"inputs": ["close"], "func": f34_tdsq_111_bars_since_setup_9_normalized_252d_d1},
    "f34_tdsq_112_bars_since_combo_13_normalized_252d_d1": {"inputs": ["close", "high"], "func": f34_tdsq_112_bars_since_combo_13_normalized_252d_d1},
    "f34_tdsq_113_bars_since_camouflage_normalized_252d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_113_bars_since_camouflage_normalized_252d_d1},
    "f34_tdsq_114_bars_since_trap_normalized_252d_d1": {"inputs": ["close", "high"], "func": f34_tdsq_114_bars_since_trap_normalized_252d_d1},
    "f34_tdsq_115_bars_since_open_up_gap_normalized_252d_d1": {"inputs": ["open", "high"], "func": f34_tdsq_115_bars_since_open_up_gap_normalized_252d_d1},
    "f34_tdsq_116_min_bars_since_any_td_signal_5signals_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_116_min_bars_since_any_td_signal_5signals_d1},
    "f34_tdsq_117_max_bars_since_any_td_signal_5signals_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_117_max_bars_since_any_td_signal_5signals_d1},
    "f34_tdsq_118_count_td_signals_active_within_21d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_118_count_td_signals_active_within_21d_d1},
    "f34_tdsq_119_count_td_signals_active_within_63d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_119_count_td_signals_active_within_63d_d1},
    "f34_tdsq_120_td_signal_density_event_count_252d_5signals_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_120_td_signal_density_event_count_252d_5signals_d1},
    "f34_tdsq_121_setup_9_x_high_volume_indicator_d1": {"inputs": ["close", "volume"], "func": f34_tdsq_121_setup_9_x_high_volume_indicator_d1},
    "f34_tdsq_122_setup_9_x_low_volume_indicator_d1": {"inputs": ["close", "volume"], "func": f34_tdsq_122_setup_9_x_low_volume_indicator_d1},
    "f34_tdsq_123_setup_9_x_atr_expansion_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_123_setup_9_x_atr_expansion_indicator_d1},
    "f34_tdsq_124_setup_9_at_wide_range_bar_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_124_setup_9_at_wide_range_bar_indicator_d1},
    "f34_tdsq_125_countdown_13_x_high_volume_indicator_d1": {"inputs": ["close", "high", "low", "volume"], "func": f34_tdsq_125_countdown_13_x_high_volume_indicator_d1},
    "f34_tdsq_126_setup_9_x_dollar_vol_top_decile_indicator_d1": {"inputs": ["close", "volume"], "func": f34_tdsq_126_setup_9_x_dollar_vol_top_decile_indicator_d1},
    "f34_tdsq_127_perfected_setup_9_x_high_volume_indicator_d1": {"inputs": ["close", "high", "volume"], "func": f34_tdsq_127_perfected_setup_9_x_high_volume_indicator_d1},
    "f34_tdsq_128_setup_9_x_close_in_top_decile_of_5d_range_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_128_setup_9_x_close_in_top_decile_of_5d_range_indicator_d1},
    "f34_tdsq_129_setup_9_x_atr_ratio_zscore_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_129_setup_9_x_atr_ratio_zscore_252d_d1},
    "f34_tdsq_130_setup_9_with_recent_3d_volume_surge_indicator_d1": {"inputs": ["close", "volume"], "func": f34_tdsq_130_setup_9_with_recent_3d_volume_surge_indicator_d1},
    "f34_tdsq_131_setup_9_x_1260d_high_x_perfected_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_131_setup_9_x_1260d_high_x_perfected_indicator_d1},
    "f34_tdsq_132_countdown_13_x_252d_high_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_132_countdown_13_x_252d_high_indicator_d1},
    "f34_tdsq_133_combo_13_x_252d_high_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_133_combo_13_x_252d_high_indicator_d1},
    "f34_tdsq_134_trap_x_252d_high_indicator_d1": {"inputs": ["close", "high"], "func": f34_tdsq_134_trap_x_252d_high_indicator_d1},
    "f34_tdsq_135_open_up_gap_x_1260d_high_indicator_d1": {"inputs": ["open", "high", "close"], "func": f34_tdsq_135_open_up_gap_x_1260d_high_indicator_d1},
    "f34_tdsq_136_rei_overbought_x_252d_high_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_136_rei_overbought_x_252d_high_indicator_d1},
    "f34_tdsq_137_camouflage_x_252d_high_indicator_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_137_camouflage_x_252d_high_indicator_d1},
    "f34_tdsq_138_differential_bearish_x_252d_high_indicator_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_138_differential_bearish_x_252d_high_indicator_d1},
    "f34_tdsq_139_count_5_td_signals_at_252d_high_in_21d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_139_count_5_td_signals_at_252d_high_in_21d_d1},
    "f34_tdsq_140_total_td_bearish_signals_at_high_252d_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_140_total_td_bearish_signals_at_high_252d_d1},
    "f34_tdsq_141_td_topping_score_weighted_composite_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_141_td_topping_score_weighted_composite_d1},
    "f34_tdsq_142_td_topping_score_bar_pattern_weighted_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_142_td_topping_score_bar_pattern_weighted_d1},
    "f34_tdsq_143_td_combined_topping_score_all_signals_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_143_td_combined_topping_score_all_signals_d1},
    "f34_tdsq_144_td_pressure_x_setup_active_composite_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_144_td_pressure_x_setup_active_composite_d1},
    "f34_tdsq_145_td_setup_intensity_index_252d_d1": {"inputs": ["close"], "func": f34_tdsq_145_td_setup_intensity_index_252d_d1},
    "f34_tdsq_146_ratio_setup9_completed_vs_inprogress_504d_d1": {"inputs": ["close"], "func": f34_tdsq_146_ratio_setup9_completed_vs_inprogress_504d_d1},
    "f34_tdsq_147_td_demark_breadth_4signals_active_in_5d_x_at_high_indicator_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_147_td_demark_breadth_4signals_active_in_5d_x_at_high_indicator_d1},
    "f34_tdsq_148_td_signal_correlation_with_252d_high_zscore_d1": {"inputs": ["close"], "func": f34_tdsq_148_td_signal_correlation_with_252d_high_zscore_d1},
    "f34_tdsq_149_td_signal_pyramid_score_252d_d1": {"inputs": ["close", "high", "low"], "func": f34_tdsq_149_td_signal_pyramid_score_252d_d1},
    "f34_tdsq_150_td_full_demark_topping_master_index_d1": {"inputs": ["open", "close", "high", "low"], "func": f34_tdsq_150_td_full_demark_topping_master_index_d1},
}
