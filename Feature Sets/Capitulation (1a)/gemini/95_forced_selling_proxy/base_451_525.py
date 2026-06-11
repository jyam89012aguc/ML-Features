"""
95_95_forced_selling_proxy — Base Features 451-525
Domain: 95_forced_selling_proxy
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).skew().fillna(0)

def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).kurt().fillna(0)

# ── Feature functions ────────────────────────────────────────────────────────

def fsel_451_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value - inst_sell_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fsel_452_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value - inst_sell_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fsel_453_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value - inst_sell_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fsel_454_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value - inst_sell_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fsel_455_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value - inst_sell_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fsel_456_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 5d horizon to identify extreme regimes.
    """
    base = holder_count
    return _rolling_mean(base, 5)

def fsel_457_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 21d horizon to identify extreme regimes.
    """
    base = holder_count
    return _rolling_mean(base, 21)

def fsel_458_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 63d horizon to identify extreme regimes.
    """
    base = holder_count
    return _rolling_mean(base, 63)

def fsel_459_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 126d horizon to identify extreme regimes.
    """
    base = holder_count
    return _rolling_mean(base, 126)

def fsel_460_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 252d horizon to identify extreme regimes.
    """
    base = holder_count
    return _rolling_mean(base, 252)

def fsel_461_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 5d mean.
    """
    base = holder_count
    return _zscore_rolling(base, 5)

def fsel_462_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 21d mean.
    """
    base = holder_count
    return _zscore_rolling(base, 21)

def fsel_463_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 63d mean.
    """
    base = holder_count
    return _zscore_rolling(base, 63)

def fsel_464_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 126d mean.
    """
    base = holder_count
    return _zscore_rolling(base, 126)

def fsel_465_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 252d mean.
    """
    base = holder_count
    return _zscore_rolling(base, 252)

def fsel_466_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = holder_count
    return _rank_pct(base, 5)

def fsel_467_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = holder_count
    return _rank_pct(base, 21)

def fsel_468_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = holder_count
    return _rank_pct(base, 63)

def fsel_469_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = holder_count
    return _rank_pct(base, 126)

def fsel_470_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = holder_count
    return _rank_pct(base, 252)

def fsel_471_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = holder_count
    return _rolling_skew(base, 5)

def fsel_472_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = holder_count
    return _rolling_skew(base, 21)

def fsel_473_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = holder_count
    return _rolling_skew(base, 63)

def fsel_474_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = holder_count
    return _rolling_skew(base, 126)

def fsel_475_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = holder_count
    return _rolling_skew(base, 252)

def fsel_476_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = holder_count
    return _rolling_kurt(base, 5)

def fsel_477_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = holder_count
    return _rolling_kurt(base, 21)

def fsel_478_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = holder_count
    return _rolling_kurt(base, 63)

def fsel_479_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = holder_count
    return _rolling_kurt(base, 126)

def fsel_480_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = holder_count
    return _rolling_kurt(base, 252)

def fsel_481_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count
    return _safe_div(base, _rolling_std(base, 5))

def fsel_482_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count
    return _safe_div(base, _rolling_std(base, 21))

def fsel_483_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count
    return _safe_div(base, _rolling_std(base, 63))

def fsel_484_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count
    return _safe_div(base, _rolling_std(base, 126))

def fsel_485_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count
    return _safe_div(base, _rolling_std(base, 252))

def fsel_486_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = holder_count
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fsel_487_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = holder_count
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fsel_488_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = holder_count
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fsel_489_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = holder_count
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fsel_490_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = holder_count
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fsel_491_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 5d horizon to identify extreme regimes.
    """
    base = inst_shares_held
    return _rolling_mean(base, 5)

def fsel_492_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 21d horizon to identify extreme regimes.
    """
    base = inst_shares_held
    return _rolling_mean(base, 21)

def fsel_493_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 63d horizon to identify extreme regimes.
    """
    base = inst_shares_held
    return _rolling_mean(base, 63)

def fsel_494_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 126d horizon to identify extreme regimes.
    """
    base = inst_shares_held
    return _rolling_mean(base, 126)

def fsel_495_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 252d horizon to identify extreme regimes.
    """
    base = inst_shares_held
    return _rolling_mean(base, 252)

def fsel_496_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 5d mean.
    """
    base = inst_shares_held
    return _zscore_rolling(base, 5)

def fsel_497_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 21d mean.
    """
    base = inst_shares_held
    return _zscore_rolling(base, 21)

def fsel_498_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 63d mean.
    """
    base = inst_shares_held
    return _zscore_rolling(base, 63)

def fsel_499_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 126d mean.
    """
    base = inst_shares_held
    return _zscore_rolling(base, 126)

def fsel_500_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 252d mean.
    """
    base = inst_shares_held
    return _zscore_rolling(base, 252)

def fsel_501_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 5)

def fsel_502_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 21)

def fsel_503_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 63)

def fsel_504_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 126)

def fsel_505_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 252)

def fsel_506_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 5)

def fsel_507_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 21)

def fsel_508_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 63)

def fsel_509_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 126)

def fsel_510_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 252)

def fsel_511_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 5)

def fsel_512_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 21)

def fsel_513_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 63)

def fsel_514_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 126)

def fsel_515_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 252)

def fsel_516_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 5))

def fsel_517_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 21))

def fsel_518_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 63))

def fsel_519_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 126))

def fsel_520_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 252))

def fsel_521_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fsel_522_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fsel_523_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fsel_524_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fsel_525_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
