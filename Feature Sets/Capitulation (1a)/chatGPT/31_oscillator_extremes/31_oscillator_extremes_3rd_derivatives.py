import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    a = _s(a)
    return a / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)


def _true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)



def osc_001_return_decay_accel_1(osc_001_return_decay_roc_1):
    feature = _s(osc_001_return_decay_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def osc_007_return_decay_accel_5(osc_007_return_decay_roc_5):
    feature = _s(osc_007_return_decay_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def osc_013_return_decay_accel_42(osc_013_return_decay_roc_42):
    feature = _s(osc_013_return_decay_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def osc_179_osc_019_return_decay_42_019_accel_126(osc_154_osc_019_return_decay_42_019_roc_126):
    feature = _s(osc_154_osc_019_return_decay_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def osc_180_osc_025_return_decay_5_025_accel_378(osc_155_osc_025_return_decay_5_025_roc_378):
    feature = _s(osc_155_osc_025_return_decay_5_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















OSCILLATOR_EXTREMES_REGISTRY_3RD_DERIVATIVES = {
    'osc_001_return_decay_accel_1': {'inputs': ['osc_001_return_decay_roc_1'], 'func': osc_001_return_decay_accel_1},
    'osc_007_return_decay_accel_5': {'inputs': ['osc_007_return_decay_roc_5'], 'func': osc_007_return_decay_accel_5},
    'osc_013_return_decay_accel_42': {'inputs': ['osc_013_return_decay_roc_42'], 'func': osc_013_return_decay_accel_42},
    'osc_179_osc_019_return_decay_42_019_accel_126': {'inputs': ['osc_154_osc_019_return_decay_42_019_roc_126'], 'func': osc_179_osc_019_return_decay_42_019_accel_126},
    'osc_180_osc_025_return_decay_5_025_accel_378': {'inputs': ['osc_155_osc_025_return_decay_5_025_roc_378'], 'func': osc_180_osc_025_return_decay_5_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def oe_replacement_d3_001(oe_replacement_d2_001):
    feature = _clean(oe_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_001'] = {'inputs': ['oe_replacement_d2_001'], 'func': oe_replacement_d3_001}


def oe_replacement_d3_002(oe_replacement_d2_002):
    feature = _clean(oe_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_002'] = {'inputs': ['oe_replacement_d2_002'], 'func': oe_replacement_d3_002}


def oe_replacement_d3_003(oe_replacement_d2_003):
    feature = _clean(oe_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_003'] = {'inputs': ['oe_replacement_d2_003'], 'func': oe_replacement_d3_003}


def oe_replacement_d3_004(oe_replacement_d2_004):
    feature = _clean(oe_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_004'] = {'inputs': ['oe_replacement_d2_004'], 'func': oe_replacement_d3_004}


def oe_replacement_d3_005(oe_replacement_d2_005):
    feature = _clean(oe_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_005'] = {'inputs': ['oe_replacement_d2_005'], 'func': oe_replacement_d3_005}


def oe_replacement_d3_006(oe_replacement_d2_006):
    feature = _clean(oe_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_006'] = {'inputs': ['oe_replacement_d2_006'], 'func': oe_replacement_d3_006}


def oe_replacement_d3_007(oe_replacement_d2_007):
    feature = _clean(oe_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_007'] = {'inputs': ['oe_replacement_d2_007'], 'func': oe_replacement_d3_007}


def oe_replacement_d3_008(oe_replacement_d2_008):
    feature = _clean(oe_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_008'] = {'inputs': ['oe_replacement_d2_008'], 'func': oe_replacement_d3_008}


def oe_replacement_d3_009(oe_replacement_d2_009):
    feature = _clean(oe_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_009'] = {'inputs': ['oe_replacement_d2_009'], 'func': oe_replacement_d3_009}


def oe_replacement_d3_010(oe_replacement_d2_010):
    feature = _clean(oe_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_010'] = {'inputs': ['oe_replacement_d2_010'], 'func': oe_replacement_d3_010}


def oe_replacement_d3_011(oe_replacement_d2_011):
    feature = _clean(oe_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_011'] = {'inputs': ['oe_replacement_d2_011'], 'func': oe_replacement_d3_011}


def oe_replacement_d3_012(oe_replacement_d2_012):
    feature = _clean(oe_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_012'] = {'inputs': ['oe_replacement_d2_012'], 'func': oe_replacement_d3_012}


def oe_replacement_d3_013(oe_replacement_d2_013):
    feature = _clean(oe_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_013'] = {'inputs': ['oe_replacement_d2_013'], 'func': oe_replacement_d3_013}


def oe_replacement_d3_014(oe_replacement_d2_014):
    feature = _clean(oe_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_014'] = {'inputs': ['oe_replacement_d2_014'], 'func': oe_replacement_d3_014}


def oe_replacement_d3_015(oe_replacement_d2_015):
    feature = _clean(oe_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_015'] = {'inputs': ['oe_replacement_d2_015'], 'func': oe_replacement_d3_015}


def oe_replacement_d3_016(oe_replacement_d2_016):
    feature = _clean(oe_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_016'] = {'inputs': ['oe_replacement_d2_016'], 'func': oe_replacement_d3_016}


def oe_replacement_d3_017(oe_replacement_d2_017):
    feature = _clean(oe_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_017'] = {'inputs': ['oe_replacement_d2_017'], 'func': oe_replacement_d3_017}


def oe_replacement_d3_018(oe_replacement_d2_018):
    feature = _clean(oe_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_018'] = {'inputs': ['oe_replacement_d2_018'], 'func': oe_replacement_d3_018}


def oe_replacement_d3_019(oe_replacement_d2_019):
    feature = _clean(oe_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_019'] = {'inputs': ['oe_replacement_d2_019'], 'func': oe_replacement_d3_019}


def oe_replacement_d3_020(oe_replacement_d2_020):
    feature = _clean(oe_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_020'] = {'inputs': ['oe_replacement_d2_020'], 'func': oe_replacement_d3_020}


def oe_replacement_d3_021(oe_replacement_d2_021):
    feature = _clean(oe_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_021'] = {'inputs': ['oe_replacement_d2_021'], 'func': oe_replacement_d3_021}


def oe_replacement_d3_022(oe_replacement_d2_022):
    feature = _clean(oe_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_022'] = {'inputs': ['oe_replacement_d2_022'], 'func': oe_replacement_d3_022}


def oe_replacement_d3_023(oe_replacement_d2_023):
    feature = _clean(oe_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_023'] = {'inputs': ['oe_replacement_d2_023'], 'func': oe_replacement_d3_023}


def oe_replacement_d3_024(oe_replacement_d2_024):
    feature = _clean(oe_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_024'] = {'inputs': ['oe_replacement_d2_024'], 'func': oe_replacement_d3_024}


def oe_replacement_d3_025(oe_replacement_d2_025):
    feature = _clean(oe_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_025'] = {'inputs': ['oe_replacement_d2_025'], 'func': oe_replacement_d3_025}


def oe_replacement_d3_026(oe_replacement_d2_026):
    feature = _clean(oe_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_026'] = {'inputs': ['oe_replacement_d2_026'], 'func': oe_replacement_d3_026}


def oe_replacement_d3_027(oe_replacement_d2_027):
    feature = _clean(oe_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_027'] = {'inputs': ['oe_replacement_d2_027'], 'func': oe_replacement_d3_027}


def oe_replacement_d3_028(oe_replacement_d2_028):
    feature = _clean(oe_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_028'] = {'inputs': ['oe_replacement_d2_028'], 'func': oe_replacement_d3_028}


def oe_replacement_d3_029(oe_replacement_d2_029):
    feature = _clean(oe_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_029'] = {'inputs': ['oe_replacement_d2_029'], 'func': oe_replacement_d3_029}


def oe_replacement_d3_030(oe_replacement_d2_030):
    feature = _clean(oe_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_030'] = {'inputs': ['oe_replacement_d2_030'], 'func': oe_replacement_d3_030}


def oe_replacement_d3_031(oe_replacement_d2_031):
    feature = _clean(oe_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_031'] = {'inputs': ['oe_replacement_d2_031'], 'func': oe_replacement_d3_031}


def oe_replacement_d3_032(oe_replacement_d2_032):
    feature = _clean(oe_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_032'] = {'inputs': ['oe_replacement_d2_032'], 'func': oe_replacement_d3_032}


def oe_replacement_d3_033(oe_replacement_d2_033):
    feature = _clean(oe_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_033'] = {'inputs': ['oe_replacement_d2_033'], 'func': oe_replacement_d3_033}


def oe_replacement_d3_034(oe_replacement_d2_034):
    feature = _clean(oe_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_034'] = {'inputs': ['oe_replacement_d2_034'], 'func': oe_replacement_d3_034}


def oe_replacement_d3_035(oe_replacement_d2_035):
    feature = _clean(oe_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_035'] = {'inputs': ['oe_replacement_d2_035'], 'func': oe_replacement_d3_035}


def oe_replacement_d3_036(oe_replacement_d2_036):
    feature = _clean(oe_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_036'] = {'inputs': ['oe_replacement_d2_036'], 'func': oe_replacement_d3_036}


def oe_replacement_d3_037(oe_replacement_d2_037):
    feature = _clean(oe_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_037'] = {'inputs': ['oe_replacement_d2_037'], 'func': oe_replacement_d3_037}


def oe_replacement_d3_038(oe_replacement_d2_038):
    feature = _clean(oe_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_038'] = {'inputs': ['oe_replacement_d2_038'], 'func': oe_replacement_d3_038}


def oe_replacement_d3_039(oe_replacement_d2_039):
    feature = _clean(oe_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_039'] = {'inputs': ['oe_replacement_d2_039'], 'func': oe_replacement_d3_039}


def oe_replacement_d3_040(oe_replacement_d2_040):
    feature = _clean(oe_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_040'] = {'inputs': ['oe_replacement_d2_040'], 'func': oe_replacement_d3_040}


def oe_replacement_d3_041(oe_replacement_d2_041):
    feature = _clean(oe_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_041'] = {'inputs': ['oe_replacement_d2_041'], 'func': oe_replacement_d3_041}


def oe_replacement_d3_042(oe_replacement_d2_042):
    feature = _clean(oe_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_042'] = {'inputs': ['oe_replacement_d2_042'], 'func': oe_replacement_d3_042}


def oe_replacement_d3_043(oe_replacement_d2_043):
    feature = _clean(oe_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_043'] = {'inputs': ['oe_replacement_d2_043'], 'func': oe_replacement_d3_043}


def oe_replacement_d3_044(oe_replacement_d2_044):
    feature = _clean(oe_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_044'] = {'inputs': ['oe_replacement_d2_044'], 'func': oe_replacement_d3_044}


def oe_replacement_d3_045(oe_replacement_d2_045):
    feature = _clean(oe_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_045'] = {'inputs': ['oe_replacement_d2_045'], 'func': oe_replacement_d3_045}


def oe_replacement_d3_046(oe_replacement_d2_046):
    feature = _clean(oe_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_046'] = {'inputs': ['oe_replacement_d2_046'], 'func': oe_replacement_d3_046}


def oe_replacement_d3_047(oe_replacement_d2_047):
    feature = _clean(oe_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_047'] = {'inputs': ['oe_replacement_d2_047'], 'func': oe_replacement_d3_047}


def oe_replacement_d3_048(oe_replacement_d2_048):
    feature = _clean(oe_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_048'] = {'inputs': ['oe_replacement_d2_048'], 'func': oe_replacement_d3_048}


def oe_replacement_d3_049(oe_replacement_d2_049):
    feature = _clean(oe_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_049'] = {'inputs': ['oe_replacement_d2_049'], 'func': oe_replacement_d3_049}


def oe_replacement_d3_050(oe_replacement_d2_050):
    feature = _clean(oe_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_050'] = {'inputs': ['oe_replacement_d2_050'], 'func': oe_replacement_d3_050}


def oe_replacement_d3_051(oe_replacement_d2_051):
    feature = _clean(oe_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_051'] = {'inputs': ['oe_replacement_d2_051'], 'func': oe_replacement_d3_051}


def oe_replacement_d3_052(oe_replacement_d2_052):
    feature = _clean(oe_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_052'] = {'inputs': ['oe_replacement_d2_052'], 'func': oe_replacement_d3_052}


def oe_replacement_d3_053(oe_replacement_d2_053):
    feature = _clean(oe_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_053'] = {'inputs': ['oe_replacement_d2_053'], 'func': oe_replacement_d3_053}


def oe_replacement_d3_054(oe_replacement_d2_054):
    feature = _clean(oe_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_054'] = {'inputs': ['oe_replacement_d2_054'], 'func': oe_replacement_d3_054}


def oe_replacement_d3_055(oe_replacement_d2_055):
    feature = _clean(oe_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_055'] = {'inputs': ['oe_replacement_d2_055'], 'func': oe_replacement_d3_055}


def oe_replacement_d3_056(oe_replacement_d2_056):
    feature = _clean(oe_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_056'] = {'inputs': ['oe_replacement_d2_056'], 'func': oe_replacement_d3_056}


def oe_replacement_d3_057(oe_replacement_d2_057):
    feature = _clean(oe_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_057'] = {'inputs': ['oe_replacement_d2_057'], 'func': oe_replacement_d3_057}


def oe_replacement_d3_058(oe_replacement_d2_058):
    feature = _clean(oe_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_058'] = {'inputs': ['oe_replacement_d2_058'], 'func': oe_replacement_d3_058}


def oe_replacement_d3_059(oe_replacement_d2_059):
    feature = _clean(oe_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_059'] = {'inputs': ['oe_replacement_d2_059'], 'func': oe_replacement_d3_059}


def oe_replacement_d3_060(oe_replacement_d2_060):
    feature = _clean(oe_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_060'] = {'inputs': ['oe_replacement_d2_060'], 'func': oe_replacement_d3_060}


def oe_replacement_d3_061(oe_replacement_d2_061):
    feature = _clean(oe_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_061'] = {'inputs': ['oe_replacement_d2_061'], 'func': oe_replacement_d3_061}


def oe_replacement_d3_062(oe_replacement_d2_062):
    feature = _clean(oe_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_062'] = {'inputs': ['oe_replacement_d2_062'], 'func': oe_replacement_d3_062}


def oe_replacement_d3_063(oe_replacement_d2_063):
    feature = _clean(oe_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_063'] = {'inputs': ['oe_replacement_d2_063'], 'func': oe_replacement_d3_063}


def oe_replacement_d3_064(oe_replacement_d2_064):
    feature = _clean(oe_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_064'] = {'inputs': ['oe_replacement_d2_064'], 'func': oe_replacement_d3_064}


def oe_replacement_d3_065(oe_replacement_d2_065):
    feature = _clean(oe_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_065'] = {'inputs': ['oe_replacement_d2_065'], 'func': oe_replacement_d3_065}


def oe_replacement_d3_066(oe_replacement_d2_066):
    feature = _clean(oe_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_066'] = {'inputs': ['oe_replacement_d2_066'], 'func': oe_replacement_d3_066}


def oe_replacement_d3_067(oe_replacement_d2_067):
    feature = _clean(oe_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_067'] = {'inputs': ['oe_replacement_d2_067'], 'func': oe_replacement_d3_067}


def oe_replacement_d3_068(oe_replacement_d2_068):
    feature = _clean(oe_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_068'] = {'inputs': ['oe_replacement_d2_068'], 'func': oe_replacement_d3_068}


def oe_replacement_d3_069(oe_replacement_d2_069):
    feature = _clean(oe_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_069'] = {'inputs': ['oe_replacement_d2_069'], 'func': oe_replacement_d3_069}


def oe_replacement_d3_070(oe_replacement_d2_070):
    feature = _clean(oe_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_070'] = {'inputs': ['oe_replacement_d2_070'], 'func': oe_replacement_d3_070}


def oe_replacement_d3_071(oe_replacement_d2_071):
    feature = _clean(oe_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_071'] = {'inputs': ['oe_replacement_d2_071'], 'func': oe_replacement_d3_071}


def oe_replacement_d3_072(oe_replacement_d2_072):
    feature = _clean(oe_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_072'] = {'inputs': ['oe_replacement_d2_072'], 'func': oe_replacement_d3_072}


def oe_replacement_d3_073(oe_replacement_d2_073):
    feature = _clean(oe_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_073'] = {'inputs': ['oe_replacement_d2_073'], 'func': oe_replacement_d3_073}


def oe_replacement_d3_074(oe_replacement_d2_074):
    feature = _clean(oe_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_074'] = {'inputs': ['oe_replacement_d2_074'], 'func': oe_replacement_d3_074}


def oe_replacement_d3_075(oe_replacement_d2_075):
    feature = _clean(oe_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_075'] = {'inputs': ['oe_replacement_d2_075'], 'func': oe_replacement_d3_075}


def oe_replacement_d3_076(oe_replacement_d2_076):
    feature = _clean(oe_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_076'] = {'inputs': ['oe_replacement_d2_076'], 'func': oe_replacement_d3_076}


def oe_replacement_d3_077(oe_replacement_d2_077):
    feature = _clean(oe_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_077'] = {'inputs': ['oe_replacement_d2_077'], 'func': oe_replacement_d3_077}


def oe_replacement_d3_078(oe_replacement_d2_078):
    feature = _clean(oe_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_078'] = {'inputs': ['oe_replacement_d2_078'], 'func': oe_replacement_d3_078}


def oe_replacement_d3_079(oe_replacement_d2_079):
    feature = _clean(oe_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_079'] = {'inputs': ['oe_replacement_d2_079'], 'func': oe_replacement_d3_079}


def oe_replacement_d3_080(oe_replacement_d2_080):
    feature = _clean(oe_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_080'] = {'inputs': ['oe_replacement_d2_080'], 'func': oe_replacement_d3_080}


def oe_replacement_d3_081(oe_replacement_d2_081):
    feature = _clean(oe_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_081'] = {'inputs': ['oe_replacement_d2_081'], 'func': oe_replacement_d3_081}


def oe_replacement_d3_082(oe_replacement_d2_082):
    feature = _clean(oe_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_082'] = {'inputs': ['oe_replacement_d2_082'], 'func': oe_replacement_d3_082}


def oe_replacement_d3_083(oe_replacement_d2_083):
    feature = _clean(oe_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_083'] = {'inputs': ['oe_replacement_d2_083'], 'func': oe_replacement_d3_083}


def oe_replacement_d3_084(oe_replacement_d2_084):
    feature = _clean(oe_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_084'] = {'inputs': ['oe_replacement_d2_084'], 'func': oe_replacement_d3_084}


def oe_replacement_d3_085(oe_replacement_d2_085):
    feature = _clean(oe_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_085'] = {'inputs': ['oe_replacement_d2_085'], 'func': oe_replacement_d3_085}


def oe_replacement_d3_086(oe_replacement_d2_086):
    feature = _clean(oe_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_086'] = {'inputs': ['oe_replacement_d2_086'], 'func': oe_replacement_d3_086}


def oe_replacement_d3_087(oe_replacement_d2_087):
    feature = _clean(oe_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_087'] = {'inputs': ['oe_replacement_d2_087'], 'func': oe_replacement_d3_087}


def oe_replacement_d3_088(oe_replacement_d2_088):
    feature = _clean(oe_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_088'] = {'inputs': ['oe_replacement_d2_088'], 'func': oe_replacement_d3_088}


def oe_replacement_d3_089(oe_replacement_d2_089):
    feature = _clean(oe_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_089'] = {'inputs': ['oe_replacement_d2_089'], 'func': oe_replacement_d3_089}


def oe_replacement_d3_090(oe_replacement_d2_090):
    feature = _clean(oe_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_090'] = {'inputs': ['oe_replacement_d2_090'], 'func': oe_replacement_d3_090}


def oe_replacement_d3_091(oe_replacement_d2_091):
    feature = _clean(oe_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_091'] = {'inputs': ['oe_replacement_d2_091'], 'func': oe_replacement_d3_091}


def oe_replacement_d3_092(oe_replacement_d2_092):
    feature = _clean(oe_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_092'] = {'inputs': ['oe_replacement_d2_092'], 'func': oe_replacement_d3_092}


def oe_replacement_d3_093(oe_replacement_d2_093):
    feature = _clean(oe_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_093'] = {'inputs': ['oe_replacement_d2_093'], 'func': oe_replacement_d3_093}


def oe_replacement_d3_094(oe_replacement_d2_094):
    feature = _clean(oe_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_094'] = {'inputs': ['oe_replacement_d2_094'], 'func': oe_replacement_d3_094}


def oe_replacement_d3_095(oe_replacement_d2_095):
    feature = _clean(oe_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_095'] = {'inputs': ['oe_replacement_d2_095'], 'func': oe_replacement_d3_095}


def oe_replacement_d3_096(oe_replacement_d2_096):
    feature = _clean(oe_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_096'] = {'inputs': ['oe_replacement_d2_096'], 'func': oe_replacement_d3_096}


def oe_replacement_d3_097(oe_replacement_d2_097):
    feature = _clean(oe_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_097'] = {'inputs': ['oe_replacement_d2_097'], 'func': oe_replacement_d3_097}


def oe_replacement_d3_098(oe_replacement_d2_098):
    feature = _clean(oe_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_098'] = {'inputs': ['oe_replacement_d2_098'], 'func': oe_replacement_d3_098}


def oe_replacement_d3_099(oe_replacement_d2_099):
    feature = _clean(oe_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_099'] = {'inputs': ['oe_replacement_d2_099'], 'func': oe_replacement_d3_099}


def oe_replacement_d3_100(oe_replacement_d2_100):
    feature = _clean(oe_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_100'] = {'inputs': ['oe_replacement_d2_100'], 'func': oe_replacement_d3_100}


def oe_replacement_d3_101(oe_replacement_d2_101):
    feature = _clean(oe_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_101'] = {'inputs': ['oe_replacement_d2_101'], 'func': oe_replacement_d3_101}


def oe_replacement_d3_102(oe_replacement_d2_102):
    feature = _clean(oe_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_102'] = {'inputs': ['oe_replacement_d2_102'], 'func': oe_replacement_d3_102}


def oe_replacement_d3_103(oe_replacement_d2_103):
    feature = _clean(oe_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_103'] = {'inputs': ['oe_replacement_d2_103'], 'func': oe_replacement_d3_103}


def oe_replacement_d3_104(oe_replacement_d2_104):
    feature = _clean(oe_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_104'] = {'inputs': ['oe_replacement_d2_104'], 'func': oe_replacement_d3_104}


def oe_replacement_d3_105(oe_replacement_d2_105):
    feature = _clean(oe_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_105'] = {'inputs': ['oe_replacement_d2_105'], 'func': oe_replacement_d3_105}


def oe_replacement_d3_106(oe_replacement_d2_106):
    feature = _clean(oe_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_106'] = {'inputs': ['oe_replacement_d2_106'], 'func': oe_replacement_d3_106}


def oe_replacement_d3_107(oe_replacement_d2_107):
    feature = _clean(oe_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_107'] = {'inputs': ['oe_replacement_d2_107'], 'func': oe_replacement_d3_107}


def oe_replacement_d3_108(oe_replacement_d2_108):
    feature = _clean(oe_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_108'] = {'inputs': ['oe_replacement_d2_108'], 'func': oe_replacement_d3_108}


def oe_replacement_d3_109(oe_replacement_d2_109):
    feature = _clean(oe_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_109'] = {'inputs': ['oe_replacement_d2_109'], 'func': oe_replacement_d3_109}


def oe_replacement_d3_110(oe_replacement_d2_110):
    feature = _clean(oe_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_110'] = {'inputs': ['oe_replacement_d2_110'], 'func': oe_replacement_d3_110}


def oe_replacement_d3_111(oe_replacement_d2_111):
    feature = _clean(oe_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_111'] = {'inputs': ['oe_replacement_d2_111'], 'func': oe_replacement_d3_111}


def oe_replacement_d3_112(oe_replacement_d2_112):
    feature = _clean(oe_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_112'] = {'inputs': ['oe_replacement_d2_112'], 'func': oe_replacement_d3_112}


def oe_replacement_d3_113(oe_replacement_d2_113):
    feature = _clean(oe_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_113'] = {'inputs': ['oe_replacement_d2_113'], 'func': oe_replacement_d3_113}


def oe_replacement_d3_114(oe_replacement_d2_114):
    feature = _clean(oe_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_114'] = {'inputs': ['oe_replacement_d2_114'], 'func': oe_replacement_d3_114}


def oe_replacement_d3_115(oe_replacement_d2_115):
    feature = _clean(oe_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_115'] = {'inputs': ['oe_replacement_d2_115'], 'func': oe_replacement_d3_115}


def oe_replacement_d3_116(oe_replacement_d2_116):
    feature = _clean(oe_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_116'] = {'inputs': ['oe_replacement_d2_116'], 'func': oe_replacement_d3_116}


def oe_replacement_d3_117(oe_replacement_d2_117):
    feature = _clean(oe_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_117'] = {'inputs': ['oe_replacement_d2_117'], 'func': oe_replacement_d3_117}


def oe_replacement_d3_118(oe_replacement_d2_118):
    feature = _clean(oe_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_118'] = {'inputs': ['oe_replacement_d2_118'], 'func': oe_replacement_d3_118}


def oe_replacement_d3_119(oe_replacement_d2_119):
    feature = _clean(oe_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_119'] = {'inputs': ['oe_replacement_d2_119'], 'func': oe_replacement_d3_119}


def oe_replacement_d3_120(oe_replacement_d2_120):
    feature = _clean(oe_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_120'] = {'inputs': ['oe_replacement_d2_120'], 'func': oe_replacement_d3_120}


def oe_replacement_d3_121(oe_replacement_d2_121):
    feature = _clean(oe_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_121'] = {'inputs': ['oe_replacement_d2_121'], 'func': oe_replacement_d3_121}


def oe_replacement_d3_122(oe_replacement_d2_122):
    feature = _clean(oe_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_122'] = {'inputs': ['oe_replacement_d2_122'], 'func': oe_replacement_d3_122}


def oe_replacement_d3_123(oe_replacement_d2_123):
    feature = _clean(oe_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_123'] = {'inputs': ['oe_replacement_d2_123'], 'func': oe_replacement_d3_123}


def oe_replacement_d3_124(oe_replacement_d2_124):
    feature = _clean(oe_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_124'] = {'inputs': ['oe_replacement_d2_124'], 'func': oe_replacement_d3_124}


def oe_replacement_d3_125(oe_replacement_d2_125):
    feature = _clean(oe_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_125'] = {'inputs': ['oe_replacement_d2_125'], 'func': oe_replacement_d3_125}


def oe_replacement_d3_126(oe_replacement_d2_126):
    feature = _clean(oe_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_126'] = {'inputs': ['oe_replacement_d2_126'], 'func': oe_replacement_d3_126}


def oe_replacement_d3_127(oe_replacement_d2_127):
    feature = _clean(oe_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_127'] = {'inputs': ['oe_replacement_d2_127'], 'func': oe_replacement_d3_127}


def oe_replacement_d3_128(oe_replacement_d2_128):
    feature = _clean(oe_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_128'] = {'inputs': ['oe_replacement_d2_128'], 'func': oe_replacement_d3_128}


def oe_replacement_d3_129(oe_replacement_d2_129):
    feature = _clean(oe_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_129'] = {'inputs': ['oe_replacement_d2_129'], 'func': oe_replacement_d3_129}


def oe_replacement_d3_130(oe_replacement_d2_130):
    feature = _clean(oe_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_130'] = {'inputs': ['oe_replacement_d2_130'], 'func': oe_replacement_d3_130}


def oe_replacement_d3_131(oe_replacement_d2_131):
    feature = _clean(oe_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_131'] = {'inputs': ['oe_replacement_d2_131'], 'func': oe_replacement_d3_131}


def oe_replacement_d3_132(oe_replacement_d2_132):
    feature = _clean(oe_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_132'] = {'inputs': ['oe_replacement_d2_132'], 'func': oe_replacement_d3_132}


def oe_replacement_d3_133(oe_replacement_d2_133):
    feature = _clean(oe_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_133'] = {'inputs': ['oe_replacement_d2_133'], 'func': oe_replacement_d3_133}


def oe_replacement_d3_134(oe_replacement_d2_134):
    feature = _clean(oe_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_134'] = {'inputs': ['oe_replacement_d2_134'], 'func': oe_replacement_d3_134}


def oe_replacement_d3_135(oe_replacement_d2_135):
    feature = _clean(oe_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_135'] = {'inputs': ['oe_replacement_d2_135'], 'func': oe_replacement_d3_135}


def oe_replacement_d3_136(oe_replacement_d2_136):
    feature = _clean(oe_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_136'] = {'inputs': ['oe_replacement_d2_136'], 'func': oe_replacement_d3_136}


def oe_replacement_d3_137(oe_replacement_d2_137):
    feature = _clean(oe_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_137'] = {'inputs': ['oe_replacement_d2_137'], 'func': oe_replacement_d3_137}


def oe_replacement_d3_138(oe_replacement_d2_138):
    feature = _clean(oe_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_138'] = {'inputs': ['oe_replacement_d2_138'], 'func': oe_replacement_d3_138}


def oe_replacement_d3_139(oe_replacement_d2_139):
    feature = _clean(oe_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_139'] = {'inputs': ['oe_replacement_d2_139'], 'func': oe_replacement_d3_139}


def oe_replacement_d3_140(oe_replacement_d2_140):
    feature = _clean(oe_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_140'] = {'inputs': ['oe_replacement_d2_140'], 'func': oe_replacement_d3_140}


def oe_replacement_d3_141(oe_replacement_d2_141):
    feature = _clean(oe_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_141'] = {'inputs': ['oe_replacement_d2_141'], 'func': oe_replacement_d3_141}


def oe_replacement_d3_142(oe_replacement_d2_142):
    feature = _clean(oe_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_142'] = {'inputs': ['oe_replacement_d2_142'], 'func': oe_replacement_d3_142}


def oe_replacement_d3_143(oe_replacement_d2_143):
    feature = _clean(oe_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_143'] = {'inputs': ['oe_replacement_d2_143'], 'func': oe_replacement_d3_143}


def oe_replacement_d3_144(oe_replacement_d2_144):
    feature = _clean(oe_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_144'] = {'inputs': ['oe_replacement_d2_144'], 'func': oe_replacement_d3_144}


def oe_replacement_d3_145(oe_replacement_d2_145):
    feature = _clean(oe_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_145'] = {'inputs': ['oe_replacement_d2_145'], 'func': oe_replacement_d3_145}


def oe_replacement_d3_146(oe_replacement_d2_146):
    feature = _clean(oe_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_146'] = {'inputs': ['oe_replacement_d2_146'], 'func': oe_replacement_d3_146}


def oe_replacement_d3_147(oe_replacement_d2_147):
    feature = _clean(oe_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_147'] = {'inputs': ['oe_replacement_d2_147'], 'func': oe_replacement_d3_147}


def oe_replacement_d3_148(oe_replacement_d2_148):
    feature = _clean(oe_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_148'] = {'inputs': ['oe_replacement_d2_148'], 'func': oe_replacement_d3_148}


def oe_replacement_d3_149(oe_replacement_d2_149):
    feature = _clean(oe_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_149'] = {'inputs': ['oe_replacement_d2_149'], 'func': oe_replacement_d3_149}


def oe_replacement_d3_150(oe_replacement_d2_150):
    feature = _clean(oe_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_150'] = {'inputs': ['oe_replacement_d2_150'], 'func': oe_replacement_d3_150}


def oe_replacement_d3_151(oe_replacement_d2_151):
    feature = _clean(oe_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_151'] = {'inputs': ['oe_replacement_d2_151'], 'func': oe_replacement_d3_151}


def oe_replacement_d3_152(oe_replacement_d2_152):
    feature = _clean(oe_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_152'] = {'inputs': ['oe_replacement_d2_152'], 'func': oe_replacement_d3_152}


def oe_replacement_d3_153(oe_replacement_d2_153):
    feature = _clean(oe_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_153'] = {'inputs': ['oe_replacement_d2_153'], 'func': oe_replacement_d3_153}


def oe_replacement_d3_154(oe_replacement_d2_154):
    feature = _clean(oe_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_154'] = {'inputs': ['oe_replacement_d2_154'], 'func': oe_replacement_d3_154}


def oe_replacement_d3_155(oe_replacement_d2_155):
    feature = _clean(oe_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_155'] = {'inputs': ['oe_replacement_d2_155'], 'func': oe_replacement_d3_155}


def oe_replacement_d3_156(oe_replacement_d2_156):
    feature = _clean(oe_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_156'] = {'inputs': ['oe_replacement_d2_156'], 'func': oe_replacement_d3_156}


def oe_replacement_d3_157(oe_replacement_d2_157):
    feature = _clean(oe_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_157'] = {'inputs': ['oe_replacement_d2_157'], 'func': oe_replacement_d3_157}


def oe_replacement_d3_158(oe_replacement_d2_158):
    feature = _clean(oe_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_158'] = {'inputs': ['oe_replacement_d2_158'], 'func': oe_replacement_d3_158}


def oe_replacement_d3_159(oe_replacement_d2_159):
    feature = _clean(oe_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_159'] = {'inputs': ['oe_replacement_d2_159'], 'func': oe_replacement_d3_159}


def oe_replacement_d3_160(oe_replacement_d2_160):
    feature = _clean(oe_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_160'] = {'inputs': ['oe_replacement_d2_160'], 'func': oe_replacement_d3_160}


def oe_replacement_d3_161(oe_replacement_d2_161):
    feature = _clean(oe_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_161'] = {'inputs': ['oe_replacement_d2_161'], 'func': oe_replacement_d3_161}


def oe_replacement_d3_162(oe_replacement_d2_162):
    feature = _clean(oe_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_162'] = {'inputs': ['oe_replacement_d2_162'], 'func': oe_replacement_d3_162}


def oe_replacement_d3_163(oe_replacement_d2_163):
    feature = _clean(oe_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_163'] = {'inputs': ['oe_replacement_d2_163'], 'func': oe_replacement_d3_163}


def oe_replacement_d3_164(oe_replacement_d2_164):
    feature = _clean(oe_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_164'] = {'inputs': ['oe_replacement_d2_164'], 'func': oe_replacement_d3_164}


def oe_replacement_d3_165(oe_replacement_d2_165):
    feature = _clean(oe_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_165'] = {'inputs': ['oe_replacement_d2_165'], 'func': oe_replacement_d3_165}


def oe_replacement_d3_166(oe_replacement_d2_166):
    feature = _clean(oe_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_166'] = {'inputs': ['oe_replacement_d2_166'], 'func': oe_replacement_d3_166}


def oe_replacement_d3_167(oe_replacement_d2_167):
    feature = _clean(oe_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_167'] = {'inputs': ['oe_replacement_d2_167'], 'func': oe_replacement_d3_167}


def oe_replacement_d3_168(oe_replacement_d2_168):
    feature = _clean(oe_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_168'] = {'inputs': ['oe_replacement_d2_168'], 'func': oe_replacement_d3_168}


def oe_replacement_d3_169(oe_replacement_d2_169):
    feature = _clean(oe_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_169'] = {'inputs': ['oe_replacement_d2_169'], 'func': oe_replacement_d3_169}


def oe_replacement_d3_170(oe_replacement_d2_170):
    feature = _clean(oe_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_170'] = {'inputs': ['oe_replacement_d2_170'], 'func': oe_replacement_d3_170}


def oe_replacement_d3_171(oe_replacement_d2_171):
    feature = _clean(oe_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_171'] = {'inputs': ['oe_replacement_d2_171'], 'func': oe_replacement_d3_171}


def oe_replacement_d3_172(oe_replacement_d2_172):
    feature = _clean(oe_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_172'] = {'inputs': ['oe_replacement_d2_172'], 'func': oe_replacement_d3_172}


def oe_replacement_d3_173(oe_replacement_d2_173):
    feature = _clean(oe_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_173'] = {'inputs': ['oe_replacement_d2_173'], 'func': oe_replacement_d3_173}


def oe_replacement_d3_174(oe_replacement_d2_174):
    feature = _clean(oe_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_174'] = {'inputs': ['oe_replacement_d2_174'], 'func': oe_replacement_d3_174}


def oe_replacement_d3_175(oe_replacement_d2_175):
    feature = _clean(oe_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
OE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['oe_replacement_d3_175'] = {'inputs': ['oe_replacement_d2_175'], 'func': oe_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def osc_base_universe_d3_001_osc_003_loss_streak_21_003(osc_base_universe_d2_001_osc_003_loss_streak_21_003):
    return _base_universe_d3(osc_base_universe_d2_001_osc_003_loss_streak_21_003, 1)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_001_osc_003_loss_streak_21_003'] = {'inputs': ['osc_base_universe_d2_001_osc_003_loss_streak_21_003'], 'func': osc_base_universe_d3_001_osc_003_loss_streak_21_003}


def osc_base_universe_d3_002_osc_004_ma_distance_42_004(osc_base_universe_d2_002_osc_004_ma_distance_42_004):
    return _base_universe_d3(osc_base_universe_d2_002_osc_004_ma_distance_42_004, 2)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_002_osc_004_ma_distance_42_004'] = {'inputs': ['osc_base_universe_d2_002_osc_004_ma_distance_42_004'], 'func': osc_base_universe_d3_002_osc_004_ma_distance_42_004}


def osc_base_universe_d3_003_osc_005_stochastic_position_63_005(osc_base_universe_d2_003_osc_005_stochastic_position_63_005):
    return _base_universe_d3(osc_base_universe_d2_003_osc_005_stochastic_position_63_005, 3)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_003_osc_005_stochastic_position_63_005'] = {'inputs': ['osc_base_universe_d2_003_osc_005_stochastic_position_63_005'], 'func': osc_base_universe_d3_003_osc_005_stochastic_position_63_005}


def osc_base_universe_d3_004_osc_009_loss_streak_252_009(osc_base_universe_d2_004_osc_009_loss_streak_252_009):
    return _base_universe_d3(osc_base_universe_d2_004_osc_009_loss_streak_252_009, 4)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_004_osc_009_loss_streak_252_009'] = {'inputs': ['osc_base_universe_d2_004_osc_009_loss_streak_252_009'], 'func': osc_base_universe_d3_004_osc_009_loss_streak_252_009}


def osc_base_universe_d3_005_osc_010_ma_distance_378_010(osc_base_universe_d2_005_osc_010_ma_distance_378_010):
    return _base_universe_d3(osc_base_universe_d2_005_osc_010_ma_distance_378_010, 5)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_005_osc_010_ma_distance_378_010'] = {'inputs': ['osc_base_universe_d2_005_osc_010_ma_distance_378_010'], 'func': osc_base_universe_d3_005_osc_010_ma_distance_378_010}


def osc_base_universe_d3_006_osc_011_stochastic_position_504_011(osc_base_universe_d2_006_osc_011_stochastic_position_504_011):
    return _base_universe_d3(osc_base_universe_d2_006_osc_011_stochastic_position_504_011, 6)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_006_osc_011_stochastic_position_504_011'] = {'inputs': ['osc_base_universe_d2_006_osc_011_stochastic_position_504_011'], 'func': osc_base_universe_d3_006_osc_011_stochastic_position_504_011}


def osc_base_universe_d3_007_osc_015_loss_streak_1512_015(osc_base_universe_d2_007_osc_015_loss_streak_1512_015):
    return _base_universe_d3(osc_base_universe_d2_007_osc_015_loss_streak_1512_015, 7)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_007_osc_015_loss_streak_1512_015'] = {'inputs': ['osc_base_universe_d2_007_osc_015_loss_streak_1512_015'], 'func': osc_base_universe_d3_007_osc_015_loss_streak_1512_015}


def osc_base_universe_d3_008_osc_016_ma_distance_5_016(osc_base_universe_d2_008_osc_016_ma_distance_5_016):
    return _base_universe_d3(osc_base_universe_d2_008_osc_016_ma_distance_5_016, 8)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_008_osc_016_ma_distance_5_016'] = {'inputs': ['osc_base_universe_d2_008_osc_016_ma_distance_5_016'], 'func': osc_base_universe_d3_008_osc_016_ma_distance_5_016}


def osc_base_universe_d3_009_osc_017_stochastic_position_10_017(osc_base_universe_d2_009_osc_017_stochastic_position_10_017):
    return _base_universe_d3(osc_base_universe_d2_009_osc_017_stochastic_position_10_017, 9)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_009_osc_017_stochastic_position_10_017'] = {'inputs': ['osc_base_universe_d2_009_osc_017_stochastic_position_10_017'], 'func': osc_base_universe_d3_009_osc_017_stochastic_position_10_017}


def osc_base_universe_d3_010_osc_021_loss_streak_84_021(osc_base_universe_d2_010_osc_021_loss_streak_84_021):
    return _base_universe_d3(osc_base_universe_d2_010_osc_021_loss_streak_84_021, 10)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_010_osc_021_loss_streak_84_021'] = {'inputs': ['osc_base_universe_d2_010_osc_021_loss_streak_84_021'], 'func': osc_base_universe_d3_010_osc_021_loss_streak_84_021}


def osc_base_universe_d3_011_osc_022_ma_distance_126_022(osc_base_universe_d2_011_osc_022_ma_distance_126_022):
    return _base_universe_d3(osc_base_universe_d2_011_osc_022_ma_distance_126_022, 11)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_011_osc_022_ma_distance_126_022'] = {'inputs': ['osc_base_universe_d2_011_osc_022_ma_distance_126_022'], 'func': osc_base_universe_d3_011_osc_022_ma_distance_126_022}


def osc_base_universe_d3_012_osc_023_stochastic_position_189_023(osc_base_universe_d2_012_osc_023_stochastic_position_189_023):
    return _base_universe_d3(osc_base_universe_d2_012_osc_023_stochastic_position_189_023, 12)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_012_osc_023_stochastic_position_189_023'] = {'inputs': ['osc_base_universe_d2_012_osc_023_stochastic_position_189_023'], 'func': osc_base_universe_d3_012_osc_023_stochastic_position_189_023}


def osc_base_universe_d3_013_osc_027_loss_streak_756_027(osc_base_universe_d2_013_osc_027_loss_streak_756_027):
    return _base_universe_d3(osc_base_universe_d2_013_osc_027_loss_streak_756_027, 13)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_013_osc_027_loss_streak_756_027'] = {'inputs': ['osc_base_universe_d2_013_osc_027_loss_streak_756_027'], 'func': osc_base_universe_d3_013_osc_027_loss_streak_756_027}


def osc_base_universe_d3_014_osc_028_ma_distance_1008_028(osc_base_universe_d2_014_osc_028_ma_distance_1008_028):
    return _base_universe_d3(osc_base_universe_d2_014_osc_028_ma_distance_1008_028, 14)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_014_osc_028_ma_distance_1008_028'] = {'inputs': ['osc_base_universe_d2_014_osc_028_ma_distance_1008_028'], 'func': osc_base_universe_d3_014_osc_028_ma_distance_1008_028}


def osc_base_universe_d3_015_osc_029_stochastic_position_1260_029(osc_base_universe_d2_015_osc_029_stochastic_position_1260_029):
    return _base_universe_d3(osc_base_universe_d2_015_osc_029_stochastic_position_1260_029, 15)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_015_osc_029_stochastic_position_1260_029'] = {'inputs': ['osc_base_universe_d2_015_osc_029_stochastic_position_1260_029'], 'func': osc_base_universe_d3_015_osc_029_stochastic_position_1260_029}


def osc_base_universe_d3_016_osc_basefill_001(osc_base_universe_d2_016_osc_basefill_001):
    return _base_universe_d3(osc_base_universe_d2_016_osc_basefill_001, 16)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_016_osc_basefill_001'] = {'inputs': ['osc_base_universe_d2_016_osc_basefill_001'], 'func': osc_base_universe_d3_016_osc_basefill_001}


def osc_base_universe_d3_017_osc_basefill_002(osc_base_universe_d2_017_osc_basefill_002):
    return _base_universe_d3(osc_base_universe_d2_017_osc_basefill_002, 17)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_017_osc_basefill_002'] = {'inputs': ['osc_base_universe_d2_017_osc_basefill_002'], 'func': osc_base_universe_d3_017_osc_basefill_002}


def osc_base_universe_d3_018_osc_basefill_006(osc_base_universe_d2_018_osc_basefill_006):
    return _base_universe_d3(osc_base_universe_d2_018_osc_basefill_006, 18)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_018_osc_basefill_006'] = {'inputs': ['osc_base_universe_d2_018_osc_basefill_006'], 'func': osc_base_universe_d3_018_osc_basefill_006}


def osc_base_universe_d3_019_osc_basefill_007(osc_base_universe_d2_019_osc_basefill_007):
    return _base_universe_d3(osc_base_universe_d2_019_osc_basefill_007, 19)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_019_osc_basefill_007'] = {'inputs': ['osc_base_universe_d2_019_osc_basefill_007'], 'func': osc_base_universe_d3_019_osc_basefill_007}


def osc_base_universe_d3_020_osc_basefill_008(osc_base_universe_d2_020_osc_basefill_008):
    return _base_universe_d3(osc_base_universe_d2_020_osc_basefill_008, 20)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_020_osc_basefill_008'] = {'inputs': ['osc_base_universe_d2_020_osc_basefill_008'], 'func': osc_base_universe_d3_020_osc_basefill_008}


def osc_base_universe_d3_021_osc_basefill_012(osc_base_universe_d2_021_osc_basefill_012):
    return _base_universe_d3(osc_base_universe_d2_021_osc_basefill_012, 21)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_021_osc_basefill_012'] = {'inputs': ['osc_base_universe_d2_021_osc_basefill_012'], 'func': osc_base_universe_d3_021_osc_basefill_012}


def osc_base_universe_d3_022_osc_basefill_013(osc_base_universe_d2_022_osc_basefill_013):
    return _base_universe_d3(osc_base_universe_d2_022_osc_basefill_013, 22)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_022_osc_basefill_013'] = {'inputs': ['osc_base_universe_d2_022_osc_basefill_013'], 'func': osc_base_universe_d3_022_osc_basefill_013}


def osc_base_universe_d3_023_osc_basefill_014(osc_base_universe_d2_023_osc_basefill_014):
    return _base_universe_d3(osc_base_universe_d2_023_osc_basefill_014, 23)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_023_osc_basefill_014'] = {'inputs': ['osc_base_universe_d2_023_osc_basefill_014'], 'func': osc_base_universe_d3_023_osc_basefill_014}


def osc_base_universe_d3_024_osc_basefill_018(osc_base_universe_d2_024_osc_basefill_018):
    return _base_universe_d3(osc_base_universe_d2_024_osc_basefill_018, 24)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_024_osc_basefill_018'] = {'inputs': ['osc_base_universe_d2_024_osc_basefill_018'], 'func': osc_base_universe_d3_024_osc_basefill_018}


def osc_base_universe_d3_025_osc_basefill_019(osc_base_universe_d2_025_osc_basefill_019):
    return _base_universe_d3(osc_base_universe_d2_025_osc_basefill_019, 25)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_025_osc_basefill_019'] = {'inputs': ['osc_base_universe_d2_025_osc_basefill_019'], 'func': osc_base_universe_d3_025_osc_basefill_019}


def osc_base_universe_d3_026_osc_basefill_020(osc_base_universe_d2_026_osc_basefill_020):
    return _base_universe_d3(osc_base_universe_d2_026_osc_basefill_020, 26)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_026_osc_basefill_020'] = {'inputs': ['osc_base_universe_d2_026_osc_basefill_020'], 'func': osc_base_universe_d3_026_osc_basefill_020}


def osc_base_universe_d3_027_osc_basefill_024(osc_base_universe_d2_027_osc_basefill_024):
    return _base_universe_d3(osc_base_universe_d2_027_osc_basefill_024, 27)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_027_osc_basefill_024'] = {'inputs': ['osc_base_universe_d2_027_osc_basefill_024'], 'func': osc_base_universe_d3_027_osc_basefill_024}


def osc_base_universe_d3_028_osc_basefill_025(osc_base_universe_d2_028_osc_basefill_025):
    return _base_universe_d3(osc_base_universe_d2_028_osc_basefill_025, 28)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_028_osc_basefill_025'] = {'inputs': ['osc_base_universe_d2_028_osc_basefill_025'], 'func': osc_base_universe_d3_028_osc_basefill_025}


def osc_base_universe_d3_029_osc_basefill_026(osc_base_universe_d2_029_osc_basefill_026):
    return _base_universe_d3(osc_base_universe_d2_029_osc_basefill_026, 29)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_029_osc_basefill_026'] = {'inputs': ['osc_base_universe_d2_029_osc_basefill_026'], 'func': osc_base_universe_d3_029_osc_basefill_026}


def osc_base_universe_d3_030_osc_basefill_030(osc_base_universe_d2_030_osc_basefill_030):
    return _base_universe_d3(osc_base_universe_d2_030_osc_basefill_030, 30)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_030_osc_basefill_030'] = {'inputs': ['osc_base_universe_d2_030_osc_basefill_030'], 'func': osc_base_universe_d3_030_osc_basefill_030}


def osc_base_universe_d3_031_osc_basefill_031(osc_base_universe_d2_031_osc_basefill_031):
    return _base_universe_d3(osc_base_universe_d2_031_osc_basefill_031, 31)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_031_osc_basefill_031'] = {'inputs': ['osc_base_universe_d2_031_osc_basefill_031'], 'func': osc_base_universe_d3_031_osc_basefill_031}


def osc_base_universe_d3_032_osc_basefill_032(osc_base_universe_d2_032_osc_basefill_032):
    return _base_universe_d3(osc_base_universe_d2_032_osc_basefill_032, 32)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_032_osc_basefill_032'] = {'inputs': ['osc_base_universe_d2_032_osc_basefill_032'], 'func': osc_base_universe_d3_032_osc_basefill_032}


def osc_base_universe_d3_033_osc_basefill_033(osc_base_universe_d2_033_osc_basefill_033):
    return _base_universe_d3(osc_base_universe_d2_033_osc_basefill_033, 33)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_033_osc_basefill_033'] = {'inputs': ['osc_base_universe_d2_033_osc_basefill_033'], 'func': osc_base_universe_d3_033_osc_basefill_033}


def osc_base_universe_d3_034_osc_basefill_034(osc_base_universe_d2_034_osc_basefill_034):
    return _base_universe_d3(osc_base_universe_d2_034_osc_basefill_034, 34)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_034_osc_basefill_034'] = {'inputs': ['osc_base_universe_d2_034_osc_basefill_034'], 'func': osc_base_universe_d3_034_osc_basefill_034}


def osc_base_universe_d3_035_osc_basefill_035(osc_base_universe_d2_035_osc_basefill_035):
    return _base_universe_d3(osc_base_universe_d2_035_osc_basefill_035, 35)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_035_osc_basefill_035'] = {'inputs': ['osc_base_universe_d2_035_osc_basefill_035'], 'func': osc_base_universe_d3_035_osc_basefill_035}


def osc_base_universe_d3_036_osc_basefill_036(osc_base_universe_d2_036_osc_basefill_036):
    return _base_universe_d3(osc_base_universe_d2_036_osc_basefill_036, 36)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_036_osc_basefill_036'] = {'inputs': ['osc_base_universe_d2_036_osc_basefill_036'], 'func': osc_base_universe_d3_036_osc_basefill_036}


def osc_base_universe_d3_037_osc_basefill_037(osc_base_universe_d2_037_osc_basefill_037):
    return _base_universe_d3(osc_base_universe_d2_037_osc_basefill_037, 37)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_037_osc_basefill_037'] = {'inputs': ['osc_base_universe_d2_037_osc_basefill_037'], 'func': osc_base_universe_d3_037_osc_basefill_037}


def osc_base_universe_d3_038_osc_basefill_038(osc_base_universe_d2_038_osc_basefill_038):
    return _base_universe_d3(osc_base_universe_d2_038_osc_basefill_038, 38)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_038_osc_basefill_038'] = {'inputs': ['osc_base_universe_d2_038_osc_basefill_038'], 'func': osc_base_universe_d3_038_osc_basefill_038}


def osc_base_universe_d3_039_osc_basefill_039(osc_base_universe_d2_039_osc_basefill_039):
    return _base_universe_d3(osc_base_universe_d2_039_osc_basefill_039, 39)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_039_osc_basefill_039'] = {'inputs': ['osc_base_universe_d2_039_osc_basefill_039'], 'func': osc_base_universe_d3_039_osc_basefill_039}


def osc_base_universe_d3_040_osc_basefill_040(osc_base_universe_d2_040_osc_basefill_040):
    return _base_universe_d3(osc_base_universe_d2_040_osc_basefill_040, 40)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_040_osc_basefill_040'] = {'inputs': ['osc_base_universe_d2_040_osc_basefill_040'], 'func': osc_base_universe_d3_040_osc_basefill_040}


def osc_base_universe_d3_041_osc_basefill_041(osc_base_universe_d2_041_osc_basefill_041):
    return _base_universe_d3(osc_base_universe_d2_041_osc_basefill_041, 41)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_041_osc_basefill_041'] = {'inputs': ['osc_base_universe_d2_041_osc_basefill_041'], 'func': osc_base_universe_d3_041_osc_basefill_041}


def osc_base_universe_d3_042_osc_basefill_042(osc_base_universe_d2_042_osc_basefill_042):
    return _base_universe_d3(osc_base_universe_d2_042_osc_basefill_042, 42)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_042_osc_basefill_042'] = {'inputs': ['osc_base_universe_d2_042_osc_basefill_042'], 'func': osc_base_universe_d3_042_osc_basefill_042}


def osc_base_universe_d3_043_osc_basefill_043(osc_base_universe_d2_043_osc_basefill_043):
    return _base_universe_d3(osc_base_universe_d2_043_osc_basefill_043, 43)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_043_osc_basefill_043'] = {'inputs': ['osc_base_universe_d2_043_osc_basefill_043'], 'func': osc_base_universe_d3_043_osc_basefill_043}


def osc_base_universe_d3_044_osc_basefill_044(osc_base_universe_d2_044_osc_basefill_044):
    return _base_universe_d3(osc_base_universe_d2_044_osc_basefill_044, 44)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_044_osc_basefill_044'] = {'inputs': ['osc_base_universe_d2_044_osc_basefill_044'], 'func': osc_base_universe_d3_044_osc_basefill_044}


def osc_base_universe_d3_045_osc_basefill_045(osc_base_universe_d2_045_osc_basefill_045):
    return _base_universe_d3(osc_base_universe_d2_045_osc_basefill_045, 45)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_045_osc_basefill_045'] = {'inputs': ['osc_base_universe_d2_045_osc_basefill_045'], 'func': osc_base_universe_d3_045_osc_basefill_045}


def osc_base_universe_d3_046_osc_basefill_046(osc_base_universe_d2_046_osc_basefill_046):
    return _base_universe_d3(osc_base_universe_d2_046_osc_basefill_046, 46)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_046_osc_basefill_046'] = {'inputs': ['osc_base_universe_d2_046_osc_basefill_046'], 'func': osc_base_universe_d3_046_osc_basefill_046}


def osc_base_universe_d3_047_osc_basefill_047(osc_base_universe_d2_047_osc_basefill_047):
    return _base_universe_d3(osc_base_universe_d2_047_osc_basefill_047, 47)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_047_osc_basefill_047'] = {'inputs': ['osc_base_universe_d2_047_osc_basefill_047'], 'func': osc_base_universe_d3_047_osc_basefill_047}


def osc_base_universe_d3_048_osc_basefill_048(osc_base_universe_d2_048_osc_basefill_048):
    return _base_universe_d3(osc_base_universe_d2_048_osc_basefill_048, 48)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_048_osc_basefill_048'] = {'inputs': ['osc_base_universe_d2_048_osc_basefill_048'], 'func': osc_base_universe_d3_048_osc_basefill_048}


def osc_base_universe_d3_049_osc_basefill_049(osc_base_universe_d2_049_osc_basefill_049):
    return _base_universe_d3(osc_base_universe_d2_049_osc_basefill_049, 49)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_049_osc_basefill_049'] = {'inputs': ['osc_base_universe_d2_049_osc_basefill_049'], 'func': osc_base_universe_d3_049_osc_basefill_049}


def osc_base_universe_d3_050_osc_basefill_050(osc_base_universe_d2_050_osc_basefill_050):
    return _base_universe_d3(osc_base_universe_d2_050_osc_basefill_050, 50)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_050_osc_basefill_050'] = {'inputs': ['osc_base_universe_d2_050_osc_basefill_050'], 'func': osc_base_universe_d3_050_osc_basefill_050}


def osc_base_universe_d3_051_osc_basefill_051(osc_base_universe_d2_051_osc_basefill_051):
    return _base_universe_d3(osc_base_universe_d2_051_osc_basefill_051, 51)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_051_osc_basefill_051'] = {'inputs': ['osc_base_universe_d2_051_osc_basefill_051'], 'func': osc_base_universe_d3_051_osc_basefill_051}


def osc_base_universe_d3_052_osc_basefill_052(osc_base_universe_d2_052_osc_basefill_052):
    return _base_universe_d3(osc_base_universe_d2_052_osc_basefill_052, 52)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_052_osc_basefill_052'] = {'inputs': ['osc_base_universe_d2_052_osc_basefill_052'], 'func': osc_base_universe_d3_052_osc_basefill_052}


def osc_base_universe_d3_053_osc_basefill_053(osc_base_universe_d2_053_osc_basefill_053):
    return _base_universe_d3(osc_base_universe_d2_053_osc_basefill_053, 53)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_053_osc_basefill_053'] = {'inputs': ['osc_base_universe_d2_053_osc_basefill_053'], 'func': osc_base_universe_d3_053_osc_basefill_053}


def osc_base_universe_d3_054_osc_basefill_054(osc_base_universe_d2_054_osc_basefill_054):
    return _base_universe_d3(osc_base_universe_d2_054_osc_basefill_054, 54)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_054_osc_basefill_054'] = {'inputs': ['osc_base_universe_d2_054_osc_basefill_054'], 'func': osc_base_universe_d3_054_osc_basefill_054}


def osc_base_universe_d3_055_osc_basefill_055(osc_base_universe_d2_055_osc_basefill_055):
    return _base_universe_d3(osc_base_universe_d2_055_osc_basefill_055, 55)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_055_osc_basefill_055'] = {'inputs': ['osc_base_universe_d2_055_osc_basefill_055'], 'func': osc_base_universe_d3_055_osc_basefill_055}


def osc_base_universe_d3_056_osc_basefill_056(osc_base_universe_d2_056_osc_basefill_056):
    return _base_universe_d3(osc_base_universe_d2_056_osc_basefill_056, 56)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_056_osc_basefill_056'] = {'inputs': ['osc_base_universe_d2_056_osc_basefill_056'], 'func': osc_base_universe_d3_056_osc_basefill_056}


def osc_base_universe_d3_057_osc_basefill_057(osc_base_universe_d2_057_osc_basefill_057):
    return _base_universe_d3(osc_base_universe_d2_057_osc_basefill_057, 57)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_057_osc_basefill_057'] = {'inputs': ['osc_base_universe_d2_057_osc_basefill_057'], 'func': osc_base_universe_d3_057_osc_basefill_057}


def osc_base_universe_d3_058_osc_basefill_058(osc_base_universe_d2_058_osc_basefill_058):
    return _base_universe_d3(osc_base_universe_d2_058_osc_basefill_058, 58)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_058_osc_basefill_058'] = {'inputs': ['osc_base_universe_d2_058_osc_basefill_058'], 'func': osc_base_universe_d3_058_osc_basefill_058}


def osc_base_universe_d3_059_osc_basefill_059(osc_base_universe_d2_059_osc_basefill_059):
    return _base_universe_d3(osc_base_universe_d2_059_osc_basefill_059, 59)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_059_osc_basefill_059'] = {'inputs': ['osc_base_universe_d2_059_osc_basefill_059'], 'func': osc_base_universe_d3_059_osc_basefill_059}


def osc_base_universe_d3_060_osc_basefill_060(osc_base_universe_d2_060_osc_basefill_060):
    return _base_universe_d3(osc_base_universe_d2_060_osc_basefill_060, 60)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_060_osc_basefill_060'] = {'inputs': ['osc_base_universe_d2_060_osc_basefill_060'], 'func': osc_base_universe_d3_060_osc_basefill_060}


def osc_base_universe_d3_061_osc_basefill_061(osc_base_universe_d2_061_osc_basefill_061):
    return _base_universe_d3(osc_base_universe_d2_061_osc_basefill_061, 61)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_061_osc_basefill_061'] = {'inputs': ['osc_base_universe_d2_061_osc_basefill_061'], 'func': osc_base_universe_d3_061_osc_basefill_061}


def osc_base_universe_d3_062_osc_basefill_062(osc_base_universe_d2_062_osc_basefill_062):
    return _base_universe_d3(osc_base_universe_d2_062_osc_basefill_062, 62)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_062_osc_basefill_062'] = {'inputs': ['osc_base_universe_d2_062_osc_basefill_062'], 'func': osc_base_universe_d3_062_osc_basefill_062}


def osc_base_universe_d3_063_osc_basefill_063(osc_base_universe_d2_063_osc_basefill_063):
    return _base_universe_d3(osc_base_universe_d2_063_osc_basefill_063, 63)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_063_osc_basefill_063'] = {'inputs': ['osc_base_universe_d2_063_osc_basefill_063'], 'func': osc_base_universe_d3_063_osc_basefill_063}


def osc_base_universe_d3_064_osc_basefill_064(osc_base_universe_d2_064_osc_basefill_064):
    return _base_universe_d3(osc_base_universe_d2_064_osc_basefill_064, 64)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_064_osc_basefill_064'] = {'inputs': ['osc_base_universe_d2_064_osc_basefill_064'], 'func': osc_base_universe_d3_064_osc_basefill_064}


def osc_base_universe_d3_065_osc_basefill_065(osc_base_universe_d2_065_osc_basefill_065):
    return _base_universe_d3(osc_base_universe_d2_065_osc_basefill_065, 65)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_065_osc_basefill_065'] = {'inputs': ['osc_base_universe_d2_065_osc_basefill_065'], 'func': osc_base_universe_d3_065_osc_basefill_065}


def osc_base_universe_d3_066_osc_basefill_066(osc_base_universe_d2_066_osc_basefill_066):
    return _base_universe_d3(osc_base_universe_d2_066_osc_basefill_066, 66)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_066_osc_basefill_066'] = {'inputs': ['osc_base_universe_d2_066_osc_basefill_066'], 'func': osc_base_universe_d3_066_osc_basefill_066}


def osc_base_universe_d3_067_osc_basefill_067(osc_base_universe_d2_067_osc_basefill_067):
    return _base_universe_d3(osc_base_universe_d2_067_osc_basefill_067, 67)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_067_osc_basefill_067'] = {'inputs': ['osc_base_universe_d2_067_osc_basefill_067'], 'func': osc_base_universe_d3_067_osc_basefill_067}


def osc_base_universe_d3_068_osc_basefill_068(osc_base_universe_d2_068_osc_basefill_068):
    return _base_universe_d3(osc_base_universe_d2_068_osc_basefill_068, 68)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_068_osc_basefill_068'] = {'inputs': ['osc_base_universe_d2_068_osc_basefill_068'], 'func': osc_base_universe_d3_068_osc_basefill_068}


def osc_base_universe_d3_069_osc_basefill_069(osc_base_universe_d2_069_osc_basefill_069):
    return _base_universe_d3(osc_base_universe_d2_069_osc_basefill_069, 69)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_069_osc_basefill_069'] = {'inputs': ['osc_base_universe_d2_069_osc_basefill_069'], 'func': osc_base_universe_d3_069_osc_basefill_069}


def osc_base_universe_d3_070_osc_basefill_070(osc_base_universe_d2_070_osc_basefill_070):
    return _base_universe_d3(osc_base_universe_d2_070_osc_basefill_070, 70)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_070_osc_basefill_070'] = {'inputs': ['osc_base_universe_d2_070_osc_basefill_070'], 'func': osc_base_universe_d3_070_osc_basefill_070}


def osc_base_universe_d3_071_osc_basefill_071(osc_base_universe_d2_071_osc_basefill_071):
    return _base_universe_d3(osc_base_universe_d2_071_osc_basefill_071, 71)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_071_osc_basefill_071'] = {'inputs': ['osc_base_universe_d2_071_osc_basefill_071'], 'func': osc_base_universe_d3_071_osc_basefill_071}


def osc_base_universe_d3_072_osc_basefill_072(osc_base_universe_d2_072_osc_basefill_072):
    return _base_universe_d3(osc_base_universe_d2_072_osc_basefill_072, 72)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_072_osc_basefill_072'] = {'inputs': ['osc_base_universe_d2_072_osc_basefill_072'], 'func': osc_base_universe_d3_072_osc_basefill_072}


def osc_base_universe_d3_073_osc_basefill_073(osc_base_universe_d2_073_osc_basefill_073):
    return _base_universe_d3(osc_base_universe_d2_073_osc_basefill_073, 73)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_073_osc_basefill_073'] = {'inputs': ['osc_base_universe_d2_073_osc_basefill_073'], 'func': osc_base_universe_d3_073_osc_basefill_073}


def osc_base_universe_d3_074_osc_basefill_074(osc_base_universe_d2_074_osc_basefill_074):
    return _base_universe_d3(osc_base_universe_d2_074_osc_basefill_074, 74)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_074_osc_basefill_074'] = {'inputs': ['osc_base_universe_d2_074_osc_basefill_074'], 'func': osc_base_universe_d3_074_osc_basefill_074}


def osc_base_universe_d3_075_osc_basefill_075(osc_base_universe_d2_075_osc_basefill_075):
    return _base_universe_d3(osc_base_universe_d2_075_osc_basefill_075, 75)
OSC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['osc_base_universe_d3_075_osc_basefill_075'] = {'inputs': ['osc_base_universe_d2_075_osc_basefill_075'], 'func': osc_base_universe_d3_075_osc_basefill_075}
