"""Family f38 - Tangible book | silver DB diluted/per-share additions base 151-156."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def tb_f38_tangible_book_tbvps_252d_base_v151_signal(tbvps):
    return _clean(_mean(tbvps, 252))


def tb_f38_tangible_book_bvps_minus_tbvps_252d_base_v152_signal(bvps, tbvps):
    return _clean(_mean(bvps - tbvps, 252))


def tb_f38_tangible_book_diluted_tangible_equity_per_share_base_v153_signal(equity, intangibles, shareswadil):
    return _clean(_safe_div(equity - intangibles, shareswadil.abs()))


def tb_f38_tangible_book_diluted_vs_reported_tbvps_base_v154_signal(equity, intangibles, shareswadil, tbvps):
    diluted_tbvps = _safe_div(equity - intangibles, shareswadil.abs())
    return _clean(diluted_tbvps - tbvps)


def tb_f38_tangible_book_tangible_book_to_marketcap_252d_base_v155_signal(equity, intangibles, marketcap):
    return _clean(_mean(_safe_div(equity - intangibles, marketcap.abs()), 252))


def tb_f38_tangible_book_tbvps_to_price_252d_base_v156_signal(tbvps, price):
    return _clean(_mean(_safe_div(tbvps, price.abs()), 252))
