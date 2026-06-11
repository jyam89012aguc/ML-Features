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



def dd_176_dd_001_drawdown_from_high_5_001_accel_1(dd_151_dd_001_drawdown_from_high_5_001_roc_1):
    feature = _s(dd_151_dd_001_drawdown_from_high_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def dd_177_dd_007_drawdown_from_high_126_007_accel_5(dd_152_dd_007_drawdown_from_high_126_007_roc_5):
    feature = _s(dd_152_dd_007_drawdown_from_high_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def dd_178_dd_013_drawdown_from_high_1008_013_accel_42(dd_153_dd_013_drawdown_from_high_1008_013_roc_42):
    feature = _s(dd_153_dd_013_drawdown_from_high_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def dd_179_dd_019_drawdown_from_high_42_019_accel_126(dd_154_dd_019_drawdown_from_high_42_019_roc_126):
    feature = _s(dd_154_dd_019_drawdown_from_high_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def dd_180_dd_025_drawdown_from_high_378_025_accel_378(dd_155_dd_025_drawdown_from_high_378_025_roc_378):
    feature = _s(dd_155_dd_025_drawdown_from_high_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















DRAWDOWN_DEPTH_REGISTRY_3RD_DERIVATIVES = {
    'dd_176_dd_001_drawdown_from_high_5_001_accel_1': {'inputs': ['dd_151_dd_001_drawdown_from_high_5_001_roc_1'], 'func': dd_176_dd_001_drawdown_from_high_5_001_accel_1},
    'dd_177_dd_007_drawdown_from_high_126_007_accel_5': {'inputs': ['dd_152_dd_007_drawdown_from_high_126_007_roc_5'], 'func': dd_177_dd_007_drawdown_from_high_126_007_accel_5},
    'dd_178_dd_013_drawdown_from_high_1008_013_accel_42': {'inputs': ['dd_153_dd_013_drawdown_from_high_1008_013_roc_42'], 'func': dd_178_dd_013_drawdown_from_high_1008_013_accel_42},
    'dd_179_dd_019_drawdown_from_high_42_019_accel_126': {'inputs': ['dd_154_dd_019_drawdown_from_high_42_019_roc_126'], 'func': dd_179_dd_019_drawdown_from_high_42_019_accel_126},
    'dd_180_dd_025_drawdown_from_high_378_025_accel_378': {'inputs': ['dd_155_dd_025_drawdown_from_high_378_025_roc_378'], 'func': dd_180_dd_025_drawdown_from_high_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def dd_replacement_d3_001(dd_replacement_d2_001):
    feature = _clean(dd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_001'] = {'inputs': ['dd_replacement_d2_001'], 'func': dd_replacement_d3_001}


def dd_replacement_d3_002(dd_replacement_d2_002):
    feature = _clean(dd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_002'] = {'inputs': ['dd_replacement_d2_002'], 'func': dd_replacement_d3_002}


def dd_replacement_d3_003(dd_replacement_d2_003):
    feature = _clean(dd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_003'] = {'inputs': ['dd_replacement_d2_003'], 'func': dd_replacement_d3_003}


def dd_replacement_d3_004(dd_replacement_d2_004):
    feature = _clean(dd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_004'] = {'inputs': ['dd_replacement_d2_004'], 'func': dd_replacement_d3_004}


def dd_replacement_d3_005(dd_replacement_d2_005):
    feature = _clean(dd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_005'] = {'inputs': ['dd_replacement_d2_005'], 'func': dd_replacement_d3_005}


def dd_replacement_d3_006(dd_replacement_d2_006):
    feature = _clean(dd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_006'] = {'inputs': ['dd_replacement_d2_006'], 'func': dd_replacement_d3_006}


def dd_replacement_d3_007(dd_replacement_d2_007):
    feature = _clean(dd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_007'] = {'inputs': ['dd_replacement_d2_007'], 'func': dd_replacement_d3_007}


def dd_replacement_d3_008(dd_replacement_d2_008):
    feature = _clean(dd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_008'] = {'inputs': ['dd_replacement_d2_008'], 'func': dd_replacement_d3_008}


def dd_replacement_d3_009(dd_replacement_d2_009):
    feature = _clean(dd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_009'] = {'inputs': ['dd_replacement_d2_009'], 'func': dd_replacement_d3_009}


def dd_replacement_d3_010(dd_replacement_d2_010):
    feature = _clean(dd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_010'] = {'inputs': ['dd_replacement_d2_010'], 'func': dd_replacement_d3_010}


def dd_replacement_d3_011(dd_replacement_d2_011):
    feature = _clean(dd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_011'] = {'inputs': ['dd_replacement_d2_011'], 'func': dd_replacement_d3_011}


def dd_replacement_d3_012(dd_replacement_d2_012):
    feature = _clean(dd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_012'] = {'inputs': ['dd_replacement_d2_012'], 'func': dd_replacement_d3_012}


def dd_replacement_d3_013(dd_replacement_d2_013):
    feature = _clean(dd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_013'] = {'inputs': ['dd_replacement_d2_013'], 'func': dd_replacement_d3_013}


def dd_replacement_d3_014(dd_replacement_d2_014):
    feature = _clean(dd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_014'] = {'inputs': ['dd_replacement_d2_014'], 'func': dd_replacement_d3_014}


def dd_replacement_d3_015(dd_replacement_d2_015):
    feature = _clean(dd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_015'] = {'inputs': ['dd_replacement_d2_015'], 'func': dd_replacement_d3_015}


def dd_replacement_d3_016(dd_replacement_d2_016):
    feature = _clean(dd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_016'] = {'inputs': ['dd_replacement_d2_016'], 'func': dd_replacement_d3_016}


def dd_replacement_d3_017(dd_replacement_d2_017):
    feature = _clean(dd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_017'] = {'inputs': ['dd_replacement_d2_017'], 'func': dd_replacement_d3_017}


def dd_replacement_d3_018(dd_replacement_d2_018):
    feature = _clean(dd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_018'] = {'inputs': ['dd_replacement_d2_018'], 'func': dd_replacement_d3_018}


def dd_replacement_d3_019(dd_replacement_d2_019):
    feature = _clean(dd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_019'] = {'inputs': ['dd_replacement_d2_019'], 'func': dd_replacement_d3_019}


def dd_replacement_d3_020(dd_replacement_d2_020):
    feature = _clean(dd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_020'] = {'inputs': ['dd_replacement_d2_020'], 'func': dd_replacement_d3_020}


def dd_replacement_d3_021(dd_replacement_d2_021):
    feature = _clean(dd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_021'] = {'inputs': ['dd_replacement_d2_021'], 'func': dd_replacement_d3_021}


def dd_replacement_d3_022(dd_replacement_d2_022):
    feature = _clean(dd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_022'] = {'inputs': ['dd_replacement_d2_022'], 'func': dd_replacement_d3_022}


def dd_replacement_d3_023(dd_replacement_d2_023):
    feature = _clean(dd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_023'] = {'inputs': ['dd_replacement_d2_023'], 'func': dd_replacement_d3_023}


def dd_replacement_d3_024(dd_replacement_d2_024):
    feature = _clean(dd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_024'] = {'inputs': ['dd_replacement_d2_024'], 'func': dd_replacement_d3_024}


def dd_replacement_d3_025(dd_replacement_d2_025):
    feature = _clean(dd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_025'] = {'inputs': ['dd_replacement_d2_025'], 'func': dd_replacement_d3_025}


def dd_replacement_d3_026(dd_replacement_d2_026):
    feature = _clean(dd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_026'] = {'inputs': ['dd_replacement_d2_026'], 'func': dd_replacement_d3_026}


def dd_replacement_d3_027(dd_replacement_d2_027):
    feature = _clean(dd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_027'] = {'inputs': ['dd_replacement_d2_027'], 'func': dd_replacement_d3_027}


def dd_replacement_d3_028(dd_replacement_d2_028):
    feature = _clean(dd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_028'] = {'inputs': ['dd_replacement_d2_028'], 'func': dd_replacement_d3_028}


def dd_replacement_d3_029(dd_replacement_d2_029):
    feature = _clean(dd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_029'] = {'inputs': ['dd_replacement_d2_029'], 'func': dd_replacement_d3_029}


def dd_replacement_d3_030(dd_replacement_d2_030):
    feature = _clean(dd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_030'] = {'inputs': ['dd_replacement_d2_030'], 'func': dd_replacement_d3_030}


def dd_replacement_d3_031(dd_replacement_d2_031):
    feature = _clean(dd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_031'] = {'inputs': ['dd_replacement_d2_031'], 'func': dd_replacement_d3_031}


def dd_replacement_d3_032(dd_replacement_d2_032):
    feature = _clean(dd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_032'] = {'inputs': ['dd_replacement_d2_032'], 'func': dd_replacement_d3_032}


def dd_replacement_d3_033(dd_replacement_d2_033):
    feature = _clean(dd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_033'] = {'inputs': ['dd_replacement_d2_033'], 'func': dd_replacement_d3_033}


def dd_replacement_d3_034(dd_replacement_d2_034):
    feature = _clean(dd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_034'] = {'inputs': ['dd_replacement_d2_034'], 'func': dd_replacement_d3_034}


def dd_replacement_d3_035(dd_replacement_d2_035):
    feature = _clean(dd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_035'] = {'inputs': ['dd_replacement_d2_035'], 'func': dd_replacement_d3_035}


def dd_replacement_d3_036(dd_replacement_d2_036):
    feature = _clean(dd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_036'] = {'inputs': ['dd_replacement_d2_036'], 'func': dd_replacement_d3_036}


def dd_replacement_d3_037(dd_replacement_d2_037):
    feature = _clean(dd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_037'] = {'inputs': ['dd_replacement_d2_037'], 'func': dd_replacement_d3_037}


def dd_replacement_d3_038(dd_replacement_d2_038):
    feature = _clean(dd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_038'] = {'inputs': ['dd_replacement_d2_038'], 'func': dd_replacement_d3_038}


def dd_replacement_d3_039(dd_replacement_d2_039):
    feature = _clean(dd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_039'] = {'inputs': ['dd_replacement_d2_039'], 'func': dd_replacement_d3_039}


def dd_replacement_d3_040(dd_replacement_d2_040):
    feature = _clean(dd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_040'] = {'inputs': ['dd_replacement_d2_040'], 'func': dd_replacement_d3_040}


def dd_replacement_d3_041(dd_replacement_d2_041):
    feature = _clean(dd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_041'] = {'inputs': ['dd_replacement_d2_041'], 'func': dd_replacement_d3_041}


def dd_replacement_d3_042(dd_replacement_d2_042):
    feature = _clean(dd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_042'] = {'inputs': ['dd_replacement_d2_042'], 'func': dd_replacement_d3_042}


def dd_replacement_d3_043(dd_replacement_d2_043):
    feature = _clean(dd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_043'] = {'inputs': ['dd_replacement_d2_043'], 'func': dd_replacement_d3_043}


def dd_replacement_d3_044(dd_replacement_d2_044):
    feature = _clean(dd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_044'] = {'inputs': ['dd_replacement_d2_044'], 'func': dd_replacement_d3_044}


def dd_replacement_d3_045(dd_replacement_d2_045):
    feature = _clean(dd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_045'] = {'inputs': ['dd_replacement_d2_045'], 'func': dd_replacement_d3_045}


def dd_replacement_d3_046(dd_replacement_d2_046):
    feature = _clean(dd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_046'] = {'inputs': ['dd_replacement_d2_046'], 'func': dd_replacement_d3_046}


def dd_replacement_d3_047(dd_replacement_d2_047):
    feature = _clean(dd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_047'] = {'inputs': ['dd_replacement_d2_047'], 'func': dd_replacement_d3_047}


def dd_replacement_d3_048(dd_replacement_d2_048):
    feature = _clean(dd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_048'] = {'inputs': ['dd_replacement_d2_048'], 'func': dd_replacement_d3_048}


def dd_replacement_d3_049(dd_replacement_d2_049):
    feature = _clean(dd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_049'] = {'inputs': ['dd_replacement_d2_049'], 'func': dd_replacement_d3_049}


def dd_replacement_d3_050(dd_replacement_d2_050):
    feature = _clean(dd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_050'] = {'inputs': ['dd_replacement_d2_050'], 'func': dd_replacement_d3_050}


def dd_replacement_d3_051(dd_replacement_d2_051):
    feature = _clean(dd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_051'] = {'inputs': ['dd_replacement_d2_051'], 'func': dd_replacement_d3_051}


def dd_replacement_d3_052(dd_replacement_d2_052):
    feature = _clean(dd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_052'] = {'inputs': ['dd_replacement_d2_052'], 'func': dd_replacement_d3_052}


def dd_replacement_d3_053(dd_replacement_d2_053):
    feature = _clean(dd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_053'] = {'inputs': ['dd_replacement_d2_053'], 'func': dd_replacement_d3_053}


def dd_replacement_d3_054(dd_replacement_d2_054):
    feature = _clean(dd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_054'] = {'inputs': ['dd_replacement_d2_054'], 'func': dd_replacement_d3_054}


def dd_replacement_d3_055(dd_replacement_d2_055):
    feature = _clean(dd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_055'] = {'inputs': ['dd_replacement_d2_055'], 'func': dd_replacement_d3_055}


def dd_replacement_d3_056(dd_replacement_d2_056):
    feature = _clean(dd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_056'] = {'inputs': ['dd_replacement_d2_056'], 'func': dd_replacement_d3_056}


def dd_replacement_d3_057(dd_replacement_d2_057):
    feature = _clean(dd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_057'] = {'inputs': ['dd_replacement_d2_057'], 'func': dd_replacement_d3_057}


def dd_replacement_d3_058(dd_replacement_d2_058):
    feature = _clean(dd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_058'] = {'inputs': ['dd_replacement_d2_058'], 'func': dd_replacement_d3_058}


def dd_replacement_d3_059(dd_replacement_d2_059):
    feature = _clean(dd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_059'] = {'inputs': ['dd_replacement_d2_059'], 'func': dd_replacement_d3_059}


def dd_replacement_d3_060(dd_replacement_d2_060):
    feature = _clean(dd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_060'] = {'inputs': ['dd_replacement_d2_060'], 'func': dd_replacement_d3_060}


def dd_replacement_d3_061(dd_replacement_d2_061):
    feature = _clean(dd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_061'] = {'inputs': ['dd_replacement_d2_061'], 'func': dd_replacement_d3_061}


def dd_replacement_d3_062(dd_replacement_d2_062):
    feature = _clean(dd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_062'] = {'inputs': ['dd_replacement_d2_062'], 'func': dd_replacement_d3_062}


def dd_replacement_d3_063(dd_replacement_d2_063):
    feature = _clean(dd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_063'] = {'inputs': ['dd_replacement_d2_063'], 'func': dd_replacement_d3_063}


def dd_replacement_d3_064(dd_replacement_d2_064):
    feature = _clean(dd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_064'] = {'inputs': ['dd_replacement_d2_064'], 'func': dd_replacement_d3_064}


def dd_replacement_d3_065(dd_replacement_d2_065):
    feature = _clean(dd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_065'] = {'inputs': ['dd_replacement_d2_065'], 'func': dd_replacement_d3_065}


def dd_replacement_d3_066(dd_replacement_d2_066):
    feature = _clean(dd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_066'] = {'inputs': ['dd_replacement_d2_066'], 'func': dd_replacement_d3_066}


def dd_replacement_d3_067(dd_replacement_d2_067):
    feature = _clean(dd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_067'] = {'inputs': ['dd_replacement_d2_067'], 'func': dd_replacement_d3_067}


def dd_replacement_d3_068(dd_replacement_d2_068):
    feature = _clean(dd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_068'] = {'inputs': ['dd_replacement_d2_068'], 'func': dd_replacement_d3_068}


def dd_replacement_d3_069(dd_replacement_d2_069):
    feature = _clean(dd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_069'] = {'inputs': ['dd_replacement_d2_069'], 'func': dd_replacement_d3_069}


def dd_replacement_d3_070(dd_replacement_d2_070):
    feature = _clean(dd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_070'] = {'inputs': ['dd_replacement_d2_070'], 'func': dd_replacement_d3_070}


def dd_replacement_d3_071(dd_replacement_d2_071):
    feature = _clean(dd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_071'] = {'inputs': ['dd_replacement_d2_071'], 'func': dd_replacement_d3_071}


def dd_replacement_d3_072(dd_replacement_d2_072):
    feature = _clean(dd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_072'] = {'inputs': ['dd_replacement_d2_072'], 'func': dd_replacement_d3_072}


def dd_replacement_d3_073(dd_replacement_d2_073):
    feature = _clean(dd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_073'] = {'inputs': ['dd_replacement_d2_073'], 'func': dd_replacement_d3_073}


def dd_replacement_d3_074(dd_replacement_d2_074):
    feature = _clean(dd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_074'] = {'inputs': ['dd_replacement_d2_074'], 'func': dd_replacement_d3_074}


def dd_replacement_d3_075(dd_replacement_d2_075):
    feature = _clean(dd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_075'] = {'inputs': ['dd_replacement_d2_075'], 'func': dd_replacement_d3_075}


def dd_replacement_d3_076(dd_replacement_d2_076):
    feature = _clean(dd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_076'] = {'inputs': ['dd_replacement_d2_076'], 'func': dd_replacement_d3_076}


def dd_replacement_d3_077(dd_replacement_d2_077):
    feature = _clean(dd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_077'] = {'inputs': ['dd_replacement_d2_077'], 'func': dd_replacement_d3_077}


def dd_replacement_d3_078(dd_replacement_d2_078):
    feature = _clean(dd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_078'] = {'inputs': ['dd_replacement_d2_078'], 'func': dd_replacement_d3_078}


def dd_replacement_d3_079(dd_replacement_d2_079):
    feature = _clean(dd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_079'] = {'inputs': ['dd_replacement_d2_079'], 'func': dd_replacement_d3_079}


def dd_replacement_d3_080(dd_replacement_d2_080):
    feature = _clean(dd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_080'] = {'inputs': ['dd_replacement_d2_080'], 'func': dd_replacement_d3_080}


def dd_replacement_d3_081(dd_replacement_d2_081):
    feature = _clean(dd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_081'] = {'inputs': ['dd_replacement_d2_081'], 'func': dd_replacement_d3_081}


def dd_replacement_d3_082(dd_replacement_d2_082):
    feature = _clean(dd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_082'] = {'inputs': ['dd_replacement_d2_082'], 'func': dd_replacement_d3_082}


def dd_replacement_d3_083(dd_replacement_d2_083):
    feature = _clean(dd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_083'] = {'inputs': ['dd_replacement_d2_083'], 'func': dd_replacement_d3_083}


def dd_replacement_d3_084(dd_replacement_d2_084):
    feature = _clean(dd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_084'] = {'inputs': ['dd_replacement_d2_084'], 'func': dd_replacement_d3_084}


def dd_replacement_d3_085(dd_replacement_d2_085):
    feature = _clean(dd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_085'] = {'inputs': ['dd_replacement_d2_085'], 'func': dd_replacement_d3_085}


def dd_replacement_d3_086(dd_replacement_d2_086):
    feature = _clean(dd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_086'] = {'inputs': ['dd_replacement_d2_086'], 'func': dd_replacement_d3_086}


def dd_replacement_d3_087(dd_replacement_d2_087):
    feature = _clean(dd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_087'] = {'inputs': ['dd_replacement_d2_087'], 'func': dd_replacement_d3_087}


def dd_replacement_d3_088(dd_replacement_d2_088):
    feature = _clean(dd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_088'] = {'inputs': ['dd_replacement_d2_088'], 'func': dd_replacement_d3_088}


def dd_replacement_d3_089(dd_replacement_d2_089):
    feature = _clean(dd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_089'] = {'inputs': ['dd_replacement_d2_089'], 'func': dd_replacement_d3_089}


def dd_replacement_d3_090(dd_replacement_d2_090):
    feature = _clean(dd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_090'] = {'inputs': ['dd_replacement_d2_090'], 'func': dd_replacement_d3_090}


def dd_replacement_d3_091(dd_replacement_d2_091):
    feature = _clean(dd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_091'] = {'inputs': ['dd_replacement_d2_091'], 'func': dd_replacement_d3_091}


def dd_replacement_d3_092(dd_replacement_d2_092):
    feature = _clean(dd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_092'] = {'inputs': ['dd_replacement_d2_092'], 'func': dd_replacement_d3_092}


def dd_replacement_d3_093(dd_replacement_d2_093):
    feature = _clean(dd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_093'] = {'inputs': ['dd_replacement_d2_093'], 'func': dd_replacement_d3_093}


def dd_replacement_d3_094(dd_replacement_d2_094):
    feature = _clean(dd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_094'] = {'inputs': ['dd_replacement_d2_094'], 'func': dd_replacement_d3_094}


def dd_replacement_d3_095(dd_replacement_d2_095):
    feature = _clean(dd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_095'] = {'inputs': ['dd_replacement_d2_095'], 'func': dd_replacement_d3_095}


def dd_replacement_d3_096(dd_replacement_d2_096):
    feature = _clean(dd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_096'] = {'inputs': ['dd_replacement_d2_096'], 'func': dd_replacement_d3_096}


def dd_replacement_d3_097(dd_replacement_d2_097):
    feature = _clean(dd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_097'] = {'inputs': ['dd_replacement_d2_097'], 'func': dd_replacement_d3_097}


def dd_replacement_d3_098(dd_replacement_d2_098):
    feature = _clean(dd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_098'] = {'inputs': ['dd_replacement_d2_098'], 'func': dd_replacement_d3_098}


def dd_replacement_d3_099(dd_replacement_d2_099):
    feature = _clean(dd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_099'] = {'inputs': ['dd_replacement_d2_099'], 'func': dd_replacement_d3_099}


def dd_replacement_d3_100(dd_replacement_d2_100):
    feature = _clean(dd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_100'] = {'inputs': ['dd_replacement_d2_100'], 'func': dd_replacement_d3_100}


def dd_replacement_d3_101(dd_replacement_d2_101):
    feature = _clean(dd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_101'] = {'inputs': ['dd_replacement_d2_101'], 'func': dd_replacement_d3_101}


def dd_replacement_d3_102(dd_replacement_d2_102):
    feature = _clean(dd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_102'] = {'inputs': ['dd_replacement_d2_102'], 'func': dd_replacement_d3_102}


def dd_replacement_d3_103(dd_replacement_d2_103):
    feature = _clean(dd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_103'] = {'inputs': ['dd_replacement_d2_103'], 'func': dd_replacement_d3_103}


def dd_replacement_d3_104(dd_replacement_d2_104):
    feature = _clean(dd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_104'] = {'inputs': ['dd_replacement_d2_104'], 'func': dd_replacement_d3_104}


def dd_replacement_d3_105(dd_replacement_d2_105):
    feature = _clean(dd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_105'] = {'inputs': ['dd_replacement_d2_105'], 'func': dd_replacement_d3_105}


def dd_replacement_d3_106(dd_replacement_d2_106):
    feature = _clean(dd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_106'] = {'inputs': ['dd_replacement_d2_106'], 'func': dd_replacement_d3_106}


def dd_replacement_d3_107(dd_replacement_d2_107):
    feature = _clean(dd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_107'] = {'inputs': ['dd_replacement_d2_107'], 'func': dd_replacement_d3_107}


def dd_replacement_d3_108(dd_replacement_d2_108):
    feature = _clean(dd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_108'] = {'inputs': ['dd_replacement_d2_108'], 'func': dd_replacement_d3_108}


def dd_replacement_d3_109(dd_replacement_d2_109):
    feature = _clean(dd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_109'] = {'inputs': ['dd_replacement_d2_109'], 'func': dd_replacement_d3_109}


def dd_replacement_d3_110(dd_replacement_d2_110):
    feature = _clean(dd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_110'] = {'inputs': ['dd_replacement_d2_110'], 'func': dd_replacement_d3_110}


def dd_replacement_d3_111(dd_replacement_d2_111):
    feature = _clean(dd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_111'] = {'inputs': ['dd_replacement_d2_111'], 'func': dd_replacement_d3_111}


def dd_replacement_d3_112(dd_replacement_d2_112):
    feature = _clean(dd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_112'] = {'inputs': ['dd_replacement_d2_112'], 'func': dd_replacement_d3_112}


def dd_replacement_d3_113(dd_replacement_d2_113):
    feature = _clean(dd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_113'] = {'inputs': ['dd_replacement_d2_113'], 'func': dd_replacement_d3_113}


def dd_replacement_d3_114(dd_replacement_d2_114):
    feature = _clean(dd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_114'] = {'inputs': ['dd_replacement_d2_114'], 'func': dd_replacement_d3_114}


def dd_replacement_d3_115(dd_replacement_d2_115):
    feature = _clean(dd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_115'] = {'inputs': ['dd_replacement_d2_115'], 'func': dd_replacement_d3_115}


def dd_replacement_d3_116(dd_replacement_d2_116):
    feature = _clean(dd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_116'] = {'inputs': ['dd_replacement_d2_116'], 'func': dd_replacement_d3_116}


def dd_replacement_d3_117(dd_replacement_d2_117):
    feature = _clean(dd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_117'] = {'inputs': ['dd_replacement_d2_117'], 'func': dd_replacement_d3_117}


def dd_replacement_d3_118(dd_replacement_d2_118):
    feature = _clean(dd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_118'] = {'inputs': ['dd_replacement_d2_118'], 'func': dd_replacement_d3_118}


def dd_replacement_d3_119(dd_replacement_d2_119):
    feature = _clean(dd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_119'] = {'inputs': ['dd_replacement_d2_119'], 'func': dd_replacement_d3_119}


def dd_replacement_d3_120(dd_replacement_d2_120):
    feature = _clean(dd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_120'] = {'inputs': ['dd_replacement_d2_120'], 'func': dd_replacement_d3_120}


def dd_replacement_d3_121(dd_replacement_d2_121):
    feature = _clean(dd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_121'] = {'inputs': ['dd_replacement_d2_121'], 'func': dd_replacement_d3_121}


def dd_replacement_d3_122(dd_replacement_d2_122):
    feature = _clean(dd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_122'] = {'inputs': ['dd_replacement_d2_122'], 'func': dd_replacement_d3_122}


def dd_replacement_d3_123(dd_replacement_d2_123):
    feature = _clean(dd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_123'] = {'inputs': ['dd_replacement_d2_123'], 'func': dd_replacement_d3_123}


def dd_replacement_d3_124(dd_replacement_d2_124):
    feature = _clean(dd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_124'] = {'inputs': ['dd_replacement_d2_124'], 'func': dd_replacement_d3_124}


def dd_replacement_d3_125(dd_replacement_d2_125):
    feature = _clean(dd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_125'] = {'inputs': ['dd_replacement_d2_125'], 'func': dd_replacement_d3_125}


def dd_replacement_d3_126(dd_replacement_d2_126):
    feature = _clean(dd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_126'] = {'inputs': ['dd_replacement_d2_126'], 'func': dd_replacement_d3_126}


def dd_replacement_d3_127(dd_replacement_d2_127):
    feature = _clean(dd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_127'] = {'inputs': ['dd_replacement_d2_127'], 'func': dd_replacement_d3_127}


def dd_replacement_d3_128(dd_replacement_d2_128):
    feature = _clean(dd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_128'] = {'inputs': ['dd_replacement_d2_128'], 'func': dd_replacement_d3_128}


def dd_replacement_d3_129(dd_replacement_d2_129):
    feature = _clean(dd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_129'] = {'inputs': ['dd_replacement_d2_129'], 'func': dd_replacement_d3_129}


def dd_replacement_d3_130(dd_replacement_d2_130):
    feature = _clean(dd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_130'] = {'inputs': ['dd_replacement_d2_130'], 'func': dd_replacement_d3_130}


def dd_replacement_d3_131(dd_replacement_d2_131):
    feature = _clean(dd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_131'] = {'inputs': ['dd_replacement_d2_131'], 'func': dd_replacement_d3_131}


def dd_replacement_d3_132(dd_replacement_d2_132):
    feature = _clean(dd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_132'] = {'inputs': ['dd_replacement_d2_132'], 'func': dd_replacement_d3_132}


def dd_replacement_d3_133(dd_replacement_d2_133):
    feature = _clean(dd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_133'] = {'inputs': ['dd_replacement_d2_133'], 'func': dd_replacement_d3_133}


def dd_replacement_d3_134(dd_replacement_d2_134):
    feature = _clean(dd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_134'] = {'inputs': ['dd_replacement_d2_134'], 'func': dd_replacement_d3_134}


def dd_replacement_d3_135(dd_replacement_d2_135):
    feature = _clean(dd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_135'] = {'inputs': ['dd_replacement_d2_135'], 'func': dd_replacement_d3_135}


def dd_replacement_d3_136(dd_replacement_d2_136):
    feature = _clean(dd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_136'] = {'inputs': ['dd_replacement_d2_136'], 'func': dd_replacement_d3_136}


def dd_replacement_d3_137(dd_replacement_d2_137):
    feature = _clean(dd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_137'] = {'inputs': ['dd_replacement_d2_137'], 'func': dd_replacement_d3_137}


def dd_replacement_d3_138(dd_replacement_d2_138):
    feature = _clean(dd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_138'] = {'inputs': ['dd_replacement_d2_138'], 'func': dd_replacement_d3_138}


def dd_replacement_d3_139(dd_replacement_d2_139):
    feature = _clean(dd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_139'] = {'inputs': ['dd_replacement_d2_139'], 'func': dd_replacement_d3_139}


def dd_replacement_d3_140(dd_replacement_d2_140):
    feature = _clean(dd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_140'] = {'inputs': ['dd_replacement_d2_140'], 'func': dd_replacement_d3_140}


def dd_replacement_d3_141(dd_replacement_d2_141):
    feature = _clean(dd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_141'] = {'inputs': ['dd_replacement_d2_141'], 'func': dd_replacement_d3_141}


def dd_replacement_d3_142(dd_replacement_d2_142):
    feature = _clean(dd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_142'] = {'inputs': ['dd_replacement_d2_142'], 'func': dd_replacement_d3_142}


def dd_replacement_d3_143(dd_replacement_d2_143):
    feature = _clean(dd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_143'] = {'inputs': ['dd_replacement_d2_143'], 'func': dd_replacement_d3_143}


def dd_replacement_d3_144(dd_replacement_d2_144):
    feature = _clean(dd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_144'] = {'inputs': ['dd_replacement_d2_144'], 'func': dd_replacement_d3_144}


def dd_replacement_d3_145(dd_replacement_d2_145):
    feature = _clean(dd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_145'] = {'inputs': ['dd_replacement_d2_145'], 'func': dd_replacement_d3_145}


def dd_replacement_d3_146(dd_replacement_d2_146):
    feature = _clean(dd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_146'] = {'inputs': ['dd_replacement_d2_146'], 'func': dd_replacement_d3_146}


def dd_replacement_d3_147(dd_replacement_d2_147):
    feature = _clean(dd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_147'] = {'inputs': ['dd_replacement_d2_147'], 'func': dd_replacement_d3_147}


def dd_replacement_d3_148(dd_replacement_d2_148):
    feature = _clean(dd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_148'] = {'inputs': ['dd_replacement_d2_148'], 'func': dd_replacement_d3_148}


def dd_replacement_d3_149(dd_replacement_d2_149):
    feature = _clean(dd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_149'] = {'inputs': ['dd_replacement_d2_149'], 'func': dd_replacement_d3_149}


def dd_replacement_d3_150(dd_replacement_d2_150):
    feature = _clean(dd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_150'] = {'inputs': ['dd_replacement_d2_150'], 'func': dd_replacement_d3_150}


def dd_replacement_d3_151(dd_replacement_d2_151):
    feature = _clean(dd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_151'] = {'inputs': ['dd_replacement_d2_151'], 'func': dd_replacement_d3_151}


def dd_replacement_d3_152(dd_replacement_d2_152):
    feature = _clean(dd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_152'] = {'inputs': ['dd_replacement_d2_152'], 'func': dd_replacement_d3_152}


def dd_replacement_d3_153(dd_replacement_d2_153):
    feature = _clean(dd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_153'] = {'inputs': ['dd_replacement_d2_153'], 'func': dd_replacement_d3_153}


def dd_replacement_d3_154(dd_replacement_d2_154):
    feature = _clean(dd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_154'] = {'inputs': ['dd_replacement_d2_154'], 'func': dd_replacement_d3_154}


def dd_replacement_d3_155(dd_replacement_d2_155):
    feature = _clean(dd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_155'] = {'inputs': ['dd_replacement_d2_155'], 'func': dd_replacement_d3_155}


def dd_replacement_d3_156(dd_replacement_d2_156):
    feature = _clean(dd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_156'] = {'inputs': ['dd_replacement_d2_156'], 'func': dd_replacement_d3_156}


def dd_replacement_d3_157(dd_replacement_d2_157):
    feature = _clean(dd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_157'] = {'inputs': ['dd_replacement_d2_157'], 'func': dd_replacement_d3_157}


def dd_replacement_d3_158(dd_replacement_d2_158):
    feature = _clean(dd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_158'] = {'inputs': ['dd_replacement_d2_158'], 'func': dd_replacement_d3_158}


def dd_replacement_d3_159(dd_replacement_d2_159):
    feature = _clean(dd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_159'] = {'inputs': ['dd_replacement_d2_159'], 'func': dd_replacement_d3_159}


def dd_replacement_d3_160(dd_replacement_d2_160):
    feature = _clean(dd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_160'] = {'inputs': ['dd_replacement_d2_160'], 'func': dd_replacement_d3_160}


def dd_replacement_d3_161(dd_replacement_d2_161):
    feature = _clean(dd_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_161'] = {'inputs': ['dd_replacement_d2_161'], 'func': dd_replacement_d3_161}


def dd_replacement_d3_162(dd_replacement_d2_162):
    feature = _clean(dd_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_162'] = {'inputs': ['dd_replacement_d2_162'], 'func': dd_replacement_d3_162}


def dd_replacement_d3_163(dd_replacement_d2_163):
    feature = _clean(dd_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_163'] = {'inputs': ['dd_replacement_d2_163'], 'func': dd_replacement_d3_163}


def dd_replacement_d3_164(dd_replacement_d2_164):
    feature = _clean(dd_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_164'] = {'inputs': ['dd_replacement_d2_164'], 'func': dd_replacement_d3_164}


def dd_replacement_d3_165(dd_replacement_d2_165):
    feature = _clean(dd_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_165'] = {'inputs': ['dd_replacement_d2_165'], 'func': dd_replacement_d3_165}


def dd_replacement_d3_166(dd_replacement_d2_166):
    feature = _clean(dd_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_166'] = {'inputs': ['dd_replacement_d2_166'], 'func': dd_replacement_d3_166}


def dd_replacement_d3_167(dd_replacement_d2_167):
    feature = _clean(dd_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_167'] = {'inputs': ['dd_replacement_d2_167'], 'func': dd_replacement_d3_167}


def dd_replacement_d3_168(dd_replacement_d2_168):
    feature = _clean(dd_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_168'] = {'inputs': ['dd_replacement_d2_168'], 'func': dd_replacement_d3_168}


def dd_replacement_d3_169(dd_replacement_d2_169):
    feature = _clean(dd_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_169'] = {'inputs': ['dd_replacement_d2_169'], 'func': dd_replacement_d3_169}


def dd_replacement_d3_170(dd_replacement_d2_170):
    feature = _clean(dd_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
DD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dd_replacement_d3_170'] = {'inputs': ['dd_replacement_d2_170'], 'func': dd_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dd_base_universe_d3_001_dd_002_low_distance_10_002(dd_base_universe_d2_001_dd_002_low_distance_10_002):
    return _base_universe_d3(dd_base_universe_d2_001_dd_002_low_distance_10_002, 1)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_001_dd_002_low_distance_10_002'] = {'inputs': ['dd_base_universe_d2_001_dd_002_low_distance_10_002'], 'func': dd_base_universe_d3_001_dd_002_low_distance_10_002}


def dd_base_universe_d3_002_dd_003_underwater_area_21_003(dd_base_universe_d2_002_dd_003_underwater_area_21_003):
    return _base_universe_d3(dd_base_universe_d2_002_dd_003_underwater_area_21_003, 2)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_002_dd_003_underwater_area_21_003'] = {'inputs': ['dd_base_universe_d2_002_dd_003_underwater_area_21_003'], 'func': dd_base_universe_d3_002_dd_003_underwater_area_21_003}


def dd_base_universe_d3_003_dd_006_lower_high_ratio_84_006(dd_base_universe_d2_003_dd_006_lower_high_ratio_84_006):
    return _base_universe_d3(dd_base_universe_d2_003_dd_006_lower_high_ratio_84_006, 3)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_003_dd_006_lower_high_ratio_84_006'] = {'inputs': ['dd_base_universe_d2_003_dd_006_lower_high_ratio_84_006'], 'func': dd_base_universe_d3_003_dd_006_lower_high_ratio_84_006}


def dd_base_universe_d3_004_dd_008_low_distance_189_008(dd_base_universe_d2_004_dd_008_low_distance_189_008):
    return _base_universe_d3(dd_base_universe_d2_004_dd_008_low_distance_189_008, 4)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_004_dd_008_low_distance_189_008'] = {'inputs': ['dd_base_universe_d2_004_dd_008_low_distance_189_008'], 'func': dd_base_universe_d3_004_dd_008_low_distance_189_008}


def dd_base_universe_d3_005_dd_009_underwater_area_252_009(dd_base_universe_d2_005_dd_009_underwater_area_252_009):
    return _base_universe_d3(dd_base_universe_d2_005_dd_009_underwater_area_252_009, 5)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_005_dd_009_underwater_area_252_009'] = {'inputs': ['dd_base_universe_d2_005_dd_009_underwater_area_252_009'], 'func': dd_base_universe_d3_005_dd_009_underwater_area_252_009}


def dd_base_universe_d3_006_dd_012_lower_high_ratio_756_012(dd_base_universe_d2_006_dd_012_lower_high_ratio_756_012):
    return _base_universe_d3(dd_base_universe_d2_006_dd_012_lower_high_ratio_756_012, 6)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_006_dd_012_lower_high_ratio_756_012'] = {'inputs': ['dd_base_universe_d2_006_dd_012_lower_high_ratio_756_012'], 'func': dd_base_universe_d3_006_dd_012_lower_high_ratio_756_012}


def dd_base_universe_d3_007_dd_014_low_distance_1260_014(dd_base_universe_d2_007_dd_014_low_distance_1260_014):
    return _base_universe_d3(dd_base_universe_d2_007_dd_014_low_distance_1260_014, 7)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_007_dd_014_low_distance_1260_014'] = {'inputs': ['dd_base_universe_d2_007_dd_014_low_distance_1260_014'], 'func': dd_base_universe_d3_007_dd_014_low_distance_1260_014}


def dd_base_universe_d3_008_dd_015_underwater_area_1512_015(dd_base_universe_d2_008_dd_015_underwater_area_1512_015):
    return _base_universe_d3(dd_base_universe_d2_008_dd_015_underwater_area_1512_015, 8)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_008_dd_015_underwater_area_1512_015'] = {'inputs': ['dd_base_universe_d2_008_dd_015_underwater_area_1512_015'], 'func': dd_base_universe_d3_008_dd_015_underwater_area_1512_015}


def dd_base_universe_d3_009_dd_018_lower_high_ratio_21_018(dd_base_universe_d2_009_dd_018_lower_high_ratio_21_018):
    return _base_universe_d3(dd_base_universe_d2_009_dd_018_lower_high_ratio_21_018, 9)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_009_dd_018_lower_high_ratio_21_018'] = {'inputs': ['dd_base_universe_d2_009_dd_018_lower_high_ratio_21_018'], 'func': dd_base_universe_d3_009_dd_018_lower_high_ratio_21_018}


def dd_base_universe_d3_010_dd_020_low_distance_63_020(dd_base_universe_d2_010_dd_020_low_distance_63_020):
    return _base_universe_d3(dd_base_universe_d2_010_dd_020_low_distance_63_020, 10)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_010_dd_020_low_distance_63_020'] = {'inputs': ['dd_base_universe_d2_010_dd_020_low_distance_63_020'], 'func': dd_base_universe_d3_010_dd_020_low_distance_63_020}


def dd_base_universe_d3_011_dd_021_underwater_area_84_021(dd_base_universe_d2_011_dd_021_underwater_area_84_021):
    return _base_universe_d3(dd_base_universe_d2_011_dd_021_underwater_area_84_021, 11)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_011_dd_021_underwater_area_84_021'] = {'inputs': ['dd_base_universe_d2_011_dd_021_underwater_area_84_021'], 'func': dd_base_universe_d3_011_dd_021_underwater_area_84_021}


def dd_base_universe_d3_012_dd_024_lower_high_ratio_252_024(dd_base_universe_d2_012_dd_024_lower_high_ratio_252_024):
    return _base_universe_d3(dd_base_universe_d2_012_dd_024_lower_high_ratio_252_024, 12)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_012_dd_024_lower_high_ratio_252_024'] = {'inputs': ['dd_base_universe_d2_012_dd_024_lower_high_ratio_252_024'], 'func': dd_base_universe_d3_012_dd_024_lower_high_ratio_252_024}


def dd_base_universe_d3_013_dd_026_low_distance_504_026(dd_base_universe_d2_013_dd_026_low_distance_504_026):
    return _base_universe_d3(dd_base_universe_d2_013_dd_026_low_distance_504_026, 13)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_013_dd_026_low_distance_504_026'] = {'inputs': ['dd_base_universe_d2_013_dd_026_low_distance_504_026'], 'func': dd_base_universe_d3_013_dd_026_low_distance_504_026}


def dd_base_universe_d3_014_dd_027_underwater_area_756_027(dd_base_universe_d2_014_dd_027_underwater_area_756_027):
    return _base_universe_d3(dd_base_universe_d2_014_dd_027_underwater_area_756_027, 14)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_014_dd_027_underwater_area_756_027'] = {'inputs': ['dd_base_universe_d2_014_dd_027_underwater_area_756_027'], 'func': dd_base_universe_d3_014_dd_027_underwater_area_756_027}


def dd_base_universe_d3_015_dd_030_lower_high_ratio_1512_030(dd_base_universe_d2_015_dd_030_lower_high_ratio_1512_030):
    return _base_universe_d3(dd_base_universe_d2_015_dd_030_lower_high_ratio_1512_030, 15)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_015_dd_030_lower_high_ratio_1512_030'] = {'inputs': ['dd_base_universe_d2_015_dd_030_lower_high_ratio_1512_030'], 'func': dd_base_universe_d3_015_dd_030_lower_high_ratio_1512_030}


def dd_base_universe_d3_016_dd_basefill_004(dd_base_universe_d2_016_dd_basefill_004):
    return _base_universe_d3(dd_base_universe_d2_016_dd_basefill_004, 16)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_016_dd_basefill_004'] = {'inputs': ['dd_base_universe_d2_016_dd_basefill_004'], 'func': dd_base_universe_d3_016_dd_basefill_004}


def dd_base_universe_d3_017_dd_basefill_005(dd_base_universe_d2_017_dd_basefill_005):
    return _base_universe_d3(dd_base_universe_d2_017_dd_basefill_005, 17)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_017_dd_basefill_005'] = {'inputs': ['dd_base_universe_d2_017_dd_basefill_005'], 'func': dd_base_universe_d3_017_dd_basefill_005}


def dd_base_universe_d3_018_dd_basefill_010(dd_base_universe_d2_018_dd_basefill_010):
    return _base_universe_d3(dd_base_universe_d2_018_dd_basefill_010, 18)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_018_dd_basefill_010'] = {'inputs': ['dd_base_universe_d2_018_dd_basefill_010'], 'func': dd_base_universe_d3_018_dd_basefill_010}


def dd_base_universe_d3_019_dd_basefill_011(dd_base_universe_d2_019_dd_basefill_011):
    return _base_universe_d3(dd_base_universe_d2_019_dd_basefill_011, 19)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_019_dd_basefill_011'] = {'inputs': ['dd_base_universe_d2_019_dd_basefill_011'], 'func': dd_base_universe_d3_019_dd_basefill_011}


def dd_base_universe_d3_020_dd_basefill_016(dd_base_universe_d2_020_dd_basefill_016):
    return _base_universe_d3(dd_base_universe_d2_020_dd_basefill_016, 20)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_020_dd_basefill_016'] = {'inputs': ['dd_base_universe_d2_020_dd_basefill_016'], 'func': dd_base_universe_d3_020_dd_basefill_016}


def dd_base_universe_d3_021_dd_basefill_017(dd_base_universe_d2_021_dd_basefill_017):
    return _base_universe_d3(dd_base_universe_d2_021_dd_basefill_017, 21)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_021_dd_basefill_017'] = {'inputs': ['dd_base_universe_d2_021_dd_basefill_017'], 'func': dd_base_universe_d3_021_dd_basefill_017}


def dd_base_universe_d3_022_dd_basefill_022(dd_base_universe_d2_022_dd_basefill_022):
    return _base_universe_d3(dd_base_universe_d2_022_dd_basefill_022, 22)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_022_dd_basefill_022'] = {'inputs': ['dd_base_universe_d2_022_dd_basefill_022'], 'func': dd_base_universe_d3_022_dd_basefill_022}


def dd_base_universe_d3_023_dd_basefill_023(dd_base_universe_d2_023_dd_basefill_023):
    return _base_universe_d3(dd_base_universe_d2_023_dd_basefill_023, 23)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_023_dd_basefill_023'] = {'inputs': ['dd_base_universe_d2_023_dd_basefill_023'], 'func': dd_base_universe_d3_023_dd_basefill_023}


def dd_base_universe_d3_024_dd_basefill_028(dd_base_universe_d2_024_dd_basefill_028):
    return _base_universe_d3(dd_base_universe_d2_024_dd_basefill_028, 24)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_024_dd_basefill_028'] = {'inputs': ['dd_base_universe_d2_024_dd_basefill_028'], 'func': dd_base_universe_d3_024_dd_basefill_028}


def dd_base_universe_d3_025_dd_basefill_029(dd_base_universe_d2_025_dd_basefill_029):
    return _base_universe_d3(dd_base_universe_d2_025_dd_basefill_029, 25)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_025_dd_basefill_029'] = {'inputs': ['dd_base_universe_d2_025_dd_basefill_029'], 'func': dd_base_universe_d3_025_dd_basefill_029}


def dd_base_universe_d3_026_dd_basefill_031(dd_base_universe_d2_026_dd_basefill_031):
    return _base_universe_d3(dd_base_universe_d2_026_dd_basefill_031, 26)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_026_dd_basefill_031'] = {'inputs': ['dd_base_universe_d2_026_dd_basefill_031'], 'func': dd_base_universe_d3_026_dd_basefill_031}


def dd_base_universe_d3_027_dd_basefill_032(dd_base_universe_d2_027_dd_basefill_032):
    return _base_universe_d3(dd_base_universe_d2_027_dd_basefill_032, 27)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_027_dd_basefill_032'] = {'inputs': ['dd_base_universe_d2_027_dd_basefill_032'], 'func': dd_base_universe_d3_027_dd_basefill_032}


def dd_base_universe_d3_028_dd_basefill_033(dd_base_universe_d2_028_dd_basefill_033):
    return _base_universe_d3(dd_base_universe_d2_028_dd_basefill_033, 28)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_028_dd_basefill_033'] = {'inputs': ['dd_base_universe_d2_028_dd_basefill_033'], 'func': dd_base_universe_d3_028_dd_basefill_033}


def dd_base_universe_d3_029_dd_basefill_034(dd_base_universe_d2_029_dd_basefill_034):
    return _base_universe_d3(dd_base_universe_d2_029_dd_basefill_034, 29)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_029_dd_basefill_034'] = {'inputs': ['dd_base_universe_d2_029_dd_basefill_034'], 'func': dd_base_universe_d3_029_dd_basefill_034}


def dd_base_universe_d3_030_dd_basefill_035(dd_base_universe_d2_030_dd_basefill_035):
    return _base_universe_d3(dd_base_universe_d2_030_dd_basefill_035, 30)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_030_dd_basefill_035'] = {'inputs': ['dd_base_universe_d2_030_dd_basefill_035'], 'func': dd_base_universe_d3_030_dd_basefill_035}


def dd_base_universe_d3_031_dd_basefill_036(dd_base_universe_d2_031_dd_basefill_036):
    return _base_universe_d3(dd_base_universe_d2_031_dd_basefill_036, 31)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_031_dd_basefill_036'] = {'inputs': ['dd_base_universe_d2_031_dd_basefill_036'], 'func': dd_base_universe_d3_031_dd_basefill_036}


def dd_base_universe_d3_032_dd_basefill_037(dd_base_universe_d2_032_dd_basefill_037):
    return _base_universe_d3(dd_base_universe_d2_032_dd_basefill_037, 32)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_032_dd_basefill_037'] = {'inputs': ['dd_base_universe_d2_032_dd_basefill_037'], 'func': dd_base_universe_d3_032_dd_basefill_037}


def dd_base_universe_d3_033_dd_basefill_038(dd_base_universe_d2_033_dd_basefill_038):
    return _base_universe_d3(dd_base_universe_d2_033_dd_basefill_038, 33)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_033_dd_basefill_038'] = {'inputs': ['dd_base_universe_d2_033_dd_basefill_038'], 'func': dd_base_universe_d3_033_dd_basefill_038}


def dd_base_universe_d3_034_dd_basefill_039(dd_base_universe_d2_034_dd_basefill_039):
    return _base_universe_d3(dd_base_universe_d2_034_dd_basefill_039, 34)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_034_dd_basefill_039'] = {'inputs': ['dd_base_universe_d2_034_dd_basefill_039'], 'func': dd_base_universe_d3_034_dd_basefill_039}


def dd_base_universe_d3_035_dd_basefill_040(dd_base_universe_d2_035_dd_basefill_040):
    return _base_universe_d3(dd_base_universe_d2_035_dd_basefill_040, 35)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_035_dd_basefill_040'] = {'inputs': ['dd_base_universe_d2_035_dd_basefill_040'], 'func': dd_base_universe_d3_035_dd_basefill_040}


def dd_base_universe_d3_036_dd_basefill_041(dd_base_universe_d2_036_dd_basefill_041):
    return _base_universe_d3(dd_base_universe_d2_036_dd_basefill_041, 36)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_036_dd_basefill_041'] = {'inputs': ['dd_base_universe_d2_036_dd_basefill_041'], 'func': dd_base_universe_d3_036_dd_basefill_041}


def dd_base_universe_d3_037_dd_basefill_042(dd_base_universe_d2_037_dd_basefill_042):
    return _base_universe_d3(dd_base_universe_d2_037_dd_basefill_042, 37)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_037_dd_basefill_042'] = {'inputs': ['dd_base_universe_d2_037_dd_basefill_042'], 'func': dd_base_universe_d3_037_dd_basefill_042}


def dd_base_universe_d3_038_dd_basefill_043(dd_base_universe_d2_038_dd_basefill_043):
    return _base_universe_d3(dd_base_universe_d2_038_dd_basefill_043, 38)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_038_dd_basefill_043'] = {'inputs': ['dd_base_universe_d2_038_dd_basefill_043'], 'func': dd_base_universe_d3_038_dd_basefill_043}


def dd_base_universe_d3_039_dd_basefill_044(dd_base_universe_d2_039_dd_basefill_044):
    return _base_universe_d3(dd_base_universe_d2_039_dd_basefill_044, 39)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_039_dd_basefill_044'] = {'inputs': ['dd_base_universe_d2_039_dd_basefill_044'], 'func': dd_base_universe_d3_039_dd_basefill_044}


def dd_base_universe_d3_040_dd_basefill_045(dd_base_universe_d2_040_dd_basefill_045):
    return _base_universe_d3(dd_base_universe_d2_040_dd_basefill_045, 40)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_040_dd_basefill_045'] = {'inputs': ['dd_base_universe_d2_040_dd_basefill_045'], 'func': dd_base_universe_d3_040_dd_basefill_045}


def dd_base_universe_d3_041_dd_basefill_046(dd_base_universe_d2_041_dd_basefill_046):
    return _base_universe_d3(dd_base_universe_d2_041_dd_basefill_046, 41)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_041_dd_basefill_046'] = {'inputs': ['dd_base_universe_d2_041_dd_basefill_046'], 'func': dd_base_universe_d3_041_dd_basefill_046}


def dd_base_universe_d3_042_dd_basefill_047(dd_base_universe_d2_042_dd_basefill_047):
    return _base_universe_d3(dd_base_universe_d2_042_dd_basefill_047, 42)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_042_dd_basefill_047'] = {'inputs': ['dd_base_universe_d2_042_dd_basefill_047'], 'func': dd_base_universe_d3_042_dd_basefill_047}


def dd_base_universe_d3_043_dd_basefill_048(dd_base_universe_d2_043_dd_basefill_048):
    return _base_universe_d3(dd_base_universe_d2_043_dd_basefill_048, 43)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_043_dd_basefill_048'] = {'inputs': ['dd_base_universe_d2_043_dd_basefill_048'], 'func': dd_base_universe_d3_043_dd_basefill_048}


def dd_base_universe_d3_044_dd_basefill_049(dd_base_universe_d2_044_dd_basefill_049):
    return _base_universe_d3(dd_base_universe_d2_044_dd_basefill_049, 44)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_044_dd_basefill_049'] = {'inputs': ['dd_base_universe_d2_044_dd_basefill_049'], 'func': dd_base_universe_d3_044_dd_basefill_049}


def dd_base_universe_d3_045_dd_basefill_050(dd_base_universe_d2_045_dd_basefill_050):
    return _base_universe_d3(dd_base_universe_d2_045_dd_basefill_050, 45)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_045_dd_basefill_050'] = {'inputs': ['dd_base_universe_d2_045_dd_basefill_050'], 'func': dd_base_universe_d3_045_dd_basefill_050}


def dd_base_universe_d3_046_dd_basefill_051(dd_base_universe_d2_046_dd_basefill_051):
    return _base_universe_d3(dd_base_universe_d2_046_dd_basefill_051, 46)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_046_dd_basefill_051'] = {'inputs': ['dd_base_universe_d2_046_dd_basefill_051'], 'func': dd_base_universe_d3_046_dd_basefill_051}


def dd_base_universe_d3_047_dd_basefill_052(dd_base_universe_d2_047_dd_basefill_052):
    return _base_universe_d3(dd_base_universe_d2_047_dd_basefill_052, 47)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_047_dd_basefill_052'] = {'inputs': ['dd_base_universe_d2_047_dd_basefill_052'], 'func': dd_base_universe_d3_047_dd_basefill_052}


def dd_base_universe_d3_048_dd_basefill_053(dd_base_universe_d2_048_dd_basefill_053):
    return _base_universe_d3(dd_base_universe_d2_048_dd_basefill_053, 48)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_048_dd_basefill_053'] = {'inputs': ['dd_base_universe_d2_048_dd_basefill_053'], 'func': dd_base_universe_d3_048_dd_basefill_053}


def dd_base_universe_d3_049_dd_basefill_054(dd_base_universe_d2_049_dd_basefill_054):
    return _base_universe_d3(dd_base_universe_d2_049_dd_basefill_054, 49)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_049_dd_basefill_054'] = {'inputs': ['dd_base_universe_d2_049_dd_basefill_054'], 'func': dd_base_universe_d3_049_dd_basefill_054}


def dd_base_universe_d3_050_dd_basefill_055(dd_base_universe_d2_050_dd_basefill_055):
    return _base_universe_d3(dd_base_universe_d2_050_dd_basefill_055, 50)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_050_dd_basefill_055'] = {'inputs': ['dd_base_universe_d2_050_dd_basefill_055'], 'func': dd_base_universe_d3_050_dd_basefill_055}


def dd_base_universe_d3_051_dd_basefill_056(dd_base_universe_d2_051_dd_basefill_056):
    return _base_universe_d3(dd_base_universe_d2_051_dd_basefill_056, 51)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_051_dd_basefill_056'] = {'inputs': ['dd_base_universe_d2_051_dd_basefill_056'], 'func': dd_base_universe_d3_051_dd_basefill_056}


def dd_base_universe_d3_052_dd_basefill_057(dd_base_universe_d2_052_dd_basefill_057):
    return _base_universe_d3(dd_base_universe_d2_052_dd_basefill_057, 52)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_052_dd_basefill_057'] = {'inputs': ['dd_base_universe_d2_052_dd_basefill_057'], 'func': dd_base_universe_d3_052_dd_basefill_057}


def dd_base_universe_d3_053_dd_basefill_058(dd_base_universe_d2_053_dd_basefill_058):
    return _base_universe_d3(dd_base_universe_d2_053_dd_basefill_058, 53)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_053_dd_basefill_058'] = {'inputs': ['dd_base_universe_d2_053_dd_basefill_058'], 'func': dd_base_universe_d3_053_dd_basefill_058}


def dd_base_universe_d3_054_dd_basefill_059(dd_base_universe_d2_054_dd_basefill_059):
    return _base_universe_d3(dd_base_universe_d2_054_dd_basefill_059, 54)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_054_dd_basefill_059'] = {'inputs': ['dd_base_universe_d2_054_dd_basefill_059'], 'func': dd_base_universe_d3_054_dd_basefill_059}


def dd_base_universe_d3_055_dd_basefill_060(dd_base_universe_d2_055_dd_basefill_060):
    return _base_universe_d3(dd_base_universe_d2_055_dd_basefill_060, 55)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_055_dd_basefill_060'] = {'inputs': ['dd_base_universe_d2_055_dd_basefill_060'], 'func': dd_base_universe_d3_055_dd_basefill_060}


def dd_base_universe_d3_056_dd_basefill_061(dd_base_universe_d2_056_dd_basefill_061):
    return _base_universe_d3(dd_base_universe_d2_056_dd_basefill_061, 56)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_056_dd_basefill_061'] = {'inputs': ['dd_base_universe_d2_056_dd_basefill_061'], 'func': dd_base_universe_d3_056_dd_basefill_061}


def dd_base_universe_d3_057_dd_basefill_062(dd_base_universe_d2_057_dd_basefill_062):
    return _base_universe_d3(dd_base_universe_d2_057_dd_basefill_062, 57)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_057_dd_basefill_062'] = {'inputs': ['dd_base_universe_d2_057_dd_basefill_062'], 'func': dd_base_universe_d3_057_dd_basefill_062}


def dd_base_universe_d3_058_dd_basefill_063(dd_base_universe_d2_058_dd_basefill_063):
    return _base_universe_d3(dd_base_universe_d2_058_dd_basefill_063, 58)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_058_dd_basefill_063'] = {'inputs': ['dd_base_universe_d2_058_dd_basefill_063'], 'func': dd_base_universe_d3_058_dd_basefill_063}


def dd_base_universe_d3_059_dd_basefill_064(dd_base_universe_d2_059_dd_basefill_064):
    return _base_universe_d3(dd_base_universe_d2_059_dd_basefill_064, 59)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_059_dd_basefill_064'] = {'inputs': ['dd_base_universe_d2_059_dd_basefill_064'], 'func': dd_base_universe_d3_059_dd_basefill_064}


def dd_base_universe_d3_060_dd_basefill_065(dd_base_universe_d2_060_dd_basefill_065):
    return _base_universe_d3(dd_base_universe_d2_060_dd_basefill_065, 60)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_060_dd_basefill_065'] = {'inputs': ['dd_base_universe_d2_060_dd_basefill_065'], 'func': dd_base_universe_d3_060_dd_basefill_065}


def dd_base_universe_d3_061_dd_basefill_066(dd_base_universe_d2_061_dd_basefill_066):
    return _base_universe_d3(dd_base_universe_d2_061_dd_basefill_066, 61)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_061_dd_basefill_066'] = {'inputs': ['dd_base_universe_d2_061_dd_basefill_066'], 'func': dd_base_universe_d3_061_dd_basefill_066}


def dd_base_universe_d3_062_dd_basefill_067(dd_base_universe_d2_062_dd_basefill_067):
    return _base_universe_d3(dd_base_universe_d2_062_dd_basefill_067, 62)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_062_dd_basefill_067'] = {'inputs': ['dd_base_universe_d2_062_dd_basefill_067'], 'func': dd_base_universe_d3_062_dd_basefill_067}


def dd_base_universe_d3_063_dd_basefill_068(dd_base_universe_d2_063_dd_basefill_068):
    return _base_universe_d3(dd_base_universe_d2_063_dd_basefill_068, 63)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_063_dd_basefill_068'] = {'inputs': ['dd_base_universe_d2_063_dd_basefill_068'], 'func': dd_base_universe_d3_063_dd_basefill_068}


def dd_base_universe_d3_064_dd_basefill_069(dd_base_universe_d2_064_dd_basefill_069):
    return _base_universe_d3(dd_base_universe_d2_064_dd_basefill_069, 64)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_064_dd_basefill_069'] = {'inputs': ['dd_base_universe_d2_064_dd_basefill_069'], 'func': dd_base_universe_d3_064_dd_basefill_069}


def dd_base_universe_d3_065_dd_basefill_070(dd_base_universe_d2_065_dd_basefill_070):
    return _base_universe_d3(dd_base_universe_d2_065_dd_basefill_070, 65)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_065_dd_basefill_070'] = {'inputs': ['dd_base_universe_d2_065_dd_basefill_070'], 'func': dd_base_universe_d3_065_dd_basefill_070}


def dd_base_universe_d3_066_dd_basefill_071(dd_base_universe_d2_066_dd_basefill_071):
    return _base_universe_d3(dd_base_universe_d2_066_dd_basefill_071, 66)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_066_dd_basefill_071'] = {'inputs': ['dd_base_universe_d2_066_dd_basefill_071'], 'func': dd_base_universe_d3_066_dd_basefill_071}


def dd_base_universe_d3_067_dd_basefill_072(dd_base_universe_d2_067_dd_basefill_072):
    return _base_universe_d3(dd_base_universe_d2_067_dd_basefill_072, 67)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_067_dd_basefill_072'] = {'inputs': ['dd_base_universe_d2_067_dd_basefill_072'], 'func': dd_base_universe_d3_067_dd_basefill_072}


def dd_base_universe_d3_068_dd_basefill_073(dd_base_universe_d2_068_dd_basefill_073):
    return _base_universe_d3(dd_base_universe_d2_068_dd_basefill_073, 68)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_068_dd_basefill_073'] = {'inputs': ['dd_base_universe_d2_068_dd_basefill_073'], 'func': dd_base_universe_d3_068_dd_basefill_073}


def dd_base_universe_d3_069_dd_basefill_074(dd_base_universe_d2_069_dd_basefill_074):
    return _base_universe_d3(dd_base_universe_d2_069_dd_basefill_074, 69)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_069_dd_basefill_074'] = {'inputs': ['dd_base_universe_d2_069_dd_basefill_074'], 'func': dd_base_universe_d3_069_dd_basefill_074}


def dd_base_universe_d3_070_dd_basefill_075(dd_base_universe_d2_070_dd_basefill_075):
    return _base_universe_d3(dd_base_universe_d2_070_dd_basefill_075, 70)
DD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dd_base_universe_d3_070_dd_basefill_075'] = {'inputs': ['dd_base_universe_d2_070_dd_basefill_075'], 'func': dd_base_universe_d3_070_dd_basefill_075}
