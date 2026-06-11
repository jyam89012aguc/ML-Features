"""jump_detection_signature d1 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Each feature
encodes a *different concept* in the jump-detection theme: jump-volume coupling
(continued), sign-pattern signatures, quadratic-variation decomposition,
Hawkes-style intensity, gap-up/gap-down distinction, intraday-range jumps,
post-jump persistence, jump-rate volatility, misc jump-structure descriptors.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). All sigma estimates used inside jump-event
indicators are constructed from a strictly prior window. Self-contained helpers
— no cross-family imports.
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


def _log_ret(close):
    return _safe_log(close).diff()


def _sigma_prior(r, n):
    return r.rolling(n, min_periods=max(n // 3, 2)).std().shift(1)


def _gap_ret(open, close):
    return _safe_log(open) - _safe_log(close.shift(1))


def _intraday_logHL(high, low):
    return _safe_log(high) - _safe_log(low)


# ============================================================
# Bucket H — Jump-volume coupling (continued; 076-080)
# ============================================================

def f38_jpdt_076_rolling_beta_absret_on_volz_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d OLS beta of |log-ret| on volume z-score — magnitude-volume sensitivity."""
    r = _log_ret(close).abs()
    volz = _rolling_zscore(volume, QDAYS).shift(1)
    cov = r.rolling(QDAYS, min_periods=MDAYS).cov(volz)
    var = volz.rolling(QDAYS, min_periods=MDAYS).var()
    return _safe_div(cov, var)


def f38_jpdt_077_high_vol_no_jump_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Decoupled-vol days: count of vol_z>2 AND |r|<σ_prior21 within 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    volz = _rolling_zscore(volume, QDAYS).shift(1)
    return ((volz > 2.0) & (r.abs() < sig)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_078_peak_volz_on_jump_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max volume z-score restricted to 3σ_21d jump days within 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    volz = _rolling_zscore(volume, QDAYS).shift(1)
    sel = volz.where(r.abs() > 3 * sig, np.nan)
    return sel.rolling(QDAYS, min_periods=MDAYS).max()


def f38_jpdt_079_corr_jump_ind_volz_ind_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr of (|r|>3σ_21d) indicator with (vol_z>2) indicator — co-occurrence."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    j = (r.abs() > 3 * sig).astype(float)
    volz = _rolling_zscore(volume, QDAYS).shift(1)
    vi = (volz > 2.0).astype(float)
    return j.rolling(YDAYS, min_periods=QDAYS).corr(vi)


def f38_jpdt_080_log_ratio_vol_jump_vs_nonjump_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log-ratio of mean volume on jump vs non-jump days over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    jmask = r.abs() > 3 * sig
    on = volume.where(jmask, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    off = volume.where(~jmask, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_log(on) - _safe_log(off)


# ============================================================
# Bucket I — Sign-pattern signatures (081-090)
# ============================================================

def f38_jpdt_081_alt_up_then_down_jump_pair_63d(close: pd.Series) -> pd.Series:
    """Echo-pair count: today is a down-jump preceded by an up-jump within prior 5 bars; summed 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up = (r > 3 * sig).astype(float)
    dn = (r < -3 * sig).astype(float)
    pair = (dn.astype(bool) & (up.shift(1).rolling(WDAYS, min_periods=1).max() > 0.5)).astype(float)
    return pair.rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_082_alt_down_then_up_jump_pair_63d(close: pd.Series) -> pd.Series:
    """Reflex-pair count: negative jump followed within 5 bars by positive jump in 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up = (r > 3 * sig).astype(float)
    dn = (r < -3 * sig).astype(float)
    pair = (up.astype(bool) & (dn.shift(1).rolling(WDAYS, min_periods=1).max() > 0.5)).astype(float)
    return pair.rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_083_ratio_updn_vs_dnup_pairs_252d(close: pd.Series) -> pd.Series:
    """Directional-sequence bias: (up→down pairs) / (down→up pairs) over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up = (r > 3 * sig).astype(float)
    dn = (r < -3 * sig).astype(float)
    updn = (dn.astype(bool) & (up.shift(1).rolling(WDAYS, min_periods=1).max() > 0.5)).astype(float)
    dnup = (up.astype(bool) & (dn.shift(1).rolling(WDAYS, min_periods=1).max() > 0.5)).astype(float)
    return _safe_div(updn.rolling(YDAYS, min_periods=QDAYS).sum(),
                     dnup.rolling(YDAYS, min_periods=QDAYS).sum())


def f38_jpdt_084_bull_jump_fraction_252d(close: pd.Series) -> pd.Series:
    """Directional jump tilt: up-jump count / total jump count (3σ_21d) over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up = (r > 3 * sig).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = (r.abs() > 3 * sig).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(up, tot)


def f38_jpdt_085_bear_jump_fraction_252d(close: pd.Series) -> pd.Series:
    """Downward jump tilt: down-jump count / total jump count over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    dn = (r < -3 * sig).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = (r.abs() > 3 * sig).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(dn, tot)


def f38_jpdt_086_net_jump_sign_tally_63d(close: pd.Series) -> pd.Series:
    """Sum of jump-day signs (3σ_21d) over 63d → directional momentum of shocks."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sgn = np.sign(r).where(r.abs() > 3 * sig, 0.0)
    return sgn.rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_087_longest_same_sign_jump_run_252d(close: pd.Series) -> pd.Series:
    """Longest run of same-sign 3σ_21d jumps within 252d window (ignoring non-jump bars)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sgn = np.sign(r).where(r.abs() > 3 * sig, 0.0).fillna(0.0)

    def _run(w):
        cur_sign = 0; cur = 0; mx = 0
        for v in w:
            if v == 0:
                continue
            if v == cur_sign:
                cur += 1
            else:
                cur_sign = v; cur = 1
            if cur > mx:
                mx = cur
        return mx
    return sgn.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True)


def f38_jpdt_088_climax_reversal_events_252d(close: pd.Series) -> pd.Series:
    """Climax-reversal pattern count: large positive r followed by large negative r next bar in 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up = (r.shift(1) > 3 * sig.shift(1))
    dn = (r < -3 * sig)
    return (up & dn).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_089_longest_dnonly_jump_run_252d(close: pd.Series) -> pd.Series:
    """Longest stretch of negative 3σ_21d jumps with no intervening positive jump in 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sgn = np.where(r > 3 * sig, 1, np.where(r < -3 * sig, -1, 0))
    s = pd.Series(sgn, index=r.index)

    def _run(w):
        cur = 0; mx = 0
        for v in w:
            if v == -1:
                cur += 1; mx = cur if cur > mx else mx
            elif v == 1:
                cur = 0
        return mx
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True)


def f38_jpdt_090_count_jump_sign_flips_63d(close: pd.Series) -> pd.Series:
    """Count of consecutive jump-day sign flips (up→down or down→up adjacent jumps) in 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    s = np.sign(r).where(r.abs() > 3 * sig, 0.0).fillna(0.0)

    def _flips(w):
        prev = 0; c = 0
        for v in w:
            if v == 0:
                continue
            if prev != 0 and v != prev:
                c += 1
            prev = v
        return c
    return s.rolling(QDAYS, min_periods=MDAYS).apply(_flips, raw=True)


# ============================================================
# Bucket J — Quadratic-variation decomposition (091-098)
# ============================================================

def _bv(r, n):
    pr = r.abs() * r.abs().shift(1)
    return (np.pi / 2.0) * pr.rolling(n, min_periods=max(n // 3, 2)).sum()


def _rv(r, n):
    return (r ** 2).rolling(n, min_periods=max(n // 3, 2)).sum()


def f38_jpdt_091_jump_variation_abs_21d(close: pd.Series) -> pd.Series:
    """Absolute jump variation: max(0, RV - BV) summed over 21d."""
    r = _log_ret(close)
    return (_rv(r, MDAYS) - _bv(r, MDAYS)).clip(lower=0.0)


def f38_jpdt_092_jump_variation_abs_252d(close: pd.Series) -> pd.Series:
    """Absolute jump variation at annual horizon: max(0, RV - BV) summed over 252d."""
    r = _log_ret(close)
    return (_rv(r, YDAYS) - _bv(r, YDAYS)).clip(lower=0.0)


def f38_jpdt_093_continuous_qv_bv_63d(close: pd.Series) -> pd.Series:
    """Continuous-component QV proxy: bipower variation over 63d (diffusion variance)."""
    r = _log_ret(close)
    return _bv(r, QDAYS)


def f38_jpdt_094_logdiff_jumpqv_vs_contqv_63d(close: pd.Series) -> pd.Series:
    """log(jump-QV + eps) − log(BV + eps) over 63d — log-scale jump-to-diffusion contrast."""
    r = _log_ret(close)
    jqv = (_rv(r, QDAYS) - _bv(r, QDAYS)).clip(lower=0.0)
    return _safe_log(jqv + 1e-12) - _safe_log(_bv(r, QDAYS) + 1e-12)


def f38_jpdt_095_jumpqv_zscore_within_252d(close: pd.Series) -> pd.Series:
    """Z-score of jump-QV(63d) within own past 252d → abnormal jump-activity flag."""
    r = _log_ret(close)
    jqv = (_rv(r, QDAYS) - _bv(r, QDAYS)).clip(lower=0.0)
    return _rolling_zscore(jqv, YDAYS)


def f38_jpdt_096_jumpqv_ratio_21_over_252(close: pd.Series) -> pd.Series:
    """Regime-shift indicator: jump-QV(21d) / jump-QV(252d) (recency of jump activity)."""
    r = _log_ret(close)
    jqv21 = (_rv(r, MDAYS) - _bv(r, MDAYS)).clip(lower=0.0)
    jqv252 = (_rv(r, YDAYS) - _bv(r, YDAYS)).clip(lower=0.0)
    return _safe_div(jqv21, jqv252)


def f38_jpdt_097_jumpqv_slope_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d slope of jump-QV (RV-BV) — rate of change of jump activity."""
    r = _log_ret(close)
    jqv = (_rv(r, QDAYS) - _bv(r, QDAYS)).clip(lower=0.0)
    return _rolling_slope(jqv, QDAYS)


def f38_jpdt_098_har_jump_coefficient_proxy_252d(close: pd.Series) -> pd.Series:
    """HAR-style jump-coefficient proxy: rolling 252d corr of today's RV with yesterday's jump-QV (causal)."""
    r = _log_ret(close)
    jqv = (_rv(r, MDAYS) - _bv(r, MDAYS)).clip(lower=0.0)
    today_rv = r ** 2
    prev_jqv = jqv.shift(1)
    return today_rv.rolling(YDAYS, min_periods=QDAYS).corr(prev_jqv)


# ============================================================
# Bucket K — Hawkes-style jump intensity proxies (099-106)
# ============================================================

def _hawkes_intensity(ind: pd.Series, half_life: float) -> pd.Series:
    alpha = 1.0 - 0.5 ** (1.0 / half_life)
    return ind.ewm(alpha=alpha, min_periods=int(half_life)).mean()


def f38_jpdt_099_hawkes_intensity_hl5(close: pd.Series) -> pd.Series:
    """Hawkes-style jump intensity (5-day half-life decay) — fast-memory regime."""
    r = _log_ret(close)
    ind = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return _hawkes_intensity(ind, 5.0)


def f38_jpdt_100_hawkes_intensity_hl21(close: pd.Series) -> pd.Series:
    """Hawkes-style jump intensity (21-day half-life) — short-term memory."""
    r = _log_ret(close)
    ind = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return _hawkes_intensity(ind, 21.0)


def f38_jpdt_101_hawkes_intensity_hl63(close: pd.Series) -> pd.Series:
    """Hawkes-style jump intensity (63-day half-life) — intermediate memory."""
    r = _log_ret(close)
    ind = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return _hawkes_intensity(ind, 63.0)


def f38_jpdt_102_hawkes_intensity_hl252(close: pd.Series) -> pd.Series:
    """Hawkes-style jump intensity (252-day half-life) — annual memory."""
    r = _log_ret(close)
    ind = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return _hawkes_intensity(ind, 252.0)


def f38_jpdt_103_hawkes_short_vs_long_ratio(close: pd.Series) -> pd.Series:
    """Hawkes 5-d-HL / Hawkes 63-d-HL — regime-shift in jump arrival rate."""
    r = _log_ret(close)
    ind = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return _safe_div(_hawkes_intensity(ind, 5.0), _hawkes_intensity(ind, 63.0))


def f38_jpdt_104_hawkes_short_minus_long(close: pd.Series) -> pd.Series:
    """Hawkes 5-d-HL − Hawkes 63-d-HL — fresh-vs-background jump arrival delta."""
    r = _log_ret(close)
    ind = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return _hawkes_intensity(ind, 5.0) - _hawkes_intensity(ind, 63.0)


def f38_jpdt_105_neg_jump_hawkes_hl21(close: pd.Series) -> pd.Series:
    """Down-jump-only Hawkes intensity (21-day half-life) — negative-shock arrival rate."""
    r = _log_ret(close)
    dn = (r < -3 * _sigma_prior(r, MDAYS)).astype(float)
    return _hawkes_intensity(dn, 21.0)


def f38_jpdt_106_pos_jump_hawkes_hl21(close: pd.Series) -> pd.Series:
    """Up-jump-only Hawkes intensity (21-day half-life) — positive-shock arrival rate."""
    r = _log_ret(close)
    up = (r > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return _hawkes_intensity(up, 21.0)


# ============================================================
# Bucket L — Gap-up vs gap-down distinction (107-112)
# ============================================================

def f38_jpdt_107_gap_down_count_3sig_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight gap-down event count: gap-ret < −3·σ_prior21_gap in 21d."""
    g = _gap_ret(open, close)
    return (g < -3 * _sigma_prior(g, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f38_jpdt_108_gap_down_count_4sig_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Annual extreme gap-down count: gap-ret < −4·σ_prior252_gap in 252d."""
    g = _gap_ret(open, close)
    return (g < -4 * _sigma_prior(g, YDAYS)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_109_gap_up_count_3sig_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight gap-up event count: gap-ret > +3·σ_prior21_gap in 21d."""
    g = _gap_ret(open, close)
    return (g > 3 * _sigma_prior(g, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f38_jpdt_110_ratio_gap_down_up_count_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight directional bias: gap-down count / gap-up count over 252d."""
    g = _gap_ret(open, close)
    sig = _sigma_prior(g, MDAYS)
    dn = (g < -3 * sig).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    up = (g > 3 * sig).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(dn, up)


def f38_jpdt_111_peak_gap_down_severity_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Peak overnight crash: min gap-ret / σ_prior252_c2c (negative ratio) within 63d."""
    g = _gap_ret(open, close)
    sig = _sigma_prior(_safe_log(close).diff(), YDAYS)
    return _safe_div(g, sig).rolling(QDAYS, min_periods=MDAYS).min()


def f38_jpdt_112_cum_gap_down_magnitude_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative gap-down severity: sum of (gap-ret · 1{gap<−3σ_prior21_gap}) over 252d."""
    g = _gap_ret(open, close)
    sig = _sigma_prior(g, MDAYS)
    return g.where(g < -3 * sig, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket M — Intraday-range jumps (113-118)
# ============================================================

def f38_jpdt_113_intraday_range_jump_count_3sig_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday-range jump count short: log(H/L) > 3·σ_prior21_logHL in 21d."""
    hl = _intraday_logHL(high, low)
    return (hl > 3 * _sigma_prior(hl, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f38_jpdt_114_intraday_range_jump_count_4sig_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday-range jump count annual: log(H/L) > 4·σ_prior252_logHL in 252d."""
    hl = _intraday_logHL(high, low)
    return (hl > 4 * _sigma_prior(hl, YDAYS)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_115_peak_intraday_range_shock_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Peak intraday-range shock: max log(H/L) / σ_prior252_logHL within 63d."""
    hl = _intraday_logHL(high, low)
    sig = _sigma_prior(hl, YDAYS)
    return _safe_div(hl, sig).rolling(QDAYS, min_periods=MDAYS).max()


def f38_jpdt_116_wide_bar_count_p95_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Wide-bar density short: log(H/L) > 252d-trailing 95th-pct, summed over 21d."""
    hl = _intraday_logHL(high, low)
    p95 = hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    return (hl > p95).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f38_jpdt_117_wide_bar_count_p95_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Wide-bar density intermediate: log(H/L) > 252d 95th-pct over 63d."""
    hl = _intraday_logHL(high, low)
    p95 = hl.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    return (hl > p95).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_118_ratio_intraday_vs_c2c_jumps_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday vs interday jump regime: intraday-range jumps / c2c jumps over 63d."""
    hl = _intraday_logHL(high, low)
    r = _log_ret(close)
    ij = (hl > 3 * _sigma_prior(hl, MDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    cj = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(ij, cj)


# ============================================================
# Bucket N — Post-jump persistence (119-124)
# Causal: past jump → current trailing return.
# ============================================================

def f38_jpdt_119_mean_5d_trailing_after_any_jump_63d(close: pd.Series) -> pd.Series:
    """Mean 5d trailing log-return on bars following any 3σ_21d jump within last 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    jmask = (r.abs() > 3 * sig).shift(1).fillna(False)  # yesterday was a jump
    trail = r.rolling(WDAYS, min_periods=2).sum()
    sel = trail.where(jmask, np.nan)
    return sel.rolling(QDAYS, min_periods=MDAYS).mean()


def f38_jpdt_120_mean_21d_trailing_after_downjump_252d(close: pd.Series) -> pd.Series:
    """Mean 21d trailing log-return on bars following a down-jump (3σ_21d) within last 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    dn = (r < -3 * sig).shift(1).fillna(False)
    trail = r.rolling(MDAYS, min_periods=WDAYS).sum()
    sel = trail.where(dn, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


def f38_jpdt_121_count_negative_post_jump_5d_drift_63d(close: pd.Series) -> pd.Series:
    """Count of jump-days whose post-5d trailing return turned negative, summed 63d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    jmask = (r.abs() > 3 * sig).shift(1).fillna(False)
    trail = r.rolling(WDAYS, min_periods=2).sum()
    flag = (jmask & (trail < 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_122_cum_5d_trailing_after_upjump_63d(close: pd.Series) -> pd.Series:
    """Cumulative 5d trailing log-return on post-up-jump bars within 63d (post-up follow-through)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up = (r > 3 * sig).shift(1).fillna(False)
    trail = r.rolling(WDAYS, min_periods=2).sum()
    sel = trail.where(up, 0.0)
    return sel.rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_123_corr_signed_jump_with_nextday_ret_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr of signed-jump-magnitude with next-day log-return (causal: prior-day jump)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sj = r.where(r.abs() > 3 * sig, 0.0).shift(1)  # prior-day signed jump magnitude
    return sj.rolling(QDAYS, min_periods=MDAYS).corr(r)


def f38_jpdt_124_mean_nextday_ret_given_downjump_252d(close: pd.Series) -> pd.Series:
    """Mean next-bar log-return conditional on prior-day down-jump (3σ_21d) over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    dn = (r < -3 * sig).shift(1).fillna(False)
    sel = r.where(dn, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean()


# ============================================================
# Bucket O — Volatility-of-jump-intensity (125-130)
# ============================================================

def f38_jpdt_125_std_jump_count_21d_over_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of jump count (3σ_21d, 21d-window) → jump-rate volatility."""
    r = _log_ret(close)
    jc = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return jc.rolling(QDAYS, min_periods=MDAYS).std()


def f38_jpdt_126_std_jump_magnitudes_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d std of |log-ret|·1{|r|>3σ_21d} (jump-magnitude volatility)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    m = r.abs().where(r.abs() > 3 * sig, np.nan)
    return m.rolling(QDAYS, min_periods=MDAYS).std()


def f38_jpdt_127_cv_jump_rate_63d(close: pd.Series) -> pd.Series:
    """CV of jump-rate (3σ_21d, 21d-window) over 63d → jump-rate coefficient of variation."""
    r = _log_ret(close)
    jc = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(jc.rolling(QDAYS, min_periods=MDAYS).std(),
                     jc.rolling(QDAYS, min_periods=MDAYS).mean())


def f38_jpdt_128_skew_jump_magnitudes_252d(close: pd.Series) -> pd.Series:
    """Rolling 252d skew of |log-ret|·1{|r|>3σ_21d} → jump-magnitude skew."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    m = r.abs().where(r.abs() > 3 * sig, np.nan)
    return m.rolling(YDAYS, min_periods=QDAYS).skew()


def f38_jpdt_129_jump_rate_momentum_21d_minus_lag21(close: pd.Series) -> pd.Series:
    """Jump-rate momentum: jump_count_21d − jump_count_21d.shift(21)."""
    r = _log_ret(close)
    jc = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return jc - jc.shift(MDAYS)


def f38_jpdt_130_std_jump_rate_21d_over_252d(close: pd.Series) -> pd.Series:
    """Annual dispersion of jump-rate (21d-window count) over 252d."""
    r = _log_ret(close)
    jc = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return jc.rolling(YDAYS, min_periods=QDAYS).std()


# ============================================================
# Bucket P — Misc jump-structure descriptors (131-150)
# ============================================================

def f38_jpdt_131_jump_count_in_last_5d_strict(close: pd.Series) -> pd.Series:
    """Very-recent jump density: count of 3σ_63d jumps in last 5 bars (distinct from 035 which uses 21d-σ)."""
    r = _log_ret(close)
    return (r.abs() > 3 * _sigma_prior(r, QDAYS)).astype(float).rolling(WDAYS, min_periods=2).sum()


def f38_jpdt_132_count_10sig_252d_in_504d(close: pd.Series) -> pd.Series:
    """Truly-extreme event count: |log-ret| > 10·σ_prior252 within 504d."""
    r = _log_ret(close)
    return (r.abs() > 10 * _sigma_prior(r, YDAYS)).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f38_jpdt_133_max_normalized_shock_252d(close: pd.Series) -> pd.Series:
    """Annual peak normalized shock: max(|log-ret| / σ_prior252) within 252d."""
    r = _log_ret(close)
    return _safe_div(r.abs(), _sigma_prior(r, YDAYS)).rolling(YDAYS, min_periods=QDAYS).max()


def f38_jpdt_134_max_normalized_shock_63d_short(close: pd.Series) -> pd.Series:
    """Short-horizon peak normalized shock: max(|log-ret| / σ_prior21) within 63d."""
    r = _log_ret(close)
    return _safe_div(r.abs(), _sigma_prior(r, MDAYS)).rolling(QDAYS, min_periods=MDAYS).max()


def f38_jpdt_135_polyjump_count_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Polyjump count: sum of (gap-jump + intraday-range-jump + c2c-jump) indicators over 63d."""
    g = _gap_ret(open, close)
    hl = _intraday_logHL(high, low)
    r = _log_ret(close)
    a = (g.abs() > 3 * _sigma_prior(g, MDAYS)).astype(float)
    b = (hl > 3 * _sigma_prior(hl, MDAYS)).astype(float)
    c = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    return (a + b + c).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_136_fraction_c2c_of_total_jumps_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of close-to-close jumps in polyjump tally over 63d."""
    g = _gap_ret(open, close)
    hl = _intraday_logHL(high, low)
    r = _log_ret(close)
    a = (g.abs() > 3 * _sigma_prior(g, MDAYS)).astype(float)
    b = (hl > 3 * _sigma_prior(hl, MDAYS)).astype(float)
    c = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    tot = (a + b + c).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(c.rolling(QDAYS, min_periods=MDAYS).sum(), tot)


def f38_jpdt_137_bars_between_two_largest_absret_252d(close: pd.Series) -> pd.Series:
    """Bars between positions of two largest |log-ret| events within 252d window."""
    r = _log_ret(close).abs()

    def _spacing(w):
        a = w[~np.isnan(w)]
        if len(a) < 2:
            return np.nan
        order = np.argsort(w)[::-1]
        return float(abs(order[0] - order[1]))
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_spacing, raw=True)


def f38_jpdt_138_gap_largest_minus_second_largest_252d(close: pd.Series) -> pd.Series:
    """Dominance gap: max |log-ret| − 2nd-largest |log-ret| in 252d."""
    r = _log_ret(close).abs()

    def _gap(w):
        a = np.sort(w[~np.isnan(w)])
        if len(a) < 2:
            return np.nan
        return float(a[-1] - a[-2])
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_gap, raw=True)


def f38_jpdt_139_today_shock_size_sigma_252d(close: pd.Series) -> pd.Series:
    """Today's single-bar shock size in σ_prior252 units (continuous version of 006)."""
    r = _log_ret(close)
    return _safe_div(r.abs(), _sigma_prior(r, YDAYS))


def f38_jpdt_140_longest_quiet_spell_252d(close: pd.Series) -> pd.Series:
    """Longest run of consecutive non-jump (|r|≤3σ_prior21) bars within 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    quiet = (r.abs() <= 3 * sig).astype(float).fillna(0.0)

    def _run(w):
        m = 0; c = 0
        for v in w:
            if v > 0.5:
                c += 1; m = c if c > m else m
            else:
                c = 0
        return m
    return quiet.rolling(YDAYS, min_periods=QDAYS).apply(_run, raw=True)


def f38_jpdt_141_pctrank_today_absret_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of today's |log-ret| within trailing 252d window."""
    r = _log_ret(close).abs()
    return r.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)


def f38_jpdt_142_pctrank_today_absret_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of today's |log-ret| within trailing 1260d window (lifetime-style)."""
    r = _log_ret(close).abs()
    return r.rolling(DDAYS_5Y, min_periods=YDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)


def f38_jpdt_143_mean_r_squared_on_top_decile_bars_63d(close: pd.Series) -> pd.Series:
    """Mean r² restricted to top-decile |log-ret| bars within trailing 63d (conditional 2nd moment of tail)."""
    r = _log_ret(close)
    a = r.abs()
    p90 = a.rolling(QDAYS, min_periods=MDAYS).quantile(0.90)
    sel = (r ** 2).where(a > p90, np.nan)
    return sel.rolling(QDAYS, min_periods=MDAYS).mean()


def f38_jpdt_144_graded_jump_score_21d(close: pd.Series) -> pd.Series:
    """Graded jump score in 21d: 1·N(3σ_21d) + 2·N(4σ_21d) + 3·N(5σ_21d) — weighted intensity."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    n3 = (r.abs() > 3 * sig).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    n4 = (r.abs() > 4 * sig).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    n5 = (r.abs() > 5 * sig).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return n3 + 2.0 * n4 + 3.0 * n5


def f38_jpdt_145_true_range_outlier_count_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """True-range outlier count: bars with TR > 3·ATR_prior21 in 63d."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, n=MDAYS).shift(1)
    return (tr > 3 * atr).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f38_jpdt_146_doji_wide_range_count_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Doji-wide-range bar count: |close-open|/range<0.1 AND range in top decile over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_ratio = (close - open).abs() / rng
    p90 = rng.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    flag = ((body_ratio < 0.1) & (rng > p90)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f38_jpdt_147_max_lee_mykland21_in_63d(close: pd.Series) -> pd.Series:
    """Max Lee-Mykland(21) test stat within 63d (peak local-shock signal)."""
    r = _log_ret(close)
    bv_prior = ((np.pi / 2.0) * (r.abs() * r.abs().shift(1)).rolling(MDAYS, min_periods=WDAYS).sum()).shift(1)
    scale = np.sqrt(_safe_div(bv_prior, MDAYS) * (np.pi / 2.0))
    stat = _safe_div(r.abs(), scale)
    return stat.rolling(QDAYS, min_periods=MDAYS).max()


def f38_jpdt_148_var_jump_magnitudes_252d(close: pd.Series) -> pd.Series:
    """Variance of |log-ret|·1{|r|>3σ_21d} over 252d → annual jump-magnitude variance."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    m = r.abs().where(r.abs() > 3 * sig, np.nan)
    return m.rolling(YDAYS, min_periods=QDAYS).var()


def f38_jpdt_149_recent_vs_annual_jump_rate_anomaly(close: pd.Series) -> pd.Series:
    """Recent jump-rate anomaly: jump_count_21d / mean(jump_count_21d) over past 252d."""
    r = _log_ret(close)
    jc = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(jc, jc.rolling(YDAYS, min_periods=QDAYS).mean())


def f38_jpdt_150_signed_cumulative_jump_return_252d(close: pd.Series) -> pd.Series:
    """Signed cumulative jump return: sum of signed log-returns on 3σ_21d jump days over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sj = r.where(r.abs() > 3 * sig, 0.0)
    return sj.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
#                         REGISTRY 076-150
# ============================================================



def f38_jpdt_076_rolling_beta_absret_on_volz_63d_d1(close, volume):
    return f38_jpdt_076_rolling_beta_absret_on_volz_63d(close, volume).diff()


def f38_jpdt_077_high_vol_no_jump_count_63d_d1(close, volume):
    return f38_jpdt_077_high_vol_no_jump_count_63d(close, volume).diff()


def f38_jpdt_078_peak_volz_on_jump_days_63d_d1(close, volume):
    return f38_jpdt_078_peak_volz_on_jump_days_63d(close, volume).diff()


def f38_jpdt_079_corr_jump_ind_volz_ind_252d_d1(close, volume):
    return f38_jpdt_079_corr_jump_ind_volz_ind_252d(close, volume).diff()


def f38_jpdt_080_log_ratio_vol_jump_vs_nonjump_252d_d1(close, volume):
    return f38_jpdt_080_log_ratio_vol_jump_vs_nonjump_252d(close, volume).diff()


def f38_jpdt_081_alt_up_then_down_jump_pair_63d_d1(close):
    return f38_jpdt_081_alt_up_then_down_jump_pair_63d(close).diff()


def f38_jpdt_082_alt_down_then_up_jump_pair_63d_d1(close):
    return f38_jpdt_082_alt_down_then_up_jump_pair_63d(close).diff()


def f38_jpdt_083_ratio_updn_vs_dnup_pairs_252d_d1(close):
    return f38_jpdt_083_ratio_updn_vs_dnup_pairs_252d(close).diff()


def f38_jpdt_084_bull_jump_fraction_252d_d1(close):
    return f38_jpdt_084_bull_jump_fraction_252d(close).diff()


def f38_jpdt_085_bear_jump_fraction_252d_d1(close):
    return f38_jpdt_085_bear_jump_fraction_252d(close).diff()


def f38_jpdt_086_net_jump_sign_tally_63d_d1(close):
    return f38_jpdt_086_net_jump_sign_tally_63d(close).diff()


def f38_jpdt_087_longest_same_sign_jump_run_252d_d1(close):
    return f38_jpdt_087_longest_same_sign_jump_run_252d(close).diff()


def f38_jpdt_088_climax_reversal_events_252d_d1(close):
    return f38_jpdt_088_climax_reversal_events_252d(close).diff()


def f38_jpdt_089_longest_dnonly_jump_run_252d_d1(close):
    return f38_jpdt_089_longest_dnonly_jump_run_252d(close).diff()


def f38_jpdt_090_count_jump_sign_flips_63d_d1(close):
    return f38_jpdt_090_count_jump_sign_flips_63d(close).diff()


def f38_jpdt_091_jump_variation_abs_21d_d1(close):
    return f38_jpdt_091_jump_variation_abs_21d(close).diff()


def f38_jpdt_092_jump_variation_abs_252d_d1(close):
    return f38_jpdt_092_jump_variation_abs_252d(close).diff()


def f38_jpdt_093_continuous_qv_bv_63d_d1(close):
    return f38_jpdt_093_continuous_qv_bv_63d(close).diff()


def f38_jpdt_094_logdiff_jumpqv_vs_contqv_63d_d1(close):
    return f38_jpdt_094_logdiff_jumpqv_vs_contqv_63d(close).diff()


def f38_jpdt_095_jumpqv_zscore_within_252d_d1(close):
    return f38_jpdt_095_jumpqv_zscore_within_252d(close).diff()


def f38_jpdt_096_jumpqv_ratio_21_over_252_d1(close):
    return f38_jpdt_096_jumpqv_ratio_21_over_252(close).diff()


def f38_jpdt_097_jumpqv_slope_63d_d1(close):
    return f38_jpdt_097_jumpqv_slope_63d(close).diff()


def f38_jpdt_098_har_jump_coefficient_proxy_252d_d1(close):
    return f38_jpdt_098_har_jump_coefficient_proxy_252d(close).diff()


def f38_jpdt_099_hawkes_intensity_hl5_d1(close):
    return f38_jpdt_099_hawkes_intensity_hl5(close).diff()


def f38_jpdt_100_hawkes_intensity_hl21_d1(close):
    return f38_jpdt_100_hawkes_intensity_hl21(close).diff()


def f38_jpdt_101_hawkes_intensity_hl63_d1(close):
    return f38_jpdt_101_hawkes_intensity_hl63(close).diff()


def f38_jpdt_102_hawkes_intensity_hl252_d1(close):
    return f38_jpdt_102_hawkes_intensity_hl252(close).diff()


def f38_jpdt_103_hawkes_short_vs_long_ratio_d1(close):
    return f38_jpdt_103_hawkes_short_vs_long_ratio(close).diff()


def f38_jpdt_104_hawkes_short_minus_long_d1(close):
    return f38_jpdt_104_hawkes_short_minus_long(close).diff()


def f38_jpdt_105_neg_jump_hawkes_hl21_d1(close):
    return f38_jpdt_105_neg_jump_hawkes_hl21(close).diff()


def f38_jpdt_106_pos_jump_hawkes_hl21_d1(close):
    return f38_jpdt_106_pos_jump_hawkes_hl21(close).diff()


def f38_jpdt_107_gap_down_count_3sig_21d_d1(open, close):
    return f38_jpdt_107_gap_down_count_3sig_21d(open, close).diff()


def f38_jpdt_108_gap_down_count_4sig_252d_d1(open, close):
    return f38_jpdt_108_gap_down_count_4sig_252d(open, close).diff()


def f38_jpdt_109_gap_up_count_3sig_21d_d1(open, close):
    return f38_jpdt_109_gap_up_count_3sig_21d(open, close).diff()


def f38_jpdt_110_ratio_gap_down_up_count_252d_d1(open, close):
    return f38_jpdt_110_ratio_gap_down_up_count_252d(open, close).diff()


def f38_jpdt_111_peak_gap_down_severity_63d_d1(open, close):
    return f38_jpdt_111_peak_gap_down_severity_63d(open, close).diff()


def f38_jpdt_112_cum_gap_down_magnitude_252d_d1(open, close):
    return f38_jpdt_112_cum_gap_down_magnitude_252d(open, close).diff()


def f38_jpdt_113_intraday_range_jump_count_3sig_21d_d1(high, low):
    return f38_jpdt_113_intraday_range_jump_count_3sig_21d(high, low).diff()


def f38_jpdt_114_intraday_range_jump_count_4sig_252d_d1(high, low):
    return f38_jpdt_114_intraday_range_jump_count_4sig_252d(high, low).diff()


def f38_jpdt_115_peak_intraday_range_shock_63d_d1(high, low):
    return f38_jpdt_115_peak_intraday_range_shock_63d(high, low).diff()


def f38_jpdt_116_wide_bar_count_p95_21d_d1(high, low):
    return f38_jpdt_116_wide_bar_count_p95_21d(high, low).diff()


def f38_jpdt_117_wide_bar_count_p95_63d_d1(high, low):
    return f38_jpdt_117_wide_bar_count_p95_63d(high, low).diff()


def f38_jpdt_118_ratio_intraday_vs_c2c_jumps_63d_d1(high, low, close):
    return f38_jpdt_118_ratio_intraday_vs_c2c_jumps_63d(high, low, close).diff()


def f38_jpdt_119_mean_5d_trailing_after_any_jump_63d_d1(close):
    return f38_jpdt_119_mean_5d_trailing_after_any_jump_63d(close).diff()


def f38_jpdt_120_mean_21d_trailing_after_downjump_252d_d1(close):
    return f38_jpdt_120_mean_21d_trailing_after_downjump_252d(close).diff()


def f38_jpdt_121_count_negative_post_jump_5d_drift_63d_d1(close):
    return f38_jpdt_121_count_negative_post_jump_5d_drift_63d(close).diff()


def f38_jpdt_122_cum_5d_trailing_after_upjump_63d_d1(close):
    return f38_jpdt_122_cum_5d_trailing_after_upjump_63d(close).diff()


def f38_jpdt_123_corr_signed_jump_with_nextday_ret_63d_d1(close):
    return f38_jpdt_123_corr_signed_jump_with_nextday_ret_63d(close).diff()


def f38_jpdt_124_mean_nextday_ret_given_downjump_252d_d1(close):
    return f38_jpdt_124_mean_nextday_ret_given_downjump_252d(close).diff()


def f38_jpdt_125_std_jump_count_21d_over_63d_d1(close):
    return f38_jpdt_125_std_jump_count_21d_over_63d(close).diff()


def f38_jpdt_126_std_jump_magnitudes_63d_d1(close):
    return f38_jpdt_126_std_jump_magnitudes_63d(close).diff()


def f38_jpdt_127_cv_jump_rate_63d_d1(close):
    return f38_jpdt_127_cv_jump_rate_63d(close).diff()


def f38_jpdt_128_skew_jump_magnitudes_252d_d1(close):
    return f38_jpdt_128_skew_jump_magnitudes_252d(close).diff()


def f38_jpdt_129_jump_rate_momentum_21d_minus_lag21_d1(close):
    return f38_jpdt_129_jump_rate_momentum_21d_minus_lag21(close).diff()


def f38_jpdt_130_std_jump_rate_21d_over_252d_d1(close):
    return f38_jpdt_130_std_jump_rate_21d_over_252d(close).diff()


def f38_jpdt_131_jump_count_in_last_5d_strict_d1(close):
    return f38_jpdt_131_jump_count_in_last_5d_strict(close).diff()


def f38_jpdt_132_count_10sig_252d_in_504d_d1(close):
    return f38_jpdt_132_count_10sig_252d_in_504d(close).diff()


def f38_jpdt_133_max_normalized_shock_252d_d1(close):
    return f38_jpdt_133_max_normalized_shock_252d(close).diff()


def f38_jpdt_134_max_normalized_shock_63d_short_d1(close):
    return f38_jpdt_134_max_normalized_shock_63d_short(close).diff()


def f38_jpdt_135_polyjump_count_63d_d1(open, high, low, close):
    return f38_jpdt_135_polyjump_count_63d(open, high, low, close).diff()


def f38_jpdt_136_fraction_c2c_of_total_jumps_63d_d1(open, high, low, close):
    return f38_jpdt_136_fraction_c2c_of_total_jumps_63d(open, high, low, close).diff()


def f38_jpdt_137_bars_between_two_largest_absret_252d_d1(close):
    return f38_jpdt_137_bars_between_two_largest_absret_252d(close).diff()


def f38_jpdt_138_gap_largest_minus_second_largest_252d_d1(close):
    return f38_jpdt_138_gap_largest_minus_second_largest_252d(close).diff()


def f38_jpdt_139_today_shock_size_sigma_252d_d1(close):
    return f38_jpdt_139_today_shock_size_sigma_252d(close).diff()


def f38_jpdt_140_longest_quiet_spell_252d_d1(close):
    return f38_jpdt_140_longest_quiet_spell_252d(close).diff()


def f38_jpdt_141_pctrank_today_absret_252d_d1(close):
    return f38_jpdt_141_pctrank_today_absret_252d(close).diff()


def f38_jpdt_142_pctrank_today_absret_1260d_d1(close):
    return f38_jpdt_142_pctrank_today_absret_1260d(close).diff()


def f38_jpdt_143_mean_r_squared_on_top_decile_bars_63d_d1(close):
    return f38_jpdt_143_mean_r_squared_on_top_decile_bars_63d(close).diff()


def f38_jpdt_144_graded_jump_score_21d_d1(close):
    return f38_jpdt_144_graded_jump_score_21d(close).diff()


def f38_jpdt_145_true_range_outlier_count_63d_d1(high, low, close):
    return f38_jpdt_145_true_range_outlier_count_63d(high, low, close).diff()


def f38_jpdt_146_doji_wide_range_count_252d_d1(open, high, low, close):
    return f38_jpdt_146_doji_wide_range_count_252d(open, high, low, close).diff()


def f38_jpdt_147_max_lee_mykland21_in_63d_d1(close):
    return f38_jpdt_147_max_lee_mykland21_in_63d(close).diff()


def f38_jpdt_148_var_jump_magnitudes_252d_d1(close):
    return f38_jpdt_148_var_jump_magnitudes_252d(close).diff()


def f38_jpdt_149_recent_vs_annual_jump_rate_anomaly_d1(close):
    return f38_jpdt_149_recent_vs_annual_jump_rate_anomaly(close).diff()


def f38_jpdt_150_signed_cumulative_jump_return_252d_d1(close):
    return f38_jpdt_150_signed_cumulative_jump_return_252d(close).diff()


JUMP_DETECTION_SIGNATURE_D1_REGISTRY_076_150 = {
    "f38_jpdt_076_rolling_beta_absret_on_volz_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_076_rolling_beta_absret_on_volz_63d_d1},
    "f38_jpdt_077_high_vol_no_jump_count_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_077_high_vol_no_jump_count_63d_d1},
    "f38_jpdt_078_peak_volz_on_jump_days_63d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_078_peak_volz_on_jump_days_63d_d1},
    "f38_jpdt_079_corr_jump_ind_volz_ind_252d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_079_corr_jump_ind_volz_ind_252d_d1},
    "f38_jpdt_080_log_ratio_vol_jump_vs_nonjump_252d_d1": {"inputs": ["close", "volume"], "func": f38_jpdt_080_log_ratio_vol_jump_vs_nonjump_252d_d1},
    "f38_jpdt_081_alt_up_then_down_jump_pair_63d_d1": {"inputs": ["close"], "func": f38_jpdt_081_alt_up_then_down_jump_pair_63d_d1},
    "f38_jpdt_082_alt_down_then_up_jump_pair_63d_d1": {"inputs": ["close"], "func": f38_jpdt_082_alt_down_then_up_jump_pair_63d_d1},
    "f38_jpdt_083_ratio_updn_vs_dnup_pairs_252d_d1": {"inputs": ["close"], "func": f38_jpdt_083_ratio_updn_vs_dnup_pairs_252d_d1},
    "f38_jpdt_084_bull_jump_fraction_252d_d1": {"inputs": ["close"], "func": f38_jpdt_084_bull_jump_fraction_252d_d1},
    "f38_jpdt_085_bear_jump_fraction_252d_d1": {"inputs": ["close"], "func": f38_jpdt_085_bear_jump_fraction_252d_d1},
    "f38_jpdt_086_net_jump_sign_tally_63d_d1": {"inputs": ["close"], "func": f38_jpdt_086_net_jump_sign_tally_63d_d1},
    "f38_jpdt_087_longest_same_sign_jump_run_252d_d1": {"inputs": ["close"], "func": f38_jpdt_087_longest_same_sign_jump_run_252d_d1},
    "f38_jpdt_088_climax_reversal_events_252d_d1": {"inputs": ["close"], "func": f38_jpdt_088_climax_reversal_events_252d_d1},
    "f38_jpdt_089_longest_dnonly_jump_run_252d_d1": {"inputs": ["close"], "func": f38_jpdt_089_longest_dnonly_jump_run_252d_d1},
    "f38_jpdt_090_count_jump_sign_flips_63d_d1": {"inputs": ["close"], "func": f38_jpdt_090_count_jump_sign_flips_63d_d1},
    "f38_jpdt_091_jump_variation_abs_21d_d1": {"inputs": ["close"], "func": f38_jpdt_091_jump_variation_abs_21d_d1},
    "f38_jpdt_092_jump_variation_abs_252d_d1": {"inputs": ["close"], "func": f38_jpdt_092_jump_variation_abs_252d_d1},
    "f38_jpdt_093_continuous_qv_bv_63d_d1": {"inputs": ["close"], "func": f38_jpdt_093_continuous_qv_bv_63d_d1},
    "f38_jpdt_094_logdiff_jumpqv_vs_contqv_63d_d1": {"inputs": ["close"], "func": f38_jpdt_094_logdiff_jumpqv_vs_contqv_63d_d1},
    "f38_jpdt_095_jumpqv_zscore_within_252d_d1": {"inputs": ["close"], "func": f38_jpdt_095_jumpqv_zscore_within_252d_d1},
    "f38_jpdt_096_jumpqv_ratio_21_over_252_d1": {"inputs": ["close"], "func": f38_jpdt_096_jumpqv_ratio_21_over_252_d1},
    "f38_jpdt_097_jumpqv_slope_63d_d1": {"inputs": ["close"], "func": f38_jpdt_097_jumpqv_slope_63d_d1},
    "f38_jpdt_098_har_jump_coefficient_proxy_252d_d1": {"inputs": ["close"], "func": f38_jpdt_098_har_jump_coefficient_proxy_252d_d1},
    "f38_jpdt_099_hawkes_intensity_hl5_d1": {"inputs": ["close"], "func": f38_jpdt_099_hawkes_intensity_hl5_d1},
    "f38_jpdt_100_hawkes_intensity_hl21_d1": {"inputs": ["close"], "func": f38_jpdt_100_hawkes_intensity_hl21_d1},
    "f38_jpdt_101_hawkes_intensity_hl63_d1": {"inputs": ["close"], "func": f38_jpdt_101_hawkes_intensity_hl63_d1},
    "f38_jpdt_102_hawkes_intensity_hl252_d1": {"inputs": ["close"], "func": f38_jpdt_102_hawkes_intensity_hl252_d1},
    "f38_jpdt_103_hawkes_short_vs_long_ratio_d1": {"inputs": ["close"], "func": f38_jpdt_103_hawkes_short_vs_long_ratio_d1},
    "f38_jpdt_104_hawkes_short_minus_long_d1": {"inputs": ["close"], "func": f38_jpdt_104_hawkes_short_minus_long_d1},
    "f38_jpdt_105_neg_jump_hawkes_hl21_d1": {"inputs": ["close"], "func": f38_jpdt_105_neg_jump_hawkes_hl21_d1},
    "f38_jpdt_106_pos_jump_hawkes_hl21_d1": {"inputs": ["close"], "func": f38_jpdt_106_pos_jump_hawkes_hl21_d1},
    "f38_jpdt_107_gap_down_count_3sig_21d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_107_gap_down_count_3sig_21d_d1},
    "f38_jpdt_108_gap_down_count_4sig_252d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_108_gap_down_count_4sig_252d_d1},
    "f38_jpdt_109_gap_up_count_3sig_21d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_109_gap_up_count_3sig_21d_d1},
    "f38_jpdt_110_ratio_gap_down_up_count_252d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_110_ratio_gap_down_up_count_252d_d1},
    "f38_jpdt_111_peak_gap_down_severity_63d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_111_peak_gap_down_severity_63d_d1},
    "f38_jpdt_112_cum_gap_down_magnitude_252d_d1": {"inputs": ["open", "close"], "func": f38_jpdt_112_cum_gap_down_magnitude_252d_d1},
    "f38_jpdt_113_intraday_range_jump_count_3sig_21d_d1": {"inputs": ["high", "low"], "func": f38_jpdt_113_intraday_range_jump_count_3sig_21d_d1},
    "f38_jpdt_114_intraday_range_jump_count_4sig_252d_d1": {"inputs": ["high", "low"], "func": f38_jpdt_114_intraday_range_jump_count_4sig_252d_d1},
    "f38_jpdt_115_peak_intraday_range_shock_63d_d1": {"inputs": ["high", "low"], "func": f38_jpdt_115_peak_intraday_range_shock_63d_d1},
    "f38_jpdt_116_wide_bar_count_p95_21d_d1": {"inputs": ["high", "low"], "func": f38_jpdt_116_wide_bar_count_p95_21d_d1},
    "f38_jpdt_117_wide_bar_count_p95_63d_d1": {"inputs": ["high", "low"], "func": f38_jpdt_117_wide_bar_count_p95_63d_d1},
    "f38_jpdt_118_ratio_intraday_vs_c2c_jumps_63d_d1": {"inputs": ["high", "low", "close"], "func": f38_jpdt_118_ratio_intraday_vs_c2c_jumps_63d_d1},
    "f38_jpdt_119_mean_5d_trailing_after_any_jump_63d_d1": {"inputs": ["close"], "func": f38_jpdt_119_mean_5d_trailing_after_any_jump_63d_d1},
    "f38_jpdt_120_mean_21d_trailing_after_downjump_252d_d1": {"inputs": ["close"], "func": f38_jpdt_120_mean_21d_trailing_after_downjump_252d_d1},
    "f38_jpdt_121_count_negative_post_jump_5d_drift_63d_d1": {"inputs": ["close"], "func": f38_jpdt_121_count_negative_post_jump_5d_drift_63d_d1},
    "f38_jpdt_122_cum_5d_trailing_after_upjump_63d_d1": {"inputs": ["close"], "func": f38_jpdt_122_cum_5d_trailing_after_upjump_63d_d1},
    "f38_jpdt_123_corr_signed_jump_with_nextday_ret_63d_d1": {"inputs": ["close"], "func": f38_jpdt_123_corr_signed_jump_with_nextday_ret_63d_d1},
    "f38_jpdt_124_mean_nextday_ret_given_downjump_252d_d1": {"inputs": ["close"], "func": f38_jpdt_124_mean_nextday_ret_given_downjump_252d_d1},
    "f38_jpdt_125_std_jump_count_21d_over_63d_d1": {"inputs": ["close"], "func": f38_jpdt_125_std_jump_count_21d_over_63d_d1},
    "f38_jpdt_126_std_jump_magnitudes_63d_d1": {"inputs": ["close"], "func": f38_jpdt_126_std_jump_magnitudes_63d_d1},
    "f38_jpdt_127_cv_jump_rate_63d_d1": {"inputs": ["close"], "func": f38_jpdt_127_cv_jump_rate_63d_d1},
    "f38_jpdt_128_skew_jump_magnitudes_252d_d1": {"inputs": ["close"], "func": f38_jpdt_128_skew_jump_magnitudes_252d_d1},
    "f38_jpdt_129_jump_rate_momentum_21d_minus_lag21_d1": {"inputs": ["close"], "func": f38_jpdt_129_jump_rate_momentum_21d_minus_lag21_d1},
    "f38_jpdt_130_std_jump_rate_21d_over_252d_d1": {"inputs": ["close"], "func": f38_jpdt_130_std_jump_rate_21d_over_252d_d1},
    "f38_jpdt_131_jump_count_in_last_5d_strict_d1": {"inputs": ["close"], "func": f38_jpdt_131_jump_count_in_last_5d_strict_d1},
    "f38_jpdt_132_count_10sig_252d_in_504d_d1": {"inputs": ["close"], "func": f38_jpdt_132_count_10sig_252d_in_504d_d1},
    "f38_jpdt_133_max_normalized_shock_252d_d1": {"inputs": ["close"], "func": f38_jpdt_133_max_normalized_shock_252d_d1},
    "f38_jpdt_134_max_normalized_shock_63d_short_d1": {"inputs": ["close"], "func": f38_jpdt_134_max_normalized_shock_63d_short_d1},
    "f38_jpdt_135_polyjump_count_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_135_polyjump_count_63d_d1},
    "f38_jpdt_136_fraction_c2c_of_total_jumps_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_136_fraction_c2c_of_total_jumps_63d_d1},
    "f38_jpdt_137_bars_between_two_largest_absret_252d_d1": {"inputs": ["close"], "func": f38_jpdt_137_bars_between_two_largest_absret_252d_d1},
    "f38_jpdt_138_gap_largest_minus_second_largest_252d_d1": {"inputs": ["close"], "func": f38_jpdt_138_gap_largest_minus_second_largest_252d_d1},
    "f38_jpdt_139_today_shock_size_sigma_252d_d1": {"inputs": ["close"], "func": f38_jpdt_139_today_shock_size_sigma_252d_d1},
    "f38_jpdt_140_longest_quiet_spell_252d_d1": {"inputs": ["close"], "func": f38_jpdt_140_longest_quiet_spell_252d_d1},
    "f38_jpdt_141_pctrank_today_absret_252d_d1": {"inputs": ["close"], "func": f38_jpdt_141_pctrank_today_absret_252d_d1},
    "f38_jpdt_142_pctrank_today_absret_1260d_d1": {"inputs": ["close"], "func": f38_jpdt_142_pctrank_today_absret_1260d_d1},
    "f38_jpdt_143_mean_r_squared_on_top_decile_bars_63d_d1": {"inputs": ["close"], "func": f38_jpdt_143_mean_r_squared_on_top_decile_bars_63d_d1},
    "f38_jpdt_144_graded_jump_score_21d_d1": {"inputs": ["close"], "func": f38_jpdt_144_graded_jump_score_21d_d1},
    "f38_jpdt_145_true_range_outlier_count_63d_d1": {"inputs": ["high", "low", "close"], "func": f38_jpdt_145_true_range_outlier_count_63d_d1},
    "f38_jpdt_146_doji_wide_range_count_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f38_jpdt_146_doji_wide_range_count_252d_d1},
    "f38_jpdt_147_max_lee_mykland21_in_63d_d1": {"inputs": ["close"], "func": f38_jpdt_147_max_lee_mykland21_in_63d_d1},
    "f38_jpdt_148_var_jump_magnitudes_252d_d1": {"inputs": ["close"], "func": f38_jpdt_148_var_jump_magnitudes_252d_d1},
    "f38_jpdt_149_recent_vs_annual_jump_rate_anomaly_d1": {"inputs": ["close"], "func": f38_jpdt_149_recent_vs_annual_jump_rate_anomaly_d1},
    "f38_jpdt_150_signed_cumulative_jump_return_252d_d1": {"inputs": ["close"], "func": f38_jpdt_150_signed_cumulative_jump_return_252d_d1},
}
