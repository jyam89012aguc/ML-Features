"""
31_oscillator_extremes — Extended 3rd Derivatives (Features osc_extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative oscillator features —
        acceleration of velocity for TSI, EFI, BOP, Vortex, Williams A/D,
        and z-scored/rank oscillator velocities
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Covers second-diff / slope-of-slope / diff-of-slope of:
TSI 5d-velocity, TSI signal-gap velocity, EFI 5d-velocity, EFI z-score velocity,
BOP 5d-velocity, BOP z-score velocity, Vortex spread velocity, Vortex neg z-score
velocity, Williams A/D ROC velocity, CMO z-score velocity, TRIX z-score velocity,
PPO z-score velocity, KST z-score velocity, Coppock z-score velocity,
SMI z-score velocity, Schaff velocity, Klinger signal slope, RVI monthly velocity,
Fisher z-score velocity, TSI min-21 velocity.
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


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────
# Each = rate of change of a 2nd-derivative concept (diff-of-diff, slope-of-slope)

def osc_extdrv3_001_tsi_25_13_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of TSI (25,13) — acceleration of true strength velocity."""
    vel = _tsi(close, 25, 13).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_002_tsi_25_13_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of TSI (25,13) 21d velocity — jerk in monthly true strength."""
    vel21 = _tsi(close, 25, 13).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def osc_extdrv3_003_tsi_signal_gap_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of (TSI - signal line) gap — acceleration of bearish divergence."""
    tsi = _tsi(close, 25, 13)
    sig = _ewm_mean(tsi, 7)
    gap = tsi - sig
    vel = gap.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_004_tsi_raw_slope_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21d OLS slope of TSI (25,13) — rate-of-slope-change."""
    slp = _linslope(_tsi(close, 25, 13), _TD_MON)
    return slp.diff(_TD_WEEK)


def osc_extdrv3_005_efi_13_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EFI (13-period) — acceleration of force index velocity."""
    vel = _elder_force_index(close, volume, 13).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_006_efi_13_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of EFI (13-period) 21d velocity — jerk in monthly force index."""
    vel21 = _elder_force_index(close, volume, 13).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def osc_extdrv3_007_efi_13_zscore_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of EFI z-score — acceleration of normalized force index."""
    e = _elder_force_index(close, volume, 13)
    zs = _safe_div(e - _rolling_mean(e, _TD_YEAR), _rolling_std(e, _TD_YEAR))
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_008_bop_14_5d_diff_5d_diff(open_: pd.Series, high: pd.Series,
                                            low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of BOP (14-day) — acceleration of selling-pressure velocity."""
    vel = _balance_of_power(open_, high, low, close, 14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_009_bop_14_21d_diff_5d_diff(open_: pd.Series, high: pd.Series,
                                             low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of BOP (14-day) 21d velocity — jerk in monthly BOP change."""
    vel21 = _balance_of_power(open_, high, low, close, 14).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def osc_extdrv3_010_bop_14_zscore_5d_diff_5d_diff(open_: pd.Series, high: pd.Series,
                                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of BOP z-score — acceleration of normalized selling dominance."""
    b = _balance_of_power(open_, high, low, close, 14)
    zs = _safe_div(b - _rolling_mean(b, _TD_YEAR), _rolling_std(b, _TD_YEAR))
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_011_vortex_spread_5d_diff_5d_diff(high: pd.Series, low: pd.Series,
                                                   close: pd.Series) -> pd.Series:
    """Second 5-day diff of (VI- - VI+) — acceleration of downtrend dominance velocity."""
    spread = _vortex_neg(high, low, close, 14) - _vortex_pos(high, low, close, 14)
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_012_vortex_neg_zscore_5d_diff_5d_diff(high: pd.Series, low: pd.Series,
                                                       close: pd.Series) -> pd.Series:
    """Second 5-day diff of VI- z-score — acceleration of normalized downtrend strength."""
    v = _vortex_neg(high, low, close, 14)
    zs = _safe_div(v - _rolling_mean(v, _TD_YEAR), _rolling_std(v, _TD_YEAR))
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_013_williams_ad_roc21_5d_diff_5d_diff(high: pd.Series, low: pd.Series,
                                                       close: pd.Series) -> pd.Series:
    """Second 5-day diff of Williams A/D 21d ROC — acceleration of distribution ROC."""
    wad = _williams_ad(high, low, close)
    roc = _safe_div(wad - wad.shift(_TD_MON), wad.shift(_TD_MON).abs() + _EPS) * 100.0
    vel = roc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_014_williams_ad_flow_slope_5d_diff(high: pd.Series, low: pd.Series,
                                                    close: pd.Series) -> pd.Series:
    """5-day diff of slope of Williams A/D 5d flow — rate of slope change in flow."""
    wad5 = _williams_ad(high, low, close).diff(_TD_WEEK)
    slp = _linslope(wad5, _TD_MON)
    return slp.diff(_TD_WEEK)


def osc_extdrv3_015_cmo_14_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of CMO z-score — acceleration of normalized Chande momentum."""
    c = _cmo(close, 14)
    zs = _safe_div(c - _rolling_mean(c, _TD_YEAR), _rolling_std(c, _TD_YEAR))
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_016_trix_14_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of TRIX z-score — acceleration of normalized triple-EMA momentum."""
    t = _trix(close, 14)
    zs = _safe_div(t - _rolling_mean(t, _TD_YEAR), _rolling_std(t, _TD_YEAR))
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_017_ppo_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of PPO z-score — acceleration of normalized PPO."""
    p = _ppo(close)
    zs = _safe_div(p - _rolling_mean(p, _TD_YEAR), _rolling_std(p, _TD_YEAR))
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_018_kst_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of KST z-score — acceleration of normalized KST."""
    k = _kst(close)
    zs = _safe_div(k - _rolling_mean(k, _TD_YEAR), _rolling_std(k, _TD_YEAR))
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_019_coppock_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of Coppock z-score — acceleration of normalized long-cycle momentum."""
    c = _coppock(close)
    zs = _safe_div(c - _rolling_mean(c, _TD_YEAR), _rolling_std(c, _TD_YEAR))
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_020_smi_14_zscore_5d_diff_5d_diff(high: pd.Series, low: pd.Series,
                                                   close: pd.Series) -> pd.Series:
    """Second 5-day diff of SMI z-score — acceleration of normalized stochastic momentum."""
    s = _smi(high, low, close, 14)
    zs = _safe_div(s - _rolling_mean(s, _TD_YEAR), _rolling_std(s, _TD_YEAR))
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_021_schaff_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of Schaff Trend Cycle — acceleration of cycle oscillator."""
    vel = _schaff_trend_cycle(close).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_022_klinger_signal_slope_5d_diff(high: pd.Series, low: pd.Series,
                                                  close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of Klinger signal OLS slope — rate-of-slope-change of volume force trend."""
    sig = _ewm_mean(_klinger(high, low, close, volume), 13)
    slp = _linslope(sig, _TD_MON)
    return slp.diff(_TD_WEEK)


def osc_extdrv3_023_rvi_21d_diff_5d_diff(open_: pd.Series, high: pd.Series,
                                          low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of RVI (10-period) 21d velocity — jerk in monthly vigor change."""
    vel21 = _rvi(open_, high, low, close, 10).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def osc_extdrv3_024_fisher_10_zscore_5d_diff_5d_diff(high: pd.Series, low: pd.Series,
                                                      close: pd.Series) -> pd.Series:
    """Second 5-day diff of Fisher z-score — acceleration of normalized Fisher extremity."""
    f = _fisher_transform(high, low, close, 10)
    zs = _safe_div(f - _rolling_mean(f, _TD_YEAR), _rolling_std(f, _TD_YEAR))
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def osc_extdrv3_025_tsi_min21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of rolling 21d min of TSI — acceleration of worst-case momentum."""
    tsi_min21 = _tsi(close, 25, 13).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    vel = tsi_min21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

OSCILLATOR_EXTREMES_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "osc_extdrv3_001_tsi_25_13_5d_diff_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_001_tsi_25_13_5d_diff_5d_diff},
    "osc_extdrv3_002_tsi_25_13_21d_diff_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_002_tsi_25_13_21d_diff_5d_diff},
    "osc_extdrv3_003_tsi_signal_gap_5d_diff_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_003_tsi_signal_gap_5d_diff_5d_diff},
    "osc_extdrv3_004_tsi_raw_slope_21d_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_004_tsi_raw_slope_21d_5d_diff},
    "osc_extdrv3_005_efi_13_5d_diff_5d_diff": {
        "inputs": ["close", "volume"], "func": osc_extdrv3_005_efi_13_5d_diff_5d_diff},
    "osc_extdrv3_006_efi_13_21d_diff_5d_diff": {
        "inputs": ["close", "volume"], "func": osc_extdrv3_006_efi_13_21d_diff_5d_diff},
    "osc_extdrv3_007_efi_13_zscore_5d_diff_5d_diff": {
        "inputs": ["close", "volume"], "func": osc_extdrv3_007_efi_13_zscore_5d_diff_5d_diff},
    "osc_extdrv3_008_bop_14_5d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"], "func": osc_extdrv3_008_bop_14_5d_diff_5d_diff},
    "osc_extdrv3_009_bop_14_21d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"], "func": osc_extdrv3_009_bop_14_21d_diff_5d_diff},
    "osc_extdrv3_010_bop_14_zscore_5d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"], "func": osc_extdrv3_010_bop_14_zscore_5d_diff_5d_diff},
    "osc_extdrv3_011_vortex_spread_5d_diff_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv3_011_vortex_spread_5d_diff_5d_diff},
    "osc_extdrv3_012_vortex_neg_zscore_5d_diff_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv3_012_vortex_neg_zscore_5d_diff_5d_diff},
    "osc_extdrv3_013_williams_ad_roc21_5d_diff_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv3_013_williams_ad_roc21_5d_diff_5d_diff},
    "osc_extdrv3_014_williams_ad_flow_slope_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv3_014_williams_ad_flow_slope_5d_diff},
    "osc_extdrv3_015_cmo_14_zscore_5d_diff_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_015_cmo_14_zscore_5d_diff_5d_diff},
    "osc_extdrv3_016_trix_14_zscore_5d_diff_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_016_trix_14_zscore_5d_diff_5d_diff},
    "osc_extdrv3_017_ppo_zscore_5d_diff_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_017_ppo_zscore_5d_diff_5d_diff},
    "osc_extdrv3_018_kst_zscore_5d_diff_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_018_kst_zscore_5d_diff_5d_diff},
    "osc_extdrv3_019_coppock_zscore_5d_diff_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_019_coppock_zscore_5d_diff_5d_diff},
    "osc_extdrv3_020_smi_14_zscore_5d_diff_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv3_020_smi_14_zscore_5d_diff_5d_diff},
    "osc_extdrv3_021_schaff_5d_diff_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_021_schaff_5d_diff_5d_diff},
    "osc_extdrv3_022_klinger_signal_slope_5d_diff": {
        "inputs": ["high", "low", "close", "volume"], "func": osc_extdrv3_022_klinger_signal_slope_5d_diff},
    "osc_extdrv3_023_rvi_21d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"], "func": osc_extdrv3_023_rvi_21d_diff_5d_diff},
    "osc_extdrv3_024_fisher_10_zscore_5d_diff_5d_diff": {
        "inputs": ["high", "low", "close"], "func": osc_extdrv3_024_fisher_10_zscore_5d_diff_5d_diff},
    "osc_extdrv3_025_tsi_min21_5d_diff_5d_diff": {
        "inputs": ["close"], "func": osc_extdrv3_025_tsi_min21_5d_diff_5d_diff},
}
