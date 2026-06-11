"""dilution_structure_snapshot base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Theme: SNAPSHOT of the equity-issuance / dilution structure at the peak.
sharesbas (basic shares outstanding), shareswa (weighted-avg basic),
shareswadil (weighted-avg diluted), and sharefactor (split adjustment).
Captures long-horizon dilution trajectories, dilution overhang
(diluted − basic), and split/reverse-split events. Continued in
__base__076_150.py for 150 total. PIT-clean: right-anchored rolling,
explicit min_periods, no centered windows, no .shift(-N).
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_3Y = 756
DDAYS_5Y = 1260


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _r(w):
        if np.isnan(w).any():
            return np.nan
        return (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
    return s.rolling(window, min_periods=min_periods).apply(_r, raw=True)


def _days_since_max(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)


def _streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag_series.rolling(window, min_periods=min_periods).apply(_streak, raw=True)


def _recency_since_event(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flag_series.rolling(window, min_periods=min_periods).apply(_r, raw=True)


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


# ============================================================
#                  FEATURES 001-075
# ============================================================

def f19_dssp_001_sharesbas_zscore_252d(sharesbas: pd.Series) -> pd.Series:
    """Z-score of basic-shares-outstanding vs 252d — annual extremity of share count."""
    return _rolling_zscore(sharesbas, YDAYS)


def f19_dssp_002_sharesbas_zscore_63d(sharesbas: pd.Series) -> pd.Series:
    """Z-score of basic-shares-outstanding vs 63d — quarterly extremity."""
    return _rolling_zscore(sharesbas, QDAYS)


def f19_dssp_003_sharesbas_log_diff_21d(sharesbas: pd.Series) -> pd.Series:
    """21d log change of basic shares — monthly raw issuance thrust."""
    return _safe_log(sharesbas).diff(MDAYS)


def f19_dssp_004_sharesbas_log_diff_63d(sharesbas: pd.Series) -> pd.Series:
    """63d log change of basic shares — quarterly raw issuance thrust."""
    return _safe_log(sharesbas).diff(QDAYS)


def f19_dssp_005_sharesbas_log_diff_252d(sharesbas: pd.Series) -> pd.Series:
    """1y log change of basic shares — annual raw issuance."""
    return _safe_log(sharesbas).diff(YDAYS)


def f19_dssp_006_sharesbas_log_diff_756d(sharesbas: pd.Series) -> pd.Series:
    """3y log change of basic shares — cumulative 3y issuance (not split-adjusted)."""
    return _safe_log(sharesbas).diff(DDAYS_3Y)


def f19_dssp_007_sharesbas_log_diff_1260d(sharesbas: pd.Series) -> pd.Series:
    """5y log change of basic shares — cumulative 5y issuance (not split-adjusted)."""
    return _safe_log(sharesbas).diff(DDAYS_5Y)


def f19_dssp_008_sharesbas_pct_change_21d(sharesbas: pd.Series) -> pd.Series:
    """21d percent change of basic shares."""
    return _safe_div(sharesbas - sharesbas.shift(MDAYS), sharesbas.shift(MDAYS))


def f19_dssp_009_sharesbas_pct_change_63d(sharesbas: pd.Series) -> pd.Series:
    """63d percent change of basic shares."""
    return _safe_div(sharesbas - sharesbas.shift(QDAYS), sharesbas.shift(QDAYS))


def f19_dssp_010_sharesbas_pct_change_252d(sharesbas: pd.Series) -> pd.Series:
    """1y percent change of basic shares."""
    return _safe_div(sharesbas - sharesbas.shift(YDAYS), sharesbas.shift(YDAYS))


def f19_dssp_011_sharesbas_rank_pct_252d(sharesbas: pd.Series) -> pd.Series:
    """Percentile rank of basic shares vs 252d."""
    return _rolling_rank_pct(sharesbas, YDAYS)


def f19_dssp_012_sharesbas_distance_to_252d_max_log(sharesbas: pd.Series) -> pd.Series:
    """log(current / 252d-rolling-max) of basic shares — distance below yearly max (≤0)."""
    mx = sharesbas.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_log(sharesbas) - _safe_log(mx)


def f19_dssp_013_days_since_sharesbas_max_252d(sharesbas: pd.Series) -> pd.Series:
    """Bars since the 252d-rolling max of basic shares — recency of yearly issuance high."""
    return _days_since_max(sharesbas, YDAYS)


def f19_dssp_014_days_since_sharesbas_max_756d(sharesbas: pd.Series) -> pd.Series:
    """Bars since the 3y-rolling max of basic shares."""
    return _days_since_max(sharesbas, DDAYS_3Y)


def f19_dssp_015_sharesbas_at_yearly_max_indicator(sharesbas: pd.Series) -> pd.Series:
    """1 if sharesbas equals 252d rolling max (1e-6 tolerance), else 0 — at-the-peak issuance."""
    mx = sharesbas.rolling(YDAYS, min_periods=QDAYS).max()
    return ((sharesbas >= mx - 1e-6) & sharesbas.notna() & mx.notna()).astype(float)


def f19_dssp_016_sharesbas_streak_above_long_mean_252d(sharesbas: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where sharesbas > 252d mean — sustained-elevated regime."""
    m = sharesbas.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (sharesbas > m).astype(int)
    return _streak_above_zero(flag, YDAYS)


def f19_dssp_017_sharesbas_above_p90_count_63d(sharesbas: pd.Series) -> pd.Series:
    """Bars in last 63d where sharesbas > trailing-252d p90."""
    thr = sharesbas.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (sharesbas >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f19_dssp_018_sharesbas_above_p99_count_252d(sharesbas: pd.Series) -> pd.Series:
    """Bars in last 252d where sharesbas > trailing-252d p99 — annual tail recurrence."""
    thr = sharesbas.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    flag = (sharesbas >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f19_dssp_019_sharesbas_acceleration_21d(sharesbas: pd.Series) -> pd.Series:
    """Second 21d log change of sharesbas — acceleration of issuance pace."""
    return _safe_log(sharesbas).diff(MDAYS).diff(MDAYS)


def f19_dssp_020_sharesbas_acceleration_63d(sharesbas: pd.Series) -> pd.Series:
    """Second 63d log change of sharesbas — quarterly acceleration of issuance."""
    return _safe_log(sharesbas).diff(QDAYS).diff(QDAYS)


def f19_dssp_021_sharesbas_sma_5_to_sma_252(sharesbas: pd.Series) -> pd.Series:
    """SMA(5)/SMA(252) of sharesbas — short vs annual ratio."""
    s5 = sharesbas.rolling(WDAYS, min_periods=2).mean()
    s252 = sharesbas.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s5, s252)


def f19_dssp_022_sharesbas_sma_21_to_sma_252(sharesbas: pd.Series) -> pd.Series:
    """SMA(21)/SMA(252) of sharesbas — monthly vs annual amplification."""
    s21 = sharesbas.rolling(MDAYS, min_periods=WDAYS).mean()
    s252 = sharesbas.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s21, s252)


def f19_dssp_023_sharesbas_sma_63_to_sma_252(sharesbas: pd.Series) -> pd.Series:
    """SMA(63)/SMA(252) of sharesbas — quarterly vs annual amplification."""
    s63 = sharesbas.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = sharesbas.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s63, s252)


def f19_dssp_024_sharesbas_sma_5_to_sma_63(sharesbas: pd.Series) -> pd.Series:
    """SMA(5)/SMA(63) of sharesbas — short vs quarterly amplification."""
    s5 = sharesbas.rolling(WDAYS, min_periods=2).mean()
    s63 = sharesbas.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(s5, s63)


def f19_dssp_025_sharesbas_ema_log_diff_speed(sharesbas: pd.Series) -> pd.Series:
    """log(EMA-5 sharesbas) − log(EMA-63 sharesbas) — exponential-smoothing speed measure."""
    e5 = _ema(sharesbas, WDAYS)
    e63 = _ema(sharesbas, QDAYS)
    return _safe_log(e5) - _safe_log(e63)


def f19_dssp_026_shareswadil_zscore_252d(shareswadil: pd.Series) -> pd.Series:
    """Z-score of weighted-avg DILUTED shares vs 252d."""
    return _rolling_zscore(shareswadil, YDAYS)


def f19_dssp_027_shareswadil_log_diff_21d(shareswadil: pd.Series) -> pd.Series:
    """21d log change of weighted-avg DILUTED shares — monthly diluted thrust."""
    return _safe_log(shareswadil).diff(MDAYS)


def f19_dssp_028_shareswadil_log_diff_63d(shareswadil: pd.Series) -> pd.Series:
    """63d log change of weighted-avg DILUTED shares — quarterly diluted thrust."""
    return _safe_log(shareswadil).diff(QDAYS)


def f19_dssp_029_shareswadil_log_diff_252d(shareswadil: pd.Series) -> pd.Series:
    """1y log change of weighted-avg DILUTED shares."""
    return _safe_log(shareswadil).diff(YDAYS)


def f19_dssp_030_shareswadil_log_diff_756d(shareswadil: pd.Series) -> pd.Series:
    """3y log change of weighted-avg DILUTED shares."""
    return _safe_log(shareswadil).diff(DDAYS_3Y)


def f19_dssp_031_shareswadil_minus_shareswa_level(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Raw (diluted − basic) weighted-avg share count — dilutive instruments overhang."""
    return shareswadil - shareswa


def f19_dssp_032_shareswadil_minus_shareswa_pct_of_shareswa(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """(diluted − basic) / basic — dilutive overhang as % of basic share count."""
    return _safe_div(shareswadil - shareswa, shareswa)


def f19_dssp_033_shareswadil_minus_shareswa_log_diff_63d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """63d log change of dilutive overhang — quarterly overhang thrust."""
    return _safe_log(shareswadil - shareswa).diff(QDAYS)


def f19_dssp_034_shareswadil_minus_shareswa_log_diff_252d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """1y log change of dilutive overhang — annual overhang thrust."""
    return _safe_log(shareswadil - shareswa).diff(YDAYS)


def f19_dssp_035_shareswadil_minus_shareswa_zscore_252d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Z-score of (diluted − basic) overhang vs 252d."""
    return _rolling_zscore(shareswadil - shareswa, YDAYS)


def f19_dssp_036_shareswadil_minus_shareswa_rank_pct_252d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Percentile rank of dilutive overhang vs 252d."""
    return _rolling_rank_pct(shareswadil - shareswa, YDAYS)


def f19_dssp_037_shareswadil_minus_shareswa_log_diff_21d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """21d log change of dilutive overhang — monthly overhang thrust."""
    return _safe_log(shareswadil - shareswa).diff(MDAYS)


def f19_dssp_038_shareswadil_minus_shareswa_top_decile_count_252d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Bars in last 252d where overhang in trailing-252d top decile."""
    over = shareswadil - shareswa
    thr = over.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (over >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f19_dssp_039_dilution_overhang_above_5pct_count_252d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Bars in last 252d where overhang / basic >= 5% — material-overhang persistence."""
    ratio = _safe_div(shareswadil - shareswa, shareswa)
    flag = (ratio >= 0.05).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f19_dssp_040_dilution_overhang_acceleration_21d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Second 21d log change of overhang — monthly acceleration of overhang."""
    return _safe_log(shareswadil - shareswa).diff(MDAYS).diff(MDAYS)


def f19_dssp_041_dilution_overhang_acceleration_63d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Second 63d log change of overhang — quarterly acceleration."""
    return _safe_log(shareswadil - shareswa).diff(QDAYS).diff(QDAYS)


def f19_dssp_042_dilution_overhang_p90_count_63d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Bars in last 63d where overhang in trailing-252d top decile."""
    over = shareswadil - shareswa
    thr = over.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (over >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f19_dssp_043_days_since_dilution_overhang_max_252d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Bars since 252d-rolling max of overhang."""
    return _days_since_max(shareswadil - shareswa, YDAYS)


def f19_dssp_044_dilution_overhang_streak_above_long_mean(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of overhang > 252d mean — sustained elevated overhang."""
    over = shareswadil - shareswa
    m = over.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (over > m).astype(int)
    return _streak_above_zero(flag, YDAYS)


def f19_dssp_045_dilution_overhang_zscore_change_63d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """63d Δ of overhang z-score (vs 252d) — z-shift over quarter."""
    z = _rolling_zscore(shareswadil - shareswa, YDAYS)
    return z.diff(QDAYS)


def f19_dssp_046_dilution_overhang_pct_above_long_baseline_63d(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Fraction of 63d bars where overhang > 252d mean — persistence above baseline."""
    over = shareswadil - shareswa
    m = over.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (over > m).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean()


def f19_dssp_047_shareswadil_vs_sharesbas_ratio(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """shareswadil / sharesbas — diluted weighted-avg vs current basic-outstanding ratio."""
    return _safe_div(shareswadil, sharesbas)


def f19_dssp_048_shareswadil_vs_sharesbas_log_diff_21d(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """21d log Δ in shareswadil/sharesbas ratio."""
    return (_safe_log(shareswadil) - _safe_log(sharesbas)).diff(MDAYS)


def f19_dssp_049_shareswadil_vs_sharesbas_log_diff_63d(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """63d log Δ in shareswadil/sharesbas ratio."""
    return (_safe_log(shareswadil) - _safe_log(sharesbas)).diff(QDAYS)


def f19_dssp_050_shareswadil_vs_sharesbas_above_p90_count_63d(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Bars in last 63d where shareswadil/sharesbas ratio in trailing-252d top decile."""
    r = _safe_div(shareswadil, sharesbas)
    thr = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (r >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f19_dssp_051_shareswa_zscore_252d(shareswa: pd.Series) -> pd.Series:
    """Z-score of weighted-avg BASIC shares vs 252d."""
    return _rolling_zscore(shareswa, YDAYS)


def f19_dssp_052_shareswa_log_diff_21d(shareswa: pd.Series) -> pd.Series:
    """21d log change of weighted-avg basic shares."""
    return _safe_log(shareswa).diff(MDAYS)


def f19_dssp_053_shareswa_log_diff_63d(shareswa: pd.Series) -> pd.Series:
    """63d log change of weighted-avg basic shares."""
    return _safe_log(shareswa).diff(QDAYS)


def f19_dssp_054_shareswa_log_diff_252d(shareswa: pd.Series) -> pd.Series:
    """1y log change of weighted-avg basic shares."""
    return _safe_log(shareswa).diff(YDAYS)


def f19_dssp_055_shareswa_log_diff_756d(shareswa: pd.Series) -> pd.Series:
    """3y log change of weighted-avg basic shares."""
    return _safe_log(shareswa).diff(DDAYS_3Y)


def f19_dssp_056_shareswa_vs_sharesbas_ratio(shareswa: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """shareswa / sharesbas — weighted-avg vs end-of-period count (issuance pace within period)."""
    return _safe_div(shareswa, sharesbas)


def f19_dssp_057_shareswa_vs_sharesbas_log_diff_63d(shareswa: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """63d log Δ in shareswa/sharesbas ratio — issuance-pace gap shift."""
    return (_safe_log(shareswa) - _safe_log(sharesbas)).diff(QDAYS)


def f19_dssp_058_shareswa_vs_sharesbas_log_diff_252d(shareswa: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """1y log Δ in shareswa/sharesbas ratio."""
    return (_safe_log(shareswa) - _safe_log(sharesbas)).diff(YDAYS)


def f19_dssp_059_shareswa_pct_change_252d(shareswa: pd.Series) -> pd.Series:
    """1y percent change of shareswa."""
    return _safe_div(shareswa - shareswa.shift(YDAYS), shareswa.shift(YDAYS))


def f19_dssp_060_shareswa_rank_pct_252d(shareswa: pd.Series) -> pd.Series:
    """Percentile rank of shareswa in 252d."""
    return _rolling_rank_pct(shareswa, YDAYS)


def f19_dssp_061_shareswa_distance_to_252d_max_log(shareswa: pd.Series) -> pd.Series:
    """log(current / 252d max) of shareswa."""
    mx = shareswa.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_log(shareswa) - _safe_log(mx)


def f19_dssp_062_shareswa_acceleration_21d(shareswa: pd.Series) -> pd.Series:
    """Second 21d log change of shareswa — monthly acceleration."""
    return _safe_log(shareswa).diff(MDAYS).diff(MDAYS)


def f19_dssp_063_shareswa_acceleration_63d(shareswa: pd.Series) -> pd.Series:
    """Second 63d log change of shareswa — quarterly acceleration."""
    return _safe_log(shareswa).diff(QDAYS).diff(QDAYS)


def f19_dssp_064_shareswa_quarterly_step_change_indicator_252d(shareswa: pd.Series) -> pd.Series:
    """Count over 252d where |21d log change of shareswa| > trailing-252d p90 — large quarterly step events."""
    d = _safe_log(shareswa).diff(MDAYS).abs()
    thr = d.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (d >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f19_dssp_065_days_since_shareswa_max_252d(shareswa: pd.Series) -> pd.Series:
    """Bars since 252d-rolling max of shareswa."""
    return _days_since_max(shareswa, YDAYS)


def f19_dssp_066_sharefactor_log_diff_21d(sharefactor: pd.Series) -> pd.Series:
    """21d log change of sharefactor — short-window split detection (positive=split, negative=reverse)."""
    return _safe_log(sharefactor).diff(MDAYS)


def f19_dssp_067_sharefactor_log_diff_63d(sharefactor: pd.Series) -> pd.Series:
    """63d log change of sharefactor."""
    return _safe_log(sharefactor).diff(QDAYS)


def f19_dssp_068_sharefactor_log_diff_252d(sharefactor: pd.Series) -> pd.Series:
    """1y log change of sharefactor."""
    return _safe_log(sharefactor).diff(YDAYS)


def f19_dssp_069_sharefactor_increase_event_count_252d(sharefactor: pd.Series) -> pd.Series:
    """Bars in last 252d where daily sharefactor diff > 0 — forward-split event recurrence."""
    flag = (sharefactor.diff() > 0).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f19_dssp_070_days_since_sharefactor_increase_252d(sharefactor: pd.Series) -> pd.Series:
    """Bars since the last forward-split event in 252d."""
    flag = (sharefactor.diff() > 0).astype(float)
    return _recency_since_event(flag, YDAYS)


def f19_dssp_071_sharefactor_increase_intensity_252d(sharefactor: pd.Series) -> pd.Series:
    """252d sum of positive sharefactor diffs — cumulative forward-split intensity."""
    d = sharefactor.diff().clip(lower=0.0)
    return d.rolling(YDAYS, min_periods=QDAYS).sum()


def f19_dssp_072_sharefactor_decrease_event_count_252d(sharefactor: pd.Series) -> pd.Series:
    """Bars in last 252d where daily sharefactor diff < 0 — REVERSE-split event recurrence (distress)."""
    flag = (sharefactor.diff() < 0).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f19_dssp_073_sharefactor_decrease_intensity_252d(sharefactor: pd.Series) -> pd.Series:
    """252d sum of |negative sharefactor diffs| — cumulative reverse-split intensity."""
    d = sharefactor.diff().clip(upper=0.0).abs()
    return d.rolling(YDAYS, min_periods=QDAYS).sum()


def f19_dssp_074_days_since_sharefactor_decrease_252d(sharefactor: pd.Series) -> pd.Series:
    """Bars since the last reverse-split event in 252d."""
    flag = (sharefactor.diff() < 0).astype(float)
    return _recency_since_event(flag, YDAYS)


def f19_dssp_075_sharefactor_reverse_split_indicator_252d(sharefactor: pd.Series) -> pd.Series:
    """1 if any reverse-split (sharefactor.diff()<0) within last 252d, else 0."""
    flag = (sharefactor.diff() < 0).astype(float)
    cnt = flag.rolling(YDAYS, min_periods=QDAYS).sum()
    return (cnt > 0).astype(float).where(cnt.notna(), np.nan)


# ============================================================
#                        REGISTRY
# ============================================================

DILUTION_STRUCTURE_SNAPSHOT_BASE_REGISTRY_001_075 = {
    "f19_dssp_001_sharesbas_zscore_252d": {"inputs": ["sharesbas"], "func": f19_dssp_001_sharesbas_zscore_252d},
    "f19_dssp_002_sharesbas_zscore_63d": {"inputs": ["sharesbas"], "func": f19_dssp_002_sharesbas_zscore_63d},
    "f19_dssp_003_sharesbas_log_diff_21d": {"inputs": ["sharesbas"], "func": f19_dssp_003_sharesbas_log_diff_21d},
    "f19_dssp_004_sharesbas_log_diff_63d": {"inputs": ["sharesbas"], "func": f19_dssp_004_sharesbas_log_diff_63d},
    "f19_dssp_005_sharesbas_log_diff_252d": {"inputs": ["sharesbas"], "func": f19_dssp_005_sharesbas_log_diff_252d},
    "f19_dssp_006_sharesbas_log_diff_756d": {"inputs": ["sharesbas"], "func": f19_dssp_006_sharesbas_log_diff_756d},
    "f19_dssp_007_sharesbas_log_diff_1260d": {"inputs": ["sharesbas"], "func": f19_dssp_007_sharesbas_log_diff_1260d},
    "f19_dssp_008_sharesbas_pct_change_21d": {"inputs": ["sharesbas"], "func": f19_dssp_008_sharesbas_pct_change_21d},
    "f19_dssp_009_sharesbas_pct_change_63d": {"inputs": ["sharesbas"], "func": f19_dssp_009_sharesbas_pct_change_63d},
    "f19_dssp_010_sharesbas_pct_change_252d": {"inputs": ["sharesbas"], "func": f19_dssp_010_sharesbas_pct_change_252d},
    "f19_dssp_011_sharesbas_rank_pct_252d": {"inputs": ["sharesbas"], "func": f19_dssp_011_sharesbas_rank_pct_252d},
    "f19_dssp_012_sharesbas_distance_to_252d_max_log": {"inputs": ["sharesbas"], "func": f19_dssp_012_sharesbas_distance_to_252d_max_log},
    "f19_dssp_013_days_since_sharesbas_max_252d": {"inputs": ["sharesbas"], "func": f19_dssp_013_days_since_sharesbas_max_252d},
    "f19_dssp_014_days_since_sharesbas_max_756d": {"inputs": ["sharesbas"], "func": f19_dssp_014_days_since_sharesbas_max_756d},
    "f19_dssp_015_sharesbas_at_yearly_max_indicator": {"inputs": ["sharesbas"], "func": f19_dssp_015_sharesbas_at_yearly_max_indicator},
    "f19_dssp_016_sharesbas_streak_above_long_mean_252d": {"inputs": ["sharesbas"], "func": f19_dssp_016_sharesbas_streak_above_long_mean_252d},
    "f19_dssp_017_sharesbas_above_p90_count_63d": {"inputs": ["sharesbas"], "func": f19_dssp_017_sharesbas_above_p90_count_63d},
    "f19_dssp_018_sharesbas_above_p99_count_252d": {"inputs": ["sharesbas"], "func": f19_dssp_018_sharesbas_above_p99_count_252d},
    "f19_dssp_019_sharesbas_acceleration_21d": {"inputs": ["sharesbas"], "func": f19_dssp_019_sharesbas_acceleration_21d},
    "f19_dssp_020_sharesbas_acceleration_63d": {"inputs": ["sharesbas"], "func": f19_dssp_020_sharesbas_acceleration_63d},
    "f19_dssp_021_sharesbas_sma_5_to_sma_252": {"inputs": ["sharesbas"], "func": f19_dssp_021_sharesbas_sma_5_to_sma_252},
    "f19_dssp_022_sharesbas_sma_21_to_sma_252": {"inputs": ["sharesbas"], "func": f19_dssp_022_sharesbas_sma_21_to_sma_252},
    "f19_dssp_023_sharesbas_sma_63_to_sma_252": {"inputs": ["sharesbas"], "func": f19_dssp_023_sharesbas_sma_63_to_sma_252},
    "f19_dssp_024_sharesbas_sma_5_to_sma_63": {"inputs": ["sharesbas"], "func": f19_dssp_024_sharesbas_sma_5_to_sma_63},
    "f19_dssp_025_sharesbas_ema_log_diff_speed": {"inputs": ["sharesbas"], "func": f19_dssp_025_sharesbas_ema_log_diff_speed},
    "f19_dssp_026_shareswadil_zscore_252d": {"inputs": ["shareswadil"], "func": f19_dssp_026_shareswadil_zscore_252d},
    "f19_dssp_027_shareswadil_log_diff_21d": {"inputs": ["shareswadil"], "func": f19_dssp_027_shareswadil_log_diff_21d},
    "f19_dssp_028_shareswadil_log_diff_63d": {"inputs": ["shareswadil"], "func": f19_dssp_028_shareswadil_log_diff_63d},
    "f19_dssp_029_shareswadil_log_diff_252d": {"inputs": ["shareswadil"], "func": f19_dssp_029_shareswadil_log_diff_252d},
    "f19_dssp_030_shareswadil_log_diff_756d": {"inputs": ["shareswadil"], "func": f19_dssp_030_shareswadil_log_diff_756d},
    "f19_dssp_031_shareswadil_minus_shareswa_level": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_031_shareswadil_minus_shareswa_level},
    "f19_dssp_032_shareswadil_minus_shareswa_pct_of_shareswa": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_032_shareswadil_minus_shareswa_pct_of_shareswa},
    "f19_dssp_033_shareswadil_minus_shareswa_log_diff_63d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_033_shareswadil_minus_shareswa_log_diff_63d},
    "f19_dssp_034_shareswadil_minus_shareswa_log_diff_252d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_034_shareswadil_minus_shareswa_log_diff_252d},
    "f19_dssp_035_shareswadil_minus_shareswa_zscore_252d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_035_shareswadil_minus_shareswa_zscore_252d},
    "f19_dssp_036_shareswadil_minus_shareswa_rank_pct_252d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_036_shareswadil_minus_shareswa_rank_pct_252d},
    "f19_dssp_037_shareswadil_minus_shareswa_log_diff_21d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_037_shareswadil_minus_shareswa_log_diff_21d},
    "f19_dssp_038_shareswadil_minus_shareswa_top_decile_count_252d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_038_shareswadil_minus_shareswa_top_decile_count_252d},
    "f19_dssp_039_dilution_overhang_above_5pct_count_252d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_039_dilution_overhang_above_5pct_count_252d},
    "f19_dssp_040_dilution_overhang_acceleration_21d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_040_dilution_overhang_acceleration_21d},
    "f19_dssp_041_dilution_overhang_acceleration_63d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_041_dilution_overhang_acceleration_63d},
    "f19_dssp_042_dilution_overhang_p90_count_63d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_042_dilution_overhang_p90_count_63d},
    "f19_dssp_043_days_since_dilution_overhang_max_252d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_043_days_since_dilution_overhang_max_252d},
    "f19_dssp_044_dilution_overhang_streak_above_long_mean": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_044_dilution_overhang_streak_above_long_mean},
    "f19_dssp_045_dilution_overhang_zscore_change_63d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_045_dilution_overhang_zscore_change_63d},
    "f19_dssp_046_dilution_overhang_pct_above_long_baseline_63d": {"inputs": ["shareswadil", "shareswa"], "func": f19_dssp_046_dilution_overhang_pct_above_long_baseline_63d},
    "f19_dssp_047_shareswadil_vs_sharesbas_ratio": {"inputs": ["shareswadil", "sharesbas"], "func": f19_dssp_047_shareswadil_vs_sharesbas_ratio},
    "f19_dssp_048_shareswadil_vs_sharesbas_log_diff_21d": {"inputs": ["shareswadil", "sharesbas"], "func": f19_dssp_048_shareswadil_vs_sharesbas_log_diff_21d},
    "f19_dssp_049_shareswadil_vs_sharesbas_log_diff_63d": {"inputs": ["shareswadil", "sharesbas"], "func": f19_dssp_049_shareswadil_vs_sharesbas_log_diff_63d},
    "f19_dssp_050_shareswadil_vs_sharesbas_above_p90_count_63d": {"inputs": ["shareswadil", "sharesbas"], "func": f19_dssp_050_shareswadil_vs_sharesbas_above_p90_count_63d},
    "f19_dssp_051_shareswa_zscore_252d": {"inputs": ["shareswa"], "func": f19_dssp_051_shareswa_zscore_252d},
    "f19_dssp_052_shareswa_log_diff_21d": {"inputs": ["shareswa"], "func": f19_dssp_052_shareswa_log_diff_21d},
    "f19_dssp_053_shareswa_log_diff_63d": {"inputs": ["shareswa"], "func": f19_dssp_053_shareswa_log_diff_63d},
    "f19_dssp_054_shareswa_log_diff_252d": {"inputs": ["shareswa"], "func": f19_dssp_054_shareswa_log_diff_252d},
    "f19_dssp_055_shareswa_log_diff_756d": {"inputs": ["shareswa"], "func": f19_dssp_055_shareswa_log_diff_756d},
    "f19_dssp_056_shareswa_vs_sharesbas_ratio": {"inputs": ["shareswa", "sharesbas"], "func": f19_dssp_056_shareswa_vs_sharesbas_ratio},
    "f19_dssp_057_shareswa_vs_sharesbas_log_diff_63d": {"inputs": ["shareswa", "sharesbas"], "func": f19_dssp_057_shareswa_vs_sharesbas_log_diff_63d},
    "f19_dssp_058_shareswa_vs_sharesbas_log_diff_252d": {"inputs": ["shareswa", "sharesbas"], "func": f19_dssp_058_shareswa_vs_sharesbas_log_diff_252d},
    "f19_dssp_059_shareswa_pct_change_252d": {"inputs": ["shareswa"], "func": f19_dssp_059_shareswa_pct_change_252d},
    "f19_dssp_060_shareswa_rank_pct_252d": {"inputs": ["shareswa"], "func": f19_dssp_060_shareswa_rank_pct_252d},
    "f19_dssp_061_shareswa_distance_to_252d_max_log": {"inputs": ["shareswa"], "func": f19_dssp_061_shareswa_distance_to_252d_max_log},
    "f19_dssp_062_shareswa_acceleration_21d": {"inputs": ["shareswa"], "func": f19_dssp_062_shareswa_acceleration_21d},
    "f19_dssp_063_shareswa_acceleration_63d": {"inputs": ["shareswa"], "func": f19_dssp_063_shareswa_acceleration_63d},
    "f19_dssp_064_shareswa_quarterly_step_change_indicator_252d": {"inputs": ["shareswa"], "func": f19_dssp_064_shareswa_quarterly_step_change_indicator_252d},
    "f19_dssp_065_days_since_shareswa_max_252d": {"inputs": ["shareswa"], "func": f19_dssp_065_days_since_shareswa_max_252d},
    "f19_dssp_066_sharefactor_log_diff_21d": {"inputs": ["sharefactor"], "func": f19_dssp_066_sharefactor_log_diff_21d},
    "f19_dssp_067_sharefactor_log_diff_63d": {"inputs": ["sharefactor"], "func": f19_dssp_067_sharefactor_log_diff_63d},
    "f19_dssp_068_sharefactor_log_diff_252d": {"inputs": ["sharefactor"], "func": f19_dssp_068_sharefactor_log_diff_252d},
    "f19_dssp_069_sharefactor_increase_event_count_252d": {"inputs": ["sharefactor"], "func": f19_dssp_069_sharefactor_increase_event_count_252d},
    "f19_dssp_070_days_since_sharefactor_increase_252d": {"inputs": ["sharefactor"], "func": f19_dssp_070_days_since_sharefactor_increase_252d},
    "f19_dssp_071_sharefactor_increase_intensity_252d": {"inputs": ["sharefactor"], "func": f19_dssp_071_sharefactor_increase_intensity_252d},
    "f19_dssp_072_sharefactor_decrease_event_count_252d": {"inputs": ["sharefactor"], "func": f19_dssp_072_sharefactor_decrease_event_count_252d},
    "f19_dssp_073_sharefactor_decrease_intensity_252d": {"inputs": ["sharefactor"], "func": f19_dssp_073_sharefactor_decrease_intensity_252d},
    "f19_dssp_074_days_since_sharefactor_decrease_252d": {"inputs": ["sharefactor"], "func": f19_dssp_074_days_since_sharefactor_decrease_252d},
    "f19_dssp_075_sharefactor_reverse_split_indicator_252d": {"inputs": ["sharefactor"], "func": f19_dssp_075_sharefactor_reverse_split_indicator_252d},
}
