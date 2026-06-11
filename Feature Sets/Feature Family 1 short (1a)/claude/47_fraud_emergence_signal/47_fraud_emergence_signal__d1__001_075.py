"""fraud_emergence_signal d1 features 001-075 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5

def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, 'index') else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)

def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)

def _safe_log_abs(s, eps=1e-12):
    if isinstance(s, pd.Series):
        a = s.abs()
        return np.log(a.where(a > eps, np.nan))
    a = np.abs(s)
    return np.log(np.where(a > eps, a, np.nan))

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _ttm(s):
    return s.rolling(4, min_periods=1).sum()

def _avg4(s):
    return s.rolling(4, min_periods=1).mean()

def _yoy(s):
    return s - s.shift(4)

def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())

def _qoq(s):
    return s.diff()

def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())

def _consec_positive_streak(s):
    pos = (s > 0).astype(float)
    grp = (pos == 0).cumsum()
    return pos.groupby(grp).cumsum()

def _consec_zero_streak(s):
    z = (s == 0).astype(float)
    grp = (z == 0).cumsum()
    return z.groupby(grp).cumsum()

def _consec_true_streak(mask):
    m = mask.astype(float)
    grp = (m == 0).cumsum()
    return m.groupby(grp).cumsum()

def _quarters_since_positive(s):
    pos = (s > 0).astype(float)
    last_idx = pd.Series(np.where(pos > 0, np.arange(len(pos)), np.nan), index=s.index).ffill()
    out = pd.Series(np.arange(len(s), dtype=float), index=s.index) - last_idx
    return out

def f47_frem_001_event_count_q_d1(event_count):
    return event_count.astype(float).diff()

def f47_frem_002_event_count_ttm_d1(event_count):
    return _ttm(event_count).diff()

def f47_frem_003_event_count_yoy_pct_d1(event_count):
    return _yoy_pct(event_count).diff()

def f47_frem_004_event_count_qoq_change_d1(event_count):
    return _qoq(event_count).diff()

def f47_frem_005_event_count_zscore_8q_d1(event_count):
    return _rolling_zscore(event_count, 8, min_periods=3).diff()

def f47_frem_006_event_count_8q_slope_d1(event_count):
    return _rolling_slope(event_count, 8, min_periods=3).diff()

def f47_frem_007_event_count_drawup_from_8q_min_d1(event_count):
    rmin = event_count.rolling(8, min_periods=3).min()
    return (event_count - rmin).diff()

def f47_frem_008_event_intensity_per_revenue_d1(event_count, revenue):
    return _safe_div(event_count, _safe_log(revenue.abs() + 1)).diff()

def f47_frem_009_log_event_count_d1(event_count):
    return np.log(event_count.astype(float) + 1.0).diff()

def f47_frem_010_event_density_per_assets_d1(event_count, assets):
    return _safe_div(event_count, _safe_log(assets + 1)).diff()

def f47_frem_011_event_count_above_75pct_baseline_indicator_d1(event_count):
    q75 = event_count.rolling(8, min_periods=3).quantile(0.75)
    return (event_count > q75).astype(float).diff()

def f47_frem_012_event_count_consec_increase_streak_d1(event_count):
    inc = (event_count.diff() > 0).astype(float)
    grp = (inc == 0).cumsum()
    return inc.groupby(grp).cumsum().diff()

def f47_frem_013_event_count_4q_max_d1(event_count):
    return event_count.rolling(4, min_periods=1).max().diff()

def f47_frem_014_event_count_8q_max_d1(event_count):
    return event_count.rolling(8, min_periods=3).max().diff()

def f47_frem_015_event_count_breach_of_8q_max_indicator_d1(event_count):
    prior_max = event_count.shift(1).rolling(8, min_periods=3).max()
    return (event_count > prior_max).astype(float).diff()

def f47_frem_016_event_count_acceleration_d1(event_count):
    return event_count.diff().diff().diff()

def f47_frem_017_event_count_persistence_above_2_count_8q_d1(event_count):
    return (event_count > 2).astype(float).rolling(8, min_periods=3).sum().diff()

def f47_frem_018_event_count_persistence_above_4_count_8q_d1(event_count):
    return (event_count > 4).astype(float).rolling(8, min_periods=3).sum().diff()

def f47_frem_019_event_count_qoq_change_volatility_8q_d1(event_count):
    return event_count.diff().rolling(8, min_periods=3).std().diff()

def f47_frem_020_event_count_to_action_count_ratio_d1(event_count, action_count):
    return _safe_div(event_count, action_count).diff()

def f47_frem_021_event_restatement_q_d1(event_restatement):
    return event_restatement.astype(float).diff()

def f47_frem_022_event_restatement_ttm_d1(event_restatement):
    return _ttm(event_restatement).diff()

def f47_frem_023_event_restatement_yoy_count_d1(event_restatement):
    return event_restatement.diff(4).diff()

def f47_frem_024_event_restatement_indicator_8q_d1(event_restatement):
    return (event_restatement.rolling(8, min_periods=3).sum() > 0).astype(float).diff()

def f47_frem_025_quarters_since_last_restatement_d1(event_restatement):
    return _quarters_since_positive(event_restatement).diff()

def f47_frem_026_event_auditor_change_q_d1(event_auditor_change):
    return event_auditor_change.astype(float).diff()

def f47_frem_027_event_auditor_change_ttm_d1(event_auditor_change):
    return _ttm(event_auditor_change).diff()

def f47_frem_028_event_auditor_change_indicator_8q_d1(event_auditor_change):
    return (event_auditor_change.rolling(8, min_periods=3).sum() > 0).astype(float).diff()

def f47_frem_029_quarters_since_last_auditor_change_d1(event_auditor_change):
    return _quarters_since_positive(event_auditor_change).diff()

def f47_frem_030_event_executive_departure_q_d1(event_executive_departure):
    return event_executive_departure.astype(float).diff()

def f47_frem_031_event_executive_departure_ttm_d1(event_executive_departure):
    return _ttm(event_executive_departure).diff()

def f47_frem_032_event_executive_departure_yoy_change_d1(event_executive_departure):
    return event_executive_departure.diff(4).diff()

def f47_frem_033_event_executive_departure_zscore_8q_d1(event_executive_departure):
    return _rolling_zscore(event_executive_departure, 8, min_periods=3).diff()

def f47_frem_034_quarters_since_last_exec_departure_d1(event_executive_departure):
    return _quarters_since_positive(event_executive_departure).diff()

def f47_frem_035_cfo_departure_proxy_d1(event_executive_departure):
    return event_executive_departure.astype(float).diff()

def f47_frem_036_event_material_writedown_q_d1(event_material_writedown):
    return event_material_writedown.astype(float).diff()

def f47_frem_037_event_material_writedown_ttm_d1(event_material_writedown):
    return _ttm(event_material_writedown).diff()

def f47_frem_038_event_writedown_indicator_8q_d1(event_material_writedown):
    return (event_material_writedown.rolling(8, min_periods=3).sum() > 0).astype(float).diff()

def f47_frem_039_event_sec_investigation_q_d1(event_sec_investigation):
    return event_sec_investigation.astype(float).diff()

def f47_frem_040_event_sec_investigation_indicator_8q_d1(event_sec_investigation):
    return (event_sec_investigation.rolling(8, min_periods=3).sum() > 0).astype(float).diff()

def f47_frem_041_event_class_action_lawsuit_q_d1(event_class_action_lawsuit):
    return event_class_action_lawsuit.astype(float).diff()

def f47_frem_042_event_class_action_indicator_8q_d1(event_class_action_lawsuit):
    return (event_class_action_lawsuit.rolling(8, min_periods=3).sum() > 0).astype(float).diff()

def f47_frem_043_governance_red_flag_count_8q_d1(event_auditor_change, event_executive_departure, event_restatement):
    combined = event_auditor_change.fillna(0) + event_executive_departure.fillna(0) + event_restatement.fillna(0)
    return combined.rolling(8, min_periods=3).sum().diff()

def f47_frem_044_governance_red_flag_indicator_any_8q_d1(event_restatement, event_auditor_change, event_sec_investigation):
    combined = event_restatement.fillna(0) + event_auditor_change.fillna(0) + event_sec_investigation.fillna(0)
    return (combined.rolling(8, min_periods=3).sum() > 0).astype(float).diff()

def f47_frem_045_serial_restatement_indicator_d1(event_restatement):
    return (event_restatement.rolling(12, min_periods=4).sum() >= 2).astype(float).diff()

def f47_frem_046_action_count_q_d1(action_count):
    return action_count.astype(float).diff()

def f47_frem_047_action_count_ttm_d1(action_count):
    return _ttm(action_count).diff()

def f47_frem_048_action_count_yoy_pct_d1(action_count):
    return _yoy_pct(action_count).diff()

def f47_frem_049_action_count_zscore_8q_d1(action_count):
    return _rolling_zscore(action_count, 8, min_periods=3).diff()

def f47_frem_050_action_count_8q_slope_d1(action_count):
    return _rolling_slope(action_count, 8, min_periods=3).diff()

def f47_frem_051_action_ticker_change_q_d1(action_ticker_change):
    return action_ticker_change.astype(float).diff()

def f47_frem_052_action_ticker_change_ttm_d1(action_ticker_change):
    return _ttm(action_ticker_change).diff()

def f47_frem_053_quarters_since_last_ticker_change_d1(action_ticker_change):
    return _quarters_since_positive(action_ticker_change).diff()

def f47_frem_054_action_reverse_split_q_d1(action_reverse_split):
    return action_reverse_split.astype(float).diff()

def f47_frem_055_action_reverse_split_ttm_d1(action_reverse_split):
    return _ttm(action_reverse_split).diff()

def f47_frem_056_action_reverse_split_indicator_8q_d1(action_reverse_split):
    return (action_reverse_split.rolling(8, min_periods=3).sum() > 0).astype(float).diff()

def f47_frem_057_action_dividend_suspension_q_d1(action_dividend_suspension):
    return action_dividend_suspension.astype(float).diff()

def f47_frem_058_action_dividend_suspension_indicator_8q_d1(action_dividend_suspension):
    return (action_dividend_suspension.rolling(8, min_periods=3).sum() > 0).astype(float).diff()

def f47_frem_059_action_acquisition_q_d1(action_acquisition):
    return action_acquisition.astype(float).diff()

def f47_frem_060_action_acquisition_ttm_d1(action_acquisition):
    return _ttm(action_acquisition).diff()

def f47_frem_061_action_acquisition_yoy_change_d1(action_acquisition):
    return action_acquisition.diff(4).diff()

def f47_frem_062_action_split_q_d1(action_split):
    return action_split.astype(float).diff()

def f47_frem_063_action_count_to_event_count_ratio_d1(action_count, event_count):
    return _safe_div(action_count, event_count).diff()

def f47_frem_064_action_count_acceleration_d1(action_count):
    return action_count.diff().diff().diff()

def f47_frem_065_action_count_qoq_volatility_8q_d1(action_count):
    return _qoq(action_count).rolling(8, min_periods=3).std().diff()

def f47_frem_066_quarters_since_last_action_d1(action_count):
    return _quarters_since_positive(action_count).diff()

def f47_frem_067_action_consec_zero_streak_d1(action_count):
    return _consec_zero_streak(action_count).diff()

def f47_frem_068_action_consec_positive_streak_d1(action_count):
    return _consec_positive_streak(action_count).diff()

def f47_frem_069_action_count_breach_of_8q_max_indicator_d1(action_count):
    prior_max = action_count.shift(1).rolling(8, min_periods=3).max()
    return (action_count > prior_max).astype(float).diff()

def f47_frem_070_action_unique_indicator_breadth_8q_d1(action_ticker_change, action_reverse_split, action_dividend_suspension, action_acquisition, action_split):
    ind = (action_ticker_change > 0).astype(float) + (action_reverse_split > 0).astype(float) + (action_dividend_suspension > 0).astype(float) + (action_acquisition > 0).astype(float) + (action_split > 0).astype(float)
    return ind.rolling(8, min_periods=3).sum().diff()

def f47_frem_071_event_count_x_netinc_negative_d1(event_count, netinc):
    return (event_count * (netinc < 0).astype(float)).diff()

def f47_frem_072_event_count_x_ncfo_negative_d1(event_count, ncfo):
    return (event_count * (ncfo < 0).astype(float)).diff()

def f47_frem_073_event_count_x_revenue_yoy_negative_d1(event_count, revenue):
    return (event_count * (_yoy_pct(revenue) < 0).astype(float)).diff()

def f47_frem_074_event_count_x_ebitda_negative_d1(event_count, ebitda):
    return (event_count * (ebitda < 0).astype(float)).diff()

def f47_frem_075_event_count_x_equity_decline_d1(event_count, equity):
    return (event_count * (equity.diff(4) < 0).astype(float)).diff()
FRAUD_EMERGENCE_SIGNAL_D1_REGISTRY_001_075 = {'f47_frem_001_event_count_q_d1': {'inputs': ['event_count'], 'func': f47_frem_001_event_count_q_d1}, 'f47_frem_002_event_count_ttm_d1': {'inputs': ['event_count'], 'func': f47_frem_002_event_count_ttm_d1}, 'f47_frem_003_event_count_yoy_pct_d1': {'inputs': ['event_count'], 'func': f47_frem_003_event_count_yoy_pct_d1}, 'f47_frem_004_event_count_qoq_change_d1': {'inputs': ['event_count'], 'func': f47_frem_004_event_count_qoq_change_d1}, 'f47_frem_005_event_count_zscore_8q_d1': {'inputs': ['event_count'], 'func': f47_frem_005_event_count_zscore_8q_d1}, 'f47_frem_006_event_count_8q_slope_d1': {'inputs': ['event_count'], 'func': f47_frem_006_event_count_8q_slope_d1}, 'f47_frem_007_event_count_drawup_from_8q_min_d1': {'inputs': ['event_count'], 'func': f47_frem_007_event_count_drawup_from_8q_min_d1}, 'f47_frem_008_event_intensity_per_revenue_d1': {'inputs': ['event_count', 'revenue'], 'func': f47_frem_008_event_intensity_per_revenue_d1}, 'f47_frem_009_log_event_count_d1': {'inputs': ['event_count'], 'func': f47_frem_009_log_event_count_d1}, 'f47_frem_010_event_density_per_assets_d1': {'inputs': ['event_count', 'assets'], 'func': f47_frem_010_event_density_per_assets_d1}, 'f47_frem_011_event_count_above_75pct_baseline_indicator_d1': {'inputs': ['event_count'], 'func': f47_frem_011_event_count_above_75pct_baseline_indicator_d1}, 'f47_frem_012_event_count_consec_increase_streak_d1': {'inputs': ['event_count'], 'func': f47_frem_012_event_count_consec_increase_streak_d1}, 'f47_frem_013_event_count_4q_max_d1': {'inputs': ['event_count'], 'func': f47_frem_013_event_count_4q_max_d1}, 'f47_frem_014_event_count_8q_max_d1': {'inputs': ['event_count'], 'func': f47_frem_014_event_count_8q_max_d1}, 'f47_frem_015_event_count_breach_of_8q_max_indicator_d1': {'inputs': ['event_count'], 'func': f47_frem_015_event_count_breach_of_8q_max_indicator_d1}, 'f47_frem_016_event_count_acceleration_d1': {'inputs': ['event_count'], 'func': f47_frem_016_event_count_acceleration_d1}, 'f47_frem_017_event_count_persistence_above_2_count_8q_d1': {'inputs': ['event_count'], 'func': f47_frem_017_event_count_persistence_above_2_count_8q_d1}, 'f47_frem_018_event_count_persistence_above_4_count_8q_d1': {'inputs': ['event_count'], 'func': f47_frem_018_event_count_persistence_above_4_count_8q_d1}, 'f47_frem_019_event_count_qoq_change_volatility_8q_d1': {'inputs': ['event_count'], 'func': f47_frem_019_event_count_qoq_change_volatility_8q_d1}, 'f47_frem_020_event_count_to_action_count_ratio_d1': {'inputs': ['event_count', 'action_count'], 'func': f47_frem_020_event_count_to_action_count_ratio_d1}, 'f47_frem_021_event_restatement_q_d1': {'inputs': ['event_restatement'], 'func': f47_frem_021_event_restatement_q_d1}, 'f47_frem_022_event_restatement_ttm_d1': {'inputs': ['event_restatement'], 'func': f47_frem_022_event_restatement_ttm_d1}, 'f47_frem_023_event_restatement_yoy_count_d1': {'inputs': ['event_restatement'], 'func': f47_frem_023_event_restatement_yoy_count_d1}, 'f47_frem_024_event_restatement_indicator_8q_d1': {'inputs': ['event_restatement'], 'func': f47_frem_024_event_restatement_indicator_8q_d1}, 'f47_frem_025_quarters_since_last_restatement_d1': {'inputs': ['event_restatement'], 'func': f47_frem_025_quarters_since_last_restatement_d1}, 'f47_frem_026_event_auditor_change_q_d1': {'inputs': ['event_auditor_change'], 'func': f47_frem_026_event_auditor_change_q_d1}, 'f47_frem_027_event_auditor_change_ttm_d1': {'inputs': ['event_auditor_change'], 'func': f47_frem_027_event_auditor_change_ttm_d1}, 'f47_frem_028_event_auditor_change_indicator_8q_d1': {'inputs': ['event_auditor_change'], 'func': f47_frem_028_event_auditor_change_indicator_8q_d1}, 'f47_frem_029_quarters_since_last_auditor_change_d1': {'inputs': ['event_auditor_change'], 'func': f47_frem_029_quarters_since_last_auditor_change_d1}, 'f47_frem_030_event_executive_departure_q_d1': {'inputs': ['event_executive_departure'], 'func': f47_frem_030_event_executive_departure_q_d1}, 'f47_frem_031_event_executive_departure_ttm_d1': {'inputs': ['event_executive_departure'], 'func': f47_frem_031_event_executive_departure_ttm_d1}, 'f47_frem_032_event_executive_departure_yoy_change_d1': {'inputs': ['event_executive_departure'], 'func': f47_frem_032_event_executive_departure_yoy_change_d1}, 'f47_frem_033_event_executive_departure_zscore_8q_d1': {'inputs': ['event_executive_departure'], 'func': f47_frem_033_event_executive_departure_zscore_8q_d1}, 'f47_frem_034_quarters_since_last_exec_departure_d1': {'inputs': ['event_executive_departure'], 'func': f47_frem_034_quarters_since_last_exec_departure_d1}, 'f47_frem_035_cfo_departure_proxy_d1': {'inputs': ['event_executive_departure'], 'func': f47_frem_035_cfo_departure_proxy_d1}, 'f47_frem_036_event_material_writedown_q_d1': {'inputs': ['event_material_writedown'], 'func': f47_frem_036_event_material_writedown_q_d1}, 'f47_frem_037_event_material_writedown_ttm_d1': {'inputs': ['event_material_writedown'], 'func': f47_frem_037_event_material_writedown_ttm_d1}, 'f47_frem_038_event_writedown_indicator_8q_d1': {'inputs': ['event_material_writedown'], 'func': f47_frem_038_event_writedown_indicator_8q_d1}, 'f47_frem_039_event_sec_investigation_q_d1': {'inputs': ['event_sec_investigation'], 'func': f47_frem_039_event_sec_investigation_q_d1}, 'f47_frem_040_event_sec_investigation_indicator_8q_d1': {'inputs': ['event_sec_investigation'], 'func': f47_frem_040_event_sec_investigation_indicator_8q_d1}, 'f47_frem_041_event_class_action_lawsuit_q_d1': {'inputs': ['event_class_action_lawsuit'], 'func': f47_frem_041_event_class_action_lawsuit_q_d1}, 'f47_frem_042_event_class_action_indicator_8q_d1': {'inputs': ['event_class_action_lawsuit'], 'func': f47_frem_042_event_class_action_indicator_8q_d1}, 'f47_frem_043_governance_red_flag_count_8q_d1': {'inputs': ['event_auditor_change', 'event_executive_departure', 'event_restatement'], 'func': f47_frem_043_governance_red_flag_count_8q_d1}, 'f47_frem_044_governance_red_flag_indicator_any_8q_d1': {'inputs': ['event_restatement', 'event_auditor_change', 'event_sec_investigation'], 'func': f47_frem_044_governance_red_flag_indicator_any_8q_d1}, 'f47_frem_045_serial_restatement_indicator_d1': {'inputs': ['event_restatement'], 'func': f47_frem_045_serial_restatement_indicator_d1}, 'f47_frem_046_action_count_q_d1': {'inputs': ['action_count'], 'func': f47_frem_046_action_count_q_d1}, 'f47_frem_047_action_count_ttm_d1': {'inputs': ['action_count'], 'func': f47_frem_047_action_count_ttm_d1}, 'f47_frem_048_action_count_yoy_pct_d1': {'inputs': ['action_count'], 'func': f47_frem_048_action_count_yoy_pct_d1}, 'f47_frem_049_action_count_zscore_8q_d1': {'inputs': ['action_count'], 'func': f47_frem_049_action_count_zscore_8q_d1}, 'f47_frem_050_action_count_8q_slope_d1': {'inputs': ['action_count'], 'func': f47_frem_050_action_count_8q_slope_d1}, 'f47_frem_051_action_ticker_change_q_d1': {'inputs': ['action_ticker_change'], 'func': f47_frem_051_action_ticker_change_q_d1}, 'f47_frem_052_action_ticker_change_ttm_d1': {'inputs': ['action_ticker_change'], 'func': f47_frem_052_action_ticker_change_ttm_d1}, 'f47_frem_053_quarters_since_last_ticker_change_d1': {'inputs': ['action_ticker_change'], 'func': f47_frem_053_quarters_since_last_ticker_change_d1}, 'f47_frem_054_action_reverse_split_q_d1': {'inputs': ['action_reverse_split'], 'func': f47_frem_054_action_reverse_split_q_d1}, 'f47_frem_055_action_reverse_split_ttm_d1': {'inputs': ['action_reverse_split'], 'func': f47_frem_055_action_reverse_split_ttm_d1}, 'f47_frem_056_action_reverse_split_indicator_8q_d1': {'inputs': ['action_reverse_split'], 'func': f47_frem_056_action_reverse_split_indicator_8q_d1}, 'f47_frem_057_action_dividend_suspension_q_d1': {'inputs': ['action_dividend_suspension'], 'func': f47_frem_057_action_dividend_suspension_q_d1}, 'f47_frem_058_action_dividend_suspension_indicator_8q_d1': {'inputs': ['action_dividend_suspension'], 'func': f47_frem_058_action_dividend_suspension_indicator_8q_d1}, 'f47_frem_059_action_acquisition_q_d1': {'inputs': ['action_acquisition'], 'func': f47_frem_059_action_acquisition_q_d1}, 'f47_frem_060_action_acquisition_ttm_d1': {'inputs': ['action_acquisition'], 'func': f47_frem_060_action_acquisition_ttm_d1}, 'f47_frem_061_action_acquisition_yoy_change_d1': {'inputs': ['action_acquisition'], 'func': f47_frem_061_action_acquisition_yoy_change_d1}, 'f47_frem_062_action_split_q_d1': {'inputs': ['action_split'], 'func': f47_frem_062_action_split_q_d1}, 'f47_frem_063_action_count_to_event_count_ratio_d1': {'inputs': ['action_count', 'event_count'], 'func': f47_frem_063_action_count_to_event_count_ratio_d1}, 'f47_frem_064_action_count_acceleration_d1': {'inputs': ['action_count'], 'func': f47_frem_064_action_count_acceleration_d1}, 'f47_frem_065_action_count_qoq_volatility_8q_d1': {'inputs': ['action_count'], 'func': f47_frem_065_action_count_qoq_volatility_8q_d1}, 'f47_frem_066_quarters_since_last_action_d1': {'inputs': ['action_count'], 'func': f47_frem_066_quarters_since_last_action_d1}, 'f47_frem_067_action_consec_zero_streak_d1': {'inputs': ['action_count'], 'func': f47_frem_067_action_consec_zero_streak_d1}, 'f47_frem_068_action_consec_positive_streak_d1': {'inputs': ['action_count'], 'func': f47_frem_068_action_consec_positive_streak_d1}, 'f47_frem_069_action_count_breach_of_8q_max_indicator_d1': {'inputs': ['action_count'], 'func': f47_frem_069_action_count_breach_of_8q_max_indicator_d1}, 'f47_frem_070_action_unique_indicator_breadth_8q_d1': {'inputs': ['action_ticker_change', 'action_reverse_split', 'action_dividend_suspension', 'action_acquisition', 'action_split'], 'func': f47_frem_070_action_unique_indicator_breadth_8q_d1}, 'f47_frem_071_event_count_x_netinc_negative_d1': {'inputs': ['event_count', 'netinc'], 'func': f47_frem_071_event_count_x_netinc_negative_d1}, 'f47_frem_072_event_count_x_ncfo_negative_d1': {'inputs': ['event_count', 'ncfo'], 'func': f47_frem_072_event_count_x_ncfo_negative_d1}, 'f47_frem_073_event_count_x_revenue_yoy_negative_d1': {'inputs': ['event_count', 'revenue'], 'func': f47_frem_073_event_count_x_revenue_yoy_negative_d1}, 'f47_frem_074_event_count_x_ebitda_negative_d1': {'inputs': ['event_count', 'ebitda'], 'func': f47_frem_074_event_count_x_ebitda_negative_d1}, 'f47_frem_075_event_count_x_equity_decline_d1': {'inputs': ['event_count', 'equity'], 'func': f47_frem_075_event_count_x_equity_decline_d1}}