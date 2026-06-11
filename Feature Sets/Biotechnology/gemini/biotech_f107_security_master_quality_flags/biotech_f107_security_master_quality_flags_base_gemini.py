
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr

def _contains(s, pattern):
    return s.astype("string").str.upper().str.contains(pattern, regex=True, na=False).astype(float)

def _bool(s):
    if pd.api.types.is_bool_dtype(s):
        return s.astype(float)
    return _contains(s, "TRUE|T|YES|Y|1")

def _notna(s):
    return s.notna().astype(float)

def _date_age_days(asof_date, source_date):
    a = pd.to_datetime(asof_date, errors="coerce")
    b = pd.to_datetime(source_date, errors="coerce")
    result = (a - b).dt.days.astype(float)
    return result.replace([np.inf, -np.inf], np.nan)

# v001: is delisted
def gm_f107_biotech_f107_is_delisted_v001_signal(isdelisted):
    result = _bool(isdelisted)
    return result.replace([np.inf, -np.inf], np.nan)

# v002: is active
def gm_f107_biotech_f107_is_active_v002_signal(is_active):
    result = _bool(is_active)
    return result.replace([np.inf, -np.inf], np.nan)

# v003: major exchange
def gm_f107_biotech_f107_major_exchange_v003_signal(exchange):
    result = _contains(exchange, "NASDAQ|NYSE|AMEX")
    return result.replace([np.inf, -np.inf], np.nan)

# v004: otc or pink
def gm_f107_biotech_f107_otc_or_pink_v004_signal(exchange):
    result = _contains(exchange, "OTC|PINK")
    return result.replace([np.inf, -np.inf], np.nan)

# v005: healthcare sector
def gm_f107_biotech_f107_healthcare_sector_v005_signal(sector):
    result = _contains(sector, "HEALTH")
    return result.replace([np.inf, -np.inf], np.nan)

# v006: biotech industry
def gm_f107_biotech_f107_biotech_industry_v006_signal(industry, sicindustry):
    result = _contains(industry, "BIOTECH|PHARMA") + _contains(sicindustry, "PHARM|BIOLOG")
    return result.replace([np.inf, -np.inf], np.nan)

# v007: medical device industry
def gm_f107_biotech_f107_medical_device_industry_v007_signal(industry, sicindustry):
    result = _contains(industry, "MEDICAL DEVICE") + _contains(sicindustry, "SURGICAL|MEDICAL|ELECTROMEDICAL")
    return result.replace([np.inf, -np.inf], np.nan)

# v008: shell company
def gm_f107_biotech_f107_shell_company_v008_signal(industry, sicindustry, category):
    result = _contains(industry, "SHELL|BLANK CHECK") + _contains(sicindustry, "BLANK CHECK") + _contains(category, "SPAC|SHELL")
    return result.replace([np.inf, -np.inf], np.nan)

# v009: us listing
def gm_f107_biotech_f107_us_listing_v009_signal(location):
    result = _contains(location, "U.S.|USA|UNITED STATES")
    return result.replace([np.inf, -np.inf], np.nan)

# v010: has related tickers
def gm_f107_biotech_f107_has_related_tickers_v010_signal(relatedtickers):
    result = _notna(relatedtickers)
    return result.replace([np.inf, -np.inf], np.nan)

# v011: related ticker count
def gm_f107_biotech_f107_related_ticker_count_v011_signal(relatedtickers):
    result = relatedtickers.astype("string").str.split(",").map(lambda x: 0.0 if x == ["<NA>"] else float(len([v for v in x if v])))
    return result.replace([np.inf, -np.inf], np.nan)

# v012: has secfilings
def gm_f107_biotech_f107_has_secfilings_v012_signal(secfilings):
    result = _notna(secfilings)
    return result.replace([np.inf, -np.inf], np.nan)

# v013: has companysite
def gm_f107_biotech_f107_has_companysite_v013_signal(companysite):
    result = _notna(companysite)
    return result.replace([np.inf, -np.inf], np.nan)

# v014: listing age days
def gm_f107_biotech_f107_listing_age_days_v014_signal(date, firstpricedate):
    return _date_age_days(date, firstpricedate)

# v015: days to last price
def gm_f107_biotech_f107_days_to_last_price_v015_signal(date, lastpricedate):
    return _date_age_days(lastpricedate, date)

# v016: public data age days
def gm_f107_biotech_f107_public_data_age_days_v016_signal(date, firstadded):
    return _date_age_days(date, firstadded)

# v017: first quarter age days
def gm_f107_biotech_f107_first_quarter_age_days_v017_signal(date, firstquarter):
    return _date_age_days(date, firstquarter)

# v018: last quarter recency days
def gm_f107_biotech_f107_last_quarter_recency_days_v018_signal(date, lastquarter):
    return _date_age_days(date, lastquarter)

# v019: report period recency days
def gm_f107_biotech_f107_report_period_recency_days_v019_signal(date, reportperiod):
    return _date_age_days(date, reportperiod)

# v020: fiscal period q4 flag
def gm_f107_biotech_f107_fiscal_period_q4_flag_v020_signal(fiscalperiod):
    result = _contains(fiscalperiod, "Q4|FY")
    return result.replace([np.inf, -np.inf], np.nan)

# v021: fiscal period q1 flag
def gm_f107_biotech_f107_fiscal_period_q1_flag_v021_signal(fiscalperiod):
    result = _contains(fiscalperiod, "Q1")
    return result.replace([np.inf, -np.inf], np.nan)

# v022: microcap scale
def gm_f107_biotech_f107_microcap_scale_v022_signal(scalemarketcap):
    result = _contains(scalemarketcap, "NANO|MICRO|SMALL")
    return result.replace([np.inf, -np.inf], np.nan)

# v023: pre revenue scale
def gm_f107_biotech_f107_pre_revenue_scale_v023_signal(scalerevenue):
    result = _contains(scalerevenue, "NANO|MICRO|NONE|ZERO|PRE")
    return result.replace([np.inf, -np.inf], np.nan)

# v024: quality bad flag
def gm_f107_biotech_f107_quality_bad_flag_v024_signal(quality_flag):
    result = _contains(quality_flag, "BAD|FAIL|ERROR|WARN|INVALID|QUARANTINE")
    return result.replace([np.inf, -np.inf], np.nan)

# v025: has flagged at
def gm_f107_biotech_f107_has_flagged_at_v025_signal(flagged_at):
    result = _notna(flagged_at)
    return result.replace([np.inf, -np.inf], np.nan)

# v026: flagged reason bad
def gm_f107_biotech_f107_flagged_reason_bad_v026_signal(flagged_reason):
    result = _contains(flagged_reason, "BAD|FAIL|ERROR|WARN|INVALID|NEGATIVE|OUTLIER|STALE|MISSING|DELIST")
    return result.replace([np.inf, -np.inf], np.nan)

# v027: negative pe flag
def gm_f107_biotech_f107_negative_pe_flag_v027_signal(has_negative_pe):
    result = _bool(has_negative_pe)
    return result.replace([np.inf, -np.inf], np.nan)

# v028: negative pb flag
def gm_f107_biotech_f107_negative_pb_flag_v028_signal(has_negative_pb):
    result = _bool(has_negative_pb)
    return result.replace([np.inf, -np.inf], np.nan)

# v029: negative earnings flag
def gm_f107_biotech_f107_negative_earnings_flag_v029_signal(has_negative_earnings):
    result = _bool(has_negative_earnings)
    return result.replace([np.inf, -np.inf], np.nan)

# v030: negative equity flag
def gm_f107_biotech_f107_negative_equity_flag_v030_signal(has_negative_equity):
    result = _bool(has_negative_equity)
    return result.replace([np.inf, -np.inf], np.nan)

# v031: turnaround candidate
def gm_f107_biotech_f107_turnaround_candidate_v031_signal(is_turnaround_candidate):
    result = _bool(is_turnaround_candidate)
    return result.replace([np.inf, -np.inf], np.nan)

# v032: growth reinvesting
def gm_f107_biotech_f107_growth_reinvesting_v032_signal(is_growth_reinvesting):
    result = _bool(is_growth_reinvesting)
    return result.replace([np.inf, -np.inf], np.nan)

# v033: alternative valuation needed
def gm_f107_biotech_f107_alternative_valuation_needed_v033_signal(alternative_valuation_needed):
    result = _bool(alternative_valuation_needed)
    return result.replace([np.inf, -np.inf], np.nan)

# v034: pe normalized
def gm_f107_biotech_f107_pe_normalized_v034_signal(pe_normalized):
    return pe_normalized.replace([np.inf, -np.inf], np.nan)

# v035: pb normalized
def gm_f107_biotech_f107_pb_normalized_v035_signal(pb_normalized):
    return pb_normalized.replace([np.inf, -np.inf], np.nan)

# v036: negative quality stack
def gm_f107_biotech_f107_negative_quality_stack_v036_signal(has_negative_pe, has_negative_pb, has_negative_earnings, has_negative_equity, alternative_valuation_needed):
    frame = pd.concat([
        _bool(has_negative_pe),
        _bool(has_negative_pb),
        _bool(has_negative_earnings),
        _bool(has_negative_equity),
        _bool(alternative_valuation_needed),
    ], axis=1)
    result = frame.sum(axis=1)
    return result.replace([np.inf, -np.inf], np.nan)
