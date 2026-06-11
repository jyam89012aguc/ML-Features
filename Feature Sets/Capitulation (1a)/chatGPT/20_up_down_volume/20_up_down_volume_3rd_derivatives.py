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



def udv_176_udv_001_volume_spike_ratio_5_001_accel_1(udv_151_udv_001_volume_spike_ratio_5_001_roc_1):
    feature = _s(udv_151_udv_001_volume_spike_ratio_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def udv_177_udv_007_volume_spike_ratio_126_007_accel_5(udv_152_udv_007_volume_spike_ratio_126_007_roc_5):
    feature = _s(udv_152_udv_007_volume_spike_ratio_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def udv_178_udv_013_volume_spike_ratio_1008_013_accel_42(udv_153_udv_013_volume_spike_ratio_1008_013_roc_42):
    feature = _s(udv_153_udv_013_volume_spike_ratio_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def udv_179_udv_019_volume_spike_ratio_42_019_accel_126(udv_154_udv_019_volume_spike_ratio_42_019_roc_126):
    feature = _s(udv_154_udv_019_volume_spike_ratio_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def udv_180_udv_025_volume_spike_ratio_378_025_accel_378(udv_155_udv_025_volume_spike_ratio_378_025_roc_378):
    feature = _s(udv_155_udv_025_volume_spike_ratio_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















UP_DOWN_VOLUME_REGISTRY_3RD_DERIVATIVES = {
    'udv_176_udv_001_volume_spike_ratio_5_001_accel_1': {'inputs': ['udv_151_udv_001_volume_spike_ratio_5_001_roc_1'], 'func': udv_176_udv_001_volume_spike_ratio_5_001_accel_1},
    'udv_177_udv_007_volume_spike_ratio_126_007_accel_5': {'inputs': ['udv_152_udv_007_volume_spike_ratio_126_007_roc_5'], 'func': udv_177_udv_007_volume_spike_ratio_126_007_accel_5},
    'udv_178_udv_013_volume_spike_ratio_1008_013_accel_42': {'inputs': ['udv_153_udv_013_volume_spike_ratio_1008_013_roc_42'], 'func': udv_178_udv_013_volume_spike_ratio_1008_013_accel_42},
    'udv_179_udv_019_volume_spike_ratio_42_019_accel_126': {'inputs': ['udv_154_udv_019_volume_spike_ratio_42_019_roc_126'], 'func': udv_179_udv_019_volume_spike_ratio_42_019_accel_126},
    'udv_180_udv_025_volume_spike_ratio_378_025_accel_378': {'inputs': ['udv_155_udv_025_volume_spike_ratio_378_025_roc_378'], 'func': udv_180_udv_025_volume_spike_ratio_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def udv_replacement_d3_001(udv_replacement_d2_001):
    feature = _clean(udv_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_001'] = {'inputs': ['udv_replacement_d2_001'], 'func': udv_replacement_d3_001}


def udv_replacement_d3_002(udv_replacement_d2_002):
    feature = _clean(udv_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_002'] = {'inputs': ['udv_replacement_d2_002'], 'func': udv_replacement_d3_002}


def udv_replacement_d3_003(udv_replacement_d2_003):
    feature = _clean(udv_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_003'] = {'inputs': ['udv_replacement_d2_003'], 'func': udv_replacement_d3_003}


def udv_replacement_d3_004(udv_replacement_d2_004):
    feature = _clean(udv_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_004'] = {'inputs': ['udv_replacement_d2_004'], 'func': udv_replacement_d3_004}


def udv_replacement_d3_005(udv_replacement_d2_005):
    feature = _clean(udv_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_005'] = {'inputs': ['udv_replacement_d2_005'], 'func': udv_replacement_d3_005}


def udv_replacement_d3_006(udv_replacement_d2_006):
    feature = _clean(udv_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_006'] = {'inputs': ['udv_replacement_d2_006'], 'func': udv_replacement_d3_006}


def udv_replacement_d3_007(udv_replacement_d2_007):
    feature = _clean(udv_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_007'] = {'inputs': ['udv_replacement_d2_007'], 'func': udv_replacement_d3_007}


def udv_replacement_d3_008(udv_replacement_d2_008):
    feature = _clean(udv_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_008'] = {'inputs': ['udv_replacement_d2_008'], 'func': udv_replacement_d3_008}


def udv_replacement_d3_009(udv_replacement_d2_009):
    feature = _clean(udv_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_009'] = {'inputs': ['udv_replacement_d2_009'], 'func': udv_replacement_d3_009}


def udv_replacement_d3_010(udv_replacement_d2_010):
    feature = _clean(udv_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_010'] = {'inputs': ['udv_replacement_d2_010'], 'func': udv_replacement_d3_010}


def udv_replacement_d3_011(udv_replacement_d2_011):
    feature = _clean(udv_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_011'] = {'inputs': ['udv_replacement_d2_011'], 'func': udv_replacement_d3_011}


def udv_replacement_d3_012(udv_replacement_d2_012):
    feature = _clean(udv_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_012'] = {'inputs': ['udv_replacement_d2_012'], 'func': udv_replacement_d3_012}


def udv_replacement_d3_013(udv_replacement_d2_013):
    feature = _clean(udv_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_013'] = {'inputs': ['udv_replacement_d2_013'], 'func': udv_replacement_d3_013}


def udv_replacement_d3_014(udv_replacement_d2_014):
    feature = _clean(udv_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_014'] = {'inputs': ['udv_replacement_d2_014'], 'func': udv_replacement_d3_014}


def udv_replacement_d3_015(udv_replacement_d2_015):
    feature = _clean(udv_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_015'] = {'inputs': ['udv_replacement_d2_015'], 'func': udv_replacement_d3_015}


def udv_replacement_d3_016(udv_replacement_d2_016):
    feature = _clean(udv_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_016'] = {'inputs': ['udv_replacement_d2_016'], 'func': udv_replacement_d3_016}


def udv_replacement_d3_017(udv_replacement_d2_017):
    feature = _clean(udv_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_017'] = {'inputs': ['udv_replacement_d2_017'], 'func': udv_replacement_d3_017}


def udv_replacement_d3_018(udv_replacement_d2_018):
    feature = _clean(udv_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_018'] = {'inputs': ['udv_replacement_d2_018'], 'func': udv_replacement_d3_018}


def udv_replacement_d3_019(udv_replacement_d2_019):
    feature = _clean(udv_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_019'] = {'inputs': ['udv_replacement_d2_019'], 'func': udv_replacement_d3_019}


def udv_replacement_d3_020(udv_replacement_d2_020):
    feature = _clean(udv_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_020'] = {'inputs': ['udv_replacement_d2_020'], 'func': udv_replacement_d3_020}


def udv_replacement_d3_021(udv_replacement_d2_021):
    feature = _clean(udv_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_021'] = {'inputs': ['udv_replacement_d2_021'], 'func': udv_replacement_d3_021}


def udv_replacement_d3_022(udv_replacement_d2_022):
    feature = _clean(udv_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_022'] = {'inputs': ['udv_replacement_d2_022'], 'func': udv_replacement_d3_022}


def udv_replacement_d3_023(udv_replacement_d2_023):
    feature = _clean(udv_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_023'] = {'inputs': ['udv_replacement_d2_023'], 'func': udv_replacement_d3_023}


def udv_replacement_d3_024(udv_replacement_d2_024):
    feature = _clean(udv_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_024'] = {'inputs': ['udv_replacement_d2_024'], 'func': udv_replacement_d3_024}


def udv_replacement_d3_025(udv_replacement_d2_025):
    feature = _clean(udv_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_025'] = {'inputs': ['udv_replacement_d2_025'], 'func': udv_replacement_d3_025}


def udv_replacement_d3_026(udv_replacement_d2_026):
    feature = _clean(udv_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_026'] = {'inputs': ['udv_replacement_d2_026'], 'func': udv_replacement_d3_026}


def udv_replacement_d3_027(udv_replacement_d2_027):
    feature = _clean(udv_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_027'] = {'inputs': ['udv_replacement_d2_027'], 'func': udv_replacement_d3_027}


def udv_replacement_d3_028(udv_replacement_d2_028):
    feature = _clean(udv_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_028'] = {'inputs': ['udv_replacement_d2_028'], 'func': udv_replacement_d3_028}


def udv_replacement_d3_029(udv_replacement_d2_029):
    feature = _clean(udv_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_029'] = {'inputs': ['udv_replacement_d2_029'], 'func': udv_replacement_d3_029}


def udv_replacement_d3_030(udv_replacement_d2_030):
    feature = _clean(udv_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_030'] = {'inputs': ['udv_replacement_d2_030'], 'func': udv_replacement_d3_030}


def udv_replacement_d3_031(udv_replacement_d2_031):
    feature = _clean(udv_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_031'] = {'inputs': ['udv_replacement_d2_031'], 'func': udv_replacement_d3_031}


def udv_replacement_d3_032(udv_replacement_d2_032):
    feature = _clean(udv_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_032'] = {'inputs': ['udv_replacement_d2_032'], 'func': udv_replacement_d3_032}


def udv_replacement_d3_033(udv_replacement_d2_033):
    feature = _clean(udv_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_033'] = {'inputs': ['udv_replacement_d2_033'], 'func': udv_replacement_d3_033}


def udv_replacement_d3_034(udv_replacement_d2_034):
    feature = _clean(udv_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_034'] = {'inputs': ['udv_replacement_d2_034'], 'func': udv_replacement_d3_034}


def udv_replacement_d3_035(udv_replacement_d2_035):
    feature = _clean(udv_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_035'] = {'inputs': ['udv_replacement_d2_035'], 'func': udv_replacement_d3_035}


def udv_replacement_d3_036(udv_replacement_d2_036):
    feature = _clean(udv_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_036'] = {'inputs': ['udv_replacement_d2_036'], 'func': udv_replacement_d3_036}


def udv_replacement_d3_037(udv_replacement_d2_037):
    feature = _clean(udv_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_037'] = {'inputs': ['udv_replacement_d2_037'], 'func': udv_replacement_d3_037}


def udv_replacement_d3_038(udv_replacement_d2_038):
    feature = _clean(udv_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_038'] = {'inputs': ['udv_replacement_d2_038'], 'func': udv_replacement_d3_038}


def udv_replacement_d3_039(udv_replacement_d2_039):
    feature = _clean(udv_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_039'] = {'inputs': ['udv_replacement_d2_039'], 'func': udv_replacement_d3_039}


def udv_replacement_d3_040(udv_replacement_d2_040):
    feature = _clean(udv_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_040'] = {'inputs': ['udv_replacement_d2_040'], 'func': udv_replacement_d3_040}


def udv_replacement_d3_041(udv_replacement_d2_041):
    feature = _clean(udv_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_041'] = {'inputs': ['udv_replacement_d2_041'], 'func': udv_replacement_d3_041}


def udv_replacement_d3_042(udv_replacement_d2_042):
    feature = _clean(udv_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_042'] = {'inputs': ['udv_replacement_d2_042'], 'func': udv_replacement_d3_042}


def udv_replacement_d3_043(udv_replacement_d2_043):
    feature = _clean(udv_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_043'] = {'inputs': ['udv_replacement_d2_043'], 'func': udv_replacement_d3_043}


def udv_replacement_d3_044(udv_replacement_d2_044):
    feature = _clean(udv_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_044'] = {'inputs': ['udv_replacement_d2_044'], 'func': udv_replacement_d3_044}


def udv_replacement_d3_045(udv_replacement_d2_045):
    feature = _clean(udv_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_045'] = {'inputs': ['udv_replacement_d2_045'], 'func': udv_replacement_d3_045}


def udv_replacement_d3_046(udv_replacement_d2_046):
    feature = _clean(udv_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_046'] = {'inputs': ['udv_replacement_d2_046'], 'func': udv_replacement_d3_046}


def udv_replacement_d3_047(udv_replacement_d2_047):
    feature = _clean(udv_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_047'] = {'inputs': ['udv_replacement_d2_047'], 'func': udv_replacement_d3_047}


def udv_replacement_d3_048(udv_replacement_d2_048):
    feature = _clean(udv_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_048'] = {'inputs': ['udv_replacement_d2_048'], 'func': udv_replacement_d3_048}


def udv_replacement_d3_049(udv_replacement_d2_049):
    feature = _clean(udv_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_049'] = {'inputs': ['udv_replacement_d2_049'], 'func': udv_replacement_d3_049}


def udv_replacement_d3_050(udv_replacement_d2_050):
    feature = _clean(udv_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_050'] = {'inputs': ['udv_replacement_d2_050'], 'func': udv_replacement_d3_050}


def udv_replacement_d3_051(udv_replacement_d2_051):
    feature = _clean(udv_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_051'] = {'inputs': ['udv_replacement_d2_051'], 'func': udv_replacement_d3_051}


def udv_replacement_d3_052(udv_replacement_d2_052):
    feature = _clean(udv_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_052'] = {'inputs': ['udv_replacement_d2_052'], 'func': udv_replacement_d3_052}


def udv_replacement_d3_053(udv_replacement_d2_053):
    feature = _clean(udv_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_053'] = {'inputs': ['udv_replacement_d2_053'], 'func': udv_replacement_d3_053}


def udv_replacement_d3_054(udv_replacement_d2_054):
    feature = _clean(udv_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_054'] = {'inputs': ['udv_replacement_d2_054'], 'func': udv_replacement_d3_054}


def udv_replacement_d3_055(udv_replacement_d2_055):
    feature = _clean(udv_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_055'] = {'inputs': ['udv_replacement_d2_055'], 'func': udv_replacement_d3_055}


def udv_replacement_d3_056(udv_replacement_d2_056):
    feature = _clean(udv_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_056'] = {'inputs': ['udv_replacement_d2_056'], 'func': udv_replacement_d3_056}


def udv_replacement_d3_057(udv_replacement_d2_057):
    feature = _clean(udv_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_057'] = {'inputs': ['udv_replacement_d2_057'], 'func': udv_replacement_d3_057}


def udv_replacement_d3_058(udv_replacement_d2_058):
    feature = _clean(udv_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_058'] = {'inputs': ['udv_replacement_d2_058'], 'func': udv_replacement_d3_058}


def udv_replacement_d3_059(udv_replacement_d2_059):
    feature = _clean(udv_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_059'] = {'inputs': ['udv_replacement_d2_059'], 'func': udv_replacement_d3_059}


def udv_replacement_d3_060(udv_replacement_d2_060):
    feature = _clean(udv_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_060'] = {'inputs': ['udv_replacement_d2_060'], 'func': udv_replacement_d3_060}


def udv_replacement_d3_061(udv_replacement_d2_061):
    feature = _clean(udv_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_061'] = {'inputs': ['udv_replacement_d2_061'], 'func': udv_replacement_d3_061}


def udv_replacement_d3_062(udv_replacement_d2_062):
    feature = _clean(udv_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_062'] = {'inputs': ['udv_replacement_d2_062'], 'func': udv_replacement_d3_062}


def udv_replacement_d3_063(udv_replacement_d2_063):
    feature = _clean(udv_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_063'] = {'inputs': ['udv_replacement_d2_063'], 'func': udv_replacement_d3_063}


def udv_replacement_d3_064(udv_replacement_d2_064):
    feature = _clean(udv_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_064'] = {'inputs': ['udv_replacement_d2_064'], 'func': udv_replacement_d3_064}


def udv_replacement_d3_065(udv_replacement_d2_065):
    feature = _clean(udv_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_065'] = {'inputs': ['udv_replacement_d2_065'], 'func': udv_replacement_d3_065}


def udv_replacement_d3_066(udv_replacement_d2_066):
    feature = _clean(udv_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_066'] = {'inputs': ['udv_replacement_d2_066'], 'func': udv_replacement_d3_066}


def udv_replacement_d3_067(udv_replacement_d2_067):
    feature = _clean(udv_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_067'] = {'inputs': ['udv_replacement_d2_067'], 'func': udv_replacement_d3_067}


def udv_replacement_d3_068(udv_replacement_d2_068):
    feature = _clean(udv_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_068'] = {'inputs': ['udv_replacement_d2_068'], 'func': udv_replacement_d3_068}


def udv_replacement_d3_069(udv_replacement_d2_069):
    feature = _clean(udv_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_069'] = {'inputs': ['udv_replacement_d2_069'], 'func': udv_replacement_d3_069}


def udv_replacement_d3_070(udv_replacement_d2_070):
    feature = _clean(udv_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_070'] = {'inputs': ['udv_replacement_d2_070'], 'func': udv_replacement_d3_070}


def udv_replacement_d3_071(udv_replacement_d2_071):
    feature = _clean(udv_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_071'] = {'inputs': ['udv_replacement_d2_071'], 'func': udv_replacement_d3_071}


def udv_replacement_d3_072(udv_replacement_d2_072):
    feature = _clean(udv_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_072'] = {'inputs': ['udv_replacement_d2_072'], 'func': udv_replacement_d3_072}


def udv_replacement_d3_073(udv_replacement_d2_073):
    feature = _clean(udv_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_073'] = {'inputs': ['udv_replacement_d2_073'], 'func': udv_replacement_d3_073}


def udv_replacement_d3_074(udv_replacement_d2_074):
    feature = _clean(udv_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_074'] = {'inputs': ['udv_replacement_d2_074'], 'func': udv_replacement_d3_074}


def udv_replacement_d3_075(udv_replacement_d2_075):
    feature = _clean(udv_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_075'] = {'inputs': ['udv_replacement_d2_075'], 'func': udv_replacement_d3_075}


def udv_replacement_d3_076(udv_replacement_d2_076):
    feature = _clean(udv_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_076'] = {'inputs': ['udv_replacement_d2_076'], 'func': udv_replacement_d3_076}


def udv_replacement_d3_077(udv_replacement_d2_077):
    feature = _clean(udv_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_077'] = {'inputs': ['udv_replacement_d2_077'], 'func': udv_replacement_d3_077}


def udv_replacement_d3_078(udv_replacement_d2_078):
    feature = _clean(udv_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_078'] = {'inputs': ['udv_replacement_d2_078'], 'func': udv_replacement_d3_078}


def udv_replacement_d3_079(udv_replacement_d2_079):
    feature = _clean(udv_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_079'] = {'inputs': ['udv_replacement_d2_079'], 'func': udv_replacement_d3_079}


def udv_replacement_d3_080(udv_replacement_d2_080):
    feature = _clean(udv_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_080'] = {'inputs': ['udv_replacement_d2_080'], 'func': udv_replacement_d3_080}


def udv_replacement_d3_081(udv_replacement_d2_081):
    feature = _clean(udv_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_081'] = {'inputs': ['udv_replacement_d2_081'], 'func': udv_replacement_d3_081}


def udv_replacement_d3_082(udv_replacement_d2_082):
    feature = _clean(udv_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_082'] = {'inputs': ['udv_replacement_d2_082'], 'func': udv_replacement_d3_082}


def udv_replacement_d3_083(udv_replacement_d2_083):
    feature = _clean(udv_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_083'] = {'inputs': ['udv_replacement_d2_083'], 'func': udv_replacement_d3_083}


def udv_replacement_d3_084(udv_replacement_d2_084):
    feature = _clean(udv_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_084'] = {'inputs': ['udv_replacement_d2_084'], 'func': udv_replacement_d3_084}


def udv_replacement_d3_085(udv_replacement_d2_085):
    feature = _clean(udv_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_085'] = {'inputs': ['udv_replacement_d2_085'], 'func': udv_replacement_d3_085}


def udv_replacement_d3_086(udv_replacement_d2_086):
    feature = _clean(udv_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_086'] = {'inputs': ['udv_replacement_d2_086'], 'func': udv_replacement_d3_086}


def udv_replacement_d3_087(udv_replacement_d2_087):
    feature = _clean(udv_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_087'] = {'inputs': ['udv_replacement_d2_087'], 'func': udv_replacement_d3_087}


def udv_replacement_d3_088(udv_replacement_d2_088):
    feature = _clean(udv_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_088'] = {'inputs': ['udv_replacement_d2_088'], 'func': udv_replacement_d3_088}


def udv_replacement_d3_089(udv_replacement_d2_089):
    feature = _clean(udv_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_089'] = {'inputs': ['udv_replacement_d2_089'], 'func': udv_replacement_d3_089}


def udv_replacement_d3_090(udv_replacement_d2_090):
    feature = _clean(udv_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_090'] = {'inputs': ['udv_replacement_d2_090'], 'func': udv_replacement_d3_090}


def udv_replacement_d3_091(udv_replacement_d2_091):
    feature = _clean(udv_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_091'] = {'inputs': ['udv_replacement_d2_091'], 'func': udv_replacement_d3_091}


def udv_replacement_d3_092(udv_replacement_d2_092):
    feature = _clean(udv_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_092'] = {'inputs': ['udv_replacement_d2_092'], 'func': udv_replacement_d3_092}


def udv_replacement_d3_093(udv_replacement_d2_093):
    feature = _clean(udv_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_093'] = {'inputs': ['udv_replacement_d2_093'], 'func': udv_replacement_d3_093}


def udv_replacement_d3_094(udv_replacement_d2_094):
    feature = _clean(udv_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_094'] = {'inputs': ['udv_replacement_d2_094'], 'func': udv_replacement_d3_094}


def udv_replacement_d3_095(udv_replacement_d2_095):
    feature = _clean(udv_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_095'] = {'inputs': ['udv_replacement_d2_095'], 'func': udv_replacement_d3_095}


def udv_replacement_d3_096(udv_replacement_d2_096):
    feature = _clean(udv_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_096'] = {'inputs': ['udv_replacement_d2_096'], 'func': udv_replacement_d3_096}


def udv_replacement_d3_097(udv_replacement_d2_097):
    feature = _clean(udv_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_097'] = {'inputs': ['udv_replacement_d2_097'], 'func': udv_replacement_d3_097}


def udv_replacement_d3_098(udv_replacement_d2_098):
    feature = _clean(udv_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_098'] = {'inputs': ['udv_replacement_d2_098'], 'func': udv_replacement_d3_098}


def udv_replacement_d3_099(udv_replacement_d2_099):
    feature = _clean(udv_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_099'] = {'inputs': ['udv_replacement_d2_099'], 'func': udv_replacement_d3_099}


def udv_replacement_d3_100(udv_replacement_d2_100):
    feature = _clean(udv_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_100'] = {'inputs': ['udv_replacement_d2_100'], 'func': udv_replacement_d3_100}


def udv_replacement_d3_101(udv_replacement_d2_101):
    feature = _clean(udv_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_101'] = {'inputs': ['udv_replacement_d2_101'], 'func': udv_replacement_d3_101}


def udv_replacement_d3_102(udv_replacement_d2_102):
    feature = _clean(udv_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_102'] = {'inputs': ['udv_replacement_d2_102'], 'func': udv_replacement_d3_102}


def udv_replacement_d3_103(udv_replacement_d2_103):
    feature = _clean(udv_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_103'] = {'inputs': ['udv_replacement_d2_103'], 'func': udv_replacement_d3_103}


def udv_replacement_d3_104(udv_replacement_d2_104):
    feature = _clean(udv_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_104'] = {'inputs': ['udv_replacement_d2_104'], 'func': udv_replacement_d3_104}


def udv_replacement_d3_105(udv_replacement_d2_105):
    feature = _clean(udv_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_105'] = {'inputs': ['udv_replacement_d2_105'], 'func': udv_replacement_d3_105}


def udv_replacement_d3_106(udv_replacement_d2_106):
    feature = _clean(udv_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_106'] = {'inputs': ['udv_replacement_d2_106'], 'func': udv_replacement_d3_106}


def udv_replacement_d3_107(udv_replacement_d2_107):
    feature = _clean(udv_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_107'] = {'inputs': ['udv_replacement_d2_107'], 'func': udv_replacement_d3_107}


def udv_replacement_d3_108(udv_replacement_d2_108):
    feature = _clean(udv_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_108'] = {'inputs': ['udv_replacement_d2_108'], 'func': udv_replacement_d3_108}


def udv_replacement_d3_109(udv_replacement_d2_109):
    feature = _clean(udv_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_109'] = {'inputs': ['udv_replacement_d2_109'], 'func': udv_replacement_d3_109}


def udv_replacement_d3_110(udv_replacement_d2_110):
    feature = _clean(udv_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_110'] = {'inputs': ['udv_replacement_d2_110'], 'func': udv_replacement_d3_110}


def udv_replacement_d3_111(udv_replacement_d2_111):
    feature = _clean(udv_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_111'] = {'inputs': ['udv_replacement_d2_111'], 'func': udv_replacement_d3_111}


def udv_replacement_d3_112(udv_replacement_d2_112):
    feature = _clean(udv_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_112'] = {'inputs': ['udv_replacement_d2_112'], 'func': udv_replacement_d3_112}


def udv_replacement_d3_113(udv_replacement_d2_113):
    feature = _clean(udv_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_113'] = {'inputs': ['udv_replacement_d2_113'], 'func': udv_replacement_d3_113}


def udv_replacement_d3_114(udv_replacement_d2_114):
    feature = _clean(udv_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_114'] = {'inputs': ['udv_replacement_d2_114'], 'func': udv_replacement_d3_114}


def udv_replacement_d3_115(udv_replacement_d2_115):
    feature = _clean(udv_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_115'] = {'inputs': ['udv_replacement_d2_115'], 'func': udv_replacement_d3_115}


def udv_replacement_d3_116(udv_replacement_d2_116):
    feature = _clean(udv_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_116'] = {'inputs': ['udv_replacement_d2_116'], 'func': udv_replacement_d3_116}


def udv_replacement_d3_117(udv_replacement_d2_117):
    feature = _clean(udv_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_117'] = {'inputs': ['udv_replacement_d2_117'], 'func': udv_replacement_d3_117}


def udv_replacement_d3_118(udv_replacement_d2_118):
    feature = _clean(udv_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_118'] = {'inputs': ['udv_replacement_d2_118'], 'func': udv_replacement_d3_118}


def udv_replacement_d3_119(udv_replacement_d2_119):
    feature = _clean(udv_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_119'] = {'inputs': ['udv_replacement_d2_119'], 'func': udv_replacement_d3_119}


def udv_replacement_d3_120(udv_replacement_d2_120):
    feature = _clean(udv_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_120'] = {'inputs': ['udv_replacement_d2_120'], 'func': udv_replacement_d3_120}


def udv_replacement_d3_121(udv_replacement_d2_121):
    feature = _clean(udv_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_121'] = {'inputs': ['udv_replacement_d2_121'], 'func': udv_replacement_d3_121}


def udv_replacement_d3_122(udv_replacement_d2_122):
    feature = _clean(udv_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_122'] = {'inputs': ['udv_replacement_d2_122'], 'func': udv_replacement_d3_122}


def udv_replacement_d3_123(udv_replacement_d2_123):
    feature = _clean(udv_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_123'] = {'inputs': ['udv_replacement_d2_123'], 'func': udv_replacement_d3_123}


def udv_replacement_d3_124(udv_replacement_d2_124):
    feature = _clean(udv_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_124'] = {'inputs': ['udv_replacement_d2_124'], 'func': udv_replacement_d3_124}


def udv_replacement_d3_125(udv_replacement_d2_125):
    feature = _clean(udv_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_125'] = {'inputs': ['udv_replacement_d2_125'], 'func': udv_replacement_d3_125}


def udv_replacement_d3_126(udv_replacement_d2_126):
    feature = _clean(udv_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_126'] = {'inputs': ['udv_replacement_d2_126'], 'func': udv_replacement_d3_126}


def udv_replacement_d3_127(udv_replacement_d2_127):
    feature = _clean(udv_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_127'] = {'inputs': ['udv_replacement_d2_127'], 'func': udv_replacement_d3_127}


def udv_replacement_d3_128(udv_replacement_d2_128):
    feature = _clean(udv_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_128'] = {'inputs': ['udv_replacement_d2_128'], 'func': udv_replacement_d3_128}


def udv_replacement_d3_129(udv_replacement_d2_129):
    feature = _clean(udv_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_129'] = {'inputs': ['udv_replacement_d2_129'], 'func': udv_replacement_d3_129}


def udv_replacement_d3_130(udv_replacement_d2_130):
    feature = _clean(udv_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_130'] = {'inputs': ['udv_replacement_d2_130'], 'func': udv_replacement_d3_130}


def udv_replacement_d3_131(udv_replacement_d2_131):
    feature = _clean(udv_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_131'] = {'inputs': ['udv_replacement_d2_131'], 'func': udv_replacement_d3_131}


def udv_replacement_d3_132(udv_replacement_d2_132):
    feature = _clean(udv_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_132'] = {'inputs': ['udv_replacement_d2_132'], 'func': udv_replacement_d3_132}


def udv_replacement_d3_133(udv_replacement_d2_133):
    feature = _clean(udv_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_133'] = {'inputs': ['udv_replacement_d2_133'], 'func': udv_replacement_d3_133}


def udv_replacement_d3_134(udv_replacement_d2_134):
    feature = _clean(udv_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_134'] = {'inputs': ['udv_replacement_d2_134'], 'func': udv_replacement_d3_134}


def udv_replacement_d3_135(udv_replacement_d2_135):
    feature = _clean(udv_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_135'] = {'inputs': ['udv_replacement_d2_135'], 'func': udv_replacement_d3_135}


def udv_replacement_d3_136(udv_replacement_d2_136):
    feature = _clean(udv_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_136'] = {'inputs': ['udv_replacement_d2_136'], 'func': udv_replacement_d3_136}


def udv_replacement_d3_137(udv_replacement_d2_137):
    feature = _clean(udv_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_137'] = {'inputs': ['udv_replacement_d2_137'], 'func': udv_replacement_d3_137}


def udv_replacement_d3_138(udv_replacement_d2_138):
    feature = _clean(udv_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_138'] = {'inputs': ['udv_replacement_d2_138'], 'func': udv_replacement_d3_138}


def udv_replacement_d3_139(udv_replacement_d2_139):
    feature = _clean(udv_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_139'] = {'inputs': ['udv_replacement_d2_139'], 'func': udv_replacement_d3_139}


def udv_replacement_d3_140(udv_replacement_d2_140):
    feature = _clean(udv_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_140'] = {'inputs': ['udv_replacement_d2_140'], 'func': udv_replacement_d3_140}


def udv_replacement_d3_141(udv_replacement_d2_141):
    feature = _clean(udv_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_141'] = {'inputs': ['udv_replacement_d2_141'], 'func': udv_replacement_d3_141}


def udv_replacement_d3_142(udv_replacement_d2_142):
    feature = _clean(udv_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_142'] = {'inputs': ['udv_replacement_d2_142'], 'func': udv_replacement_d3_142}


def udv_replacement_d3_143(udv_replacement_d2_143):
    feature = _clean(udv_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_143'] = {'inputs': ['udv_replacement_d2_143'], 'func': udv_replacement_d3_143}


def udv_replacement_d3_144(udv_replacement_d2_144):
    feature = _clean(udv_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_144'] = {'inputs': ['udv_replacement_d2_144'], 'func': udv_replacement_d3_144}


def udv_replacement_d3_145(udv_replacement_d2_145):
    feature = _clean(udv_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_145'] = {'inputs': ['udv_replacement_d2_145'], 'func': udv_replacement_d3_145}


def udv_replacement_d3_146(udv_replacement_d2_146):
    feature = _clean(udv_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_146'] = {'inputs': ['udv_replacement_d2_146'], 'func': udv_replacement_d3_146}


def udv_replacement_d3_147(udv_replacement_d2_147):
    feature = _clean(udv_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_147'] = {'inputs': ['udv_replacement_d2_147'], 'func': udv_replacement_d3_147}


def udv_replacement_d3_148(udv_replacement_d2_148):
    feature = _clean(udv_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_148'] = {'inputs': ['udv_replacement_d2_148'], 'func': udv_replacement_d3_148}


def udv_replacement_d3_149(udv_replacement_d2_149):
    feature = _clean(udv_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_149'] = {'inputs': ['udv_replacement_d2_149'], 'func': udv_replacement_d3_149}


def udv_replacement_d3_150(udv_replacement_d2_150):
    feature = _clean(udv_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_150'] = {'inputs': ['udv_replacement_d2_150'], 'func': udv_replacement_d3_150}


def udv_replacement_d3_151(udv_replacement_d2_151):
    feature = _clean(udv_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_151'] = {'inputs': ['udv_replacement_d2_151'], 'func': udv_replacement_d3_151}


def udv_replacement_d3_152(udv_replacement_d2_152):
    feature = _clean(udv_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_152'] = {'inputs': ['udv_replacement_d2_152'], 'func': udv_replacement_d3_152}


def udv_replacement_d3_153(udv_replacement_d2_153):
    feature = _clean(udv_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_153'] = {'inputs': ['udv_replacement_d2_153'], 'func': udv_replacement_d3_153}


def udv_replacement_d3_154(udv_replacement_d2_154):
    feature = _clean(udv_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_154'] = {'inputs': ['udv_replacement_d2_154'], 'func': udv_replacement_d3_154}


def udv_replacement_d3_155(udv_replacement_d2_155):
    feature = _clean(udv_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_155'] = {'inputs': ['udv_replacement_d2_155'], 'func': udv_replacement_d3_155}


def udv_replacement_d3_156(udv_replacement_d2_156):
    feature = _clean(udv_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_156'] = {'inputs': ['udv_replacement_d2_156'], 'func': udv_replacement_d3_156}


def udv_replacement_d3_157(udv_replacement_d2_157):
    feature = _clean(udv_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_157'] = {'inputs': ['udv_replacement_d2_157'], 'func': udv_replacement_d3_157}


def udv_replacement_d3_158(udv_replacement_d2_158):
    feature = _clean(udv_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_158'] = {'inputs': ['udv_replacement_d2_158'], 'func': udv_replacement_d3_158}


def udv_replacement_d3_159(udv_replacement_d2_159):
    feature = _clean(udv_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_159'] = {'inputs': ['udv_replacement_d2_159'], 'func': udv_replacement_d3_159}


def udv_replacement_d3_160(udv_replacement_d2_160):
    feature = _clean(udv_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
UDV_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['udv_replacement_d3_160'] = {'inputs': ['udv_replacement_d2_160'], 'func': udv_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def udv_base_universe_d3_001_udv_002_volume_zscore_10_002(udv_base_universe_d2_001_udv_002_volume_zscore_10_002):
    return _base_universe_d3(udv_base_universe_d2_001_udv_002_volume_zscore_10_002, 1)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_001_udv_002_volume_zscore_10_002'] = {'inputs': ['udv_base_universe_d2_001_udv_002_volume_zscore_10_002'], 'func': udv_base_universe_d3_001_udv_002_volume_zscore_10_002}


def udv_base_universe_d3_002_udv_003_down_volume_share_21_003(udv_base_universe_d2_002_udv_003_down_volume_share_21_003):
    return _base_universe_d3(udv_base_universe_d2_002_udv_003_down_volume_share_21_003, 2)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_002_udv_003_down_volume_share_21_003'] = {'inputs': ['udv_base_universe_d2_002_udv_003_down_volume_share_21_003'], 'func': udv_base_universe_d3_002_udv_003_down_volume_share_21_003}


def udv_base_universe_d3_003_udv_004_dollar_volume_shock_42_004(udv_base_universe_d2_003_udv_004_dollar_volume_shock_42_004):
    return _base_universe_d3(udv_base_universe_d2_003_udv_004_dollar_volume_shock_42_004, 3)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_003_udv_004_dollar_volume_shock_42_004'] = {'inputs': ['udv_base_universe_d2_003_udv_004_dollar_volume_shock_42_004'], 'func': udv_base_universe_d3_003_udv_004_dollar_volume_shock_42_004}


def udv_base_universe_d3_004_udv_005_volume_trend_slope_63_005(udv_base_universe_d2_004_udv_005_volume_trend_slope_63_005):
    return _base_universe_d3(udv_base_universe_d2_004_udv_005_volume_trend_slope_63_005, 4)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_004_udv_005_volume_trend_slope_63_005'] = {'inputs': ['udv_base_universe_d2_004_udv_005_volume_trend_slope_63_005'], 'func': udv_base_universe_d3_004_udv_005_volume_trend_slope_63_005}


def udv_base_universe_d3_005_udv_006_price_volume_divergence_84_006(udv_base_universe_d2_005_udv_006_price_volume_divergence_84_006):
    return _base_universe_d3(udv_base_universe_d2_005_udv_006_price_volume_divergence_84_006, 5)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_005_udv_006_price_volume_divergence_84_006'] = {'inputs': ['udv_base_universe_d2_005_udv_006_price_volume_divergence_84_006'], 'func': udv_base_universe_d3_005_udv_006_price_volume_divergence_84_006}


def udv_base_universe_d3_006_udv_008_volume_zscore_189_008(udv_base_universe_d2_006_udv_008_volume_zscore_189_008):
    return _base_universe_d3(udv_base_universe_d2_006_udv_008_volume_zscore_189_008, 6)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_006_udv_008_volume_zscore_189_008'] = {'inputs': ['udv_base_universe_d2_006_udv_008_volume_zscore_189_008'], 'func': udv_base_universe_d3_006_udv_008_volume_zscore_189_008}


def udv_base_universe_d3_007_udv_009_down_volume_share_252_009(udv_base_universe_d2_007_udv_009_down_volume_share_252_009):
    return _base_universe_d3(udv_base_universe_d2_007_udv_009_down_volume_share_252_009, 7)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_007_udv_009_down_volume_share_252_009'] = {'inputs': ['udv_base_universe_d2_007_udv_009_down_volume_share_252_009'], 'func': udv_base_universe_d3_007_udv_009_down_volume_share_252_009}


def udv_base_universe_d3_008_udv_010_dollar_volume_shock_378_010(udv_base_universe_d2_008_udv_010_dollar_volume_shock_378_010):
    return _base_universe_d3(udv_base_universe_d2_008_udv_010_dollar_volume_shock_378_010, 8)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_008_udv_010_dollar_volume_shock_378_010'] = {'inputs': ['udv_base_universe_d2_008_udv_010_dollar_volume_shock_378_010'], 'func': udv_base_universe_d3_008_udv_010_dollar_volume_shock_378_010}


def udv_base_universe_d3_009_udv_011_volume_trend_slope_504_011(udv_base_universe_d2_009_udv_011_volume_trend_slope_504_011):
    return _base_universe_d3(udv_base_universe_d2_009_udv_011_volume_trend_slope_504_011, 9)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_009_udv_011_volume_trend_slope_504_011'] = {'inputs': ['udv_base_universe_d2_009_udv_011_volume_trend_slope_504_011'], 'func': udv_base_universe_d3_009_udv_011_volume_trend_slope_504_011}


def udv_base_universe_d3_010_udv_012_price_volume_divergence_756_012(udv_base_universe_d2_010_udv_012_price_volume_divergence_756_012):
    return _base_universe_d3(udv_base_universe_d2_010_udv_012_price_volume_divergence_756_012, 10)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_010_udv_012_price_volume_divergence_756_012'] = {'inputs': ['udv_base_universe_d2_010_udv_012_price_volume_divergence_756_012'], 'func': udv_base_universe_d3_010_udv_012_price_volume_divergence_756_012}


def udv_base_universe_d3_011_udv_014_volume_zscore_1260_014(udv_base_universe_d2_011_udv_014_volume_zscore_1260_014):
    return _base_universe_d3(udv_base_universe_d2_011_udv_014_volume_zscore_1260_014, 11)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_011_udv_014_volume_zscore_1260_014'] = {'inputs': ['udv_base_universe_d2_011_udv_014_volume_zscore_1260_014'], 'func': udv_base_universe_d3_011_udv_014_volume_zscore_1260_014}


def udv_base_universe_d3_012_udv_015_down_volume_share_1512_015(udv_base_universe_d2_012_udv_015_down_volume_share_1512_015):
    return _base_universe_d3(udv_base_universe_d2_012_udv_015_down_volume_share_1512_015, 12)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_012_udv_015_down_volume_share_1512_015'] = {'inputs': ['udv_base_universe_d2_012_udv_015_down_volume_share_1512_015'], 'func': udv_base_universe_d3_012_udv_015_down_volume_share_1512_015}


def udv_base_universe_d3_013_udv_016_dollar_volume_shock_5_016(udv_base_universe_d2_013_udv_016_dollar_volume_shock_5_016):
    return _base_universe_d3(udv_base_universe_d2_013_udv_016_dollar_volume_shock_5_016, 13)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_013_udv_016_dollar_volume_shock_5_016'] = {'inputs': ['udv_base_universe_d2_013_udv_016_dollar_volume_shock_5_016'], 'func': udv_base_universe_d3_013_udv_016_dollar_volume_shock_5_016}


def udv_base_universe_d3_014_udv_017_volume_trend_slope_10_017(udv_base_universe_d2_014_udv_017_volume_trend_slope_10_017):
    return _base_universe_d3(udv_base_universe_d2_014_udv_017_volume_trend_slope_10_017, 14)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_014_udv_017_volume_trend_slope_10_017'] = {'inputs': ['udv_base_universe_d2_014_udv_017_volume_trend_slope_10_017'], 'func': udv_base_universe_d3_014_udv_017_volume_trend_slope_10_017}


def udv_base_universe_d3_015_udv_018_price_volume_divergence_21_018(udv_base_universe_d2_015_udv_018_price_volume_divergence_21_018):
    return _base_universe_d3(udv_base_universe_d2_015_udv_018_price_volume_divergence_21_018, 15)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_015_udv_018_price_volume_divergence_21_018'] = {'inputs': ['udv_base_universe_d2_015_udv_018_price_volume_divergence_21_018'], 'func': udv_base_universe_d3_015_udv_018_price_volume_divergence_21_018}


def udv_base_universe_d3_016_udv_020_volume_zscore_63_020(udv_base_universe_d2_016_udv_020_volume_zscore_63_020):
    return _base_universe_d3(udv_base_universe_d2_016_udv_020_volume_zscore_63_020, 16)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_016_udv_020_volume_zscore_63_020'] = {'inputs': ['udv_base_universe_d2_016_udv_020_volume_zscore_63_020'], 'func': udv_base_universe_d3_016_udv_020_volume_zscore_63_020}


def udv_base_universe_d3_017_udv_021_down_volume_share_84_021(udv_base_universe_d2_017_udv_021_down_volume_share_84_021):
    return _base_universe_d3(udv_base_universe_d2_017_udv_021_down_volume_share_84_021, 17)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_017_udv_021_down_volume_share_84_021'] = {'inputs': ['udv_base_universe_d2_017_udv_021_down_volume_share_84_021'], 'func': udv_base_universe_d3_017_udv_021_down_volume_share_84_021}


def udv_base_universe_d3_018_udv_022_dollar_volume_shock_126_022(udv_base_universe_d2_018_udv_022_dollar_volume_shock_126_022):
    return _base_universe_d3(udv_base_universe_d2_018_udv_022_dollar_volume_shock_126_022, 18)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_018_udv_022_dollar_volume_shock_126_022'] = {'inputs': ['udv_base_universe_d2_018_udv_022_dollar_volume_shock_126_022'], 'func': udv_base_universe_d3_018_udv_022_dollar_volume_shock_126_022}


def udv_base_universe_d3_019_udv_023_volume_trend_slope_189_023(udv_base_universe_d2_019_udv_023_volume_trend_slope_189_023):
    return _base_universe_d3(udv_base_universe_d2_019_udv_023_volume_trend_slope_189_023, 19)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_019_udv_023_volume_trend_slope_189_023'] = {'inputs': ['udv_base_universe_d2_019_udv_023_volume_trend_slope_189_023'], 'func': udv_base_universe_d3_019_udv_023_volume_trend_slope_189_023}


def udv_base_universe_d3_020_udv_024_price_volume_divergence_252_024(udv_base_universe_d2_020_udv_024_price_volume_divergence_252_024):
    return _base_universe_d3(udv_base_universe_d2_020_udv_024_price_volume_divergence_252_024, 20)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_020_udv_024_price_volume_divergence_252_024'] = {'inputs': ['udv_base_universe_d2_020_udv_024_price_volume_divergence_252_024'], 'func': udv_base_universe_d3_020_udv_024_price_volume_divergence_252_024}


def udv_base_universe_d3_021_udv_026_volume_zscore_504_026(udv_base_universe_d2_021_udv_026_volume_zscore_504_026):
    return _base_universe_d3(udv_base_universe_d2_021_udv_026_volume_zscore_504_026, 21)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_021_udv_026_volume_zscore_504_026'] = {'inputs': ['udv_base_universe_d2_021_udv_026_volume_zscore_504_026'], 'func': udv_base_universe_d3_021_udv_026_volume_zscore_504_026}


def udv_base_universe_d3_022_udv_027_down_volume_share_756_027(udv_base_universe_d2_022_udv_027_down_volume_share_756_027):
    return _base_universe_d3(udv_base_universe_d2_022_udv_027_down_volume_share_756_027, 22)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_022_udv_027_down_volume_share_756_027'] = {'inputs': ['udv_base_universe_d2_022_udv_027_down_volume_share_756_027'], 'func': udv_base_universe_d3_022_udv_027_down_volume_share_756_027}


def udv_base_universe_d3_023_udv_028_dollar_volume_shock_1008_028(udv_base_universe_d2_023_udv_028_dollar_volume_shock_1008_028):
    return _base_universe_d3(udv_base_universe_d2_023_udv_028_dollar_volume_shock_1008_028, 23)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_023_udv_028_dollar_volume_shock_1008_028'] = {'inputs': ['udv_base_universe_d2_023_udv_028_dollar_volume_shock_1008_028'], 'func': udv_base_universe_d3_023_udv_028_dollar_volume_shock_1008_028}


def udv_base_universe_d3_024_udv_029_volume_trend_slope_1260_029(udv_base_universe_d2_024_udv_029_volume_trend_slope_1260_029):
    return _base_universe_d3(udv_base_universe_d2_024_udv_029_volume_trend_slope_1260_029, 24)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_024_udv_029_volume_trend_slope_1260_029'] = {'inputs': ['udv_base_universe_d2_024_udv_029_volume_trend_slope_1260_029'], 'func': udv_base_universe_d3_024_udv_029_volume_trend_slope_1260_029}


def udv_base_universe_d3_025_udv_030_price_volume_divergence_1512_030(udv_base_universe_d2_025_udv_030_price_volume_divergence_1512_030):
    return _base_universe_d3(udv_base_universe_d2_025_udv_030_price_volume_divergence_1512_030, 25)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_025_udv_030_price_volume_divergence_1512_030'] = {'inputs': ['udv_base_universe_d2_025_udv_030_price_volume_divergence_1512_030'], 'func': udv_base_universe_d3_025_udv_030_price_volume_divergence_1512_030}


def udv_base_universe_d3_026_udv_basefill_031(udv_base_universe_d2_026_udv_basefill_031):
    return _base_universe_d3(udv_base_universe_d2_026_udv_basefill_031, 26)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_026_udv_basefill_031'] = {'inputs': ['udv_base_universe_d2_026_udv_basefill_031'], 'func': udv_base_universe_d3_026_udv_basefill_031}


def udv_base_universe_d3_027_udv_basefill_032(udv_base_universe_d2_027_udv_basefill_032):
    return _base_universe_d3(udv_base_universe_d2_027_udv_basefill_032, 27)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_027_udv_basefill_032'] = {'inputs': ['udv_base_universe_d2_027_udv_basefill_032'], 'func': udv_base_universe_d3_027_udv_basefill_032}


def udv_base_universe_d3_028_udv_basefill_033(udv_base_universe_d2_028_udv_basefill_033):
    return _base_universe_d3(udv_base_universe_d2_028_udv_basefill_033, 28)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_028_udv_basefill_033'] = {'inputs': ['udv_base_universe_d2_028_udv_basefill_033'], 'func': udv_base_universe_d3_028_udv_basefill_033}


def udv_base_universe_d3_029_udv_basefill_034(udv_base_universe_d2_029_udv_basefill_034):
    return _base_universe_d3(udv_base_universe_d2_029_udv_basefill_034, 29)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_029_udv_basefill_034'] = {'inputs': ['udv_base_universe_d2_029_udv_basefill_034'], 'func': udv_base_universe_d3_029_udv_basefill_034}


def udv_base_universe_d3_030_udv_basefill_035(udv_base_universe_d2_030_udv_basefill_035):
    return _base_universe_d3(udv_base_universe_d2_030_udv_basefill_035, 30)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_030_udv_basefill_035'] = {'inputs': ['udv_base_universe_d2_030_udv_basefill_035'], 'func': udv_base_universe_d3_030_udv_basefill_035}


def udv_base_universe_d3_031_udv_basefill_036(udv_base_universe_d2_031_udv_basefill_036):
    return _base_universe_d3(udv_base_universe_d2_031_udv_basefill_036, 31)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_031_udv_basefill_036'] = {'inputs': ['udv_base_universe_d2_031_udv_basefill_036'], 'func': udv_base_universe_d3_031_udv_basefill_036}


def udv_base_universe_d3_032_udv_basefill_037(udv_base_universe_d2_032_udv_basefill_037):
    return _base_universe_d3(udv_base_universe_d2_032_udv_basefill_037, 32)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_032_udv_basefill_037'] = {'inputs': ['udv_base_universe_d2_032_udv_basefill_037'], 'func': udv_base_universe_d3_032_udv_basefill_037}


def udv_base_universe_d3_033_udv_basefill_038(udv_base_universe_d2_033_udv_basefill_038):
    return _base_universe_d3(udv_base_universe_d2_033_udv_basefill_038, 33)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_033_udv_basefill_038'] = {'inputs': ['udv_base_universe_d2_033_udv_basefill_038'], 'func': udv_base_universe_d3_033_udv_basefill_038}


def udv_base_universe_d3_034_udv_basefill_039(udv_base_universe_d2_034_udv_basefill_039):
    return _base_universe_d3(udv_base_universe_d2_034_udv_basefill_039, 34)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_034_udv_basefill_039'] = {'inputs': ['udv_base_universe_d2_034_udv_basefill_039'], 'func': udv_base_universe_d3_034_udv_basefill_039}


def udv_base_universe_d3_035_udv_basefill_040(udv_base_universe_d2_035_udv_basefill_040):
    return _base_universe_d3(udv_base_universe_d2_035_udv_basefill_040, 35)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_035_udv_basefill_040'] = {'inputs': ['udv_base_universe_d2_035_udv_basefill_040'], 'func': udv_base_universe_d3_035_udv_basefill_040}


def udv_base_universe_d3_036_udv_basefill_041(udv_base_universe_d2_036_udv_basefill_041):
    return _base_universe_d3(udv_base_universe_d2_036_udv_basefill_041, 36)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_036_udv_basefill_041'] = {'inputs': ['udv_base_universe_d2_036_udv_basefill_041'], 'func': udv_base_universe_d3_036_udv_basefill_041}


def udv_base_universe_d3_037_udv_basefill_042(udv_base_universe_d2_037_udv_basefill_042):
    return _base_universe_d3(udv_base_universe_d2_037_udv_basefill_042, 37)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_037_udv_basefill_042'] = {'inputs': ['udv_base_universe_d2_037_udv_basefill_042'], 'func': udv_base_universe_d3_037_udv_basefill_042}


def udv_base_universe_d3_038_udv_basefill_043(udv_base_universe_d2_038_udv_basefill_043):
    return _base_universe_d3(udv_base_universe_d2_038_udv_basefill_043, 38)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_038_udv_basefill_043'] = {'inputs': ['udv_base_universe_d2_038_udv_basefill_043'], 'func': udv_base_universe_d3_038_udv_basefill_043}


def udv_base_universe_d3_039_udv_basefill_044(udv_base_universe_d2_039_udv_basefill_044):
    return _base_universe_d3(udv_base_universe_d2_039_udv_basefill_044, 39)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_039_udv_basefill_044'] = {'inputs': ['udv_base_universe_d2_039_udv_basefill_044'], 'func': udv_base_universe_d3_039_udv_basefill_044}


def udv_base_universe_d3_040_udv_basefill_045(udv_base_universe_d2_040_udv_basefill_045):
    return _base_universe_d3(udv_base_universe_d2_040_udv_basefill_045, 40)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_040_udv_basefill_045'] = {'inputs': ['udv_base_universe_d2_040_udv_basefill_045'], 'func': udv_base_universe_d3_040_udv_basefill_045}


def udv_base_universe_d3_041_udv_basefill_046(udv_base_universe_d2_041_udv_basefill_046):
    return _base_universe_d3(udv_base_universe_d2_041_udv_basefill_046, 41)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_041_udv_basefill_046'] = {'inputs': ['udv_base_universe_d2_041_udv_basefill_046'], 'func': udv_base_universe_d3_041_udv_basefill_046}


def udv_base_universe_d3_042_udv_basefill_047(udv_base_universe_d2_042_udv_basefill_047):
    return _base_universe_d3(udv_base_universe_d2_042_udv_basefill_047, 42)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_042_udv_basefill_047'] = {'inputs': ['udv_base_universe_d2_042_udv_basefill_047'], 'func': udv_base_universe_d3_042_udv_basefill_047}


def udv_base_universe_d3_043_udv_basefill_048(udv_base_universe_d2_043_udv_basefill_048):
    return _base_universe_d3(udv_base_universe_d2_043_udv_basefill_048, 43)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_043_udv_basefill_048'] = {'inputs': ['udv_base_universe_d2_043_udv_basefill_048'], 'func': udv_base_universe_d3_043_udv_basefill_048}


def udv_base_universe_d3_044_udv_basefill_049(udv_base_universe_d2_044_udv_basefill_049):
    return _base_universe_d3(udv_base_universe_d2_044_udv_basefill_049, 44)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_044_udv_basefill_049'] = {'inputs': ['udv_base_universe_d2_044_udv_basefill_049'], 'func': udv_base_universe_d3_044_udv_basefill_049}


def udv_base_universe_d3_045_udv_basefill_050(udv_base_universe_d2_045_udv_basefill_050):
    return _base_universe_d3(udv_base_universe_d2_045_udv_basefill_050, 45)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_045_udv_basefill_050'] = {'inputs': ['udv_base_universe_d2_045_udv_basefill_050'], 'func': udv_base_universe_d3_045_udv_basefill_050}


def udv_base_universe_d3_046_udv_basefill_051(udv_base_universe_d2_046_udv_basefill_051):
    return _base_universe_d3(udv_base_universe_d2_046_udv_basefill_051, 46)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_046_udv_basefill_051'] = {'inputs': ['udv_base_universe_d2_046_udv_basefill_051'], 'func': udv_base_universe_d3_046_udv_basefill_051}


def udv_base_universe_d3_047_udv_basefill_052(udv_base_universe_d2_047_udv_basefill_052):
    return _base_universe_d3(udv_base_universe_d2_047_udv_basefill_052, 47)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_047_udv_basefill_052'] = {'inputs': ['udv_base_universe_d2_047_udv_basefill_052'], 'func': udv_base_universe_d3_047_udv_basefill_052}


def udv_base_universe_d3_048_udv_basefill_053(udv_base_universe_d2_048_udv_basefill_053):
    return _base_universe_d3(udv_base_universe_d2_048_udv_basefill_053, 48)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_048_udv_basefill_053'] = {'inputs': ['udv_base_universe_d2_048_udv_basefill_053'], 'func': udv_base_universe_d3_048_udv_basefill_053}


def udv_base_universe_d3_049_udv_basefill_054(udv_base_universe_d2_049_udv_basefill_054):
    return _base_universe_d3(udv_base_universe_d2_049_udv_basefill_054, 49)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_049_udv_basefill_054'] = {'inputs': ['udv_base_universe_d2_049_udv_basefill_054'], 'func': udv_base_universe_d3_049_udv_basefill_054}


def udv_base_universe_d3_050_udv_basefill_055(udv_base_universe_d2_050_udv_basefill_055):
    return _base_universe_d3(udv_base_universe_d2_050_udv_basefill_055, 50)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_050_udv_basefill_055'] = {'inputs': ['udv_base_universe_d2_050_udv_basefill_055'], 'func': udv_base_universe_d3_050_udv_basefill_055}


def udv_base_universe_d3_051_udv_basefill_056(udv_base_universe_d2_051_udv_basefill_056):
    return _base_universe_d3(udv_base_universe_d2_051_udv_basefill_056, 51)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_051_udv_basefill_056'] = {'inputs': ['udv_base_universe_d2_051_udv_basefill_056'], 'func': udv_base_universe_d3_051_udv_basefill_056}


def udv_base_universe_d3_052_udv_basefill_057(udv_base_universe_d2_052_udv_basefill_057):
    return _base_universe_d3(udv_base_universe_d2_052_udv_basefill_057, 52)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_052_udv_basefill_057'] = {'inputs': ['udv_base_universe_d2_052_udv_basefill_057'], 'func': udv_base_universe_d3_052_udv_basefill_057}


def udv_base_universe_d3_053_udv_basefill_058(udv_base_universe_d2_053_udv_basefill_058):
    return _base_universe_d3(udv_base_universe_d2_053_udv_basefill_058, 53)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_053_udv_basefill_058'] = {'inputs': ['udv_base_universe_d2_053_udv_basefill_058'], 'func': udv_base_universe_d3_053_udv_basefill_058}


def udv_base_universe_d3_054_udv_basefill_059(udv_base_universe_d2_054_udv_basefill_059):
    return _base_universe_d3(udv_base_universe_d2_054_udv_basefill_059, 54)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_054_udv_basefill_059'] = {'inputs': ['udv_base_universe_d2_054_udv_basefill_059'], 'func': udv_base_universe_d3_054_udv_basefill_059}


def udv_base_universe_d3_055_udv_basefill_060(udv_base_universe_d2_055_udv_basefill_060):
    return _base_universe_d3(udv_base_universe_d2_055_udv_basefill_060, 55)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_055_udv_basefill_060'] = {'inputs': ['udv_base_universe_d2_055_udv_basefill_060'], 'func': udv_base_universe_d3_055_udv_basefill_060}


def udv_base_universe_d3_056_udv_basefill_061(udv_base_universe_d2_056_udv_basefill_061):
    return _base_universe_d3(udv_base_universe_d2_056_udv_basefill_061, 56)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_056_udv_basefill_061'] = {'inputs': ['udv_base_universe_d2_056_udv_basefill_061'], 'func': udv_base_universe_d3_056_udv_basefill_061}


def udv_base_universe_d3_057_udv_basefill_062(udv_base_universe_d2_057_udv_basefill_062):
    return _base_universe_d3(udv_base_universe_d2_057_udv_basefill_062, 57)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_057_udv_basefill_062'] = {'inputs': ['udv_base_universe_d2_057_udv_basefill_062'], 'func': udv_base_universe_d3_057_udv_basefill_062}


def udv_base_universe_d3_058_udv_basefill_063(udv_base_universe_d2_058_udv_basefill_063):
    return _base_universe_d3(udv_base_universe_d2_058_udv_basefill_063, 58)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_058_udv_basefill_063'] = {'inputs': ['udv_base_universe_d2_058_udv_basefill_063'], 'func': udv_base_universe_d3_058_udv_basefill_063}


def udv_base_universe_d3_059_udv_basefill_064(udv_base_universe_d2_059_udv_basefill_064):
    return _base_universe_d3(udv_base_universe_d2_059_udv_basefill_064, 59)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_059_udv_basefill_064'] = {'inputs': ['udv_base_universe_d2_059_udv_basefill_064'], 'func': udv_base_universe_d3_059_udv_basefill_064}


def udv_base_universe_d3_060_udv_basefill_065(udv_base_universe_d2_060_udv_basefill_065):
    return _base_universe_d3(udv_base_universe_d2_060_udv_basefill_065, 60)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_060_udv_basefill_065'] = {'inputs': ['udv_base_universe_d2_060_udv_basefill_065'], 'func': udv_base_universe_d3_060_udv_basefill_065}


def udv_base_universe_d3_061_udv_basefill_066(udv_base_universe_d2_061_udv_basefill_066):
    return _base_universe_d3(udv_base_universe_d2_061_udv_basefill_066, 61)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_061_udv_basefill_066'] = {'inputs': ['udv_base_universe_d2_061_udv_basefill_066'], 'func': udv_base_universe_d3_061_udv_basefill_066}


def udv_base_universe_d3_062_udv_basefill_067(udv_base_universe_d2_062_udv_basefill_067):
    return _base_universe_d3(udv_base_universe_d2_062_udv_basefill_067, 62)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_062_udv_basefill_067'] = {'inputs': ['udv_base_universe_d2_062_udv_basefill_067'], 'func': udv_base_universe_d3_062_udv_basefill_067}


def udv_base_universe_d3_063_udv_basefill_068(udv_base_universe_d2_063_udv_basefill_068):
    return _base_universe_d3(udv_base_universe_d2_063_udv_basefill_068, 63)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_063_udv_basefill_068'] = {'inputs': ['udv_base_universe_d2_063_udv_basefill_068'], 'func': udv_base_universe_d3_063_udv_basefill_068}


def udv_base_universe_d3_064_udv_basefill_069(udv_base_universe_d2_064_udv_basefill_069):
    return _base_universe_d3(udv_base_universe_d2_064_udv_basefill_069, 64)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_064_udv_basefill_069'] = {'inputs': ['udv_base_universe_d2_064_udv_basefill_069'], 'func': udv_base_universe_d3_064_udv_basefill_069}


def udv_base_universe_d3_065_udv_basefill_070(udv_base_universe_d2_065_udv_basefill_070):
    return _base_universe_d3(udv_base_universe_d2_065_udv_basefill_070, 65)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_065_udv_basefill_070'] = {'inputs': ['udv_base_universe_d2_065_udv_basefill_070'], 'func': udv_base_universe_d3_065_udv_basefill_070}


def udv_base_universe_d3_066_udv_basefill_071(udv_base_universe_d2_066_udv_basefill_071):
    return _base_universe_d3(udv_base_universe_d2_066_udv_basefill_071, 66)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_066_udv_basefill_071'] = {'inputs': ['udv_base_universe_d2_066_udv_basefill_071'], 'func': udv_base_universe_d3_066_udv_basefill_071}


def udv_base_universe_d3_067_udv_basefill_072(udv_base_universe_d2_067_udv_basefill_072):
    return _base_universe_d3(udv_base_universe_d2_067_udv_basefill_072, 67)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_067_udv_basefill_072'] = {'inputs': ['udv_base_universe_d2_067_udv_basefill_072'], 'func': udv_base_universe_d3_067_udv_basefill_072}


def udv_base_universe_d3_068_udv_basefill_073(udv_base_universe_d2_068_udv_basefill_073):
    return _base_universe_d3(udv_base_universe_d2_068_udv_basefill_073, 68)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_068_udv_basefill_073'] = {'inputs': ['udv_base_universe_d2_068_udv_basefill_073'], 'func': udv_base_universe_d3_068_udv_basefill_073}


def udv_base_universe_d3_069_udv_basefill_074(udv_base_universe_d2_069_udv_basefill_074):
    return _base_universe_d3(udv_base_universe_d2_069_udv_basefill_074, 69)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_069_udv_basefill_074'] = {'inputs': ['udv_base_universe_d2_069_udv_basefill_074'], 'func': udv_base_universe_d3_069_udv_basefill_074}


def udv_base_universe_d3_070_udv_basefill_075(udv_base_universe_d2_070_udv_basefill_075):
    return _base_universe_d3(udv_base_universe_d2_070_udv_basefill_075, 70)
UDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['udv_base_universe_d3_070_udv_basefill_075'] = {'inputs': ['udv_base_universe_d2_070_udv_basefill_075'], 'func': udv_base_universe_d3_070_udv_basefill_075}
