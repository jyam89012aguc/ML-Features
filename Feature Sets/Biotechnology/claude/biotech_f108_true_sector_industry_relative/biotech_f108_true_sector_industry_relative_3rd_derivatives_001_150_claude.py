"""Family f108 - True sector/industry relative inputs | third derivatives 001-012."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return _slope(s, w).diff(periods=w)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _runway(cashneq, ncfo):
    burn = (-ncfo).where(ncfo < 0)
    return _safe_div(cashneq, burn.abs())


def tsir_f108_true_sector_industry_relative_cash_runway_vs_industry_median_accel_v001_signal(cashneq, ncfo, industry_cash_runway_median):
    return _clean(_accel(_runway(cashneq, ncfo) - industry_cash_runway_median, 63))


def tsir_f108_true_sector_industry_relative_cash_runway_industry_percentile_accel_v002_signal(industry_cash_runway_percentile):
    return _clean(_accel(industry_cash_runway_percentile, 63))


def tsir_f108_true_sector_industry_relative_cash_marketcap_vs_industry_median_accel_v003_signal(cashneq, marketcap, industry_cash_marketcap_median):
    return _clean(_accel(_safe_div(cashneq, marketcap.abs()) - industry_cash_marketcap_median, 63))


def tsir_f108_true_sector_industry_relative_rnd_marketcap_vs_industry_median_accel_v004_signal(rnd, marketcap, industry_rnd_marketcap_median):
    return _clean(_accel(_safe_div(rnd, marketcap.abs()) - industry_rnd_marketcap_median, 63))


def tsir_f108_true_sector_industry_relative_burn_marketcap_vs_industry_median_accel_v005_signal(ncfo, marketcap, industry_burn_marketcap_median):
    burn = (-ncfo).where(ncfo < 0)
    return _clean(_accel(_safe_div(burn, marketcap.abs()) - industry_burn_marketcap_median, 63))


def tsir_f108_true_sector_industry_relative_revenue_growth_industry_percentile_accel_v006_signal(industry_revenue_growth_percentile):
    return _clean(_accel(industry_revenue_growth_percentile, 63))


def tsir_f108_true_sector_industry_relative_ev_revenue_industry_percentile_accel_v007_signal(industry_ev_revenue_percentile):
    return _clean(_accel(industry_ev_revenue_percentile, 63))


def tsir_f108_true_sector_industry_relative_price_book_industry_percentile_accel_v008_signal(industry_price_book_percentile):
    return _clean(_accel(industry_price_book_percentile, 63))


def tsir_f108_true_sector_industry_relative_biotech_cash_strength_score_accel_v009_signal(industry_cash_runway_percentile, industry_cash_marketcap_percentile):
    return _clean(_accel((industry_cash_runway_percentile + industry_cash_marketcap_percentile) / 2, 63))


def tsir_f108_true_sector_industry_relative_biotech_funding_pressure_score_accel_v010_signal(industry_cash_runway_percentile, industry_burn_marketcap_percentile):
    return _clean(_accel(industry_burn_marketcap_percentile - industry_cash_runway_percentile, 63))


def tsir_f108_true_sector_industry_relative_biotech_rnd_commitment_score_accel_v011_signal(industry_rnd_marketcap_percentile, industry_cash_runway_percentile):
    return _clean(_accel(industry_rnd_marketcap_percentile * industry_cash_runway_percentile, 63))


def tsir_f108_true_sector_industry_relative_biotech_relative_quality_252d_accel_v012_signal(industry_cash_runway_percentile, industry_revenue_growth_percentile, industry_ev_revenue_percentile):
    raw = industry_cash_runway_percentile + industry_revenue_growth_percentile - industry_ev_revenue_percentile
    return _clean(_accel(_mean(raw, 252), 63))
