"""
36_volatility_spike — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative vol-spike concepts — acceleration
        of velocity (jerk) in GKYZ vol, bipower variation, realized quarticity,
        jump fraction, downside semivariance, overnight/intraday vol decomposition,
        vol term-structure slope pairs, and cross-estimator spreads derived from
        the extended-base file (extended_001_075).
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_ANN     = np.sqrt(_TD_YEAR)
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _log_ret(close: pd.Series) -> pd.Series:
    return np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized realized volatility (rolling std of log-returns * sqrt(252))."""
    return _rolling_std(_log_ret(close), w) * _ANN


def _true_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    prev_c = close.shift(1)
    return pd.concat([high - low,
                      (high - prev_c).abs(),
                      (low  - prev_c).abs()], axis=1).max(axis=1)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Wilder-smoothed ATR."""
    tr = _true_range(high, low, close)
    return tr.ewm(alpha=1.0 / w, min_periods=max(1, w // 2), adjust=False).mean()


def _rs_day(open_: pd.Series, high: pd.Series,
            low: pd.Series, close: pd.Series) -> pd.Series:
    lhc = np.log(high.clip(lower=_EPS)  / close.clip(lower=_EPS))
    lho = np.log(high.clip(lower=_EPS)  / open_.clip(lower=_EPS))
    llc = np.log(low.clip(lower=_EPS)   / close.clip(lower=_EPS))
    llo = np.log(low.clip(lower=_EPS)   / open_.clip(lower=_EPS))
    return lhc * lho + llc * llo


def _rs_vol(open_: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    rs = _rs_day(open_, high, low, close)
    return np.sqrt(_rolling_mean(rs.clip(lower=0.0), w) * _TD_YEAR)


def _yz_vol(open_: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    """Yang-Zhang annualized vol."""
    if w < 2:
        w = 2
    prev_close = close.shift(1)
    ln_oc  = np.log(open_.clip(lower=_EPS) / prev_close.clip(lower=_EPS))
    ln_co  = np.log(close.clip(lower=_EPS)  / open_.clip(lower=_EPS))
    ov_m   = _rolling_mean(ln_oc, w)
    ov_var = _rolling_mean((ln_oc - ov_m) ** 2, w)
    oc_m   = _rolling_mean(ln_co, w)
    oc_var = _rolling_mean((ln_co - oc_m) ** 2, w)
    rs_var = _rolling_mean(_rs_day(open_, high, low, close).clip(lower=0.0), w)
    k = 0.34 / (1.34 + (w + 1.0) / max(w - 1.0, _EPS))
    yz_var = (ov_var + k * oc_var + (1.0 - k) * rs_var).clip(lower=0.0)
    return np.sqrt(yz_var * _TD_YEAR)


def _gk_vol(open_: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    """Garman-Klass annualized vol."""
    hl  = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    co  = np.log(close.clip(lower=_EPS) / open_.clip(lower=_EPS))
    gk_day = 0.5 * hl ** 2 - (2.0 * np.log(2.0) - 1.0) * co ** 2
    return np.sqrt(_rolling_mean(gk_day, w) * _TD_YEAR)


def _gkyz_vol(open_: pd.Series, high: pd.Series, low: pd.Series,
              close: pd.Series, w: int) -> pd.Series:
    """Garman-Klass-Yang-Zhang combined estimator."""
    prev_c = close.shift(1)
    ln_on  = np.log(open_.clip(lower=_EPS) / prev_c.clip(lower=_EPS))
    hl     = np.log(high.clip(lower=_EPS)  / low.clip(lower=_EPS))
    co     = np.log(close.clip(lower=_EPS) / open_.clip(lower=_EPS))
    gk_day = 0.5 * hl ** 2 - (2.0 * np.log(2.0) - 1.0) * co ** 2
    on_var = _rolling_mean(ln_on ** 2, w)
    gk_var = _rolling_mean(gk_day, w)
    return np.sqrt((on_var + gk_var).clip(lower=0.0) * _TD_YEAR)


def _bipower_var(close: pd.Series, w: int) -> pd.Series:
    """Bipower variation (annualized)."""
    lr = _log_ret(close).abs()
    bpv_daily = lr * lr.shift(1)
    return (np.pi / 2.0) * _rolling_mean(bpv_daily, w) * _TD_YEAR


def _realized_quarticity(close: pd.Series, w: int) -> pd.Series:
    """Realized quarticity: (n/3) * mean(r_t^4) * 252^2."""
    lr4 = _log_ret(close) ** 4
    return (w / 3.0) * _rolling_mean(lr4, w) * (_TD_YEAR ** 2)


def _overnight_ret(open_: pd.Series, close: pd.Series) -> pd.Series:
    return np.log(open_.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))


def _intraday_ret(open_: pd.Series, close: pd.Series) -> pd.Series:
    return np.log(close.clip(lower=_EPS) / open_.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Extended 3rd-Derivative Feature Functions ─────────────────────────────────
# Each function = diff/slope applied to the corresponding extended-2nd-derivative
# concept (second diff / slope-of-slope / diff-of-slope).

# --- Group A (001-005): GKYZ vol jerk (acceleration of velocity) ---

def vsp_extdrv3_001_gkyz_vol5_5d_diff_5d_diff(open_: pd.Series, high: pd.Series,
                                               low: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day GKYZ vol (jerk in GKYZ short-term vol)."""
    vel = _gkyz_vol(open_, high, low, close, _TD_WEEK).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_002_gkyz_vol21_5d_diff_5d_diff(open_: pd.Series, high: pd.Series,
                                                low: pd.Series,
                                                close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day GKYZ vol (jerk in monthly GKYZ vol)."""
    vel = _gkyz_vol(open_, high, low, close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_003_gkyz_vol5_zscore_252d_5d_diff_5d_diff(open_: pd.Series,
                                                            high: pd.Series,
                                                            low: pd.Series,
                                                            close: pd.Series) -> pd.Series:
    """Second 5-day diff of GKYZ-5d z-score (jerk in GKYZ extremity)."""
    v = _gkyz_vol(open_, high, low, close, _TD_WEEK)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_004_gkyz_vol5_vs_median63_5d_diff_5d_diff(open_: pd.Series,
                                                            high: pd.Series,
                                                            low: pd.Series,
                                                            close: pd.Series) -> pd.Series:
    """Second 5-day diff of GKYZ-5d/63d-median ratio (jerk in GKYZ spike ratio)."""
    v = _gkyz_vol(open_, high, low, close, _TD_WEEK)
    ratio = _safe_div(v, _rolling_median(v, _TD_QTR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_005_gkyz_vs_gk_ratio5_5d_diff_5d_diff(open_: pd.Series,
                                                        high: pd.Series,
                                                        low: pd.Series,
                                                        close: pd.Series) -> pd.Series:
    """Second 5-day diff of GKYZ/GK ratio (jerk in overnight jump premium)."""
    ratio = _safe_div(
        _gkyz_vol(open_, high, low, close, _TD_WEEK),
        _gk_vol(open_, high, low, close, _TD_WEEK)
    )
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group B (006-009): Bipower variation jerk ---

def vsp_extdrv3_006_bipower_var21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day bipower variation (jerk in jump-robust vol)."""
    vel = _bipower_var(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_007_bipower_var21_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d-bipower var 21d-velocity (slope of monthly bipower change)."""
    vel = _bipower_var(close, _TD_MON).diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_008_bipower_var21_vs_median252_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d bipower var / 252d-median ratio (jerk in spike ratio)."""
    v = _bipower_var(close, _TD_MON)
    ratio = _safe_div(v, _rolling_median(v, _TD_YEAR))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_009_jump_fraction21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day jump fraction (jerk in jump share of total vol)."""
    rv  = (_rolling_mean(_log_ret(close) ** 2, _TD_MON) * _TD_YEAR).clip(lower=_EPS)
    bpv = _bipower_var(close, _TD_MON).clip(lower=0.0)
    jf  = _safe_div((rv - bpv).clip(lower=0.0), rv)
    vel = jf.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group C (010-013): Downside semivariance jerk ---

def vsp_extdrv3_010_downside_semivar21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day downside semivariance (jerk in fear vol)."""
    lr = _log_ret(close)
    neg_sq = (lr.clip(upper=0.0)) ** 2
    v = _rolling_mean(neg_sq, _TD_MON) * _TD_YEAR
    vel = v.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_011_downside_semivar21_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d-downside-semivar monthly velocity (slope of monthly fear change)."""
    lr = _log_ret(close)
    neg_sq = (lr.clip(upper=0.0)) ** 2
    v = _rolling_mean(neg_sq, _TD_MON) * _TD_YEAR
    vel = v.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_012_semivol_ratio_down_up21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of down/up semivariance ratio (jerk in fear asymmetry)."""
    lr = _log_ret(close)
    neg_sq = (lr.clip(upper=0.0)) ** 2
    pos_sq = (lr.clip(lower=0.0)) ** 2
    d = _rolling_mean(neg_sq, _TD_MON) * _TD_YEAR
    u = (_rolling_mean(pos_sq, _TD_MON) * _TD_YEAR).replace(0, np.nan)
    ratio = _safe_div(d, u)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_013_downside_semivar21_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d downside semivar z-score (jerk in fear extremity)."""
    lr = _log_ret(close)
    neg_sq = (lr.clip(upper=0.0)) ** 2
    v = _rolling_mean(neg_sq, _TD_MON) * _TD_YEAR
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group D (014-017): Overnight / intraday vol jerk ---

def vsp_extdrv3_014_overnight_vol21_5d_diff_5d_diff(open_: pd.Series,
                                                     close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day overnight vol (jerk in gap risk)."""
    on_r = _overnight_ret(open_, close)
    v = _rolling_std(on_r, _TD_MON) * _ANN
    vel = v.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_015_intraday_vol21_5d_diff_5d_diff(open_: pd.Series,
                                                    close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day intraday vol (jerk in session vol)."""
    id_r = _intraday_ret(open_, close)
    v = _rolling_std(id_r, _TD_MON) * _ANN
    vel = v.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_016_overnight_vs_intraday_ratio21_5d_diff_5d_diff(
        open_: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight/intraday vol ratio (jerk in gap dominance)."""
    on_r = _overnight_ret(open_, close)
    id_r = _intraday_ret(open_, close)
    on_v = _rolling_std(on_r, _TD_MON) * _ANN
    id_v = (_rolling_std(id_r, _TD_MON) * _ANN).replace(0, np.nan)
    ratio = _safe_div(on_v, id_v)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_017_overnight_vol21_zscore_5d_diff_5d_diff(open_: pd.Series,
                                                            close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d overnight vol z-score (jerk in gap vol extremity)."""
    on_r = _overnight_ret(open_, close)
    v = _rolling_std(on_r, _TD_MON) * _ANN
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group E (018-020): Extended vol term-structure slope jerk ---

def vsp_extdrv3_018_rvol_term_slope_3_21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 3d-21d vol term slope (jerk in ultra-short slope)."""
    slope = _realized_vol(close, 3) - _realized_vol(close, _TD_MON)
    vel = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_019_rvol_term_slope_21_126_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d-126d vol term slope (jerk in monthly/semi-annual slope)."""
    slope = _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_HALF)
    vel = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_020_rvol_term_slope_10_63_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 10d-63d vol term slope (jerk in bi-weekly/quarterly slope)."""
    slope = _realized_vol(close, 10) - _realized_vol(close, _TD_QTR)
    vel = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group F (021-022): Cross-estimator spread jerk ---

def vsp_extdrv3_021_yz_vs_rs_spread21_5d_diff_5d_diff(open_: pd.Series, high: pd.Series,
                                                        low: pd.Series,
                                                        close: pd.Series) -> pd.Series:
    """Second 5-day diff of |YZ - RS| vol spread (21d) — jerk in overnight contribution."""
    spread = (_yz_vol(open_, high, low, close, _TD_MON)
              - _rs_vol(open_, high, low, close, _TD_MON)).abs()
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_022_gkyz_vs_yz_spread5_5d_diff_5d_diff(open_: pd.Series, high: pd.Series,
                                                         low: pd.Series,
                                                         close: pd.Series) -> pd.Series:
    """Second 5-day diff of GKYZ-minus-YZ spread (5d) — jerk in overnight variance component."""
    spread = (_gkyz_vol(open_, high, low, close, _TD_WEEK)
              - _yz_vol(open_, high, low, close, _TD_WEEK))
    vel = spread.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group G (023-024): Realized quarticity jerk ---

def vsp_extdrv3_023_quarticity21_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day realized quarticity (jerk in tail risk measure)."""
    vel = _realized_quarticity(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vsp_extdrv3_024_quarticity21_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d quarticity z-score (jerk in tail extremity)."""
    v = _realized_quarticity(close, _TD_MON)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    z = _safe_div(v - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group H (025): ATR extended baseline jerk ---

def vsp_extdrv3_025_atr5_vs_median126_5d_diff_5d_diff(high: pd.Series, low: pd.Series,
                                                        close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5d ATR / 126d-median ratio (jerk in short ATR vs long baseline)."""
    v = _atr(high, low, close, _TD_WEEK)
    ratio = _safe_div(v, _rolling_median(v, _TD_HALF))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_SPIKE_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "vsp_extdrv3_001_gkyz_vol5_5d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"],
        "func": vsp_extdrv3_001_gkyz_vol5_5d_diff_5d_diff,
    },
    "vsp_extdrv3_002_gkyz_vol21_5d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"],
        "func": vsp_extdrv3_002_gkyz_vol21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_003_gkyz_vol5_zscore_252d_5d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"],
        "func": vsp_extdrv3_003_gkyz_vol5_zscore_252d_5d_diff_5d_diff,
    },
    "vsp_extdrv3_004_gkyz_vol5_vs_median63_5d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"],
        "func": vsp_extdrv3_004_gkyz_vol5_vs_median63_5d_diff_5d_diff,
    },
    "vsp_extdrv3_005_gkyz_vs_gk_ratio5_5d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"],
        "func": vsp_extdrv3_005_gkyz_vs_gk_ratio5_5d_diff_5d_diff,
    },
    "vsp_extdrv3_006_bipower_var21_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_006_bipower_var21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_007_bipower_var21_21d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_007_bipower_var21_21d_diff_5d_diff,
    },
    "vsp_extdrv3_008_bipower_var21_vs_median252_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_008_bipower_var21_vs_median252_5d_diff_5d_diff,
    },
    "vsp_extdrv3_009_jump_fraction21_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_009_jump_fraction21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_010_downside_semivar21_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_010_downside_semivar21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_011_downside_semivar21_21d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_011_downside_semivar21_21d_diff_5d_diff,
    },
    "vsp_extdrv3_012_semivol_ratio_down_up21_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_012_semivol_ratio_down_up21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_013_downside_semivar21_zscore_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_013_downside_semivar21_zscore_5d_diff_5d_diff,
    },
    "vsp_extdrv3_014_overnight_vol21_5d_diff_5d_diff": {
        "inputs": ["open", "close"],
        "func": vsp_extdrv3_014_overnight_vol21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_015_intraday_vol21_5d_diff_5d_diff": {
        "inputs": ["open", "close"],
        "func": vsp_extdrv3_015_intraday_vol21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_016_overnight_vs_intraday_ratio21_5d_diff_5d_diff": {
        "inputs": ["open", "close"],
        "func": vsp_extdrv3_016_overnight_vs_intraday_ratio21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_017_overnight_vol21_zscore_5d_diff_5d_diff": {
        "inputs": ["open", "close"],
        "func": vsp_extdrv3_017_overnight_vol21_zscore_5d_diff_5d_diff,
    },
    "vsp_extdrv3_018_rvol_term_slope_3_21_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_018_rvol_term_slope_3_21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_019_rvol_term_slope_21_126_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_019_rvol_term_slope_21_126_5d_diff_5d_diff,
    },
    "vsp_extdrv3_020_rvol_term_slope_10_63_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_020_rvol_term_slope_10_63_5d_diff_5d_diff,
    },
    "vsp_extdrv3_021_yz_vs_rs_spread21_5d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"],
        "func": vsp_extdrv3_021_yz_vs_rs_spread21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_022_gkyz_vs_yz_spread5_5d_diff_5d_diff": {
        "inputs": ["open", "high", "low", "close"],
        "func": vsp_extdrv3_022_gkyz_vs_yz_spread5_5d_diff_5d_diff,
    },
    "vsp_extdrv3_023_quarticity21_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_023_quarticity21_5d_diff_5d_diff,
    },
    "vsp_extdrv3_024_quarticity21_zscore_5d_diff_5d_diff": {
        "inputs": ["close"],
        "func": vsp_extdrv3_024_quarticity21_zscore_5d_diff_5d_diff,
    },
    "vsp_extdrv3_025_atr5_vs_median126_5d_diff_5d_diff": {
        "inputs": ["high", "low", "close"],
        "func": vsp_extdrv3_025_atr5_vs_median126_5d_diff_5d_diff,
    },
}
