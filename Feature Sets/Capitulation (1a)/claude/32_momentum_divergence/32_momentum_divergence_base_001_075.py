"""
32_momentum_divergence — Base Features 001-075
Domain: price makes a new low while a momentum indicator does NOT — bullish divergence signals
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — price-vs-momentum extreme mismatch at multi-year lows
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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _rsi(close: pd.Series, period: int) -> pd.Series:
    """Wilder RSI, returns 0-100 series."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period // 2, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period // 2, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - _safe_div(pd.Series(100.0, index=close.index), 1.0 + rs)


def _macd_line(close: pd.Series, fast: int = 12, slow: int = 26) -> pd.Series:
    """MACD line = EMA(fast) - EMA(slow)."""
    return _ewm_mean(close, fast) - _ewm_mean(close, slow)


def _roc(close: pd.Series, period: int) -> pd.Series:
    """Rate of change over period days."""
    return _safe_div(close - close.shift(period), close.shift(period))


def _cci(close: pd.Series, high: pd.Series, low: pd.Series, period: int) -> pd.Series:
    """Commodity Channel Index."""
    tp = (high + low + close) / 3.0
    tp_ma = _rolling_mean(tp, period)
    mad = tp.rolling(period, min_periods=max(1, period // 2)).apply(
        lambda x: np.mean(np.abs(x - x.mean())), raw=True
    )
    return _safe_div(tp - tp_ma, 0.015 * mad)


def _stoch_k(close: pd.Series, high: pd.Series, low: pd.Series, period: int = 14) -> pd.Series:
    """Stochastic %K."""
    lo = _rolling_min(low, period)
    hi = _rolling_max(high, period)
    return _safe_div(close - lo, hi - lo) * 100.0


def _williams_r(close: pd.Series, high: pd.Series, low: pd.Series, period: int = 14) -> pd.Series:
    """Williams %R."""
    hi = _rolling_max(high, period)
    lo = _rolling_min(low, period)
    return _safe_div(hi - close, hi - lo) * -100.0


def _price_new_low(close: pd.Series, w: int) -> pd.Series:
    """Boolean: close makes a new w-period low vs prior bar."""
    prior_min = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return (close < prior_min).astype(float)


def _pct_rank(s: pd.Series, w: int) -> pd.Series:
    """Rolling percentile rank within window w."""
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): RSI divergence — price new low, RSI not at new low ---

def mdv_001_rsi14_divg_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: price makes 21-day new low but RSI(14) does NOT; bullish divergence flag."""
    price_nl = _price_new_low(close, _TD_MON)
    rsi = _rsi(close, 14)
    rsi_nl = (rsi < rsi.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()).astype(float)
    return (price_nl * (1.0 - rsi_nl))


def mdv_002_rsi14_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: price makes 63-day new low but RSI(14) does NOT."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    rsi_nl = (rsi < rsi.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    return (price_nl * (1.0 - rsi_nl))


def mdv_003_rsi14_divg_flag_126d(close: pd.Series) -> pd.Series:
    """Binary: price makes 126-day new low but RSI(14) does NOT."""
    price_nl = _price_new_low(close, _TD_HALF)
    rsi = _rsi(close, 14)
    rsi_nl = (rsi < rsi.shift(1).rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).min()).astype(float)
    return (price_nl * (1.0 - rsi_nl))


def mdv_004_rsi14_divg_flag_252d(close: pd.Series) -> pd.Series:
    """Binary: price makes 252-day new low but RSI(14) does NOT."""
    price_nl = _price_new_low(close, _TD_YEAR)
    rsi = _rsi(close, 14)
    rsi_nl = (rsi < rsi.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()).astype(float)
    return (price_nl * (1.0 - rsi_nl))


def mdv_005_rsi14_gap_at_price_low_21d(close: pd.Series) -> pd.Series:
    """RSI(14) level minus its 21-day min at each price-new-low bar; 0 otherwise."""
    price_nl = _price_new_low(close, _TD_MON)
    rsi = _rsi(close, 14)
    rsi_floor = rsi.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    gap = (rsi - rsi_floor).clip(lower=0.0)
    return gap * price_nl


def mdv_006_rsi14_gap_at_price_low_63d(close: pd.Series) -> pd.Series:
    """RSI(14) minus its 63-day min at each 63-day price-new-low bar; 0 otherwise."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, 14)
    rsi_floor = rsi.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    gap = (rsi - rsi_floor).clip(lower=0.0)
    return gap * price_nl


def mdv_007_rsi14_gap_at_price_low_252d(close: pd.Series) -> pd.Series:
    """RSI(14) minus its 252-day min at each 252-day price-new-low bar; 0 otherwise."""
    price_nl = _price_new_low(close, _TD_YEAR)
    rsi = _rsi(close, 14)
    rsi_floor = rsi.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    gap = (rsi - rsi_floor).clip(lower=0.0)
    return gap * price_nl


def mdv_008_rsi14_divg_count_63d(close: pd.Series) -> pd.Series:
    """Count of RSI-14 bullish divergence flags in trailing 63 days."""
    flag = mdv_002_rsi14_divg_flag_63d(close)
    return _rolling_sum(flag, _TD_QTR)


def mdv_009_rsi14_divg_count_252d(close: pd.Series) -> pd.Series:
    """Count of RSI-14 bullish divergence flags in trailing 252 days."""
    flag = mdv_002_rsi14_divg_flag_63d(close)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_010_rsi14_pctrank_spread_21d(close: pd.Series) -> pd.Series:
    """Spread: RSI(14) pct-rank minus price pct-rank over 21-day window (divergence gap)."""
    rsi = _rsi(close, 14)
    rsi_rank = _pct_rank(rsi, _TD_MON)
    price_rank = _pct_rank(close, _TD_MON)
    return rsi_rank - price_rank


# --- Group B (011-020): RSI variants and multi-period divergence magnitude ---

def mdv_011_rsi7_divg_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: price 21-day new low but RSI(7) does NOT."""
    price_nl = _price_new_low(close, _TD_MON)
    rsi = _rsi(close, 7)
    rsi_nl = (rsi < rsi.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()).astype(float)
    return price_nl * (1.0 - rsi_nl)


def mdv_012_rsi21_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but RSI(21) does NOT."""
    price_nl = _price_new_low(close, _TD_QTR)
    rsi = _rsi(close, _TD_MON)
    rsi_nl = (rsi < rsi.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    return price_nl * (1.0 - rsi_nl)


def mdv_013_rsi14_pctrank_spread_63d(close: pd.Series) -> pd.Series:
    """RSI(14) pct-rank minus price pct-rank over 63-day window."""
    rsi = _rsi(close, 14)
    rsi_rank = _pct_rank(rsi, _TD_QTR)
    price_rank = _pct_rank(close, _TD_QTR)
    return rsi_rank - price_rank


def mdv_014_rsi14_pctrank_spread_252d(close: pd.Series) -> pd.Series:
    """RSI(14) pct-rank minus price pct-rank over 252-day window."""
    rsi = _rsi(close, 14)
    rsi_rank = _pct_rank(rsi, _TD_YEAR)
    price_rank = _pct_rank(close, _TD_YEAR)
    return rsi_rank - price_rank


def mdv_015_rsi14_spread_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI-price spread within trailing 252 days."""
    spread = mdv_014_rsi14_pctrank_spread_252d(close)
    return _pct_rank(spread, _TD_YEAR)


def mdv_016_rsi14_divg_magnitude_21d(close: pd.Series) -> pd.Series:
    """Price drawdown from 21-day high minus RSI drawdown from 21-day high (normalized)."""
    rsi = _rsi(close, 14)
    price_hi = _rolling_max(close, _TD_MON)
    rsi_hi = _rolling_max(rsi, _TD_MON)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    rsi_dd = _safe_div(rsi_hi - rsi, rsi_hi.clip(lower=_EPS))
    return price_dd - rsi_dd


def mdv_017_rsi14_divg_magnitude_63d(close: pd.Series) -> pd.Series:
    """Price drawdown from 63-day high minus RSI drawdown from 63-day high."""
    rsi = _rsi(close, 14)
    price_hi = _rolling_max(close, _TD_QTR)
    rsi_hi = _rolling_max(rsi, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    rsi_dd = _safe_div(rsi_hi - rsi, rsi_hi.clip(lower=_EPS))
    return price_dd - rsi_dd


def mdv_018_rsi14_divg_magnitude_252d(close: pd.Series) -> pd.Series:
    """Price drawdown from 252-day high minus RSI drawdown from 252-day high."""
    rsi = _rsi(close, 14)
    price_hi = _rolling_max(close, _TD_YEAR)
    rsi_hi = _rolling_max(rsi, _TD_YEAR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    rsi_dd = _safe_div(rsi_hi - rsi, rsi_hi.clip(lower=_EPS))
    return price_dd - rsi_dd


def mdv_019_rsi14_max_gap_at_low_63d(close: pd.Series) -> pd.Series:
    """Maximum RSI gap above its min observed over last 63 days on price-new-low days."""
    gap = mdv_006_rsi14_gap_at_price_low_63d(close)
    return _rolling_max(gap, _TD_QTR)


def mdv_020_rsi14_max_gap_at_low_252d(close: pd.Series) -> pd.Series:
    """Maximum RSI gap above its min over last 252 days on price-new-low days."""
    gap = mdv_007_rsi14_gap_at_price_low_252d(close)
    return _rolling_max(gap, _TD_YEAR)


# --- Group C (021-030): MACD divergence ---

def mdv_021_macd_divg_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: price 21-day new low but MACD line does NOT."""
    price_nl = _price_new_low(close, _TD_MON)
    macd = _macd_line(close)
    macd_nl = (macd < macd.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()).astype(float)
    return price_nl * (1.0 - macd_nl)


def mdv_022_macd_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but MACD line does NOT."""
    price_nl = _price_new_low(close, _TD_QTR)
    macd = _macd_line(close)
    macd_nl = (macd < macd.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    return price_nl * (1.0 - macd_nl)


def mdv_023_macd_divg_flag_252d(close: pd.Series) -> pd.Series:
    """Binary: price 252-day new low but MACD line does NOT."""
    price_nl = _price_new_low(close, _TD_YEAR)
    macd = _macd_line(close)
    macd_nl = (macd < macd.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()).astype(float)
    return price_nl * (1.0 - macd_nl)


def mdv_024_macd_gap_at_price_low_63d(close: pd.Series) -> pd.Series:
    """MACD level minus its 63-day min when price makes a 63-day low; 0 otherwise."""
    price_nl = _price_new_low(close, _TD_QTR)
    macd = _macd_line(close)
    macd_floor = macd.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    gap = (macd - macd_floor)
    return gap * price_nl


def mdv_025_macd_pctrank_spread_63d(close: pd.Series) -> pd.Series:
    """MACD pct-rank minus price pct-rank over 63-day window."""
    macd = _macd_line(close)
    macd_rank = _pct_rank(macd, _TD_QTR)
    price_rank = _pct_rank(close, _TD_QTR)
    return macd_rank - price_rank


def mdv_026_macd_pctrank_spread_252d(close: pd.Series) -> pd.Series:
    """MACD pct-rank minus price pct-rank over 252-day window."""
    macd = _macd_line(close)
    macd_rank = _pct_rank(macd, _TD_YEAR)
    price_rank = _pct_rank(close, _TD_YEAR)
    return macd_rank - price_rank


def mdv_027_macd_hist_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but MACD histogram does NOT make a new low."""
    price_nl = _price_new_low(close, _TD_QTR)
    macd = _macd_line(close)
    signal = _ewm_mean(macd, 9)
    hist = macd - signal
    hist_nl = (hist < hist.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    return price_nl * (1.0 - hist_nl)


def mdv_028_macd_divg_count_252d(close: pd.Series) -> pd.Series:
    """Count of MACD bullish divergence flags over trailing 252 days."""
    flag = mdv_022_macd_divg_flag_63d(close)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_029_macd_divg_magnitude_63d(close: pd.Series) -> pd.Series:
    """Price pct-drawdown from 63d high minus MACD pct-drawdown from 63d high."""
    macd = _macd_line(close)
    price_hi = _rolling_max(close, _TD_QTR)
    macd_hi = _rolling_max(macd, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    macd_range = macd_hi - macd.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    macd_dd = _safe_div(macd_hi - macd, macd_range.clip(lower=_EPS))
    return price_dd - macd_dd


def mdv_030_macd_divg_magnitude_252d(close: pd.Series) -> pd.Series:
    """Price pct-drawdown from 252d high minus MACD pct-drawdown from 252d high."""
    macd = _macd_line(close)
    price_hi = _rolling_max(close, _TD_YEAR)
    macd_hi = _rolling_max(macd, _TD_YEAR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    macd_range = macd_hi - macd.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    macd_dd = _safe_div(macd_hi - macd, macd_range.clip(lower=_EPS))
    return price_dd - macd_dd


# --- Group D (031-040): ROC divergence ---

def mdv_031_roc10_divg_flag_21d(close: pd.Series) -> pd.Series:
    """Binary: price 21-day new low but ROC(10) does NOT."""
    price_nl = _price_new_low(close, _TD_MON)
    roc = _roc(close, 10)
    roc_nl = (roc < roc.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()).astype(float)
    return price_nl * (1.0 - roc_nl)


def mdv_032_roc10_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but ROC(10) does NOT."""
    price_nl = _price_new_low(close, _TD_QTR)
    roc = _roc(close, 10)
    roc_nl = (roc < roc.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    return price_nl * (1.0 - roc_nl)


def mdv_033_roc21_divg_flag_63d(close: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but ROC(21) does NOT."""
    price_nl = _price_new_low(close, _TD_QTR)
    roc = _roc(close, _TD_MON)
    roc_nl = (roc < roc.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    return price_nl * (1.0 - roc_nl)


def mdv_034_roc63_divg_flag_252d(close: pd.Series) -> pd.Series:
    """Binary: price 252-day new low but ROC(63) does NOT."""
    price_nl = _price_new_low(close, _TD_YEAR)
    roc = _roc(close, _TD_QTR)
    roc_nl = (roc < roc.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()).astype(float)
    return price_nl * (1.0 - roc_nl)


def mdv_035_roc10_pctrank_spread_63d(close: pd.Series) -> pd.Series:
    """ROC(10) pct-rank minus price pct-rank over 63-day window."""
    roc = _roc(close, 10)
    roc_rank = _pct_rank(roc, _TD_QTR)
    price_rank = _pct_rank(close, _TD_QTR)
    return roc_rank - price_rank


def mdv_036_roc21_pctrank_spread_63d(close: pd.Series) -> pd.Series:
    """ROC(21) pct-rank minus price pct-rank over 63-day window."""
    roc = _roc(close, _TD_MON)
    roc_rank = _pct_rank(roc, _TD_QTR)
    price_rank = _pct_rank(close, _TD_QTR)
    return roc_rank - price_rank


def mdv_037_roc10_gap_at_price_low_63d(close: pd.Series) -> pd.Series:
    """ROC(10) minus its 63-day min when price makes a 63-day new low; 0 otherwise."""
    price_nl = _price_new_low(close, _TD_QTR)
    roc = _roc(close, 10)
    roc_floor = roc.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return (roc - roc_floor).clip(lower=0.0) * price_nl


def mdv_038_roc21_gap_at_price_low_63d(close: pd.Series) -> pd.Series:
    """ROC(21) minus its 63-day min when price makes a 63-day new low; 0 otherwise."""
    price_nl = _price_new_low(close, _TD_QTR)
    roc = _roc(close, _TD_MON)
    roc_floor = roc.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return (roc - roc_floor).clip(lower=0.0) * price_nl


def mdv_039_roc10_divg_count_252d(close: pd.Series) -> pd.Series:
    """Count of ROC(10) bullish divergence flags over trailing 252 days."""
    flag = mdv_032_roc10_divg_flag_63d(close)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_040_roc_multi_divg_score_63d(close: pd.Series) -> pd.Series:
    """Sum of ROC(10), ROC(21) divergence flags at price 63-day low; 0-2 score."""
    return mdv_032_roc10_divg_flag_63d(close) + mdv_033_roc21_divg_flag_63d(close)


# --- Group E (041-050): Stochastic and Williams %R divergence ---

def mdv_041_stoch_divg_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 21-day new low but Stochastic %K does NOT."""
    price_nl = _price_new_low(close, _TD_MON)
    sk = _stoch_k(close, high, low, 14)
    sk_nl = (sk < sk.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()).astype(float)
    return price_nl * (1.0 - sk_nl)


def mdv_042_stoch_divg_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but Stochastic %K does NOT."""
    price_nl = _price_new_low(close, _TD_QTR)
    sk = _stoch_k(close, high, low, 14)
    sk_nl = (sk < sk.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    return price_nl * (1.0 - sk_nl)


def mdv_043_stoch_gap_at_price_low_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Stoch %K minus its 63-day min at each 63-day price-new-low; 0 otherwise."""
    price_nl = _price_new_low(close, _TD_QTR)
    sk = _stoch_k(close, high, low, 14)
    sk_floor = sk.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return (sk - sk_floor).clip(lower=0.0) * price_nl


def mdv_044_stoch_pctrank_spread_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Stoch %K pct-rank minus price pct-rank over 63-day window."""
    sk = _stoch_k(close, high, low, 14)
    return _pct_rank(sk, _TD_QTR) - _pct_rank(close, _TD_QTR)


def mdv_045_stoch_pctrank_spread_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Stoch %K pct-rank minus price pct-rank over 252-day window."""
    sk = _stoch_k(close, high, low, 14)
    return _pct_rank(sk, _TD_YEAR) - _pct_rank(close, _TD_YEAR)


def mdv_046_willr_divg_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 21-day new low but Williams %R does NOT make new low."""
    price_nl = _price_new_low(close, _TD_MON)
    wr = _williams_r(close, high, low, 14)
    wr_nl = (wr < wr.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()).astype(float)
    return price_nl * (1.0 - wr_nl)


def mdv_047_willr_divg_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but Williams %R does NOT make new low."""
    price_nl = _price_new_low(close, _TD_QTR)
    wr = _williams_r(close, high, low, 14)
    wr_nl = (wr < wr.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    return price_nl * (1.0 - wr_nl)


def mdv_048_willr_gap_at_price_low_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Williams %R above its 63-day min at each 63-day price-new-low bar; 0 otherwise."""
    price_nl = _price_new_low(close, _TD_QTR)
    wr = _williams_r(close, high, low, 14)
    wr_floor = wr.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return (wr - wr_floor).clip(lower=0.0) * price_nl


def mdv_049_stoch_divg_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Stochastic bullish divergence flags in trailing 252 days."""
    flag = mdv_042_stoch_divg_flag_63d(close, high, low)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_050_willr_pctrank_spread_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Williams %R pct-rank minus price pct-rank (note: %R negated for alignment)."""
    wr = -_williams_r(close, high, low, 14)
    return _pct_rank(wr, _TD_QTR) - _pct_rank(close, _TD_QTR)


# --- Group F (051-060): CCI divergence ---

def mdv_051_cci_divg_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 21-day new low but CCI(20) does NOT."""
    price_nl = _price_new_low(close, _TD_MON)
    cci = _cci(close, high, low, 20)
    cci_nl = (cci < cci.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()).astype(float)
    return price_nl * (1.0 - cci_nl)


def mdv_052_cci_divg_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but CCI(20) does NOT."""
    price_nl = _price_new_low(close, _TD_QTR)
    cci = _cci(close, high, low, 20)
    cci_nl = (cci < cci.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    return price_nl * (1.0 - cci_nl)


def mdv_053_cci_gap_at_price_low_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CCI(20) above its 63-day min at each 63-day price-new-low bar; 0 otherwise."""
    price_nl = _price_new_low(close, _TD_QTR)
    cci = _cci(close, high, low, 20)
    cci_floor = cci.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return (cci - cci_floor).clip(lower=0.0) * price_nl


def mdv_054_cci_pctrank_spread_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CCI(20) pct-rank minus price pct-rank over 63-day window."""
    cci = _cci(close, high, low, 20)
    return _pct_rank(cci, _TD_QTR) - _pct_rank(close, _TD_QTR)


def mdv_055_cci_pctrank_spread_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CCI(20) pct-rank minus price pct-rank over 252-day window."""
    cci = _cci(close, high, low, 20)
    return _pct_rank(cci, _TD_YEAR) - _pct_rank(close, _TD_YEAR)


def mdv_056_cci_divg_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of CCI bullish divergence flags in trailing 252 days."""
    flag = mdv_052_cci_divg_flag_63d(close, high, low)
    return _rolling_sum(flag, _TD_YEAR)


def mdv_057_cci_divg_magnitude_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Price drawdown fraction minus CCI drawdown fraction from 63-day high."""
    cci = _cci(close, high, low, 20)
    price_hi = _rolling_max(close, _TD_QTR)
    cci_hi = _rolling_max(cci, _TD_QTR)
    price_dd = _safe_div(price_hi - close, price_hi.clip(lower=_EPS))
    cci_range = cci_hi - cci.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    cci_dd = _safe_div(cci_hi - cci, cci_range.clip(lower=_EPS))
    return price_dd - cci_dd


def mdv_058_cci14_divg_flag_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 63-day new low but CCI(14) does NOT."""
    price_nl = _price_new_low(close, _TD_QTR)
    cci = _cci(close, high, low, 14)
    cci_nl = (cci < cci.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()).astype(float)
    return price_nl * (1.0 - cci_nl)


def mdv_059_cci_gap_max_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max CCI gap at price-new-low over trailing 252 days."""
    gap = mdv_053_cci_gap_at_price_low_63d(close, high, low)
    return _rolling_max(gap, _TD_YEAR)


def mdv_060_cci_divg_flag_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: price 252-day new low but CCI(20) does NOT."""
    price_nl = _price_new_low(close, _TD_YEAR)
    cci = _cci(close, high, low, 20)
    cci_nl = (cci < cci.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()).astype(float)
    return price_nl * (1.0 - cci_nl)


# --- Group G (061-075): Multi-indicator composite divergence scores ---

def mdv_061_composite_divg_score_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of RSI, MACD, ROC(10), Stoch, Williams divergence flags at 21-day low; 0-5."""
    a = mdv_001_rsi14_divg_flag_21d(close)
    b = mdv_021_macd_divg_flag_21d(close)
    c = mdv_031_roc10_divg_flag_21d(close)
    d = mdv_041_stoch_divg_flag_21d(close, high, low)
    e = mdv_046_willr_divg_flag_21d(close, high, low)
    return a + b + c + d + e


def mdv_062_composite_divg_score_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of RSI, MACD, ROC(10), ROC(21), Stoch, Williams, CCI divergence flags at 63-day low; 0-7."""
    a = mdv_002_rsi14_divg_flag_63d(close)
    b = mdv_022_macd_divg_flag_63d(close)
    c = mdv_032_roc10_divg_flag_63d(close)
    d = mdv_033_roc21_divg_flag_63d(close)
    e = mdv_042_stoch_divg_flag_63d(close, high, low)
    f = mdv_047_willr_divg_flag_63d(close, high, low)
    g = mdv_052_cci_divg_flag_63d(close, high, low)
    return a + b + c + d + e + f + g


def mdv_063_composite_divg_score_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of RSI, MACD, ROC(63), CCI divergence flags at 252-day low; 0-4."""
    a = mdv_004_rsi14_divg_flag_252d(close)
    b = mdv_023_macd_divg_flag_252d(close)
    c = mdv_034_roc63_divg_flag_252d(close)
    d = mdv_060_cci_divg_flag_252d(close, high, low)
    return a + b + c + d


def mdv_064_pctrank_spread_avg_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average of RSI, MACD, ROC(10) pct-rank spreads vs price over 63-day window."""
    a = mdv_013_rsi14_pctrank_spread_63d(close)
    b = mdv_025_macd_pctrank_spread_63d(close)
    c = mdv_035_roc10_pctrank_spread_63d(close)
    d = mdv_044_stoch_pctrank_spread_63d(close, high, low)
    return (a + b + c + d) / 4.0


def mdv_065_pctrank_spread_avg_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average of RSI, MACD pct-rank spreads vs price over 252-day window."""
    a = mdv_014_rsi14_pctrank_spread_252d(close)
    b = mdv_026_macd_pctrank_spread_252d(close)
    c = mdv_045_stoch_pctrank_spread_252d(close, high, low)
    d = mdv_055_cci_pctrank_spread_252d(close, high, low)
    return (a + b + c + d) / 4.0


def mdv_066_composite_divg_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Total indicator divergence events (RSI+MACD+ROC+Stoch+CCI) over 252 days."""
    return (
        mdv_009_rsi14_divg_count_252d(close)
        + mdv_028_macd_divg_count_252d(close)
        + mdv_039_roc10_divg_count_252d(close)
        + mdv_049_stoch_divg_count_252d(close, high, low)
        + mdv_056_cci_divg_count_252d(close, high, low)
    )


def mdv_067_composite_pctrank_spread_pctrank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of composite pct-rank spread within trailing 252 days."""
    avg = mdv_064_pctrank_spread_avg_63d(close, high, low)
    return _pct_rank(avg, _TD_YEAR)


def mdv_068_divg_score_63d_pctrank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63-day composite divergence score within trailing 252 days."""
    score = mdv_062_composite_divg_score_63d(close, high, low)
    return _pct_rank(score, _TD_YEAR)


def mdv_069_rsi_macd_divg_agree_63d(close: pd.Series) -> pd.Series:
    """Binary: both RSI and MACD signal divergence at same 63-day price low."""
    return (mdv_002_rsi14_divg_flag_63d(close) * mdv_022_macd_divg_flag_63d(close))


def mdv_070_three_indicator_divg_agree_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: RSI, MACD, and ROC(10) all diverge at 63-day price low simultaneously."""
    a = mdv_002_rsi14_divg_flag_63d(close)
    b = mdv_022_macd_divg_flag_63d(close)
    c = mdv_032_roc10_divg_flag_63d(close)
    return ((a + b + c) >= 3.0).astype(float)


def mdv_071_divg_score_21d_rolling_max_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum composite divergence score at 21-day lows over trailing 63 days."""
    score = mdv_061_composite_divg_score_21d(close, high, low)
    return _rolling_max(score, _TD_QTR)


def mdv_072_divg_score_63d_rolling_max_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum composite divergence score at 63-day lows over trailing 252 days."""
    score = mdv_062_composite_divg_score_63d(close, high, low)
    return _rolling_max(score, _TD_YEAR)


def mdv_073_consecutive_price_lows_no_rsi_low_21d(close: pd.Series) -> pd.Series:
    """Consecutive 21-day new price lows where RSI(14) does NOT also hit new low."""
    flag = mdv_001_rsi14_divg_flag_21d(close)
    c = flag.astype(int)
    group = (flag == 0).cumsum()
    return c.groupby(group).cumsum().astype(float)


def mdv_074_consecutive_price_lows_no_macd_low_63d(close: pd.Series) -> pd.Series:
    """Consecutive 63-day new price lows where MACD does NOT also hit new low."""
    flag = mdv_022_macd_divg_flag_63d(close)
    c = flag.astype(int)
    group = (flag == 0).cumsum()
    return c.groupby(group).cumsum().astype(float)


def mdv_075_momentum_price_divergence_strength_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite strength: composite pct-rank spread * composite divergence flag agreement."""
    spread = mdv_064_pctrank_spread_avg_63d(close, high, low)
    flag = (mdv_062_composite_divg_score_63d(close, high, low) >= 3.0).astype(float)
    return spread * flag


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DIVERGENCE_REGISTRY_001_075 = {
    "mdv_001_rsi14_divg_flag_21d": {"inputs": ["close"], "func": mdv_001_rsi14_divg_flag_21d},
    "mdv_002_rsi14_divg_flag_63d": {"inputs": ["close"], "func": mdv_002_rsi14_divg_flag_63d},
    "mdv_003_rsi14_divg_flag_126d": {"inputs": ["close"], "func": mdv_003_rsi14_divg_flag_126d},
    "mdv_004_rsi14_divg_flag_252d": {"inputs": ["close"], "func": mdv_004_rsi14_divg_flag_252d},
    "mdv_005_rsi14_gap_at_price_low_21d": {"inputs": ["close"], "func": mdv_005_rsi14_gap_at_price_low_21d},
    "mdv_006_rsi14_gap_at_price_low_63d": {"inputs": ["close"], "func": mdv_006_rsi14_gap_at_price_low_63d},
    "mdv_007_rsi14_gap_at_price_low_252d": {"inputs": ["close"], "func": mdv_007_rsi14_gap_at_price_low_252d},
    "mdv_008_rsi14_divg_count_63d": {"inputs": ["close"], "func": mdv_008_rsi14_divg_count_63d},
    "mdv_009_rsi14_divg_count_252d": {"inputs": ["close"], "func": mdv_009_rsi14_divg_count_252d},
    "mdv_010_rsi14_pctrank_spread_21d": {"inputs": ["close"], "func": mdv_010_rsi14_pctrank_spread_21d},
    "mdv_011_rsi7_divg_flag_21d": {"inputs": ["close"], "func": mdv_011_rsi7_divg_flag_21d},
    "mdv_012_rsi21_divg_flag_63d": {"inputs": ["close"], "func": mdv_012_rsi21_divg_flag_63d},
    "mdv_013_rsi14_pctrank_spread_63d": {"inputs": ["close"], "func": mdv_013_rsi14_pctrank_spread_63d},
    "mdv_014_rsi14_pctrank_spread_252d": {"inputs": ["close"], "func": mdv_014_rsi14_pctrank_spread_252d},
    "mdv_015_rsi14_spread_pctrank_252d": {"inputs": ["close"], "func": mdv_015_rsi14_spread_pctrank_252d},
    "mdv_016_rsi14_divg_magnitude_21d": {"inputs": ["close"], "func": mdv_016_rsi14_divg_magnitude_21d},
    "mdv_017_rsi14_divg_magnitude_63d": {"inputs": ["close"], "func": mdv_017_rsi14_divg_magnitude_63d},
    "mdv_018_rsi14_divg_magnitude_252d": {"inputs": ["close"], "func": mdv_018_rsi14_divg_magnitude_252d},
    "mdv_019_rsi14_max_gap_at_low_63d": {"inputs": ["close"], "func": mdv_019_rsi14_max_gap_at_low_63d},
    "mdv_020_rsi14_max_gap_at_low_252d": {"inputs": ["close"], "func": mdv_020_rsi14_max_gap_at_low_252d},
    "mdv_021_macd_divg_flag_21d": {"inputs": ["close"], "func": mdv_021_macd_divg_flag_21d},
    "mdv_022_macd_divg_flag_63d": {"inputs": ["close"], "func": mdv_022_macd_divg_flag_63d},
    "mdv_023_macd_divg_flag_252d": {"inputs": ["close"], "func": mdv_023_macd_divg_flag_252d},
    "mdv_024_macd_gap_at_price_low_63d": {"inputs": ["close"], "func": mdv_024_macd_gap_at_price_low_63d},
    "mdv_025_macd_pctrank_spread_63d": {"inputs": ["close"], "func": mdv_025_macd_pctrank_spread_63d},
    "mdv_026_macd_pctrank_spread_252d": {"inputs": ["close"], "func": mdv_026_macd_pctrank_spread_252d},
    "mdv_027_macd_hist_divg_flag_63d": {"inputs": ["close"], "func": mdv_027_macd_hist_divg_flag_63d},
    "mdv_028_macd_divg_count_252d": {"inputs": ["close"], "func": mdv_028_macd_divg_count_252d},
    "mdv_029_macd_divg_magnitude_63d": {"inputs": ["close"], "func": mdv_029_macd_divg_magnitude_63d},
    "mdv_030_macd_divg_magnitude_252d": {"inputs": ["close"], "func": mdv_030_macd_divg_magnitude_252d},
    "mdv_031_roc10_divg_flag_21d": {"inputs": ["close"], "func": mdv_031_roc10_divg_flag_21d},
    "mdv_032_roc10_divg_flag_63d": {"inputs": ["close"], "func": mdv_032_roc10_divg_flag_63d},
    "mdv_033_roc21_divg_flag_63d": {"inputs": ["close"], "func": mdv_033_roc21_divg_flag_63d},
    "mdv_034_roc63_divg_flag_252d": {"inputs": ["close"], "func": mdv_034_roc63_divg_flag_252d},
    "mdv_035_roc10_pctrank_spread_63d": {"inputs": ["close"], "func": mdv_035_roc10_pctrank_spread_63d},
    "mdv_036_roc21_pctrank_spread_63d": {"inputs": ["close"], "func": mdv_036_roc21_pctrank_spread_63d},
    "mdv_037_roc10_gap_at_price_low_63d": {"inputs": ["close"], "func": mdv_037_roc10_gap_at_price_low_63d},
    "mdv_038_roc21_gap_at_price_low_63d": {"inputs": ["close"], "func": mdv_038_roc21_gap_at_price_low_63d},
    "mdv_039_roc10_divg_count_252d": {"inputs": ["close"], "func": mdv_039_roc10_divg_count_252d},
    "mdv_040_roc_multi_divg_score_63d": {"inputs": ["close"], "func": mdv_040_roc_multi_divg_score_63d},
    "mdv_041_stoch_divg_flag_21d": {"inputs": ["close", "high", "low"], "func": mdv_041_stoch_divg_flag_21d},
    "mdv_042_stoch_divg_flag_63d": {"inputs": ["close", "high", "low"], "func": mdv_042_stoch_divg_flag_63d},
    "mdv_043_stoch_gap_at_price_low_63d": {"inputs": ["close", "high", "low"], "func": mdv_043_stoch_gap_at_price_low_63d},
    "mdv_044_stoch_pctrank_spread_63d": {"inputs": ["close", "high", "low"], "func": mdv_044_stoch_pctrank_spread_63d},
    "mdv_045_stoch_pctrank_spread_252d": {"inputs": ["close", "high", "low"], "func": mdv_045_stoch_pctrank_spread_252d},
    "mdv_046_willr_divg_flag_21d": {"inputs": ["close", "high", "low"], "func": mdv_046_willr_divg_flag_21d},
    "mdv_047_willr_divg_flag_63d": {"inputs": ["close", "high", "low"], "func": mdv_047_willr_divg_flag_63d},
    "mdv_048_willr_gap_at_price_low_63d": {"inputs": ["close", "high", "low"], "func": mdv_048_willr_gap_at_price_low_63d},
    "mdv_049_stoch_divg_count_252d": {"inputs": ["close", "high", "low"], "func": mdv_049_stoch_divg_count_252d},
    "mdv_050_willr_pctrank_spread_63d": {"inputs": ["close", "high", "low"], "func": mdv_050_willr_pctrank_spread_63d},
    "mdv_051_cci_divg_flag_21d": {"inputs": ["close", "high", "low"], "func": mdv_051_cci_divg_flag_21d},
    "mdv_052_cci_divg_flag_63d": {"inputs": ["close", "high", "low"], "func": mdv_052_cci_divg_flag_63d},
    "mdv_053_cci_gap_at_price_low_63d": {"inputs": ["close", "high", "low"], "func": mdv_053_cci_gap_at_price_low_63d},
    "mdv_054_cci_pctrank_spread_63d": {"inputs": ["close", "high", "low"], "func": mdv_054_cci_pctrank_spread_63d},
    "mdv_055_cci_pctrank_spread_252d": {"inputs": ["close", "high", "low"], "func": mdv_055_cci_pctrank_spread_252d},
    "mdv_056_cci_divg_count_252d": {"inputs": ["close", "high", "low"], "func": mdv_056_cci_divg_count_252d},
    "mdv_057_cci_divg_magnitude_63d": {"inputs": ["close", "high", "low"], "func": mdv_057_cci_divg_magnitude_63d},
    "mdv_058_cci14_divg_flag_63d": {"inputs": ["close", "high", "low"], "func": mdv_058_cci14_divg_flag_63d},
    "mdv_059_cci_gap_max_252d": {"inputs": ["close", "high", "low"], "func": mdv_059_cci_gap_max_252d},
    "mdv_060_cci_divg_flag_252d": {"inputs": ["close", "high", "low"], "func": mdv_060_cci_divg_flag_252d},
    "mdv_061_composite_divg_score_21d": {"inputs": ["close", "high", "low"], "func": mdv_061_composite_divg_score_21d},
    "mdv_062_composite_divg_score_63d": {"inputs": ["close", "high", "low"], "func": mdv_062_composite_divg_score_63d},
    "mdv_063_composite_divg_score_252d": {"inputs": ["close", "high", "low"], "func": mdv_063_composite_divg_score_252d},
    "mdv_064_pctrank_spread_avg_63d": {"inputs": ["close", "high", "low"], "func": mdv_064_pctrank_spread_avg_63d},
    "mdv_065_pctrank_spread_avg_252d": {"inputs": ["close", "high", "low"], "func": mdv_065_pctrank_spread_avg_252d},
    "mdv_066_composite_divg_count_252d": {"inputs": ["close", "high", "low"], "func": mdv_066_composite_divg_count_252d},
    "mdv_067_composite_pctrank_spread_pctrank_252d": {"inputs": ["close", "high", "low"], "func": mdv_067_composite_pctrank_spread_pctrank_252d},
    "mdv_068_divg_score_63d_pctrank_252d": {"inputs": ["close", "high", "low"], "func": mdv_068_divg_score_63d_pctrank_252d},
    "mdv_069_rsi_macd_divg_agree_63d": {"inputs": ["close"], "func": mdv_069_rsi_macd_divg_agree_63d},
    "mdv_070_three_indicator_divg_agree_63d": {"inputs": ["close", "high", "low"], "func": mdv_070_three_indicator_divg_agree_63d},
    "mdv_071_divg_score_21d_rolling_max_63d": {"inputs": ["close", "high", "low"], "func": mdv_071_divg_score_21d_rolling_max_63d},
    "mdv_072_divg_score_63d_rolling_max_252d": {"inputs": ["close", "high", "low"], "func": mdv_072_divg_score_63d_rolling_max_252d},
    "mdv_073_consecutive_price_lows_no_rsi_low_21d": {"inputs": ["close"], "func": mdv_073_consecutive_price_lows_no_rsi_low_21d},
    "mdv_074_consecutive_price_lows_no_macd_low_63d": {"inputs": ["close"], "func": mdv_074_consecutive_price_lows_no_macd_low_63d},
    "mdv_075_momentum_price_divergence_strength_score": {"inputs": ["close", "high", "low"], "func": mdv_075_momentum_price_divergence_strength_score},
}
