"""Family f107 - Listing lifecycle metadata from silver DB tickers/sep | base 001-012."""
import numpy as np
import pandas as pd


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _days(a, b):
    return (pd.to_datetime(a, errors="coerce") - pd.to_datetime(b, errors="coerce")).dt.days.astype(float)


def _flag(value):
    return value.fillna("").astype(str).str.upper().isin({"Y", "TRUE", "1"}).astype(float)


def llm_f107_listing_lifecycle_metadata_listing_age_days_base_v001_signal(date, firstpricedate):
    result = _days(date, firstpricedate)
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_listing_age_years_base_v002_signal(date, firstpricedate):
    result = _days(date, firstpricedate) / 365.25
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_log_listing_age_base_v003_signal(date, firstpricedate):
    result = np.log1p(_days(date, firstpricedate).clip(lower=0))
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_days_to_last_price_base_v004_signal(date, lastpricedate):
    result = _days(lastpricedate, date)
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_lifecycle_progress_base_v005_signal(date, firstpricedate, lastpricedate):
    age = _days(date, firstpricedate)
    total = _days(lastpricedate, firstpricedate)
    result = _safe_div(age, total)
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_delisted_flag_base_v006_signal(isdelisted):
    result = _flag(isdelisted)
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_stale_price_window_base_v007_signal(date, lastpricedate):
    result = (_days(lastpricedate, date) < 0).astype(float)
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_new_listing_flag_base_v008_signal(date, firstpricedate):
    result = (_days(date, firstpricedate).between(0, 365)).astype(float)
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_mature_listing_flag_base_v009_signal(date, firstpricedate):
    result = (_days(date, firstpricedate) >= 3650).astype(float)
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_exchange_changed_flag_base_v010_signal(exchange):
    result = exchange.fillna("").astype(str).ne("").astype(float)
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_common_stock_category_flag_base_v011_signal(category):
    result = category.fillna("").astype(str).str.lower().str.contains("common stock", regex=False).astype(float)
    return _clean(result)


def llm_f107_listing_lifecycle_metadata_biotech_industry_flag_base_v012_signal(industry, sicindustry):
    text = industry.fillna("").astype(str).str.cat(sicindustry.fillna("").astype(str), sep=" ").str.lower()
    result = text.str.contains("biotech", regex=False).astype(float)
    return _clean(result)
