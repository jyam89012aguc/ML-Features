"""
103_multi_timeframe_oversold — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of the 2nd-derivative multi-timeframe features —
        captures the inflection / exhaustion of building oversold confluence.
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


def _accel(s: pd.Series, n: int = 5) -> pd.Series:
    """Second difference: rate of change of the n-day rate of change."""
    return s.diff(n).diff(n)


_RSI_TF = (7, 14, 21, 63)
_RSI_EXT_TF = (7, 14, 21, 42, 63, 126, 252)
_MA_TF = (10, 21, 50, 100, 200)
_DD_TF = (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR, 504)
_DD_EXT_TF = (_TD_MON, 42, _TD_QTR, _TD_HALF, _TD_YEAR, 504, 756)
_PCTILE_TF = (_TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)
_MOM_TF = (_TD_WEEK, _TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)
_CHAN_TF = (14, _TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def mto_drv3_001_rsi_min_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the cross-horizon minimum RSI."""
    mn = pd.concat([_rsi(close, w) for w in _RSI_TF], axis=1).min(axis=1)
    return _accel(mn)


def mto_drv3_002_rsi_oversold_count_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the RSI oversold-horizon count."""
    cnt = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    return _accel(cnt)


def mto_drv3_003_below_ma_count_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the below-moving-average count."""
    cnt = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    return _accel(cnt)


def mto_drv3_004_dd_min_across_tf_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the deepest drawdown across horizons."""
    mn = pd.concat([_drawdown(close, w) for w in _DD_TF], axis=1).min(axis=1)
    return _accel(mn)


def mto_drv3_005_dd_extreme_count_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the count of horizons with drawdown worse than -20%."""
    cnt = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    return _accel(cnt)


def mto_drv3_006_new_low_count_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the multi-horizon new-low count."""
    cnt = sum((close <= _rolling_min(close, w)).astype(float) for w in _DD_TF)
    return _accel(cnt)


def mto_drv3_007_price_pctile_min_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the lowest close percentile rank across horizons."""
    mn = pd.concat([_rolling_rank_pct(close, w) for w in _PCTILE_TF], axis=1).min(axis=1)
    return _accel(mn)


def mto_drv3_008_stoch_min_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the minimum stochastic %K across channel horizons."""
    mn = pd.concat([_stoch_k(close, w) for w in _CHAN_TF], axis=1).min(axis=1)
    return _accel(mn)


def mto_drv3_009_oversold_breadth_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the oversold breadth index."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    ma_c = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    pc_c = sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF)
    total = len(_RSI_TF) + len(_MA_TF) + len(_DD_TF) + len(_PCTILE_TF)
    return _accel((rsi_c + ma_c + dd_c + pc_c) / total)


def mto_drv3_010_master_count_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the master oversold-signal count."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    return _accel(rsi_c + dd_c)


def mto_drv3_011_momentum_oversold_count_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the count of trailing-return horizons worse than -15%."""
    cnt = sum((close.pct_change(w) < -0.15).astype(float) for w in _MOM_TF)
    return _accel(cnt)


def mto_drv3_012_rsi_14d_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 14-day RSI."""
    return _accel(_rsi(close, 14))


def mto_drv3_013_rsi_consensus_extremity_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the RSI consensus extremity."""
    depth = sum((40.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_EXT_TF)
    return _accel(depth / len(_RSI_EXT_TF))


def mto_drv3_014_pctb_min_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the minimum Bollinger %B across horizons."""
    mn = pd.concat([_pct_b(close, w) for w in _PCTILE_TF], axis=1).min(axis=1)
    return _accel(mn)


def mto_drv3_015_dd_confluence_score_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the drawdown confluence score."""
    score = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF) / len(_DD_TF)
    return _accel(score)


def mto_drv3_016_oversold_alignment_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the cross-family oversold alignment score."""
    rsi_f = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF) / len(_RSI_TF)
    ma_f = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF) / len(_MA_TF)
    pc_f = sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF) / len(_PCTILE_TF)
    return _accel(rsi_f * ma_f * pc_f)


def mto_drv3_017_negative_momentum_confluence_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the negative-momentum confluence fraction."""
    frac = sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF) / len(_MOM_TF)
    return _accel(frac)


def mto_drv3_018_capitulation_confluence_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the capitulation confluence count."""
    rsi_c = sum((_rsi(close, w) < 25).astype(float) for w in _RSI_EXT_TF)
    dd_c = sum((_drawdown(close, w) < -0.30).astype(float) for w in _DD_EXT_TF)
    return _accel(rsi_c + dd_c)


def mto_drv3_019_ma_cascade_alignment_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the moving-average cascade alignment fraction."""
    cnt = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    return _accel(cnt / len(_MA_TF))


def mto_drv3_020_williams_min_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the minimum Williams %R across channel horizons."""
    mn = pd.concat([_williams_r(close, w) for w in _CHAN_TF], axis=1).min(axis=1)
    return _accel(mn)


def mto_drv3_021_rsi_min_21d_accel(close: pd.Series) -> pd.Series:
    """21-day-horizon acceleration of the cross-horizon minimum RSI."""
    mn = pd.concat([_rsi(close, w) for w in _RSI_TF], axis=1).min(axis=1)
    return _accel(mn, _TD_MON)


def mto_drv3_022_capitulation_index_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the multi-timeframe capitulation index."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF)
    ma_c = sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF)
    pc_c = sum((_rolling_rank_pct(close, w) < 0.10).astype(float) for w in _PCTILE_TF)
    total = len(_RSI_TF) + len(_MA_TF) + len(_DD_TF) + len(_PCTILE_TF)
    breadth = (rsi_c + ma_c + dd_c + pc_c) / total
    depth = sum((30.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_TF) / (len(_RSI_TF) * 30.0)
    return _accel(breadth * (0.5 + depth))


def mto_drv3_023_dd_mean_across_tf_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the mean drawdown across horizons."""
    mean_dd = pd.concat([_drawdown(close, w) for w in _DD_TF], axis=1).mean(axis=1)
    return _accel(mean_dd)


def mto_drv3_024_oversold_family_count_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the count of majority-oversold indicator families."""
    rsi_f = (sum((_rsi(close, w) < 30).astype(float) for w in _RSI_TF) / 4 > 0.5).astype(float)
    ma_f = (sum((close < _rolling_mean(close, w)).astype(float) for w in _MA_TF) / 5 > 0.5).astype(float)
    dd_f = (sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_TF) / 5 > 0.5).astype(float)
    mo_f = (sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF) / 5 > 0.5).astype(float)
    return _accel(rsi_f + ma_f + dd_f + mo_f)


def mto_drv3_025_master_index_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the master multi-timeframe capitulation index."""
    rsi_c = sum((_rsi(close, w) < 30).astype(float) for w in _RSI_EXT_TF)
    dd_c = sum((_drawdown(close, w) < -0.20).astype(float) for w in _DD_EXT_TF)
    mo_c = sum((close.pct_change(w) < 0).astype(float) for w in _MOM_TF)
    total = len(_RSI_EXT_TF) + len(_DD_EXT_TF) + len(_MOM_TF)
    breadth = (rsi_c + dd_c + mo_c) / total
    depth = sum((30.0 - _rsi(close, w)).clip(lower=0) for w in _RSI_EXT_TF) / (len(_RSI_EXT_TF) * 30.0)
    return _accel(breadth * (0.5 + depth))


# ── Registry ──────────────────────────────────────────────────────────────────

MULTI_TIMEFRAME_OVERSOLD_REGISTRY_3RD_DERIVATIVES = {
    "mto_drv3_001_rsi_min_accel": {"inputs": ["close"], "func": mto_drv3_001_rsi_min_accel},
    "mto_drv3_002_rsi_oversold_count_accel": {"inputs": ["close"], "func": mto_drv3_002_rsi_oversold_count_accel},
    "mto_drv3_003_below_ma_count_accel": {"inputs": ["close"], "func": mto_drv3_003_below_ma_count_accel},
    "mto_drv3_004_dd_min_across_tf_accel": {"inputs": ["close"], "func": mto_drv3_004_dd_min_across_tf_accel},
    "mto_drv3_005_dd_extreme_count_accel": {"inputs": ["close"], "func": mto_drv3_005_dd_extreme_count_accel},
    "mto_drv3_006_new_low_count_accel": {"inputs": ["close"], "func": mto_drv3_006_new_low_count_accel},
    "mto_drv3_007_price_pctile_min_accel": {"inputs": ["close"], "func": mto_drv3_007_price_pctile_min_accel},
    "mto_drv3_008_stoch_min_accel": {"inputs": ["close"], "func": mto_drv3_008_stoch_min_accel},
    "mto_drv3_009_oversold_breadth_accel": {"inputs": ["close"], "func": mto_drv3_009_oversold_breadth_accel},
    "mto_drv3_010_master_count_accel": {"inputs": ["close"], "func": mto_drv3_010_master_count_accel},
    "mto_drv3_011_momentum_oversold_count_accel": {"inputs": ["close"], "func": mto_drv3_011_momentum_oversold_count_accel},
    "mto_drv3_012_rsi_14d_accel": {"inputs": ["close"], "func": mto_drv3_012_rsi_14d_accel},
    "mto_drv3_013_rsi_consensus_extremity_accel": {"inputs": ["close"], "func": mto_drv3_013_rsi_consensus_extremity_accel},
    "mto_drv3_014_pctb_min_accel": {"inputs": ["close"], "func": mto_drv3_014_pctb_min_accel},
    "mto_drv3_015_dd_confluence_score_accel": {"inputs": ["close"], "func": mto_drv3_015_dd_confluence_score_accel},
    "mto_drv3_016_oversold_alignment_accel": {"inputs": ["close"], "func": mto_drv3_016_oversold_alignment_accel},
    "mto_drv3_017_negative_momentum_confluence_accel": {"inputs": ["close"], "func": mto_drv3_017_negative_momentum_confluence_accel},
    "mto_drv3_018_capitulation_confluence_accel": {"inputs": ["close"], "func": mto_drv3_018_capitulation_confluence_accel},
    "mto_drv3_019_ma_cascade_alignment_accel": {"inputs": ["close"], "func": mto_drv3_019_ma_cascade_alignment_accel},
    "mto_drv3_020_williams_min_accel": {"inputs": ["close"], "func": mto_drv3_020_williams_min_accel},
    "mto_drv3_021_rsi_min_21d_accel": {"inputs": ["close"], "func": mto_drv3_021_rsi_min_21d_accel},
    "mto_drv3_022_capitulation_index_accel": {"inputs": ["close"], "func": mto_drv3_022_capitulation_index_accel},
    "mto_drv3_023_dd_mean_across_tf_accel": {"inputs": ["close"], "func": mto_drv3_023_dd_mean_across_tf_accel},
    "mto_drv3_024_oversold_family_count_accel": {"inputs": ["close"], "func": mto_drv3_024_oversold_family_count_accel},
    "mto_drv3_025_master_index_accel": {"inputs": ["close"], "func": mto_drv3_025_master_index_accel},
}
