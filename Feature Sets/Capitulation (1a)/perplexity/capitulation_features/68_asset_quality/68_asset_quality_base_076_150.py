"""Generated capitulation features for 68_asset_quality: asset-quality contraction.
All windows look backward only. Trading-day constants: 252/year, 63/quarter, 21/month, 5/week.
"""
import numpy as np
import pandas as pd


def _align_to_close(s, close):
    s = pd.Series(s).copy()
    close = pd.Series(close)
    return s.reindex(close.index).ffill()

def _s(s):
    return pd.Series(s).replace([np.inf, -np.inf], np.nan)

def _div(a, b):
    return _s(a) / _s(b).replace(0, np.nan)

def _z(s, w):
    x = _s(s)
    return _div(x - x.rolling(w, min_periods=max(3, w // 4)).mean(), x.rolling(w, min_periods=max(3, w // 4)).std())

def _rank(s, w):
    x = _s(s)
    return x.rolling(w, min_periods=max(3, w // 4)).rank(pct=True)

def _true_range(high, low, close):
    pc = _s(close).shift(1)
    return pd.concat([_s(high) - _s(low), (_s(high) - pc).abs(), (_s(low) - pc).abs()], axis=1).max(axis=1)

def aqy_076_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def aqy_077_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(x, _s(close))

def aqy_078_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def aqy_079_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def aqy_080_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def aqy_081_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def aqy_082_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def aqy_083_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def aqy_084_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(21)

def aqy_085_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _z(x, 63)

def aqy_086_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(x, y)

def aqy_087_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(x - y, y.abs())

def aqy_088_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _rank(x, 504)

def aqy_089_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def aqy_090_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def aqy_091_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(x, _s(close))

def aqy_092_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def aqy_093_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def aqy_094_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def aqy_095_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def aqy_096_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def aqy_097_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def aqy_098_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(126)

def aqy_099_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _z(x, 252)

def aqy_100_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(x, y)

def aqy_101_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(x - y, y.abs())

def aqy_102_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _rank(x, 21)

def aqy_103_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def aqy_104_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def aqy_105_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close))

def aqy_106_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def aqy_107_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def aqy_108_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

def aqy_109_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _s(x).pct_change(15) - _s(x).pct_change(63)

def aqy_110_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def aqy_111_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _div(_s(x).rolling(252, min_periods=max(3, 252//4)).min(), _s(x).rolling(252, min_periods=max(3, 252//4)).max())

def aqy_112_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _s(x).pct_change(504)

def aqy_113_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _z(x, 756)

def aqy_114_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(x, y)

def aqy_115_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(x - y, y.abs())

def aqy_116_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _rank(x, 126)

def aqy_117_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return x.rolling(252, min_periods=max(3, 252//4)).mean().diff(63)

def aqy_118_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _s(x).rolling(504, min_periods=max(3, 504//4)).std()

def aqy_119_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close))

def aqy_120_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(x, _s(close).rolling(21, min_periods=max(3, 21//4)).mean())

def aqy_121_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return (_s(x) < 0).rolling(63, min_periods=max(3, 63//4)).mean()

def aqy_122_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _s(x).diff().rolling(126, min_periods=max(3, 126//4)).sum()

def aqy_123_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _s(x).pct_change(63) - _s(x).pct_change(252)

def aqy_124_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def aqy_125_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _div(_s(x).rolling(756, min_periods=max(3, 756//4)).min(), _s(x).rolling(756, min_periods=max(3, 756//4)).max())

def aqy_126_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _s(x).pct_change(21)

def aqy_127_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _z(x, 63)

def aqy_128_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(x, y)

def aqy_129_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(x - y, y.abs())

def aqy_130_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _rank(x, 504)

def aqy_131_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return x.rolling(756, min_periods=max(3, 756//4)).mean().diff(189)

def aqy_132_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _s(x).rolling(21, min_periods=max(3, 21//4)).std()

def aqy_133_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close))

def aqy_134_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(x, _s(close).rolling(126, min_periods=max(3, 126//4)).mean())

def aqy_135_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return (_s(x) < 0).rolling(252, min_periods=max(3, 252//4)).mean()

def aqy_136_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _s(x).diff().rolling(504, min_periods=max(3, 504//4)).sum()

def aqy_137_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _s(x).pct_change(189) - _s(x).pct_change(756)

def aqy_138_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(_s(x).diff(), _s(y).diff().abs())

def aqy_139_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _div(_s(x).rolling(63, min_periods=max(3, 63//4)).min(), _s(x).rolling(63, min_periods=max(3, 63//4)).max())

def aqy_140_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _s(x).pct_change(126)

def aqy_141_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _z(x, 252)

def aqy_142_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(x, y)

def aqy_143_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(x - y, y.abs())

def aqy_144_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return _rank(x, 21)

def aqy_145_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return x.rolling(63, min_periods=max(3, 63//4)).mean().diff(15)

def aqy_146_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assetsc, close)
    y = _align_to_close(ppe, close)
    return _s(x).rolling(126, min_periods=max(3, 126//4)).std()

def aqy_147_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(ppe, close)
    y = _align_to_close(intangibles, close)
    return _div(x, _s(close))

def aqy_148_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(intangibles, close)
    y = _align_to_close(revenue, close)
    return _div(x, _s(close).rolling(504, min_periods=max(3, 504//4)).mean())

def aqy_149_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(revenue, close)
    y = _align_to_close(assets, close)
    return (_s(x) < 0).rolling(756, min_periods=max(3, 756//4)).mean()

def aqy_150_capitulation_signal(close, assets, assetsc, ppe, intangibles, revenue):
    x = _align_to_close(assets, close)
    y = _align_to_close(assetsc, close)
    return _s(x).diff().rolling(21, min_periods=max(3, 21//4)).sum()

ASSET_QUALITY_REGISTRY_076_150 = {
    "aqy_076_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_076_capitulation_signal},
    "aqy_077_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_077_capitulation_signal},
    "aqy_078_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_078_capitulation_signal},
    "aqy_079_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_079_capitulation_signal},
    "aqy_080_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_080_capitulation_signal},
    "aqy_081_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_081_capitulation_signal},
    "aqy_082_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_082_capitulation_signal},
    "aqy_083_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_083_capitulation_signal},
    "aqy_084_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_084_capitulation_signal},
    "aqy_085_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_085_capitulation_signal},
    "aqy_086_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_086_capitulation_signal},
    "aqy_087_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_087_capitulation_signal},
    "aqy_088_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_088_capitulation_signal},
    "aqy_089_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_089_capitulation_signal},
    "aqy_090_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_090_capitulation_signal},
    "aqy_091_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_091_capitulation_signal},
    "aqy_092_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_092_capitulation_signal},
    "aqy_093_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_093_capitulation_signal},
    "aqy_094_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_094_capitulation_signal},
    "aqy_095_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_095_capitulation_signal},
    "aqy_096_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_096_capitulation_signal},
    "aqy_097_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_097_capitulation_signal},
    "aqy_098_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_098_capitulation_signal},
    "aqy_099_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_099_capitulation_signal},
    "aqy_100_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_100_capitulation_signal},
    "aqy_101_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_101_capitulation_signal},
    "aqy_102_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_102_capitulation_signal},
    "aqy_103_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_103_capitulation_signal},
    "aqy_104_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_104_capitulation_signal},
    "aqy_105_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_105_capitulation_signal},
    "aqy_106_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_106_capitulation_signal},
    "aqy_107_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_107_capitulation_signal},
    "aqy_108_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_108_capitulation_signal},
    "aqy_109_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_109_capitulation_signal},
    "aqy_110_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_110_capitulation_signal},
    "aqy_111_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_111_capitulation_signal},
    "aqy_112_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_112_capitulation_signal},
    "aqy_113_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_113_capitulation_signal},
    "aqy_114_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_114_capitulation_signal},
    "aqy_115_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_115_capitulation_signal},
    "aqy_116_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_116_capitulation_signal},
    "aqy_117_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_117_capitulation_signal},
    "aqy_118_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_118_capitulation_signal},
    "aqy_119_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_119_capitulation_signal},
    "aqy_120_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_120_capitulation_signal},
    "aqy_121_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_121_capitulation_signal},
    "aqy_122_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_122_capitulation_signal},
    "aqy_123_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_123_capitulation_signal},
    "aqy_124_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_124_capitulation_signal},
    "aqy_125_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_125_capitulation_signal},
    "aqy_126_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_126_capitulation_signal},
    "aqy_127_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_127_capitulation_signal},
    "aqy_128_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_128_capitulation_signal},
    "aqy_129_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_129_capitulation_signal},
    "aqy_130_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_130_capitulation_signal},
    "aqy_131_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_131_capitulation_signal},
    "aqy_132_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_132_capitulation_signal},
    "aqy_133_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_133_capitulation_signal},
    "aqy_134_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_134_capitulation_signal},
    "aqy_135_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_135_capitulation_signal},
    "aqy_136_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_136_capitulation_signal},
    "aqy_137_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_137_capitulation_signal},
    "aqy_138_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_138_capitulation_signal},
    "aqy_139_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_139_capitulation_signal},
    "aqy_140_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_140_capitulation_signal},
    "aqy_141_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_141_capitulation_signal},
    "aqy_142_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_142_capitulation_signal},
    "aqy_143_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_143_capitulation_signal},
    "aqy_144_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_144_capitulation_signal},
    "aqy_145_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_145_capitulation_signal},
    "aqy_146_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_146_capitulation_signal},
    "aqy_147_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_147_capitulation_signal},
    "aqy_148_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_148_capitulation_signal},
    "aqy_149_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_149_capitulation_signal},
    "aqy_150_capitulation_signal": {"inputs": ['close', 'assets', 'assetsc', 'ppe', 'intangibles', 'revenue'], "func": aqy_150_capitulation_signal},
}
