"""Family f38 - Tangible book | silver DB diluted/per-share additions second derivatives 151-156."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def tb_f38_tangible_book_tbvps_252d_slope_v151_signal(tbvps):
    return _clean(_slope(_mean(tbvps, 252), 63))


def tb_f38_tangible_book_bvps_minus_tbvps_252d_slope_v152_signal(bvps, tbvps):
    return _clean(_slope(_mean(bvps - tbvps, 252), 63))


def tb_f38_tangible_book_diluted_tangible_equity_per_share_slope_v153_signal(equity, intangibles, shareswadil):
    return _clean(_slope(_safe_div(equity - intangibles, shareswadil.abs()), 63))


def tb_f38_tangible_book_diluted_vs_reported_tbvps_slope_v154_signal(equity, intangibles, shareswadil, tbvps):
    diluted_tbvps = _safe_div(equity - intangibles, shareswadil.abs())
    return _clean(_slope(diluted_tbvps - tbvps, 63))


def tb_f38_tangible_book_tangible_book_to_marketcap_252d_slope_v155_signal(equity, intangibles, marketcap):
    return _clean(_slope(_mean(_safe_div(equity - intangibles, marketcap.abs()), 252), 63))


def tb_f38_tangible_book_tbvps_to_price_252d_slope_v156_signal(tbvps, price):
    return _clean(_slope(_mean(_safe_div(tbvps, price.abs()), 252), 63))
