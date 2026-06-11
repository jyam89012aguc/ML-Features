"""Family f55 - EPS level | silver DB diluted/USD additions base 151-156."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def eps_f55_eps_level_diluted_eps_252d_base_v151_signal(epsdil):
    return _clean(_mean(epsdil, 252))


def eps_f55_eps_level_usd_eps_252d_base_v152_signal(epsusd):
    return _clean(_mean(epsusd, 252))


def eps_f55_eps_level_basic_minus_diluted_eps_252d_base_v153_signal(eps, epsdil):
    return _clean(_mean(eps - epsdil, 252))


def eps_f55_eps_level_epsusd_to_eps_252d_base_v154_signal(epsusd, eps):
    return _clean(_mean(_safe_div(epsusd, eps.abs()), 252))


def eps_f55_eps_level_eps_to_pe_context_252d_base_v155_signal(eps, pe):
    return _clean(_mean(_safe_div(eps, pe.abs()), 252))


def eps_f55_eps_level_diluted_eps_to_pe1_context_252d_base_v156_signal(epsdil, pe1):
    return _clean(_mean(_safe_div(epsdil, pe1.abs()), 252))
