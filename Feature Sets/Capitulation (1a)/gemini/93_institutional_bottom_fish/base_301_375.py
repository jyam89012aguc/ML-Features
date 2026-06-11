"""
93_93_institutional_bottom_fish — Base Features 301-375
Domain: 93_institutional_bottom_fish
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

def ibf_301_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 5)

def ibf_302_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 21)

def ibf_303_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 63)

def ibf_304_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 126)

def ibf_305_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = holder_count.diff(21).abs()
    return _rolling_kurt(base, 252)

def ibf_306_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 5))

def ibf_307_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 21))

def ibf_308_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 63))

def ibf_309_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 126))

def ibf_310_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = holder_count.diff(21).abs()
    return _safe_div(base, _rolling_std(base, 252))

def ibf_311_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 5d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibf_312_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 21d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibf_313_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 63d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibf_314_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 126d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibf_315_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 252d to stabilize variance and capture exponential shifts.
    """
    base = holder_count.diff(21).abs()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibf_316_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 5)

def ibf_317_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 21)

def ibf_318_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 63)

def ibf_319_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 126)

def ibf_320_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_mean(base, 252)

def ibf_321_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 5d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 5)

def ibf_322_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 21d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 21)

def ibf_323_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 63d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 63)

def ibf_324_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 126d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 126)

def ibf_325_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 252d mean.
    """
    base = inst_buy_value + inst_sell_value
    return _zscore_rolling(base, 252)

def ibf_326_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_buy_value + inst_sell_value
    return _rank_pct(base, 5)

def ibf_327_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_buy_value + inst_sell_value
    return _rank_pct(base, 21)

def ibf_328_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_buy_value + inst_sell_value
    return _rank_pct(base, 63)

def ibf_329_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_buy_value + inst_sell_value
    return _rank_pct(base, 126)

def ibf_330_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_buy_value + inst_sell_value
    return _rank_pct(base, 252)

def ibf_331_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_skew(base, 5)

def ibf_332_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_skew(base, 21)

def ibf_333_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_skew(base, 63)

def ibf_334_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_skew(base, 126)

def ibf_335_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_skew(base, 252)

def ibf_336_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_kurt(base, 5)

def ibf_337_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_kurt(base, 21)

def ibf_338_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_kurt(base, 63)

def ibf_339_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_kurt(base, 126)

def ibf_340_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value + inst_sell_value
    return _rolling_kurt(base, 252)

def ibf_341_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value + inst_sell_value
    return _safe_div(base, _rolling_std(base, 5))

def ibf_342_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value + inst_sell_value
    return _safe_div(base, _rolling_std(base, 21))

def ibf_343_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value + inst_sell_value
    return _safe_div(base, _rolling_std(base, 63))

def ibf_344_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value + inst_sell_value
    return _safe_div(base, _rolling_std(base, 126))

def ibf_345_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 93 institutional bottom fish for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_buy_value + inst_sell_value
    return _safe_div(base, _rolling_std(base, 252))

def ibf_346_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value + inst_sell_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ibf_347_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value + inst_sell_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ibf_348_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value + inst_sell_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ibf_349_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value + inst_sell_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ibf_350_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 93 institutional bottom fish over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_buy_value + inst_sell_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ibf_351_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 5d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 5)

def ibf_352_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 21d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 21)

def ibf_353_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 63d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 63)

def ibf_354_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 126d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 126)

def ibf_355_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 93 institutional bottom fish over a 252d horizon to identify extreme regimes.
    """
    base = inst_buy_value
    return _rolling_mean(base, 252)

def ibf_356_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 5d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 5)

def ibf_357_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 21d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 21)

def ibf_358_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 63d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 63)

def ibf_359_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 126d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 126)

def ibf_360_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 93 institutional bottom fish by measuring deviations from the 252d mean.
    """
    base = inst_buy_value
    return _zscore_rolling(base, 252)

def ibf_361_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 5)

def ibf_362_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 21)

def ibf_363_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 63)

def ibf_364_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 126)

def ibf_365_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 93 institutional bottom fish to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_buy_value
    return _rank_pct(base, 252)

def ibf_366_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 5)

def ibf_367_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 21)

def ibf_368_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 63)

def ibf_369_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 126)

def ibf_370_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 93 institutional bottom fish distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_buy_value
    return _rolling_skew(base, 252)

def ibf_371_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 5)

def ibf_372_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 21)

def ibf_373_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 63)

def ibf_374_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 126)

def ibf_375_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 93 institutional bottom fish over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_buy_value
    return _rolling_kurt(base, 252)
