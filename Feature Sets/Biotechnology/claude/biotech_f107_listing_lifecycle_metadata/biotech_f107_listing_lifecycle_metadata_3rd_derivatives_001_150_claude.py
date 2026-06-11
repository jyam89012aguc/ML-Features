"""Family f107 - Listing lifecycle metadata from silver DB tickers/sep | third derivatives 001-012."""
import numpy as np
import pandas as pd


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return _slope(s, w).diff(periods=w)


def _days(a, b):
    return (pd.to_datetime(a, errors="coerce") - pd.to_datetime(b, errors="coerce")).dt.days.astype(float)


def _flag(value):
    return value.fillna("").astype(str).str.upper().isin({"Y", "TRUE", "1"}).astype(float)


def llm_f107_listing_lifecycle_metadata_listing_age_days_accel_v001_signal(date, firstpricedate):
    return _clean(_accel(_days(date, firstpricedate), 21))


def llm_f107_listing_lifecycle_metadata_listing_age_years_accel_v002_signal(date, firstpricedate):
    return _clean(_accel(_days(date, firstpricedate) / 365.25, 21))


def llm_f107_listing_lifecycle_metadata_log_listing_age_accel_v003_signal(date, firstpricedate):
    return _clean(_accel(np.log1p(_days(date, firstpricedate).clip(lower=0)), 21))


def llm_f107_listing_lifecycle_metadata_days_to_last_price_accel_v004_signal(date, lastpricedate):
    return _clean(_accel(_days(lastpricedate, date), 21))


def llm_f107_listing_lifecycle_metadata_lifecycle_progress_accel_v005_signal(date, firstpricedate, lastpricedate):
    base = _safe_div(_days(date, firstpricedate), _days(lastpricedate, firstpricedate))
    return _clean(_accel(base, 21))


def llm_f107_listing_lifecycle_metadata_delisted_flag_accel_v006_signal(isdelisted):
    return _clean(_flag(isdelisted).diff(1).diff(1))


def llm_f107_listing_lifecycle_metadata_stale_price_window_accel_v007_signal(date, lastpricedate):
    return _clean((_days(lastpricedate, date) < 0).astype(float).diff(1).diff(1))


def llm_f107_listing_lifecycle_metadata_new_listing_flag_accel_v008_signal(date, firstpricedate):
    return _clean((_days(date, firstpricedate).between(0, 365)).astype(float).diff(21).diff(21))


def llm_f107_listing_lifecycle_metadata_mature_listing_flag_accel_v009_signal(date, firstpricedate):
    return _clean((_days(date, firstpricedate) >= 3650).astype(float).diff(21).diff(21))


def llm_f107_listing_lifecycle_metadata_exchange_changed_flag_accel_v010_signal(exchange):
    return _clean(exchange.fillna("").astype(str).ne("").astype(float).diff(1).diff(1))


def llm_f107_listing_lifecycle_metadata_common_stock_category_flag_accel_v011_signal(category):
    base = category.fillna("").astype(str).str.lower().str.contains("common stock", regex=False).astype(float)
    return _clean(base.diff(1).diff(1))


def llm_f107_listing_lifecycle_metadata_biotech_industry_flag_accel_v012_signal(industry, sicindustry):
    text = industry.fillna("").astype(str).str.cat(sicindustry.fillna("").astype(str), sep=" ").str.lower()
    return _clean(text.str.contains("biotech", regex=False).astype(float).diff(1).diff(1))
