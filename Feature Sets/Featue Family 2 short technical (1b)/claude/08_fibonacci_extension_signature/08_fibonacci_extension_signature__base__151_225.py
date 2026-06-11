"""fibonacci_extension_signature base features 151-225 — Pipeline 1b-technical.

GAP-FILL extension to base 001-150. Each feature here encodes a DISTINCT
concept NOT covered by 001-150:

- Fibonacci RETRACEMENT levels (0.236 / 0.382 / 0.5 / 0.618 / 0.786 / 0.886)
  — pullback depth from swing high (001-150 only covered extension > 1.0)
- Harmonic patterns: Gartley, Butterfly, Bat, Crab, Cypher, Shark, 5-0 (XABCD)
  — canonical 5-pivot patterns with specific Fib-ratio validation
- Multi-anchor Fib confluence — count of distinct swing horizons whose Fib
  targets cluster near current price
- Bear-side / downward Fib extensions (high → low → further down)
- Fib time zones (8/13/21/34/55/89/144 bar intervals)
- Fib MA-anchored extensions (extension as N×ATR above SMA)
- Fib + volume confluence (volume profile at Fib zones)
- Historical Fib respect / hit rate (level reliability)
- Multi-swing extension (oldest vs newest swing-low anchors)
- Failures / traps (bull traps at extension, bear traps at retracement)
- Composite top/bottom signatures

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
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


# ---- family-specific PIT helpers ----

def _swing_low(low, n):
    win = 2 * n + 1
    rolling_min = low.rolling(win, min_periods=win).min()
    cand = low.shift(n)
    is_pivot = (cand == rolling_min) & cand.notna() & rolling_min.notna()
    return cand.where(is_pivot, np.nan).ffill()


def _swing_high(high, n):
    win = 2 * n + 1
    rolling_max = high.rolling(win, min_periods=win).max()
    cand = high.shift(n)
    is_pivot = (cand == rolling_max) & cand.notna() & rolling_max.notna()
    return cand.where(is_pivot, np.nan).ffill()


def _ext_value(price, sl, sh):
    return _safe_div(price - sl, sh - sl)


def _fib_target(sl, sh, ratio):
    return sl + ratio * (sh - sl)


def _retracement_value(price, sl, sh):
    """For an up-swing: how far has price pulled back from sh, normalized 0..1 of (sh-sl).
    0 = at swing high, 1 = back to swing low. >1 = below swing low (broken structure)."""
    return _safe_div(sh - price, sh - sl)


def _bear_extension_value(price, sh, sl):
    """For a down-swing (high → low → further down): extension value.
    1.0 = at swing low, 1.618 = price at 1.618 fib extension BELOW swing low."""
    return _safe_div(sh - price, sh - sl)


def _zigzag_pivots(close, threshold):
    """Causal zigzag returning (pivot_value, pivot_dir, pivot_idx). Same convention as family-10."""
    n = len(close)
    arr = close.to_numpy()
    pivot_val = np.full(n, np.nan)
    pivot_dir = np.full(n, 0)
    pivot_idx = np.full(n, np.nan)
    if n == 0:
        return pivot_val, pivot_dir, pivot_idx
    state = 0; ext_val = arr[0]; ext_idx = 0
    for i in range(1, n):
        v = arr[i]
        if np.isnan(v) or np.isnan(ext_val):
            if not np.isnan(v) and np.isnan(ext_val):
                ext_val = v; ext_idx = i; state = 0
            continue
        if state == 0:
            if v >= ext_val * (1.0 + threshold): state = 1; ext_val = v; ext_idx = i
            elif v <= ext_val * (1.0 - threshold): state = -1; ext_val = v; ext_idx = i
        elif state == 1:
            if v > ext_val: ext_val = v; ext_idx = i
            elif v <= ext_val * (1.0 - threshold):
                pivot_val[i] = ext_val; pivot_dir[i] = 1; pivot_idx[i] = float(ext_idx)
                state = -1; ext_val = v; ext_idx = i
        else:
            if v < ext_val: ext_val = v; ext_idx = i
            elif v >= ext_val * (1.0 + threshold):
                pivot_val[i] = ext_val; pivot_dir[i] = -1; pivot_idx[i] = float(ext_idx)
                state = 1; ext_val = v; ext_idx = i
    return pivot_val, pivot_dir, pivot_idx


def _last_n_zigzag_pivots(close, threshold, n_pivots):
    """At each bar, return the prices/dirs of the last n_pivots confirmed zigzag pivots.
    Returns two arrays of shape (len(close), n_pivots) — newest pivot at col n_pivots-1."""
    pivot_val, pivot_dir, _ = _zigzag_pivots(close, threshold)
    n = len(close)
    out_v = np.full((n, n_pivots), np.nan)
    out_d = np.full((n, n_pivots), 0)
    buf_v = []
    buf_d = []
    for i in range(n):
        if not np.isnan(pivot_val[i]):
            buf_v.append(pivot_val[i])
            buf_d.append(int(pivot_dir[i]))
            if len(buf_v) > n_pivots:
                buf_v.pop(0); buf_d.pop(0)
        if len(buf_v) == n_pivots:
            out_v[i] = np.array(buf_v)
            out_d[i] = np.array(buf_d)
    return out_v, out_d


def _check_xabcd_fib(x, a, b, c, d, ab_ratio_min, ab_ratio_max, bc_ratio_min, bc_ratio_max, cd_ratio_min, cd_ratio_max, xd_ratio_min, xd_ratio_max):
    """Vectorized check for harmonic XABCD pattern. Returns 1.0 if all ratios match, 0.0 if not.
    All inputs are scalars. Direction-agnostic — works for bullish (X low, A high, B low, C high, D low)
    or bearish (X high, A low, B high, C low, D high) — uses absolute leg magnitudes."""
    xa = abs(a - x)
    ab = abs(b - a)
    bc = abs(c - b)
    cd = abs(d - c)
    xd = abs(d - x)
    if xa == 0 or ab == 0 or bc == 0: return 0.0
    ab_xa = ab / xa
    bc_ab = bc / ab
    cd_bc = cd / bc
    xd_xa = xd / xa
    if not (ab_ratio_min <= ab_xa <= ab_ratio_max): return 0.0
    if not (bc_ratio_min <= bc_ab <= bc_ratio_max): return 0.0
    if not (cd_ratio_min <= cd_bc <= cd_ratio_max): return 0.0
    if not (xd_ratio_min <= xd_xa <= xd_ratio_max): return 0.0
    return 1.0


SW_S = 10
SW_M = 30
SW_L = 90

# ============================================================
# Bucket A — Fibonacci RETRACEMENT (price between SL and SH, NOT extension) (151-164)
# ============================================================

def f08_fibx_151_log_dist_below_0_618_retracement_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance of close BELOW the 0.618 retracement of medium swing (sh down to 0.618 retracement).
    Positive = close is below 0.618 retracement (deeper pullback). 0 = at 0.618. Negative = shallower."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.618)  # = sl + 0.382*(sh-sl), i.e. retracement to 0.618 level
    return _safe_log(target) - _safe_log(close)


def f08_fibx_152_log_dist_below_0_786_retracement_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist below 0.786 retracement of medium swing — deep-pullback test."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.786)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_153_log_dist_below_0_382_retracement_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist below 0.382 retracement of medium swing — shallow-pullback test."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.382)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_154_current_retracement_value_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Retracement value: 0 = at swing high, 1 = back to swing low, >1 = broken below swing low."""
    return _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))


def f08_fibx_155_current_retracement_value_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Retracement value on long swing."""
    return _retracement_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))


def f08_fibx_156_golden_pocket_retracement_indicator_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close in 'golden pocket' (61.8%-65% retracement). Classic reversal zone."""
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return ((rv >= 0.618) & (rv <= 0.65)).astype(float).where(rv.notna(), np.nan)


def f08_fibx_157_failed_retracement_below_786_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: retracement value > 0.786 (close broke deeper than 78.6% retrace — uptrend invalidation warning)."""
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return (rv > 0.786).astype(float).where(rv.notna(), np.nan)


def f08_fibx_158_retracement_zone_id_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Categorical zone of current retracement: 0=<0.236, 1=[0.236,0.382), 2=[0.382,0.5), 3=[0.5,0.618), 4=[0.618,0.786), 5=[0.786,1.0), 6=>=1.0."""
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    arr = rv.to_numpy()
    out = np.full(len(rv), np.nan)
    m = ~np.isnan(arr)
    out = np.where(m & (arr < 0.236), 0, out)
    out = np.where(m & (arr >= 0.236) & (arr < 0.382), 1, out)
    out = np.where(m & (arr >= 0.382) & (arr < 0.5), 2, out)
    out = np.where(m & (arr >= 0.5) & (arr < 0.618), 3, out)
    out = np.where(m & (arr >= 0.618) & (arr < 0.786), 4, out)
    out = np.where(m & (arr >= 0.786) & (arr < 1.0), 5, out)
    out = np.where(m & (arr >= 1.0), 6, out)
    return pd.Series(out, index=close.index)


def f08_fibx_159_pullback_log_depth_from_peak_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log depth of pullback from the most-recent swing high: log(swing_high / close)."""
    sh = _swing_high(high, SW_M)
    return _safe_log(sh) - _safe_log(close)


def f08_fibx_160_retracement_velocity_5d_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day change in retracement value — how fast price is pulling back."""
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return rv - rv.shift(WDAYS)


def f08_fibx_161_retracement_acceleration_5d_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day acceleration of retracement value."""
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return rv.diff(WDAYS).diff(WDAYS)


def f08_fibx_162_retracement_drawdown_from_swing_high_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized drawdown of close from swing high — direct retracement magnitude in vol units."""
    sh = _swing_high(high, SW_M)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(sh - close, atr)


def f08_fibx_163_shallow_retracement_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: retracement value < 0.236 AND structure age > 21d — strong uptrend with no real pullback."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    rv = _retracement_value(close, sl, sh)
    changed = sl.ne(sl.shift(1)).fillna(False)
    idx_at = np.where(changed.to_numpy(), np.arange(len(close)), np.nan)
    last_idx = pd.Series(idx_at, index=close.index).ffill()
    age = pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_idx
    return ((rv < 0.236) & (age > MDAYS)).astype(float).where(rv.notna(), np.nan)


def f08_fibx_164_deep_retracement_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: retracement value > 0.786 — deep pullback approaching swing-low test."""
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return (rv > 0.786).astype(float).where(rv.notna(), np.nan)


# ============================================================
# Bucket B — Harmonic XABCD patterns (165-174)
# ============================================================

def _harmonic_pattern_detector(close, threshold, ab_lo, ab_hi, bc_lo, bc_hi, cd_lo, cd_hi, xd_lo, xd_hi):
    """Returns indicator series: 1.0 at bars where the last 5 zigzag pivots (XABCD) match the given pattern's Fib ratios.
    Direction-agnostic. Carries forward until next 5-pivot window."""
    out_v, _ = _last_n_zigzag_pivots(close, threshold, 5)
    n = len(close)
    out = np.full(n, np.nan)
    for i in range(n):
        row = out_v[i]
        if np.isnan(row).any(): continue
        match = _check_xabcd_fib(row[0], row[1], row[2], row[3], row[4],
                                 ab_lo, ab_hi, bc_lo, bc_hi, cd_lo, cd_hi, xd_lo, xd_hi)
        out[i] = match
    return pd.Series(out, index=close.index).ffill().fillna(0.0)


def f08_fibx_165_gartley_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gartley pattern indicator (5% zigzag): AB=0.618±0.05 of XA, BC=0.382-0.886 of AB, CD=1.13-1.618 of BC, XD=0.786±0.05 of XA."""
    return _harmonic_pattern_detector(close, 0.05, 0.568, 0.668, 0.382, 0.886, 1.13, 1.618, 0.736, 0.836)


def f08_fibx_166_butterfly_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Butterfly pattern (5% zigzag): AB=0.786 of XA, BC=0.382-0.886 of AB, CD=1.618-2.618 of BC, XD=1.27-1.618 of XA — D beyond X (extension)."""
    return _harmonic_pattern_detector(close, 0.05, 0.736, 0.836, 0.382, 0.886, 1.618, 2.618, 1.27, 1.618)


def f08_fibx_167_bat_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bat pattern (5% zigzag): AB=0.382-0.5 of XA, BC=0.382-0.886 of AB, CD=1.618-2.618 of BC, XD=0.886 of XA."""
    return _harmonic_pattern_detector(close, 0.05, 0.382, 0.5, 0.382, 0.886, 1.618, 2.618, 0.836, 0.936)


def f08_fibx_168_crab_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Crab pattern (5% zigzag): AB=0.382-0.618 of XA, BC=0.382-0.886 of AB, CD=2.618-3.618 of BC, XD=1.618 of XA — extreme extension."""
    return _harmonic_pattern_detector(close, 0.05, 0.382, 0.618, 0.382, 0.886, 2.618, 3.618, 1.55, 1.68)


def f08_fibx_169_cypher_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cypher pattern (5% zigzag): AB=0.382-0.618 of XA, BC=1.13-1.414 of AB (extension!), CD=0.786 of XC (we approximate via BC), XD=0.786 of XA."""
    return _harmonic_pattern_detector(close, 0.05, 0.382, 0.618, 1.13, 1.414, 0.6, 1.2, 0.736, 0.836)


def f08_fibx_170_shark_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shark pattern (5% zigzag): AB=0.382-0.618 of XA, BC=1.13-1.618 of AB, CD=1.618-2.24 of BC, XD=0.886-1.13 of XA."""
    return _harmonic_pattern_detector(close, 0.05, 0.382, 0.618, 1.13, 1.618, 1.618, 2.24, 0.836, 1.18)


def f08_fibx_171_five_zero_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-0 pattern (5% zigzag): unconventional — AB=1.13-1.618 of XA, BC=1.618-2.24 of AB, CD=0.5 of BC."""
    return _harmonic_pattern_detector(close, 0.05, 1.13, 1.618, 1.618, 2.24, 0.45, 0.55, 0.5, 2.0)


def f08_fibx_172_any_harmonic_pattern_count_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d that completed ANY of the 7 harmonic patterns above."""
    s = (f08_fibx_165_gartley_pattern_indicator_5pct(high, low, close) +
         f08_fibx_166_butterfly_pattern_indicator_5pct(high, low, close) +
         f08_fibx_167_bat_pattern_indicator_5pct(high, low, close) +
         f08_fibx_168_crab_pattern_indicator_5pct(high, low, close) +
         f08_fibx_169_cypher_pattern_indicator_5pct(high, low, close) +
         f08_fibx_170_shark_pattern_indicator_5pct(high, low, close) +
         f08_fibx_171_five_zero_pattern_indicator_5pct(high, low, close))
    completion = (s.diff() > 0).astype(float)
    return completion.rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_173_bars_since_last_harmonic_completion_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since the last bar where any harmonic pattern indicator turned on."""
    s = (f08_fibx_165_gartley_pattern_indicator_5pct(high, low, close) +
         f08_fibx_166_butterfly_pattern_indicator_5pct(high, low, close) +
         f08_fibx_167_bat_pattern_indicator_5pct(high, low, close) +
         f08_fibx_168_crab_pattern_indicator_5pct(high, low, close) +
         f08_fibx_169_cypher_pattern_indicator_5pct(high, low, close) +
         f08_fibx_170_shark_pattern_indicator_5pct(high, low, close) +
         f08_fibx_171_five_zero_pattern_indicator_5pct(high, low, close))
    event = (s.diff() > 0).fillna(False)
    idx_at = np.where(event.to_numpy(), np.arange(len(close)), np.nan)
    last = pd.Series(idx_at, index=close.index).ffill()
    return pd.Series(np.arange(len(close), dtype=float), index=close.index) - last


def f08_fibx_174_log_dist_close_to_d_point_of_recent_pattern_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance of current close to D point of the most-recent 5-pivot zigzag structure
    — proximity to potential reversal zone of harmonic pattern."""
    out_v, _ = _last_n_zigzag_pivots(close, 0.05, 5)
    d_point = pd.Series(out_v[:, 4], index=close.index).ffill()
    return _safe_log(close) - _safe_log(d_point)


# ============================================================
# Bucket C — Multi-anchor Fib confluence (175-181)
# ============================================================

def _confluence_count_for_ratio(high, low, close, ratio, tol_atr=1.0):
    """Count of anchor swings (short/medium/long + lifetime) whose `ratio` fib target is within
    tol_atr of close."""
    atr = _atr(high, low, close, n=MDAYS)
    sl_s = _swing_low(low, SW_S); sh_s = _swing_high(high, SW_S)
    sl_m = _swing_low(low, SW_M); sh_m = _swing_high(high, SW_M)
    sl_l = _swing_low(low, SW_L); sh_l = _swing_high(high, SW_L)
    sl_life = low.expanding(min_periods=QDAYS).min(); sh_life = high.expanding(min_periods=QDAYS).max()
    cnt = pd.Series(0.0, index=close.index)
    for sl, sh in [(sl_s, sh_s), (sl_m, sh_m), (sl_l, sh_l), (sl_life, sh_life)]:
        tgt = _fib_target(sl, sh, ratio)
        within = ((tgt - close).abs() <= tol_atr * atr).astype(float)
        cnt = cnt + within
    return cnt


def f08_fibx_175_confluence_count_anchors_at_1_618_within_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of anchor swings (S/M/L/lifetime) whose 1.618 ext is within 1 ATR of close — confluence at golden ext."""
    return _confluence_count_for_ratio(high, low, close, 1.618, tol_atr=1.0)


def f08_fibx_176_confluence_count_anchors_at_2_0_within_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Confluence at 2.0 ext."""
    return _confluence_count_for_ratio(high, low, close, 2.0, tol_atr=1.0)


def f08_fibx_177_confluence_count_anchors_at_2_618_within_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Confluence at 2.618 ext."""
    return _confluence_count_for_ratio(high, low, close, 2.618, tol_atr=1.0)


def f08_fibx_178_closest_confluent_fib_above_close_log_dist(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance UP to nearest fib level from any of 4 anchors that has at least 2 anchors agreeing within 2 ATR."""
    atr = _atr(high, low, close, n=MDAYS)
    sl_s = _swing_low(low, SW_S); sh_s = _swing_high(high, SW_S)
    sl_m = _swing_low(low, SW_M); sh_m = _swing_high(high, SW_M)
    sl_l = _swing_low(low, SW_L); sh_l = _swing_high(high, SW_L)
    sl_life = low.expanding(min_periods=QDAYS).min(); sh_life = high.expanding(min_periods=QDAYS).max()
    ratios = [1.272, 1.618, 2.0, 2.618, 4.236]
    n = len(close)
    close_arr = close.to_numpy(); atr_arr = atr.to_numpy()
    targets_per_bar = []
    for sl, sh in [(sl_s, sh_s), (sl_m, sh_m), (sl_l, sh_l), (sl_life, sh_life)]:
        for r in ratios:
            targets_per_bar.append(_fib_target(sl, sh, r).to_numpy())
    targets_mat = np.column_stack(targets_per_bar)
    out = np.full(n, np.nan)
    for i in range(n):
        c = close_arr[i]; a = atr_arr[i]
        if np.isnan(c) or np.isnan(a) or a == 0: continue
        row = targets_mat[i]; row = row[~np.isnan(row)]
        above = np.sort(row[row > c])
        # find lowest above that has at least 1 neighbor within 2 ATR (confluent)
        for lvl in above:
            n_near = np.sum(np.abs(above - lvl) <= 2 * a)
            if n_near >= 2:
                out[i] = float(np.log(lvl) - np.log(c))
                break
    return pd.Series(out, index=close.index)


def f08_fibx_179_closest_confluent_fib_below_close_log_dist(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance DOWN to nearest confluent fib level below close (mirror of 178)."""
    atr = _atr(high, low, close, n=MDAYS)
    sl_s = _swing_low(low, SW_S); sh_s = _swing_high(high, SW_S)
    sl_m = _swing_low(low, SW_M); sh_m = _swing_high(high, SW_M)
    sl_l = _swing_low(low, SW_L); sh_l = _swing_high(high, SW_L)
    sl_life = low.expanding(min_periods=QDAYS).min(); sh_life = high.expanding(min_periods=QDAYS).max()
    ratios = [0.382, 0.5, 0.618, 1.0, 1.272, 1.618]
    n = len(close)
    close_arr = close.to_numpy(); atr_arr = atr.to_numpy()
    parts = []
    for sl, sh in [(sl_s, sh_s), (sl_m, sh_m), (sl_l, sh_l), (sl_life, sh_life)]:
        for r in ratios:
            parts.append(_fib_target(sl, sh, r).to_numpy())
    targets_mat = np.column_stack(parts)
    out = np.full(n, np.nan)
    for i in range(n):
        c = close_arr[i]; a = atr_arr[i]
        if np.isnan(c) or np.isnan(a) or a == 0: continue
        row = targets_mat[i]; row = row[~np.isnan(row)]
        below = np.sort(row[row < c])[::-1]
        for lvl in below:
            n_near = np.sum(np.abs(below - lvl) <= 2 * a)
            if n_near >= 2:
                out[i] = float(np.log(c) - np.log(lvl))
                break
    return pd.Series(out, index=close.index)


def f08_fibx_180_confluence_zone_density_total_within_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Total count of fib levels (4 anchors × 5 ratios = 20) within 1 ATR of close — total cluster density."""
    atr = _atr(high, low, close, n=MDAYS)
    sl_s = _swing_low(low, SW_S); sh_s = _swing_high(high, SW_S)
    sl_m = _swing_low(low, SW_M); sh_m = _swing_high(high, SW_M)
    sl_l = _swing_low(low, SW_L); sh_l = _swing_high(high, SW_L)
    sl_life = low.expanding(min_periods=QDAYS).min(); sh_life = high.expanding(min_periods=QDAYS).max()
    ratios = [1.0, 1.272, 1.618, 2.0, 2.618]
    cnt = pd.Series(0.0, index=close.index)
    for sl, sh in [(sl_s, sh_s), (sl_m, sh_m), (sl_l, sh_l), (sl_life, sh_life)]:
        for r in ratios:
            cnt = cnt + ((_fib_target(sl, sh, r) - close).abs() <= atr).astype(float)
    return cnt


def f08_fibx_181_magnet_fib_level_signed_log_dist(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed log distance to the strongest 'magnet' fib (any anchor) — closest level with at least 2 confluent levels."""
    above = f08_fibx_178_closest_confluent_fib_above_close_log_dist(high, low, close)
    below = f08_fibx_179_closest_confluent_fib_below_close_log_dist(high, low, close)
    # whichever absolute value is smaller; sign positive = above
    closer_above = above.where(above < below.fillna(np.inf), -below)
    return closer_above


# ============================================================
# Bucket D — Bear-side fib (downward extension after H→L) (182-188)
# ============================================================

def _bear_swing_pivots(high, low, n):
    """For bear extension, anchor is a confirmed swing HIGH then a swing LOW.
    sh = most recent confirmed swing-high (carried forward), sl = most recent swing-low after that."""
    sh = _swing_high(high, n)
    sl = _swing_low(low, n)
    return sh, sl


def f08_fibx_182_bear_swing_extension_value_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bear extension value: how far close is BELOW swing low as fraction of (sh-sl).
    0 = at swing low. Negative = above swing low (still in retracement zone). >0 = below swing low (breakdown)."""
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    return _safe_div(sl - close, sh - sl)


def f08_fibx_183_log_dist_below_neg_0_272_bear_extension_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist below the -0.272 bear extension level (sl - 0.272*(sh-sl)) of medium swing."""
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    target = sl - 0.272 * (sh - sl)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_184_log_dist_below_neg_0_618_bear_extension_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist below -0.618 bear extension."""
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    target = sl - 0.618 * (sh - sl)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_185_log_dist_below_neg_1_0_measured_move_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist below the -1.0 measured move target (sl - 1.0*(sh-sl)) — full bear measured move."""
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    target = sl - (sh - sl)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_186_log_dist_below_neg_1_618_bear_extension_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist below -1.618 bear extension — extreme breakdown."""
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    target = sl - 1.618 * (sh - sl)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_187_count_bear_fib_levels_breached_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """How many of {-0.272, -0.618, -1.0, -1.618, -2.618} bear-extension targets close is currently below."""
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    cnt = pd.Series(0.0, index=close.index)
    valid = sh.notna() & sl.notna()
    for r in [0.272, 0.618, 1.0, 1.618, 2.618]:
        cnt = cnt + (close < (sl - r * (sh - sl))).astype(float)
    return cnt.where(valid, np.nan)


def f08_fibx_188_bear_abcd_measured_move_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: current down-leg (sl - close) is within ±10% of the prior down-leg (sh - sl) — clean bear ABCD."""
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    down_leg1 = sh - sl
    down_leg2 = sl - close
    r = _safe_div(down_leg2, down_leg1)
    return ((r >= 0.9) & (r <= 1.1)).astype(float).where(r.notna(), np.nan)


# ============================================================
# Bucket E — Fib time zones (Fibonacci numbers as time intervals) (189-191)
# ============================================================

def _bars_since_event(event):
    idx_at = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last = pd.Series(idx_at, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last


def f08_fibx_189_distance_to_nearest_fib_time_window_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars-since most recent swing low ÷ closest Fibonacci number {8, 13, 21, 34, 55, 89, 144}, signed.
    Positive = past the fib number. 0 = exactly at."""
    sl = _swing_low(low, SW_M)
    changed = sl.ne(sl.shift(1)).fillna(False)
    bars = _bars_since_event(changed)
    fib_nums = np.array([8.0, 13.0, 21.0, 34.0, 55.0, 89.0, 144.0])
    arr = bars.to_numpy()
    out = np.full(len(bars), np.nan)
    for i in range(len(bars)):
        if np.isnan(arr[i]): continue
        idx = np.argmin(np.abs(fib_nums - arr[i]))
        out[i] = arr[i] - fib_nums[idx]
    return pd.Series(out, index=close.index)


def f08_fibx_190_fib_time_target_proximity_score_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 / (1 + |bars_since - nearest_fib_number|) — peaks at exact fib-number bars-since pivot."""
    dist = f08_fibx_189_distance_to_nearest_fib_time_window_medium(high, low, close)
    return _safe_div(1.0, 1.0 + dist.abs())


def f08_fibx_191_current_leg_duration_vs_fib_of_prior_leg_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of current leg duration to 1.618 × prior leg duration on medium swing — time-symmetry test."""
    pv, _, pidx = _zigzag_pivots(close, 0.05)
    last_ext_idx = pd.Series(pidx, index=close.index).ffill()
    cur_dur = pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_ext_idx
    prior_idx = pd.Series(pidx, index=close.index).ffill().shift(1)
    prior_dur = last_ext_idx - prior_idx
    return _safe_div(cur_dur, 1.618 * prior_dur)


# ============================================================
# Bucket F — Fib MA extension (non-pivot anchor) (192-195)
# ============================================================

def f08_fibx_192_log_dist_above_1_618_atr_above_21d_sma(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist of close above (21d SMA + 1.618 × 21d ATR) — MA-anchored fib band."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_log(close) - _safe_log(sma + 1.618 * atr)


def f08_fibx_193_log_dist_above_2_618_atr_above_63d_sma(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist of close above (63d SMA + 2.618 × 21d ATR)."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_log(close) - _safe_log(sma + 2.618 * atr)


def f08_fibx_194_above_2_618_atr_band_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close above 2.618 ATR band on 63d SMA."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    return (close > sma + 2.618 * atr).astype(float).where(sma.notna() & atr.notna(), np.nan)


def f08_fibx_195_count_band_touches_above_1_618_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where high tagged (21d SMA + 1.618 ATR)."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    band = sma + 1.618 * atr
    return (high >= band).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket G — Fib + volume confluence (196-198)
# ============================================================

def f08_fibx_196_mean_volume_when_close_within_1pct_of_1_618_fib_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on bars in last 63d where close was within 1% of the 1.618 fib target of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.618)
    near = (close - target).abs() <= 0.01 * close
    vol_near = volume.where(near, np.nan)
    return vol_near.rolling(QDAYS, min_periods=WDAYS).mean()


def f08_fibx_197_volume_zscore_when_at_1_618_fib_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume on bars near 1.618 fib vs trailing 252d volume distribution. Carried forward."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.618)
    near = (close - target).abs() <= 0.01 * close
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return vz.where(near, np.nan).ffill()


def f08_fibx_198_cum_volume_at_fib_extension_zones_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative volume in last 63d on bars where close was within 1% of any fib extension level (1.272/1.618/2.0/2.618) of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    at_any = pd.Series(False, index=close.index)
    for r in [1.272, 1.618, 2.0, 2.618]:
        target = _fib_target(sl, sh, r)
        at_any = at_any | ((close - target).abs() <= 0.01 * close)
    return volume.where(at_any, 0.0).rolling(QDAYS, min_periods=WDAYS).sum()


# ============================================================
# Bucket H — Historical Fib respect / hit rate (199-203)
# ============================================================

def f08_fibx_199_count_1_618_touches_with_reversal_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where high tagged 1.618 fib (medium swing) AND close 5 bars later was >2% below."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.618)
    touched = (high >= target) & (target > 0)
    touched_lag = touched.shift(WDAYS).fillna(False)
    target_lag = target.shift(WDAYS)
    reversed_ = (close < 0.98 * target_lag)
    event = touched_lag & reversed_
    return event.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_200_fib_1_618_resistance_hit_rate_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rate: touches with reversal / total touches in last 252d."""
    rev = f08_fibx_199_count_1_618_touches_with_reversal_252d(high, low, close)
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.618)
    touched = (high >= target).shift(WDAYS).astype(float)
    tot = touched.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(rev, tot)


def f08_fibx_201_count_0_618_retracement_bounces_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where low tagged 0.618 retracement (= 0.382 fib target) of medium swing
    AND close 5 bars later was >2% above target."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.618)  # 0.382 level
    touched_low = (low <= target) & (target > 0)
    touched_lag = touched_low.shift(WDAYS).fillna(False)
    target_lag = target.shift(WDAYS)
    bounced = (close > 1.02 * target_lag)
    return (touched_lag & bounced).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_202_mean_5d_bounce_magnitude_from_0_618_retracement_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean log return over 5 bars following a 0.618 retracement touch in last 252d."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.618)
    touched_lag = ((low <= target) & (target > 0)).shift(WDAYS).fillna(False)
    log_ret = _safe_log(close) - _safe_log(close.shift(WDAYS))
    return log_ret.where(touched_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f08_fibx_203_fib_level_reliability_score_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite reliability: resistance_hit_rate + 0.5 × bounce_rate at supports."""
    res_rate = f08_fibx_200_fib_1_618_resistance_hit_rate_252d(high, low, close)
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.618)
    touched = ((low <= target) & (target > 0)).shift(WDAYS).astype(float)
    bounces = f08_fibx_201_count_0_618_retracement_bounces_252d(high, low, close)
    tot = touched.rolling(YDAYS, min_periods=QDAYS).sum()
    bounce_rate = _safe_div(bounces, tot)
    return res_rate.fillna(0) + 0.5 * bounce_rate.fillna(0)


# ============================================================
# Bucket I — Multi-anchor extension (oldest vs newest swing) (204-207)
# ============================================================

def f08_fibx_204_log_dist_above_1_618_of_oldest_swing_low_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist of close above the 1.618 ext of the OLDEST medium swing-low in trailing 252d."""
    n = len(close); low_arr = low.to_numpy(); high_arr = high.to_numpy(); close_arr = close.to_numpy()
    sl_series = _swing_low(low, SW_M); sh_series = _swing_high(high, SW_M)
    sl_arr = sl_series.to_numpy(); sh_arr = sh_series.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win_sl = sl_arr[start:i + 1]; win_sh = sh_arr[start:i + 1]
        valid_idx = np.where(~np.isnan(win_sl) & ~np.isnan(win_sh))[0]
        if valid_idx.size == 0: continue
        # oldest is first valid
        oi = valid_idx[0]
        sl_val = win_sl[oi]; sh_val = win_sh[oi]
        target = sl_val + 1.618 * (sh_val - sl_val)
        if target > 0 and close_arr[i] > 0:
            out[i] = float(np.log(close_arr[i]) - np.log(target))
    return pd.Series(out, index=close.index)


def f08_fibx_205_log_dist_above_1_618_of_2nd_most_recent_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist above 1.618 ext using the previous swing-low (not the most recent)."""
    sl_series = _swing_low(low, SW_M); sh_series = _swing_high(high, SW_M)
    sl_prior = sl_series.where(sl_series.ne(sl_series.shift(1))).ffill().shift(1)
    sh_prior = sh_series.where(sh_series.ne(sh_series.shift(1))).ffill().shift(1)
    target = sl_prior + 1.618 * (sh_prior - sl_prior)
    return _safe_log(close) - _safe_log(target)


def f08_fibx_206_count_swings_whose_1_618_ext_close_exceeds_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """How many distinct medium-swing 1.618-ext targets in last 252d does the current close exceed."""
    sl_series = _swing_low(low, SW_M); sh_series = _swing_high(high, SW_M)
    sl_arr = sl_series.to_numpy(); sh_arr = sh_series.to_numpy()
    close_arr = close.to_numpy(); n = len(close)
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win_sl = sl_arr[start:i + 1]; win_sh = sh_arr[start:i + 1]
        valid = ~np.isnan(win_sl) & ~np.isnan(win_sh)
        if not valid.any(): continue
        targets = win_sl[valid] + 1.618 * (win_sh[valid] - win_sl[valid])
        targets = np.unique(targets)
        c = close_arr[i]
        if np.isnan(c): continue
        out[i] = float(np.sum(c > targets))
    return pd.Series(out, index=close.index)


def f08_fibx_207_extension_disagreement_oldest_vs_newest_swing_log(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log dist above 1.618 of newest swing minus log dist above 1.618 of oldest swing in 252d."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target_new = _fib_target(sl, sh, 1.618)
    new_dist = _safe_log(close) - _safe_log(target_new)
    old_dist = f08_fibx_204_log_dist_above_1_618_of_oldest_swing_low_in_252d(high, low, close)
    return new_dist - old_dist


# ============================================================
# Bucket J — Failures and traps (208-212)
# ============================================================

def f08_fibx_208_bull_trap_at_2_0_extension_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where high tagged 2.0 ext (medium swing) but close 5 bars later was >5% lower than the touch-bar close."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 2.0)
    touched = (high >= target) & (target > 0)
    touched_lag = touched.shift(WDAYS).fillna(False)
    close_at_touch_lag = close.shift(WDAYS)
    trap = (close < 0.95 * close_at_touch_lag)
    return (touched_lag & trap).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_209_bear_trap_at_786_retracement_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where low tagged 0.786 retracement but close 5 bars later was >5% higher."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.786)
    touched_low = (low <= target) & (target > 0)
    touched_lag = touched_low.shift(WDAYS).fillna(False)
    close_at_touch_lag = close.shift(WDAYS)
    trap = (close > 1.05 * close_at_touch_lag)
    return (touched_lag & trap).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_210_extension_breakdown_recent_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close was above 1.618 ext within last 21d AND is now below 1.272 ext — breakdown of extension regime."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    above_1618_recent = (close > _fib_target(sl, sh, 1.618)).rolling(MDAYS, min_periods=1).max().astype(float)
    below_1272_now = (close < _fib_target(sl, sh, 1.272)).astype(float)
    return ((above_1618_recent == 1) & (below_1272_now == 1)).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_211_count_extension_breakdowns_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d that triggered extension_breakdown_recent."""
    ev = f08_fibx_210_extension_breakdown_recent_indicator_medium(high, low, close).fillna(0)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_212_count_failed_retracements_below_786_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where retracement value > 0.786 — uptrend invalidation event count."""
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return (rv > 0.786).fillna(False).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket K — Composite top/bottom signatures (213-225)
# ============================================================

def f08_fibx_213_fib_terminal_blowoff_composite_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: above 2.618 ext NOW + at least 1 failure-to-extend event in last 5d + close in top decile of 252d range."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    above_2618 = (close > _fib_target(sl, sh, 2.618)).astype(float)
    tgt_1618 = _fib_target(sl, sh, 1.618)
    fail = ((high > tgt_1618) & (close < tgt_1618)).astype(float)
    fail_recent = (fail.rolling(WDAYS, min_periods=1).sum() >= 1).astype(float)
    hi252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    lo252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - lo252, hi252 - lo252)
    in_top = (pos >= 0.9).astype(float)
    return above_2618 + fail_recent + in_top


def f08_fibx_214_fib_capitulation_composite_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite bear bottom: bear ext > 0.618 NOW + no recovery to retracement < 0.382 in last 21d."""
    bev = f08_fibx_182_bear_swing_extension_value_medium(high, low, close)
    below = (bev > 0.618).astype(float)
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    no_recovery = (rv > 0.618).rolling(MDAYS, min_periods=WDAYS).min().astype(float)
    return below + no_recovery


def f08_fibx_215_parabolic_fib_progression_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: each successive fib extension level (1.272 → 1.618 → 2.0 → 2.618) was reached in shorter time than the prior — parabolic progression."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    bars_arr = np.arange(len(close), dtype=float)
    cross_idx = {}
    for r in [1.272, 1.618, 2.0, 2.618]:
        tgt = _fib_target(sl, sh, r)
        crossed = (close > tgt) & (close.shift(1) <= tgt.shift(1))
        idx_at = np.where(crossed.to_numpy(), bars_arr, np.nan)
        cross_idx[r] = pd.Series(idx_at, index=close.index).ffill()
    gap_12 = cross_idx[1.618] - cross_idx[1.272]
    gap_23 = cross_idx[2.0] - cross_idx[1.618]
    gap_34 = cross_idx[2.618] - cross_idx[2.0]
    return ((gap_23 < gap_12) & (gap_34 < gap_23) & gap_12.notna() & gap_23.notna() & gap_34.notna()).astype(float)


def f08_fibx_216_fib_exhaustion_score_breach_count_extreme(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of (close > target) for extreme fib levels {2.0, 2.618, 4.236} across short/medium/long swings — exhaustion breach count."""
    score = pd.Series(0.0, index=close.index)
    for nw in [SW_S, SW_M, SW_L]:
        sl = _swing_low(low, nw); sh = _swing_high(high, nw)
        for r in [2.0, 2.618, 4.236]:
            score = score + (close > _fib_target(sl, sh, r)).astype(float)
    return score


def f08_fibx_217_fib_compression_score_no_extension_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Score: count of fib extension levels {1.272, 1.618, 2.0, 2.618} NEVER breached in last 252d (across S/M/L swings)."""
    score = pd.Series(0.0, index=close.index)
    for nw in [SW_S, SW_M, SW_L]:
        sl = _swing_low(low, nw); sh = _swing_high(high, nw)
        for r in [1.272, 1.618, 2.0, 2.618]:
            breached_in_252 = (close > _fib_target(sl, sh, r)).astype(float).rolling(YDAYS, min_periods=QDAYS).max()
            score = score + (breached_in_252 == 0).astype(float)
    return score


def f08_fibx_218_extension_zone_residence_time_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in current fib zone (long swing) — how long has price been in this regime."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    rv = _ext_value(close, sl, sh)
    # zone id same as f08_fibx_031 for long swing
    arr = rv.to_numpy()
    out = np.full(len(rv), np.nan)
    m = ~np.isnan(arr)
    zone = np.full(len(rv), np.nan)
    zone = np.where(m & (arr < 1.0), 0, zone)
    zone = np.where(m & (arr >= 1.0) & (arr < 1.272), 1, zone)
    zone = np.where(m & (arr >= 1.272) & (arr < 1.618), 2, zone)
    zone = np.where(m & (arr >= 1.618) & (arr < 2.0), 3, zone)
    zone = np.where(m & (arr >= 2.0) & (arr < 2.618), 4, zone)
    zone = np.where(m & (arr >= 2.618) & (arr < 4.236), 5, zone)
    zone = np.where(m & (arr >= 4.236), 6, zone)
    cur = np.nan; run = 0.0
    for i in range(len(rv)):
        z = zone[i]
        if np.isnan(z):
            out[i] = np.nan; cur = np.nan; run = 0.0
        else:
            if z == cur:
                run += 1.0
            else:
                cur = z; run = 1.0
            out[i] = run
    return pd.Series(out, index=close.index)


def f08_fibx_219_weighted_extension_across_S_M_L_swings(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Weighted mean ext value across S/M/L swings (weights 1/3/9 favoring long horizon)."""
    es = _ext_value(close, _swing_low(low, SW_S), _swing_high(high, SW_S))
    em = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    el = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return (1.0 * es + 3.0 * em + 9.0 * el) / 13.0


def f08_fibx_220_log_ratio_short_swing_ext_to_long_swing_ext(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log ratio of short-swing ext value to long-swing ext value — multi-scale ratio signal."""
    es = _ext_value(close, _swing_low(low, SW_S), _swing_high(high, SW_S))
    el = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return _safe_log(es) - _safe_log(el)


def f08_fibx_221_extension_top_warning_composite_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite warning: parabolic progression + bull traps in last 252d + at-or-above-2_0 currently."""
    para = f08_fibx_215_parabolic_fib_progression_indicator_medium(high, low, close).fillna(0)
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    at_2_0 = (close > _fib_target(sl, sh, 2.0)).astype(float)
    traps = f08_fibx_208_bull_trap_at_2_0_extension_count_252d(high, low, close).fillna(0)
    return para + at_2_0 + (traps > 0).astype(float)


def f08_fibx_222_breakdown_warning_composite_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite breakdown warning: ext below 1.0 NOW + recent above 1.618 in 21d + retracement > 0.5."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    below_1 = (close < sh).astype(float)
    recent_above_1618 = ((close > _fib_target(sl, sh, 1.618)).rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    rv = _retracement_value(close, sl, sh)
    deep_retrace = (rv > 0.5).astype(float)
    return below_1 + recent_above_1618 + deep_retrace


def f08_fibx_223_bearish_engulfing_of_fib_levels_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today's range engulfs the 1.272 and 1.618 fib levels of medium swing AND close < open implied by high/low position."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt1 = _fib_target(sl, sh, 1.272)
    tgt2 = _fib_target(sl, sh, 1.618)
    engulf = (low <= tgt1) & (high >= tgt2)
    pos = _safe_div(close - low, high - low)
    weak_close = pos < 0.4
    return (engulf & weak_close).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_224_extension_velocity_acceleration_decline_composite(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Composite: extension velocity (5d) > 0 historically AND recent (5d) velocity < 0 AND in top decile of ext-value distribution."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    v_recent = e - e.shift(WDAYS)
    v_prior = e.shift(WDAYS) - e.shift(2 * WDAYS)
    decel = (v_recent < 0) & (v_prior > 0)
    def _rk(w):
        if np.isnan(w).all(): return np.nan
        last = w[-1]
        if np.isnan(last): return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0: return np.nan
        return float((v <= last).sum()) / float(v.size)
    pct_rank = e.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    in_top = pct_rank >= 0.9
    return (decel & in_top).astype(float)


def f08_fibx_225_full_top_signature_score_weighted(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Final weighted top signature: 3 × terminal_blowoff + 2 × parabolic_progression + 1 × bull_trap_count + 1 × velocity_accel_decline_composite."""
    a = f08_fibx_213_fib_terminal_blowoff_composite_252d(high, low, close).fillna(0)
    b = f08_fibx_215_parabolic_fib_progression_indicator_medium(high, low, close).fillna(0)
    c = (f08_fibx_208_bull_trap_at_2_0_extension_count_252d(high, low, close).fillna(0) > 0).astype(float)
    d = f08_fibx_224_extension_velocity_acceleration_decline_composite(high, low, close).fillna(0)
    return 3.0 * a + 2.0 * b + c + d


# ============================================================
#                         REGISTRY 151-225
# ============================================================

FIBONACCI_EXTENSION_SIGNATURE_BASE_REGISTRY_151_225 = {
    "f08_fibx_151_log_dist_below_0_618_retracement_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_151_log_dist_below_0_618_retracement_medium_swing},
    "f08_fibx_152_log_dist_below_0_786_retracement_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_152_log_dist_below_0_786_retracement_medium_swing},
    "f08_fibx_153_log_dist_below_0_382_retracement_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_153_log_dist_below_0_382_retracement_medium_swing},
    "f08_fibx_154_current_retracement_value_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_154_current_retracement_value_medium_swing},
    "f08_fibx_155_current_retracement_value_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_155_current_retracement_value_long_swing},
    "f08_fibx_156_golden_pocket_retracement_indicator_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_156_golden_pocket_retracement_indicator_medium_swing},
    "f08_fibx_157_failed_retracement_below_786_indicator_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_157_failed_retracement_below_786_indicator_medium},
    "f08_fibx_158_retracement_zone_id_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_158_retracement_zone_id_medium_swing},
    "f08_fibx_159_pullback_log_depth_from_peak_medium_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_159_pullback_log_depth_from_peak_medium_swing},
    "f08_fibx_160_retracement_velocity_5d_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_160_retracement_velocity_5d_medium},
    "f08_fibx_161_retracement_acceleration_5d_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_161_retracement_acceleration_5d_medium},
    "f08_fibx_162_retracement_drawdown_from_swing_high_atr": {"inputs": ["high", "low", "close"], "func": f08_fibx_162_retracement_drawdown_from_swing_high_atr},
    "f08_fibx_163_shallow_retracement_indicator_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_163_shallow_retracement_indicator_medium},
    "f08_fibx_164_deep_retracement_indicator_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_164_deep_retracement_indicator_medium},
    "f08_fibx_165_gartley_pattern_indicator_5pct": {"inputs": ["high", "low", "close"], "func": f08_fibx_165_gartley_pattern_indicator_5pct},
    "f08_fibx_166_butterfly_pattern_indicator_5pct": {"inputs": ["high", "low", "close"], "func": f08_fibx_166_butterfly_pattern_indicator_5pct},
    "f08_fibx_167_bat_pattern_indicator_5pct": {"inputs": ["high", "low", "close"], "func": f08_fibx_167_bat_pattern_indicator_5pct},
    "f08_fibx_168_crab_pattern_indicator_5pct": {"inputs": ["high", "low", "close"], "func": f08_fibx_168_crab_pattern_indicator_5pct},
    "f08_fibx_169_cypher_pattern_indicator_5pct": {"inputs": ["high", "low", "close"], "func": f08_fibx_169_cypher_pattern_indicator_5pct},
    "f08_fibx_170_shark_pattern_indicator_5pct": {"inputs": ["high", "low", "close"], "func": f08_fibx_170_shark_pattern_indicator_5pct},
    "f08_fibx_171_five_zero_pattern_indicator_5pct": {"inputs": ["high", "low", "close"], "func": f08_fibx_171_five_zero_pattern_indicator_5pct},
    "f08_fibx_172_any_harmonic_pattern_count_252d_5pct": {"inputs": ["high", "low", "close"], "func": f08_fibx_172_any_harmonic_pattern_count_252d_5pct},
    "f08_fibx_173_bars_since_last_harmonic_completion_5pct": {"inputs": ["high", "low", "close"], "func": f08_fibx_173_bars_since_last_harmonic_completion_5pct},
    "f08_fibx_174_log_dist_close_to_d_point_of_recent_pattern_5pct": {"inputs": ["high", "low", "close"], "func": f08_fibx_174_log_dist_close_to_d_point_of_recent_pattern_5pct},
    "f08_fibx_175_confluence_count_anchors_at_1_618_within_atr": {"inputs": ["high", "low", "close"], "func": f08_fibx_175_confluence_count_anchors_at_1_618_within_atr},
    "f08_fibx_176_confluence_count_anchors_at_2_0_within_atr": {"inputs": ["high", "low", "close"], "func": f08_fibx_176_confluence_count_anchors_at_2_0_within_atr},
    "f08_fibx_177_confluence_count_anchors_at_2_618_within_atr": {"inputs": ["high", "low", "close"], "func": f08_fibx_177_confluence_count_anchors_at_2_618_within_atr},
    "f08_fibx_178_closest_confluent_fib_above_close_log_dist": {"inputs": ["high", "low", "close"], "func": f08_fibx_178_closest_confluent_fib_above_close_log_dist},
    "f08_fibx_179_closest_confluent_fib_below_close_log_dist": {"inputs": ["high", "low", "close"], "func": f08_fibx_179_closest_confluent_fib_below_close_log_dist},
    "f08_fibx_180_confluence_zone_density_total_within_atr": {"inputs": ["high", "low", "close"], "func": f08_fibx_180_confluence_zone_density_total_within_atr},
    "f08_fibx_181_magnet_fib_level_signed_log_dist": {"inputs": ["high", "low", "close"], "func": f08_fibx_181_magnet_fib_level_signed_log_dist},
    "f08_fibx_182_bear_swing_extension_value_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_182_bear_swing_extension_value_medium},
    "f08_fibx_183_log_dist_below_neg_0_272_bear_extension_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_183_log_dist_below_neg_0_272_bear_extension_medium},
    "f08_fibx_184_log_dist_below_neg_0_618_bear_extension_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_184_log_dist_below_neg_0_618_bear_extension_medium},
    "f08_fibx_185_log_dist_below_neg_1_0_measured_move_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_185_log_dist_below_neg_1_0_measured_move_medium},
    "f08_fibx_186_log_dist_below_neg_1_618_bear_extension_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_186_log_dist_below_neg_1_618_bear_extension_medium},
    "f08_fibx_187_count_bear_fib_levels_breached_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_187_count_bear_fib_levels_breached_medium},
    "f08_fibx_188_bear_abcd_measured_move_indicator_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_188_bear_abcd_measured_move_indicator_medium},
    "f08_fibx_189_distance_to_nearest_fib_time_window_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_189_distance_to_nearest_fib_time_window_medium},
    "f08_fibx_190_fib_time_target_proximity_score_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_190_fib_time_target_proximity_score_medium},
    "f08_fibx_191_current_leg_duration_vs_fib_of_prior_leg_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_191_current_leg_duration_vs_fib_of_prior_leg_medium},
    "f08_fibx_192_log_dist_above_1_618_atr_above_21d_sma": {"inputs": ["high", "low", "close"], "func": f08_fibx_192_log_dist_above_1_618_atr_above_21d_sma},
    "f08_fibx_193_log_dist_above_2_618_atr_above_63d_sma": {"inputs": ["high", "low", "close"], "func": f08_fibx_193_log_dist_above_2_618_atr_above_63d_sma},
    "f08_fibx_194_above_2_618_atr_band_indicator_63d": {"inputs": ["high", "low", "close"], "func": f08_fibx_194_above_2_618_atr_band_indicator_63d},
    "f08_fibx_195_count_band_touches_above_1_618_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_195_count_band_touches_above_1_618_252d},
    "f08_fibx_196_mean_volume_when_close_within_1pct_of_1_618_fib_63d": {"inputs": ["high", "low", "close", "volume"], "func": f08_fibx_196_mean_volume_when_close_within_1pct_of_1_618_fib_63d},
    "f08_fibx_197_volume_zscore_when_at_1_618_fib_252d": {"inputs": ["high", "low", "close", "volume"], "func": f08_fibx_197_volume_zscore_when_at_1_618_fib_252d},
    "f08_fibx_198_cum_volume_at_fib_extension_zones_63d": {"inputs": ["high", "low", "close", "volume"], "func": f08_fibx_198_cum_volume_at_fib_extension_zones_63d},
    "f08_fibx_199_count_1_618_touches_with_reversal_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_199_count_1_618_touches_with_reversal_252d},
    "f08_fibx_200_fib_1_618_resistance_hit_rate_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_200_fib_1_618_resistance_hit_rate_252d},
    "f08_fibx_201_count_0_618_retracement_bounces_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_201_count_0_618_retracement_bounces_252d},
    "f08_fibx_202_mean_5d_bounce_magnitude_from_0_618_retracement_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_202_mean_5d_bounce_magnitude_from_0_618_retracement_252d},
    "f08_fibx_203_fib_level_reliability_score_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_203_fib_level_reliability_score_medium},
    "f08_fibx_204_log_dist_above_1_618_of_oldest_swing_low_in_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_204_log_dist_above_1_618_of_oldest_swing_low_in_252d},
    "f08_fibx_205_log_dist_above_1_618_of_2nd_most_recent_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_205_log_dist_above_1_618_of_2nd_most_recent_swing},
    "f08_fibx_206_count_swings_whose_1_618_ext_close_exceeds_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_206_count_swings_whose_1_618_ext_close_exceeds_medium},
    "f08_fibx_207_extension_disagreement_oldest_vs_newest_swing_log": {"inputs": ["high", "low", "close"], "func": f08_fibx_207_extension_disagreement_oldest_vs_newest_swing_log},
    "f08_fibx_208_bull_trap_at_2_0_extension_count_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_208_bull_trap_at_2_0_extension_count_252d},
    "f08_fibx_209_bear_trap_at_786_retracement_count_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_209_bear_trap_at_786_retracement_count_252d},
    "f08_fibx_210_extension_breakdown_recent_indicator_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_210_extension_breakdown_recent_indicator_medium},
    "f08_fibx_211_count_extension_breakdowns_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_211_count_extension_breakdowns_252d},
    "f08_fibx_212_count_failed_retracements_below_786_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_212_count_failed_retracements_below_786_252d},
    "f08_fibx_213_fib_terminal_blowoff_composite_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_213_fib_terminal_blowoff_composite_252d},
    "f08_fibx_214_fib_capitulation_composite_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_214_fib_capitulation_composite_252d},
    "f08_fibx_215_parabolic_fib_progression_indicator_medium": {"inputs": ["high", "low", "close"], "func": f08_fibx_215_parabolic_fib_progression_indicator_medium},
    "f08_fibx_216_fib_exhaustion_score_breach_count_extreme": {"inputs": ["high", "low", "close"], "func": f08_fibx_216_fib_exhaustion_score_breach_count_extreme},
    "f08_fibx_217_fib_compression_score_no_extension_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_217_fib_compression_score_no_extension_252d},
    "f08_fibx_218_extension_zone_residence_time_long_swing": {"inputs": ["high", "low", "close"], "func": f08_fibx_218_extension_zone_residence_time_long_swing},
    "f08_fibx_219_weighted_extension_across_S_M_L_swings": {"inputs": ["high", "low", "close"], "func": f08_fibx_219_weighted_extension_across_S_M_L_swings},
    "f08_fibx_220_log_ratio_short_swing_ext_to_long_swing_ext": {"inputs": ["high", "low", "close"], "func": f08_fibx_220_log_ratio_short_swing_ext_to_long_swing_ext},
    "f08_fibx_221_extension_top_warning_composite_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_221_extension_top_warning_composite_252d},
    "f08_fibx_222_breakdown_warning_composite_252d": {"inputs": ["high", "low", "close"], "func": f08_fibx_222_breakdown_warning_composite_252d},
    "f08_fibx_223_bearish_engulfing_of_fib_levels_indicator": {"inputs": ["high", "low", "close"], "func": f08_fibx_223_bearish_engulfing_of_fib_levels_indicator},
    "f08_fibx_224_extension_velocity_acceleration_decline_composite": {"inputs": ["high", "low", "close"], "func": f08_fibx_224_extension_velocity_acceleration_decline_composite},
    "f08_fibx_225_full_top_signature_score_weighted": {"inputs": ["high", "low", "close"], "func": f08_fibx_225_full_top_signature_score_weighted},
}
