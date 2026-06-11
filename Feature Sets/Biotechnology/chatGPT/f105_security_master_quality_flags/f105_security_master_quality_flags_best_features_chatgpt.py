"""Family f105 - Security master and validated-fundamental quality flags.

Sharadar tables: TICKERS, FUNDAMENTALS, SEP, DAILY_PRICES
Fields: exchange, isdelisted, category, siccode, sicsector, sicindustry,
famasector, famaindustry, sector, industry, scalemarketcap, scalerevenue,
relatedtickers, currency, location, firstadded, firstpricedate, lastpricedate,
firstquarter, lastquarter, secfilings, companysite, quality_flag, is_active,
has_negative_pe, has_negative_pb, has_negative_earnings, has_negative_equity,
is_turnaround_candidate, is_growth_reinvesting, pe_normalized, pb_normalized,
alternative_valuation_needed.

The generated metadata families mostly use numeric fundamentals. This module
adds explicit raw universe, listing, quality, and validation flags available in
silverdb.
"""
import numpy as np
import pandas as pd


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


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
    return _clean((a - b).dt.days.astype(float))


def smq_f105_is_delisted_signal(isdelisted):
    return _bool(isdelisted)


def smq_f105_is_active_signal(is_active):
    return _bool(is_active)


def smq_f105_major_exchange_signal(exchange):
    return _contains(exchange, "NASDAQ|NYSE|AMEX")


def smq_f105_otc_or_pink_signal(exchange):
    return _contains(exchange, "OTC|PINK")


def smq_f105_healthcare_sector_signal(sector):
    return _contains(sector, "HEALTH")


def smq_f105_biotech_industry_signal(industry, sicindustry):
    return _contains(industry, "BIOTECH|PHARMA") + _contains(sicindustry, "PHARM|BIOLOG")


def smq_f105_medical_device_industry_signal(industry, sicindustry):
    return _contains(industry, "MEDICAL DEVICE") + _contains(sicindustry, "SURGICAL|MEDICAL|ELECTROMEDICAL")


def smq_f105_shell_company_signal(industry, sicindustry, category):
    return _contains(industry, "SHELL|BLANK CHECK") + _contains(sicindustry, "BLANK CHECK") + _contains(category, "SPAC|SHELL")


def smq_f105_us_listing_signal(location):
    return _contains(location, "U.S.|USA|UNITED STATES")


def smq_f105_has_related_tickers_signal(relatedtickers):
    return _notna(relatedtickers)


def smq_f105_related_ticker_count_signal(relatedtickers):
    return relatedtickers.astype("string").str.split(",").map(lambda x: 0.0 if x == ["<NA>"] else float(len([v for v in x if v]))).replace([np.inf, -np.inf], np.nan)


def smq_f105_has_secfilings_signal(secfilings):
    return _notna(secfilings)


def smq_f105_has_companysite_signal(companysite):
    return _notna(companysite)


def smq_f105_listing_age_days_signal(date, firstpricedate):
    return _date_age_days(date, firstpricedate)


def smq_f105_days_to_last_price_signal(date, lastpricedate):
    return _date_age_days(lastpricedate, date)


def smq_f105_public_data_age_days_signal(date, firstadded):
    return _date_age_days(date, firstadded)


def smq_f105_first_quarter_age_days_signal(date, firstquarter):
    return _date_age_days(date, firstquarter)


def smq_f105_last_quarter_recency_days_signal(date, lastquarter):
    return _date_age_days(date, lastquarter)


def smq_f105_report_period_recency_days_signal(date, reportperiod):
    return _date_age_days(date, reportperiod)


def smq_f105_fiscal_period_q4_flag_signal(fiscalperiod):
    return _contains(fiscalperiod, "Q4|FY")


def smq_f105_fiscal_period_q1_flag_signal(fiscalperiod):
    return _contains(fiscalperiod, "Q1")


def smq_f105_microcap_scale_signal(scalemarketcap):
    return _contains(scalemarketcap, "NANO|MICRO|SMALL")


def smq_f105_pre_revenue_scale_signal(scalerevenue):
    return _contains(scalerevenue, "NANO|MICRO|NONE|ZERO|PRE")


def smq_f105_quality_bad_flag_signal(quality_flag):
    return _contains(quality_flag, "BAD|FAIL|ERROR|WARN|INVALID|QUARANTINE")


def smq_f105_has_flagged_at_signal(flagged_at):
    return _notna(flagged_at)


def smq_f105_flagged_reason_bad_signal(flagged_reason):
    return _contains(flagged_reason, "BAD|FAIL|ERROR|WARN|INVALID|NEGATIVE|OUTLIER|STALE|MISSING|DELIST")


def smq_f105_negative_pe_flag_signal(has_negative_pe):
    return _bool(has_negative_pe)


def smq_f105_negative_pb_flag_signal(has_negative_pb):
    return _bool(has_negative_pb)


def smq_f105_negative_earnings_flag_signal(has_negative_earnings):
    return _bool(has_negative_earnings)


def smq_f105_negative_equity_flag_signal(has_negative_equity):
    return _bool(has_negative_equity)


def smq_f105_turnaround_candidate_signal(is_turnaround_candidate):
    return _bool(is_turnaround_candidate)


def smq_f105_growth_reinvesting_signal(is_growth_reinvesting):
    return _bool(is_growth_reinvesting)


def smq_f105_alternative_valuation_needed_signal(alternative_valuation_needed):
    return _bool(alternative_valuation_needed)


def smq_f105_pe_normalized_signal(pe_normalized):
    return _clean(pe_normalized)


def smq_f105_pb_normalized_signal(pb_normalized):
    return _clean(pb_normalized)


def smq_f105_negative_quality_stack_signal(has_negative_pe, has_negative_pb, has_negative_earnings, has_negative_equity, alternative_valuation_needed):
    frame = pd.concat([
        smq_f105_negative_pe_flag_signal(has_negative_pe),
        smq_f105_negative_pb_flag_signal(has_negative_pb),
        smq_f105_negative_earnings_flag_signal(has_negative_earnings),
        smq_f105_negative_equity_flag_signal(has_negative_equity),
        smq_f105_alternative_valuation_needed_signal(alternative_valuation_needed),
    ], axis=1)
    return _clean(frame.sum(axis=1))
