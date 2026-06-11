import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core05 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core05_delta_21d_base_v076_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    result = _diff(series,21)
    return _clean(result)

# core06 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core06_delta_21d_base_v077_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    result = _diff(series,21)
    return _clean(result)

# core07 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core07_delta_21d_base_v078_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    result = _diff(series,21)
    return _clean(result)

# core08 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core08_delta_21d_base_v079_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    result = _diff(series,21)
    return _clean(result)

# core09 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core09_delta_21d_base_v080_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    result = _diff(series,21)
    return _clean(result)

# core00 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core00_pct_21d_base_v081_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    result = _pct_change(series,21)
    return _clean(result)

# core01 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core01_pct_21d_base_v082_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    result = _pct_change(series,21)
    return _clean(result)

# core02 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core02_pct_21d_base_v083_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    result = _pct_change(series,21)
    return _clean(result)

# core03 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core03_pct_21d_base_v084_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    result = _pct_change(series,21)
    return _clean(result)

# core04 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core04_pct_21d_base_v085_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    result = _pct_change(series,21)
    return _clean(result)

# core05 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core05_pct_21d_base_v086_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    result = _pct_change(series,21)
    return _clean(result)

# core06 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core06_pct_21d_base_v087_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    result = _pct_change(series,21)
    return _clean(result)

# core07 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core07_pct_21d_base_v088_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    result = _pct_change(series,21)
    return _clean(result)

# core08 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core08_pct_21d_base_v089_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    result = _pct_change(series,21)
    return _clean(result)

# core09 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core09_pct_21d_base_v090_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    result = _pct_change(series,21)
    return _clean(result)

# core00 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core00_ewm_21d_base_v091_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    result = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core01 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core01_ewm_21d_base_v092_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    result = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core02 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core02_ewm_21d_base_v093_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    result = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core03 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core03_ewm_21d_base_v094_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    result = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core04 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core04_ewm_21d_base_v095_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    result = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core05 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core05_ewm_21d_base_v096_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    result = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core06 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core06_ewm_21d_base_v097_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    result = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core07 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core07_ewm_21d_base_v098_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    result = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core08 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core08_ewm_21d_base_v099_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    result = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core09 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core09_ewm_21d_base_v100_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    result = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    return _clean(result)

# core00 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core00_slope_63d_base_v101_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    result = _slope(series,63)
    return _clean(result)

# core01 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core01_slope_63d_base_v102_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    result = _slope(series,63)
    return _clean(result)

# core02 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core02_slope_63d_base_v103_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    result = _slope(series,63)
    return _clean(result)

# core03 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core03_slope_63d_base_v104_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    result = _slope(series,63)
    return _clean(result)

# core04 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core04_slope_63d_base_v105_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    result = _slope(series,63)
    return _clean(result)

# core05 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core05_slope_63d_base_v106_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    result = _slope(series,63)
    return _clean(result)

# core06 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core06_slope_63d_base_v107_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    result = _slope(series,63)
    return _clean(result)

# core07 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core07_slope_63d_base_v108_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    result = _slope(series,63)
    return _clean(result)

# core08 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core08_slope_63d_base_v109_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    result = _slope(series,63)
    return _clean(result)

# core09 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core09_slope_63d_base_v110_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    result = _slope(series,63)
    return _clean(result)

# core00 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core00_pos_mag_63d_base_v111_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    result = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    return _clean(result)

# core01 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core01_pos_mag_63d_base_v112_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    result = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    return _clean(result)

# core02 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core02_pos_mag_63d_base_v113_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    result = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    return _clean(result)

# core03 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core03_pos_mag_63d_base_v114_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    result = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    return _clean(result)

# core04 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core04_pos_mag_63d_base_v115_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    result = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    return _clean(result)

# core05 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core05_pos_mag_63d_base_v116_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    result = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    return _clean(result)

# core06 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core06_pos_mag_63d_base_v117_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    result = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    return _clean(result)

# core07 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core07_pos_mag_63d_base_v118_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    result = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    return _clean(result)

# core08 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core08_pos_mag_63d_base_v119_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    result = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    return _clean(result)

# core09 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core09_pos_mag_63d_base_v120_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    result = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    return _clean(result)

# core00 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core00_neg_mag_63d_base_v121_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    result = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    return _clean(result)

# core01 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core01_neg_mag_63d_base_v122_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    result = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    return _clean(result)

# core02 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core02_neg_mag_63d_base_v123_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    result = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    return _clean(result)

# core03 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core03_neg_mag_63d_base_v124_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    result = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    return _clean(result)

# core04 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core04_neg_mag_63d_base_v125_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    result = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    return _clean(result)

# core05 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core05_neg_mag_63d_base_v126_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    result = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    return _clean(result)

# core06 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core06_neg_mag_63d_base_v127_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    result = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    return _clean(result)

# core07 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core07_neg_mag_63d_base_v128_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    result = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    return _clean(result)

# core08 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core08_neg_mag_63d_base_v129_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    result = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    return _clean(result)

# core09 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core09_neg_mag_63d_base_v130_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    result = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    return _clean(result)

# core00 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core00_recent_vs_long_21_126_base_v131_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    result = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    return _clean(result)

# core01 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core01_recent_vs_long_21_126_base_v132_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    result = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    return _clean(result)

# core02 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core02_recent_vs_long_21_126_base_v133_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    result = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    return _clean(result)

# core03 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core03_recent_vs_long_21_126_base_v134_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    result = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    return _clean(result)

# core04 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core04_recent_vs_long_21_126_base_v135_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    result = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    return _clean(result)

# core05 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core05_recent_vs_long_21_126_base_v136_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    result = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    return _clean(result)

# core06 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core06_recent_vs_long_21_126_base_v137_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    result = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    return _clean(result)

# core07 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core07_recent_vs_long_21_126_base_v138_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    result = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    return _clean(result)

# core08 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core08_recent_vs_long_21_126_base_v139_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    result = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    return _clean(result)

# core09 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core09_recent_vs_long_21_126_base_v140_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    result = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    return _clean(result)

# core00 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core00_centered_range_126d_base_v141_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    result = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    return _clean(result)

# core01 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core01_centered_range_126d_base_v142_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    result = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    return _clean(result)

# core02 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core02_centered_range_126d_base_v143_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    result = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    return _clean(result)

# core03 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core03_centered_range_126d_base_v144_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    result = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    return _clean(result)

# core04 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core04_centered_range_126d_base_v145_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    result = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    return _clean(result)

# core05 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core05_centered_range_126d_base_v146_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    result = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    return _clean(result)

# core06 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core06_centered_range_126d_base_v147_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    result = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    return _clean(result)

# core07 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core07_centered_range_126d_base_v148_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    result = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    return _clean(result)

# core08 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core08_centered_range_126d_base_v149_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    result = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    return _clean(result)

# core09 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core09_centered_range_126d_base_v150_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    result = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    return _clean(result)

