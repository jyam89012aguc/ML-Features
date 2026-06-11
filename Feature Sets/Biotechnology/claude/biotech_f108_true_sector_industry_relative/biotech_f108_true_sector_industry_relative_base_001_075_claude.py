"""Family f108 - True sector/industry relative inputs | base 001-012.

These signals expect point-in-time peer aggregates or percentile ranks from the
upstream feature join. The functions intentionally do not form peer groups
internally, which avoids lookahead from changing sector/industry membership.
"""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _runway(cashneq, ncfo):
    burn = (-ncfo).where(ncfo < 0)
    return _safe_div(cashneq, burn.abs())


def tsir_f108_true_sector_industry_relative_cash_runway_vs_industry_median_base_v001_signal(cashneq, ncfo, industry_cash_runway_median):
    result = _runway(cashneq, ncfo) - industry_cash_runway_median
    return _clean(result)


def tsir_f108_true_sector_industry_relative_cash_runway_industry_percentile_base_v002_signal(industry_cash_runway_percentile):
    return _clean(industry_cash_runway_percentile)


def tsir_f108_true_sector_industry_relative_cash_marketcap_vs_industry_median_base_v003_signal(cashneq, marketcap, industry_cash_marketcap_median):
    result = _safe_div(cashneq, marketcap.abs()) - industry_cash_marketcap_median
    return _clean(result)


def tsir_f108_true_sector_industry_relative_rnd_marketcap_vs_industry_median_base_v004_signal(rnd, marketcap, industry_rnd_marketcap_median):
    result = _safe_div(rnd, marketcap.abs()) - industry_rnd_marketcap_median
    return _clean(result)


def tsir_f108_true_sector_industry_relative_burn_marketcap_vs_industry_median_base_v005_signal(ncfo, marketcap, industry_burn_marketcap_median):
    burn = (-ncfo).where(ncfo < 0)
    result = _safe_div(burn, marketcap.abs()) - industry_burn_marketcap_median
    return _clean(result)


def tsir_f108_true_sector_industry_relative_revenue_growth_industry_percentile_base_v006_signal(industry_revenue_growth_percentile):
    return _clean(industry_revenue_growth_percentile)


def tsir_f108_true_sector_industry_relative_ev_revenue_industry_percentile_base_v007_signal(industry_ev_revenue_percentile):
    return _clean(industry_ev_revenue_percentile)


def tsir_f108_true_sector_industry_relative_price_book_industry_percentile_base_v008_signal(industry_price_book_percentile):
    return _clean(industry_price_book_percentile)


def tsir_f108_true_sector_industry_relative_biotech_cash_strength_score_base_v009_signal(industry_cash_runway_percentile, industry_cash_marketcap_percentile):
    result = (industry_cash_runway_percentile + industry_cash_marketcap_percentile) / 2
    return _clean(result)


def tsir_f108_true_sector_industry_relative_biotech_funding_pressure_score_base_v010_signal(industry_cash_runway_percentile, industry_burn_marketcap_percentile):
    result = industry_burn_marketcap_percentile - industry_cash_runway_percentile
    return _clean(result)


def tsir_f108_true_sector_industry_relative_biotech_rnd_commitment_score_base_v011_signal(industry_rnd_marketcap_percentile, industry_cash_runway_percentile):
    result = industry_rnd_marketcap_percentile * industry_cash_runway_percentile
    return _clean(result)


def tsir_f108_true_sector_industry_relative_biotech_relative_quality_252d_base_v012_signal(industry_cash_runway_percentile, industry_revenue_growth_percentile, industry_ev_revenue_percentile):
    raw = industry_cash_runway_percentile + industry_revenue_growth_percentile - industry_ev_revenue_percentile
    result = _mean(raw, 252)
    return _clean(result)
