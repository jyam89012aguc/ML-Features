import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)



# ===== folder domain primitives =====
def _f50_quality_composite(roic, fcf, revenue, w):
    fcf_yield = fcf / revenue.replace(0, np.nan)
    return roic.rolling(w, min_periods=max(1, w // 2)).mean() + fcf_yield.rolling(w, min_periods=max(1, w // 2)).mean()


def _f50_low_vol_high_growth(closeadj, revenue, w):
    vol = closeadj.pct_change().rolling(w, min_periods=max(1, w // 2)).std()
    growth = revenue.pct_change(w)
    return growth / vol.replace(0, np.nan)


def _f50_idiosyncratic_alpha_score(roic, fcf, ebitdamargin, w):
    return (roic.rolling(w, min_periods=max(1, w // 2)).mean()
            + ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
            + (fcf / fcf.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan)) - 1.0)



def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn5_slope_v001_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct5_slope_v002_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_pct(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean5_slope_v003_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema5_slope_v004_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff5_slope_v005_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _diff(base, 5) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn10_slope_v006_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct10_slope_v007_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_pct(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean10_slope_v008_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema10_slope_v009_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff10_slope_v010_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _diff(base, 10) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn21_slope_v011_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct21_slope_v012_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_pct(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean21_slope_v013_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema21_slope_v014_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff21_slope_v015_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _diff(base, 21) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn42_slope_v016_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct42_slope_v017_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_pct(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean42_slope_v018_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema42_slope_v019_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff42_slope_v020_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _diff(base, 42) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn63_slope_v021_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct63_slope_v022_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_pct(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean63_slope_v023_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema63_slope_v024_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff63_slope_v025_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _diff(base, 63) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn126_slope_v026_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct126_slope_v027_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_pct(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean126_slope_v028_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema126_slope_v029_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _slope_diff_norm(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff126_slope_v030_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _diff(base, 126) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn5_slope_v031_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct5_slope_v032_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_pct(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean5_slope_v033_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema5_slope_v034_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff5_slope_v035_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _diff(base, 5) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn10_slope_v036_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct10_slope_v037_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_pct(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean10_slope_v038_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema10_slope_v039_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff10_slope_v040_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _diff(base, 10) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn21_slope_v041_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct21_slope_v042_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_pct(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean21_slope_v043_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema21_slope_v044_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff21_slope_v045_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _diff(base, 21) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn42_slope_v046_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct42_slope_v047_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_pct(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean42_slope_v048_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema42_slope_v049_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff42_slope_v050_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _diff(base, 42) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn63_slope_v051_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct63_slope_v052_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_pct(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean63_slope_v053_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema63_slope_v054_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff63_slope_v055_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _diff(base, 63) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn126_slope_v056_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct126_slope_v057_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_pct(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean126_slope_v058_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema126_slope_v059_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _slope_diff_norm(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff126_slope_v060_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _diff(base, 126) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn5_slope_v061_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct5_slope_v062_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_pct(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean5_slope_v063_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema5_slope_v064_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff5_slope_v065_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _diff(base, 5) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn10_slope_v066_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct10_slope_v067_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_pct(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean10_slope_v068_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema10_slope_v069_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff10_slope_v070_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _diff(base, 10) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn21_slope_v071_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct21_slope_v072_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_pct(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean21_slope_v073_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema21_slope_v074_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff21_slope_v075_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _diff(base, 21) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn42_slope_v076_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct42_slope_v077_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_pct(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean42_slope_v078_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema42_slope_v079_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff42_slope_v080_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _diff(base, 42) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn63_slope_v081_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct63_slope_v082_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_pct(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean63_slope_v083_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema63_slope_v084_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff63_slope_v085_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _diff(base, 63) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn126_slope_v086_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct126_slope_v087_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_pct(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean126_slope_v088_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema126_slope_v089_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _slope_diff_norm(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff126_slope_v090_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _diff(base, 126) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn5_slope_v091_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct5_slope_v092_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_pct(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean5_slope_v093_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema5_slope_v094_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff5_slope_v095_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _diff(base, 5) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn10_slope_v096_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct10_slope_v097_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_pct(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean10_slope_v098_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema10_slope_v099_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff10_slope_v100_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _diff(base, 10) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn21_slope_v101_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct21_slope_v102_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_pct(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean21_slope_v103_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema21_slope_v104_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff21_slope_v105_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _diff(base, 21) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn42_slope_v106_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct42_slope_v107_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_pct(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean42_slope_v108_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema42_slope_v109_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff42_slope_v110_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _diff(base, 42) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn63_slope_v111_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct63_slope_v112_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_pct(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean63_slope_v113_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema63_slope_v114_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff63_slope_v115_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _diff(base, 63) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn126_slope_v116_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct126_slope_v117_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_pct(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean126_slope_v118_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema126_slope_v119_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _slope_diff_norm(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff126_slope_v120_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _diff(base, 126) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn5_slope_v121_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct5_slope_v122_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_pct(base, 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean5_slope_v123_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(_mean(base, 5), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema5_slope_v124_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base.ewm(span=5, min_periods=2).mean(), 5)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff5_slope_v125_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _diff(base, 5) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn10_slope_v126_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct10_slope_v127_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_pct(base, 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean10_slope_v128_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(_mean(base, 10), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema10_slope_v129_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base.ewm(span=10, min_periods=2).mean(), 10)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff10_slope_v130_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _diff(base, 10) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn21_slope_v131_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct21_slope_v132_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_pct(base, 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean21_slope_v133_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(_mean(base, 21), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema21_slope_v134_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base.ewm(span=21, min_periods=2).mean(), 21)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff21_slope_v135_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _diff(base, 21) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn42_slope_v136_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct42_slope_v137_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_pct(base, 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean42_slope_v138_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(_mean(base, 42), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema42_slope_v139_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base.ewm(span=42, min_periods=2).mean(), 42)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff42_slope_v140_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _diff(base, 42) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn63_slope_v141_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct63_slope_v142_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_pct(base, 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean63_slope_v143_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(_mean(base, 63), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema63_slope_v144_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base.ewm(span=63, min_periods=2).mean(), 63)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff63_slope_v145_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _diff(base, 63) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn126_slope_v146_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct126_slope_v147_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_pct(base, 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean126_slope_v148_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(_mean(base, 126), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema126_slope_v149_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _slope_diff_norm(base.ewm(span=126, min_periods=2).mean(), 126)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff126_slope_v150_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 504)
    result = _diff(base, 126) / _mean(base.abs(), 252).replace(0, np.nan)
    result = result * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn5_slope_v001_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct5_slope_v002_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean5_slope_v003_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema5_slope_v004_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff5_slope_v005_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn10_slope_v006_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct10_slope_v007_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean10_slope_v008_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema10_slope_v009_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff10_slope_v010_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn21_slope_v011_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct21_slope_v012_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean21_slope_v013_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema21_slope_v014_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff21_slope_v015_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn42_slope_v016_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct42_slope_v017_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean42_slope_v018_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema42_slope_v019_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff42_slope_v020_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn63_slope_v021_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct63_slope_v022_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean63_slope_v023_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema63_slope_v024_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff63_slope_v025_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopedn126_slope_v026_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopepct126_slope_v027_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopemean126_slope_v028_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopeema126_slope_v029_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_21d_slopediff126_slope_v030_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn5_slope_v031_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct5_slope_v032_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean5_slope_v033_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema5_slope_v034_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff5_slope_v035_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn10_slope_v036_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct10_slope_v037_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean10_slope_v038_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema10_slope_v039_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff10_slope_v040_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn21_slope_v041_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct21_slope_v042_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean21_slope_v043_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema21_slope_v044_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff21_slope_v045_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn42_slope_v046_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct42_slope_v047_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean42_slope_v048_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema42_slope_v049_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff42_slope_v050_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn63_slope_v051_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct63_slope_v052_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean63_slope_v053_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema63_slope_v054_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff63_slope_v055_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopedn126_slope_v056_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopepct126_slope_v057_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopemean126_slope_v058_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopeema126_slope_v059_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_63d_slopediff126_slope_v060_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn5_slope_v061_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct5_slope_v062_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean5_slope_v063_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema5_slope_v064_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff5_slope_v065_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn10_slope_v066_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct10_slope_v067_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean10_slope_v068_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema10_slope_v069_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff10_slope_v070_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn21_slope_v071_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct21_slope_v072_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean21_slope_v073_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema21_slope_v074_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff21_slope_v075_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn42_slope_v076_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct42_slope_v077_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean42_slope_v078_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema42_slope_v079_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff42_slope_v080_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn63_slope_v081_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct63_slope_v082_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean63_slope_v083_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema63_slope_v084_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff63_slope_v085_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopedn126_slope_v086_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopepct126_slope_v087_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopemean126_slope_v088_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopeema126_slope_v089_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_126d_slopediff126_slope_v090_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn5_slope_v091_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct5_slope_v092_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean5_slope_v093_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema5_slope_v094_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff5_slope_v095_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn10_slope_v096_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct10_slope_v097_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean10_slope_v098_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema10_slope_v099_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff10_slope_v100_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn21_slope_v101_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct21_slope_v102_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean21_slope_v103_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema21_slope_v104_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff21_slope_v105_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn42_slope_v106_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct42_slope_v107_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean42_slope_v108_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema42_slope_v109_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff42_slope_v110_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn63_slope_v111_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct63_slope_v112_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean63_slope_v113_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema63_slope_v114_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff63_slope_v115_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopedn126_slope_v116_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopepct126_slope_v117_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopemean126_slope_v118_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopeema126_slope_v119_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_252d_slopediff126_slope_v120_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn5_slope_v121_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct5_slope_v122_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean5_slope_v123_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema5_slope_v124_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff5_slope_v125_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn10_slope_v126_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct10_slope_v127_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean10_slope_v128_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema10_slope_v129_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff10_slope_v130_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn21_slope_v131_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct21_slope_v132_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean21_slope_v133_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema21_slope_v134_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff21_slope_v135_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn42_slope_v136_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct42_slope_v137_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean42_slope_v138_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema42_slope_v139_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff42_slope_v140_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn63_slope_v141_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct63_slope_v142_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean63_slope_v143_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema63_slope_v144_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff63_slope_v145_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopedn126_slope_v146_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopepct126_slope_v147_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopemean126_slope_v148_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopeema126_slope_v149_signal,
    f50cda_f50_cd_idiosyncratic_alpha_qual_504d_slopediff126_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_CD_IDIOSYNCRATIC_ALPHA_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")

    cols = {"closeadj": closeadj, "fcf": fcf, "revenue": revenue, "roic": roic}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f50_quality_composite", "_f50_low_vol_high_growth", "_f50_idiosyncratic_alpha_score")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f50_cd_idiosyncratic_alpha_2nd_derivatives_001_150_claude: {n_features} features pass")
