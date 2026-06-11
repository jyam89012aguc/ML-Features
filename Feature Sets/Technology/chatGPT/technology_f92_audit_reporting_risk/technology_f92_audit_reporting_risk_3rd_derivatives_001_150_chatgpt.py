import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 mean_5d
def cg_f92_technology_f92_audit_reporting_risk_core00_mean_5d_3rd_v001_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _mean(series,5)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 mean_5d
def cg_f92_technology_f92_audit_reporting_risk_core01_mean_5d_3rd_v002_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _mean(series,5)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 mean_5d
def cg_f92_technology_f92_audit_reporting_risk_core02_mean_5d_3rd_v003_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _mean(series,5)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 mean_5d
def cg_f92_technology_f92_audit_reporting_risk_core03_mean_5d_3rd_v004_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _mean(series,5)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 mean_5d
def cg_f92_technology_f92_audit_reporting_risk_core04_mean_5d_3rd_v005_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _mean(series,5)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 mean_5d
def cg_f92_technology_f92_audit_reporting_risk_core05_mean_5d_3rd_v006_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _mean(series,5)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 mean_5d
def cg_f92_technology_f92_audit_reporting_risk_core06_mean_5d_3rd_v007_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _mean(series,5)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 mean_5d
def cg_f92_technology_f92_audit_reporting_risk_core07_mean_5d_3rd_v008_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _mean(series,5)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 mean_5d
def cg_f92_technology_f92_audit_reporting_risk_core08_mean_5d_3rd_v009_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _mean(series,5)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 mean_5d
def cg_f92_technology_f92_audit_reporting_risk_core09_mean_5d_3rd_v010_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _mean(series,5)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 mean_21d
def cg_f92_technology_f92_audit_reporting_risk_core00_mean_21d_3rd_v011_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _mean(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 mean_21d
def cg_f92_technology_f92_audit_reporting_risk_core01_mean_21d_3rd_v012_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _mean(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 mean_21d
def cg_f92_technology_f92_audit_reporting_risk_core02_mean_21d_3rd_v013_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _mean(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 mean_21d
def cg_f92_technology_f92_audit_reporting_risk_core03_mean_21d_3rd_v014_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _mean(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 mean_21d
def cg_f92_technology_f92_audit_reporting_risk_core04_mean_21d_3rd_v015_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _mean(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 mean_21d
def cg_f92_technology_f92_audit_reporting_risk_core05_mean_21d_3rd_v016_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _mean(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 mean_21d
def cg_f92_technology_f92_audit_reporting_risk_core06_mean_21d_3rd_v017_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _mean(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 mean_21d
def cg_f92_technology_f92_audit_reporting_risk_core07_mean_21d_3rd_v018_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _mean(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 mean_21d
def cg_f92_technology_f92_audit_reporting_risk_core08_mean_21d_3rd_v019_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _mean(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 mean_21d
def cg_f92_technology_f92_audit_reporting_risk_core09_mean_21d_3rd_v020_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _mean(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 mean_63d
def cg_f92_technology_f92_audit_reporting_risk_core00_mean_63d_3rd_v021_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _mean(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 mean_63d
def cg_f92_technology_f92_audit_reporting_risk_core01_mean_63d_3rd_v022_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _mean(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 mean_63d
def cg_f92_technology_f92_audit_reporting_risk_core02_mean_63d_3rd_v023_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _mean(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 mean_63d
def cg_f92_technology_f92_audit_reporting_risk_core03_mean_63d_3rd_v024_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _mean(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 mean_63d
def cg_f92_technology_f92_audit_reporting_risk_core04_mean_63d_3rd_v025_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _mean(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 mean_63d
def cg_f92_technology_f92_audit_reporting_risk_core05_mean_63d_3rd_v026_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _mean(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 mean_63d
def cg_f92_technology_f92_audit_reporting_risk_core06_mean_63d_3rd_v027_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _mean(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 mean_63d
def cg_f92_technology_f92_audit_reporting_risk_core07_mean_63d_3rd_v028_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _mean(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 mean_63d
def cg_f92_technology_f92_audit_reporting_risk_core08_mean_63d_3rd_v029_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _mean(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 mean_63d
def cg_f92_technology_f92_audit_reporting_risk_core09_mean_63d_3rd_v030_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _mean(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 z_63d
def cg_f92_technology_f92_audit_reporting_risk_core00_z_63d_3rd_v031_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 z_63d
def cg_f92_technology_f92_audit_reporting_risk_core01_z_63d_3rd_v032_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 z_63d
def cg_f92_technology_f92_audit_reporting_risk_core02_z_63d_3rd_v033_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 z_63d
def cg_f92_technology_f92_audit_reporting_risk_core03_z_63d_3rd_v034_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 z_63d
def cg_f92_technology_f92_audit_reporting_risk_core04_z_63d_3rd_v035_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 z_63d
def cg_f92_technology_f92_audit_reporting_risk_core05_z_63d_3rd_v036_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 z_63d
def cg_f92_technology_f92_audit_reporting_risk_core06_z_63d_3rd_v037_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 z_63d
def cg_f92_technology_f92_audit_reporting_risk_core07_z_63d_3rd_v038_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 z_63d
def cg_f92_technology_f92_audit_reporting_risk_core08_z_63d_3rd_v039_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 z_63d
def cg_f92_technology_f92_audit_reporting_risk_core09_z_63d_3rd_v040_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 z_252d
def cg_f92_technology_f92_audit_reporting_risk_core00_z_252d_3rd_v041_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 z_252d
def cg_f92_technology_f92_audit_reporting_risk_core01_z_252d_3rd_v042_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 z_252d
def cg_f92_technology_f92_audit_reporting_risk_core02_z_252d_3rd_v043_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 z_252d
def cg_f92_technology_f92_audit_reporting_risk_core03_z_252d_3rd_v044_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 z_252d
def cg_f92_technology_f92_audit_reporting_risk_core04_z_252d_3rd_v045_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 z_252d
def cg_f92_technology_f92_audit_reporting_risk_core05_z_252d_3rd_v046_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 z_252d
def cg_f92_technology_f92_audit_reporting_risk_core06_z_252d_3rd_v047_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 z_252d
def cg_f92_technology_f92_audit_reporting_risk_core07_z_252d_3rd_v048_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 z_252d
def cg_f92_technology_f92_audit_reporting_risk_core08_z_252d_3rd_v049_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 z_252d
def cg_f92_technology_f92_audit_reporting_risk_core09_z_252d_3rd_v050_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 rank_126d
def cg_f92_technology_f92_audit_reporting_risk_core00_rank_126d_3rd_v051_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _rank(series,126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 rank_126d
def cg_f92_technology_f92_audit_reporting_risk_core01_rank_126d_3rd_v052_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _rank(series,126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 rank_126d
def cg_f92_technology_f92_audit_reporting_risk_core02_rank_126d_3rd_v053_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _rank(series,126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 rank_126d
def cg_f92_technology_f92_audit_reporting_risk_core03_rank_126d_3rd_v054_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _rank(series,126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 rank_126d
def cg_f92_technology_f92_audit_reporting_risk_core04_rank_126d_3rd_v055_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _rank(series,126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 rank_126d
def cg_f92_technology_f92_audit_reporting_risk_core05_rank_126d_3rd_v056_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _rank(series,126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 rank_126d
def cg_f92_technology_f92_audit_reporting_risk_core06_rank_126d_3rd_v057_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _rank(series,126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 rank_126d
def cg_f92_technology_f92_audit_reporting_risk_core07_rank_126d_3rd_v058_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _rank(series,126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 rank_126d
def cg_f92_technology_f92_audit_reporting_risk_core08_rank_126d_3rd_v059_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _rank(series,126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 rank_126d
def cg_f92_technology_f92_audit_reporting_risk_core09_rank_126d_3rd_v060_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _rank(series,126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 std_63d
def cg_f92_technology_f92_audit_reporting_risk_core00_std_63d_3rd_v061_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _std(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 std_63d
def cg_f92_technology_f92_audit_reporting_risk_core01_std_63d_3rd_v062_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _std(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 std_63d
def cg_f92_technology_f92_audit_reporting_risk_core02_std_63d_3rd_v063_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _std(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 std_63d
def cg_f92_technology_f92_audit_reporting_risk_core03_std_63d_3rd_v064_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _std(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 std_63d
def cg_f92_technology_f92_audit_reporting_risk_core04_std_63d_3rd_v065_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _std(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 std_63d
def cg_f92_technology_f92_audit_reporting_risk_core05_std_63d_3rd_v066_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _std(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 std_63d
def cg_f92_technology_f92_audit_reporting_risk_core06_std_63d_3rd_v067_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _std(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 std_63d
def cg_f92_technology_f92_audit_reporting_risk_core07_std_63d_3rd_v068_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _std(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 std_63d
def cg_f92_technology_f92_audit_reporting_risk_core08_std_63d_3rd_v069_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _std(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 std_63d
def cg_f92_technology_f92_audit_reporting_risk_core09_std_63d_3rd_v070_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _std(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core00_delta_21d_3rd_v071_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _diff(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core01_delta_21d_3rd_v072_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _diff(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core02_delta_21d_3rd_v073_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _diff(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core03_delta_21d_3rd_v074_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _diff(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core04_delta_21d_3rd_v075_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _diff(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core05_delta_21d_3rd_v076_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _diff(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core06_delta_21d_3rd_v077_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _diff(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core07_delta_21d_3rd_v078_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _diff(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core08_delta_21d_3rd_v079_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _diff(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 delta_21d
def cg_f92_technology_f92_audit_reporting_risk_core09_delta_21d_3rd_v080_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _diff(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core00_pct_21d_3rd_v081_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _pct_change(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core01_pct_21d_3rd_v082_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _pct_change(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core02_pct_21d_3rd_v083_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _pct_change(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core03_pct_21d_3rd_v084_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _pct_change(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core04_pct_21d_3rd_v085_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _pct_change(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core05_pct_21d_3rd_v086_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _pct_change(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core06_pct_21d_3rd_v087_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _pct_change(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core07_pct_21d_3rd_v088_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _pct_change(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core08_pct_21d_3rd_v089_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _pct_change(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 pct_21d
def cg_f92_technology_f92_audit_reporting_risk_core09_pct_21d_3rd_v090_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _pct_change(series,21)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core00_ewm_21d_3rd_v091_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core01_ewm_21d_3rd_v092_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core02_ewm_21d_3rd_v093_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core03_ewm_21d_3rd_v094_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core04_ewm_21d_3rd_v095_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core05_ewm_21d_3rd_v096_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core06_ewm_21d_3rd_v097_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core07_ewm_21d_3rd_v098_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core08_ewm_21d_3rd_v099_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 ewm_21d
def cg_f92_technology_f92_audit_reporting_risk_core09_ewm_21d_3rd_v100_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _ewm(series,21) + 0.01*_z(_pct_change(closeadj,21),126)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core00_slope_63d_3rd_v101_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _slope(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core01_slope_63d_3rd_v102_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _slope(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core02_slope_63d_3rd_v103_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _slope(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core03_slope_63d_3rd_v104_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _slope(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core04_slope_63d_3rd_v105_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _slope(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core05_slope_63d_3rd_v106_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _slope(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core06_slope_63d_3rd_v107_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _slope(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core07_slope_63d_3rd_v108_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _slope(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core08_slope_63d_3rd_v109_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _slope(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 slope_63d
def cg_f92_technology_f92_audit_reporting_risk_core09_slope_63d_3rd_v110_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _slope(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core00_pos_mag_63d_3rd_v111_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core01_pos_mag_63d_3rd_v112_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core02_pos_mag_63d_3rd_v113_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core03_pos_mag_63d_3rd_v114_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core04_pos_mag_63d_3rd_v115_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core05_pos_mag_63d_3rd_v116_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core06_pos_mag_63d_3rd_v117_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core07_pos_mag_63d_3rd_v118_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core08_pos_mag_63d_3rd_v119_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 pos_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core09_pos_mag_63d_3rd_v120_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _corr(series, _pct_change(closeadj,21),126) + 0.01*_z(series,63)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core00_neg_mag_63d_3rd_v121_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core01_neg_mag_63d_3rd_v122_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core02_neg_mag_63d_3rd_v123_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core03_neg_mag_63d_3rd_v124_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core04_neg_mag_63d_3rd_v125_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core05_neg_mag_63d_3rd_v126_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core06_neg_mag_63d_3rd_v127_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core07_neg_mag_63d_3rd_v128_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core08_neg_mag_63d_3rd_v129_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 neg_mag_63d
def cg_f92_technology_f92_audit_reporting_risk_core09_neg_mag_63d_3rd_v130_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _corr(series, _pct_change(closeadj,63),126) - 0.01*_z(series,252)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core00_recent_vs_long_21_126_3rd_v131_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core01_recent_vs_long_21_126_3rd_v132_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core02_recent_vs_long_21_126_3rd_v133_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core03_recent_vs_long_21_126_3rd_v134_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core04_recent_vs_long_21_126_3rd_v135_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core05_recent_vs_long_21_126_3rd_v136_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core06_recent_vs_long_21_126_3rd_v137_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core07_recent_vs_long_21_126_3rd_v138_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core08_recent_vs_long_21_126_3rd_v139_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 recent_vs_long_21_126
def cg_f92_technology_f92_audit_reporting_risk_core09_recent_vs_long_21_126_3rd_v140_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _safe_div(_mean(series,21), _mean(series,126).abs()+1e-9)-1.0
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core00 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core00_centered_range_126d_3rd_v141_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(nt_filing_event,252)+0.1*_z(days_since_filing,252)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core01 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core01_centered_range_126d_3rd_v142_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(late_filings_count,252)+0.05*_z(_pct_change(closeadj,21),126)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core02 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core02_centered_range_126d_3rd_v143_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(non_reliance_event,252)*_std(_pct_change(closeadj,1),63)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core03 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core03_centered_range_126d_3rd_v144_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_rate(going_concern_event,252)*_safe_div(_diff(marketcap,63),_std(marketcap,252).abs()+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core04 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core04_centered_range_126d_3rd_v145_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_restatement,252)+0.02*_z(_pct_change(closeadj,63),252)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core05 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core05_centered_range_126d_3rd_v146_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_sec_investigation,252)+0.02*_z(days_since_filing,126)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core06 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core06_centered_range_126d_3rd_v147_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _event_count(event_auditor_change,252)+0.02*_z(_std(_pct_change(closeadj,1),21),126)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core07 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core07_centered_range_126d_3rd_v148_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(nt_filing_event+late_filings_count,252),days_since_filing.abs()+1.0)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core08 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core08_centered_range_126d_3rd_v149_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _corr(_event_flag(nt_filing_event+event_restatement),_pct_change(closeadj,21),252)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

# core09 centered_range_126d
def cg_f92_technology_f92_audit_reporting_risk_core09_centered_range_126d_3rd_v150_signal(nt_filing_event, late_filings_count, non_reliance_event, going_concern_event, event_restatement, event_sec_investigation, event_auditor_change, days_since_filing, closeadj, marketcap):
    series = _safe_div(_event_count(non_reliance_event+going_concern_event+event_sec_investigation,252),_rank(marketcap,252)+1e-9)
    base = _safe_div(series-_mean(series,126), (_max(series,126)-_min(series,126)).abs()+1e-9)
    speed = _safe_div(_diff(base,21), _std(base,63).abs()+1e-9)
    result = _safe_div(_diff(speed,21), _std(speed,63).abs()+1e-9)
    return _clean(result)

