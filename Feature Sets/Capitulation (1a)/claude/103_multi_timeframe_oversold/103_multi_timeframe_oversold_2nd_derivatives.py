"""
103_multi_timeframe_oversold — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base multi-timeframe-oversold features — captures the
        speed at which oversold confluence across horizons is building.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
All features are backward-looking only; no forward information.
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
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _rsi(close: pd.Series, w: int) -> pd.Series:
    delta = close.diff(1)
    up = delta.clip(lower=0)
    down = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / w, min_periods=max(2, w // 2)).mean()
    ad = down.ewm(alpha=1.0 / w, min_periods=max(2, w // 2)).mean()
    rs = _safe_div(au, ad)
    return 100.0 - _safe_div(100.0, 1.0 + rs)


def _stoch_k(close: pd.Series, w: int) -> pd.Series:
    lo = _rolling_min(close, w)
    hi = _rolling_max(close, w)
    return 100.0 * _safe_div(close - lo, hi - lo)


def _williams_r(close: pd.Series, w: int) -> pd.Series:
    lo = _rolling_min(close, w)
    hi = _rolling_max(close, w)
    return -100.0 * _safe_div(hi - close, hi - lo)


def _drawdown(close: pd.Series, w: int) -> pd.Series:
    h = _rolling_max(close, w)
    return _safe_div(close - h, h)


def _pct_b(close: pd.Series, w: int) -> pd.Series:
    ma = _rolling_mean(close, w)
    sd = _rolling_std(close, w)
    return _safe_div(close - (ma - 2.0 * sd), 4.0 * sd)


_RSI_TF = (7, 14, 21, 63)
_RSI_EXT_TF = (7, 14, 21, 42, 63, 126, 252)
_MA_TF = (10, 21, 50, 100, 200)
_DD_TF = (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR, 504)
_DD_EXT_TF = (_TD_MON, 42, _TD_QTR, _TD_HALF, _TD_YEAR, 504, 756)
_PCTILE_TF = (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)
_MOM_TF = (_TD_WEEK, _TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)
_CHAN_TF = (14, _TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def mto_drv2_001_rsi_min_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the cross-horizon minimum RSI."""
    mn = pd.concat([_rsi(close, w) for w in _RSI_TF], axis=1).min(axis=1)
    return mn.diff(5)


def mto_drv2_002_rsi_oversold_count_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the RSI oversold-horizon count."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    return cnt.diff(5)


def mto_drv2_003_below_ma_count_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the below-moving-average count."""
    cnt = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    return cnt.diff(5)


def mto_drv2_004_dd_min_across_tf_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the deepest drawdown across horizons."""
    mn = pd.concat([_drawdown(close, w) for w in _DD_TF], axis=1).min(axis=1)
    return mn.diff(5)


def mto_drv2_005_dd_extreme_count_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the count of horizons with drawdown worse than -20%."""
    cnt = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    return cnt.diff(5)


def mto_drv2_006_new_low_count_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the multi-horizon new-low count."""
    cnt = sum((close <= _rolling_min(close, w)).astype(float) for w in _DD_TF)
    return cnt.diff(5)


def mto_drv2_007_price_pctile_min_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the lowest close percentile rank across horizons."""
    mn = pd.concat([_rolling_rank_pct(close, w) for w in _PCTILE_TF], axis=1).min(axis=1)
    return mn.diff(5)


def mto_drv2_008_stoch_min_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the minimum stochastic %K across channel horizons."""
    mn = pd.concat([_stoch_k(close, w) for w in _CHAN_TF], axis=1).min(axis=1)
    return mn.diff(5)


def mto_drv2_009_oversold_breadth_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the oversold breadth index."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    ma_c = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    pc_c = sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF)
    total = len(_RSI_TF) + len(_MA_TF) + len(_DD_TF) + len(_PCTILE_TF)
    return ((rsi_c + ma_c + dd_c + pc_c) / total).diff(5)


def mto_drv2_010_master_count_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the master oversold-signal count."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    return (rsi_c + dd_c).diff(5)


def mto_drv2_011_momentum_oversold_count_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the count of trailing-return horizons worse than -15%."""
    cnt = sum((close.pct_change(w) < -0.15).astype(float) for w in _MOM_TF)
    return cnt.diff(5)


def mto_drv2_012_rsi_14d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 14-day RSI."""
    return _rsi(close, 14).diff(5)


def mto_drv2_013_rsi_consensus_extremity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the RSI consensus extremity (mean oversold depth)."""
    depth = sum((40.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_EXT_TF)
    return (depth / len(_RSI_EXT_TF)).diff(5)


def mto_drv2_014_pctb_min_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the minimum Bollinger %B across horizons."""
    mn = pd.concat([_pct_b(close, w) for w in _PCTILE_TF], axis=1).min(axis=1)
    return mn.diff(5)


def mto_drv2_015_dd_confluence_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the drawdown confluence score."""
    score = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF) / len(_DD_TF)
    return score.diff(5)


def mto_drv2_016_oversold_alignment_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the cross-family oversold alignment score."""
    rsi_f = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF) / len(_RSI_TF)
    ma_f = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF) / len(_MA_TF)
    pc_f = sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF) / len(_PCTILE_TF)
    return (rsi_f * ma_f * pc_f).diff(5)


def mto_drv2_017_negative_momentum_confluence_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the negative-momentum confluence fraction."""
    frac = sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF) / len(_MOM_TF)
    return frac.diff(5)


def mto_drv2_018_capitulation_confluence_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the capitulation confluence count."""
    rsi_c = sum((_rsi(close, w) < 25).astype(float) for w in _RSI_EXT_TF)
    dd_c = sum((_drawdown(close, w) < -0.30).astype(float) for w in _DD_EXT_TF)
    return (rsi_c + dd_c).diff(5)


def mto_drv2_019_ma_cascade_alignment_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the moving-average cascade alignment fraction."""
    cnt = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    return (cnt / len(_MA_TF)).diff(5)


def mto_drv2_020_williams_min_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the minimum Williams %R across channel horizons."""
    mn = pd.concat([_williams_r(close, w) for w in _CHAN_TF], axis=1).min(axis=1)
    return mn.diff(5)


def mto_drv2_021_rsi_min_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the cross-horizon minimum RSI (monthly pace)."""
    mn = pd.concat([_rsi(close, w) for w in _RSI_TF], axis=1).min(axis=1)
    return mn.diff(_TD_MON)


def mto_drv2_022_capitulation_index_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the multi-timeframe capitulation index."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    ma_c = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    pc_c = sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF)
    total = len(_RSI_TF) + len(_MA_TF) + len(_DD_TF) + len(_PCTILE_TF)
    breadth = (rsi_c + ma_c + dd_c + pc_c) / total
    depth = sum((30.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_TF) / (len(_RSI_TF) * 30.0)
    return (breadth * (0.5 + depth)).diff(5)


def mto_drv2_023_dd_mean_across_tf_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the mean drawdown across horizons."""
    mean_dd = pd.concat([_drawdown(close, w) for w in _DD_TF], axis=1).mean(axis=1)
    return mean_dd.diff(5)


def mto_drv2_024_oversold_family_count_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the count of majority-oversold indicator families."""
    rsi_f = (sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF) / 4 > 0.5).astype(float)
    ma_f = (sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF) / 5 > 0.5).astype(float)
    dd_f = (sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF) / 5 > 0.5).astype(float)
    mo_f = (sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF) / 5 > 0.5).astype(float)
    return (rsi_f + ma_f + dd_f + mo_f).diff(5)


def mto_drv2_025_master_index_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the master multi-timeframe capitulation index."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_EXT_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_EXT_TF)
    mo_c = sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF)
    total = len(_RSI_EXT_TF) + len(_DD_EXT_TF) + len(_MOM_TF)
    breadth = (rsi_c + dd_c + mo_c) / total
    depth = sum((30.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_EXT_TF) / (len(_RSI_EXT_TF) * 30.0)
    return (breadth * (0.5 + depth)).diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

MULTI_TIMEFRAME_OVERSOLD_REGISTRY_2ND_DERIVATIVES = {
    "mto_drv2_001_rsi_min_5d_diff": {"inputs": ["close"], "func": mto_drv2_001_rsi_min_5d_diff},
    "mto_drv2_002_rsi_oversold_count_5d_diff": {"inputs": ["close"], "func": mto_drv2_002_rsi_oversold_count_5d_diff},
    "mto_drv2_003_below_ma_count_5d_diff": {"inputs": ["close"], "func": mto_drv2_003_below_ma_count_5d_diff},
    "mto_drv2_004_dd_min_across_tf_5d_diff": {"inputs": ["close"], "func": mto_drv2_004_dd_min_across_tf_5d_diff},
    "mto_drv2_005_dd_extreme_count_5d_diff": {"inputs": ["close"], "func": mto_drv2_005_dd_extreme_count_5d_diff},
    "mto_drv2_006_new_low_count_5d_diff": {"inputs": ["close"], "func": mto_drv2_006_new_low_count_5d_diff},
    "mto_drv2_007_price_pctile_min_5d_diff": {"inputs": ["close"], "func": mto_drv2_007_price_pctile_min_5d_diff},
    "mto_drv2_008_stoch_min_5d_diff": {"inputs": ["close"], "func": mto_drv2_008_stoch_min_5d_diff},
    "mto_drv2_009_oversold_breadth_5d_diff": {"inputs": ["close"], "func": mto_drv2_009_oversold_breadth_5d_diff},
    "mto_drv2_010_master_count_5d_diff": {"inputs": ["close"], "func": mto_drv2_010_master_count_5d_diff},
    "mto_drv2_011_momentum_oversold_count_5d_diff": {"inputs": ["close"], "func": mto_drv2_011_momentum_oversold_count_5d_diff},
    "mto_drv2_012_rsi_14d_5d_diff": {"inputs": ["close"], "func": mto_drv2_012_rsi_14d_5d_diff},
    "mto_drv2_013_rsi_consensus_extremity_5d_diff": {"inputs": ["close"], "func": mto_drv2_013_rsi_consensus_extremity_5d_diff},
    "mto_drv2_014_pctb_min_5d_diff": {"inputs": ["close"], "func": mto_drv2_014_pctb_min_5d_diff},
    "mto_drv2_015_dd_confluence_score_5d_diff": {"inputs": ["close"], "func": mto_drv2_015_dd_confluence_score_5d_diff},
    "mto_drv2_016_oversold_alignment_5d_diff": {"inputs": ["close"], "func": mto_drv2_016_oversold_alignment_5d_diff},
    "mto_drv2_017_negative_momentum_confluence_5d_diff": {"inputs": ["close"], "func": mto_drv2_017_negative_momentum_confluence_5d_diff},
    "mto_drv2_018_capitulation_confluence_5d_diff": {"inputs": ["close"], "func": mto_drv2_018_capitulation_confluence_5d_diff},
    "mto_drv2_019_ma_cascade_alignment_5d_diff": {"inputs": ["close"], "func": mto_drv2_019_ma_cascade_alignment_5d_diff},
    "mto_drv2_020_williams_min_5d_diff": {"inputs": ["close"], "func": mto_drv2_020_williams_min_5d_diff},
    "mto_drv2_021_rsi_min_21d_diff": {"inputs": ["close"], "func": mto_drv2_021_rsi_min_21d_diff},
    "mto_drv2_022_capitulation_index_5d_diff": {"inputs": ["close"], "func": mto_drv2_022_capitulation_index_5d_diff},
    "mto_drv2_023_dd_mean_across_tf_5d_diff": {"inputs": ["close"], "func": mto_drv2_023_dd_mean_across_tf_5d_diff},
    "mto_drv2_024_oversold_family_count_5d_diff": {"inputs": ["close"], "func": mto_drv2_024_oversold_family_count_5d_diff},
    "mto_drv2_025_master_index_5d_diff": {"inputs": ["close"], "func": mto_drv2_025_master_index_5d_diff},
}
