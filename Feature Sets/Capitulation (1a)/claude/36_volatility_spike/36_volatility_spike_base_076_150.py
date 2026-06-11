"""
36_volatility_spike — Base Features 076-150
Domain: realized volatility spikes vs trailing baseline — Parkinson estimator;
        Garman-Klass estimator; ATR (Average True Range) spikes vs baseline;
        Rogers-Satchell drift-independent estimator; Yang-Zhang estimator
        (overnight + open-to-close + RS combined); intraday high-low range spikes;
        squared-return spikes; vol term-structure shape; composite spike indices.
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
    """Parkinson high-low range annualized vol estimator."""
    hl2 = (np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS)) ** 2)
    return np.sqrt(_rolling_mean(hl2, w) / (4.0 * np.log(2.0))) * _ANN


def _gk_vol(open: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    """Garman-Klass annualized volatility estimator."""
    hl  = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    co  = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    gk_day = 0.5 * hl ** 2 - (2.0 * np.log(2.0) - 1.0) * co ** 2
    return np.sqrt(_rolling_mean(gk_day, w) * _TD_YEAR)


def _true_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily True Range = max(H-L, |H-prevC|, |L-prevC|)."""
    prev_close = close.shift(1)
    tr1 = high - low
    tr2 = (high - prev_close).abs()
    tr3 = (low  - prev_close).abs()
    return pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Wilder-smoothed Average True Range over w periods."""
    tr = _true_range(high, low, close)
    # Wilder smoothing: EWM with alpha=1/w (equivalent to span=2*w-1)
    return tr.ewm(alpha=1.0 / w, min_periods=max(1, w // 2), adjust=False).mean()


def _rs_day(open: pd.Series, high: pd.Series,
            low: pd.Series, close: pd.Series) -> pd.Series:
    """Daily Rogers-Satchell term: ln(H/C)*ln(H/O) + ln(L/C)*ln(L/O)."""
    lhc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    lho = np.log(high.clip(lower=_EPS) / open.clip(lower=_EPS))
    llc = np.log(low.clip(lower=_EPS)  / close.clip(lower=_EPS))
    llo = np.log(low.clip(lower=_EPS)  / open.clip(lower=_EPS))
    return lhc * lho + llc * llo


def _rs_vol(open: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    """Rogers-Satchell annualized volatility (drift-independent)."""
    rs = _rs_day(open, high, low, close)
    return np.sqrt(_rolling_mean(rs.clip(lower=0.0), w) * _TD_YEAR)


def _yz_vol(open: pd.Series, high: pd.Series, low: pd.Series,
            close: pd.Series, w: int) -> pd.Series:
    """Yang-Zhang annualized volatility estimator.
    Combines overnight vol, open-to-close vol, and Rogers-Satchell term.
    k = 0.34 / (1.34 + (w+1)/(w-1))  — optimal k for YZ estimator.
    """
    if w < 2:
        w = 2
    prev_close = close.shift(1)
    # Overnight return: ln(open/prevclose)
    ln_oc = np.log(open.clip(lower=_EPS) / prev_close.clip(lower=_EPS))
    # Open-to-close return: ln(close/open)
    ln_co = np.log(close.clip(lower=_EPS) / open.clip(lower=_EPS))
    # Overnight variance component
    ov_mean = _rolling_mean(ln_oc, w)
    overnight_var = _rolling_mean((ln_oc - ov_mean) ** 2, w)
    # Open-to-close variance component
    oc_mean = _rolling_mean(ln_co, w)
    oc_var = _rolling_mean((ln_co - oc_mean) ** 2, w)
    # Rogers-Satchell component (daily, no mean subtraction needed — drift-independent)
    rs = _rs_day(open, high, low, close)
    rs_var = _rolling_mean(rs.clip(lower=0.0), w)
    # YZ weighting constant
    k = 0.34 / (1.34 + (w + 1.0) / max(w - 1.0, 1e-9))
    yz_var = (overnight_var + k * oc_var + (1.0 - k) * rs_var).clip(lower=0.0)
    return np.sqrt(yz_var * _TD_YEAR)


def _hl_range_pct(high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily high-low range as fraction of low."""
    return _safe_div(high - low, low)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-090): Parkinson vol spikes (15 features) ---

def vsp_076_pk_vol_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day Parkinson (high-low range) annualized vol."""
    return _parkinson_vol(high, low, _TD_WEEK)


def vsp_077_pk_vol_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day Parkinson annualized vol."""
    return _parkinson_vol(high, low, _TD_MON)


def vsp_078_pk_vol_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day Parkinson annualized vol."""
    return _parkinson_vol(high, low, _TD_QTR)


def vsp_079_pk_vol_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day Parkinson annualized vol."""
    return _parkinson_vol(high, low, _TD_YEAR)


def vsp_080_pk_vol5_vs_median63(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day Parkinson vol to its 63-day trailing median."""
    v = vsp_076_pk_vol_5d(high, low)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_081_pk_vol5_vs_median252(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day Parkinson vol to its 252-day trailing median."""
    v = vsp_076_pk_vol_5d(high, low)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_082_pk_vol5_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 5-day Parkinson vol over trailing 252 days."""
    v = vsp_076_pk_vol_5d(high, low)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_083_pk_vol21_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day Parkinson vol over trailing 252 days."""
    v = vsp_077_pk_vol_21d(high, low)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_084_pk_vol5_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 5-day Parkinson vol within trailing 252-day series."""
    v = vsp_076_pk_vol_5d(high, low)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_085_pk_vol5_vs_rvol5(close: pd.Series, high: pd.Series,
                              low: pd.Series) -> pd.Series:
    """Ratio of 5-day Parkinson vol to 5-day close-to-close realized vol."""
    return _safe_div(
        _parkinson_vol(high, low, _TD_WEEK),
        _realized_vol(close, _TD_WEEK)
    )


def vsp_086_pk_vol21_vs_rvol21(close: pd.Series, high: pd.Series,
                                low: pd.Series) -> pd.Series:
    """Ratio of 21-day Parkinson vol to 21-day close-to-close realized vol."""
    return _safe_div(
        _parkinson_vol(high, low, _TD_MON),
        _realized_vol(close, _TD_MON)
    )


def vsp_087_pk_vol5_max_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum 5-day Parkinson vol seen in trailing 63 days."""
    return _rolling_max(vsp_076_pk_vol_5d(high, low), _TD_QTR)


def vsp_088_pk_vol5_max_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum 5-day Parkinson vol seen in trailing 252 days."""
    return _rolling_max(vsp_076_pk_vol_5d(high, low), _TD_YEAR)


def vsp_089_pk_vol_spike_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in trailing 63d where 5-day Parkinson vol > 2x its 63d median."""
    v = vsp_076_pk_vol_5d(high, low)
    is_spike = (v > 2.0 * _rolling_median(v, _TD_QTR)).astype(float)
    return _rolling_sum(is_spike, _TD_QTR)


def vsp_090_pk_vol_spike_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in trailing 252d where 5-day Parkinson vol > 2x its 63d median."""
    v = vsp_076_pk_vol_5d(high, low)
    is_spike = (v > 2.0 * _rolling_median(v, _TD_QTR)).astype(float)
    return _rolling_sum(is_spike, _TD_YEAR)


# --- Group I (091-100): Garman-Klass vol spikes (10 features) ---

def vsp_091_gk_vol_5d(open: pd.Series, high: pd.Series,
                       low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day Garman-Klass annualized vol."""
    return _gk_vol(open, high, low, close, _TD_WEEK)


def vsp_092_gk_vol_21d(open: pd.Series, high: pd.Series,
                        low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Garman-Klass annualized vol."""
    return _gk_vol(open, high, low, close, _TD_MON)


def vsp_093_gk_vol_63d(open: pd.Series, high: pd.Series,
                        low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day Garman-Klass annualized vol."""
    return _gk_vol(open, high, low, close, _TD_QTR)


def vsp_094_gk_vol5_vs_median63(open: pd.Series, high: pd.Series,
                                  low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day GK vol to its 63-day trailing median."""
    v = vsp_091_gk_vol_5d(open, high, low, close)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_095_gk_vol5_vs_median252(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day GK vol to its 252-day trailing median."""
    v = vsp_091_gk_vol_5d(open, high, low, close)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_096_gk_vol5_zscore_252d(open: pd.Series, high: pd.Series,
                                  low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 5-day GK vol over trailing 252 days."""
    v = vsp_091_gk_vol_5d(open, high, low, close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_097_gk_vol21_zscore_252d(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21-day GK vol over trailing 252 days."""
    v = vsp_092_gk_vol_21d(open, high, low, close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_098_gk_vol5_pct_rank_252d(open: pd.Series, high: pd.Series,
                                    low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day GK vol within trailing 252-day series."""
    v = vsp_091_gk_vol_5d(open, high, low, close)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_099_gk_spike_count_63d(open: pd.Series, high: pd.Series,
                                 low: pd.Series, close: pd.Series) -> pd.Series:
    """Days in trailing 63d where 5-day GK vol > 2x its 63d trailing median."""
    v = vsp_091_gk_vol_5d(open, high, low, close)
    is_spike = (v > 2.0 * _rolling_median(v, _TD_QTR)).astype(float)
    return _rolling_sum(is_spike, _TD_QTR)


def vsp_100_gk_vs_pk_ratio_5d(open: pd.Series, high: pd.Series,
                                low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 5-day GK vol to 5-day Parkinson vol (open-close contribution)."""
    return _safe_div(
        _gk_vol(open, high, low, close, _TD_WEEK),
        _parkinson_vol(high, low, _TD_WEEK)
    )


# --- Group J (101-112): ATR (Average True Range) features (12 features) ---

def vsp_101_atr_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """14-day Wilder-smoothed ATR (standard period)."""
    return _atr(high, low, close, 14)


def vsp_102_atr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Wilder-smoothed ATR (monthly period)."""
    return _atr(high, low, close, _TD_MON)


def vsp_103_atr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day Wilder-smoothed ATR (quarterly period)."""
    return _atr(high, low, close, _TD_QTR)


def vsp_104_natr_14d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Normalized ATR (14d): ATR divided by closing price — scale-free."""
    return _safe_div(_atr(high, low, close, 14), close.clip(lower=_EPS))


def vsp_105_natr_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Normalized ATR (21d): ATR divided by closing price."""
    return _safe_div(_atr(high, low, close, _TD_MON), close.clip(lower=_EPS))


def vsp_106_natr_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Normalized ATR (63d): ATR divided by closing price."""
    return _safe_div(_atr(high, low, close, _TD_QTR), close.clip(lower=_EPS))


def vsp_107_atr14_vs_median63(high: pd.Series, low: pd.Series,
                               close: pd.Series) -> pd.Series:
    """14-day ATR divided by its 63-day trailing median (ATR spike ratio)."""
    v = _atr(high, low, close, 14)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_108_atr14_vs_median252(high: pd.Series, low: pd.Series,
                                close: pd.Series) -> pd.Series:
    """14-day ATR divided by its 252-day trailing median."""
    v = _atr(high, low, close, 14)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_109_atr14_zscore_63d(high: pd.Series, low: pd.Series,
                              close: pd.Series) -> pd.Series:
    """Z-score of 14-day ATR relative to its 63-day rolling distribution."""
    v = _atr(high, low, close, 14)
    m = _rolling_mean(v, _TD_QTR)
    s = _rolling_std(v, _TD_QTR)
    return _safe_div(v - m, s)


def vsp_110_atr14_zscore_252d(high: pd.Series, low: pd.Series,
                               close: pd.Series) -> pd.Series:
    """Z-score of 14-day ATR relative to its 252-day rolling distribution."""
    v = _atr(high, low, close, 14)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_111_atr14_pct_rank_252d(high: pd.Series, low: pd.Series,
                                 close: pd.Series) -> pd.Series:
    """Percentile rank of 14-day ATR within trailing 252-day series."""
    v = _atr(high, low, close, 14)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_112_atr14_spike_count_63d(high: pd.Series, low: pd.Series,
                                   close: pd.Series) -> pd.Series:
    """Days in trailing 63d where 14-day ATR > 2x its 63-day trailing median."""
    v = _atr(high, low, close, 14)
    is_spike = (v > 2.0 * _rolling_median(v, _TD_QTR)).astype(float)
    return _rolling_sum(is_spike, _TD_QTR)


# --- Group K (113-120): Rogers-Satchell estimator (8 features) ---

def vsp_113_rs_vol_21d(open: pd.Series, high: pd.Series,
                        low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Rogers-Satchell annualized vol (drift-independent)."""
    return _rs_vol(open, high, low, close, _TD_MON)


def vsp_114_rs_vol_63d(open: pd.Series, high: pd.Series,
                        low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day Rogers-Satchell annualized vol (drift-independent)."""
    return _rs_vol(open, high, low, close, _TD_QTR)


def vsp_115_rs_vol21_vs_median63(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day RS vol divided by its 63-day trailing median (RS spike ratio)."""
    v = vsp_113_rs_vol_21d(open, high, low, close)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_116_rs_vol21_vs_median252(open: pd.Series, high: pd.Series,
                                    low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day RS vol divided by its 252-day trailing median."""
    v = vsp_113_rs_vol_21d(open, high, low, close)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_117_rs_vol21_zscore_252d(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21-day RS vol over trailing 252-day distribution."""
    v = vsp_113_rs_vol_21d(open, high, low, close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_118_rs_vol63_zscore_252d(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 63-day RS vol over trailing 252-day distribution."""
    v = vsp_114_rs_vol_63d(open, high, low, close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_119_rs_vol21_pct_rank_252d(open: pd.Series, high: pd.Series,
                                     low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day RS vol within trailing 252-day series."""
    v = vsp_113_rs_vol_21d(open, high, low, close)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_120_rs_vs_rvol_ratio_21d(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day RS vol to 21-day close-to-close realized vol."""
    return _safe_div(
        _rs_vol(open, high, low, close, _TD_MON),
        _realized_vol(close, _TD_MON)
    )


# --- Group L (121-128): Yang-Zhang estimator (8 features) ---

def vsp_121_yz_vol_21d(open: pd.Series, high: pd.Series,
                        low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Yang-Zhang annualized vol (overnight + open-to-close + RS)."""
    return _yz_vol(open, high, low, close, _TD_MON)


def vsp_122_yz_vol_63d(open: pd.Series, high: pd.Series,
                        low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day Yang-Zhang annualized vol."""
    return _yz_vol(open, high, low, close, _TD_QTR)


def vsp_123_yz_vol21_vs_median63(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day YZ vol divided by its 63-day trailing median (YZ spike ratio)."""
    v = vsp_121_yz_vol_21d(open, high, low, close)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_124_yz_vol21_vs_median252(open: pd.Series, high: pd.Series,
                                    low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day YZ vol divided by its 252-day trailing median."""
    v = vsp_121_yz_vol_21d(open, high, low, close)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_125_yz_vol21_zscore_252d(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21-day YZ vol over trailing 252-day distribution."""
    v = vsp_121_yz_vol_21d(open, high, low, close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_126_yz_vol63_zscore_252d(open: pd.Series, high: pd.Series,
                                   low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 63-day YZ vol over trailing 252-day distribution."""
    v = vsp_122_yz_vol_63d(open, high, low, close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_127_yz_vol21_pct_rank_252d(open: pd.Series, high: pd.Series,
                                     low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day YZ vol within trailing 252-day series."""
    v = vsp_121_yz_vol_21d(open, high, low, close)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_128_yz_vs_gk_ratio_21d(open: pd.Series, high: pd.Series,
                                 low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21-day YZ vol to 21-day GK vol (overnight jump contribution)."""
    return _safe_div(
        _yz_vol(open, high, low, close, _TD_MON),
        _gk_vol(open, high, low, close, _TD_MON)
    )


# --- Group M (129-134): Intraday HL range spikes (6 features) ---

def vsp_129_hl_range_pct_5d_mean(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day mean of daily high-low range as pct of low."""
    return _rolling_mean(_hl_range_pct(high, low), _TD_WEEK)


def vsp_130_hl_range_vs_median63(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day mean HL range divided by its 63-day trailing median."""
    v = vsp_129_hl_range_pct_5d_mean(high, low)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


def vsp_131_hl_range_vs_median252(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day mean HL range divided by its 252-day trailing median."""
    v = vsp_129_hl_range_pct_5d_mean(high, low)
    return _safe_div(v, _rolling_median(v, _TD_YEAR))


def vsp_132_hl_range_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 5-day mean HL range over trailing 252 days."""
    v = vsp_129_hl_range_pct_5d_mean(high, low)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_133_hl_range_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 5-day HL range within trailing 252-day series."""
    v = vsp_129_hl_range_pct_5d_mean(high, low)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_134_hl_spike_count_gt2x_median_63d(high: pd.Series,
                                             low: pd.Series) -> pd.Series:
    """Days in trailing 63d where daily HL range > 2x its 63d trailing median."""
    r = _hl_range_pct(high, low)
    is_spike = (r > 2.0 * _rolling_median(r, _TD_QTR)).astype(float)
    return _rolling_sum(is_spike, _TD_QTR)


# --- Group N (135-140): Squared-return spike features (6 features) ---

def vsp_135_sq_ret_5d_mean(close: pd.Series) -> pd.Series:
    """5-day rolling mean of squared daily log-returns (realized variance proxy)."""
    lr2 = _log_ret(close) ** 2
    return _rolling_mean(lr2, _TD_WEEK)


def vsp_136_sq_ret5_vs_sq_ret63(close: pd.Series) -> pd.Series:
    """Ratio of 5-day mean squared-return to 63-day mean squared-return."""
    lr2 = _log_ret(close) ** 2
    return _safe_div(_rolling_mean(lr2, _TD_WEEK), _rolling_mean(lr2, _TD_QTR))


def vsp_137_sq_ret5_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day mean squared-return over 252-day distribution."""
    v = vsp_135_sq_ret_5d_mean(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_138_sq_ret5_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day mean squared-return within trailing 252 days."""
    v = vsp_135_sq_ret_5d_mean(close)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_139_abs_ret_5d_mean(close: pd.Series) -> pd.Series:
    """5-day rolling mean of absolute daily log-returns."""
    return _rolling_mean(_log_ret(close).abs(), _TD_WEEK)


def vsp_140_abs_ret5_vs_median_63d(close: pd.Series) -> pd.Series:
    """5-day mean absolute return divided by its 63-day trailing median."""
    v = vsp_139_abs_ret_5d_mean(close)
    return _safe_div(v, _rolling_median(v, _TD_QTR))


# --- Group O (141-146): Vol term-structure shape (6 features) ---

def vsp_141_rvol_term_slope_5_63(close: pd.Series) -> pd.Series:
    """Difference of 5-day vol minus 63-day vol (term-structure steepness)."""
    return _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_QTR)


def vsp_142_rvol_term_slope_5_252(close: pd.Series) -> pd.Series:
    """Difference of 5-day vol minus 252-day vol."""
    return _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_YEAR)


def vsp_143_rvol_term_slope_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-63 vol term slope over trailing 252-day distribution."""
    v = vsp_141_rvol_term_slope_5_63(close)
    m = _rolling_mean(v, _TD_YEAR)
    s = _rolling_std(v, _TD_YEAR)
    return _safe_div(v - m, s)


def vsp_144_rvol_contango_flag(close: pd.Series) -> pd.Series:
    """Flag: 5-day vol < 63-day vol (short-term calmer than long-term, contango-like)."""
    return (_realized_vol(close, _TD_WEEK) < _realized_vol(close, _TD_QTR)).astype(float)


def vsp_145_rvol_backwardation_flag(close: pd.Series) -> pd.Series:
    """Flag: 5-day vol > 252-day vol by more than 50% (extreme backwardation)."""
    r5 = _realized_vol(close, _TD_WEEK)
    r252 = _realized_vol(close, _TD_YEAR)
    return (r5 > 1.5 * r252).astype(float)


def vsp_146_rvol5_21_63_composite_ratio(close: pd.Series) -> pd.Series:
    """Mean of 5/21, 5/63, 21/63 vol ratios (composite short-term vs long-term)."""
    r5  = _realized_vol(close, _TD_WEEK)
    r21 = _realized_vol(close, _TD_MON)
    r63 = _realized_vol(close, _TD_QTR)
    a = _safe_div(r5, r21)
    b = _safe_div(r5, r63)
    c = _safe_div(r21, r63)
    return (a + b + c) / 3.0


# --- Group P (147-150): Multi-estimator composite spike indices (4 features) ---

def vsp_147_composite_vol_spike_index(close: pd.Series, high: pd.Series,
                                       low: pd.Series) -> pd.Series:
    """Mean z-score of 5d close-vol, 5d Parkinson vol, 5d HL range (vs 252d)."""
    rv5 = _realized_vol(close, _TD_WEEK)
    pk5 = _parkinson_vol(high, low, _TD_WEEK)
    hl5 = _rolling_mean(_hl_range_pct(high, low), _TD_WEEK)
    def zs(v):
        m = _rolling_mean(v, _TD_YEAR)
        s = _rolling_std(v, _TD_YEAR)
        return _safe_div(v - m, s)
    return (zs(rv5) + zs(pk5) + zs(hl5)) / 3.0


def vsp_148_composite_spike_pct_rank_252d(close: pd.Series, high: pd.Series,
                                           low: pd.Series) -> pd.Series:
    """Percentile rank of composite spike index within trailing 252 days."""
    v = vsp_147_composite_vol_spike_index(close, high, low)
    return v.rolling(_TD_YEAR, min_periods=_TD_HALF).rank(pct=True)


def vsp_149_five_estimator_composite(close: pd.Series, high: pd.Series,
                                      low: pd.Series, open: pd.Series) -> pd.Series:
    """Mean z-score across 5 estimators: rvol5, pk5, gk5, rs21, yz21 (vs 252d)."""
    rv5 = _realized_vol(close, _TD_WEEK)
    pk5 = _parkinson_vol(high, low, _TD_WEEK)
    gk5 = _gk_vol(open, high, low, close, _TD_WEEK)
    rs21 = _rs_vol(open, high, low, close, _TD_MON)
    yz21 = _yz_vol(open, high, low, close, _TD_MON)
    def zs(v):
        m = _rolling_mean(v, _TD_YEAR)
        s = _rolling_std(v, _TD_YEAR)
        return _safe_div(v - m, s)
    return (zs(rv5) + zs(pk5) + zs(gk5) + zs(rs21) + zs(yz21)) / 5.0


def vsp_150_vol_spike_persistence_score(close: pd.Series) -> pd.Series:
    """Ratio of 21-day count of spike-days to 63-day count (recency weighting)."""
    v = _realized_vol(close, _TD_WEEK)
    is_spike = (v > 2.0 * _rolling_median(v, _TD_QTR)).astype(float)
    c21 = _rolling_sum(is_spike, _TD_MON).clip(lower=0)
    c63 = _rolling_sum(is_spike, _TD_QTR).clip(lower=_EPS)
    return _safe_div(c21, c63)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_SPIKE_REGISTRY_076_150 = {
    "vsp_076_pk_vol_5d": {"inputs": ["high", "low"], "func": vsp_076_pk_vol_5d},
    "vsp_077_pk_vol_21d": {"inputs": ["high", "low"], "func": vsp_077_pk_vol_21d},
    "vsp_078_pk_vol_63d": {"inputs": ["high", "low"], "func": vsp_078_pk_vol_63d},
    "vsp_079_pk_vol_252d": {"inputs": ["high", "low"], "func": vsp_079_pk_vol_252d},
    "vsp_080_pk_vol5_vs_median63": {"inputs": ["high", "low"], "func": vsp_080_pk_vol5_vs_median63},
    "vsp_081_pk_vol5_vs_median252": {"inputs": ["high", "low"], "func": vsp_081_pk_vol5_vs_median252},
    "vsp_082_pk_vol5_zscore_252d": {"inputs": ["high", "low"], "func": vsp_082_pk_vol5_zscore_252d},
    "vsp_083_pk_vol21_zscore_252d": {"inputs": ["high", "low"], "func": vsp_083_pk_vol21_zscore_252d},
    "vsp_084_pk_vol5_pct_rank_252d": {"inputs": ["high", "low"], "func": vsp_084_pk_vol5_pct_rank_252d},
    "vsp_085_pk_vol5_vs_rvol5": {"inputs": ["close", "high", "low"], "func": vsp_085_pk_vol5_vs_rvol5},
    "vsp_086_pk_vol21_vs_rvol21": {"inputs": ["close", "high", "low"], "func": vsp_086_pk_vol21_vs_rvol21},
    "vsp_087_pk_vol5_max_63d": {"inputs": ["high", "low"], "func": vsp_087_pk_vol5_max_63d},
    "vsp_088_pk_vol5_max_252d": {"inputs": ["high", "low"], "func": vsp_088_pk_vol5_max_252d},
    "vsp_089_pk_vol_spike_count_63d": {"inputs": ["high", "low"], "func": vsp_089_pk_vol_spike_count_63d},
    "vsp_090_pk_vol_spike_count_252d": {"inputs": ["high", "low"], "func": vsp_090_pk_vol_spike_count_252d},
    "vsp_091_gk_vol_5d": {"inputs": ["open", "high", "low", "close"], "func": vsp_091_gk_vol_5d},
    "vsp_092_gk_vol_21d": {"inputs": ["open", "high", "low", "close"], "func": vsp_092_gk_vol_21d},
    "vsp_093_gk_vol_63d": {"inputs": ["open", "high", "low", "close"], "func": vsp_093_gk_vol_63d},
    "vsp_094_gk_vol5_vs_median63": {"inputs": ["open", "high", "low", "close"], "func": vsp_094_gk_vol5_vs_median63},
    "vsp_095_gk_vol5_vs_median252": {"inputs": ["open", "high", "low", "close"], "func": vsp_095_gk_vol5_vs_median252},
    "vsp_096_gk_vol5_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_096_gk_vol5_zscore_252d},
    "vsp_097_gk_vol21_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_097_gk_vol21_zscore_252d},
    "vsp_098_gk_vol5_pct_rank_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_098_gk_vol5_pct_rank_252d},
    "vsp_099_gk_spike_count_63d": {"inputs": ["open", "high", "low", "close"], "func": vsp_099_gk_spike_count_63d},
    "vsp_100_gk_vs_pk_ratio_5d": {"inputs": ["open", "high", "low", "close"], "func": vsp_100_gk_vs_pk_ratio_5d},
    "vsp_101_atr_14d": {"inputs": ["high", "low", "close"], "func": vsp_101_atr_14d},
    "vsp_102_atr_21d": {"inputs": ["high", "low", "close"], "func": vsp_102_atr_21d},
    "vsp_103_atr_63d": {"inputs": ["high", "low", "close"], "func": vsp_103_atr_63d},
    "vsp_104_natr_14d": {"inputs": ["high", "low", "close"], "func": vsp_104_natr_14d},
    "vsp_105_natr_21d": {"inputs": ["high", "low", "close"], "func": vsp_105_natr_21d},
    "vsp_106_natr_63d": {"inputs": ["high", "low", "close"], "func": vsp_106_natr_63d},
    "vsp_107_atr14_vs_median63": {"inputs": ["high", "low", "close"], "func": vsp_107_atr14_vs_median63},
    "vsp_108_atr14_vs_median252": {"inputs": ["high", "low", "close"], "func": vsp_108_atr14_vs_median252},
    "vsp_109_atr14_zscore_63d": {"inputs": ["high", "low", "close"], "func": vsp_109_atr14_zscore_63d},
    "vsp_110_atr14_zscore_252d": {"inputs": ["high", "low", "close"], "func": vsp_110_atr14_zscore_252d},
    "vsp_111_atr14_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": vsp_111_atr14_pct_rank_252d},
    "vsp_112_atr14_spike_count_63d": {"inputs": ["high", "low", "close"], "func": vsp_112_atr14_spike_count_63d},
    "vsp_113_rs_vol_21d": {"inputs": ["open", "high", "low", "close"], "func": vsp_113_rs_vol_21d},
    "vsp_114_rs_vol_63d": {"inputs": ["open", "high", "low", "close"], "func": vsp_114_rs_vol_63d},
    "vsp_115_rs_vol21_vs_median63": {"inputs": ["open", "high", "low", "close"], "func": vsp_115_rs_vol21_vs_median63},
    "vsp_116_rs_vol21_vs_median252": {"inputs": ["open", "high", "low", "close"], "func": vsp_116_rs_vol21_vs_median252},
    "vsp_117_rs_vol21_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_117_rs_vol21_zscore_252d},
    "vsp_118_rs_vol63_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_118_rs_vol63_zscore_252d},
    "vsp_119_rs_vol21_pct_rank_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_119_rs_vol21_pct_rank_252d},
    "vsp_120_rs_vs_rvol_ratio_21d": {"inputs": ["open", "high", "low", "close"], "func": vsp_120_rs_vs_rvol_ratio_21d},
    "vsp_121_yz_vol_21d": {"inputs": ["open", "high", "low", "close"], "func": vsp_121_yz_vol_21d},
    "vsp_122_yz_vol_63d": {"inputs": ["open", "high", "low", "close"], "func": vsp_122_yz_vol_63d},
    "vsp_123_yz_vol21_vs_median63": {"inputs": ["open", "high", "low", "close"], "func": vsp_123_yz_vol21_vs_median63},
    "vsp_124_yz_vol21_vs_median252": {"inputs": ["open", "high", "low", "close"], "func": vsp_124_yz_vol21_vs_median252},
    "vsp_125_yz_vol21_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_125_yz_vol21_zscore_252d},
    "vsp_126_yz_vol63_zscore_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_126_yz_vol63_zscore_252d},
    "vsp_127_yz_vol21_pct_rank_252d": {"inputs": ["open", "high", "low", "close"], "func": vsp_127_yz_vol21_pct_rank_252d},
    "vsp_128_yz_vs_gk_ratio_21d": {"inputs": ["open", "high", "low", "close"], "func": vsp_128_yz_vs_gk_ratio_21d},
    "vsp_129_hl_range_pct_5d_mean": {"inputs": ["high", "low"], "func": vsp_129_hl_range_pct_5d_mean},
    "vsp_130_hl_range_vs_median63": {"inputs": ["high", "low"], "func": vsp_130_hl_range_vs_median63},
    "vsp_131_hl_range_vs_median252": {"inputs": ["high", "low"], "func": vsp_131_hl_range_vs_median252},
    "vsp_132_hl_range_zscore_252d": {"inputs": ["high", "low"], "func": vsp_132_hl_range_zscore_252d},
    "vsp_133_hl_range_pct_rank_252d": {"inputs": ["high", "low"], "func": vsp_133_hl_range_pct_rank_252d},
    "vsp_134_hl_spike_count_gt2x_median_63d": {"inputs": ["high", "low"], "func": vsp_134_hl_spike_count_gt2x_median_63d},
    "vsp_135_sq_ret_5d_mean": {"inputs": ["close"], "func": vsp_135_sq_ret_5d_mean},
    "vsp_136_sq_ret5_vs_sq_ret63": {"inputs": ["close"], "func": vsp_136_sq_ret5_vs_sq_ret63},
    "vsp_137_sq_ret5_zscore_252d": {"inputs": ["close"], "func": vsp_137_sq_ret5_zscore_252d},
    "vsp_138_sq_ret5_pct_rank_252d": {"inputs": ["close"], "func": vsp_138_sq_ret5_pct_rank_252d},
    "vsp_139_abs_ret_5d_mean": {"inputs": ["close"], "func": vsp_139_abs_ret_5d_mean},
    "vsp_140_abs_ret5_vs_median_63d": {"inputs": ["close"], "func": vsp_140_abs_ret5_vs_median_63d},
    "vsp_141_rvol_term_slope_5_63": {"inputs": ["close"], "func": vsp_141_rvol_term_slope_5_63},
    "vsp_142_rvol_term_slope_5_252": {"inputs": ["close"], "func": vsp_142_rvol_term_slope_5_252},
    "vsp_143_rvol_term_slope_zscore_252d": {"inputs": ["close"], "func": vsp_143_rvol_term_slope_zscore_252d},
    "vsp_144_rvol_contango_flag": {"inputs": ["close"], "func": vsp_144_rvol_contango_flag},
    "vsp_145_rvol_backwardation_flag": {"inputs": ["close"], "func": vsp_145_rvol_backwardation_flag},
    "vsp_146_rvol5_21_63_composite_ratio": {"inputs": ["close"], "func": vsp_146_rvol5_21_63_composite_ratio},
    "vsp_147_composite_vol_spike_index": {"inputs": ["close", "high", "low"], "func": vsp_147_composite_vol_spike_index},
    "vsp_148_composite_spike_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": vsp_148_composite_spike_pct_rank_252d},
    "vsp_149_five_estimator_composite": {"inputs": ["close", "high", "low", "open"], "func": vsp_149_five_estimator_composite},
    "vsp_150_vol_spike_persistence_score": {"inputs": ["close"], "func": vsp_150_vol_spike_persistence_score},
}
