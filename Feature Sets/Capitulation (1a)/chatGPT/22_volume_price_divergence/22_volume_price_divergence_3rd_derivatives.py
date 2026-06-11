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



def vpd_176_vpd_001_volume_spike_ratio_5_001_accel_1(vpd_151_vpd_001_volume_spike_ratio_5_001_roc_1):
    feature = _s(vpd_151_vpd_001_volume_spike_ratio_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vpd_177_vpd_007_volume_spike_ratio_126_007_accel_5(vpd_152_vpd_007_volume_spike_ratio_126_007_roc_5):
    feature = _s(vpd_152_vpd_007_volume_spike_ratio_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vpd_178_vpd_013_volume_spike_ratio_1008_013_accel_42(vpd_153_vpd_013_volume_spike_ratio_1008_013_roc_42):
    feature = _s(vpd_153_vpd_013_volume_spike_ratio_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vpd_179_vpd_019_volume_spike_ratio_42_019_accel_126(vpd_154_vpd_019_volume_spike_ratio_42_019_roc_126):
    feature = _s(vpd_154_vpd_019_volume_spike_ratio_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vpd_180_vpd_025_volume_spike_ratio_378_025_accel_378(vpd_155_vpd_025_volume_spike_ratio_378_025_roc_378):
    feature = _s(vpd_155_vpd_025_volume_spike_ratio_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VOLUME_PRICE_DIVERGENCE_REGISTRY_3RD_DERIVATIVES = {
    'vpd_176_vpd_001_volume_spike_ratio_5_001_accel_1': {'inputs': ['vpd_151_vpd_001_volume_spike_ratio_5_001_roc_1'], 'func': vpd_176_vpd_001_volume_spike_ratio_5_001_accel_1},
    'vpd_177_vpd_007_volume_spike_ratio_126_007_accel_5': {'inputs': ['vpd_152_vpd_007_volume_spike_ratio_126_007_roc_5'], 'func': vpd_177_vpd_007_volume_spike_ratio_126_007_accel_5},
    'vpd_178_vpd_013_volume_spike_ratio_1008_013_accel_42': {'inputs': ['vpd_153_vpd_013_volume_spike_ratio_1008_013_roc_42'], 'func': vpd_178_vpd_013_volume_spike_ratio_1008_013_accel_42},
    'vpd_179_vpd_019_volume_spike_ratio_42_019_accel_126': {'inputs': ['vpd_154_vpd_019_volume_spike_ratio_42_019_roc_126'], 'func': vpd_179_vpd_019_volume_spike_ratio_42_019_accel_126},
    'vpd_180_vpd_025_volume_spike_ratio_378_025_accel_378': {'inputs': ['vpd_155_vpd_025_volume_spike_ratio_378_025_roc_378'], 'func': vpd_180_vpd_025_volume_spike_ratio_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vpd_replacement_d3_001(vpd_replacement_d2_001):
    feature = _clean(vpd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_001'] = {'inputs': ['vpd_replacement_d2_001'], 'func': vpd_replacement_d3_001}


def vpd_replacement_d3_002(vpd_replacement_d2_002):
    feature = _clean(vpd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_002'] = {'inputs': ['vpd_replacement_d2_002'], 'func': vpd_replacement_d3_002}


def vpd_replacement_d3_003(vpd_replacement_d2_003):
    feature = _clean(vpd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_003'] = {'inputs': ['vpd_replacement_d2_003'], 'func': vpd_replacement_d3_003}


def vpd_replacement_d3_004(vpd_replacement_d2_004):
    feature = _clean(vpd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_004'] = {'inputs': ['vpd_replacement_d2_004'], 'func': vpd_replacement_d3_004}


def vpd_replacement_d3_005(vpd_replacement_d2_005):
    feature = _clean(vpd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_005'] = {'inputs': ['vpd_replacement_d2_005'], 'func': vpd_replacement_d3_005}


def vpd_replacement_d3_006(vpd_replacement_d2_006):
    feature = _clean(vpd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_006'] = {'inputs': ['vpd_replacement_d2_006'], 'func': vpd_replacement_d3_006}


def vpd_replacement_d3_007(vpd_replacement_d2_007):
    feature = _clean(vpd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_007'] = {'inputs': ['vpd_replacement_d2_007'], 'func': vpd_replacement_d3_007}


def vpd_replacement_d3_008(vpd_replacement_d2_008):
    feature = _clean(vpd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_008'] = {'inputs': ['vpd_replacement_d2_008'], 'func': vpd_replacement_d3_008}


def vpd_replacement_d3_009(vpd_replacement_d2_009):
    feature = _clean(vpd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_009'] = {'inputs': ['vpd_replacement_d2_009'], 'func': vpd_replacement_d3_009}


def vpd_replacement_d3_010(vpd_replacement_d2_010):
    feature = _clean(vpd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_010'] = {'inputs': ['vpd_replacement_d2_010'], 'func': vpd_replacement_d3_010}


def vpd_replacement_d3_011(vpd_replacement_d2_011):
    feature = _clean(vpd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_011'] = {'inputs': ['vpd_replacement_d2_011'], 'func': vpd_replacement_d3_011}


def vpd_replacement_d3_012(vpd_replacement_d2_012):
    feature = _clean(vpd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_012'] = {'inputs': ['vpd_replacement_d2_012'], 'func': vpd_replacement_d3_012}


def vpd_replacement_d3_013(vpd_replacement_d2_013):
    feature = _clean(vpd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_013'] = {'inputs': ['vpd_replacement_d2_013'], 'func': vpd_replacement_d3_013}


def vpd_replacement_d3_014(vpd_replacement_d2_014):
    feature = _clean(vpd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_014'] = {'inputs': ['vpd_replacement_d2_014'], 'func': vpd_replacement_d3_014}


def vpd_replacement_d3_015(vpd_replacement_d2_015):
    feature = _clean(vpd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_015'] = {'inputs': ['vpd_replacement_d2_015'], 'func': vpd_replacement_d3_015}


def vpd_replacement_d3_016(vpd_replacement_d2_016):
    feature = _clean(vpd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_016'] = {'inputs': ['vpd_replacement_d2_016'], 'func': vpd_replacement_d3_016}


def vpd_replacement_d3_017(vpd_replacement_d2_017):
    feature = _clean(vpd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_017'] = {'inputs': ['vpd_replacement_d2_017'], 'func': vpd_replacement_d3_017}


def vpd_replacement_d3_018(vpd_replacement_d2_018):
    feature = _clean(vpd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_018'] = {'inputs': ['vpd_replacement_d2_018'], 'func': vpd_replacement_d3_018}


def vpd_replacement_d3_019(vpd_replacement_d2_019):
    feature = _clean(vpd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_019'] = {'inputs': ['vpd_replacement_d2_019'], 'func': vpd_replacement_d3_019}


def vpd_replacement_d3_020(vpd_replacement_d2_020):
    feature = _clean(vpd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_020'] = {'inputs': ['vpd_replacement_d2_020'], 'func': vpd_replacement_d3_020}


def vpd_replacement_d3_021(vpd_replacement_d2_021):
    feature = _clean(vpd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_021'] = {'inputs': ['vpd_replacement_d2_021'], 'func': vpd_replacement_d3_021}


def vpd_replacement_d3_022(vpd_replacement_d2_022):
    feature = _clean(vpd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_022'] = {'inputs': ['vpd_replacement_d2_022'], 'func': vpd_replacement_d3_022}


def vpd_replacement_d3_023(vpd_replacement_d2_023):
    feature = _clean(vpd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_023'] = {'inputs': ['vpd_replacement_d2_023'], 'func': vpd_replacement_d3_023}


def vpd_replacement_d3_024(vpd_replacement_d2_024):
    feature = _clean(vpd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_024'] = {'inputs': ['vpd_replacement_d2_024'], 'func': vpd_replacement_d3_024}


def vpd_replacement_d3_025(vpd_replacement_d2_025):
    feature = _clean(vpd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_025'] = {'inputs': ['vpd_replacement_d2_025'], 'func': vpd_replacement_d3_025}


def vpd_replacement_d3_026(vpd_replacement_d2_026):
    feature = _clean(vpd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_026'] = {'inputs': ['vpd_replacement_d2_026'], 'func': vpd_replacement_d3_026}


def vpd_replacement_d3_027(vpd_replacement_d2_027):
    feature = _clean(vpd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_027'] = {'inputs': ['vpd_replacement_d2_027'], 'func': vpd_replacement_d3_027}


def vpd_replacement_d3_028(vpd_replacement_d2_028):
    feature = _clean(vpd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_028'] = {'inputs': ['vpd_replacement_d2_028'], 'func': vpd_replacement_d3_028}


def vpd_replacement_d3_029(vpd_replacement_d2_029):
    feature = _clean(vpd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_029'] = {'inputs': ['vpd_replacement_d2_029'], 'func': vpd_replacement_d3_029}


def vpd_replacement_d3_030(vpd_replacement_d2_030):
    feature = _clean(vpd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_030'] = {'inputs': ['vpd_replacement_d2_030'], 'func': vpd_replacement_d3_030}


def vpd_replacement_d3_031(vpd_replacement_d2_031):
    feature = _clean(vpd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_031'] = {'inputs': ['vpd_replacement_d2_031'], 'func': vpd_replacement_d3_031}


def vpd_replacement_d3_032(vpd_replacement_d2_032):
    feature = _clean(vpd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_032'] = {'inputs': ['vpd_replacement_d2_032'], 'func': vpd_replacement_d3_032}


def vpd_replacement_d3_033(vpd_replacement_d2_033):
    feature = _clean(vpd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_033'] = {'inputs': ['vpd_replacement_d2_033'], 'func': vpd_replacement_d3_033}


def vpd_replacement_d3_034(vpd_replacement_d2_034):
    feature = _clean(vpd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_034'] = {'inputs': ['vpd_replacement_d2_034'], 'func': vpd_replacement_d3_034}


def vpd_replacement_d3_035(vpd_replacement_d2_035):
    feature = _clean(vpd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_035'] = {'inputs': ['vpd_replacement_d2_035'], 'func': vpd_replacement_d3_035}


def vpd_replacement_d3_036(vpd_replacement_d2_036):
    feature = _clean(vpd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_036'] = {'inputs': ['vpd_replacement_d2_036'], 'func': vpd_replacement_d3_036}


def vpd_replacement_d3_037(vpd_replacement_d2_037):
    feature = _clean(vpd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_037'] = {'inputs': ['vpd_replacement_d2_037'], 'func': vpd_replacement_d3_037}


def vpd_replacement_d3_038(vpd_replacement_d2_038):
    feature = _clean(vpd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_038'] = {'inputs': ['vpd_replacement_d2_038'], 'func': vpd_replacement_d3_038}


def vpd_replacement_d3_039(vpd_replacement_d2_039):
    feature = _clean(vpd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_039'] = {'inputs': ['vpd_replacement_d2_039'], 'func': vpd_replacement_d3_039}


def vpd_replacement_d3_040(vpd_replacement_d2_040):
    feature = _clean(vpd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_040'] = {'inputs': ['vpd_replacement_d2_040'], 'func': vpd_replacement_d3_040}


def vpd_replacement_d3_041(vpd_replacement_d2_041):
    feature = _clean(vpd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_041'] = {'inputs': ['vpd_replacement_d2_041'], 'func': vpd_replacement_d3_041}


def vpd_replacement_d3_042(vpd_replacement_d2_042):
    feature = _clean(vpd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_042'] = {'inputs': ['vpd_replacement_d2_042'], 'func': vpd_replacement_d3_042}


def vpd_replacement_d3_043(vpd_replacement_d2_043):
    feature = _clean(vpd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_043'] = {'inputs': ['vpd_replacement_d2_043'], 'func': vpd_replacement_d3_043}


def vpd_replacement_d3_044(vpd_replacement_d2_044):
    feature = _clean(vpd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_044'] = {'inputs': ['vpd_replacement_d2_044'], 'func': vpd_replacement_d3_044}


def vpd_replacement_d3_045(vpd_replacement_d2_045):
    feature = _clean(vpd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_045'] = {'inputs': ['vpd_replacement_d2_045'], 'func': vpd_replacement_d3_045}


def vpd_replacement_d3_046(vpd_replacement_d2_046):
    feature = _clean(vpd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_046'] = {'inputs': ['vpd_replacement_d2_046'], 'func': vpd_replacement_d3_046}


def vpd_replacement_d3_047(vpd_replacement_d2_047):
    feature = _clean(vpd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_047'] = {'inputs': ['vpd_replacement_d2_047'], 'func': vpd_replacement_d3_047}


def vpd_replacement_d3_048(vpd_replacement_d2_048):
    feature = _clean(vpd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_048'] = {'inputs': ['vpd_replacement_d2_048'], 'func': vpd_replacement_d3_048}


def vpd_replacement_d3_049(vpd_replacement_d2_049):
    feature = _clean(vpd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_049'] = {'inputs': ['vpd_replacement_d2_049'], 'func': vpd_replacement_d3_049}


def vpd_replacement_d3_050(vpd_replacement_d2_050):
    feature = _clean(vpd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_050'] = {'inputs': ['vpd_replacement_d2_050'], 'func': vpd_replacement_d3_050}


def vpd_replacement_d3_051(vpd_replacement_d2_051):
    feature = _clean(vpd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_051'] = {'inputs': ['vpd_replacement_d2_051'], 'func': vpd_replacement_d3_051}


def vpd_replacement_d3_052(vpd_replacement_d2_052):
    feature = _clean(vpd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_052'] = {'inputs': ['vpd_replacement_d2_052'], 'func': vpd_replacement_d3_052}


def vpd_replacement_d3_053(vpd_replacement_d2_053):
    feature = _clean(vpd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_053'] = {'inputs': ['vpd_replacement_d2_053'], 'func': vpd_replacement_d3_053}


def vpd_replacement_d3_054(vpd_replacement_d2_054):
    feature = _clean(vpd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_054'] = {'inputs': ['vpd_replacement_d2_054'], 'func': vpd_replacement_d3_054}


def vpd_replacement_d3_055(vpd_replacement_d2_055):
    feature = _clean(vpd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_055'] = {'inputs': ['vpd_replacement_d2_055'], 'func': vpd_replacement_d3_055}


def vpd_replacement_d3_056(vpd_replacement_d2_056):
    feature = _clean(vpd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_056'] = {'inputs': ['vpd_replacement_d2_056'], 'func': vpd_replacement_d3_056}


def vpd_replacement_d3_057(vpd_replacement_d2_057):
    feature = _clean(vpd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_057'] = {'inputs': ['vpd_replacement_d2_057'], 'func': vpd_replacement_d3_057}


def vpd_replacement_d3_058(vpd_replacement_d2_058):
    feature = _clean(vpd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_058'] = {'inputs': ['vpd_replacement_d2_058'], 'func': vpd_replacement_d3_058}


def vpd_replacement_d3_059(vpd_replacement_d2_059):
    feature = _clean(vpd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_059'] = {'inputs': ['vpd_replacement_d2_059'], 'func': vpd_replacement_d3_059}


def vpd_replacement_d3_060(vpd_replacement_d2_060):
    feature = _clean(vpd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_060'] = {'inputs': ['vpd_replacement_d2_060'], 'func': vpd_replacement_d3_060}


def vpd_replacement_d3_061(vpd_replacement_d2_061):
    feature = _clean(vpd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_061'] = {'inputs': ['vpd_replacement_d2_061'], 'func': vpd_replacement_d3_061}


def vpd_replacement_d3_062(vpd_replacement_d2_062):
    feature = _clean(vpd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_062'] = {'inputs': ['vpd_replacement_d2_062'], 'func': vpd_replacement_d3_062}


def vpd_replacement_d3_063(vpd_replacement_d2_063):
    feature = _clean(vpd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_063'] = {'inputs': ['vpd_replacement_d2_063'], 'func': vpd_replacement_d3_063}


def vpd_replacement_d3_064(vpd_replacement_d2_064):
    feature = _clean(vpd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_064'] = {'inputs': ['vpd_replacement_d2_064'], 'func': vpd_replacement_d3_064}


def vpd_replacement_d3_065(vpd_replacement_d2_065):
    feature = _clean(vpd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_065'] = {'inputs': ['vpd_replacement_d2_065'], 'func': vpd_replacement_d3_065}


def vpd_replacement_d3_066(vpd_replacement_d2_066):
    feature = _clean(vpd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_066'] = {'inputs': ['vpd_replacement_d2_066'], 'func': vpd_replacement_d3_066}


def vpd_replacement_d3_067(vpd_replacement_d2_067):
    feature = _clean(vpd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_067'] = {'inputs': ['vpd_replacement_d2_067'], 'func': vpd_replacement_d3_067}


def vpd_replacement_d3_068(vpd_replacement_d2_068):
    feature = _clean(vpd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_068'] = {'inputs': ['vpd_replacement_d2_068'], 'func': vpd_replacement_d3_068}


def vpd_replacement_d3_069(vpd_replacement_d2_069):
    feature = _clean(vpd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_069'] = {'inputs': ['vpd_replacement_d2_069'], 'func': vpd_replacement_d3_069}


def vpd_replacement_d3_070(vpd_replacement_d2_070):
    feature = _clean(vpd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_070'] = {'inputs': ['vpd_replacement_d2_070'], 'func': vpd_replacement_d3_070}


def vpd_replacement_d3_071(vpd_replacement_d2_071):
    feature = _clean(vpd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_071'] = {'inputs': ['vpd_replacement_d2_071'], 'func': vpd_replacement_d3_071}


def vpd_replacement_d3_072(vpd_replacement_d2_072):
    feature = _clean(vpd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_072'] = {'inputs': ['vpd_replacement_d2_072'], 'func': vpd_replacement_d3_072}


def vpd_replacement_d3_073(vpd_replacement_d2_073):
    feature = _clean(vpd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_073'] = {'inputs': ['vpd_replacement_d2_073'], 'func': vpd_replacement_d3_073}


def vpd_replacement_d3_074(vpd_replacement_d2_074):
    feature = _clean(vpd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_074'] = {'inputs': ['vpd_replacement_d2_074'], 'func': vpd_replacement_d3_074}


def vpd_replacement_d3_075(vpd_replacement_d2_075):
    feature = _clean(vpd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_075'] = {'inputs': ['vpd_replacement_d2_075'], 'func': vpd_replacement_d3_075}


def vpd_replacement_d3_076(vpd_replacement_d2_076):
    feature = _clean(vpd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_076'] = {'inputs': ['vpd_replacement_d2_076'], 'func': vpd_replacement_d3_076}


def vpd_replacement_d3_077(vpd_replacement_d2_077):
    feature = _clean(vpd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_077'] = {'inputs': ['vpd_replacement_d2_077'], 'func': vpd_replacement_d3_077}


def vpd_replacement_d3_078(vpd_replacement_d2_078):
    feature = _clean(vpd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_078'] = {'inputs': ['vpd_replacement_d2_078'], 'func': vpd_replacement_d3_078}


def vpd_replacement_d3_079(vpd_replacement_d2_079):
    feature = _clean(vpd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_079'] = {'inputs': ['vpd_replacement_d2_079'], 'func': vpd_replacement_d3_079}


def vpd_replacement_d3_080(vpd_replacement_d2_080):
    feature = _clean(vpd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_080'] = {'inputs': ['vpd_replacement_d2_080'], 'func': vpd_replacement_d3_080}


def vpd_replacement_d3_081(vpd_replacement_d2_081):
    feature = _clean(vpd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_081'] = {'inputs': ['vpd_replacement_d2_081'], 'func': vpd_replacement_d3_081}


def vpd_replacement_d3_082(vpd_replacement_d2_082):
    feature = _clean(vpd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_082'] = {'inputs': ['vpd_replacement_d2_082'], 'func': vpd_replacement_d3_082}


def vpd_replacement_d3_083(vpd_replacement_d2_083):
    feature = _clean(vpd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_083'] = {'inputs': ['vpd_replacement_d2_083'], 'func': vpd_replacement_d3_083}


def vpd_replacement_d3_084(vpd_replacement_d2_084):
    feature = _clean(vpd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_084'] = {'inputs': ['vpd_replacement_d2_084'], 'func': vpd_replacement_d3_084}


def vpd_replacement_d3_085(vpd_replacement_d2_085):
    feature = _clean(vpd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_085'] = {'inputs': ['vpd_replacement_d2_085'], 'func': vpd_replacement_d3_085}


def vpd_replacement_d3_086(vpd_replacement_d2_086):
    feature = _clean(vpd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_086'] = {'inputs': ['vpd_replacement_d2_086'], 'func': vpd_replacement_d3_086}


def vpd_replacement_d3_087(vpd_replacement_d2_087):
    feature = _clean(vpd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_087'] = {'inputs': ['vpd_replacement_d2_087'], 'func': vpd_replacement_d3_087}


def vpd_replacement_d3_088(vpd_replacement_d2_088):
    feature = _clean(vpd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_088'] = {'inputs': ['vpd_replacement_d2_088'], 'func': vpd_replacement_d3_088}


def vpd_replacement_d3_089(vpd_replacement_d2_089):
    feature = _clean(vpd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_089'] = {'inputs': ['vpd_replacement_d2_089'], 'func': vpd_replacement_d3_089}


def vpd_replacement_d3_090(vpd_replacement_d2_090):
    feature = _clean(vpd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_090'] = {'inputs': ['vpd_replacement_d2_090'], 'func': vpd_replacement_d3_090}


def vpd_replacement_d3_091(vpd_replacement_d2_091):
    feature = _clean(vpd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_091'] = {'inputs': ['vpd_replacement_d2_091'], 'func': vpd_replacement_d3_091}


def vpd_replacement_d3_092(vpd_replacement_d2_092):
    feature = _clean(vpd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_092'] = {'inputs': ['vpd_replacement_d2_092'], 'func': vpd_replacement_d3_092}


def vpd_replacement_d3_093(vpd_replacement_d2_093):
    feature = _clean(vpd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_093'] = {'inputs': ['vpd_replacement_d2_093'], 'func': vpd_replacement_d3_093}


def vpd_replacement_d3_094(vpd_replacement_d2_094):
    feature = _clean(vpd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_094'] = {'inputs': ['vpd_replacement_d2_094'], 'func': vpd_replacement_d3_094}


def vpd_replacement_d3_095(vpd_replacement_d2_095):
    feature = _clean(vpd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_095'] = {'inputs': ['vpd_replacement_d2_095'], 'func': vpd_replacement_d3_095}


def vpd_replacement_d3_096(vpd_replacement_d2_096):
    feature = _clean(vpd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_096'] = {'inputs': ['vpd_replacement_d2_096'], 'func': vpd_replacement_d3_096}


def vpd_replacement_d3_097(vpd_replacement_d2_097):
    feature = _clean(vpd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_097'] = {'inputs': ['vpd_replacement_d2_097'], 'func': vpd_replacement_d3_097}


def vpd_replacement_d3_098(vpd_replacement_d2_098):
    feature = _clean(vpd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_098'] = {'inputs': ['vpd_replacement_d2_098'], 'func': vpd_replacement_d3_098}


def vpd_replacement_d3_099(vpd_replacement_d2_099):
    feature = _clean(vpd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_099'] = {'inputs': ['vpd_replacement_d2_099'], 'func': vpd_replacement_d3_099}


def vpd_replacement_d3_100(vpd_replacement_d2_100):
    feature = _clean(vpd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_100'] = {'inputs': ['vpd_replacement_d2_100'], 'func': vpd_replacement_d3_100}


def vpd_replacement_d3_101(vpd_replacement_d2_101):
    feature = _clean(vpd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_101'] = {'inputs': ['vpd_replacement_d2_101'], 'func': vpd_replacement_d3_101}


def vpd_replacement_d3_102(vpd_replacement_d2_102):
    feature = _clean(vpd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_102'] = {'inputs': ['vpd_replacement_d2_102'], 'func': vpd_replacement_d3_102}


def vpd_replacement_d3_103(vpd_replacement_d2_103):
    feature = _clean(vpd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_103'] = {'inputs': ['vpd_replacement_d2_103'], 'func': vpd_replacement_d3_103}


def vpd_replacement_d3_104(vpd_replacement_d2_104):
    feature = _clean(vpd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_104'] = {'inputs': ['vpd_replacement_d2_104'], 'func': vpd_replacement_d3_104}


def vpd_replacement_d3_105(vpd_replacement_d2_105):
    feature = _clean(vpd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_105'] = {'inputs': ['vpd_replacement_d2_105'], 'func': vpd_replacement_d3_105}


def vpd_replacement_d3_106(vpd_replacement_d2_106):
    feature = _clean(vpd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_106'] = {'inputs': ['vpd_replacement_d2_106'], 'func': vpd_replacement_d3_106}


def vpd_replacement_d3_107(vpd_replacement_d2_107):
    feature = _clean(vpd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_107'] = {'inputs': ['vpd_replacement_d2_107'], 'func': vpd_replacement_d3_107}


def vpd_replacement_d3_108(vpd_replacement_d2_108):
    feature = _clean(vpd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_108'] = {'inputs': ['vpd_replacement_d2_108'], 'func': vpd_replacement_d3_108}


def vpd_replacement_d3_109(vpd_replacement_d2_109):
    feature = _clean(vpd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_109'] = {'inputs': ['vpd_replacement_d2_109'], 'func': vpd_replacement_d3_109}


def vpd_replacement_d3_110(vpd_replacement_d2_110):
    feature = _clean(vpd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_110'] = {'inputs': ['vpd_replacement_d2_110'], 'func': vpd_replacement_d3_110}


def vpd_replacement_d3_111(vpd_replacement_d2_111):
    feature = _clean(vpd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_111'] = {'inputs': ['vpd_replacement_d2_111'], 'func': vpd_replacement_d3_111}


def vpd_replacement_d3_112(vpd_replacement_d2_112):
    feature = _clean(vpd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_112'] = {'inputs': ['vpd_replacement_d2_112'], 'func': vpd_replacement_d3_112}


def vpd_replacement_d3_113(vpd_replacement_d2_113):
    feature = _clean(vpd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_113'] = {'inputs': ['vpd_replacement_d2_113'], 'func': vpd_replacement_d3_113}


def vpd_replacement_d3_114(vpd_replacement_d2_114):
    feature = _clean(vpd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_114'] = {'inputs': ['vpd_replacement_d2_114'], 'func': vpd_replacement_d3_114}


def vpd_replacement_d3_115(vpd_replacement_d2_115):
    feature = _clean(vpd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_115'] = {'inputs': ['vpd_replacement_d2_115'], 'func': vpd_replacement_d3_115}


def vpd_replacement_d3_116(vpd_replacement_d2_116):
    feature = _clean(vpd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_116'] = {'inputs': ['vpd_replacement_d2_116'], 'func': vpd_replacement_d3_116}


def vpd_replacement_d3_117(vpd_replacement_d2_117):
    feature = _clean(vpd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_117'] = {'inputs': ['vpd_replacement_d2_117'], 'func': vpd_replacement_d3_117}


def vpd_replacement_d3_118(vpd_replacement_d2_118):
    feature = _clean(vpd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_118'] = {'inputs': ['vpd_replacement_d2_118'], 'func': vpd_replacement_d3_118}


def vpd_replacement_d3_119(vpd_replacement_d2_119):
    feature = _clean(vpd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_119'] = {'inputs': ['vpd_replacement_d2_119'], 'func': vpd_replacement_d3_119}


def vpd_replacement_d3_120(vpd_replacement_d2_120):
    feature = _clean(vpd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_120'] = {'inputs': ['vpd_replacement_d2_120'], 'func': vpd_replacement_d3_120}


def vpd_replacement_d3_121(vpd_replacement_d2_121):
    feature = _clean(vpd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_121'] = {'inputs': ['vpd_replacement_d2_121'], 'func': vpd_replacement_d3_121}


def vpd_replacement_d3_122(vpd_replacement_d2_122):
    feature = _clean(vpd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_122'] = {'inputs': ['vpd_replacement_d2_122'], 'func': vpd_replacement_d3_122}


def vpd_replacement_d3_123(vpd_replacement_d2_123):
    feature = _clean(vpd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_123'] = {'inputs': ['vpd_replacement_d2_123'], 'func': vpd_replacement_d3_123}


def vpd_replacement_d3_124(vpd_replacement_d2_124):
    feature = _clean(vpd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_124'] = {'inputs': ['vpd_replacement_d2_124'], 'func': vpd_replacement_d3_124}


def vpd_replacement_d3_125(vpd_replacement_d2_125):
    feature = _clean(vpd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_125'] = {'inputs': ['vpd_replacement_d2_125'], 'func': vpd_replacement_d3_125}


def vpd_replacement_d3_126(vpd_replacement_d2_126):
    feature = _clean(vpd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_126'] = {'inputs': ['vpd_replacement_d2_126'], 'func': vpd_replacement_d3_126}


def vpd_replacement_d3_127(vpd_replacement_d2_127):
    feature = _clean(vpd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_127'] = {'inputs': ['vpd_replacement_d2_127'], 'func': vpd_replacement_d3_127}


def vpd_replacement_d3_128(vpd_replacement_d2_128):
    feature = _clean(vpd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_128'] = {'inputs': ['vpd_replacement_d2_128'], 'func': vpd_replacement_d3_128}


def vpd_replacement_d3_129(vpd_replacement_d2_129):
    feature = _clean(vpd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_129'] = {'inputs': ['vpd_replacement_d2_129'], 'func': vpd_replacement_d3_129}


def vpd_replacement_d3_130(vpd_replacement_d2_130):
    feature = _clean(vpd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_130'] = {'inputs': ['vpd_replacement_d2_130'], 'func': vpd_replacement_d3_130}


def vpd_replacement_d3_131(vpd_replacement_d2_131):
    feature = _clean(vpd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_131'] = {'inputs': ['vpd_replacement_d2_131'], 'func': vpd_replacement_d3_131}


def vpd_replacement_d3_132(vpd_replacement_d2_132):
    feature = _clean(vpd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_132'] = {'inputs': ['vpd_replacement_d2_132'], 'func': vpd_replacement_d3_132}


def vpd_replacement_d3_133(vpd_replacement_d2_133):
    feature = _clean(vpd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_133'] = {'inputs': ['vpd_replacement_d2_133'], 'func': vpd_replacement_d3_133}


def vpd_replacement_d3_134(vpd_replacement_d2_134):
    feature = _clean(vpd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_134'] = {'inputs': ['vpd_replacement_d2_134'], 'func': vpd_replacement_d3_134}


def vpd_replacement_d3_135(vpd_replacement_d2_135):
    feature = _clean(vpd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_135'] = {'inputs': ['vpd_replacement_d2_135'], 'func': vpd_replacement_d3_135}


def vpd_replacement_d3_136(vpd_replacement_d2_136):
    feature = _clean(vpd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_136'] = {'inputs': ['vpd_replacement_d2_136'], 'func': vpd_replacement_d3_136}


def vpd_replacement_d3_137(vpd_replacement_d2_137):
    feature = _clean(vpd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_137'] = {'inputs': ['vpd_replacement_d2_137'], 'func': vpd_replacement_d3_137}


def vpd_replacement_d3_138(vpd_replacement_d2_138):
    feature = _clean(vpd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_138'] = {'inputs': ['vpd_replacement_d2_138'], 'func': vpd_replacement_d3_138}


def vpd_replacement_d3_139(vpd_replacement_d2_139):
    feature = _clean(vpd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_139'] = {'inputs': ['vpd_replacement_d2_139'], 'func': vpd_replacement_d3_139}


def vpd_replacement_d3_140(vpd_replacement_d2_140):
    feature = _clean(vpd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_140'] = {'inputs': ['vpd_replacement_d2_140'], 'func': vpd_replacement_d3_140}


def vpd_replacement_d3_141(vpd_replacement_d2_141):
    feature = _clean(vpd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_141'] = {'inputs': ['vpd_replacement_d2_141'], 'func': vpd_replacement_d3_141}


def vpd_replacement_d3_142(vpd_replacement_d2_142):
    feature = _clean(vpd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_142'] = {'inputs': ['vpd_replacement_d2_142'], 'func': vpd_replacement_d3_142}


def vpd_replacement_d3_143(vpd_replacement_d2_143):
    feature = _clean(vpd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_143'] = {'inputs': ['vpd_replacement_d2_143'], 'func': vpd_replacement_d3_143}


def vpd_replacement_d3_144(vpd_replacement_d2_144):
    feature = _clean(vpd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_144'] = {'inputs': ['vpd_replacement_d2_144'], 'func': vpd_replacement_d3_144}


def vpd_replacement_d3_145(vpd_replacement_d2_145):
    feature = _clean(vpd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_145'] = {'inputs': ['vpd_replacement_d2_145'], 'func': vpd_replacement_d3_145}


def vpd_replacement_d3_146(vpd_replacement_d2_146):
    feature = _clean(vpd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_146'] = {'inputs': ['vpd_replacement_d2_146'], 'func': vpd_replacement_d3_146}


def vpd_replacement_d3_147(vpd_replacement_d2_147):
    feature = _clean(vpd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_147'] = {'inputs': ['vpd_replacement_d2_147'], 'func': vpd_replacement_d3_147}


def vpd_replacement_d3_148(vpd_replacement_d2_148):
    feature = _clean(vpd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_148'] = {'inputs': ['vpd_replacement_d2_148'], 'func': vpd_replacement_d3_148}


def vpd_replacement_d3_149(vpd_replacement_d2_149):
    feature = _clean(vpd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_149'] = {'inputs': ['vpd_replacement_d2_149'], 'func': vpd_replacement_d3_149}


def vpd_replacement_d3_150(vpd_replacement_d2_150):
    feature = _clean(vpd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_150'] = {'inputs': ['vpd_replacement_d2_150'], 'func': vpd_replacement_d3_150}


def vpd_replacement_d3_151(vpd_replacement_d2_151):
    feature = _clean(vpd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_151'] = {'inputs': ['vpd_replacement_d2_151'], 'func': vpd_replacement_d3_151}


def vpd_replacement_d3_152(vpd_replacement_d2_152):
    feature = _clean(vpd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_152'] = {'inputs': ['vpd_replacement_d2_152'], 'func': vpd_replacement_d3_152}


def vpd_replacement_d3_153(vpd_replacement_d2_153):
    feature = _clean(vpd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_153'] = {'inputs': ['vpd_replacement_d2_153'], 'func': vpd_replacement_d3_153}


def vpd_replacement_d3_154(vpd_replacement_d2_154):
    feature = _clean(vpd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_154'] = {'inputs': ['vpd_replacement_d2_154'], 'func': vpd_replacement_d3_154}


def vpd_replacement_d3_155(vpd_replacement_d2_155):
    feature = _clean(vpd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_155'] = {'inputs': ['vpd_replacement_d2_155'], 'func': vpd_replacement_d3_155}


def vpd_replacement_d3_156(vpd_replacement_d2_156):
    feature = _clean(vpd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_156'] = {'inputs': ['vpd_replacement_d2_156'], 'func': vpd_replacement_d3_156}


def vpd_replacement_d3_157(vpd_replacement_d2_157):
    feature = _clean(vpd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_157'] = {'inputs': ['vpd_replacement_d2_157'], 'func': vpd_replacement_d3_157}


def vpd_replacement_d3_158(vpd_replacement_d2_158):
    feature = _clean(vpd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_158'] = {'inputs': ['vpd_replacement_d2_158'], 'func': vpd_replacement_d3_158}


def vpd_replacement_d3_159(vpd_replacement_d2_159):
    feature = _clean(vpd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_159'] = {'inputs': ['vpd_replacement_d2_159'], 'func': vpd_replacement_d3_159}


def vpd_replacement_d3_160(vpd_replacement_d2_160):
    feature = _clean(vpd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VPD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vpd_replacement_d3_160'] = {'inputs': ['vpd_replacement_d2_160'], 'func': vpd_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vpd_base_universe_d3_001_vpd_002_volume_zscore_10_002(vpd_base_universe_d2_001_vpd_002_volume_zscore_10_002):
    return _base_universe_d3(vpd_base_universe_d2_001_vpd_002_volume_zscore_10_002, 1)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_001_vpd_002_volume_zscore_10_002'] = {'inputs': ['vpd_base_universe_d2_001_vpd_002_volume_zscore_10_002'], 'func': vpd_base_universe_d3_001_vpd_002_volume_zscore_10_002}


def vpd_base_universe_d3_002_vpd_003_down_volume_share_21_003(vpd_base_universe_d2_002_vpd_003_down_volume_share_21_003):
    return _base_universe_d3(vpd_base_universe_d2_002_vpd_003_down_volume_share_21_003, 2)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_002_vpd_003_down_volume_share_21_003'] = {'inputs': ['vpd_base_universe_d2_002_vpd_003_down_volume_share_21_003'], 'func': vpd_base_universe_d3_002_vpd_003_down_volume_share_21_003}


def vpd_base_universe_d3_003_vpd_004_dollar_volume_shock_42_004(vpd_base_universe_d2_003_vpd_004_dollar_volume_shock_42_004):
    return _base_universe_d3(vpd_base_universe_d2_003_vpd_004_dollar_volume_shock_42_004, 3)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_003_vpd_004_dollar_volume_shock_42_004'] = {'inputs': ['vpd_base_universe_d2_003_vpd_004_dollar_volume_shock_42_004'], 'func': vpd_base_universe_d3_003_vpd_004_dollar_volume_shock_42_004}


def vpd_base_universe_d3_004_vpd_005_volume_trend_slope_63_005(vpd_base_universe_d2_004_vpd_005_volume_trend_slope_63_005):
    return _base_universe_d3(vpd_base_universe_d2_004_vpd_005_volume_trend_slope_63_005, 4)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_004_vpd_005_volume_trend_slope_63_005'] = {'inputs': ['vpd_base_universe_d2_004_vpd_005_volume_trend_slope_63_005'], 'func': vpd_base_universe_d3_004_vpd_005_volume_trend_slope_63_005}


def vpd_base_universe_d3_005_vpd_006_price_volume_divergence_84_006(vpd_base_universe_d2_005_vpd_006_price_volume_divergence_84_006):
    return _base_universe_d3(vpd_base_universe_d2_005_vpd_006_price_volume_divergence_84_006, 5)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_005_vpd_006_price_volume_divergence_84_006'] = {'inputs': ['vpd_base_universe_d2_005_vpd_006_price_volume_divergence_84_006'], 'func': vpd_base_universe_d3_005_vpd_006_price_volume_divergence_84_006}


def vpd_base_universe_d3_006_vpd_008_volume_zscore_189_008(vpd_base_universe_d2_006_vpd_008_volume_zscore_189_008):
    return _base_universe_d3(vpd_base_universe_d2_006_vpd_008_volume_zscore_189_008, 6)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_006_vpd_008_volume_zscore_189_008'] = {'inputs': ['vpd_base_universe_d2_006_vpd_008_volume_zscore_189_008'], 'func': vpd_base_universe_d3_006_vpd_008_volume_zscore_189_008}


def vpd_base_universe_d3_007_vpd_009_down_volume_share_252_009(vpd_base_universe_d2_007_vpd_009_down_volume_share_252_009):
    return _base_universe_d3(vpd_base_universe_d2_007_vpd_009_down_volume_share_252_009, 7)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_007_vpd_009_down_volume_share_252_009'] = {'inputs': ['vpd_base_universe_d2_007_vpd_009_down_volume_share_252_009'], 'func': vpd_base_universe_d3_007_vpd_009_down_volume_share_252_009}


def vpd_base_universe_d3_008_vpd_010_dollar_volume_shock_378_010(vpd_base_universe_d2_008_vpd_010_dollar_volume_shock_378_010):
    return _base_universe_d3(vpd_base_universe_d2_008_vpd_010_dollar_volume_shock_378_010, 8)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_008_vpd_010_dollar_volume_shock_378_010'] = {'inputs': ['vpd_base_universe_d2_008_vpd_010_dollar_volume_shock_378_010'], 'func': vpd_base_universe_d3_008_vpd_010_dollar_volume_shock_378_010}


def vpd_base_universe_d3_009_vpd_011_volume_trend_slope_504_011(vpd_base_universe_d2_009_vpd_011_volume_trend_slope_504_011):
    return _base_universe_d3(vpd_base_universe_d2_009_vpd_011_volume_trend_slope_504_011, 9)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_009_vpd_011_volume_trend_slope_504_011'] = {'inputs': ['vpd_base_universe_d2_009_vpd_011_volume_trend_slope_504_011'], 'func': vpd_base_universe_d3_009_vpd_011_volume_trend_slope_504_011}


def vpd_base_universe_d3_010_vpd_012_price_volume_divergence_756_012(vpd_base_universe_d2_010_vpd_012_price_volume_divergence_756_012):
    return _base_universe_d3(vpd_base_universe_d2_010_vpd_012_price_volume_divergence_756_012, 10)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_010_vpd_012_price_volume_divergence_756_012'] = {'inputs': ['vpd_base_universe_d2_010_vpd_012_price_volume_divergence_756_012'], 'func': vpd_base_universe_d3_010_vpd_012_price_volume_divergence_756_012}


def vpd_base_universe_d3_011_vpd_014_volume_zscore_1260_014(vpd_base_universe_d2_011_vpd_014_volume_zscore_1260_014):
    return _base_universe_d3(vpd_base_universe_d2_011_vpd_014_volume_zscore_1260_014, 11)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_011_vpd_014_volume_zscore_1260_014'] = {'inputs': ['vpd_base_universe_d2_011_vpd_014_volume_zscore_1260_014'], 'func': vpd_base_universe_d3_011_vpd_014_volume_zscore_1260_014}


def vpd_base_universe_d3_012_vpd_015_down_volume_share_1512_015(vpd_base_universe_d2_012_vpd_015_down_volume_share_1512_015):
    return _base_universe_d3(vpd_base_universe_d2_012_vpd_015_down_volume_share_1512_015, 12)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_012_vpd_015_down_volume_share_1512_015'] = {'inputs': ['vpd_base_universe_d2_012_vpd_015_down_volume_share_1512_015'], 'func': vpd_base_universe_d3_012_vpd_015_down_volume_share_1512_015}


def vpd_base_universe_d3_013_vpd_016_dollar_volume_shock_5_016(vpd_base_universe_d2_013_vpd_016_dollar_volume_shock_5_016):
    return _base_universe_d3(vpd_base_universe_d2_013_vpd_016_dollar_volume_shock_5_016, 13)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_013_vpd_016_dollar_volume_shock_5_016'] = {'inputs': ['vpd_base_universe_d2_013_vpd_016_dollar_volume_shock_5_016'], 'func': vpd_base_universe_d3_013_vpd_016_dollar_volume_shock_5_016}


def vpd_base_universe_d3_014_vpd_017_volume_trend_slope_10_017(vpd_base_universe_d2_014_vpd_017_volume_trend_slope_10_017):
    return _base_universe_d3(vpd_base_universe_d2_014_vpd_017_volume_trend_slope_10_017, 14)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_014_vpd_017_volume_trend_slope_10_017'] = {'inputs': ['vpd_base_universe_d2_014_vpd_017_volume_trend_slope_10_017'], 'func': vpd_base_universe_d3_014_vpd_017_volume_trend_slope_10_017}


def vpd_base_universe_d3_015_vpd_018_price_volume_divergence_21_018(vpd_base_universe_d2_015_vpd_018_price_volume_divergence_21_018):
    return _base_universe_d3(vpd_base_universe_d2_015_vpd_018_price_volume_divergence_21_018, 15)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_015_vpd_018_price_volume_divergence_21_018'] = {'inputs': ['vpd_base_universe_d2_015_vpd_018_price_volume_divergence_21_018'], 'func': vpd_base_universe_d3_015_vpd_018_price_volume_divergence_21_018}


def vpd_base_universe_d3_016_vpd_020_volume_zscore_63_020(vpd_base_universe_d2_016_vpd_020_volume_zscore_63_020):
    return _base_universe_d3(vpd_base_universe_d2_016_vpd_020_volume_zscore_63_020, 16)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_016_vpd_020_volume_zscore_63_020'] = {'inputs': ['vpd_base_universe_d2_016_vpd_020_volume_zscore_63_020'], 'func': vpd_base_universe_d3_016_vpd_020_volume_zscore_63_020}


def vpd_base_universe_d3_017_vpd_021_down_volume_share_84_021(vpd_base_universe_d2_017_vpd_021_down_volume_share_84_021):
    return _base_universe_d3(vpd_base_universe_d2_017_vpd_021_down_volume_share_84_021, 17)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_017_vpd_021_down_volume_share_84_021'] = {'inputs': ['vpd_base_universe_d2_017_vpd_021_down_volume_share_84_021'], 'func': vpd_base_universe_d3_017_vpd_021_down_volume_share_84_021}


def vpd_base_universe_d3_018_vpd_022_dollar_volume_shock_126_022(vpd_base_universe_d2_018_vpd_022_dollar_volume_shock_126_022):
    return _base_universe_d3(vpd_base_universe_d2_018_vpd_022_dollar_volume_shock_126_022, 18)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_018_vpd_022_dollar_volume_shock_126_022'] = {'inputs': ['vpd_base_universe_d2_018_vpd_022_dollar_volume_shock_126_022'], 'func': vpd_base_universe_d3_018_vpd_022_dollar_volume_shock_126_022}


def vpd_base_universe_d3_019_vpd_023_volume_trend_slope_189_023(vpd_base_universe_d2_019_vpd_023_volume_trend_slope_189_023):
    return _base_universe_d3(vpd_base_universe_d2_019_vpd_023_volume_trend_slope_189_023, 19)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_019_vpd_023_volume_trend_slope_189_023'] = {'inputs': ['vpd_base_universe_d2_019_vpd_023_volume_trend_slope_189_023'], 'func': vpd_base_universe_d3_019_vpd_023_volume_trend_slope_189_023}


def vpd_base_universe_d3_020_vpd_024_price_volume_divergence_252_024(vpd_base_universe_d2_020_vpd_024_price_volume_divergence_252_024):
    return _base_universe_d3(vpd_base_universe_d2_020_vpd_024_price_volume_divergence_252_024, 20)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_020_vpd_024_price_volume_divergence_252_024'] = {'inputs': ['vpd_base_universe_d2_020_vpd_024_price_volume_divergence_252_024'], 'func': vpd_base_universe_d3_020_vpd_024_price_volume_divergence_252_024}


def vpd_base_universe_d3_021_vpd_026_volume_zscore_504_026(vpd_base_universe_d2_021_vpd_026_volume_zscore_504_026):
    return _base_universe_d3(vpd_base_universe_d2_021_vpd_026_volume_zscore_504_026, 21)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_021_vpd_026_volume_zscore_504_026'] = {'inputs': ['vpd_base_universe_d2_021_vpd_026_volume_zscore_504_026'], 'func': vpd_base_universe_d3_021_vpd_026_volume_zscore_504_026}


def vpd_base_universe_d3_022_vpd_027_down_volume_share_756_027(vpd_base_universe_d2_022_vpd_027_down_volume_share_756_027):
    return _base_universe_d3(vpd_base_universe_d2_022_vpd_027_down_volume_share_756_027, 22)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_022_vpd_027_down_volume_share_756_027'] = {'inputs': ['vpd_base_universe_d2_022_vpd_027_down_volume_share_756_027'], 'func': vpd_base_universe_d3_022_vpd_027_down_volume_share_756_027}


def vpd_base_universe_d3_023_vpd_028_dollar_volume_shock_1008_028(vpd_base_universe_d2_023_vpd_028_dollar_volume_shock_1008_028):
    return _base_universe_d3(vpd_base_universe_d2_023_vpd_028_dollar_volume_shock_1008_028, 23)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_023_vpd_028_dollar_volume_shock_1008_028'] = {'inputs': ['vpd_base_universe_d2_023_vpd_028_dollar_volume_shock_1008_028'], 'func': vpd_base_universe_d3_023_vpd_028_dollar_volume_shock_1008_028}


def vpd_base_universe_d3_024_vpd_029_volume_trend_slope_1260_029(vpd_base_universe_d2_024_vpd_029_volume_trend_slope_1260_029):
    return _base_universe_d3(vpd_base_universe_d2_024_vpd_029_volume_trend_slope_1260_029, 24)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_024_vpd_029_volume_trend_slope_1260_029'] = {'inputs': ['vpd_base_universe_d2_024_vpd_029_volume_trend_slope_1260_029'], 'func': vpd_base_universe_d3_024_vpd_029_volume_trend_slope_1260_029}


def vpd_base_universe_d3_025_vpd_030_price_volume_divergence_1512_030(vpd_base_universe_d2_025_vpd_030_price_volume_divergence_1512_030):
    return _base_universe_d3(vpd_base_universe_d2_025_vpd_030_price_volume_divergence_1512_030, 25)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_025_vpd_030_price_volume_divergence_1512_030'] = {'inputs': ['vpd_base_universe_d2_025_vpd_030_price_volume_divergence_1512_030'], 'func': vpd_base_universe_d3_025_vpd_030_price_volume_divergence_1512_030}


def vpd_base_universe_d3_026_vpd_basefill_031(vpd_base_universe_d2_026_vpd_basefill_031):
    return _base_universe_d3(vpd_base_universe_d2_026_vpd_basefill_031, 26)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_026_vpd_basefill_031'] = {'inputs': ['vpd_base_universe_d2_026_vpd_basefill_031'], 'func': vpd_base_universe_d3_026_vpd_basefill_031}


def vpd_base_universe_d3_027_vpd_basefill_032(vpd_base_universe_d2_027_vpd_basefill_032):
    return _base_universe_d3(vpd_base_universe_d2_027_vpd_basefill_032, 27)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_027_vpd_basefill_032'] = {'inputs': ['vpd_base_universe_d2_027_vpd_basefill_032'], 'func': vpd_base_universe_d3_027_vpd_basefill_032}


def vpd_base_universe_d3_028_vpd_basefill_033(vpd_base_universe_d2_028_vpd_basefill_033):
    return _base_universe_d3(vpd_base_universe_d2_028_vpd_basefill_033, 28)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_028_vpd_basefill_033'] = {'inputs': ['vpd_base_universe_d2_028_vpd_basefill_033'], 'func': vpd_base_universe_d3_028_vpd_basefill_033}


def vpd_base_universe_d3_029_vpd_basefill_034(vpd_base_universe_d2_029_vpd_basefill_034):
    return _base_universe_d3(vpd_base_universe_d2_029_vpd_basefill_034, 29)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_029_vpd_basefill_034'] = {'inputs': ['vpd_base_universe_d2_029_vpd_basefill_034'], 'func': vpd_base_universe_d3_029_vpd_basefill_034}


def vpd_base_universe_d3_030_vpd_basefill_035(vpd_base_universe_d2_030_vpd_basefill_035):
    return _base_universe_d3(vpd_base_universe_d2_030_vpd_basefill_035, 30)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_030_vpd_basefill_035'] = {'inputs': ['vpd_base_universe_d2_030_vpd_basefill_035'], 'func': vpd_base_universe_d3_030_vpd_basefill_035}


def vpd_base_universe_d3_031_vpd_basefill_036(vpd_base_universe_d2_031_vpd_basefill_036):
    return _base_universe_d3(vpd_base_universe_d2_031_vpd_basefill_036, 31)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_031_vpd_basefill_036'] = {'inputs': ['vpd_base_universe_d2_031_vpd_basefill_036'], 'func': vpd_base_universe_d3_031_vpd_basefill_036}


def vpd_base_universe_d3_032_vpd_basefill_037(vpd_base_universe_d2_032_vpd_basefill_037):
    return _base_universe_d3(vpd_base_universe_d2_032_vpd_basefill_037, 32)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_032_vpd_basefill_037'] = {'inputs': ['vpd_base_universe_d2_032_vpd_basefill_037'], 'func': vpd_base_universe_d3_032_vpd_basefill_037}


def vpd_base_universe_d3_033_vpd_basefill_038(vpd_base_universe_d2_033_vpd_basefill_038):
    return _base_universe_d3(vpd_base_universe_d2_033_vpd_basefill_038, 33)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_033_vpd_basefill_038'] = {'inputs': ['vpd_base_universe_d2_033_vpd_basefill_038'], 'func': vpd_base_universe_d3_033_vpd_basefill_038}


def vpd_base_universe_d3_034_vpd_basefill_039(vpd_base_universe_d2_034_vpd_basefill_039):
    return _base_universe_d3(vpd_base_universe_d2_034_vpd_basefill_039, 34)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_034_vpd_basefill_039'] = {'inputs': ['vpd_base_universe_d2_034_vpd_basefill_039'], 'func': vpd_base_universe_d3_034_vpd_basefill_039}


def vpd_base_universe_d3_035_vpd_basefill_040(vpd_base_universe_d2_035_vpd_basefill_040):
    return _base_universe_d3(vpd_base_universe_d2_035_vpd_basefill_040, 35)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_035_vpd_basefill_040'] = {'inputs': ['vpd_base_universe_d2_035_vpd_basefill_040'], 'func': vpd_base_universe_d3_035_vpd_basefill_040}


def vpd_base_universe_d3_036_vpd_basefill_041(vpd_base_universe_d2_036_vpd_basefill_041):
    return _base_universe_d3(vpd_base_universe_d2_036_vpd_basefill_041, 36)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_036_vpd_basefill_041'] = {'inputs': ['vpd_base_universe_d2_036_vpd_basefill_041'], 'func': vpd_base_universe_d3_036_vpd_basefill_041}


def vpd_base_universe_d3_037_vpd_basefill_042(vpd_base_universe_d2_037_vpd_basefill_042):
    return _base_universe_d3(vpd_base_universe_d2_037_vpd_basefill_042, 37)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_037_vpd_basefill_042'] = {'inputs': ['vpd_base_universe_d2_037_vpd_basefill_042'], 'func': vpd_base_universe_d3_037_vpd_basefill_042}


def vpd_base_universe_d3_038_vpd_basefill_043(vpd_base_universe_d2_038_vpd_basefill_043):
    return _base_universe_d3(vpd_base_universe_d2_038_vpd_basefill_043, 38)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_038_vpd_basefill_043'] = {'inputs': ['vpd_base_universe_d2_038_vpd_basefill_043'], 'func': vpd_base_universe_d3_038_vpd_basefill_043}


def vpd_base_universe_d3_039_vpd_basefill_044(vpd_base_universe_d2_039_vpd_basefill_044):
    return _base_universe_d3(vpd_base_universe_d2_039_vpd_basefill_044, 39)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_039_vpd_basefill_044'] = {'inputs': ['vpd_base_universe_d2_039_vpd_basefill_044'], 'func': vpd_base_universe_d3_039_vpd_basefill_044}


def vpd_base_universe_d3_040_vpd_basefill_045(vpd_base_universe_d2_040_vpd_basefill_045):
    return _base_universe_d3(vpd_base_universe_d2_040_vpd_basefill_045, 40)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_040_vpd_basefill_045'] = {'inputs': ['vpd_base_universe_d2_040_vpd_basefill_045'], 'func': vpd_base_universe_d3_040_vpd_basefill_045}


def vpd_base_universe_d3_041_vpd_basefill_046(vpd_base_universe_d2_041_vpd_basefill_046):
    return _base_universe_d3(vpd_base_universe_d2_041_vpd_basefill_046, 41)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_041_vpd_basefill_046'] = {'inputs': ['vpd_base_universe_d2_041_vpd_basefill_046'], 'func': vpd_base_universe_d3_041_vpd_basefill_046}


def vpd_base_universe_d3_042_vpd_basefill_047(vpd_base_universe_d2_042_vpd_basefill_047):
    return _base_universe_d3(vpd_base_universe_d2_042_vpd_basefill_047, 42)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_042_vpd_basefill_047'] = {'inputs': ['vpd_base_universe_d2_042_vpd_basefill_047'], 'func': vpd_base_universe_d3_042_vpd_basefill_047}


def vpd_base_universe_d3_043_vpd_basefill_048(vpd_base_universe_d2_043_vpd_basefill_048):
    return _base_universe_d3(vpd_base_universe_d2_043_vpd_basefill_048, 43)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_043_vpd_basefill_048'] = {'inputs': ['vpd_base_universe_d2_043_vpd_basefill_048'], 'func': vpd_base_universe_d3_043_vpd_basefill_048}


def vpd_base_universe_d3_044_vpd_basefill_049(vpd_base_universe_d2_044_vpd_basefill_049):
    return _base_universe_d3(vpd_base_universe_d2_044_vpd_basefill_049, 44)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_044_vpd_basefill_049'] = {'inputs': ['vpd_base_universe_d2_044_vpd_basefill_049'], 'func': vpd_base_universe_d3_044_vpd_basefill_049}


def vpd_base_universe_d3_045_vpd_basefill_050(vpd_base_universe_d2_045_vpd_basefill_050):
    return _base_universe_d3(vpd_base_universe_d2_045_vpd_basefill_050, 45)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_045_vpd_basefill_050'] = {'inputs': ['vpd_base_universe_d2_045_vpd_basefill_050'], 'func': vpd_base_universe_d3_045_vpd_basefill_050}


def vpd_base_universe_d3_046_vpd_basefill_051(vpd_base_universe_d2_046_vpd_basefill_051):
    return _base_universe_d3(vpd_base_universe_d2_046_vpd_basefill_051, 46)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_046_vpd_basefill_051'] = {'inputs': ['vpd_base_universe_d2_046_vpd_basefill_051'], 'func': vpd_base_universe_d3_046_vpd_basefill_051}


def vpd_base_universe_d3_047_vpd_basefill_052(vpd_base_universe_d2_047_vpd_basefill_052):
    return _base_universe_d3(vpd_base_universe_d2_047_vpd_basefill_052, 47)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_047_vpd_basefill_052'] = {'inputs': ['vpd_base_universe_d2_047_vpd_basefill_052'], 'func': vpd_base_universe_d3_047_vpd_basefill_052}


def vpd_base_universe_d3_048_vpd_basefill_053(vpd_base_universe_d2_048_vpd_basefill_053):
    return _base_universe_d3(vpd_base_universe_d2_048_vpd_basefill_053, 48)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_048_vpd_basefill_053'] = {'inputs': ['vpd_base_universe_d2_048_vpd_basefill_053'], 'func': vpd_base_universe_d3_048_vpd_basefill_053}


def vpd_base_universe_d3_049_vpd_basefill_054(vpd_base_universe_d2_049_vpd_basefill_054):
    return _base_universe_d3(vpd_base_universe_d2_049_vpd_basefill_054, 49)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_049_vpd_basefill_054'] = {'inputs': ['vpd_base_universe_d2_049_vpd_basefill_054'], 'func': vpd_base_universe_d3_049_vpd_basefill_054}


def vpd_base_universe_d3_050_vpd_basefill_055(vpd_base_universe_d2_050_vpd_basefill_055):
    return _base_universe_d3(vpd_base_universe_d2_050_vpd_basefill_055, 50)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_050_vpd_basefill_055'] = {'inputs': ['vpd_base_universe_d2_050_vpd_basefill_055'], 'func': vpd_base_universe_d3_050_vpd_basefill_055}


def vpd_base_universe_d3_051_vpd_basefill_056(vpd_base_universe_d2_051_vpd_basefill_056):
    return _base_universe_d3(vpd_base_universe_d2_051_vpd_basefill_056, 51)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_051_vpd_basefill_056'] = {'inputs': ['vpd_base_universe_d2_051_vpd_basefill_056'], 'func': vpd_base_universe_d3_051_vpd_basefill_056}


def vpd_base_universe_d3_052_vpd_basefill_057(vpd_base_universe_d2_052_vpd_basefill_057):
    return _base_universe_d3(vpd_base_universe_d2_052_vpd_basefill_057, 52)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_052_vpd_basefill_057'] = {'inputs': ['vpd_base_universe_d2_052_vpd_basefill_057'], 'func': vpd_base_universe_d3_052_vpd_basefill_057}


def vpd_base_universe_d3_053_vpd_basefill_058(vpd_base_universe_d2_053_vpd_basefill_058):
    return _base_universe_d3(vpd_base_universe_d2_053_vpd_basefill_058, 53)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_053_vpd_basefill_058'] = {'inputs': ['vpd_base_universe_d2_053_vpd_basefill_058'], 'func': vpd_base_universe_d3_053_vpd_basefill_058}


def vpd_base_universe_d3_054_vpd_basefill_059(vpd_base_universe_d2_054_vpd_basefill_059):
    return _base_universe_d3(vpd_base_universe_d2_054_vpd_basefill_059, 54)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_054_vpd_basefill_059'] = {'inputs': ['vpd_base_universe_d2_054_vpd_basefill_059'], 'func': vpd_base_universe_d3_054_vpd_basefill_059}


def vpd_base_universe_d3_055_vpd_basefill_060(vpd_base_universe_d2_055_vpd_basefill_060):
    return _base_universe_d3(vpd_base_universe_d2_055_vpd_basefill_060, 55)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_055_vpd_basefill_060'] = {'inputs': ['vpd_base_universe_d2_055_vpd_basefill_060'], 'func': vpd_base_universe_d3_055_vpd_basefill_060}


def vpd_base_universe_d3_056_vpd_basefill_061(vpd_base_universe_d2_056_vpd_basefill_061):
    return _base_universe_d3(vpd_base_universe_d2_056_vpd_basefill_061, 56)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_056_vpd_basefill_061'] = {'inputs': ['vpd_base_universe_d2_056_vpd_basefill_061'], 'func': vpd_base_universe_d3_056_vpd_basefill_061}


def vpd_base_universe_d3_057_vpd_basefill_062(vpd_base_universe_d2_057_vpd_basefill_062):
    return _base_universe_d3(vpd_base_universe_d2_057_vpd_basefill_062, 57)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_057_vpd_basefill_062'] = {'inputs': ['vpd_base_universe_d2_057_vpd_basefill_062'], 'func': vpd_base_universe_d3_057_vpd_basefill_062}


def vpd_base_universe_d3_058_vpd_basefill_063(vpd_base_universe_d2_058_vpd_basefill_063):
    return _base_universe_d3(vpd_base_universe_d2_058_vpd_basefill_063, 58)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_058_vpd_basefill_063'] = {'inputs': ['vpd_base_universe_d2_058_vpd_basefill_063'], 'func': vpd_base_universe_d3_058_vpd_basefill_063}


def vpd_base_universe_d3_059_vpd_basefill_064(vpd_base_universe_d2_059_vpd_basefill_064):
    return _base_universe_d3(vpd_base_universe_d2_059_vpd_basefill_064, 59)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_059_vpd_basefill_064'] = {'inputs': ['vpd_base_universe_d2_059_vpd_basefill_064'], 'func': vpd_base_universe_d3_059_vpd_basefill_064}


def vpd_base_universe_d3_060_vpd_basefill_065(vpd_base_universe_d2_060_vpd_basefill_065):
    return _base_universe_d3(vpd_base_universe_d2_060_vpd_basefill_065, 60)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_060_vpd_basefill_065'] = {'inputs': ['vpd_base_universe_d2_060_vpd_basefill_065'], 'func': vpd_base_universe_d3_060_vpd_basefill_065}


def vpd_base_universe_d3_061_vpd_basefill_066(vpd_base_universe_d2_061_vpd_basefill_066):
    return _base_universe_d3(vpd_base_universe_d2_061_vpd_basefill_066, 61)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_061_vpd_basefill_066'] = {'inputs': ['vpd_base_universe_d2_061_vpd_basefill_066'], 'func': vpd_base_universe_d3_061_vpd_basefill_066}


def vpd_base_universe_d3_062_vpd_basefill_067(vpd_base_universe_d2_062_vpd_basefill_067):
    return _base_universe_d3(vpd_base_universe_d2_062_vpd_basefill_067, 62)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_062_vpd_basefill_067'] = {'inputs': ['vpd_base_universe_d2_062_vpd_basefill_067'], 'func': vpd_base_universe_d3_062_vpd_basefill_067}


def vpd_base_universe_d3_063_vpd_basefill_068(vpd_base_universe_d2_063_vpd_basefill_068):
    return _base_universe_d3(vpd_base_universe_d2_063_vpd_basefill_068, 63)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_063_vpd_basefill_068'] = {'inputs': ['vpd_base_universe_d2_063_vpd_basefill_068'], 'func': vpd_base_universe_d3_063_vpd_basefill_068}


def vpd_base_universe_d3_064_vpd_basefill_069(vpd_base_universe_d2_064_vpd_basefill_069):
    return _base_universe_d3(vpd_base_universe_d2_064_vpd_basefill_069, 64)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_064_vpd_basefill_069'] = {'inputs': ['vpd_base_universe_d2_064_vpd_basefill_069'], 'func': vpd_base_universe_d3_064_vpd_basefill_069}


def vpd_base_universe_d3_065_vpd_basefill_070(vpd_base_universe_d2_065_vpd_basefill_070):
    return _base_universe_d3(vpd_base_universe_d2_065_vpd_basefill_070, 65)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_065_vpd_basefill_070'] = {'inputs': ['vpd_base_universe_d2_065_vpd_basefill_070'], 'func': vpd_base_universe_d3_065_vpd_basefill_070}


def vpd_base_universe_d3_066_vpd_basefill_071(vpd_base_universe_d2_066_vpd_basefill_071):
    return _base_universe_d3(vpd_base_universe_d2_066_vpd_basefill_071, 66)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_066_vpd_basefill_071'] = {'inputs': ['vpd_base_universe_d2_066_vpd_basefill_071'], 'func': vpd_base_universe_d3_066_vpd_basefill_071}


def vpd_base_universe_d3_067_vpd_basefill_072(vpd_base_universe_d2_067_vpd_basefill_072):
    return _base_universe_d3(vpd_base_universe_d2_067_vpd_basefill_072, 67)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_067_vpd_basefill_072'] = {'inputs': ['vpd_base_universe_d2_067_vpd_basefill_072'], 'func': vpd_base_universe_d3_067_vpd_basefill_072}


def vpd_base_universe_d3_068_vpd_basefill_073(vpd_base_universe_d2_068_vpd_basefill_073):
    return _base_universe_d3(vpd_base_universe_d2_068_vpd_basefill_073, 68)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_068_vpd_basefill_073'] = {'inputs': ['vpd_base_universe_d2_068_vpd_basefill_073'], 'func': vpd_base_universe_d3_068_vpd_basefill_073}


def vpd_base_universe_d3_069_vpd_basefill_074(vpd_base_universe_d2_069_vpd_basefill_074):
    return _base_universe_d3(vpd_base_universe_d2_069_vpd_basefill_074, 69)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_069_vpd_basefill_074'] = {'inputs': ['vpd_base_universe_d2_069_vpd_basefill_074'], 'func': vpd_base_universe_d3_069_vpd_basefill_074}


def vpd_base_universe_d3_070_vpd_basefill_075(vpd_base_universe_d2_070_vpd_basefill_075):
    return _base_universe_d3(vpd_base_universe_d2_070_vpd_basefill_075, 70)
VPD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vpd_base_universe_d3_070_vpd_basefill_075'] = {'inputs': ['vpd_base_universe_d2_070_vpd_basefill_075'], 'func': vpd_base_universe_d3_070_vpd_basefill_075}
