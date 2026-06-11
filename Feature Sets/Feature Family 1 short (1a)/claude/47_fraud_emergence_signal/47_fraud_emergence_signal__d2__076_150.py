"""fraud_emergence_signal d2 features 076-150 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _consec_true_streak(mask):
    m = mask.astype(float)
    grp = (m == 0).cumsum()
    return m.groupby(grp).cumsum()

def _quarters_since_positive(s):
    pos = (s > 0).astype(float)
    last_idx = pd.Series(np.where(pos > 0, np.arange(len(pos)), np.nan), index=s.index).ffill()
    out = pd.Series(np.arange(len(s), dtype=float), index=s.index) - last_idx
    return out

def _quarters_since_true(mask):
    m = mask.astype(float)
    last_idx = pd.Series(np.where(m > 0, np.arange(len(m)), np.nan), index=m.index).ffill()
    out = pd.Series(np.arange(len(m), dtype=float), index=m.index) - last_idx
    return out

def _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit):
    return 2.0 * event_material_writedown.fillna(0) + 3.0 * event_restatement.fillna(0) + 4.0 * event_sec_investigation.fillna(0) + 4.0 * event_class_action_lawsuit.fillna(0)

def _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown):
    return event_auditor_change.fillna(0) + event_restatement.fillna(0) + event_executive_departure.fillna(0) + event_material_writedown.fillna(0)

def f47_frem_076_event_count_during_revenue_decel_4q_d2(event_count, revenue):
    decel = (_yoy_pct(revenue).diff() < 0).astype(float)
    return (event_count.fillna(0) * decel).rolling(4, min_periods=1).sum().diff().diff()

def f47_frem_077_event_count_during_margin_drop_4q_d2(event_count, netinc, revenue):
    margin = _safe_div(netinc, revenue)
    drop = (margin.diff(4) < 0).astype(float)
    return (event_count.fillna(0) * drop).rolling(4, min_periods=1).sum().diff().diff()

def f47_frem_078_event_count_when_debt_growing_d2(event_count, debt):
    return (event_count * (_qoq(debt) > 0).astype(float)).diff().diff()

def f47_frem_079_event_count_when_ncfo_decel_d2(event_count, ncfo):
    return (event_count * (_qoq_pct(ncfo) < 0).astype(float)).diff().diff()

def f47_frem_080_event_count_after_4q_losses_indicator_d2(event_count, netinc):
    losses = (netinc < 0).astype(float).rolling(4, min_periods=4).sum()
    cond = (losses >= 4).astype(float)
    return ((event_count > 0).astype(float) * cond).astype(float).diff().diff()

def f47_frem_081_restatement_during_decel_indicator_d2(event_restatement, revenue):
    return ((event_restatement > 0) & (_yoy_pct(revenue).diff() < 0)).astype(float).diff().diff()

def f47_frem_082_auditor_change_with_loss_indicator_d2(event_auditor_change, netinc):
    return ((event_auditor_change > 0) & (netinc < 0)).astype(float).diff().diff()

def f47_frem_083_exec_departure_with_revenue_decline_indicator_d2(event_executive_departure, revenue):
    return ((event_executive_departure > 0) & (_yoy_pct(revenue) < 0)).astype(float).diff().diff()

def f47_frem_084_writedown_with_debt_growth_indicator_d2(event_material_writedown, debt):
    return ((event_material_writedown > 0) & (_yoy_pct(debt) > 0)).astype(float).diff().diff()

def f47_frem_085_event_count_yoy_when_growth_slowing_d2(event_count, revenue):
    return (_yoy_pct(event_count) * (_yoy_pct(revenue).diff() < 0).astype(float)).diff().diff()

def f47_frem_086_event_count_during_dilution_proxy_d2(event_count, sharesbas):
    return (event_count * (_yoy_pct(sharesbas) > 0.05).astype(float)).diff().diff()

def f47_frem_087_governance_red_flags_during_blowoff_proxy_d2(event_auditor_change, event_executive_departure, event_restatement, revenue):
    combined = event_auditor_change.fillna(0) + event_executive_departure.fillna(0) + event_restatement.fillna(0)
    grf_count = combined.rolling(8, min_periods=3).sum()
    return (grf_count * (_yoy_pct(revenue) < 0).astype(float)).diff().diff()

def f47_frem_088_event_acceleration_during_decel_d2(event_count, revenue):
    return (event_count.diff() * (_yoy_pct(revenue).diff() < 0).astype(float)).diff().diff()

def f47_frem_089_event_intensity_per_loss_dollar_d2(event_count, netinc):
    return _safe_div(event_count, _safe_log(netinc.abs() + 1)).diff().diff()

def f47_frem_090_action_count_during_decline_4q_d2(action_count, revenue):
    decline = (_yoy_pct(revenue) < 0).astype(float)
    return (action_count.fillna(0) * decline).rolling(4, min_periods=1).sum().diff().diff()

def f47_frem_091_reverse_split_during_loss_indicator_d2(action_reverse_split, netinc):
    return ((action_reverse_split > 0) & (netinc < 0)).astype(float).diff().diff()

def f47_frem_092_dividend_suspension_during_revenue_decline_indicator_d2(action_dividend_suspension, revenue):
    return ((action_dividend_suspension > 0) & (_yoy_pct(revenue) < 0)).astype(float).diff().diff()

def f47_frem_093_acquisition_during_cash_burn_indicator_d2(action_acquisition, ncfo):
    return ((action_acquisition > 0) & (ncfo < 0)).astype(float).diff().diff()

def f47_frem_094_ticker_change_with_loss_indicator_d2(action_ticker_change, netinc):
    return ((action_ticker_change > 0) & (netinc < 0)).astype(float).diff().diff()

def f47_frem_095_event_count_in_8q_window_when_avg_netinc_negative_d2(event_count, netinc):
    cond = (netinc.rolling(8, min_periods=3).mean() < 0).astype(float)
    return (event_count.fillna(0) * cond).rolling(8, min_periods=3).sum().diff().diff()

def f47_frem_096_event_share_during_revenue_collapse_d2(event_count, revenue):
    cond = (_yoy_pct(revenue) < -0.1).astype(float)
    return (event_count.fillna(0) * cond).rolling(8, min_periods=3).sum().diff().diff()

def f47_frem_097_event_intensity_during_decel_8q_avg_d2(event_count, revenue):
    decel = (_yoy_pct(revenue).diff() < 0).astype(float)
    masked = event_count.fillna(0) * decel
    return masked.rolling(8, min_periods=3).mean().diff().diff()

def f47_frem_098_fundamental_event_composite_d2(event_count, revenue):
    yp = _yoy_pct(revenue)
    neg_only = (-yp).clip(lower=0)
    return (event_count.fillna(0) * neg_only).diff().diff()

def f47_frem_099_event_count_during_assets_decline_d2(event_count, assets):
    return (event_count * (_yoy_pct(assets) < 0).astype(float)).diff().diff()

def f47_frem_100_event_count_during_equity_decline_d2(event_count, equity):
    return (event_count * (_yoy_pct(equity) < 0).astype(float)).diff().diff()

def f47_frem_101_event_clustering_overdispersion_8q_d2(event_count):
    v = event_count.rolling(8, min_periods=3).var()
    m = event_count.rolling(8, min_periods=3).mean()
    return _safe_div(v, m).diff().diff()

def f47_frem_102_event_burst_indicator_d2(event_count):
    m = event_count.rolling(8, min_periods=3).mean()
    return (event_count > 2.0 * m).astype(float).diff().diff()

def f47_frem_103_event_burst_count_8q_d2(event_count):
    m = event_count.rolling(8, min_periods=3).mean()
    burst = (event_count > 2.0 * m).astype(float)
    return burst.rolling(8, min_periods=3).sum().diff().diff()

def f47_frem_104_event_count_autocorr_lag1_8q_d2(event_count):
    lag = event_count.shift(1)
    return event_count.rolling(8, min_periods=3).corr(lag).diff().diff()

def f47_frem_105_event_count_jumpiness_8q_d2(event_count):
    return (event_count.rolling(8, min_periods=3).max() - event_count.rolling(8, min_periods=3).min()).diff().diff()

def f47_frem_106_event_count_step_change_size_8q_d2(event_count):
    return event_count.diff().abs().rolling(8, min_periods=3).max().diff().diff()

def f47_frem_107_governance_event_sequence_score_d2(event_auditor_change, event_restatement, event_executive_departure):
    ind_audit = (event_auditor_change.rolling(8, min_periods=3).sum() > 0).astype(float)
    ind_rest = (event_restatement.rolling(8, min_periods=3).sum() > 0).astype(float)
    exec_ttm = event_executive_departure.rolling(4, min_periods=1).sum()
    return (1.0 * ind_audit + 2.0 * ind_rest + 1.0 * exec_ttm).diff().diff()

def f47_frem_108_action_event_alignment_indicator_d2(action_count, event_count):
    return ((action_count > 0) & (event_count > 0)).astype(float).diff().diff()

def f47_frem_109_event_count_consec_positive_runs_8q_d2(event_count):
    pos = (event_count > 0).astype(int)
    run_start = ((pos == 1) & (pos.shift(1).fillna(0) == 0)).astype(float)
    return run_start.rolling(8, min_periods=3).sum().diff().diff()

def f47_frem_110_event_count_below_baseline_consec_streak_d2(event_count):
    q25 = event_count.rolling(8, min_periods=3).quantile(0.25)
    below = (event_count < q25).astype(float)
    grp = (below == 0).cumsum()
    return below.groupby(grp).cumsum().diff().diff()

def f47_frem_111_quarters_since_any_red_flag_d2(event_restatement, event_auditor_change, event_sec_investigation, event_class_action_lawsuit):
    any_flag = event_restatement.fillna(0) + event_auditor_change.fillna(0) + event_sec_investigation.fillna(0) + event_class_action_lawsuit.fillna(0) > 0
    return _quarters_since_true(any_flag).diff().diff()

def f47_frem_112_red_flag_density_8q_d2(event_restatement, event_auditor_change, event_sec_investigation, event_class_action_lawsuit):
    combined = event_restatement.fillna(0) + event_auditor_change.fillna(0) + event_sec_investigation.fillna(0) + event_class_action_lawsuit.fillna(0)
    return (combined.rolling(8, min_periods=3).sum() / 8.0).diff().diff()

def f47_frem_113_red_flag_density_12q_d2(event_restatement, event_auditor_change, event_sec_investigation, event_class_action_lawsuit):
    combined = event_restatement.fillna(0) + event_auditor_change.fillna(0) + event_sec_investigation.fillna(0) + event_class_action_lawsuit.fillna(0)
    return (combined.rolling(12, min_periods=4).sum() / 12.0).diff().diff()

def f47_frem_114_red_flag_acceleration_4q_d2(event_restatement, event_auditor_change, event_sec_investigation, event_class_action_lawsuit):
    combined = event_restatement.fillna(0) + event_auditor_change.fillna(0) + event_sec_investigation.fillna(0) + event_class_action_lawsuit.fillna(0)
    density = combined.rolling(8, min_periods=3).sum() / 8.0
    return density.diff(4).diff().diff()

def f47_frem_115_fraud_keyword_proxy_count_d2(event_sec_investigation, event_class_action_lawsuit):
    return (event_sec_investigation.fillna(0) + event_class_action_lawsuit.fillna(0)).diff().diff()

def f47_frem_116_event_count_persistence_above_median_8q_d2(event_count):
    med = event_count.rolling(8, min_periods=3).median()
    return (event_count > med).astype(float).rolling(8, min_periods=3).sum().diff().diff()

def f47_frem_117_action_persistence_above_median_8q_d2(action_count):
    med = action_count.rolling(8, min_periods=3).median()
    return (action_count > med).astype(float).rolling(8, min_periods=3).sum().diff().diff()

def f47_frem_118_event_count_8q_skewness_d2(event_count):
    return event_count.rolling(8, min_periods=3).skew().diff().diff()

def f47_frem_119_event_count_12q_skewness_d2(event_count):
    return event_count.rolling(12, min_periods=4).skew().diff().diff()

def f47_frem_120_event_count_8q_kurtosis_d2(event_count):
    return event_count.rolling(8, min_periods=4).kurt().diff().diff()

def f47_frem_121_event_distress_action_alignment_indicator_d2(event_material_writedown, event_auditor_change, action_dividend_suspension, action_reverse_split):
    distress = (event_material_writedown > 0) | (event_auditor_change > 0)
    action = (action_dividend_suspension > 0) | (action_reverse_split > 0)
    return (distress & action).astype(float).diff().diff()

def f47_frem_122_event_severity_index_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit):
    return _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit).diff().diff()

def f47_frem_123_event_severity_index_8q_max_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    return sev.rolling(8, min_periods=3).max().diff().diff()

def f47_frem_124_event_severity_index_drawup_from_8q_min_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    return (sev - sev.rolling(8, min_periods=3).min()).diff().diff()

def f47_frem_125_event_severity_index_8q_slope_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    return _rolling_slope(sev, 8, min_periods=3).diff().diff()

def f47_frem_126_event_severity_x_revenue_decel_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit, revenue):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    yp = _yoy_pct(revenue)
    weight = yp.abs().where(yp < 0, 0.0)
    return (sev * weight).diff().diff()

def f47_frem_127_event_severity_x_margin_drop_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit, netinc, revenue):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    margin = _safe_div(netinc, revenue)
    drop = margin.diff(4)
    weight = drop.abs().where(drop < 0, 0.0)
    return (sev * weight).diff().diff()

def f47_frem_128_event_severity_x_assets_decline_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit, assets):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    return (sev * (_yoy_pct(assets) < 0).astype(float)).diff().diff()

def f47_frem_129_event_severity_during_cash_burn_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit, ncfo):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    return (sev * (ncfo < 0).astype(float)).diff().diff()

def f47_frem_130_event_severity_with_dilution_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit, sharesbas):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    return (sev * _yoy_pct(sharesbas).clip(lower=0)).diff().diff()

def f47_frem_131_fundamental_event_terminal_signal_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit, ncfo, netinc):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    sev_ttm = sev.rolling(8, min_periods=3).sum()
    return ((sev_ttm > 5) & (ncfo < 0) & (netinc < 0)).astype(float).diff().diff()

def f47_frem_132_event_severity_per_assets_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit, assets):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    return _safe_div(sev, _safe_log(assets + 1)).diff().diff()

def f47_frem_133_event_severity_per_equity_d2(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit, equity):
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    return _safe_div(sev, _safe_log(equity.abs() + 1)).diff().diff()

def f47_frem_134_fraud_emergence_composite_8q_d2(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown):
    comp = _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown)
    return comp.rolling(8, min_periods=3).sum().diff().diff()

def f47_frem_135_fraud_emergence_composite_12q_d2(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown):
    comp = _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown)
    return comp.rolling(12, min_periods=4).sum().diff().diff()

def f47_frem_136_fraud_emergence_composite_qoq_change_d2(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown):
    comp = _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown)
    comp_8q = comp.rolling(8, min_periods=3).sum()
    return comp_8q.diff().diff().diff()

def f47_frem_137_fraud_emergence_composite_yoy_change_d2(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown):
    comp = _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown)
    comp_8q = comp.rolling(8, min_periods=3).sum()
    return comp_8q.diff(4).diff().diff()

def f47_frem_138_fraud_emergence_composite_zscore_8q_d2(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown):
    comp = _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown)
    return _rolling_zscore(comp, 8, min_periods=3).diff().diff()

def f47_frem_139_fraud_emergence_composite_8q_slope_d2(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown):
    comp = _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown)
    comp_8q = comp.rolling(8, min_periods=3).sum()
    return _rolling_slope(comp_8q, 8, min_periods=3).diff().diff()

def f47_frem_140_fraud_emergence_composite_breach_of_8q_max_d2(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown):
    comp = _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown)
    comp_8q = comp.rolling(8, min_periods=3).sum()
    prior_max = comp_8q.shift(1).rolling(8, min_periods=3).max()
    return (comp_8q > prior_max).astype(float).diff().diff()

def f47_frem_141_fraud_emergence_composite_persistence_above_median_8q_d2(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown):
    comp = _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown)
    comp_8q = comp.rolling(8, min_periods=3).sum()
    med = comp_8q.rolling(8, min_periods=3).median()
    return (comp_8q > med).astype(float).rolling(8, min_periods=3).sum().diff().diff()

def f47_frem_142_fraud_emergence_composite_during_decline_4q_d2(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown, revenue):
    comp = _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown)
    comp_8q = comp.rolling(8, min_periods=3).sum()
    cond = (_yoy_pct(revenue) < 0).astype(float)
    return (comp_8q * cond).rolling(4, min_periods=1).sum().diff().diff()

def f47_frem_143_consec_quarters_with_any_red_flag_d2(event_restatement, event_auditor_change, event_sec_investigation, event_class_action_lawsuit):
    any_flag = event_restatement.fillna(0) + event_auditor_change.fillna(0) + event_sec_investigation.fillna(0) + event_class_action_lawsuit.fillna(0) > 0
    return _consec_true_streak(any_flag).diff().diff()

def f47_frem_144_consec_quarters_zero_events_d2(event_count):
    zero = event_count == 0
    return _consec_true_streak(zero).diff().diff()

def f47_frem_145_event_jump_after_calm_indicator_d2(event_count):
    calm = event_count.rolling(4, min_periods=4).sum().shift(1) == 0
    return (calm & (event_count >= 2)).astype(float).diff().diff()

def f47_frem_146_governance_breakdown_indicator_d2(event_auditor_change, event_restatement, event_executive_departure):
    combined = event_auditor_change.fillna(0) + event_restatement.fillna(0) + event_executive_departure.fillna(0)
    return (combined.rolling(4, min_periods=2).sum() >= 2).astype(float).diff().diff()

def f47_frem_147_material_event_yoy_rise_d2(event_material_writedown, event_restatement, event_sec_investigation):
    combined = event_material_writedown.fillna(0) + event_restatement.fillna(0) + event_sec_investigation.fillna(0)
    return _ttm(combined).diff(4).diff().diff()

def f47_frem_148_event_emergence_velocity_d2(event_count):
    return _ttm(event_count).diff(4).diff().diff()

def f47_frem_149_event_emergence_acceleration_d2(event_count):
    return _ttm(event_count).diff(4).diff().diff().diff()

def f47_frem_150_fraud_emergence_terminal_signal_d2(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown, event_sec_investigation, event_class_action_lawsuit, revenue):
    comp = _fraud_composite(event_auditor_change, event_restatement, event_executive_departure, event_material_writedown)
    comp_8q = comp.rolling(8, min_periods=3).sum()
    sev = _severity_index(event_material_writedown, event_restatement, event_sec_investigation, event_class_action_lawsuit)
    return ((comp_8q > 3) & (sev > 5) & (_yoy_pct(revenue) < 0)).astype(float).diff().diff()
FRAUD_EMERGENCE_SIGNAL_D2_REGISTRY_076_150 = {'f47_frem_076_event_count_during_revenue_decel_4q_d2': {'inputs': ['event_count', 'revenue'], 'func': f47_frem_076_event_count_during_revenue_decel_4q_d2}, 'f47_frem_077_event_count_during_margin_drop_4q_d2': {'inputs': ['event_count', 'netinc', 'revenue'], 'func': f47_frem_077_event_count_during_margin_drop_4q_d2}, 'f47_frem_078_event_count_when_debt_growing_d2': {'inputs': ['event_count', 'debt'], 'func': f47_frem_078_event_count_when_debt_growing_d2}, 'f47_frem_079_event_count_when_ncfo_decel_d2': {'inputs': ['event_count', 'ncfo'], 'func': f47_frem_079_event_count_when_ncfo_decel_d2}, 'f47_frem_080_event_count_after_4q_losses_indicator_d2': {'inputs': ['event_count', 'netinc'], 'func': f47_frem_080_event_count_after_4q_losses_indicator_d2}, 'f47_frem_081_restatement_during_decel_indicator_d2': {'inputs': ['event_restatement', 'revenue'], 'func': f47_frem_081_restatement_during_decel_indicator_d2}, 'f47_frem_082_auditor_change_with_loss_indicator_d2': {'inputs': ['event_auditor_change', 'netinc'], 'func': f47_frem_082_auditor_change_with_loss_indicator_d2}, 'f47_frem_083_exec_departure_with_revenue_decline_indicator_d2': {'inputs': ['event_executive_departure', 'revenue'], 'func': f47_frem_083_exec_departure_with_revenue_decline_indicator_d2}, 'f47_frem_084_writedown_with_debt_growth_indicator_d2': {'inputs': ['event_material_writedown', 'debt'], 'func': f47_frem_084_writedown_with_debt_growth_indicator_d2}, 'f47_frem_085_event_count_yoy_when_growth_slowing_d2': {'inputs': ['event_count', 'revenue'], 'func': f47_frem_085_event_count_yoy_when_growth_slowing_d2}, 'f47_frem_086_event_count_during_dilution_proxy_d2': {'inputs': ['event_count', 'sharesbas'], 'func': f47_frem_086_event_count_during_dilution_proxy_d2}, 'f47_frem_087_governance_red_flags_during_blowoff_proxy_d2': {'inputs': ['event_auditor_change', 'event_executive_departure', 'event_restatement', 'revenue'], 'func': f47_frem_087_governance_red_flags_during_blowoff_proxy_d2}, 'f47_frem_088_event_acceleration_during_decel_d2': {'inputs': ['event_count', 'revenue'], 'func': f47_frem_088_event_acceleration_during_decel_d2}, 'f47_frem_089_event_intensity_per_loss_dollar_d2': {'inputs': ['event_count', 'netinc'], 'func': f47_frem_089_event_intensity_per_loss_dollar_d2}, 'f47_frem_090_action_count_during_decline_4q_d2': {'inputs': ['action_count', 'revenue'], 'func': f47_frem_090_action_count_during_decline_4q_d2}, 'f47_frem_091_reverse_split_during_loss_indicator_d2': {'inputs': ['action_reverse_split', 'netinc'], 'func': f47_frem_091_reverse_split_during_loss_indicator_d2}, 'f47_frem_092_dividend_suspension_during_revenue_decline_indicator_d2': {'inputs': ['action_dividend_suspension', 'revenue'], 'func': f47_frem_092_dividend_suspension_during_revenue_decline_indicator_d2}, 'f47_frem_093_acquisition_during_cash_burn_indicator_d2': {'inputs': ['action_acquisition', 'ncfo'], 'func': f47_frem_093_acquisition_during_cash_burn_indicator_d2}, 'f47_frem_094_ticker_change_with_loss_indicator_d2': {'inputs': ['action_ticker_change', 'netinc'], 'func': f47_frem_094_ticker_change_with_loss_indicator_d2}, 'f47_frem_095_event_count_in_8q_window_when_avg_netinc_negative_d2': {'inputs': ['event_count', 'netinc'], 'func': f47_frem_095_event_count_in_8q_window_when_avg_netinc_negative_d2}, 'f47_frem_096_event_share_during_revenue_collapse_d2': {'inputs': ['event_count', 'revenue'], 'func': f47_frem_096_event_share_during_revenue_collapse_d2}, 'f47_frem_097_event_intensity_during_decel_8q_avg_d2': {'inputs': ['event_count', 'revenue'], 'func': f47_frem_097_event_intensity_during_decel_8q_avg_d2}, 'f47_frem_098_fundamental_event_composite_d2': {'inputs': ['event_count', 'revenue'], 'func': f47_frem_098_fundamental_event_composite_d2}, 'f47_frem_099_event_count_during_assets_decline_d2': {'inputs': ['event_count', 'assets'], 'func': f47_frem_099_event_count_during_assets_decline_d2}, 'f47_frem_100_event_count_during_equity_decline_d2': {'inputs': ['event_count', 'equity'], 'func': f47_frem_100_event_count_during_equity_decline_d2}, 'f47_frem_101_event_clustering_overdispersion_8q_d2': {'inputs': ['event_count'], 'func': f47_frem_101_event_clustering_overdispersion_8q_d2}, 'f47_frem_102_event_burst_indicator_d2': {'inputs': ['event_count'], 'func': f47_frem_102_event_burst_indicator_d2}, 'f47_frem_103_event_burst_count_8q_d2': {'inputs': ['event_count'], 'func': f47_frem_103_event_burst_count_8q_d2}, 'f47_frem_104_event_count_autocorr_lag1_8q_d2': {'inputs': ['event_count'], 'func': f47_frem_104_event_count_autocorr_lag1_8q_d2}, 'f47_frem_105_event_count_jumpiness_8q_d2': {'inputs': ['event_count'], 'func': f47_frem_105_event_count_jumpiness_8q_d2}, 'f47_frem_106_event_count_step_change_size_8q_d2': {'inputs': ['event_count'], 'func': f47_frem_106_event_count_step_change_size_8q_d2}, 'f47_frem_107_governance_event_sequence_score_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure'], 'func': f47_frem_107_governance_event_sequence_score_d2}, 'f47_frem_108_action_event_alignment_indicator_d2': {'inputs': ['action_count', 'event_count'], 'func': f47_frem_108_action_event_alignment_indicator_d2}, 'f47_frem_109_event_count_consec_positive_runs_8q_d2': {'inputs': ['event_count'], 'func': f47_frem_109_event_count_consec_positive_runs_8q_d2}, 'f47_frem_110_event_count_below_baseline_consec_streak_d2': {'inputs': ['event_count'], 'func': f47_frem_110_event_count_below_baseline_consec_streak_d2}, 'f47_frem_111_quarters_since_any_red_flag_d2': {'inputs': ['event_restatement', 'event_auditor_change', 'event_sec_investigation', 'event_class_action_lawsuit'], 'func': f47_frem_111_quarters_since_any_red_flag_d2}, 'f47_frem_112_red_flag_density_8q_d2': {'inputs': ['event_restatement', 'event_auditor_change', 'event_sec_investigation', 'event_class_action_lawsuit'], 'func': f47_frem_112_red_flag_density_8q_d2}, 'f47_frem_113_red_flag_density_12q_d2': {'inputs': ['event_restatement', 'event_auditor_change', 'event_sec_investigation', 'event_class_action_lawsuit'], 'func': f47_frem_113_red_flag_density_12q_d2}, 'f47_frem_114_red_flag_acceleration_4q_d2': {'inputs': ['event_restatement', 'event_auditor_change', 'event_sec_investigation', 'event_class_action_lawsuit'], 'func': f47_frem_114_red_flag_acceleration_4q_d2}, 'f47_frem_115_fraud_keyword_proxy_count_d2': {'inputs': ['event_sec_investigation', 'event_class_action_lawsuit'], 'func': f47_frem_115_fraud_keyword_proxy_count_d2}, 'f47_frem_116_event_count_persistence_above_median_8q_d2': {'inputs': ['event_count'], 'func': f47_frem_116_event_count_persistence_above_median_8q_d2}, 'f47_frem_117_action_persistence_above_median_8q_d2': {'inputs': ['action_count'], 'func': f47_frem_117_action_persistence_above_median_8q_d2}, 'f47_frem_118_event_count_8q_skewness_d2': {'inputs': ['event_count'], 'func': f47_frem_118_event_count_8q_skewness_d2}, 'f47_frem_119_event_count_12q_skewness_d2': {'inputs': ['event_count'], 'func': f47_frem_119_event_count_12q_skewness_d2}, 'f47_frem_120_event_count_8q_kurtosis_d2': {'inputs': ['event_count'], 'func': f47_frem_120_event_count_8q_kurtosis_d2}, 'f47_frem_121_event_distress_action_alignment_indicator_d2': {'inputs': ['event_material_writedown', 'event_auditor_change', 'action_dividend_suspension', 'action_reverse_split'], 'func': f47_frem_121_event_distress_action_alignment_indicator_d2}, 'f47_frem_122_event_severity_index_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit'], 'func': f47_frem_122_event_severity_index_d2}, 'f47_frem_123_event_severity_index_8q_max_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit'], 'func': f47_frem_123_event_severity_index_8q_max_d2}, 'f47_frem_124_event_severity_index_drawup_from_8q_min_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit'], 'func': f47_frem_124_event_severity_index_drawup_from_8q_min_d2}, 'f47_frem_125_event_severity_index_8q_slope_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit'], 'func': f47_frem_125_event_severity_index_8q_slope_d2}, 'f47_frem_126_event_severity_x_revenue_decel_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit', 'revenue'], 'func': f47_frem_126_event_severity_x_revenue_decel_d2}, 'f47_frem_127_event_severity_x_margin_drop_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit', 'netinc', 'revenue'], 'func': f47_frem_127_event_severity_x_margin_drop_d2}, 'f47_frem_128_event_severity_x_assets_decline_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit', 'assets'], 'func': f47_frem_128_event_severity_x_assets_decline_d2}, 'f47_frem_129_event_severity_during_cash_burn_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit', 'ncfo'], 'func': f47_frem_129_event_severity_during_cash_burn_d2}, 'f47_frem_130_event_severity_with_dilution_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit', 'sharesbas'], 'func': f47_frem_130_event_severity_with_dilution_d2}, 'f47_frem_131_fundamental_event_terminal_signal_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit', 'ncfo', 'netinc'], 'func': f47_frem_131_fundamental_event_terminal_signal_d2}, 'f47_frem_132_event_severity_per_assets_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit', 'assets'], 'func': f47_frem_132_event_severity_per_assets_d2}, 'f47_frem_133_event_severity_per_equity_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation', 'event_class_action_lawsuit', 'equity'], 'func': f47_frem_133_event_severity_per_equity_d2}, 'f47_frem_134_fraud_emergence_composite_8q_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure', 'event_material_writedown'], 'func': f47_frem_134_fraud_emergence_composite_8q_d2}, 'f47_frem_135_fraud_emergence_composite_12q_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure', 'event_material_writedown'], 'func': f47_frem_135_fraud_emergence_composite_12q_d2}, 'f47_frem_136_fraud_emergence_composite_qoq_change_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure', 'event_material_writedown'], 'func': f47_frem_136_fraud_emergence_composite_qoq_change_d2}, 'f47_frem_137_fraud_emergence_composite_yoy_change_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure', 'event_material_writedown'], 'func': f47_frem_137_fraud_emergence_composite_yoy_change_d2}, 'f47_frem_138_fraud_emergence_composite_zscore_8q_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure', 'event_material_writedown'], 'func': f47_frem_138_fraud_emergence_composite_zscore_8q_d2}, 'f47_frem_139_fraud_emergence_composite_8q_slope_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure', 'event_material_writedown'], 'func': f47_frem_139_fraud_emergence_composite_8q_slope_d2}, 'f47_frem_140_fraud_emergence_composite_breach_of_8q_max_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure', 'event_material_writedown'], 'func': f47_frem_140_fraud_emergence_composite_breach_of_8q_max_d2}, 'f47_frem_141_fraud_emergence_composite_persistence_above_median_8q_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure', 'event_material_writedown'], 'func': f47_frem_141_fraud_emergence_composite_persistence_above_median_8q_d2}, 'f47_frem_142_fraud_emergence_composite_during_decline_4q_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure', 'event_material_writedown', 'revenue'], 'func': f47_frem_142_fraud_emergence_composite_during_decline_4q_d2}, 'f47_frem_143_consec_quarters_with_any_red_flag_d2': {'inputs': ['event_restatement', 'event_auditor_change', 'event_sec_investigation', 'event_class_action_lawsuit'], 'func': f47_frem_143_consec_quarters_with_any_red_flag_d2}, 'f47_frem_144_consec_quarters_zero_events_d2': {'inputs': ['event_count'], 'func': f47_frem_144_consec_quarters_zero_events_d2}, 'f47_frem_145_event_jump_after_calm_indicator_d2': {'inputs': ['event_count'], 'func': f47_frem_145_event_jump_after_calm_indicator_d2}, 'f47_frem_146_governance_breakdown_indicator_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure'], 'func': f47_frem_146_governance_breakdown_indicator_d2}, 'f47_frem_147_material_event_yoy_rise_d2': {'inputs': ['event_material_writedown', 'event_restatement', 'event_sec_investigation'], 'func': f47_frem_147_material_event_yoy_rise_d2}, 'f47_frem_148_event_emergence_velocity_d2': {'inputs': ['event_count'], 'func': f47_frem_148_event_emergence_velocity_d2}, 'f47_frem_149_event_emergence_acceleration_d2': {'inputs': ['event_count'], 'func': f47_frem_149_event_emergence_acceleration_d2}, 'f47_frem_150_fraud_emergence_terminal_signal_d2': {'inputs': ['event_auditor_change', 'event_restatement', 'event_executive_departure', 'event_material_writedown', 'event_sec_investigation', 'event_class_action_lawsuit', 'revenue'], 'func': f47_frem_150_fraud_emergence_terminal_signal_d2}}