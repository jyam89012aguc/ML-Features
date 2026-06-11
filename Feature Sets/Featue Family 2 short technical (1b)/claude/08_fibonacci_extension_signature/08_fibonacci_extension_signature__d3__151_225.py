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
    return _safe_div(sh - price, sh - sl)


def _bear_extension_value(price, sh, sl):
    return _safe_div(sh - price, sh - sl)


def _zigzag_pivots(close, threshold):
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


def f08_fibx_151_log_dist_below_0_618_retracement_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.618)  # = sl + 0.382*(sh-sl), i.e. retracement to 0.618 level
    return _safe_log(target) - _safe_log(close)


def f08_fibx_152_log_dist_below_0_786_retracement_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.786)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_153_log_dist_below_0_382_retracement_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.382)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_154_current_retracement_value_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))


def f08_fibx_155_current_retracement_value_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _retracement_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))


def f08_fibx_156_golden_pocket_retracement_indicator_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return ((rv >= 0.618) & (rv <= 0.65)).astype(float).where(rv.notna(), np.nan)


def f08_fibx_157_failed_retracement_below_786_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return (rv > 0.786).astype(float).where(rv.notna(), np.nan)


def f08_fibx_158_retracement_zone_id_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    sh = _swing_high(high, SW_M)
    return _safe_log(sh) - _safe_log(close)


def f08_fibx_160_retracement_velocity_5d_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return rv - rv.shift(WDAYS)


def f08_fibx_161_retracement_acceleration_5d_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return rv.diff(WDAYS).diff(WDAYS)


def f08_fibx_162_retracement_drawdown_from_swing_high_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sh = _swing_high(high, SW_M)
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_div(sh - close, atr)


def f08_fibx_163_shallow_retracement_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    rv = _retracement_value(close, sl, sh)
    changed = sl.ne(sl.shift(1)).fillna(False)
    idx_at = np.where(changed.to_numpy(), np.arange(len(close)), np.nan)
    last_idx = pd.Series(idx_at, index=close.index).ffill()
    age = pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_idx
    return ((rv < 0.236) & (age > MDAYS)).astype(float).where(rv.notna(), np.nan)


def f08_fibx_164_deep_retracement_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return (rv > 0.786).astype(float).where(rv.notna(), np.nan)



def _harmonic_pattern_detector(close, threshold, ab_lo, ab_hi, bc_lo, bc_hi, cd_lo, cd_hi, xd_lo, xd_hi):
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
    return _harmonic_pattern_detector(close, 0.05, 0.568, 0.668, 0.382, 0.886, 1.13, 1.618, 0.736, 0.836)


def f08_fibx_166_butterfly_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _harmonic_pattern_detector(close, 0.05, 0.736, 0.836, 0.382, 0.886, 1.618, 2.618, 1.27, 1.618)


def f08_fibx_167_bat_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _harmonic_pattern_detector(close, 0.05, 0.382, 0.5, 0.382, 0.886, 1.618, 2.618, 0.836, 0.936)


def f08_fibx_168_crab_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _harmonic_pattern_detector(close, 0.05, 0.382, 0.618, 0.382, 0.886, 2.618, 3.618, 1.55, 1.68)


def f08_fibx_169_cypher_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _harmonic_pattern_detector(close, 0.05, 0.382, 0.618, 1.13, 1.414, 0.6, 1.2, 0.736, 0.836)


def f08_fibx_170_shark_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _harmonic_pattern_detector(close, 0.05, 0.382, 0.618, 1.13, 1.618, 1.618, 2.24, 0.836, 1.18)


def f08_fibx_171_five_zero_pattern_indicator_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _harmonic_pattern_detector(close, 0.05, 1.13, 1.618, 1.618, 2.24, 0.45, 0.55, 0.5, 2.0)


def f08_fibx_172_any_harmonic_pattern_count_252d_5pct(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    out_v, _ = _last_n_zigzag_pivots(close, 0.05, 5)
    d_point = pd.Series(out_v[:, 4], index=close.index).ffill()
    return _safe_log(close) - _safe_log(d_point)



def _confluence_count_for_ratio(high, low, close, ratio, tol_atr=1.0):
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
    return _confluence_count_for_ratio(high, low, close, 1.618, tol_atr=1.0)


def f08_fibx_176_confluence_count_anchors_at_2_0_within_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _confluence_count_for_ratio(high, low, close, 2.0, tol_atr=1.0)


def f08_fibx_177_confluence_count_anchors_at_2_618_within_atr(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _confluence_count_for_ratio(high, low, close, 2.618, tol_atr=1.0)


def f08_fibx_178_closest_confluent_fib_above_close_log_dist(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
        for lvl in above:
            n_near = np.sum(np.abs(above - lvl) <= 2 * a)
            if n_near >= 2:
                out[i] = float(np.log(lvl) - np.log(c))
                break
    return pd.Series(out, index=close.index)


def f08_fibx_179_closest_confluent_fib_below_close_log_dist(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    above = f08_fibx_178_closest_confluent_fib_above_close_log_dist(high, low, close)
    below = f08_fibx_179_closest_confluent_fib_below_close_log_dist(high, low, close)
    closer_above = above.where(above < below.fillna(np.inf), -below)
    return closer_above



def _bear_swing_pivots(high, low, n):
    sh = _swing_high(high, n)
    sl = _swing_low(low, n)
    return sh, sl


def f08_fibx_182_bear_swing_extension_value_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    return _safe_div(sl - close, sh - sl)


def f08_fibx_183_log_dist_below_neg_0_272_bear_extension_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    target = sl - 0.272 * (sh - sl)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_184_log_dist_below_neg_0_618_bear_extension_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    target = sl - 0.618 * (sh - sl)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_185_log_dist_below_neg_1_0_measured_move_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    target = sl - (sh - sl)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_186_log_dist_below_neg_1_618_bear_extension_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    target = sl - 1.618 * (sh - sl)
    return _safe_log(target) - _safe_log(close)


def f08_fibx_187_count_bear_fib_levels_breached_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    cnt = pd.Series(0.0, index=close.index)
    valid = sh.notna() & sl.notna()
    for r in [0.272, 0.618, 1.0, 1.618, 2.618]:
        cnt = cnt + (close < (sl - r * (sh - sl))).astype(float)
    return cnt.where(valid, np.nan)


def f08_fibx_188_bear_abcd_measured_move_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sh, sl = _bear_swing_pivots(high, low, SW_M)
    down_leg1 = sh - sl
    down_leg2 = sl - close
    r = _safe_div(down_leg2, down_leg1)
    return ((r >= 0.9) & (r <= 1.1)).astype(float).where(r.notna(), np.nan)



def _bars_since_event(event):
    idx_at = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last = pd.Series(idx_at, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last


def f08_fibx_189_distance_to_nearest_fib_time_window_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    dist = f08_fibx_189_distance_to_nearest_fib_time_window_medium(high, low, close)
    return _safe_div(1.0, 1.0 + dist.abs())


def f08_fibx_191_current_leg_duration_vs_fib_of_prior_leg_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    pv, _, pidx = _zigzag_pivots(close, 0.05)
    last_ext_idx = pd.Series(pidx, index=close.index).ffill()
    cur_dur = pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_ext_idx
    prior_idx = pd.Series(pidx, index=close.index).ffill().shift(1)
    prior_dur = last_ext_idx - prior_idx
    return _safe_div(cur_dur, 1.618 * prior_dur)



def f08_fibx_192_log_dist_above_1_618_atr_above_21d_sma(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_log(close) - _safe_log(sma + 1.618 * atr)


def f08_fibx_193_log_dist_above_2_618_atr_above_63d_sma(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    return _safe_log(close) - _safe_log(sma + 2.618 * atr)


def f08_fibx_194_above_2_618_atr_band_indicator_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    return (close > sma + 2.618 * atr).astype(float).where(sma.notna() & atr.notna(), np.nan)


def f08_fibx_195_count_band_touches_above_1_618_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    atr = _atr(high, low, close, n=MDAYS)
    band = sma + 1.618 * atr
    return (high >= band).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()



def f08_fibx_196_mean_volume_when_close_within_1pct_of_1_618_fib_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.618)
    near = (close - target).abs() <= 0.01 * close
    vol_near = volume.where(near, np.nan)
    return vol_near.rolling(QDAYS, min_periods=WDAYS).mean()


def f08_fibx_197_volume_zscore_when_at_1_618_fib_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.618)
    near = (close - target).abs() <= 0.01 * close
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    return vz.where(near, np.nan).ffill()


def f08_fibx_198_cum_volume_at_fib_extension_zones_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    at_any = pd.Series(False, index=close.index)
    for r in [1.272, 1.618, 2.0, 2.618]:
        target = _fib_target(sl, sh, r)
        at_any = at_any | ((close - target).abs() <= 0.01 * close)
    return volume.where(at_any, 0.0).rolling(QDAYS, min_periods=WDAYS).sum()



def f08_fibx_199_count_1_618_touches_with_reversal_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.618)
    touched = (high >= target) & (target > 0)
    touched_lag = touched.shift(WDAYS).fillna(False)
    target_lag = target.shift(WDAYS)
    reversed_ = (close < 0.98 * target_lag)
    event = touched_lag & reversed_
    return event.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_200_fib_1_618_resistance_hit_rate_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rev = f08_fibx_199_count_1_618_touches_with_reversal_252d(high, low, close)
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.618)
    touched = (high >= target).shift(WDAYS).astype(float)
    tot = touched.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(rev, tot)


def f08_fibx_201_count_0_618_retracement_bounces_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.618)  # 0.382 level
    touched_low = (low <= target) & (target > 0)
    touched_lag = touched_low.shift(WDAYS).fillna(False)
    target_lag = target.shift(WDAYS)
    bounced = (close > 1.02 * target_lag)
    return (touched_lag & bounced).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_202_mean_5d_bounce_magnitude_from_0_618_retracement_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.618)
    touched_lag = ((low <= target) & (target > 0)).shift(WDAYS).fillna(False)
    log_ret = _safe_log(close) - _safe_log(close.shift(WDAYS))
    return log_ret.where(touched_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f08_fibx_203_fib_level_reliability_score_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res_rate = f08_fibx_200_fib_1_618_resistance_hit_rate_252d(high, low, close)
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.618)
    touched = ((low <= target) & (target > 0)).shift(WDAYS).astype(float)
    bounces = f08_fibx_201_count_0_618_retracement_bounces_252d(high, low, close)
    tot = touched.rolling(YDAYS, min_periods=QDAYS).sum()
    bounce_rate = _safe_div(bounces, tot)
    return res_rate.fillna(0) + 0.5 * bounce_rate.fillna(0)



def f08_fibx_204_log_dist_above_1_618_of_oldest_swing_low_in_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    n = len(close); low_arr = low.to_numpy(); high_arr = high.to_numpy(); close_arr = close.to_numpy()
    sl_series = _swing_low(low, SW_M); sh_series = _swing_high(high, SW_M)
    sl_arr = sl_series.to_numpy(); sh_arr = sh_series.to_numpy()
    out = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - YDAYS + 1)
        win_sl = sl_arr[start:i + 1]; win_sh = sh_arr[start:i + 1]
        valid_idx = np.where(~np.isnan(win_sl) & ~np.isnan(win_sh))[0]
        if valid_idx.size == 0: continue
        oi = valid_idx[0]
        sl_val = win_sl[oi]; sh_val = win_sh[oi]
        target = sl_val + 1.618 * (sh_val - sl_val)
        if target > 0 and close_arr[i] > 0:
            out[i] = float(np.log(close_arr[i]) - np.log(target))
    return pd.Series(out, index=close.index)


def f08_fibx_205_log_dist_above_1_618_of_2nd_most_recent_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl_series = _swing_low(low, SW_M); sh_series = _swing_high(high, SW_M)
    sl_prior = sl_series.where(sl_series.ne(sl_series.shift(1))).ffill().shift(1)
    sh_prior = sh_series.where(sh_series.ne(sh_series.shift(1))).ffill().shift(1)
    target = sl_prior + 1.618 * (sh_prior - sl_prior)
    return _safe_log(close) - _safe_log(target)


def f08_fibx_206_count_swings_whose_1_618_ext_close_exceeds_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target_new = _fib_target(sl, sh, 1.618)
    new_dist = _safe_log(close) - _safe_log(target_new)
    old_dist = f08_fibx_204_log_dist_above_1_618_of_oldest_swing_low_in_252d(high, low, close)
    return new_dist - old_dist



def f08_fibx_208_bull_trap_at_2_0_extension_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 2.0)
    touched = (high >= target) & (target > 0)
    touched_lag = touched.shift(WDAYS).fillna(False)
    close_at_touch_lag = close.shift(WDAYS)
    trap = (close < 0.95 * close_at_touch_lag)
    return (touched_lag & trap).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_209_bear_trap_at_786_retracement_count_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    target = _fib_target(sl, sh, 1.0 - 0.786)
    touched_low = (low <= target) & (target > 0)
    touched_lag = touched_low.shift(WDAYS).fillna(False)
    close_at_touch_lag = close.shift(WDAYS)
    trap = (close > 1.05 * close_at_touch_lag)
    return (touched_lag & trap).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_210_extension_breakdown_recent_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    above_1618_recent = (close > _fib_target(sl, sh, 1.618)).rolling(MDAYS, min_periods=1).max().astype(float)
    below_1272_now = (close < _fib_target(sl, sh, 1.272)).astype(float)
    return ((above_1618_recent == 1) & (below_1272_now == 1)).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_211_count_extension_breakdowns_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ev = f08_fibx_210_extension_breakdown_recent_indicator_medium(high, low, close).fillna(0)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_212_count_failed_retracements_below_786_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return (rv > 0.786).fillna(False).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()



def f08_fibx_213_fib_terminal_blowoff_composite_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    bev = f08_fibx_182_bear_swing_extension_value_medium(high, low, close)
    below = (bev > 0.618).astype(float)
    rv = _retracement_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    no_recovery = (rv > 0.618).rolling(MDAYS, min_periods=WDAYS).min().astype(float)
    return below + no_recovery


def f08_fibx_215_parabolic_fib_progression_indicator_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    score = pd.Series(0.0, index=close.index)
    for nw in [SW_S, SW_M, SW_L]:
        sl = _swing_low(low, nw); sh = _swing_high(high, nw)
        for r in [2.0, 2.618, 4.236]:
            score = score + (close > _fib_target(sl, sh, r)).astype(float)
    return score


def f08_fibx_217_fib_compression_score_no_extension_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    score = pd.Series(0.0, index=close.index)
    for nw in [SW_S, SW_M, SW_L]:
        sl = _swing_low(low, nw); sh = _swing_high(high, nw)
        for r in [1.272, 1.618, 2.0, 2.618]:
            breached_in_252 = (close > _fib_target(sl, sh, r)).astype(float).rolling(YDAYS, min_periods=QDAYS).max()
            score = score + (breached_in_252 == 0).astype(float)
    return score


def f08_fibx_218_extension_zone_residence_time_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    rv = _ext_value(close, sl, sh)
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
    es = _ext_value(close, _swing_low(low, SW_S), _swing_high(high, SW_S))
    em = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    el = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return (1.0 * es + 3.0 * em + 9.0 * el) / 13.0


def f08_fibx_220_log_ratio_short_swing_ext_to_long_swing_ext(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    es = _ext_value(close, _swing_low(low, SW_S), _swing_high(high, SW_S))
    el = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return _safe_log(es) - _safe_log(el)


def f08_fibx_221_extension_top_warning_composite_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    para = f08_fibx_215_parabolic_fib_progression_indicator_medium(high, low, close).fillna(0)
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    at_2_0 = (close > _fib_target(sl, sh, 2.0)).astype(float)
    traps = f08_fibx_208_bull_trap_at_2_0_extension_count_252d(high, low, close).fillna(0)
    return para + at_2_0 + (traps > 0).astype(float)


def f08_fibx_222_breakdown_warning_composite_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    below_1 = (close < sh).astype(float)
    recent_above_1618 = ((close > _fib_target(sl, sh, 1.618)).rolling(MDAYS, min_periods=WDAYS).max()).astype(float)
    rv = _retracement_value(close, sl, sh)
    deep_retrace = (rv > 0.5).astype(float)
    return below_1 + recent_above_1618 + deep_retrace


def f08_fibx_223_bearish_engulfing_of_fib_levels_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    tgt1 = _fib_target(sl, sh, 1.272)
    tgt2 = _fib_target(sl, sh, 1.618)
    engulf = (low <= tgt1) & (high >= tgt2)
    pos = _safe_div(close - low, high - low)
    weak_close = pos < 0.4
    return (engulf & weak_close).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_224_extension_velocity_acceleration_decline_composite(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
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
    a = f08_fibx_213_fib_terminal_blowoff_composite_252d(high, low, close).fillna(0)
    b = f08_fibx_215_parabolic_fib_progression_indicator_medium(high, low, close).fillna(0)
    c = (f08_fibx_208_bull_trap_at_2_0_extension_count_252d(high, low, close).fillna(0) > 0).astype(float)
    d = f08_fibx_224_extension_velocity_acceleration_decline_composite(high, low, close).fillna(0)
    return 3.0 * a + 2.0 * b + c + d




def f08_fibx_151_log_dist_below_0_618_retracement_medium_swing_d3(high, low, close): return f08_fibx_151_log_dist_below_0_618_retracement_medium_swing(high, low, close).diff().diff().diff()

def f08_fibx_152_log_dist_below_0_786_retracement_medium_swing_d3(high, low, close): return f08_fibx_152_log_dist_below_0_786_retracement_medium_swing(high, low, close).diff().diff().diff()

def f08_fibx_153_log_dist_below_0_382_retracement_medium_swing_d3(high, low, close): return f08_fibx_153_log_dist_below_0_382_retracement_medium_swing(high, low, close).diff().diff().diff()

def f08_fibx_154_current_retracement_value_medium_swing_d3(high, low, close): return f08_fibx_154_current_retracement_value_medium_swing(high, low, close).diff().diff().diff()

def f08_fibx_155_current_retracement_value_long_swing_d3(high, low, close): return f08_fibx_155_current_retracement_value_long_swing(high, low, close).diff().diff().diff()

def f08_fibx_156_golden_pocket_retracement_indicator_medium_swing_d3(high, low, close): return f08_fibx_156_golden_pocket_retracement_indicator_medium_swing(high, low, close).diff().diff().diff()

def f08_fibx_157_failed_retracement_below_786_indicator_medium_d3(high, low, close): return f08_fibx_157_failed_retracement_below_786_indicator_medium(high, low, close).diff().diff().diff()

def f08_fibx_158_retracement_zone_id_medium_swing_d3(high, low, close): return f08_fibx_158_retracement_zone_id_medium_swing(high, low, close).diff().diff().diff()

def f08_fibx_159_pullback_log_depth_from_peak_medium_swing_d3(high, low, close): return f08_fibx_159_pullback_log_depth_from_peak_medium_swing(high, low, close).diff().diff().diff()

def f08_fibx_160_retracement_velocity_5d_medium_d3(high, low, close): return f08_fibx_160_retracement_velocity_5d_medium(high, low, close).diff().diff().diff()

def f08_fibx_161_retracement_acceleration_5d_medium_d3(high, low, close): return f08_fibx_161_retracement_acceleration_5d_medium(high, low, close).diff().diff().diff()

def f08_fibx_162_retracement_drawdown_from_swing_high_atr_d3(high, low, close): return f08_fibx_162_retracement_drawdown_from_swing_high_atr(high, low, close).diff().diff().diff()

def f08_fibx_163_shallow_retracement_indicator_medium_d3(high, low, close): return f08_fibx_163_shallow_retracement_indicator_medium(high, low, close).diff().diff().diff()

def f08_fibx_164_deep_retracement_indicator_medium_d3(high, low, close): return f08_fibx_164_deep_retracement_indicator_medium(high, low, close).diff().diff().diff()

def f08_fibx_165_gartley_pattern_indicator_5pct_d3(high, low, close): return f08_fibx_165_gartley_pattern_indicator_5pct(high, low, close).diff().diff().diff()

def f08_fibx_166_butterfly_pattern_indicator_5pct_d3(high, low, close): return f08_fibx_166_butterfly_pattern_indicator_5pct(high, low, close).diff().diff().diff()

def f08_fibx_167_bat_pattern_indicator_5pct_d3(high, low, close): return f08_fibx_167_bat_pattern_indicator_5pct(high, low, close).diff().diff().diff()

def f08_fibx_168_crab_pattern_indicator_5pct_d3(high, low, close): return f08_fibx_168_crab_pattern_indicator_5pct(high, low, close).diff().diff().diff()

def f08_fibx_169_cypher_pattern_indicator_5pct_d3(high, low, close): return f08_fibx_169_cypher_pattern_indicator_5pct(high, low, close).diff().diff().diff()

def f08_fibx_170_shark_pattern_indicator_5pct_d3(high, low, close): return f08_fibx_170_shark_pattern_indicator_5pct(high, low, close).diff().diff().diff()

def f08_fibx_171_five_zero_pattern_indicator_5pct_d3(high, low, close): return f08_fibx_171_five_zero_pattern_indicator_5pct(high, low, close).diff().diff().diff()

def f08_fibx_172_any_harmonic_pattern_count_252d_5pct_d3(high, low, close): return f08_fibx_172_any_harmonic_pattern_count_252d_5pct(high, low, close).diff().diff().diff()

def f08_fibx_173_bars_since_last_harmonic_completion_5pct_d3(high, low, close): return f08_fibx_173_bars_since_last_harmonic_completion_5pct(high, low, close).diff().diff().diff()

def f08_fibx_174_log_dist_close_to_d_point_of_recent_pattern_5pct_d3(high, low, close): return f08_fibx_174_log_dist_close_to_d_point_of_recent_pattern_5pct(high, low, close).diff().diff().diff()

def f08_fibx_175_confluence_count_anchors_at_1_618_within_atr_d3(high, low, close): return f08_fibx_175_confluence_count_anchors_at_1_618_within_atr(high, low, close).diff().diff().diff()

def f08_fibx_176_confluence_count_anchors_at_2_0_within_atr_d3(high, low, close): return f08_fibx_176_confluence_count_anchors_at_2_0_within_atr(high, low, close).diff().diff().diff()

def f08_fibx_177_confluence_count_anchors_at_2_618_within_atr_d3(high, low, close): return f08_fibx_177_confluence_count_anchors_at_2_618_within_atr(high, low, close).diff().diff().diff()

def f08_fibx_178_closest_confluent_fib_above_close_log_dist_d3(high, low, close): return f08_fibx_178_closest_confluent_fib_above_close_log_dist(high, low, close).diff().diff().diff()

def f08_fibx_179_closest_confluent_fib_below_close_log_dist_d3(high, low, close): return f08_fibx_179_closest_confluent_fib_below_close_log_dist(high, low, close).diff().diff().diff()

def f08_fibx_180_confluence_zone_density_total_within_atr_d3(high, low, close): return f08_fibx_180_confluence_zone_density_total_within_atr(high, low, close).diff().diff().diff()

def f08_fibx_181_magnet_fib_level_signed_log_dist_d3(high, low, close): return f08_fibx_181_magnet_fib_level_signed_log_dist(high, low, close).diff().diff().diff()

def f08_fibx_182_bear_swing_extension_value_medium_d3(high, low, close): return f08_fibx_182_bear_swing_extension_value_medium(high, low, close).diff().diff().diff()

def f08_fibx_183_log_dist_below_neg_0_272_bear_extension_medium_d3(high, low, close): return f08_fibx_183_log_dist_below_neg_0_272_bear_extension_medium(high, low, close).diff().diff().diff()

def f08_fibx_184_log_dist_below_neg_0_618_bear_extension_medium_d3(high, low, close): return f08_fibx_184_log_dist_below_neg_0_618_bear_extension_medium(high, low, close).diff().diff().diff()

def f08_fibx_185_log_dist_below_neg_1_0_measured_move_medium_d3(high, low, close): return f08_fibx_185_log_dist_below_neg_1_0_measured_move_medium(high, low, close).diff().diff().diff()

def f08_fibx_186_log_dist_below_neg_1_618_bear_extension_medium_d3(high, low, close): return f08_fibx_186_log_dist_below_neg_1_618_bear_extension_medium(high, low, close).diff().diff().diff()

def f08_fibx_187_count_bear_fib_levels_breached_medium_d3(high, low, close): return f08_fibx_187_count_bear_fib_levels_breached_medium(high, low, close).diff().diff().diff()

def f08_fibx_188_bear_abcd_measured_move_indicator_medium_d3(high, low, close): return f08_fibx_188_bear_abcd_measured_move_indicator_medium(high, low, close).diff().diff().diff()

def f08_fibx_189_distance_to_nearest_fib_time_window_medium_d3(high, low, close): return f08_fibx_189_distance_to_nearest_fib_time_window_medium(high, low, close).diff().diff().diff()

def f08_fibx_190_fib_time_target_proximity_score_medium_d3(high, low, close): return f08_fibx_190_fib_time_target_proximity_score_medium(high, low, close).diff().diff().diff()

def f08_fibx_191_current_leg_duration_vs_fib_of_prior_leg_medium_d3(high, low, close): return f08_fibx_191_current_leg_duration_vs_fib_of_prior_leg_medium(high, low, close).diff().diff().diff()

def f08_fibx_192_log_dist_above_1_618_atr_above_21d_sma_d3(high, low, close): return f08_fibx_192_log_dist_above_1_618_atr_above_21d_sma(high, low, close).diff().diff().diff()

def f08_fibx_193_log_dist_above_2_618_atr_above_63d_sma_d3(high, low, close): return f08_fibx_193_log_dist_above_2_618_atr_above_63d_sma(high, low, close).diff().diff().diff()

def f08_fibx_194_above_2_618_atr_band_indicator_63d_d3(high, low, close): return f08_fibx_194_above_2_618_atr_band_indicator_63d(high, low, close).diff().diff().diff()

def f08_fibx_195_count_band_touches_above_1_618_252d_d3(high, low, close): return f08_fibx_195_count_band_touches_above_1_618_252d(high, low, close).diff().diff().diff()

def f08_fibx_196_mean_volume_when_close_within_1pct_of_1_618_fib_63d_d3(high, low, close, volume): return f08_fibx_196_mean_volume_when_close_within_1pct_of_1_618_fib_63d(high, low, close, volume).diff().diff().diff()

def f08_fibx_197_volume_zscore_when_at_1_618_fib_252d_d3(high, low, close, volume): return f08_fibx_197_volume_zscore_when_at_1_618_fib_252d(high, low, close, volume).diff().diff().diff()

def f08_fibx_198_cum_volume_at_fib_extension_zones_63d_d3(high, low, close, volume): return f08_fibx_198_cum_volume_at_fib_extension_zones_63d(high, low, close, volume).diff().diff().diff()

def f08_fibx_199_count_1_618_touches_with_reversal_252d_d3(high, low, close): return f08_fibx_199_count_1_618_touches_with_reversal_252d(high, low, close).diff().diff().diff()

def f08_fibx_200_fib_1_618_resistance_hit_rate_252d_d3(high, low, close): return f08_fibx_200_fib_1_618_resistance_hit_rate_252d(high, low, close).diff().diff().diff()

def f08_fibx_201_count_0_618_retracement_bounces_252d_d3(high, low, close): return f08_fibx_201_count_0_618_retracement_bounces_252d(high, low, close).diff().diff().diff()

def f08_fibx_202_mean_5d_bounce_magnitude_from_0_618_retracement_252d_d3(high, low, close): return f08_fibx_202_mean_5d_bounce_magnitude_from_0_618_retracement_252d(high, low, close).diff().diff().diff()

def f08_fibx_203_fib_level_reliability_score_medium_d3(high, low, close): return f08_fibx_203_fib_level_reliability_score_medium(high, low, close).diff().diff().diff()

def f08_fibx_204_log_dist_above_1_618_of_oldest_swing_low_in_252d_d3(high, low, close): return f08_fibx_204_log_dist_above_1_618_of_oldest_swing_low_in_252d(high, low, close).diff().diff().diff()

def f08_fibx_205_log_dist_above_1_618_of_2nd_most_recent_swing_d3(high, low, close): return f08_fibx_205_log_dist_above_1_618_of_2nd_most_recent_swing(high, low, close).diff().diff().diff()

def f08_fibx_206_count_swings_whose_1_618_ext_close_exceeds_medium_d3(high, low, close): return f08_fibx_206_count_swings_whose_1_618_ext_close_exceeds_medium(high, low, close).diff().diff().diff()

def f08_fibx_207_extension_disagreement_oldest_vs_newest_swing_log_d3(high, low, close): return f08_fibx_207_extension_disagreement_oldest_vs_newest_swing_log(high, low, close).diff().diff().diff()

def f08_fibx_208_bull_trap_at_2_0_extension_count_252d_d3(high, low, close): return f08_fibx_208_bull_trap_at_2_0_extension_count_252d(high, low, close).diff().diff().diff()

def f08_fibx_209_bear_trap_at_786_retracement_count_252d_d3(high, low, close): return f08_fibx_209_bear_trap_at_786_retracement_count_252d(high, low, close).diff().diff().diff()

def f08_fibx_210_extension_breakdown_recent_indicator_medium_d3(high, low, close): return f08_fibx_210_extension_breakdown_recent_indicator_medium(high, low, close).diff().diff().diff()

def f08_fibx_211_count_extension_breakdowns_252d_d3(high, low, close): return f08_fibx_211_count_extension_breakdowns_252d(high, low, close).diff().diff().diff()

def f08_fibx_212_count_failed_retracements_below_786_252d_d3(high, low, close): return f08_fibx_212_count_failed_retracements_below_786_252d(high, low, close).diff().diff().diff()

def f08_fibx_213_fib_terminal_blowoff_composite_252d_d3(high, low, close): return f08_fibx_213_fib_terminal_blowoff_composite_252d(high, low, close).diff().diff().diff()

def f08_fibx_214_fib_capitulation_composite_252d_d3(high, low, close): return f08_fibx_214_fib_capitulation_composite_252d(high, low, close).diff().diff().diff()

def f08_fibx_215_parabolic_fib_progression_indicator_medium_d3(high, low, close): return f08_fibx_215_parabolic_fib_progression_indicator_medium(high, low, close).diff().diff().diff()

def f08_fibx_216_fib_exhaustion_score_breach_count_extreme_d3(high, low, close): return f08_fibx_216_fib_exhaustion_score_breach_count_extreme(high, low, close).diff().diff().diff()

def f08_fibx_217_fib_compression_score_no_extension_252d_d3(high, low, close): return f08_fibx_217_fib_compression_score_no_extension_252d(high, low, close).diff().diff().diff()

def f08_fibx_218_extension_zone_residence_time_long_swing_d3(high, low, close): return f08_fibx_218_extension_zone_residence_time_long_swing(high, low, close).diff().diff().diff()

def f08_fibx_219_weighted_extension_across_S_M_L_swings_d3(high, low, close): return f08_fibx_219_weighted_extension_across_S_M_L_swings(high, low, close).diff().diff().diff()

def f08_fibx_220_log_ratio_short_swing_ext_to_long_swing_ext_d3(high, low, close): return f08_fibx_220_log_ratio_short_swing_ext_to_long_swing_ext(high, low, close).diff().diff().diff()

def f08_fibx_221_extension_top_warning_composite_252d_d3(high, low, close): return f08_fibx_221_extension_top_warning_composite_252d(high, low, close).diff().diff().diff()

def f08_fibx_222_breakdown_warning_composite_252d_d3(high, low, close): return f08_fibx_222_breakdown_warning_composite_252d(high, low, close).diff().diff().diff()

def f08_fibx_223_bearish_engulfing_of_fib_levels_indicator_d3(high, low, close): return f08_fibx_223_bearish_engulfing_of_fib_levels_indicator(high, low, close).diff().diff().diff()

def f08_fibx_224_extension_velocity_acceleration_decline_composite_d3(high, low, close): return f08_fibx_224_extension_velocity_acceleration_decline_composite(high, low, close).diff().diff().diff()

def f08_fibx_225_full_top_signature_score_weighted_d3(high, low, close): return f08_fibx_225_full_top_signature_score_weighted(high, low, close).diff().diff().diff()


FIBONACCI_EXTENSION_SIGNATURE_D3_REGISTRY_151_225 = {
    "f08_fibx_151_log_dist_below_0_618_retracement_medium_swing_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_151_log_dist_below_0_618_retracement_medium_swing_d3},
    "f08_fibx_152_log_dist_below_0_786_retracement_medium_swing_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_152_log_dist_below_0_786_retracement_medium_swing_d3},
    "f08_fibx_153_log_dist_below_0_382_retracement_medium_swing_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_153_log_dist_below_0_382_retracement_medium_swing_d3},
    "f08_fibx_154_current_retracement_value_medium_swing_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_154_current_retracement_value_medium_swing_d3},
    "f08_fibx_155_current_retracement_value_long_swing_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_155_current_retracement_value_long_swing_d3},
    "f08_fibx_156_golden_pocket_retracement_indicator_medium_swing_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_156_golden_pocket_retracement_indicator_medium_swing_d3},
    "f08_fibx_157_failed_retracement_below_786_indicator_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_157_failed_retracement_below_786_indicator_medium_d3},
    "f08_fibx_158_retracement_zone_id_medium_swing_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_158_retracement_zone_id_medium_swing_d3},
    "f08_fibx_159_pullback_log_depth_from_peak_medium_swing_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_159_pullback_log_depth_from_peak_medium_swing_d3},
    "f08_fibx_160_retracement_velocity_5d_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_160_retracement_velocity_5d_medium_d3},
    "f08_fibx_161_retracement_acceleration_5d_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_161_retracement_acceleration_5d_medium_d3},
    "f08_fibx_162_retracement_drawdown_from_swing_high_atr_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_162_retracement_drawdown_from_swing_high_atr_d3},
    "f08_fibx_163_shallow_retracement_indicator_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_163_shallow_retracement_indicator_medium_d3},
    "f08_fibx_164_deep_retracement_indicator_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_164_deep_retracement_indicator_medium_d3},
    "f08_fibx_165_gartley_pattern_indicator_5pct_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_165_gartley_pattern_indicator_5pct_d3},
    "f08_fibx_166_butterfly_pattern_indicator_5pct_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_166_butterfly_pattern_indicator_5pct_d3},
    "f08_fibx_167_bat_pattern_indicator_5pct_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_167_bat_pattern_indicator_5pct_d3},
    "f08_fibx_168_crab_pattern_indicator_5pct_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_168_crab_pattern_indicator_5pct_d3},
    "f08_fibx_169_cypher_pattern_indicator_5pct_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_169_cypher_pattern_indicator_5pct_d3},
    "f08_fibx_170_shark_pattern_indicator_5pct_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_170_shark_pattern_indicator_5pct_d3},
    "f08_fibx_171_five_zero_pattern_indicator_5pct_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_171_five_zero_pattern_indicator_5pct_d3},
    "f08_fibx_172_any_harmonic_pattern_count_252d_5pct_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_172_any_harmonic_pattern_count_252d_5pct_d3},
    "f08_fibx_173_bars_since_last_harmonic_completion_5pct_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_173_bars_since_last_harmonic_completion_5pct_d3},
    "f08_fibx_174_log_dist_close_to_d_point_of_recent_pattern_5pct_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_174_log_dist_close_to_d_point_of_recent_pattern_5pct_d3},
    "f08_fibx_175_confluence_count_anchors_at_1_618_within_atr_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_175_confluence_count_anchors_at_1_618_within_atr_d3},
    "f08_fibx_176_confluence_count_anchors_at_2_0_within_atr_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_176_confluence_count_anchors_at_2_0_within_atr_d3},
    "f08_fibx_177_confluence_count_anchors_at_2_618_within_atr_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_177_confluence_count_anchors_at_2_618_within_atr_d3},
    "f08_fibx_178_closest_confluent_fib_above_close_log_dist_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_178_closest_confluent_fib_above_close_log_dist_d3},
    "f08_fibx_179_closest_confluent_fib_below_close_log_dist_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_179_closest_confluent_fib_below_close_log_dist_d3},
    "f08_fibx_180_confluence_zone_density_total_within_atr_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_180_confluence_zone_density_total_within_atr_d3},
    "f08_fibx_181_magnet_fib_level_signed_log_dist_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_181_magnet_fib_level_signed_log_dist_d3},
    "f08_fibx_182_bear_swing_extension_value_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_182_bear_swing_extension_value_medium_d3},
    "f08_fibx_183_log_dist_below_neg_0_272_bear_extension_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_183_log_dist_below_neg_0_272_bear_extension_medium_d3},
    "f08_fibx_184_log_dist_below_neg_0_618_bear_extension_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_184_log_dist_below_neg_0_618_bear_extension_medium_d3},
    "f08_fibx_185_log_dist_below_neg_1_0_measured_move_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_185_log_dist_below_neg_1_0_measured_move_medium_d3},
    "f08_fibx_186_log_dist_below_neg_1_618_bear_extension_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_186_log_dist_below_neg_1_618_bear_extension_medium_d3},
    "f08_fibx_187_count_bear_fib_levels_breached_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_187_count_bear_fib_levels_breached_medium_d3},
    "f08_fibx_188_bear_abcd_measured_move_indicator_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_188_bear_abcd_measured_move_indicator_medium_d3},
    "f08_fibx_189_distance_to_nearest_fib_time_window_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_189_distance_to_nearest_fib_time_window_medium_d3},
    "f08_fibx_190_fib_time_target_proximity_score_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_190_fib_time_target_proximity_score_medium_d3},
    "f08_fibx_191_current_leg_duration_vs_fib_of_prior_leg_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_191_current_leg_duration_vs_fib_of_prior_leg_medium_d3},
    "f08_fibx_192_log_dist_above_1_618_atr_above_21d_sma_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_192_log_dist_above_1_618_atr_above_21d_sma_d3},
    "f08_fibx_193_log_dist_above_2_618_atr_above_63d_sma_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_193_log_dist_above_2_618_atr_above_63d_sma_d3},
    "f08_fibx_194_above_2_618_atr_band_indicator_63d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_194_above_2_618_atr_band_indicator_63d_d3},
    "f08_fibx_195_count_band_touches_above_1_618_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_195_count_band_touches_above_1_618_252d_d3},
    "f08_fibx_196_mean_volume_when_close_within_1pct_of_1_618_fib_63d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f08_fibx_196_mean_volume_when_close_within_1pct_of_1_618_fib_63d_d3},
    "f08_fibx_197_volume_zscore_when_at_1_618_fib_252d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f08_fibx_197_volume_zscore_when_at_1_618_fib_252d_d3},
    "f08_fibx_198_cum_volume_at_fib_extension_zones_63d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f08_fibx_198_cum_volume_at_fib_extension_zones_63d_d3},
    "f08_fibx_199_count_1_618_touches_with_reversal_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_199_count_1_618_touches_with_reversal_252d_d3},
    "f08_fibx_200_fib_1_618_resistance_hit_rate_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_200_fib_1_618_resistance_hit_rate_252d_d3},
    "f08_fibx_201_count_0_618_retracement_bounces_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_201_count_0_618_retracement_bounces_252d_d3},
    "f08_fibx_202_mean_5d_bounce_magnitude_from_0_618_retracement_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_202_mean_5d_bounce_magnitude_from_0_618_retracement_252d_d3},
    "f08_fibx_203_fib_level_reliability_score_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_203_fib_level_reliability_score_medium_d3},
    "f08_fibx_204_log_dist_above_1_618_of_oldest_swing_low_in_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_204_log_dist_above_1_618_of_oldest_swing_low_in_252d_d3},
    "f08_fibx_205_log_dist_above_1_618_of_2nd_most_recent_swing_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_205_log_dist_above_1_618_of_2nd_most_recent_swing_d3},
    "f08_fibx_206_count_swings_whose_1_618_ext_close_exceeds_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_206_count_swings_whose_1_618_ext_close_exceeds_medium_d3},
    "f08_fibx_207_extension_disagreement_oldest_vs_newest_swing_log_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_207_extension_disagreement_oldest_vs_newest_swing_log_d3},
    "f08_fibx_208_bull_trap_at_2_0_extension_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_208_bull_trap_at_2_0_extension_count_252d_d3},
    "f08_fibx_209_bear_trap_at_786_retracement_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_209_bear_trap_at_786_retracement_count_252d_d3},
    "f08_fibx_210_extension_breakdown_recent_indicator_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_210_extension_breakdown_recent_indicator_medium_d3},
    "f08_fibx_211_count_extension_breakdowns_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_211_count_extension_breakdowns_252d_d3},
    "f08_fibx_212_count_failed_retracements_below_786_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_212_count_failed_retracements_below_786_252d_d3},
    "f08_fibx_213_fib_terminal_blowoff_composite_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_213_fib_terminal_blowoff_composite_252d_d3},
    "f08_fibx_214_fib_capitulation_composite_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_214_fib_capitulation_composite_252d_d3},
    "f08_fibx_215_parabolic_fib_progression_indicator_medium_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_215_parabolic_fib_progression_indicator_medium_d3},
    "f08_fibx_216_fib_exhaustion_score_breach_count_extreme_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_216_fib_exhaustion_score_breach_count_extreme_d3},
    "f08_fibx_217_fib_compression_score_no_extension_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_217_fib_compression_score_no_extension_252d_d3},
    "f08_fibx_218_extension_zone_residence_time_long_swing_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_218_extension_zone_residence_time_long_swing_d3},
    "f08_fibx_219_weighted_extension_across_S_M_L_swings_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_219_weighted_extension_across_S_M_L_swings_d3},
    "f08_fibx_220_log_ratio_short_swing_ext_to_long_swing_ext_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_220_log_ratio_short_swing_ext_to_long_swing_ext_d3},
    "f08_fibx_221_extension_top_warning_composite_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_221_extension_top_warning_composite_252d_d3},
    "f08_fibx_222_breakdown_warning_composite_252d_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_222_breakdown_warning_composite_252d_d3},
    "f08_fibx_223_bearish_engulfing_of_fib_levels_indicator_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_223_bearish_engulfing_of_fib_levels_indicator_d3},
    "f08_fibx_224_extension_velocity_acceleration_decline_composite_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_224_extension_velocity_acceleration_decline_composite_d3},
    "f08_fibx_225_full_top_signature_score_weighted_d3": {"inputs": ["high", "low", "close"], "func": f08_fibx_225_full_top_signature_score_weighted_d3},
}
