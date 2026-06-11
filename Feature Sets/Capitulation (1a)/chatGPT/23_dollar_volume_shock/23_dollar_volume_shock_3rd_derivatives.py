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



def dvs_176_dvs_001_volume_spike_ratio_5_001_accel_1(dvs_151_dvs_001_volume_spike_ratio_5_001_roc_1):
    feature = _s(dvs_151_dvs_001_volume_spike_ratio_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def dvs_177_dvs_007_volume_spike_ratio_126_007_accel_5(dvs_152_dvs_007_volume_spike_ratio_126_007_roc_5):
    feature = _s(dvs_152_dvs_007_volume_spike_ratio_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def dvs_178_dvs_013_volume_spike_ratio_1008_013_accel_42(dvs_153_dvs_013_volume_spike_ratio_1008_013_roc_42):
    feature = _s(dvs_153_dvs_013_volume_spike_ratio_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def dvs_179_dvs_019_volume_spike_ratio_42_019_accel_126(dvs_154_dvs_019_volume_spike_ratio_42_019_roc_126):
    feature = _s(dvs_154_dvs_019_volume_spike_ratio_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def dvs_180_dvs_025_volume_spike_ratio_378_025_accel_378(dvs_155_dvs_025_volume_spike_ratio_378_025_roc_378):
    feature = _s(dvs_155_dvs_025_volume_spike_ratio_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















DOLLAR_VOLUME_SHOCK_REGISTRY_3RD_DERIVATIVES = {
    'dvs_176_dvs_001_volume_spike_ratio_5_001_accel_1': {'inputs': ['dvs_151_dvs_001_volume_spike_ratio_5_001_roc_1'], 'func': dvs_176_dvs_001_volume_spike_ratio_5_001_accel_1},
    'dvs_177_dvs_007_volume_spike_ratio_126_007_accel_5': {'inputs': ['dvs_152_dvs_007_volume_spike_ratio_126_007_roc_5'], 'func': dvs_177_dvs_007_volume_spike_ratio_126_007_accel_5},
    'dvs_178_dvs_013_volume_spike_ratio_1008_013_accel_42': {'inputs': ['dvs_153_dvs_013_volume_spike_ratio_1008_013_roc_42'], 'func': dvs_178_dvs_013_volume_spike_ratio_1008_013_accel_42},
    'dvs_179_dvs_019_volume_spike_ratio_42_019_accel_126': {'inputs': ['dvs_154_dvs_019_volume_spike_ratio_42_019_roc_126'], 'func': dvs_179_dvs_019_volume_spike_ratio_42_019_accel_126},
    'dvs_180_dvs_025_volume_spike_ratio_378_025_accel_378': {'inputs': ['dvs_155_dvs_025_volume_spike_ratio_378_025_roc_378'], 'func': dvs_180_dvs_025_volume_spike_ratio_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def dvs_replacement_d3_001(dvs_replacement_d2_001):
    feature = _clean(dvs_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_001'] = {'inputs': ['dvs_replacement_d2_001'], 'func': dvs_replacement_d3_001}


def dvs_replacement_d3_002(dvs_replacement_d2_002):
    feature = _clean(dvs_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_002'] = {'inputs': ['dvs_replacement_d2_002'], 'func': dvs_replacement_d3_002}


def dvs_replacement_d3_003(dvs_replacement_d2_003):
    feature = _clean(dvs_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_003'] = {'inputs': ['dvs_replacement_d2_003'], 'func': dvs_replacement_d3_003}


def dvs_replacement_d3_004(dvs_replacement_d2_004):
    feature = _clean(dvs_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_004'] = {'inputs': ['dvs_replacement_d2_004'], 'func': dvs_replacement_d3_004}


def dvs_replacement_d3_005(dvs_replacement_d2_005):
    feature = _clean(dvs_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_005'] = {'inputs': ['dvs_replacement_d2_005'], 'func': dvs_replacement_d3_005}


def dvs_replacement_d3_006(dvs_replacement_d2_006):
    feature = _clean(dvs_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_006'] = {'inputs': ['dvs_replacement_d2_006'], 'func': dvs_replacement_d3_006}


def dvs_replacement_d3_007(dvs_replacement_d2_007):
    feature = _clean(dvs_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_007'] = {'inputs': ['dvs_replacement_d2_007'], 'func': dvs_replacement_d3_007}


def dvs_replacement_d3_008(dvs_replacement_d2_008):
    feature = _clean(dvs_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_008'] = {'inputs': ['dvs_replacement_d2_008'], 'func': dvs_replacement_d3_008}


def dvs_replacement_d3_009(dvs_replacement_d2_009):
    feature = _clean(dvs_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_009'] = {'inputs': ['dvs_replacement_d2_009'], 'func': dvs_replacement_d3_009}


def dvs_replacement_d3_010(dvs_replacement_d2_010):
    feature = _clean(dvs_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_010'] = {'inputs': ['dvs_replacement_d2_010'], 'func': dvs_replacement_d3_010}


def dvs_replacement_d3_011(dvs_replacement_d2_011):
    feature = _clean(dvs_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_011'] = {'inputs': ['dvs_replacement_d2_011'], 'func': dvs_replacement_d3_011}


def dvs_replacement_d3_012(dvs_replacement_d2_012):
    feature = _clean(dvs_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_012'] = {'inputs': ['dvs_replacement_d2_012'], 'func': dvs_replacement_d3_012}


def dvs_replacement_d3_013(dvs_replacement_d2_013):
    feature = _clean(dvs_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_013'] = {'inputs': ['dvs_replacement_d2_013'], 'func': dvs_replacement_d3_013}


def dvs_replacement_d3_014(dvs_replacement_d2_014):
    feature = _clean(dvs_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_014'] = {'inputs': ['dvs_replacement_d2_014'], 'func': dvs_replacement_d3_014}


def dvs_replacement_d3_015(dvs_replacement_d2_015):
    feature = _clean(dvs_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_015'] = {'inputs': ['dvs_replacement_d2_015'], 'func': dvs_replacement_d3_015}


def dvs_replacement_d3_016(dvs_replacement_d2_016):
    feature = _clean(dvs_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_016'] = {'inputs': ['dvs_replacement_d2_016'], 'func': dvs_replacement_d3_016}


def dvs_replacement_d3_017(dvs_replacement_d2_017):
    feature = _clean(dvs_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_017'] = {'inputs': ['dvs_replacement_d2_017'], 'func': dvs_replacement_d3_017}


def dvs_replacement_d3_018(dvs_replacement_d2_018):
    feature = _clean(dvs_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_018'] = {'inputs': ['dvs_replacement_d2_018'], 'func': dvs_replacement_d3_018}


def dvs_replacement_d3_019(dvs_replacement_d2_019):
    feature = _clean(dvs_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_019'] = {'inputs': ['dvs_replacement_d2_019'], 'func': dvs_replacement_d3_019}


def dvs_replacement_d3_020(dvs_replacement_d2_020):
    feature = _clean(dvs_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_020'] = {'inputs': ['dvs_replacement_d2_020'], 'func': dvs_replacement_d3_020}


def dvs_replacement_d3_021(dvs_replacement_d2_021):
    feature = _clean(dvs_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_021'] = {'inputs': ['dvs_replacement_d2_021'], 'func': dvs_replacement_d3_021}


def dvs_replacement_d3_022(dvs_replacement_d2_022):
    feature = _clean(dvs_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_022'] = {'inputs': ['dvs_replacement_d2_022'], 'func': dvs_replacement_d3_022}


def dvs_replacement_d3_023(dvs_replacement_d2_023):
    feature = _clean(dvs_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_023'] = {'inputs': ['dvs_replacement_d2_023'], 'func': dvs_replacement_d3_023}


def dvs_replacement_d3_024(dvs_replacement_d2_024):
    feature = _clean(dvs_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_024'] = {'inputs': ['dvs_replacement_d2_024'], 'func': dvs_replacement_d3_024}


def dvs_replacement_d3_025(dvs_replacement_d2_025):
    feature = _clean(dvs_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_025'] = {'inputs': ['dvs_replacement_d2_025'], 'func': dvs_replacement_d3_025}


def dvs_replacement_d3_026(dvs_replacement_d2_026):
    feature = _clean(dvs_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_026'] = {'inputs': ['dvs_replacement_d2_026'], 'func': dvs_replacement_d3_026}


def dvs_replacement_d3_027(dvs_replacement_d2_027):
    feature = _clean(dvs_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_027'] = {'inputs': ['dvs_replacement_d2_027'], 'func': dvs_replacement_d3_027}


def dvs_replacement_d3_028(dvs_replacement_d2_028):
    feature = _clean(dvs_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_028'] = {'inputs': ['dvs_replacement_d2_028'], 'func': dvs_replacement_d3_028}


def dvs_replacement_d3_029(dvs_replacement_d2_029):
    feature = _clean(dvs_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_029'] = {'inputs': ['dvs_replacement_d2_029'], 'func': dvs_replacement_d3_029}


def dvs_replacement_d3_030(dvs_replacement_d2_030):
    feature = _clean(dvs_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_030'] = {'inputs': ['dvs_replacement_d2_030'], 'func': dvs_replacement_d3_030}


def dvs_replacement_d3_031(dvs_replacement_d2_031):
    feature = _clean(dvs_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_031'] = {'inputs': ['dvs_replacement_d2_031'], 'func': dvs_replacement_d3_031}


def dvs_replacement_d3_032(dvs_replacement_d2_032):
    feature = _clean(dvs_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_032'] = {'inputs': ['dvs_replacement_d2_032'], 'func': dvs_replacement_d3_032}


def dvs_replacement_d3_033(dvs_replacement_d2_033):
    feature = _clean(dvs_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_033'] = {'inputs': ['dvs_replacement_d2_033'], 'func': dvs_replacement_d3_033}


def dvs_replacement_d3_034(dvs_replacement_d2_034):
    feature = _clean(dvs_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_034'] = {'inputs': ['dvs_replacement_d2_034'], 'func': dvs_replacement_d3_034}


def dvs_replacement_d3_035(dvs_replacement_d2_035):
    feature = _clean(dvs_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_035'] = {'inputs': ['dvs_replacement_d2_035'], 'func': dvs_replacement_d3_035}


def dvs_replacement_d3_036(dvs_replacement_d2_036):
    feature = _clean(dvs_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_036'] = {'inputs': ['dvs_replacement_d2_036'], 'func': dvs_replacement_d3_036}


def dvs_replacement_d3_037(dvs_replacement_d2_037):
    feature = _clean(dvs_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_037'] = {'inputs': ['dvs_replacement_d2_037'], 'func': dvs_replacement_d3_037}


def dvs_replacement_d3_038(dvs_replacement_d2_038):
    feature = _clean(dvs_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_038'] = {'inputs': ['dvs_replacement_d2_038'], 'func': dvs_replacement_d3_038}


def dvs_replacement_d3_039(dvs_replacement_d2_039):
    feature = _clean(dvs_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_039'] = {'inputs': ['dvs_replacement_d2_039'], 'func': dvs_replacement_d3_039}


def dvs_replacement_d3_040(dvs_replacement_d2_040):
    feature = _clean(dvs_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_040'] = {'inputs': ['dvs_replacement_d2_040'], 'func': dvs_replacement_d3_040}


def dvs_replacement_d3_041(dvs_replacement_d2_041):
    feature = _clean(dvs_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_041'] = {'inputs': ['dvs_replacement_d2_041'], 'func': dvs_replacement_d3_041}


def dvs_replacement_d3_042(dvs_replacement_d2_042):
    feature = _clean(dvs_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_042'] = {'inputs': ['dvs_replacement_d2_042'], 'func': dvs_replacement_d3_042}


def dvs_replacement_d3_043(dvs_replacement_d2_043):
    feature = _clean(dvs_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_043'] = {'inputs': ['dvs_replacement_d2_043'], 'func': dvs_replacement_d3_043}


def dvs_replacement_d3_044(dvs_replacement_d2_044):
    feature = _clean(dvs_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_044'] = {'inputs': ['dvs_replacement_d2_044'], 'func': dvs_replacement_d3_044}


def dvs_replacement_d3_045(dvs_replacement_d2_045):
    feature = _clean(dvs_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_045'] = {'inputs': ['dvs_replacement_d2_045'], 'func': dvs_replacement_d3_045}


def dvs_replacement_d3_046(dvs_replacement_d2_046):
    feature = _clean(dvs_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_046'] = {'inputs': ['dvs_replacement_d2_046'], 'func': dvs_replacement_d3_046}


def dvs_replacement_d3_047(dvs_replacement_d2_047):
    feature = _clean(dvs_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_047'] = {'inputs': ['dvs_replacement_d2_047'], 'func': dvs_replacement_d3_047}


def dvs_replacement_d3_048(dvs_replacement_d2_048):
    feature = _clean(dvs_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_048'] = {'inputs': ['dvs_replacement_d2_048'], 'func': dvs_replacement_d3_048}


def dvs_replacement_d3_049(dvs_replacement_d2_049):
    feature = _clean(dvs_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_049'] = {'inputs': ['dvs_replacement_d2_049'], 'func': dvs_replacement_d3_049}


def dvs_replacement_d3_050(dvs_replacement_d2_050):
    feature = _clean(dvs_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_050'] = {'inputs': ['dvs_replacement_d2_050'], 'func': dvs_replacement_d3_050}


def dvs_replacement_d3_051(dvs_replacement_d2_051):
    feature = _clean(dvs_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_051'] = {'inputs': ['dvs_replacement_d2_051'], 'func': dvs_replacement_d3_051}


def dvs_replacement_d3_052(dvs_replacement_d2_052):
    feature = _clean(dvs_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_052'] = {'inputs': ['dvs_replacement_d2_052'], 'func': dvs_replacement_d3_052}


def dvs_replacement_d3_053(dvs_replacement_d2_053):
    feature = _clean(dvs_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_053'] = {'inputs': ['dvs_replacement_d2_053'], 'func': dvs_replacement_d3_053}


def dvs_replacement_d3_054(dvs_replacement_d2_054):
    feature = _clean(dvs_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_054'] = {'inputs': ['dvs_replacement_d2_054'], 'func': dvs_replacement_d3_054}


def dvs_replacement_d3_055(dvs_replacement_d2_055):
    feature = _clean(dvs_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_055'] = {'inputs': ['dvs_replacement_d2_055'], 'func': dvs_replacement_d3_055}


def dvs_replacement_d3_056(dvs_replacement_d2_056):
    feature = _clean(dvs_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_056'] = {'inputs': ['dvs_replacement_d2_056'], 'func': dvs_replacement_d3_056}


def dvs_replacement_d3_057(dvs_replacement_d2_057):
    feature = _clean(dvs_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_057'] = {'inputs': ['dvs_replacement_d2_057'], 'func': dvs_replacement_d3_057}


def dvs_replacement_d3_058(dvs_replacement_d2_058):
    feature = _clean(dvs_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_058'] = {'inputs': ['dvs_replacement_d2_058'], 'func': dvs_replacement_d3_058}


def dvs_replacement_d3_059(dvs_replacement_d2_059):
    feature = _clean(dvs_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_059'] = {'inputs': ['dvs_replacement_d2_059'], 'func': dvs_replacement_d3_059}


def dvs_replacement_d3_060(dvs_replacement_d2_060):
    feature = _clean(dvs_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_060'] = {'inputs': ['dvs_replacement_d2_060'], 'func': dvs_replacement_d3_060}


def dvs_replacement_d3_061(dvs_replacement_d2_061):
    feature = _clean(dvs_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_061'] = {'inputs': ['dvs_replacement_d2_061'], 'func': dvs_replacement_d3_061}


def dvs_replacement_d3_062(dvs_replacement_d2_062):
    feature = _clean(dvs_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_062'] = {'inputs': ['dvs_replacement_d2_062'], 'func': dvs_replacement_d3_062}


def dvs_replacement_d3_063(dvs_replacement_d2_063):
    feature = _clean(dvs_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_063'] = {'inputs': ['dvs_replacement_d2_063'], 'func': dvs_replacement_d3_063}


def dvs_replacement_d3_064(dvs_replacement_d2_064):
    feature = _clean(dvs_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_064'] = {'inputs': ['dvs_replacement_d2_064'], 'func': dvs_replacement_d3_064}


def dvs_replacement_d3_065(dvs_replacement_d2_065):
    feature = _clean(dvs_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_065'] = {'inputs': ['dvs_replacement_d2_065'], 'func': dvs_replacement_d3_065}


def dvs_replacement_d3_066(dvs_replacement_d2_066):
    feature = _clean(dvs_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_066'] = {'inputs': ['dvs_replacement_d2_066'], 'func': dvs_replacement_d3_066}


def dvs_replacement_d3_067(dvs_replacement_d2_067):
    feature = _clean(dvs_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_067'] = {'inputs': ['dvs_replacement_d2_067'], 'func': dvs_replacement_d3_067}


def dvs_replacement_d3_068(dvs_replacement_d2_068):
    feature = _clean(dvs_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_068'] = {'inputs': ['dvs_replacement_d2_068'], 'func': dvs_replacement_d3_068}


def dvs_replacement_d3_069(dvs_replacement_d2_069):
    feature = _clean(dvs_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_069'] = {'inputs': ['dvs_replacement_d2_069'], 'func': dvs_replacement_d3_069}


def dvs_replacement_d3_070(dvs_replacement_d2_070):
    feature = _clean(dvs_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_070'] = {'inputs': ['dvs_replacement_d2_070'], 'func': dvs_replacement_d3_070}


def dvs_replacement_d3_071(dvs_replacement_d2_071):
    feature = _clean(dvs_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_071'] = {'inputs': ['dvs_replacement_d2_071'], 'func': dvs_replacement_d3_071}


def dvs_replacement_d3_072(dvs_replacement_d2_072):
    feature = _clean(dvs_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_072'] = {'inputs': ['dvs_replacement_d2_072'], 'func': dvs_replacement_d3_072}


def dvs_replacement_d3_073(dvs_replacement_d2_073):
    feature = _clean(dvs_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_073'] = {'inputs': ['dvs_replacement_d2_073'], 'func': dvs_replacement_d3_073}


def dvs_replacement_d3_074(dvs_replacement_d2_074):
    feature = _clean(dvs_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_074'] = {'inputs': ['dvs_replacement_d2_074'], 'func': dvs_replacement_d3_074}


def dvs_replacement_d3_075(dvs_replacement_d2_075):
    feature = _clean(dvs_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_075'] = {'inputs': ['dvs_replacement_d2_075'], 'func': dvs_replacement_d3_075}


def dvs_replacement_d3_076(dvs_replacement_d2_076):
    feature = _clean(dvs_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_076'] = {'inputs': ['dvs_replacement_d2_076'], 'func': dvs_replacement_d3_076}


def dvs_replacement_d3_077(dvs_replacement_d2_077):
    feature = _clean(dvs_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_077'] = {'inputs': ['dvs_replacement_d2_077'], 'func': dvs_replacement_d3_077}


def dvs_replacement_d3_078(dvs_replacement_d2_078):
    feature = _clean(dvs_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_078'] = {'inputs': ['dvs_replacement_d2_078'], 'func': dvs_replacement_d3_078}


def dvs_replacement_d3_079(dvs_replacement_d2_079):
    feature = _clean(dvs_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_079'] = {'inputs': ['dvs_replacement_d2_079'], 'func': dvs_replacement_d3_079}


def dvs_replacement_d3_080(dvs_replacement_d2_080):
    feature = _clean(dvs_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_080'] = {'inputs': ['dvs_replacement_d2_080'], 'func': dvs_replacement_d3_080}


def dvs_replacement_d3_081(dvs_replacement_d2_081):
    feature = _clean(dvs_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_081'] = {'inputs': ['dvs_replacement_d2_081'], 'func': dvs_replacement_d3_081}


def dvs_replacement_d3_082(dvs_replacement_d2_082):
    feature = _clean(dvs_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_082'] = {'inputs': ['dvs_replacement_d2_082'], 'func': dvs_replacement_d3_082}


def dvs_replacement_d3_083(dvs_replacement_d2_083):
    feature = _clean(dvs_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_083'] = {'inputs': ['dvs_replacement_d2_083'], 'func': dvs_replacement_d3_083}


def dvs_replacement_d3_084(dvs_replacement_d2_084):
    feature = _clean(dvs_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_084'] = {'inputs': ['dvs_replacement_d2_084'], 'func': dvs_replacement_d3_084}


def dvs_replacement_d3_085(dvs_replacement_d2_085):
    feature = _clean(dvs_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_085'] = {'inputs': ['dvs_replacement_d2_085'], 'func': dvs_replacement_d3_085}


def dvs_replacement_d3_086(dvs_replacement_d2_086):
    feature = _clean(dvs_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_086'] = {'inputs': ['dvs_replacement_d2_086'], 'func': dvs_replacement_d3_086}


def dvs_replacement_d3_087(dvs_replacement_d2_087):
    feature = _clean(dvs_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_087'] = {'inputs': ['dvs_replacement_d2_087'], 'func': dvs_replacement_d3_087}


def dvs_replacement_d3_088(dvs_replacement_d2_088):
    feature = _clean(dvs_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_088'] = {'inputs': ['dvs_replacement_d2_088'], 'func': dvs_replacement_d3_088}


def dvs_replacement_d3_089(dvs_replacement_d2_089):
    feature = _clean(dvs_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_089'] = {'inputs': ['dvs_replacement_d2_089'], 'func': dvs_replacement_d3_089}


def dvs_replacement_d3_090(dvs_replacement_d2_090):
    feature = _clean(dvs_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_090'] = {'inputs': ['dvs_replacement_d2_090'], 'func': dvs_replacement_d3_090}


def dvs_replacement_d3_091(dvs_replacement_d2_091):
    feature = _clean(dvs_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_091'] = {'inputs': ['dvs_replacement_d2_091'], 'func': dvs_replacement_d3_091}


def dvs_replacement_d3_092(dvs_replacement_d2_092):
    feature = _clean(dvs_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_092'] = {'inputs': ['dvs_replacement_d2_092'], 'func': dvs_replacement_d3_092}


def dvs_replacement_d3_093(dvs_replacement_d2_093):
    feature = _clean(dvs_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_093'] = {'inputs': ['dvs_replacement_d2_093'], 'func': dvs_replacement_d3_093}


def dvs_replacement_d3_094(dvs_replacement_d2_094):
    feature = _clean(dvs_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_094'] = {'inputs': ['dvs_replacement_d2_094'], 'func': dvs_replacement_d3_094}


def dvs_replacement_d3_095(dvs_replacement_d2_095):
    feature = _clean(dvs_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_095'] = {'inputs': ['dvs_replacement_d2_095'], 'func': dvs_replacement_d3_095}


def dvs_replacement_d3_096(dvs_replacement_d2_096):
    feature = _clean(dvs_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_096'] = {'inputs': ['dvs_replacement_d2_096'], 'func': dvs_replacement_d3_096}


def dvs_replacement_d3_097(dvs_replacement_d2_097):
    feature = _clean(dvs_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_097'] = {'inputs': ['dvs_replacement_d2_097'], 'func': dvs_replacement_d3_097}


def dvs_replacement_d3_098(dvs_replacement_d2_098):
    feature = _clean(dvs_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_098'] = {'inputs': ['dvs_replacement_d2_098'], 'func': dvs_replacement_d3_098}


def dvs_replacement_d3_099(dvs_replacement_d2_099):
    feature = _clean(dvs_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_099'] = {'inputs': ['dvs_replacement_d2_099'], 'func': dvs_replacement_d3_099}


def dvs_replacement_d3_100(dvs_replacement_d2_100):
    feature = _clean(dvs_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_100'] = {'inputs': ['dvs_replacement_d2_100'], 'func': dvs_replacement_d3_100}


def dvs_replacement_d3_101(dvs_replacement_d2_101):
    feature = _clean(dvs_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_101'] = {'inputs': ['dvs_replacement_d2_101'], 'func': dvs_replacement_d3_101}


def dvs_replacement_d3_102(dvs_replacement_d2_102):
    feature = _clean(dvs_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_102'] = {'inputs': ['dvs_replacement_d2_102'], 'func': dvs_replacement_d3_102}


def dvs_replacement_d3_103(dvs_replacement_d2_103):
    feature = _clean(dvs_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_103'] = {'inputs': ['dvs_replacement_d2_103'], 'func': dvs_replacement_d3_103}


def dvs_replacement_d3_104(dvs_replacement_d2_104):
    feature = _clean(dvs_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_104'] = {'inputs': ['dvs_replacement_d2_104'], 'func': dvs_replacement_d3_104}


def dvs_replacement_d3_105(dvs_replacement_d2_105):
    feature = _clean(dvs_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_105'] = {'inputs': ['dvs_replacement_d2_105'], 'func': dvs_replacement_d3_105}


def dvs_replacement_d3_106(dvs_replacement_d2_106):
    feature = _clean(dvs_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_106'] = {'inputs': ['dvs_replacement_d2_106'], 'func': dvs_replacement_d3_106}


def dvs_replacement_d3_107(dvs_replacement_d2_107):
    feature = _clean(dvs_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_107'] = {'inputs': ['dvs_replacement_d2_107'], 'func': dvs_replacement_d3_107}


def dvs_replacement_d3_108(dvs_replacement_d2_108):
    feature = _clean(dvs_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_108'] = {'inputs': ['dvs_replacement_d2_108'], 'func': dvs_replacement_d3_108}


def dvs_replacement_d3_109(dvs_replacement_d2_109):
    feature = _clean(dvs_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_109'] = {'inputs': ['dvs_replacement_d2_109'], 'func': dvs_replacement_d3_109}


def dvs_replacement_d3_110(dvs_replacement_d2_110):
    feature = _clean(dvs_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_110'] = {'inputs': ['dvs_replacement_d2_110'], 'func': dvs_replacement_d3_110}


def dvs_replacement_d3_111(dvs_replacement_d2_111):
    feature = _clean(dvs_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_111'] = {'inputs': ['dvs_replacement_d2_111'], 'func': dvs_replacement_d3_111}


def dvs_replacement_d3_112(dvs_replacement_d2_112):
    feature = _clean(dvs_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_112'] = {'inputs': ['dvs_replacement_d2_112'], 'func': dvs_replacement_d3_112}


def dvs_replacement_d3_113(dvs_replacement_d2_113):
    feature = _clean(dvs_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_113'] = {'inputs': ['dvs_replacement_d2_113'], 'func': dvs_replacement_d3_113}


def dvs_replacement_d3_114(dvs_replacement_d2_114):
    feature = _clean(dvs_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_114'] = {'inputs': ['dvs_replacement_d2_114'], 'func': dvs_replacement_d3_114}


def dvs_replacement_d3_115(dvs_replacement_d2_115):
    feature = _clean(dvs_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_115'] = {'inputs': ['dvs_replacement_d2_115'], 'func': dvs_replacement_d3_115}


def dvs_replacement_d3_116(dvs_replacement_d2_116):
    feature = _clean(dvs_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_116'] = {'inputs': ['dvs_replacement_d2_116'], 'func': dvs_replacement_d3_116}


def dvs_replacement_d3_117(dvs_replacement_d2_117):
    feature = _clean(dvs_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_117'] = {'inputs': ['dvs_replacement_d2_117'], 'func': dvs_replacement_d3_117}


def dvs_replacement_d3_118(dvs_replacement_d2_118):
    feature = _clean(dvs_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_118'] = {'inputs': ['dvs_replacement_d2_118'], 'func': dvs_replacement_d3_118}


def dvs_replacement_d3_119(dvs_replacement_d2_119):
    feature = _clean(dvs_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_119'] = {'inputs': ['dvs_replacement_d2_119'], 'func': dvs_replacement_d3_119}


def dvs_replacement_d3_120(dvs_replacement_d2_120):
    feature = _clean(dvs_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_120'] = {'inputs': ['dvs_replacement_d2_120'], 'func': dvs_replacement_d3_120}


def dvs_replacement_d3_121(dvs_replacement_d2_121):
    feature = _clean(dvs_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_121'] = {'inputs': ['dvs_replacement_d2_121'], 'func': dvs_replacement_d3_121}


def dvs_replacement_d3_122(dvs_replacement_d2_122):
    feature = _clean(dvs_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_122'] = {'inputs': ['dvs_replacement_d2_122'], 'func': dvs_replacement_d3_122}


def dvs_replacement_d3_123(dvs_replacement_d2_123):
    feature = _clean(dvs_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_123'] = {'inputs': ['dvs_replacement_d2_123'], 'func': dvs_replacement_d3_123}


def dvs_replacement_d3_124(dvs_replacement_d2_124):
    feature = _clean(dvs_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_124'] = {'inputs': ['dvs_replacement_d2_124'], 'func': dvs_replacement_d3_124}


def dvs_replacement_d3_125(dvs_replacement_d2_125):
    feature = _clean(dvs_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_125'] = {'inputs': ['dvs_replacement_d2_125'], 'func': dvs_replacement_d3_125}


def dvs_replacement_d3_126(dvs_replacement_d2_126):
    feature = _clean(dvs_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_126'] = {'inputs': ['dvs_replacement_d2_126'], 'func': dvs_replacement_d3_126}


def dvs_replacement_d3_127(dvs_replacement_d2_127):
    feature = _clean(dvs_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_127'] = {'inputs': ['dvs_replacement_d2_127'], 'func': dvs_replacement_d3_127}


def dvs_replacement_d3_128(dvs_replacement_d2_128):
    feature = _clean(dvs_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_128'] = {'inputs': ['dvs_replacement_d2_128'], 'func': dvs_replacement_d3_128}


def dvs_replacement_d3_129(dvs_replacement_d2_129):
    feature = _clean(dvs_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_129'] = {'inputs': ['dvs_replacement_d2_129'], 'func': dvs_replacement_d3_129}


def dvs_replacement_d3_130(dvs_replacement_d2_130):
    feature = _clean(dvs_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_130'] = {'inputs': ['dvs_replacement_d2_130'], 'func': dvs_replacement_d3_130}


def dvs_replacement_d3_131(dvs_replacement_d2_131):
    feature = _clean(dvs_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_131'] = {'inputs': ['dvs_replacement_d2_131'], 'func': dvs_replacement_d3_131}


def dvs_replacement_d3_132(dvs_replacement_d2_132):
    feature = _clean(dvs_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_132'] = {'inputs': ['dvs_replacement_d2_132'], 'func': dvs_replacement_d3_132}


def dvs_replacement_d3_133(dvs_replacement_d2_133):
    feature = _clean(dvs_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_133'] = {'inputs': ['dvs_replacement_d2_133'], 'func': dvs_replacement_d3_133}


def dvs_replacement_d3_134(dvs_replacement_d2_134):
    feature = _clean(dvs_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_134'] = {'inputs': ['dvs_replacement_d2_134'], 'func': dvs_replacement_d3_134}


def dvs_replacement_d3_135(dvs_replacement_d2_135):
    feature = _clean(dvs_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_135'] = {'inputs': ['dvs_replacement_d2_135'], 'func': dvs_replacement_d3_135}


def dvs_replacement_d3_136(dvs_replacement_d2_136):
    feature = _clean(dvs_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_136'] = {'inputs': ['dvs_replacement_d2_136'], 'func': dvs_replacement_d3_136}


def dvs_replacement_d3_137(dvs_replacement_d2_137):
    feature = _clean(dvs_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_137'] = {'inputs': ['dvs_replacement_d2_137'], 'func': dvs_replacement_d3_137}


def dvs_replacement_d3_138(dvs_replacement_d2_138):
    feature = _clean(dvs_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_138'] = {'inputs': ['dvs_replacement_d2_138'], 'func': dvs_replacement_d3_138}


def dvs_replacement_d3_139(dvs_replacement_d2_139):
    feature = _clean(dvs_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_139'] = {'inputs': ['dvs_replacement_d2_139'], 'func': dvs_replacement_d3_139}


def dvs_replacement_d3_140(dvs_replacement_d2_140):
    feature = _clean(dvs_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_140'] = {'inputs': ['dvs_replacement_d2_140'], 'func': dvs_replacement_d3_140}


def dvs_replacement_d3_141(dvs_replacement_d2_141):
    feature = _clean(dvs_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_141'] = {'inputs': ['dvs_replacement_d2_141'], 'func': dvs_replacement_d3_141}


def dvs_replacement_d3_142(dvs_replacement_d2_142):
    feature = _clean(dvs_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_142'] = {'inputs': ['dvs_replacement_d2_142'], 'func': dvs_replacement_d3_142}


def dvs_replacement_d3_143(dvs_replacement_d2_143):
    feature = _clean(dvs_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_143'] = {'inputs': ['dvs_replacement_d2_143'], 'func': dvs_replacement_d3_143}


def dvs_replacement_d3_144(dvs_replacement_d2_144):
    feature = _clean(dvs_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_144'] = {'inputs': ['dvs_replacement_d2_144'], 'func': dvs_replacement_d3_144}


def dvs_replacement_d3_145(dvs_replacement_d2_145):
    feature = _clean(dvs_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_145'] = {'inputs': ['dvs_replacement_d2_145'], 'func': dvs_replacement_d3_145}


def dvs_replacement_d3_146(dvs_replacement_d2_146):
    feature = _clean(dvs_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_146'] = {'inputs': ['dvs_replacement_d2_146'], 'func': dvs_replacement_d3_146}


def dvs_replacement_d3_147(dvs_replacement_d2_147):
    feature = _clean(dvs_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_147'] = {'inputs': ['dvs_replacement_d2_147'], 'func': dvs_replacement_d3_147}


def dvs_replacement_d3_148(dvs_replacement_d2_148):
    feature = _clean(dvs_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_148'] = {'inputs': ['dvs_replacement_d2_148'], 'func': dvs_replacement_d3_148}


def dvs_replacement_d3_149(dvs_replacement_d2_149):
    feature = _clean(dvs_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_149'] = {'inputs': ['dvs_replacement_d2_149'], 'func': dvs_replacement_d3_149}


def dvs_replacement_d3_150(dvs_replacement_d2_150):
    feature = _clean(dvs_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_150'] = {'inputs': ['dvs_replacement_d2_150'], 'func': dvs_replacement_d3_150}


def dvs_replacement_d3_151(dvs_replacement_d2_151):
    feature = _clean(dvs_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_151'] = {'inputs': ['dvs_replacement_d2_151'], 'func': dvs_replacement_d3_151}


def dvs_replacement_d3_152(dvs_replacement_d2_152):
    feature = _clean(dvs_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_152'] = {'inputs': ['dvs_replacement_d2_152'], 'func': dvs_replacement_d3_152}


def dvs_replacement_d3_153(dvs_replacement_d2_153):
    feature = _clean(dvs_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_153'] = {'inputs': ['dvs_replacement_d2_153'], 'func': dvs_replacement_d3_153}


def dvs_replacement_d3_154(dvs_replacement_d2_154):
    feature = _clean(dvs_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_154'] = {'inputs': ['dvs_replacement_d2_154'], 'func': dvs_replacement_d3_154}


def dvs_replacement_d3_155(dvs_replacement_d2_155):
    feature = _clean(dvs_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_155'] = {'inputs': ['dvs_replacement_d2_155'], 'func': dvs_replacement_d3_155}


def dvs_replacement_d3_156(dvs_replacement_d2_156):
    feature = _clean(dvs_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_156'] = {'inputs': ['dvs_replacement_d2_156'], 'func': dvs_replacement_d3_156}


def dvs_replacement_d3_157(dvs_replacement_d2_157):
    feature = _clean(dvs_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_157'] = {'inputs': ['dvs_replacement_d2_157'], 'func': dvs_replacement_d3_157}


def dvs_replacement_d3_158(dvs_replacement_d2_158):
    feature = _clean(dvs_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_158'] = {'inputs': ['dvs_replacement_d2_158'], 'func': dvs_replacement_d3_158}


def dvs_replacement_d3_159(dvs_replacement_d2_159):
    feature = _clean(dvs_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_159'] = {'inputs': ['dvs_replacement_d2_159'], 'func': dvs_replacement_d3_159}


def dvs_replacement_d3_160(dvs_replacement_d2_160):
    feature = _clean(dvs_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
DVS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dvs_replacement_d3_160'] = {'inputs': ['dvs_replacement_d2_160'], 'func': dvs_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dvs_base_universe_d3_001_dvs_002_volume_zscore_10_002(dvs_base_universe_d2_001_dvs_002_volume_zscore_10_002):
    return _base_universe_d3(dvs_base_universe_d2_001_dvs_002_volume_zscore_10_002, 1)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_001_dvs_002_volume_zscore_10_002'] = {'inputs': ['dvs_base_universe_d2_001_dvs_002_volume_zscore_10_002'], 'func': dvs_base_universe_d3_001_dvs_002_volume_zscore_10_002}


def dvs_base_universe_d3_002_dvs_003_down_volume_share_21_003(dvs_base_universe_d2_002_dvs_003_down_volume_share_21_003):
    return _base_universe_d3(dvs_base_universe_d2_002_dvs_003_down_volume_share_21_003, 2)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_002_dvs_003_down_volume_share_21_003'] = {'inputs': ['dvs_base_universe_d2_002_dvs_003_down_volume_share_21_003'], 'func': dvs_base_universe_d3_002_dvs_003_down_volume_share_21_003}


def dvs_base_universe_d3_003_dvs_004_dollar_volume_shock_42_004(dvs_base_universe_d2_003_dvs_004_dollar_volume_shock_42_004):
    return _base_universe_d3(dvs_base_universe_d2_003_dvs_004_dollar_volume_shock_42_004, 3)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_003_dvs_004_dollar_volume_shock_42_004'] = {'inputs': ['dvs_base_universe_d2_003_dvs_004_dollar_volume_shock_42_004'], 'func': dvs_base_universe_d3_003_dvs_004_dollar_volume_shock_42_004}


def dvs_base_universe_d3_004_dvs_005_volume_trend_slope_63_005(dvs_base_universe_d2_004_dvs_005_volume_trend_slope_63_005):
    return _base_universe_d3(dvs_base_universe_d2_004_dvs_005_volume_trend_slope_63_005, 4)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_004_dvs_005_volume_trend_slope_63_005'] = {'inputs': ['dvs_base_universe_d2_004_dvs_005_volume_trend_slope_63_005'], 'func': dvs_base_universe_d3_004_dvs_005_volume_trend_slope_63_005}


def dvs_base_universe_d3_005_dvs_006_price_volume_divergence_84_006(dvs_base_universe_d2_005_dvs_006_price_volume_divergence_84_006):
    return _base_universe_d3(dvs_base_universe_d2_005_dvs_006_price_volume_divergence_84_006, 5)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_005_dvs_006_price_volume_divergence_84_006'] = {'inputs': ['dvs_base_universe_d2_005_dvs_006_price_volume_divergence_84_006'], 'func': dvs_base_universe_d3_005_dvs_006_price_volume_divergence_84_006}


def dvs_base_universe_d3_006_dvs_008_volume_zscore_189_008(dvs_base_universe_d2_006_dvs_008_volume_zscore_189_008):
    return _base_universe_d3(dvs_base_universe_d2_006_dvs_008_volume_zscore_189_008, 6)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_006_dvs_008_volume_zscore_189_008'] = {'inputs': ['dvs_base_universe_d2_006_dvs_008_volume_zscore_189_008'], 'func': dvs_base_universe_d3_006_dvs_008_volume_zscore_189_008}


def dvs_base_universe_d3_007_dvs_009_down_volume_share_252_009(dvs_base_universe_d2_007_dvs_009_down_volume_share_252_009):
    return _base_universe_d3(dvs_base_universe_d2_007_dvs_009_down_volume_share_252_009, 7)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_007_dvs_009_down_volume_share_252_009'] = {'inputs': ['dvs_base_universe_d2_007_dvs_009_down_volume_share_252_009'], 'func': dvs_base_universe_d3_007_dvs_009_down_volume_share_252_009}


def dvs_base_universe_d3_008_dvs_010_dollar_volume_shock_378_010(dvs_base_universe_d2_008_dvs_010_dollar_volume_shock_378_010):
    return _base_universe_d3(dvs_base_universe_d2_008_dvs_010_dollar_volume_shock_378_010, 8)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_008_dvs_010_dollar_volume_shock_378_010'] = {'inputs': ['dvs_base_universe_d2_008_dvs_010_dollar_volume_shock_378_010'], 'func': dvs_base_universe_d3_008_dvs_010_dollar_volume_shock_378_010}


def dvs_base_universe_d3_009_dvs_011_volume_trend_slope_504_011(dvs_base_universe_d2_009_dvs_011_volume_trend_slope_504_011):
    return _base_universe_d3(dvs_base_universe_d2_009_dvs_011_volume_trend_slope_504_011, 9)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_009_dvs_011_volume_trend_slope_504_011'] = {'inputs': ['dvs_base_universe_d2_009_dvs_011_volume_trend_slope_504_011'], 'func': dvs_base_universe_d3_009_dvs_011_volume_trend_slope_504_011}


def dvs_base_universe_d3_010_dvs_012_price_volume_divergence_756_012(dvs_base_universe_d2_010_dvs_012_price_volume_divergence_756_012):
    return _base_universe_d3(dvs_base_universe_d2_010_dvs_012_price_volume_divergence_756_012, 10)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_010_dvs_012_price_volume_divergence_756_012'] = {'inputs': ['dvs_base_universe_d2_010_dvs_012_price_volume_divergence_756_012'], 'func': dvs_base_universe_d3_010_dvs_012_price_volume_divergence_756_012}


def dvs_base_universe_d3_011_dvs_014_volume_zscore_1260_014(dvs_base_universe_d2_011_dvs_014_volume_zscore_1260_014):
    return _base_universe_d3(dvs_base_universe_d2_011_dvs_014_volume_zscore_1260_014, 11)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_011_dvs_014_volume_zscore_1260_014'] = {'inputs': ['dvs_base_universe_d2_011_dvs_014_volume_zscore_1260_014'], 'func': dvs_base_universe_d3_011_dvs_014_volume_zscore_1260_014}


def dvs_base_universe_d3_012_dvs_015_down_volume_share_1512_015(dvs_base_universe_d2_012_dvs_015_down_volume_share_1512_015):
    return _base_universe_d3(dvs_base_universe_d2_012_dvs_015_down_volume_share_1512_015, 12)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_012_dvs_015_down_volume_share_1512_015'] = {'inputs': ['dvs_base_universe_d2_012_dvs_015_down_volume_share_1512_015'], 'func': dvs_base_universe_d3_012_dvs_015_down_volume_share_1512_015}


def dvs_base_universe_d3_013_dvs_016_dollar_volume_shock_5_016(dvs_base_universe_d2_013_dvs_016_dollar_volume_shock_5_016):
    return _base_universe_d3(dvs_base_universe_d2_013_dvs_016_dollar_volume_shock_5_016, 13)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_013_dvs_016_dollar_volume_shock_5_016'] = {'inputs': ['dvs_base_universe_d2_013_dvs_016_dollar_volume_shock_5_016'], 'func': dvs_base_universe_d3_013_dvs_016_dollar_volume_shock_5_016}


def dvs_base_universe_d3_014_dvs_017_volume_trend_slope_10_017(dvs_base_universe_d2_014_dvs_017_volume_trend_slope_10_017):
    return _base_universe_d3(dvs_base_universe_d2_014_dvs_017_volume_trend_slope_10_017, 14)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_014_dvs_017_volume_trend_slope_10_017'] = {'inputs': ['dvs_base_universe_d2_014_dvs_017_volume_trend_slope_10_017'], 'func': dvs_base_universe_d3_014_dvs_017_volume_trend_slope_10_017}


def dvs_base_universe_d3_015_dvs_018_price_volume_divergence_21_018(dvs_base_universe_d2_015_dvs_018_price_volume_divergence_21_018):
    return _base_universe_d3(dvs_base_universe_d2_015_dvs_018_price_volume_divergence_21_018, 15)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_015_dvs_018_price_volume_divergence_21_018'] = {'inputs': ['dvs_base_universe_d2_015_dvs_018_price_volume_divergence_21_018'], 'func': dvs_base_universe_d3_015_dvs_018_price_volume_divergence_21_018}


def dvs_base_universe_d3_016_dvs_020_volume_zscore_63_020(dvs_base_universe_d2_016_dvs_020_volume_zscore_63_020):
    return _base_universe_d3(dvs_base_universe_d2_016_dvs_020_volume_zscore_63_020, 16)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_016_dvs_020_volume_zscore_63_020'] = {'inputs': ['dvs_base_universe_d2_016_dvs_020_volume_zscore_63_020'], 'func': dvs_base_universe_d3_016_dvs_020_volume_zscore_63_020}


def dvs_base_universe_d3_017_dvs_021_down_volume_share_84_021(dvs_base_universe_d2_017_dvs_021_down_volume_share_84_021):
    return _base_universe_d3(dvs_base_universe_d2_017_dvs_021_down_volume_share_84_021, 17)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_017_dvs_021_down_volume_share_84_021'] = {'inputs': ['dvs_base_universe_d2_017_dvs_021_down_volume_share_84_021'], 'func': dvs_base_universe_d3_017_dvs_021_down_volume_share_84_021}


def dvs_base_universe_d3_018_dvs_022_dollar_volume_shock_126_022(dvs_base_universe_d2_018_dvs_022_dollar_volume_shock_126_022):
    return _base_universe_d3(dvs_base_universe_d2_018_dvs_022_dollar_volume_shock_126_022, 18)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_018_dvs_022_dollar_volume_shock_126_022'] = {'inputs': ['dvs_base_universe_d2_018_dvs_022_dollar_volume_shock_126_022'], 'func': dvs_base_universe_d3_018_dvs_022_dollar_volume_shock_126_022}


def dvs_base_universe_d3_019_dvs_023_volume_trend_slope_189_023(dvs_base_universe_d2_019_dvs_023_volume_trend_slope_189_023):
    return _base_universe_d3(dvs_base_universe_d2_019_dvs_023_volume_trend_slope_189_023, 19)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_019_dvs_023_volume_trend_slope_189_023'] = {'inputs': ['dvs_base_universe_d2_019_dvs_023_volume_trend_slope_189_023'], 'func': dvs_base_universe_d3_019_dvs_023_volume_trend_slope_189_023}


def dvs_base_universe_d3_020_dvs_024_price_volume_divergence_252_024(dvs_base_universe_d2_020_dvs_024_price_volume_divergence_252_024):
    return _base_universe_d3(dvs_base_universe_d2_020_dvs_024_price_volume_divergence_252_024, 20)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_020_dvs_024_price_volume_divergence_252_024'] = {'inputs': ['dvs_base_universe_d2_020_dvs_024_price_volume_divergence_252_024'], 'func': dvs_base_universe_d3_020_dvs_024_price_volume_divergence_252_024}


def dvs_base_universe_d3_021_dvs_026_volume_zscore_504_026(dvs_base_universe_d2_021_dvs_026_volume_zscore_504_026):
    return _base_universe_d3(dvs_base_universe_d2_021_dvs_026_volume_zscore_504_026, 21)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_021_dvs_026_volume_zscore_504_026'] = {'inputs': ['dvs_base_universe_d2_021_dvs_026_volume_zscore_504_026'], 'func': dvs_base_universe_d3_021_dvs_026_volume_zscore_504_026}


def dvs_base_universe_d3_022_dvs_027_down_volume_share_756_027(dvs_base_universe_d2_022_dvs_027_down_volume_share_756_027):
    return _base_universe_d3(dvs_base_universe_d2_022_dvs_027_down_volume_share_756_027, 22)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_022_dvs_027_down_volume_share_756_027'] = {'inputs': ['dvs_base_universe_d2_022_dvs_027_down_volume_share_756_027'], 'func': dvs_base_universe_d3_022_dvs_027_down_volume_share_756_027}


def dvs_base_universe_d3_023_dvs_028_dollar_volume_shock_1008_028(dvs_base_universe_d2_023_dvs_028_dollar_volume_shock_1008_028):
    return _base_universe_d3(dvs_base_universe_d2_023_dvs_028_dollar_volume_shock_1008_028, 23)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_023_dvs_028_dollar_volume_shock_1008_028'] = {'inputs': ['dvs_base_universe_d2_023_dvs_028_dollar_volume_shock_1008_028'], 'func': dvs_base_universe_d3_023_dvs_028_dollar_volume_shock_1008_028}


def dvs_base_universe_d3_024_dvs_029_volume_trend_slope_1260_029(dvs_base_universe_d2_024_dvs_029_volume_trend_slope_1260_029):
    return _base_universe_d3(dvs_base_universe_d2_024_dvs_029_volume_trend_slope_1260_029, 24)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_024_dvs_029_volume_trend_slope_1260_029'] = {'inputs': ['dvs_base_universe_d2_024_dvs_029_volume_trend_slope_1260_029'], 'func': dvs_base_universe_d3_024_dvs_029_volume_trend_slope_1260_029}


def dvs_base_universe_d3_025_dvs_030_price_volume_divergence_1512_030(dvs_base_universe_d2_025_dvs_030_price_volume_divergence_1512_030):
    return _base_universe_d3(dvs_base_universe_d2_025_dvs_030_price_volume_divergence_1512_030, 25)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_025_dvs_030_price_volume_divergence_1512_030'] = {'inputs': ['dvs_base_universe_d2_025_dvs_030_price_volume_divergence_1512_030'], 'func': dvs_base_universe_d3_025_dvs_030_price_volume_divergence_1512_030}


def dvs_base_universe_d3_026_dvs_basefill_031(dvs_base_universe_d2_026_dvs_basefill_031):
    return _base_universe_d3(dvs_base_universe_d2_026_dvs_basefill_031, 26)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_026_dvs_basefill_031'] = {'inputs': ['dvs_base_universe_d2_026_dvs_basefill_031'], 'func': dvs_base_universe_d3_026_dvs_basefill_031}


def dvs_base_universe_d3_027_dvs_basefill_032(dvs_base_universe_d2_027_dvs_basefill_032):
    return _base_universe_d3(dvs_base_universe_d2_027_dvs_basefill_032, 27)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_027_dvs_basefill_032'] = {'inputs': ['dvs_base_universe_d2_027_dvs_basefill_032'], 'func': dvs_base_universe_d3_027_dvs_basefill_032}


def dvs_base_universe_d3_028_dvs_basefill_033(dvs_base_universe_d2_028_dvs_basefill_033):
    return _base_universe_d3(dvs_base_universe_d2_028_dvs_basefill_033, 28)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_028_dvs_basefill_033'] = {'inputs': ['dvs_base_universe_d2_028_dvs_basefill_033'], 'func': dvs_base_universe_d3_028_dvs_basefill_033}


def dvs_base_universe_d3_029_dvs_basefill_034(dvs_base_universe_d2_029_dvs_basefill_034):
    return _base_universe_d3(dvs_base_universe_d2_029_dvs_basefill_034, 29)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_029_dvs_basefill_034'] = {'inputs': ['dvs_base_universe_d2_029_dvs_basefill_034'], 'func': dvs_base_universe_d3_029_dvs_basefill_034}


def dvs_base_universe_d3_030_dvs_basefill_035(dvs_base_universe_d2_030_dvs_basefill_035):
    return _base_universe_d3(dvs_base_universe_d2_030_dvs_basefill_035, 30)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_030_dvs_basefill_035'] = {'inputs': ['dvs_base_universe_d2_030_dvs_basefill_035'], 'func': dvs_base_universe_d3_030_dvs_basefill_035}


def dvs_base_universe_d3_031_dvs_basefill_036(dvs_base_universe_d2_031_dvs_basefill_036):
    return _base_universe_d3(dvs_base_universe_d2_031_dvs_basefill_036, 31)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_031_dvs_basefill_036'] = {'inputs': ['dvs_base_universe_d2_031_dvs_basefill_036'], 'func': dvs_base_universe_d3_031_dvs_basefill_036}


def dvs_base_universe_d3_032_dvs_basefill_037(dvs_base_universe_d2_032_dvs_basefill_037):
    return _base_universe_d3(dvs_base_universe_d2_032_dvs_basefill_037, 32)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_032_dvs_basefill_037'] = {'inputs': ['dvs_base_universe_d2_032_dvs_basefill_037'], 'func': dvs_base_universe_d3_032_dvs_basefill_037}


def dvs_base_universe_d3_033_dvs_basefill_038(dvs_base_universe_d2_033_dvs_basefill_038):
    return _base_universe_d3(dvs_base_universe_d2_033_dvs_basefill_038, 33)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_033_dvs_basefill_038'] = {'inputs': ['dvs_base_universe_d2_033_dvs_basefill_038'], 'func': dvs_base_universe_d3_033_dvs_basefill_038}


def dvs_base_universe_d3_034_dvs_basefill_039(dvs_base_universe_d2_034_dvs_basefill_039):
    return _base_universe_d3(dvs_base_universe_d2_034_dvs_basefill_039, 34)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_034_dvs_basefill_039'] = {'inputs': ['dvs_base_universe_d2_034_dvs_basefill_039'], 'func': dvs_base_universe_d3_034_dvs_basefill_039}


def dvs_base_universe_d3_035_dvs_basefill_040(dvs_base_universe_d2_035_dvs_basefill_040):
    return _base_universe_d3(dvs_base_universe_d2_035_dvs_basefill_040, 35)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_035_dvs_basefill_040'] = {'inputs': ['dvs_base_universe_d2_035_dvs_basefill_040'], 'func': dvs_base_universe_d3_035_dvs_basefill_040}


def dvs_base_universe_d3_036_dvs_basefill_041(dvs_base_universe_d2_036_dvs_basefill_041):
    return _base_universe_d3(dvs_base_universe_d2_036_dvs_basefill_041, 36)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_036_dvs_basefill_041'] = {'inputs': ['dvs_base_universe_d2_036_dvs_basefill_041'], 'func': dvs_base_universe_d3_036_dvs_basefill_041}


def dvs_base_universe_d3_037_dvs_basefill_042(dvs_base_universe_d2_037_dvs_basefill_042):
    return _base_universe_d3(dvs_base_universe_d2_037_dvs_basefill_042, 37)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_037_dvs_basefill_042'] = {'inputs': ['dvs_base_universe_d2_037_dvs_basefill_042'], 'func': dvs_base_universe_d3_037_dvs_basefill_042}


def dvs_base_universe_d3_038_dvs_basefill_043(dvs_base_universe_d2_038_dvs_basefill_043):
    return _base_universe_d3(dvs_base_universe_d2_038_dvs_basefill_043, 38)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_038_dvs_basefill_043'] = {'inputs': ['dvs_base_universe_d2_038_dvs_basefill_043'], 'func': dvs_base_universe_d3_038_dvs_basefill_043}


def dvs_base_universe_d3_039_dvs_basefill_044(dvs_base_universe_d2_039_dvs_basefill_044):
    return _base_universe_d3(dvs_base_universe_d2_039_dvs_basefill_044, 39)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_039_dvs_basefill_044'] = {'inputs': ['dvs_base_universe_d2_039_dvs_basefill_044'], 'func': dvs_base_universe_d3_039_dvs_basefill_044}


def dvs_base_universe_d3_040_dvs_basefill_045(dvs_base_universe_d2_040_dvs_basefill_045):
    return _base_universe_d3(dvs_base_universe_d2_040_dvs_basefill_045, 40)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_040_dvs_basefill_045'] = {'inputs': ['dvs_base_universe_d2_040_dvs_basefill_045'], 'func': dvs_base_universe_d3_040_dvs_basefill_045}


def dvs_base_universe_d3_041_dvs_basefill_046(dvs_base_universe_d2_041_dvs_basefill_046):
    return _base_universe_d3(dvs_base_universe_d2_041_dvs_basefill_046, 41)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_041_dvs_basefill_046'] = {'inputs': ['dvs_base_universe_d2_041_dvs_basefill_046'], 'func': dvs_base_universe_d3_041_dvs_basefill_046}


def dvs_base_universe_d3_042_dvs_basefill_047(dvs_base_universe_d2_042_dvs_basefill_047):
    return _base_universe_d3(dvs_base_universe_d2_042_dvs_basefill_047, 42)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_042_dvs_basefill_047'] = {'inputs': ['dvs_base_universe_d2_042_dvs_basefill_047'], 'func': dvs_base_universe_d3_042_dvs_basefill_047}


def dvs_base_universe_d3_043_dvs_basefill_048(dvs_base_universe_d2_043_dvs_basefill_048):
    return _base_universe_d3(dvs_base_universe_d2_043_dvs_basefill_048, 43)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_043_dvs_basefill_048'] = {'inputs': ['dvs_base_universe_d2_043_dvs_basefill_048'], 'func': dvs_base_universe_d3_043_dvs_basefill_048}


def dvs_base_universe_d3_044_dvs_basefill_049(dvs_base_universe_d2_044_dvs_basefill_049):
    return _base_universe_d3(dvs_base_universe_d2_044_dvs_basefill_049, 44)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_044_dvs_basefill_049'] = {'inputs': ['dvs_base_universe_d2_044_dvs_basefill_049'], 'func': dvs_base_universe_d3_044_dvs_basefill_049}


def dvs_base_universe_d3_045_dvs_basefill_050(dvs_base_universe_d2_045_dvs_basefill_050):
    return _base_universe_d3(dvs_base_universe_d2_045_dvs_basefill_050, 45)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_045_dvs_basefill_050'] = {'inputs': ['dvs_base_universe_d2_045_dvs_basefill_050'], 'func': dvs_base_universe_d3_045_dvs_basefill_050}


def dvs_base_universe_d3_046_dvs_basefill_051(dvs_base_universe_d2_046_dvs_basefill_051):
    return _base_universe_d3(dvs_base_universe_d2_046_dvs_basefill_051, 46)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_046_dvs_basefill_051'] = {'inputs': ['dvs_base_universe_d2_046_dvs_basefill_051'], 'func': dvs_base_universe_d3_046_dvs_basefill_051}


def dvs_base_universe_d3_047_dvs_basefill_052(dvs_base_universe_d2_047_dvs_basefill_052):
    return _base_universe_d3(dvs_base_universe_d2_047_dvs_basefill_052, 47)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_047_dvs_basefill_052'] = {'inputs': ['dvs_base_universe_d2_047_dvs_basefill_052'], 'func': dvs_base_universe_d3_047_dvs_basefill_052}


def dvs_base_universe_d3_048_dvs_basefill_053(dvs_base_universe_d2_048_dvs_basefill_053):
    return _base_universe_d3(dvs_base_universe_d2_048_dvs_basefill_053, 48)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_048_dvs_basefill_053'] = {'inputs': ['dvs_base_universe_d2_048_dvs_basefill_053'], 'func': dvs_base_universe_d3_048_dvs_basefill_053}


def dvs_base_universe_d3_049_dvs_basefill_054(dvs_base_universe_d2_049_dvs_basefill_054):
    return _base_universe_d3(dvs_base_universe_d2_049_dvs_basefill_054, 49)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_049_dvs_basefill_054'] = {'inputs': ['dvs_base_universe_d2_049_dvs_basefill_054'], 'func': dvs_base_universe_d3_049_dvs_basefill_054}


def dvs_base_universe_d3_050_dvs_basefill_055(dvs_base_universe_d2_050_dvs_basefill_055):
    return _base_universe_d3(dvs_base_universe_d2_050_dvs_basefill_055, 50)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_050_dvs_basefill_055'] = {'inputs': ['dvs_base_universe_d2_050_dvs_basefill_055'], 'func': dvs_base_universe_d3_050_dvs_basefill_055}


def dvs_base_universe_d3_051_dvs_basefill_056(dvs_base_universe_d2_051_dvs_basefill_056):
    return _base_universe_d3(dvs_base_universe_d2_051_dvs_basefill_056, 51)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_051_dvs_basefill_056'] = {'inputs': ['dvs_base_universe_d2_051_dvs_basefill_056'], 'func': dvs_base_universe_d3_051_dvs_basefill_056}


def dvs_base_universe_d3_052_dvs_basefill_057(dvs_base_universe_d2_052_dvs_basefill_057):
    return _base_universe_d3(dvs_base_universe_d2_052_dvs_basefill_057, 52)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_052_dvs_basefill_057'] = {'inputs': ['dvs_base_universe_d2_052_dvs_basefill_057'], 'func': dvs_base_universe_d3_052_dvs_basefill_057}


def dvs_base_universe_d3_053_dvs_basefill_058(dvs_base_universe_d2_053_dvs_basefill_058):
    return _base_universe_d3(dvs_base_universe_d2_053_dvs_basefill_058, 53)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_053_dvs_basefill_058'] = {'inputs': ['dvs_base_universe_d2_053_dvs_basefill_058'], 'func': dvs_base_universe_d3_053_dvs_basefill_058}


def dvs_base_universe_d3_054_dvs_basefill_059(dvs_base_universe_d2_054_dvs_basefill_059):
    return _base_universe_d3(dvs_base_universe_d2_054_dvs_basefill_059, 54)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_054_dvs_basefill_059'] = {'inputs': ['dvs_base_universe_d2_054_dvs_basefill_059'], 'func': dvs_base_universe_d3_054_dvs_basefill_059}


def dvs_base_universe_d3_055_dvs_basefill_060(dvs_base_universe_d2_055_dvs_basefill_060):
    return _base_universe_d3(dvs_base_universe_d2_055_dvs_basefill_060, 55)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_055_dvs_basefill_060'] = {'inputs': ['dvs_base_universe_d2_055_dvs_basefill_060'], 'func': dvs_base_universe_d3_055_dvs_basefill_060}


def dvs_base_universe_d3_056_dvs_basefill_061(dvs_base_universe_d2_056_dvs_basefill_061):
    return _base_universe_d3(dvs_base_universe_d2_056_dvs_basefill_061, 56)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_056_dvs_basefill_061'] = {'inputs': ['dvs_base_universe_d2_056_dvs_basefill_061'], 'func': dvs_base_universe_d3_056_dvs_basefill_061}


def dvs_base_universe_d3_057_dvs_basefill_062(dvs_base_universe_d2_057_dvs_basefill_062):
    return _base_universe_d3(dvs_base_universe_d2_057_dvs_basefill_062, 57)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_057_dvs_basefill_062'] = {'inputs': ['dvs_base_universe_d2_057_dvs_basefill_062'], 'func': dvs_base_universe_d3_057_dvs_basefill_062}


def dvs_base_universe_d3_058_dvs_basefill_063(dvs_base_universe_d2_058_dvs_basefill_063):
    return _base_universe_d3(dvs_base_universe_d2_058_dvs_basefill_063, 58)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_058_dvs_basefill_063'] = {'inputs': ['dvs_base_universe_d2_058_dvs_basefill_063'], 'func': dvs_base_universe_d3_058_dvs_basefill_063}


def dvs_base_universe_d3_059_dvs_basefill_064(dvs_base_universe_d2_059_dvs_basefill_064):
    return _base_universe_d3(dvs_base_universe_d2_059_dvs_basefill_064, 59)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_059_dvs_basefill_064'] = {'inputs': ['dvs_base_universe_d2_059_dvs_basefill_064'], 'func': dvs_base_universe_d3_059_dvs_basefill_064}


def dvs_base_universe_d3_060_dvs_basefill_065(dvs_base_universe_d2_060_dvs_basefill_065):
    return _base_universe_d3(dvs_base_universe_d2_060_dvs_basefill_065, 60)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_060_dvs_basefill_065'] = {'inputs': ['dvs_base_universe_d2_060_dvs_basefill_065'], 'func': dvs_base_universe_d3_060_dvs_basefill_065}


def dvs_base_universe_d3_061_dvs_basefill_066(dvs_base_universe_d2_061_dvs_basefill_066):
    return _base_universe_d3(dvs_base_universe_d2_061_dvs_basefill_066, 61)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_061_dvs_basefill_066'] = {'inputs': ['dvs_base_universe_d2_061_dvs_basefill_066'], 'func': dvs_base_universe_d3_061_dvs_basefill_066}


def dvs_base_universe_d3_062_dvs_basefill_067(dvs_base_universe_d2_062_dvs_basefill_067):
    return _base_universe_d3(dvs_base_universe_d2_062_dvs_basefill_067, 62)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_062_dvs_basefill_067'] = {'inputs': ['dvs_base_universe_d2_062_dvs_basefill_067'], 'func': dvs_base_universe_d3_062_dvs_basefill_067}


def dvs_base_universe_d3_063_dvs_basefill_068(dvs_base_universe_d2_063_dvs_basefill_068):
    return _base_universe_d3(dvs_base_universe_d2_063_dvs_basefill_068, 63)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_063_dvs_basefill_068'] = {'inputs': ['dvs_base_universe_d2_063_dvs_basefill_068'], 'func': dvs_base_universe_d3_063_dvs_basefill_068}


def dvs_base_universe_d3_064_dvs_basefill_069(dvs_base_universe_d2_064_dvs_basefill_069):
    return _base_universe_d3(dvs_base_universe_d2_064_dvs_basefill_069, 64)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_064_dvs_basefill_069'] = {'inputs': ['dvs_base_universe_d2_064_dvs_basefill_069'], 'func': dvs_base_universe_d3_064_dvs_basefill_069}


def dvs_base_universe_d3_065_dvs_basefill_070(dvs_base_universe_d2_065_dvs_basefill_070):
    return _base_universe_d3(dvs_base_universe_d2_065_dvs_basefill_070, 65)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_065_dvs_basefill_070'] = {'inputs': ['dvs_base_universe_d2_065_dvs_basefill_070'], 'func': dvs_base_universe_d3_065_dvs_basefill_070}


def dvs_base_universe_d3_066_dvs_basefill_071(dvs_base_universe_d2_066_dvs_basefill_071):
    return _base_universe_d3(dvs_base_universe_d2_066_dvs_basefill_071, 66)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_066_dvs_basefill_071'] = {'inputs': ['dvs_base_universe_d2_066_dvs_basefill_071'], 'func': dvs_base_universe_d3_066_dvs_basefill_071}


def dvs_base_universe_d3_067_dvs_basefill_072(dvs_base_universe_d2_067_dvs_basefill_072):
    return _base_universe_d3(dvs_base_universe_d2_067_dvs_basefill_072, 67)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_067_dvs_basefill_072'] = {'inputs': ['dvs_base_universe_d2_067_dvs_basefill_072'], 'func': dvs_base_universe_d3_067_dvs_basefill_072}


def dvs_base_universe_d3_068_dvs_basefill_073(dvs_base_universe_d2_068_dvs_basefill_073):
    return _base_universe_d3(dvs_base_universe_d2_068_dvs_basefill_073, 68)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_068_dvs_basefill_073'] = {'inputs': ['dvs_base_universe_d2_068_dvs_basefill_073'], 'func': dvs_base_universe_d3_068_dvs_basefill_073}


def dvs_base_universe_d3_069_dvs_basefill_074(dvs_base_universe_d2_069_dvs_basefill_074):
    return _base_universe_d3(dvs_base_universe_d2_069_dvs_basefill_074, 69)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_069_dvs_basefill_074'] = {'inputs': ['dvs_base_universe_d2_069_dvs_basefill_074'], 'func': dvs_base_universe_d3_069_dvs_basefill_074}


def dvs_base_universe_d3_070_dvs_basefill_075(dvs_base_universe_d2_070_dvs_basefill_075):
    return _base_universe_d3(dvs_base_universe_d2_070_dvs_basefill_075, 70)
DVS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dvs_base_universe_d3_070_dvs_basefill_075'] = {'inputs': ['dvs_base_universe_d2_070_dvs_basefill_075'], 'func': dvs_base_universe_d3_070_dvs_basefill_075}
