"""
36_volatility_spike — Extended Features 001-075
Domain: realized volatility spikes vs trailing baseline — deeper spike coverage:
        ATR/RS/YZ at additional lookbacks and baselines; Garman-Klass-Yang-Zhang;
        bipower variation and realized quarticity; jump vs continuous decomposition;
        upside vs downside realized semivariance; intraday vs overnight vol split;
        vol term-structure slope at additional pairs; vol-spike acceleration (ROC);
        cross-estimator spread/divergence; consecutive elevated-vol streaks;
        days-since-last-spike; spike-count at additional thresholds.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _log_ret(close: pd.Series) -> pd.Series:
    return np.log(close.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized realized volatility (rolling std of log-returns * sqrt(252))."""
    return _rolling_std(_log_ret(close), w) * _ANN


def _parkinson_vol(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    hl2 = (np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS)) ** 2)
    return np.sqrt(_rolling_mean(hl2, w) / (4.0 * np.log(2.0))) * _ANN


def _gk_vol(open_: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    """Garman-Klass annualized volatility estimator."""
    hl  = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    co  = np.log(close.clip(lower=_EPS) / open_.clip(lower=_EPS))
    gk_day = 0.5 * hl ** 2 - (2.0 * np.log(2.0) - 1.0) * co ** 2
    return np.sqrt(_rolling_mean(gk_day, w) * _TD_YEAR)


def _rs_day(open_: pd.Series, high: pd.Series,
            low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily Rogers-Satchell term: ln(H/C)*ln(H/O) + ln(L/C)*ln(L/O)."""
    lhc = np.log(high.clip(lower=_EPS)  / close.clip(lower=_EPS))
    lho = np.log(high.clip(lower=_EPS)  / open_.clip(lower=_EPS))
    llc = np.log(low.clip(lower=_EPS)   / close.clip(lower=_EPS))
    llo = np.log(low.clip(lower=_EPS)   / open_.clip(lower=_EPS))
    return lhc * lho + llc * llo


def _rs_vol(open_: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    """Rogers-Satchell annualized vol."""
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


def _true_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    prev_c = close.shift(1)
    return pd.concat([high - low,
                      (high - prev_c).abs(),
                      (low  - prev_c).abs()], axis=1).max(axis=1)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Wilder-smoothed ATR."""
    tr = _true_range(high, low, close)
    return tr.ewm(alpha=1.0 / w, min_periods=max(1, w // 2), adjust=False).mean()


def _gkyz_vol(open_: pd.Series, high: pd.Series, low: pd.Series,
              close: pd.Series, w: int) -> pd.Series:
    """Garman-Klass-Yang-Zhang combined estimator.
    GKYZ = GK variance + overnight variance component.
    overnight_var = rolling_mean(ln(open/prev_close)^2, w)
    gk_var        = rolling_mean(0.5*ln(H/L)^2 - (2*ln2-1)*ln(C/O)^2, w)
    gkyz_var      = overnight_var + gk_var
    """
    prev_c = close.shift(1)
    ln_on  = np.log(open_.clip(lower=_EPS) / prev_c.clip(lower=_EPS))
    hl     = np.log(high.clip(lower=_EPS)  / low.clip(lower=_EPS))
    co     = np.log(close.clip(lower=_EPS) / open_.clip(lower=_EPS))
    gk_day = 0.5 * hl ** 2 - (2.0 * np.log(2.0) - 1.0) * co ** 2
    on_var = _rolling_mean(ln_on ** 2, w)
    gk_var = _rolling_mean(gk_day, w)
    return np.sqrt((on_var + gk_var).clip(lower=0.0) * _TD_YEAR)


def _bipower_var(close: pd.Series, w: int) -> pd.Series:
    """Bipower variation (Barndorff-Nielsen & Shephard): (pi/2) * mean(|r_t|*|r_{t-1}|).
    Annualized by multiplying by 252."""
    lr = _log_ret(close).abs()
    bpv_daily = lr * lr.shift(1)
    return (np.pi / 2.0) * _rolling_mean(bpv_daily, w) * _TD_YEAR


def _realized_quarticity(close: pd.Series, w: int) -> pd.Series:
    """Realized quarticity: (n/3) * mean(r_t^4) * 252^2 — scaled."""
    lr4 = _log_ret(close) ** 4
    n = w
    return (n / 3.0) * _rolling_mean(lr4, w) * (_TD_YEAR ** 2)


def _overnight_ret(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Log overnight return: ln(open / prev_close)."""
    return np.log(open_.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))


def _intraday_ret(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Log intraday return: ln(close / open)."""
    return np.log(close.clip(lower=_EPS) / open_.clip(lower=_EPS))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-008): ATR at additional lookbacks & baseline windows ---

def vsp_ext_001_atr_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day Wilder ATR (shorter window not in existing 14/21/63d set)."""
    return _atr(high, low, close, _TD_WEEK)


def vsp_ext_002_atr_7d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """7-day Wilder ATR."""
    return _atr(high, low, close, 7)


def vsp_ext_003_atr_42d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """42-day Wilder ATR (2-month window)."""
    return _atr(high, low, close, 42)


def vsp_ext_004_atr5_vs_median126(high: pd.Series, low: pd.Series,
                                   close: pd.Series) -> pd.Series:
    """5-day ATR divided by its 126-day trailing median (longer baseline)."""
    v = _atr(high, low, close, _TD_WEEK)
    return _safe_div(v, _rolling_median(v, _TD_HALF))


def vsp_ext_005_atr21_vs_median126(high: pd.Series, low: pd.Series,
                                    close: pd.Series) -> pd.Series:
    """21-day ATR divided by its 126-day trailing median."""
    v = _atr(high, low, close, _TD_MON)
    return _safe_div(v, _rolling_median(v, _TD_HALF))


def vsp_ext_006_atr14_zscore_126d(high: pd.Series, low: pd.Series,
                                   close: pd.Series) -> pd.Series:
    """Z-score of 14-day ATR vs its 126-day rolling distribution (medium baseline)."""
    v = _atr(high, low, close, 14)
    m = _rolling_mean(v, _TD_HALF)
    s = _rolling_std(v, _TD_HALF)
    return _safe_div(v - m, s)


def vsp_ext_007_natr5_vs_median252(high: pd.Series, low: pd.Series,
                                    close: pd.Series) -> pd.Series:
    """Normalized 5-day ATR/close divided by its 252-day trailing median."""
    natr = _safe_div(_atr(high, low, close, _TD_WEEK), close.clip(lower=_EPS))
    return _safe_div(natr, _rolling_median(natr, _TD_YEAR))


def vsp_ext_008_atr14_spike_count_252d(high: pd.Series, low: pd.Series,
                                        close: pd.Series) -> pd.Series:
    """Days in trailing 252d where 14-day ATR > 2x its 63-day trailing median."""
    v = _atr(high, low, close, 14)
    is_spike = (v > 2.0 * _rolling_median(v, _TD_QTR)).astype(float)
    return _rolling_sum(is_spike, _TD_YEAR)


# --- Group B (009-016): Rogers-Satchell at additional windows & baselines ---

def vsp_ext_009_rs_vol_5d(open_: pd.Series, high: pd.Series,
                           low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day Rogers-Satchell annualized vol (shorter than existing 21/63d)."""
    return _rs_vol(open_, high, low, close, _TD_WEEK)


def vsp_ext_010_rs_vol_126d(open_: pd.Series, high: pd.Series,
                             low: pd.Series, close: pd.Series) -> pd.Series:
    """126-day Rogers-Satchell annualized vol (half-year baseline)."""
    return _rs_vol(open_, high, low, close, _TD_HALF)


def vsp_ext_011_rs_vol5_vs_median63(open_: pd.Series, high: pd.Series,
                                     low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day RS vol divided by its 63-day trailing median."""
    v = _rs_vol(open_, high, low, close, _TD_WEEK)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_ext_012_rs_vol5_zscore_252d(open_: pd.Series, high: pd.Series,
                                     low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 5-day RS vol vs 252-day rolling distribution."""
    v = _rs_vol(open_, high, low, close, _TD_WEEK)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_ext_013_rs_vol63_vs_median252(open_: pd.Series, high: pd.Series,
                                       low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day RS vol divided by its 252-day trailing median."""
    v = _rs_vol(open_, high, low, close, _TD_QTR)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_ext_014_rs_vol21_spike_count_252d(open_: pd.Series, high: pd.Series,
                                           low: pd.Series, close: pd.Series) -> pd.Series:
    """Days in trailing 252d where 21-day RS vol > 2x its 63-day trailing median."""
    v = _rs_vol(open_, high, low, close, _TD_MON)
    is_spike = (v > 2.0 * _rolling_median(v, _TD_QTR)).astype(float)
    return _rolling_sum(is_spike, _TD_YEAR)


def vsp_ext_015_rs_vol21_pct_rank_126d(open_: pd.Series, high: pd.Series,
                                        low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day RS vol within trailing 126-day series."""
    v = _rs_vol(open_, high, low, close, _TD_MON)
    return v.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def vsp_ext_016_rs_vol5_vs_rvol5(open_: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day RS vol to 5-day close-to-close realized vol."""
    return _safe_div(
        _rs_vol(open_, high, low, close, _TD_WEEK),
        _realized_vol(close, _TD_WEEK)
    )


# --- Group C (017-024): Yang-Zhang at additional windows & baselines ---

def vsp_ext_017_yz_vol_5d(open_: pd.Series, high: pd.Series,
                           low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day Yang-Zhang annualized vol (shorter than existing 21/63d)."""
    return _yz_vol(open_, high, low, close, _TD_WEEK)


def vsp_ext_018_yz_vol_126d(open_: pd.Series, high: pd.Series,
                             low: pd.Series, close: pd.Series) -> pd.Series:
    """126-day Yang-Zhang annualized vol."""
    return _yz_vol(open_, high, low, close, _TD_HALF)


def vsp_ext_019_yz_vol5_vs_median63(open_: pd.Series, high: pd.Series,
                                     low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day YZ vol divided by its 63-day trailing median."""
    v = _yz_vol(open_, high, low, close, _TD_WEEK)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_ext_020_yz_vol5_zscore_252d(open_: pd.Series, high: pd.Series,
                                     low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 5-day YZ vol vs 252-day rolling distribution."""
    v = _yz_vol(open_, high, low, close, _TD_WEEK)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_ext_021_yz_vol63_vs_median252(open_: pd.Series, high: pd.Series,
                                       low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day YZ vol divided by its 252-day trailing median."""
    v = _yz_vol(open_, high, low, close, _TD_QTR)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_ext_022_yz_vol21_spike_count_252d(open_: pd.Series, high: pd.Series,
                                           low: pd.Series, close: pd.Series) -> pd.Series:
    """Days in trailing 252d where 21-day YZ vol > 2x its 63-day trailing median."""
    v = _yz_vol(open_, high, low, close, _TD_MON)
    is_spike = (v > 2.0 * _rolling_median(v, _TD_QTR)).astype(float)
    return _rolling_sum(is_spike, _TD_YEAR)


def vsp_ext_023_yz_vol5_vs_rvol5(open_: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day YZ vol to 5-day close-to-close realized vol."""
    return _safe_div(
        _yz_vol(open_, high, low, close, _TD_WEEK),
        _realized_vol(close, _TD_WEEK)
    )


def vsp_ext_024_yz_vol21_pct_rank_126d(open_: pd.Series, high: pd.Series,
                                        low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day YZ vol within trailing 126-day series."""
    v = _yz_vol(open_, high, low, close, _TD_MON)
    return v.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


# --- Group D (025-030): Garman-Klass-Yang-Zhang estimator ---

def vsp_ext_025_gkyz_vol_5d(open_: pd.Series, high: pd.Series,
                              low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day Garman-Klass-Yang-Zhang annualized vol (GK + overnight variance)."""
    return _gkyz_vol(open_, high, low, close, _TD_WEEK)


def vsp_ext_026_gkyz_vol_21d(open_: pd.Series, high: pd.Series,
                               low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Garman-Klass-Yang-Zhang annualized vol."""
    return _gkyz_vol(open_, high, low, close, _TD_MON)


def vsp_ext_027_gkyz_vol5_vs_median63(open_: pd.Series, high: pd.Series,
                                        low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day GKYZ vol divided by its 63-day trailing median."""
    v = _gkyz_vol(open_, high, low, close, _TD_WEEK)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_ext_028_gkyz_vol5_zscore_252d(open_: pd.Series, high: pd.Series,
                                        low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 5-day GKYZ vol vs 252-day rolling distribution."""
    v = _gkyz_vol(open_, high, low, close, _TD_WEEK)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_ext_029_gkyz_vs_gk_ratio_5d(open_: pd.Series, high: pd.Series,
                                      low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day GKYZ vol to 5-day GK vol (overnight jump premium)."""
    return _safe_div(
        _gkyz_vol(open_, high, low, close, _TD_WEEK),
        _gk_vol(open_, high, low, close, _TD_WEEK)
    )


def vsp_ext_030_gkyz_vol21_pct_rank_252d(open_: pd.Series, high: pd.Series,
                                          low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day GKYZ vol within trailing 252-day series."""
    v = _gkyz_vol(open_, high, low, close, _TD_MON)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


# --- Group E (031-036): Bipower variation and realized quarticity ---

def vsp_ext_031_bipower_var_21d(close: pd.Series) -> pd.Series:
    """21-day bipower variation (annualized) — robust to jumps."""
    return _bipower_var(close, _TD_MON)


def vsp_ext_032_bipower_var_63d(close: pd.Series) -> pd.Series:
    """63-day bipower variation (annualized)."""
    return _bipower_var(close, _TD_QTR)


def vsp_ext_033_bipower_var21_vs_median252(close: pd.Series) -> pd.Series:
    """21-day bipower var divided by its 252-day trailing median."""
    v = _bipower_var(close, _TD_MON)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_ext_034_realized_quarticity_21d(close: pd.Series) -> pd.Series:
    """21-day realized quarticity (scaled fourth moment of returns)."""
    return _realized_quarticity(close, _TD_MON)


def vsp_ext_035_quarticity21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day realized quarticity vs 252-day rolling distribution."""
    v = _realized_quarticity(close, _TD_MON)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_ext_036_quarticity21_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day realized quarticity within trailing 252-day series."""
    v = _realized_quarticity(close, _TD_MON)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


# --- Group F (037-040): Jump vs continuous variation split ---

def vsp_ext_037_jump_var_21d(close: pd.Series) -> pd.Series:
    """21-day jump variance = max(realized_var - bipower_var, 0) (annualized).
    Isolates the jump component of total variance."""
    rv = _rolling_mean(_log_ret(close) ** 2, _TD_MON) * _TD_YEAR
    bpv = _bipower_var(close, _TD_MON)
    return (rv - bpv).clip(lower=0.0)


def vsp_ext_038_continuous_var_21d(close: pd.Series) -> pd.Series:
    """21-day continuous variance = bipower variation (annualized).
    Diffusive component free of jump contamination."""
    return _bipower_var(close, _TD_MON)


def vsp_ext_039_jump_fraction_21d(close: pd.Series) -> pd.Series:
    """Jump fraction: jump_var / total_realized_var over 21 days.
    Near 1 = vol dominated by jumps; near 0 = diffusive."""
    rv = (_rolling_mean(_log_ret(close) ** 2, _TD_MON) * _TD_YEAR).clip(lower=_EPS)
    bpv = _bipower_var(close, _TD_MON).clip(lower=0.0)
    jump_var = (rv - bpv).clip(lower=0.0)
    return _safe_div(jump_var, rv)


def vsp_ext_040_jump_fraction21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day jump fraction vs trailing 252-day distribution."""
    rv  = (_rolling_mean(_log_ret(close) ** 2, _TD_MON) * _TD_YEAR).clip(lower=_EPS)
    bpv = _bipower_var(close, _TD_MON).clip(lower=0.0)
    jf  = _safe_div((rv - bpv).clip(lower=0.0), rv)
    m   = _rolling_mean(jf, _TD_YEAR)
    s   = _rolling_std(jf, _TD_YEAR)
    return _safe_div(jf - m, s)


# --- Group G (041-046): Upside vs downside realized semivariance ---

def vsp_ext_041_downside_semivar_21d(close: pd.Series) -> pd.Series:
    """21-day downside realized semivariance (annualized): mean of negative-return^2.
    Captures vol concentrated in down-moves."""
    lr = _log_ret(close)
    neg_sq = (lr.clip(upper=0.0)) ** 2
    return _rolling_mean(neg_sq, _TD_MON) * _TD_YEAR


def vsp_ext_042_upside_semivar_21d(close: pd.Series) -> pd.Series:
    """21-day upside realized semivariance (annualized): mean of positive-return^2."""
    lr = _log_ret(close)
    pos_sq = (lr.clip(lower=0.0)) ** 2
    return _rolling_mean(pos_sq, _TD_MON) * _TD_YEAR


def vsp_ext_043_semivol_ratio_down_up_21d(close: pd.Series) -> pd.Series:
    """Ratio of downside to upside semivariance over 21 days.
    >1 = fear-driven; spikes near capitulation."""
    d = vsp_ext_041_downside_semivar_21d(close)
    u = vsp_ext_042_upside_semivar_21d(close)
    return _safe_div(d, u.replace(0, np.nan))


def vsp_ext_044_downside_semivar21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day downside semivariance vs trailing 252-day distribution."""
    v = vsp_ext_041_downside_semivar_21d(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_ext_045_downside_semivar21_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day downside semivariance within trailing 252 days."""
    v = vsp_ext_041_downside_semivar_21d(close)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_ext_046_semivol_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of down/up semivariance ratio vs trailing 252-day distribution."""
    v = vsp_ext_043_semivol_ratio_down_up_21d(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


# --- Group H (047-052): Intraday vs overnight volatility decomposition ---

def vsp_ext_047_overnight_vol_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """21-day overnight realized vol (annualized): std of ln(open/prev_close)."""
    on_r = _overnight_ret(open_, close)
    return _rolling_std(on_r, _TD_MON) * _ANN


def vsp_ext_048_intraday_vol_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """21-day intraday realized vol (annualized): std of ln(close/open)."""
    id_r = _intraday_ret(open_, close)
    return _rolling_std(id_r, _TD_MON) * _ANN


def vsp_ext_049_overnight_vs_intraday_vol_ratio_21d(open_: pd.Series,
                                                      close: pd.Series) -> pd.Series:
    """Ratio of 21-day overnight vol to 21-day intraday vol.
    High ratio = gaps dominating; capitulation often gap-driven."""
    return _safe_div(
        vsp_ext_047_overnight_vol_21d(open_, close),
        vsp_ext_048_intraday_vol_21d(open_, close)
    )


def vsp_ext_050_overnight_vol21_zscore_252d(open_: pd.Series,
                                             close: pd.Series) -> pd.Series:
    """Z-score of 21-day overnight vol vs trailing 252-day distribution."""
    v = vsp_ext_047_overnight_vol_21d(open_, close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_ext_051_overnight_vol21_pct_rank_252d(open_: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day overnight vol within trailing 252-day series."""
    v = vsp_ext_047_overnight_vol_21d(open_, close)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_ext_052_overnight_vs_total_vol_fraction_21d(open_: pd.Series,
                                                     close: pd.Series) -> pd.Series:
    """Fraction of total 21-day variance attributable to overnight moves.
    Total variance ≈ overnight_var + intraday_var."""
    on_r = _overnight_ret(open_, close)
    id_r = _intraday_ret(open_, close)
    on_var = _rolling_mean(on_r ** 2, _TD_MON)
    id_var = _rolling_mean(id_r ** 2, _TD_MON)
    total = (on_var + id_var).replace(0, np.nan)
    return _safe_div(on_var, total)


# --- Group I (053-057): Vol term-structure slope additional pairs ---

def vsp_ext_053_rvol_term_slope_3_21(close: pd.Series) -> pd.Series:
    """Diff of 3-day realized vol minus 21-day (ultra-short vs monthly term slope)."""
    return _realized_vol(close, 3) - _realized_vol(close, _TD_MON)


def vsp_ext_054_rvol_term_slope_10_63(close: pd.Series) -> pd.Series:
    """Diff of 10-day realized vol minus 63-day (bi-weekly vs quarterly slope)."""
    return _realized_vol(close, 10) - _realized_vol(close, _TD_QTR)


def vsp_ext_055_rvol_term_slope_21_126(close: pd.Series) -> pd.Series:
    """Diff of 21-day realized vol minus 126-day (monthly vs semi-annual slope)."""
    return _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_HALF)


def vsp_ext_056_rvol_term_slope_21_126_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-126 day vol term-structure slope vs 252-day distribution."""
    v = vsp_ext_055_rvol_term_slope_21_126(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_ext_057_rvol_term_slope_5_63_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-63 day vol term-structure slope within trailing 252 days."""
    v = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_QTR)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


# --- Group J (058-063): Vol-spike acceleration (rate-of-change variants) ---

def vsp_ext_058_rvol5_roc_5d(close: pd.Series) -> pd.Series:
    """Pct rate-of-change of 5-day realized vol over 5 days: (v/v_lag - 1)."""
    v = _realized_vol(close, _TD_WEEK)
    return _safe_div(v, v.shift(_TD_WEEK).replace(0, np.nan)) - 1.0


def vsp_ext_059_rvol5_roc_21d(close: pd.Series) -> pd.Series:
    """Pct rate-of-change of 5-day realized vol over 21 days."""
    v = _realized_vol(close, _TD_WEEK)
    return _safe_div(v, v.shift(_TD_MON).replace(0, np.nan)) - 1.0


def vsp_ext_060_atr14_roc_5d(high: pd.Series, low: pd.Series,
                               close: pd.Series) -> pd.Series:
    """Pct rate-of-change of 14-day ATR over 5 days."""
    v = _atr(high, low, close, 14)
    return _safe_div(v, v.shift(_TD_WEEK).replace(0, np.nan)) - 1.0


def vsp_ext_061_yz_vol21_roc_5d(open_: pd.Series, high: pd.Series,
                                  low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct rate-of-change of 21-day YZ vol over 5 days."""
    v = _yz_vol(open_, high, low, close, _TD_MON)
    return _safe_div(v, v.shift(_TD_WEEK).replace(0, np.nan)) - 1.0


def vsp_ext_062_rvol5_roc_5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day vol 5d-ROC vs trailing 252-day distribution."""
    v = vsp_ext_058_rvol5_roc_5d(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_ext_063_rs_vol21_roc_5d(open_: pd.Series, high: pd.Series,
                                  low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct rate-of-change of 21-day RS vol over 5 days."""
    v = _rs_vol(open_, high, low, close, _TD_MON)
    return _safe_div(v, v.shift(_TD_WEEK).replace(0, np.nan)) - 1.0


# --- Group K (064-068): Cross-estimator spread / divergence features ---

def vsp_ext_064_yz_vs_rs_spread_21d(open_: pd.Series, high: pd.Series,
                                      low: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute spread between 21-day YZ vol and 21-day RS vol.
    YZ includes overnight; RS does not — spread measures overnight contribution."""
    return (_yz_vol(open_, high, low, close, _TD_MON)
            - _rs_vol(open_, high, low, close, _TD_MON)).abs()


def vsp_ext_065_gk_vs_rvol_spread_5d(open_: pd.Series, high: pd.Series,
                                       low: pd.Series, close: pd.Series) -> pd.Series:
    """GK vol minus close-to-close realized vol (5d): intraday range premium."""
    return (_gk_vol(open_, high, low, close, _TD_WEEK)
            - _realized_vol(close, _TD_WEEK))


def vsp_ext_066_pk_vs_rvol_spread_5d(close: pd.Series, high: pd.Series,
                                       low: pd.Series) -> pd.Series:
    """Parkinson vol minus close-to-close realized vol (5d): range-close divergence."""
    return (_parkinson_vol(high, low, _TD_WEEK)
            - _realized_vol(close, _TD_WEEK))


def vsp_ext_067_cross_estimator_spread_zscore_252d(open_: pd.Series, high: pd.Series,
                                                     low: pd.Series,
                                                     close: pd.Series) -> pd.Series:
    """Z-score of YZ-RS spread (21d) vs its 252-day distribution."""
    v = vsp_ext_064_yz_vs_rs_spread_21d(open_, high, low, close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_ext_068_gkyz_vs_yz_spread_5d(open_: pd.Series, high: pd.Series,
                                       low: pd.Series, close: pd.Series) -> pd.Series:
    """GKYZ vol minus YZ vol (5d): incremental overnight variance contribution."""
    return (_gkyz_vol(open_, high, low, close, _TD_WEEK)
            - _yz_vol(open_, high, low, close, _TD_WEEK))


# --- Group L (069-072): Consecutive elevated-vol streaks ---

def vsp_ext_069_consec_elevated_streak_rvol5(close: pd.Series) -> pd.Series:
    """Consecutive days where 5-day realized vol > its trailing 63-day median.
    Resets to 0 on non-elevated days. Uses cumsum trick."""
    v = _realized_vol(close, _TD_WEEK)
    med = _rolling_median(v, _TD_QTR)
    flag = (v > med).astype(int)
    # cumsum-based streak: streak_i = flag_i * (streak_{i-1} + flag_i)
    # implemented via iterative pandas cumsum group method
    group = (flag == 0).cumsum()
    streak = flag.groupby(group).cumsum()
    return streak.astype(float)


def vsp_ext_070_consec_elevated_streak_atr14(high: pd.Series, low: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """Consecutive days where 14-day ATR > its trailing 63-day median."""
    v = _atr(high, low, close, 14)
    med = _rolling_median(v, _TD_QTR)
    flag = (v > med).astype(int)
    group = (flag == 0).cumsum()
    streak = flag.groupby(group).cumsum()
    return streak.astype(float)


def vsp_ext_071_consec_spike_streak_rvol5_2x(close: pd.Series) -> pd.Series:
    """Consecutive days where 5-day realized vol > 2x its 63-day trailing median."""
    v = _realized_vol(close, _TD_WEEK)
    med = _rolling_median(v, _TD_QTR)
    flag = (v > 2.0 * med).astype(int)
    group = (flag == 0).cumsum()
    streak = flag.groupby(group).cumsum()
    return streak.astype(float)


def vsp_ext_072_max_consec_spike_streak_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive-spike-streak value seen in trailing 63 days."""
    streak = vsp_ext_071_consec_spike_streak_rvol5_2x(close)
    return _rolling_max(streak, _TD_QTR)


# --- Group M (073-075): Days-since-last-spike ---

def vsp_ext_073_days_since_rvol5_spike_2x(close: pd.Series) -> pd.Series:
    """Days elapsed since last day where 5-day vol > 2x its 63-day trailing median.
    Returns forward-filled count; NaN before first spike."""
    v = _realized_vol(close, _TD_WEEK)
    med = _rolling_median(v, _TD_QTR)
    flag = (v > 2.0 * med)
    # assign row index as int counter; where spike, reset counter
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_spike_idx = idx.where(flag).ffill()
    return (idx - last_spike_idx).where(last_spike_idx.notna())


def vsp_ext_074_days_since_atr14_spike_2x(high: pd.Series, low: pd.Series,
                                            close: pd.Series) -> pd.Series:
    """Days elapsed since last day where 14-day ATR > 2x its 63-day trailing median."""
    v = _atr(high, low, close, 14)
    med = _rolling_median(v, _TD_QTR)
    flag = (v > 2.0 * med)
    idx = pd.Series(np.arange(len(close)), index=close.index, dtype=float)
    last_spike_idx = idx.where(flag).ffill()
    return (idx - last_spike_idx).where(last_spike_idx.notna())


def vsp_ext_075_spike_count_gt3x_median_63d_rvol5(close: pd.Series) -> pd.Series:
    """Days in trailing 63d where 5-day realized vol > 3x its 63-day trailing median.
    Extreme-spike count (complement to existing 2x counts)."""
    v = _realized_vol(close, _TD_WEEK)
    med = _rolling_median(v, _TD_QTR)
    is_spike = (v > 3.0 * med).astype(float)
    return _rolling_sum(is_spike, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_SPIKE_EXTENDED_REGISTRY_001_075 = {
    "vsp_ext_001_atr_5d": {"inputs": ["high", "low", "close"], "func": vsp_ext_001_atr_5d},
    "vsp_ext_002_atr_7d": {"inputs": ["high", "low", "close"], "func": vsp_ext_002_atr_7d},
    "vsp_ext_003_atr_42d": {"inputs": ["high", "low", "close"], "func": vsp_ext_003_atr_42d},
    "vsp_ext_004_atr5_vs_median126": {"inputs": ["high", "low", "close"], "func": vsp_ext_004_atr5_vs_median126},
    "vsp_ext_005_atr21_vs_median126": {"inputs": ["high", "low", "close"], "func": vsp_ext_005_atr21_vs_median126},
    "vsp_ext_006_atr14_zscore_126d": {"inputs": ["high", "low", "close"], "func": vsp_ext_006_atr14_zscore_126d},
    "vsp_ext_007_natr5_vs_median252": {"inputs": ["high", "low", "close"], "func": vsp_ext_007_natr5_vs_median252},
    "vsp_ext_008_atr14_spike_count_252d": {"inputs": ["high", "low", "close"], "func": vsp_ext_008_atr14_spike_count_252d},
    "vsp_ext_009_rs_vol_5d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_009_rs_vol_5d},
    "vsp_ext_010_rs_vol_126d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_010_rs_vol_126d},
    "vsp_ext_011_rs_vol5_vs_median63": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_011_rs_vol5_vs_median63},
    "vsp_ext_012_rs_vol5_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_012_rs_vol5_zscore_252d},
    "vsp_ext_013_rs_vol63_vs_median252": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_013_rs_vol63_vs_median252},
    "vsp_ext_014_rs_vol21_spike_count_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_014_rs_vol21_spike_count_252d},
    "vsp_ext_015_rs_vol21_pct_rank_126d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_015_rs_vol21_pct_rank_126d},
    "vsp_ext_016_rs_vol5_vs_rvol5": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_016_rs_vol5_vs_rvol5},
    "vsp_ext_017_yz_vol_5d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_017_yz_vol_5d},
    "vsp_ext_018_yz_vol_126d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_018_yz_vol_126d},
    "vsp_ext_019_yz_vol5_vs_median63": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_019_yz_vol5_vs_median63},
    "vsp_ext_020_yz_vol5_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_020_yz_vol5_zscore_252d},
    "vsp_ext_021_yz_vol63_vs_median252": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_021_yz_vol63_vs_median252},
    "vsp_ext_022_yz_vol21_spike_count_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_022_yz_vol21_spike_count_252d},
    "vsp_ext_023_yz_vol5_vs_rvol5": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_023_yz_vol5_vs_rvol5},
    "vsp_ext_024_yz_vol21_pct_rank_126d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_024_yz_vol21_pct_rank_126d},
    "vsp_ext_025_gkyz_vol_5d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_025_gkyz_vol_5d},
    "vsp_ext_026_gkyz_vol_21d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_026_gkyz_vol_21d},
    "vsp_ext_027_gkyz_vol5_vs_median63": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_027_gkyz_vol5_vs_median63},
    "vsp_ext_028_gkyz_vol5_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_028_gkyz_vol5_zscore_252d},
    "vsp_ext_029_gkyz_vs_gk_ratio_5d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_029_gkyz_vs_gk_ratio_5d},
    "vsp_ext_030_gkyz_vol21_pct_rank_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_030_gkyz_vol21_pct_rank_252d},
    "vsp_ext_031_bipower_var_21d": {"inputs": ["close"], "func": vsp_ext_031_bipower_var_21d},
    "vsp_ext_032_bipower_var_63d": {"inputs": ["close"], "func": vsp_ext_032_bipower_var_63d},
    "vsp_ext_033_bipower_var21_vs_median252": {"inputs": ["close"], "func": vsp_ext_033_bipower_var21_vs_median252},
    "vsp_ext_034_realized_quarticity_21d": {"inputs": ["close"], "func": vsp_ext_034_realized_quarticity_21d},
    "vsp_ext_035_quarticity21_zscore_252d": {"inputs": ["close"], "func": vsp_ext_035_quarticity21_zscore_252d},
    "vsp_ext_036_quarticity21_pct_rank_252d": {"inputs": ["close"], "func": vsp_ext_036_quarticity21_pct_rank_252d},
    "vsp_ext_037_jump_var_21d": {"inputs": ["close"], "func": vsp_ext_037_jump_var_21d},
    "vsp_ext_038_continuous_var_21d": {"inputs": ["close"], "func": vsp_ext_038_continuous_var_21d},
    "vsp_ext_039_jump_fraction_21d": {"inputs": ["close"], "func": vsp_ext_039_jump_fraction_21d},
    "vsp_ext_040_jump_fraction21_zscore_252d": {"inputs": ["close"], "func": vsp_ext_040_jump_fraction21_zscore_252d},
    "vsp_ext_041_downside_semivar_21d": {"inputs": ["close"], "func": vsp_ext_041_downside_semivar_21d},
    "vsp_ext_042_upside_semivar_21d": {"inputs": ["close"], "func": vsp_ext_042_upside_semivar_21d},
    "vsp_ext_043_semivol_ratio_down_up_21d": {"inputs": ["close"], "func": vsp_ext_043_semivol_ratio_down_up_21d},
    "vsp_ext_044_downside_semivar21_zscore_252d": {"inputs": ["close"], "func": vsp_ext_044_downside_semivar21_zscore_252d},
    "vsp_ext_045_downside_semivar21_pct_rank_252d": {"inputs": ["close"], "func": vsp_ext_045_downside_semivar21_pct_rank_252d},
    "vsp_ext_046_semivol_ratio_zscore_252d": {"inputs": ["close"], "func": vsp_ext_046_semivol_ratio_zscore_252d},
    "vsp_ext_047_overnight_vol_21d": {"inputs": ["open", "close"], "func": vsp_ext_047_overnight_vol_21d},
    "vsp_ext_048_intraday_vol_21d": {"inputs": ["open", "close"], "func": vsp_ext_048_intraday_vol_21d},
    "vsp_ext_049_overnight_vs_intraday_vol_ratio_21d": {"inputs": ["open", "close"], "func": vsp_ext_049_overnight_vs_intraday_vol_ratio_21d},
    "vsp_ext_050_overnight_vol21_zscore_252d": {"inputs": ["open", "close"], "func": vsp_ext_050_overnight_vol21_zscore_252d},
    "vsp_ext_051_overnight_vol21_pct_rank_252d": {"inputs": ["open", "close"], "func": vsp_ext_051_overnight_vol21_pct_rank_252d},
    "vsp_ext_052_overnight_vs_total_vol_fraction_21d": {"inputs": ["open", "close"], "func": vsp_ext_052_overnight_vs_total_vol_fraction_21d},
    "vsp_ext_053_rvol_term_slope_3_21": {"inputs": ["close"], "func": vsp_ext_053_rvol_term_slope_3_21},
    "vsp_ext_054_rvol_term_slope_10_63": {"inputs": ["close"], "func": vsp_ext_054_rvol_term_slope_10_63},
    "vsp_ext_055_rvol_term_slope_21_126": {"inputs": ["close"], "func": vsp_ext_055_rvol_term_slope_21_126},
    "vsp_ext_056_rvol_term_slope_21_126_zscore_252d": {"inputs": ["close"], "func": vsp_ext_056_rvol_term_slope_21_126_zscore_252d},
    "vsp_ext_057_rvol_term_slope_5_63_pct_rank_252d": {"inputs": ["close"], "func": vsp_ext_057_rvol_term_slope_5_63_pct_rank_252d},
    "vsp_ext_058_rvol5_roc_5d": {"inputs": ["close"], "func": vsp_ext_058_rvol5_roc_5d},
    "vsp_ext_059_rvol5_roc_21d": {"inputs": ["close"], "func": vsp_ext_059_rvol5_roc_21d},
    "vsp_ext_060_atr14_roc_5d": {"inputs": ["high", "low", "close"], "func": vsp_ext_060_atr14_roc_5d},
    "vsp_ext_061_yz_vol21_roc_5d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_061_yz_vol21_roc_5d},
    "vsp_ext_062_rvol5_roc_5d_zscore_252d": {"inputs": ["close"], "func": vsp_ext_062_rvol5_roc_5d_zscore_252d},
    "vsp_ext_063_rs_vol21_roc_5d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_063_rs_vol21_roc_5d},
    "vsp_ext_064_yz_vs_rs_spread_21d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_064_yz_vs_rs_spread_21d},
    "vsp_ext_065_gk_vs_rvol_spread_5d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_065_gk_vs_rvol_spread_5d},
    "vsp_ext_066_pk_vs_rvol_spread_5d": {"inputs": ["close", "high", "low"], "func": vsp_ext_066_pk_vs_rvol_spread_5d},
    "vsp_ext_067_cross_estimator_spread_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_067_cross_estimator_spread_zscore_252d},
    "vsp_ext_068_gkyz_vs_yz_spread_5d": {"inputs": ["open", "high", "low", "close"], "func": vsp_ext_068_gkyz_vs_yz_spread_5d},
    "vsp_ext_069_consec_elevated_streak_rvol5": {"inputs": ["close"], "func": vsp_ext_069_consec_elevated_streak_rvol5},
    "vsp_ext_070_consec_elevated_streak_atr14": {"inputs": ["high", "low", "close"], "func": vsp_ext_070_consec_elevated_streak_atr14},
    "vsp_ext_071_consec_spike_streak_rvol5_2x": {"inputs": ["close"], "func": vsp_ext_071_consec_spike_streak_rvol5_2x},
    "vsp_ext_072_max_consec_spike_streak_63d": {"inputs": ["close"], "func": vsp_ext_072_max_consec_spike_streak_63d},
    "vsp_ext_073_days_since_rvol5_spike_2x": {"inputs": ["close"], "func": vsp_ext_073_days_since_rvol5_spike_2x},
    "vsp_ext_074_days_since_atr14_spike_2x": {"inputs": ["high", "low", "close"], "func": vsp_ext_074_days_since_atr14_spike_2x},
    "vsp_ext_075_spike_count_gt3x_median_63d_rvol5": {"inputs": ["close"], "func": vsp_ext_075_spike_count_gt3x_median_63d_rvol5},
}
