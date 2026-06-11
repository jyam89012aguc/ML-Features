"""
31_oscillator_extremes — Extended 2nd Derivatives (Features osc_extdrv2_001-025)
Domain: rate of change of extended oscillator base features — velocity of TSI, EFI,
        BOP, Vortex, Williams A/D, and z-scored/rank oscillators
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Covers velocity (5d/21d diffs, pct_change, rolling OLS slope) of:
TSI raw, TSI signal-line gap, EFI raw, EFI z-score, BOP raw, Vortex spread,
Williams A/D ROC, CMO z-score, TRIX z-score, PPO z-score, KST z-score,
Coppock z-score, SMI z-score, Fisher z-score, Schaff raw,
Klinger signal line, RVI raw, confluence scores.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (backward-looking)."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Oscillator helpers (inline re-implementations) ────────────────────────────

def _tsi(close: pd.Series, r: int = 25, s: int = 13) -> pd.Series:
    """True Strength Index."""
    delta = close.diff(1)
    ds1 = _ewm_mean(delta, r)
    ds2 = _ewm_mean(ds1, s)
    abs_ds1 = _ewm_mean(delta.abs(), r)
    abs_ds2 = _ewm_mean(abs_ds1, s)
    return _safe_div(ds2, abs_ds2) * 100.0


def _elder_force_index(close: pd.Series, volume: pd.Series, n: int = 13) -> pd.Series:
    """Elder Force Index."""
    raw = close.diff(1) * volume
    return _ewm_mean(raw, n)


def _balance_of_power(open_: pd.Series, high: pd.Series, low: pd.Series,
                      close: pd.Series, n: int = 14) -> pd.Series:
    """Balance of Power."""
    raw = _safe_div(close - open_, (high - low).replace(0, np.nan))
    return _rolling_mean(raw, n)


def _vortex_neg(high: pd.Series, low: pd.Series, close: pd.Series,
                n: int = 14) -> pd.Series:
    """Vortex Indicator negative line."""
    prev_high = high.shift(1)
    prev_close = close.shift(1)
    vm_neg = (low - prev_high).abs()
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs()
    ], axis=1).max(axis=1)
    return _safe_div(_rolling_sum(vm_neg, n), _rolling_sum(tr, n))


def _vortex_pos(high: pd.Series, low: pd.Series, close: pd.Series,
                n: int = 14) -> pd.Series:
    """Vortex Indicator positive line."""
    prev_low = low.shift(1)
    prev_close = close.shift(1)
    vm_pos = (high - prev_low).abs()
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs()
    ], axis=1).max(axis=1)
    return _safe_div(_rolling_sum(vm_pos, n), _rolling_sum(tr, n))


def _williams_ad(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams Accumulation/Distribution."""
    prev_close = close.shift(1)
    true_range_high = pd.concat([high, prev_close], axis=1).max(axis=1)
    true_range_low = pd.concat([low, prev_close], axis=1).min(axis=1)
    cond_up = close > prev_close
    cond_dn = close < prev_close
    ad = pd.Series(
        np.where(cond_up, close - true_range_low,
                 np.where(cond_dn, close - true_range_high, 0.0)),
        index=close.index
    )
    return ad.cumsum()


def _cmo(close: pd.Series, n: int) -> pd.Series:
    """Chande Momentum Oscillator."""
    delta = close.diff(1)
    up = delta.clip(lower=0.0)
    dn = (-delta).clip(lower=0.0)
    return _safe_div(100.0 * (_rolling_sum(up, n) - _rolling_sum(dn, n)),
                     _rolling_sum(up, n) + _rolling_sum(dn, n))


def _trix(close: pd.Series, n: int) -> pd.Series:
    """TRIX oscillator."""
    log_c = np.log(close.replace(0, np.nan))
    ema1 = _ewm_mean(log_c, n)
    ema2 = _ewm_mean(ema1, n)
    ema3 = _ewm_mean(ema2, n)
    return _safe_div(ema3 - ema3.shift(1), ema3.shift(1)) * 100.0


def _fisher_transform(high: pd.Series, low: pd.Series, close: pd.Series, n: int) -> pd.Series:
    """Fisher Transform."""
    hh = _rolling_max(high, n)
    ll = _rolling_min(low, n)
    rng = (hh - ll).replace(0, np.nan)
    val = (2.0 * ((close - ll) / rng) - 1.0).clip(-0.999, 0.999)
    return 0.5 * np.log((1.0 + val) / (1.0 - val))


def _ppo(close: pd.Series, fast: int = 12, slow: int = 26) -> pd.Series:
    """Percentage Price Oscillator."""
    ema_f = _ewm_mean(close, fast)
    ema_s = _ewm_mean(close, slow)
    return _safe_div((ema_f - ema_s), ema_s) * 100.0


def _kst(close: pd.Series) -> pd.Series:
    """KST oscillator."""
    def _roc(c: pd.Series, n: int) -> pd.Series:
        return _safe_div(c - c.shift(n), c.shift(n)) * 100.0
    r1 = _rolling_mean(_roc(close, 10), 10)
    r2 = _rolling_mean(_roc(close, 15), 10)
    r3 = _rolling_mean(_roc(close, 20), 10)
    r4 = _rolling_mean(_roc(close, 30), 15)
    return r1 * 1.0 + r2 * 2.0 + r3 * 3.0 + r4 * 4.0


def _coppock(close: pd.Series) -> pd.Series:
    """Coppock Curve."""
    def _roc(c: pd.Series, n: int) -> pd.Series:
        return _safe_div(c - c.shift(n), c.shift(n)) * 100.0
    combined = _roc(close, 14) + _roc(close, 11)
    w = 10
    def _wma(x):
        if len(x) < w // 2:
            return np.nan
        wts = np.arange(1, len(x) + 1, dtype=float)
        return float(np.dot(x, wts) / wts.sum())
    return combined.rolling(w, min_periods=max(1, w // 2)).apply(_wma, raw=True)


def _smi(high: pd.Series, low: pd.Series, close: pd.Series, n: int,
         smooth1: int = 3, smooth2: int = 3) -> pd.Series:
    """Stochastic Momentum Index."""
    hh = _rolling_max(high, n)
    ll = _rolling_min(low, n)
    midpoint = (hh + ll) / 2.0
    diff = close - midpoint
    half_range = (hh - ll) / 2.0
    diff_sm = _ewm_mean(_ewm_mean(diff, smooth1), smooth2)
    range_sm = _ewm_mean(_ewm_mean(half_range, smooth1), smooth2)
    return _safe_div(diff_sm, range_sm) * 100.0


def _schaff_trend_cycle(close: pd.Series, fast: int = 23, slow: int = 50,
                        cycle: int = 10) -> pd.Series:
    """Schaff Trend Cycle."""
    ema_f = _ewm_mean(close, fast)
    ema_s = _ewm_mean(close, slow)
    macd = ema_f - ema_s
    m_min = _rolling_min(macd, cycle)
    m_max = _rolling_max(macd, cycle)
    stoch1 = _safe_div((macd - m_min) * 100.0, m_max - m_min)
    f1 = _ewm_mean(stoch1, 2)
    f1_min = _rolling_min(f1, cycle)
    f1_max = _rolling_max(f1, cycle)
    stoch2 = _safe_div((f1 - f1_min) * 100.0, f1_max - f1_min)
    return _ewm_mean(stoch2, 2)


def _klinger(high: pd.Series, low: pd.Series, close: pd.Series,
             volume: pd.Series) -> pd.Series:
    """Klinger Volume Oscillator."""
    tp = high + low + close
    trend = pd.Series(np.where(tp > tp.shift(1), 1.0, -1.0), index=close.index)
    dm = high - low
    sv = volume * trend * 2.0 * _safe_div(dm, (high - low).replace(0, np.nan))
    return _ewm_mean(sv, 34) - _ewm_mean(sv, 55)


def _rvi(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series,
         n: int = 10) -> pd.Series:
    """Relative Vigor Index."""
    num = close - open_
    den = high - low
    def _sym4(s: pd.Series) -> pd.Series:
        return (s + 2.0 * s.shift(1) + 2.0 * s.shift(2) + s.shift(3)) / 6.0
    ratio = _safe_div(_sym4(num), _sym4(den).replace(0, np.nan))
    return _rolling_mean(ratio, n)


def _stoch_k(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Stochastic %K."""
    hh = _rolling_max(high, w)
    ll = _rolling_min(low, w)
    return _safe_div((close - ll) * 100.0, hh - ll)


def _mfi(high: pd.Series, low: pd.Series, close: pd.Series,
         volume: pd.Series, w: int) -> pd.Series:
    """Money Flow Index."""
    tp = (high + low + close) / 3.0
    mf = tp * volume
    pos_mf = mf.where(tp > tp.shift(1), 0.0)
    neg_mf = mf.where(tp < tp.shift(1), 0.0)
    pos_sum = _rolling_sum(pos_mf, w)
    neg_sum = _rolling_sum(neg_mf, w)
    mfr = _safe_div(pos_sum, neg_sum)
    return 100.0 - _safe_div(100.0, 1.0 + mfr)


# ── Extended 2nd-Derivative Feature Functions ─────────────────────────────────
# Each = rate of change of an EXTENDED BASE concept from extended_001_075

def osc_extdrv2_001_tsi_25_13_raw_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of TSI (25,13) raw value — weekly velocity of true strength."""
    return _tsi(close, 25, 13).diff(_TD_WEEK)


def osc_extdrv2_002_tsi_25_13_raw_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of TSI (25,13) raw value — monthly velocity of true strength."""
    return _tsi(close, 25, 13).diff(_TD_MON)


def osc_extdrv2_003_tsi_25_13_signal_gap_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of (TSI - signal line) gap — velocity of bearish divergence from signal."""
    tsi = _tsi(close, 25, 13)
    sig = _ewm_mean(tsi, 7)
    gap = tsi - sig
    return gap.diff(_TD_WEEK)


def osc_extdrv2_004_tsi_25_13_raw_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of TSI (25,13) raw over trailing 21 days — trend of true strength."""
    return _linslope(_tsi(close, 25, 13), _TD_MON)


def osc_extdrv2_005_efi_13_raw_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EFI (13-period) raw — weekly velocity of elder force."""
    return _elder_force_index(close, volume, 13).diff(_TD_WEEK)


def osc_extdrv2_006_efi_13_raw_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of EFI (13-period) raw — monthly velocity of force index."""
    return _elder_force_index(close, volume, 13).diff(_TD_MON)


def osc_extdrv2_007_efi_13_zscore_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EFI z-score (252d) — velocity of normalized force index."""
    e = _elder_force_index(close, volume, 13)
    zs = _safe_div(e - _rolling_mean(e, _TD_YEAR), _rolling_std(e, _TD_YEAR))
    return zs.diff(_TD_WEEK)


def osc_extdrv2_008_bop_14_raw_5d_diff(open_: pd.Series, high: pd.Series,
                                        low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of BOP (14-day) raw — weekly velocity of balance of power."""
    return _balance_of_power(open_, high, low, close, 14).diff(_TD_WEEK)


def osc_extdrv2_009_bop_14_raw_21d_diff(open_: pd.Series, high: pd.Series,
                                         low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of BOP (14-day) raw — monthly velocity of balance of power."""
    return _balance_of_power(open_, high, low, close, 14).diff(_TD_MON)


def osc_extdrv2_010_bop_14_zscore_5d_diff(open_: pd.Series, high: pd.Series,
                                           low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of BOP (14-day) z-score — velocity of normalized selling dominance."""
    b = _balance_of_power(open_, high, low, close, 14)
    zs = _safe_div(b - _rolling_mean(b, _TD_YEAR), _rolling_std(b, _TD_YEAR))
    return zs.diff(_TD_WEEK)


def osc_extdrv2_011_vortex_spread_21d_diff(high: pd.Series, low: pd.Series,
                                            close: pd.Series) -> pd.Series:
    """21-day diff of (VI- - VI+) spread — monthly velocity of downtrend dominance."""
    spread = _vortex_neg(high, low, close, 14) - _vortex_pos(high, low, close, 14)
    return spread.diff(_TD_MON)


def osc_extdrv2_012_vortex_neg_zscore_5d_diff(high: pd.Series, low: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """5-day diff of VI- z-score (252d) — velocity of normalized downtrend strength."""
    v = _vortex_neg(high, low, close, 14)
    zs = _safe_div(v - _rolling_mean(v, _TD_YEAR), _rolling_std(v, _TD_YEAR))
    return zs.diff(_TD_WEEK)


def osc_extdrv2_013_williams_ad_roc21_5d_diff(high: pd.Series, low: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """5-day diff of Williams A/D 21d ROC — velocity of distribution-phase ROC."""
    wad = _williams_ad(high, low, close)
    roc = _safe_div(wad - wad.shift(_TD_MON), wad.shift(_TD_MON).abs() + _EPS) * 100.0
    return roc.diff(_TD_WEEK)


def osc_extdrv2_014_williams_ad_5d_diff_slope_21d(high: pd.Series, low: pd.Series,
                                                   close: pd.Series) -> pd.Series:
    """OLS slope of Williams A/D 5d diff over trailing 21 days — trend of flow velocity."""
    wad5 = _williams_ad(high, low, close).diff(_TD_WEEK)
    return _linslope(wad5, _TD_MON)


def osc_extdrv2_015_cmo_14_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of CMO (14-day) z-score — velocity of normalized Chande momentum."""
    c = _cmo(close, 14)
    zs = _safe_div(c - _rolling_mean(c, _TD_YEAR), _rolling_std(c, _TD_YEAR))
    return zs.diff(_TD_WEEK)


def osc_extdrv2_016_trix_14_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of TRIX (14) z-score — velocity of normalized triple-EMA momentum."""
    t = _trix(close, 14)
    zs = _safe_div(t - _rolling_mean(t, _TD_YEAR), _rolling_std(t, _TD_YEAR))
    return zs.diff(_TD_WEEK)


def osc_extdrv2_017_ppo_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of PPO z-score — velocity of normalized percentage price oscillator."""
    p = _ppo(close)
    zs = _safe_div(p - _rolling_mean(p, _TD_YEAR), _rolling_std(p, _TD_YEAR))
    return zs.diff(_TD_WEEK)


def osc_extdrv2_018_kst_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of KST z-score — velocity of normalized know-sure-thing oscillator."""
    k = _kst(close)
    zs = _safe_div(k - _rolling_mean(k, _TD_YEAR), _rolling_std(k, _TD_YEAR))
    return zs.diff(_TD_WEEK)


def osc_extdrv2_019_coppock_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Coppock z-score — velocity of normalized long-cycle momentum."""
    c = _coppock(close)
    zs = _safe_div(c - _rolling_mean(c, _TD_YEAR), _rolling_std(c, _TD_YEAR))
    return zs.diff(_TD_WEEK)


def osc_extdrv2_020_smi_14_zscore_5d_diff(high: pd.Series, low: pd.Series,
                                           close: pd.Series) -> pd.Series:
    """5-day diff of SMI (14-day) z-score — velocity of normalized stochastic momentum."""
    s = _smi(high, low, close, 14)
    zs = _safe_div(s - _rolling_mean(s, _TD_YEAR), _rolling_std(s, _TD_YEAR))
    return zs.diff(_TD_WEEK)


def osc_extdrv2_021_schaff_raw_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of Schaff Trend Cycle raw — velocity of cycle position."""
    return _schaff_trend_cycle(close).diff(_TD_WEEK)


def osc_extdrv2_022_klinger_signal_slope_21d(high: pd.Series, low: pd.Series,
                                              close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of Klinger signal line (13-EMA of KVO) over 21 days."""
    sig = _ewm_mean(_klinger(high, low, close, volume), 13)
    return _linslope(sig, _TD_MON)


def osc_extdrv2_023_rvi_raw_21d_diff(open_: pd.Series, high: pd.Series,
                                      low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day diff of RVI (10-period) raw — monthly velocity of relative vigor."""
    return _rvi(open_, high, low, close, 10).diff(_TD_MON)


def osc_extdrv2_024_fisher_10_zscore_5d_diff(high: pd.Series, low: pd.Series,
                                              close: pd.Series) -> pd.Series:
    """5-day diff of Fisher Transform (10-day) z-score — velocity of normalized Fisher."""
    f = _fisher_transform(high, low, close, 10)
    zs = _safe_div(f - _rolling_mean(f, _TD_YEAR), _rolling_std(f, _TD_YEAR))
    return zs.diff(_TD_WEEK)


def osc_extdrv2_025_tsi_25_13_min21_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of rolling 21d minimum of TSI (25,13) — velocity of worst-case momentum."""
    tsi_min21 = _tsi(close, 25, 13).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    return tsi_min21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

OSCILLATOR_EXTREMES_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "osc_extdrv2_001_tsi_25_13_raw_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv2_001_tsi_25_13_raw_5d_diff},
    "osc_extdrv2_002_tsi_25_13_raw_21d_diff": {
        "inputs": ["close"], "func": osc_extdrv2_002_tsi_25_13_raw_21d_diff},
    "osc_extdrv2_003_tsi_25_13_signal_gap_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv2_003_tsi_25_13_signal_gap_5d_diff},
    "osc_extdrv2_004_tsi_25_13_raw_slope_21d": {
        "inputs": ["close"], "func": osc_extdrv2_004_tsi_25_13_raw_slope_21d},
    "osc_extdrv2_005_efi_13_raw_5d_diff": {
        "inputs": ["close", "volume"], "func": osc_extdrv2_005_efi_13_raw_5d_diff},
    "osc_extdrv2_006_efi_13_raw_21d_diff": {
        "inputs": ["close", "volume"], "func": osc_extdrv2_006_efi_13_raw_21d_diff},
    "osc_extdrv2_007_efi_13_zscore_5d_diff": {
        "inputs": ["close", "volume"], "func": osc_extdrv2_007_efi_13_zscore_5d_diff},
    "osc_extdrv2_008_bop_14_raw_5d_diff": {
        "inputs": ["open", "high", "low", "close"], "func": osc_extdrv2_008_bop_14_raw_5d_diff},
    "osc_extdrv2_009_bop_14_raw_21d_diff": {
        "inputs": ["open", "high", "low", "close"], "func": osc_extdrv2_009_bop_14_raw_21d_diff},
    "osc_extdrv2_010_bop_14_zscore_5d_diff": {
        "inputs": ["open", "high", "low", "close"], "func": osc_extdrv2_010_bop_14_zscore_5d_diff},
    "osc_extdrv2_011_vortex_spread_21d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv2_011_vortex_spread_21d_diff},
    "osc_extdrv2_012_vortex_neg_zscore_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv2_012_vortex_neg_zscore_5d_diff},
    "osc_extdrv2_013_williams_ad_roc21_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv2_013_williams_ad_roc21_5d_diff},
    "osc_extdrv2_014_williams_ad_5d_diff_slope_21d": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv2_014_williams_ad_5d_diff_slope_21d},
    "osc_extdrv2_015_cmo_14_zscore_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv2_015_cmo_14_zscore_5d_diff},
    "osc_extdrv2_016_trix_14_zscore_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv2_016_trix_14_zscore_5d_diff},
    "osc_extdrv2_017_ppo_zscore_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv2_017_ppo_zscore_5d_diff},
    "osc_extdrv2_018_kst_zscore_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv2_018_kst_zscore_5d_diff},
    "osc_extdrv2_019_coppock_zscore_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv2_019_coppock_zscore_5d_diff},
    "osc_extdrv2_020_smi_14_zscore_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv2_020_smi_14_zscore_5d_diff},
    "osc_extdrv2_021_schaff_raw_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv2_021_schaff_raw_5d_diff},
    "osc_extdrv2_022_klinger_signal_slope_21d": {
        "inputs": ["high", "low", "close", "volume"], "func": osc_extdrv2_022_klinger_signal_slope_21d},
    "osc_extdrv2_023_rvi_raw_21d_diff": {
        "inputs": ["open", "high", "low", "close"], "func": osc_extdrv2_023_rvi_raw_21d_diff},
    "osc_extdrv2_024_fisher_10_zscore_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv2_024_fisher_10_zscore_5d_diff},
    "osc_extdrv2_025_tsi_25_13_min21_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv2_025_tsi_25_13_min21_5d_diff},
}
