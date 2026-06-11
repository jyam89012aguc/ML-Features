
import numpy as np
import pandas as pd
from gemini_helpers import _mean, _std, _z, _pct_change, _diff, _safe_div, _slope, _log, _rank, _skew, _kurt, _autocorr


def _contains(s, pattern):
    return s.astype("string").str.upper().str.contains(pattern, regex=True, na=False).astype(float)


def _notna(s):
    return s.notna().astype(float)


def gm_f109_biotech_f109_text_category_and_specialist_signals_sf3_common_share_security_signal(securitytype):
    return _contains(securitytype, "^SHR$").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_sf3_fund_security_signal(securitytype):
    return _contains(securitytype, "^FND$").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_sf3_option_security_signal(securitytype):
    return _contains(securitytype, "^CLL$|^PUT$").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_sf3_warrant_security_signal(securitytype):
    return _contains(securitytype, "^WNT$").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_sf3_senior_security_signal(securitytype):
    return _contains(securitytype, "^DBT$|^PRF$").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_investor_biotech_specialist_signal(investorname):
    return _contains(investorname, "BAKER BROS|ORBIMED|PERCEPTIVE|RA CAPITAL|BVF|VENBIO|FRAZIER|RTW|REDMILE|DEERFIELD|TANG CAPITAL|FARALLON|ECOR1|AISLING").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_investor_index_passive_signal(investorname):
    return _contains(investorname, "VANGUARD|BLACKROCK|STATE STREET|GEODE|DIMENSIONAL|NORTHERN TRUST|INVESCO|ISHARES|FIDELITY").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_investor_activist_or_event_signal(investorname):
    return _contains(investorname, "ICAHN|SABA|STARBOARD|ELLIOTT|JANA|SARISSA|CORVEX|ENGAGED CAPITAL").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_specialist_ownership_value_signal(investorname, value):
    return (gm_f109_biotech_f109_text_category_and_specialist_signals_investor_biotech_specialist_signal(investorname) * value).replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_specialist_ownership_units_signal(investorname, units):
    return (gm_f109_biotech_f109_text_category_and_specialist_signals_investor_biotech_specialist_signal(investorname) * units).replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_specialist_ownership_252d_mean_signal(investorname, value):
    return _mean(gm_f109_biotech_f109_text_category_and_specialist_signals_specialist_ownership_value_signal(investorname, value), 252).replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_ceo_title_signal(officertitle):
    return _contains(officertitle, "CEO|CHIEF EXECUTIVE").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_cfo_title_signal(officertitle):
    return _contains(officertitle, "CFO|CHIEF FINANCIAL").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_science_medical_title_signal(officertitle):
    return _contains(officertitle, "SCIENTIFIC|MEDICAL|CLINICAL|R&D|RESEARCH").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_direct_ownership_signal(directorindirect):
    return _contains(directorindirect, "^D|DIRECT").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_indirect_ownership_signal(directorindirect):
    return _contains(directorindirect, "^I|INDIRECT").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_trust_or_family_ownership_signal(natureofownership):
    return _contains(natureofownership, "TRUST|FAMILY|SPOUSE|CHILD|HOUSEHOLD").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_option_security_title_signal(securitytitle):
    return _contains(securitytitle, "OPTION|WARRANT|RIGHT").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_common_stock_security_title_signal(securitytitle):
    return _contains(securitytitle, "COMMON|ORDINARY").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_issuer_owner_same_name_signal(issuername, ownername):
    issuer = issuername.astype("string").str.upper().str.strip()
    owner = ownername.astype("string").str.upper().str.strip()
    return (issuer == owner).astype(float).replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_indicator_is_filter_signal(isfilter):
    return _contains(isfilter, "Y|TRUE|1").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_indicator_is_primary_key_signal(isprimarykey):
    return _contains(isprimarykey, "Y|TRUE|1").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_indicator_financial_statement_signal(table, title, description):
    text = table.astype("string") + " " + title.astype("string") + " " + description.astype("string")
    return _contains(text, "SF1|FUNDAMENTAL|BALANCE|INCOME|CASH FLOW").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_indicator_market_data_signal(table, title, description):
    text = table.astype("string") + " " + title.astype("string") + " " + description.astype("string")
    return _contains(text, "SEP|SFP|PRICE|VOLUME|MARKET").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_indicator_percent_unit_signal(unittype):
    return _contains(unittype, "PERCENT|RATIO").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_usd_currency_signal(currency):
    return _contains(currency, "^USD$").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_has_cusip_signal(cusips):
    return _notna(cusips).replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_has_permaticker_signal(permaticker):
    return _notna(permaticker).replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_healthcare_sic_fama_signal(sicsector, famasector, famaindustry):
    text = sicsector.astype("string") + " " + famasector.astype("string") + " " + famaindustry.astype("string")
    return _contains(text, "HEALTH|MEDICAL|PHARMA|DRUG|BIOTECH").replace([np.inf, -np.inf], np.nan)


def gm_f109_biotech_f109_text_category_and_specialist_signals_siccode_biotech_band_signal(siccode):
    return ((siccode >= 2830) & (siccode <= 2836)).astype(float).replace([np.inf, -np.inf], np.nan)
