# f26_accumulation_distribution_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _mf_mult(h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    return ((c - l) - (h - c)) / (h - l).abs().replace(0, np.nan)

def _mf_vol(mult: pd.Series, v: pd.Series) -> pd.Series:
    return mult * v

def _ad_osc(mfv: pd.Series, w: int) -> pd.Series:
    return mfv.rolling(w).sum() / mfv.rolling(w).std().abs().replace(0, np.nan)

def _sma(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _zscore(s: pd.Series, w: int) -> pd.Series:
    return (s - _sma(s, w)) / s.rolling(w, min_periods=min(w, 5)).std().replace(0, np.nan)

# Accumulation Distribution Persistence (Fraction of Positive MF) 5d
def f26ad_accumulation_distribution_persistence_5d_v076_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(5).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 10d
def f26ad_accumulation_distribution_persistence_10d_v077_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(10).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 21d
def f26ad_accumulation_distribution_persistence_21d_v078_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(21).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 42d
def f26ad_accumulation_distribution_persistence_42d_v079_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(42).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 63d
def f26ad_accumulation_distribution_persistence_63d_v080_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(63).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 84d
def f26ad_accumulation_distribution_persistence_84d_v081_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(84).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 126d
def f26ad_accumulation_distribution_persistence_126d_v082_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(126).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 168d
def f26ad_accumulation_distribution_persistence_168d_v083_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(168).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 252d
def f26ad_accumulation_distribution_persistence_252d_v084_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(252).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 336d
def f26ad_accumulation_distribution_persistence_336d_v085_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(336).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 504d
def f26ad_accumulation_distribution_persistence_504d_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(504).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 756d
def f26ad_accumulation_distribution_persistence_756d_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    res = (mult > 0).rolling(756).mean()
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Persistence (Fraction of Positive MF) 5d
# Accumulation Distribution Persistence (Fraction of Positive MF) 10d
# Accumulation Distribution Persistence (Fraction of Positive MF) 21d
# Accumulation Distribution Persistence (Fraction of Positive MF) 42d
# Accumulation Distribution Persistence (Fraction of Positive MF) 63d
# Accumulation Distribution Persistence (Fraction of Positive MF) 84d
# Accumulation Distribution Persistence (Fraction of Positive MF) 126d
# Accumulation Distribution Persistence (Fraction of Positive MF) 168d
# Divergence: AD Oscillator 5d trend minus Price trend
def f26ad_accumulation_distribution_divergence_5d_v096_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 5)
    res = osc.pct_change(5) - close.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 10d trend minus Price trend
def f26ad_accumulation_distribution_divergence_10d_v097_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 10)
    res = osc.pct_change(10) - close.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 21d trend minus Price trend
def f26ad_accumulation_distribution_divergence_21d_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 21)
    res = osc.pct_change(21) - close.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 42d trend minus Price trend
def f26ad_accumulation_distribution_divergence_42d_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 42)
    res = osc.pct_change(42) - close.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 63d trend minus Price trend
def f26ad_accumulation_distribution_divergence_63d_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 63)
    res = osc.pct_change(63) - close.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 84d trend minus Price trend
def f26ad_accumulation_distribution_divergence_84d_v101_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 84)
    res = osc.pct_change(84) - close.pct_change(84)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 126d trend minus Price trend
def f26ad_accumulation_distribution_divergence_126d_v102_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 126)
    res = osc.pct_change(126) - close.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 168d trend minus Price trend
def f26ad_accumulation_distribution_divergence_168d_v103_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 168)
    res = osc.pct_change(168) - close.pct_change(168)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 252d trend minus Price trend
def f26ad_accumulation_distribution_divergence_252d_v104_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 252)
    res = osc.pct_change(252) - close.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 336d trend minus Price trend
def f26ad_accumulation_distribution_divergence_336d_v105_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 336)
    res = osc.pct_change(336) - close.pct_change(336)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 504d trend minus Price trend
def f26ad_accumulation_distribution_divergence_504d_v106_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 504)
    res = osc.pct_change(504) - close.pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 756d trend minus Price trend
def f26ad_accumulation_distribution_divergence_756d_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 756)
    res = osc.pct_change(756) - close.pct_change(756)
    return res.replace([np.inf, -np.inf], np.nan)
# Divergence: AD Oscillator 5d trend minus Price trend
# Divergence: AD Oscillator 10d trend minus Price trend
# Divergence: AD Oscillator 21d trend minus Price trend
# Divergence: AD Oscillator 42d trend minus Price trend
# Divergence: AD Oscillator 63d trend minus Price trend
# Divergence: AD Oscillator 84d trend minus Price trend
# Divergence: AD Oscillator 126d trend minus Price trend
# Divergence: AD Oscillator 168d trend minus Price trend
# Accumulation Distribution Volatility 5d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_5d_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 5)
    res = osc.rolling(5).std() / osc.rolling(5).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 10d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_10d_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 10)
    res = osc.rolling(10).std() / osc.rolling(10).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 21d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_21d_v118_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 21)
    res = osc.rolling(21).std() / osc.rolling(21).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 42d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_42d_v119_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 42)
    res = osc.rolling(42).std() / osc.rolling(42).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 63d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_63d_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 63)
    res = osc.rolling(63).std() / osc.rolling(63).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 84d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_84d_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 84)
    res = osc.rolling(84).std() / osc.rolling(84).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 126d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_126d_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 126)
    res = osc.rolling(126).std() / osc.rolling(126).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 168d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_168d_v123_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 168)
    res = osc.rolling(168).std() / osc.rolling(168).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 252d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_252d_v124_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 252)
    res = osc.rolling(252).std() / osc.rolling(252).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 336d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_336d_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 336)
    res = osc.rolling(336).std() / osc.rolling(336).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 504d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_504d_v126_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 504)
    res = osc.rolling(504).std() / osc.rolling(504).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 756d (Rolling Std of AD Osc)
def f26ad_accumulation_distribution_volatility_756d_v127_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 756)
    res = osc.rolling(756).std() / osc.rolling(756).mean().abs().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Volatility 5d (Rolling Std of AD Osc)
# Accumulation Distribution Volatility 10d (Rolling Std of AD Osc)
# Accumulation Distribution Volatility 21d (Rolling Std of AD Osc)
# Accumulation Distribution Volatility 42d (Rolling Std of AD Osc)
# Accumulation Distribution Volatility 63d (Rolling Std of AD Osc)
# Accumulation Distribution Volatility 84d (Rolling Std of AD Osc)
# Accumulation Distribution Volatility 126d (Rolling Std of AD Osc)
# Accumulation Distribution Volatility 168d (Rolling Std of AD Osc)
# Accumulation Distribution Rank 5d
def f26ad_accumulation_distribution_rank_5d_v136_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 5)
    res = osc.rolling(5).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 10d
def f26ad_accumulation_distribution_rank_10d_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 10)
    res = osc.rolling(10).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 21d
def f26ad_accumulation_distribution_rank_21d_v138_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 21)
    res = osc.rolling(21).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 42d
def f26ad_accumulation_distribution_rank_42d_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 42)
    res = osc.rolling(42).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 63d
def f26ad_accumulation_distribution_rank_63d_v140_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 63)
    res = osc.rolling(63).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 84d
def f26ad_accumulation_distribution_rank_84d_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 84)
    res = osc.rolling(84).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 126d
def f26ad_accumulation_distribution_rank_126d_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 126)
    res = osc.rolling(126).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 168d
def f26ad_accumulation_distribution_rank_168d_v143_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 168)
    res = osc.rolling(168).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 252d
def f26ad_accumulation_distribution_rank_252d_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 252)
    res = osc.rolling(252).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 336d
def f26ad_accumulation_distribution_rank_336d_v145_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 336)
    res = osc.rolling(336).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 504d
def f26ad_accumulation_distribution_rank_504d_v146_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 504)
    res = osc.rolling(504).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 756d
def f26ad_accumulation_distribution_rank_756d_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    mult = _mf_mult(high, low, close)
    mfv = _mf_vol(mult, volume)
    osc = _ad_osc(mfv, 756)
    res = osc.rolling(756).rank(pct=True)
    return res.replace([np.inf, -np.inf], np.nan)
# Accumulation Distribution Rank 5d
# Accumulation Distribution Rank 10d
# Accumulation Distribution Rank 21d
SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low", "volume"]}

BASE_NAMES = [f for f in globals() if f.startswith("f26ad_") and f.endswith("_signal")]

F26_ACCUMULATION_DISTRIBUTION_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "volume": np.random.randint(100, 1000, sz).astype(float), "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F26_ACCUMULATION_DISTRIBUTION_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
