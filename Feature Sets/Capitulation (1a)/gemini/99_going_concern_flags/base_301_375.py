"""
99_99_going_concern_flags — Base Features 301-375
Domain: 99_going_concern_flags
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

def gcon_301_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 5)

def gcon_302_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 21)

def gcon_303_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 63)

def gcon_304_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 126)

def gcon_305_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 252)

def gcon_306_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 5))

def gcon_307_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 21))

def gcon_308_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 63))

def gcon_309_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 126))

def gcon_310_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 252))

def gcon_311_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gcon_312_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gcon_313_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gcon_314_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gcon_315_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gcon_316_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 5)

def gcon_317_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 21)

def gcon_318_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 63)

def gcon_319_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 126)

def gcon_320_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 252)

def gcon_321_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 5d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 5)

def gcon_322_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 21d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 21)

def gcon_323_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 63d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 63)

def gcon_324_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 126d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 126)

def gcon_325_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 252d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 252)

def gcon_326_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(liabs, equity)
    return _rank_pct(base, 5)

def gcon_327_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(liabs, equity)
    return _rank_pct(base, 21)

def gcon_328_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(liabs, equity)
    return _rank_pct(base, 63)

def gcon_329_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(liabs, equity)
    return _rank_pct(base, 126)

def gcon_330_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(liabs, equity)
    return _rank_pct(base, 252)

def gcon_331_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(liabs, equity)
    return _rolling_skew(base, 5)

def gcon_332_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(liabs, equity)
    return _rolling_skew(base, 21)

def gcon_333_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(liabs, equity)
    return _rolling_skew(base, 63)

def gcon_334_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(liabs, equity)
    return _rolling_skew(base, 126)

def gcon_335_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(liabs, equity)
    return _rolling_skew(base, 252)

def gcon_336_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(liabs, equity)
    return _rolling_kurt(base, 5)

def gcon_337_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(liabs, equity)
    return _rolling_kurt(base, 21)

def gcon_338_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(liabs, equity)
    return _rolling_kurt(base, 63)

def gcon_339_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(liabs, equity)
    return _rolling_kurt(base, 126)

def gcon_340_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(liabs, equity)
    return _rolling_kurt(base, 252)

def gcon_341_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(liabs, equity)
    return _safe_div(base, _rolling_std(base, 5))

def gcon_342_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(liabs, equity)
    return _safe_div(base, _rolling_std(base, 21))

def gcon_343_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(liabs, equity)
    return _safe_div(base, _rolling_std(base, 63))

def gcon_344_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(liabs, equity)
    return _safe_div(base, _rolling_std(base, 126))

def gcon_345_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(liabs, equity)
    return _safe_div(base, _rolling_std(base, 252))

def gcon_346_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(liabs, equity)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gcon_347_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(liabs, equity)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gcon_348_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(liabs, equity)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gcon_349_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(liabs, equity)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gcon_350_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(liabs, equity)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gcon_351_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 5)

def gcon_352_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 21)

def gcon_353_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 63)

def gcon_354_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 126)

def gcon_355_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 252)

def gcon_356_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 5d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 5)

def gcon_357_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 21d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 21)

def gcon_358_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 63d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 63)

def gcon_359_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 126d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 126)

def gcon_360_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 252d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 252)

def gcon_361_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 5)

def gcon_362_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 21)

def gcon_363_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 63)

def gcon_364_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 126)

def gcon_365_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 252)

def gcon_366_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 5)

def gcon_367_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 21)

def gcon_368_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 63)

def gcon_369_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 126)

def gcon_370_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 252)

def gcon_371_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 5)

def gcon_372_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 21)

def gcon_373_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 63)

def gcon_374_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 126)

def gcon_375_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 252)
