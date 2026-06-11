"""Family f77 - Price/book | silver DB normalized valuation additions third derivatives 151-156."""
import numpy as np
import pandas as pd


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return _slope(s, w).diff(periods=w)


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _bool(s):
    if s.dtype == bool:
        return s.astype(float)
    return s.fillna("").astype(str).str.upper().isin({"TRUE", "1", "Y"}).astype(float)


def pb_f77_price_book_normalized_pb_252d_accel_v151_signal(pb_normalized):
    return _clean(_accel(_mean(pb_normalized, 252), 63))


def pb_f77_price_book_pb_normalized_gap_252d_accel_v152_signal(pb, pb_normalized):
    return _clean(_accel(_mean(pb_normalized - pb, 252), 63))


def pb_f77_price_book_negative_pb_flag_accel_v153_signal(has_negative_pb):
    return _clean(_bool(has_negative_pb).diff(1).diff(1))


def pb_f77_price_book_negative_equity_flag_accel_v154_signal(has_negative_equity):
    return _clean(_bool(has_negative_equity).diff(1).diff(1))


def pb_f77_price_book_validity_adjusted_pb_accel_v155_signal(pb, pb_normalized, has_negative_pb, has_negative_equity):
    base = pb_normalized.where((_bool(has_negative_pb) + _bool(has_negative_equity)).gt(0), pb)
    return _clean(_accel(base, 63))


def pb_f77_price_book_invalid_pb_rate_252d_accel_v156_signal(has_negative_pb, has_negative_equity):
    flags = ((_bool(has_negative_pb) + _bool(has_negative_equity)) > 0).astype(float)
    return _clean(_accel(_mean(flags, 252), 63))
