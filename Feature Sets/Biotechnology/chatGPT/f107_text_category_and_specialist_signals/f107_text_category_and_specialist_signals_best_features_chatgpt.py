"""Family f107 - Text category and specialist ownership signals.

Sharadar tables: SF2, SF3, TICKERS, INDICATORS
Fields: investorname, securitytype, officertitle, securitytitle,
natureofownership, directorindirect, issuername, ownername, table, isfilter,
isprimarykey, title, description, unittype, currency, sicsector, famasector,
famaindustry, siccode, cusips, permaticker.

These are intentionally compact text/category features. They use fields that
remain after the numeric source-backed batches and avoid high-cardinality raw
IDs except for simple availability/quality flags.
"""
import numpy as np


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _contains(s, pattern):
    return s.astype("string").str.upper().str.contains(pattern, regex=True, na=False).astype(float)


def _notna(s):
    return s.notna().astype(float)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def tcs_f107_sf3_common_share_security_signal(securitytype):
    return _contains(securitytype, "^SHR$")


def tcs_f107_sf3_fund_security_signal(securitytype):
    return _contains(securitytype, "^FND$")


def tcs_f107_sf3_option_security_signal(securitytype):
    return _contains(securitytype, "^CLL$|^PUT$")


def tcs_f107_sf3_warrant_security_signal(securitytype):
    return _contains(securitytype, "^WNT$")


def tcs_f107_sf3_senior_security_signal(securitytype):
    return _contains(securitytype, "^DBT$|^PRF$")


def tcs_f107_investor_biotech_specialist_signal(investorname):
    return _contains(investorname, "BAKER BROS|ORBIMED|PERCEPTIVE|RA CAPITAL|BVF|VENBIO|FRAZIER|RTW|REDMILE|DEERFIELD|TANG CAPITAL|FARALLON|ECOR1|AISLING")


def tcs_f107_investor_index_passive_signal(investorname):
    return _contains(investorname, "VANGUARD|BLACKROCK|STATE STREET|GEODE|DIMENSIONAL|NORTHERN TRUST|INVESCO|ISHARES|FIDELITY")


def tcs_f107_investor_activist_or_event_signal(investorname):
    return _contains(investorname, "ICAHN|SABA|STARBOARD|ELLIOTT|JANA|SARISSA|CORVEX|ENGAGED CAPITAL")


def tcs_f107_specialist_ownership_value_signal(investorname, value):
    return _clean(tcs_f107_investor_biotech_specialist_signal(investorname) * value)


def tcs_f107_specialist_ownership_units_signal(investorname, units):
    return _clean(tcs_f107_investor_biotech_specialist_signal(investorname) * units)


def tcs_f107_specialist_ownership_252d_mean_signal(investorname, value):
    return _clean(_mean(tcs_f107_specialist_ownership_value_signal(investorname, value), 252))


def tcs_f107_ceo_title_signal(officertitle):
    return _contains(officertitle, "CEO|CHIEF EXECUTIVE")


def tcs_f107_cfo_title_signal(officertitle):
    return _contains(officertitle, "CFO|CHIEF FINANCIAL")


def tcs_f107_science_medical_title_signal(officertitle):
    return _contains(officertitle, "SCIENTIFIC|MEDICAL|CLINICAL|R&D|RESEARCH")


def tcs_f107_direct_ownership_signal(directorindirect):
    return _contains(directorindirect, "^D|DIRECT")


def tcs_f107_indirect_ownership_signal(directorindirect):
    return _contains(directorindirect, "^I|INDIRECT")


def tcs_f107_trust_or_family_ownership_signal(natureofownership):
    return _contains(natureofownership, "TRUST|FAMILY|SPOUSE|CHILD|HOUSEHOLD")


def tcs_f107_option_security_title_signal(securitytitle):
    return _contains(securitytitle, "OPTION|WARRANT|RIGHT")


def tcs_f107_common_stock_security_title_signal(securitytitle):
    return _contains(securitytitle, "COMMON|ORDINARY")


def tcs_f107_issuer_owner_same_name_signal(issuername, ownername):
    issuer = issuername.astype("string").str.upper().str.strip()
    owner = ownername.astype("string").str.upper().str.strip()
    return (issuer == owner).astype(float)


def tcs_f107_indicator_is_filter_signal(isfilter):
    return _contains(isfilter, "Y|TRUE|1")


def tcs_f107_indicator_is_primary_key_signal(isprimarykey):
    return _contains(isprimarykey, "Y|TRUE|1")


def tcs_f107_indicator_financial_statement_signal(table, title, description):
    text = table.astype("string") + " " + title.astype("string") + " " + description.astype("string")
    return _contains(text, "SF1|FUNDAMENTAL|BALANCE|INCOME|CASH FLOW")


def tcs_f107_indicator_market_data_signal(table, title, description):
    text = table.astype("string") + " " + title.astype("string") + " " + description.astype("string")
    return _contains(text, "SEP|SFP|PRICE|VOLUME|MARKET")


def tcs_f107_indicator_percent_unit_signal(unittype):
    return _contains(unittype, "PERCENT|RATIO")


def tcs_f107_usd_currency_signal(currency):
    return _contains(currency, "^USD$")


def tcs_f107_has_cusip_signal(cusips):
    return _notna(cusips)


def tcs_f107_has_permaticker_signal(permaticker):
    return _notna(permaticker)


def tcs_f107_healthcare_sic_fama_signal(sicsector, famasector, famaindustry):
    text = sicsector.astype("string") + " " + famasector.astype("string") + " " + famaindustry.astype("string")
    return _contains(text, "HEALTH|MEDICAL|PHARMA|DRUG|BIOTECH")


def tcs_f107_siccode_biotech_band_signal(siccode):
    return ((siccode >= 2830) & (siccode <= 2836)).astype(float)
