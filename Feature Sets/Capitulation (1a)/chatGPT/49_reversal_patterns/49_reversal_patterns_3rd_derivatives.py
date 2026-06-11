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



def rev_176_rev_001_gap_down_frequency_5_001_accel_1(rev_151_rev_001_gap_down_frequency_5_001_roc_1):
    feature = _s(rev_151_rev_001_gap_down_frequency_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def rev_177_rev_007_gap_down_frequency_126_007_accel_5(rev_152_rev_007_gap_down_frequency_126_007_roc_5):
    feature = _s(rev_152_rev_007_gap_down_frequency_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def rev_178_rev_013_gap_down_frequency_1008_013_accel_42(rev_153_rev_013_gap_down_frequency_1008_013_roc_42):
    feature = _s(rev_153_rev_013_gap_down_frequency_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def rev_179_rev_019_gap_down_frequency_42_019_accel_126(rev_154_rev_019_gap_down_frequency_42_019_roc_126):
    feature = _s(rev_154_rev_019_gap_down_frequency_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def rev_180_rev_025_gap_down_frequency_378_025_accel_378(rev_155_rev_025_gap_down_frequency_378_025_roc_378):
    feature = _s(rev_155_rev_025_gap_down_frequency_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















REVERSAL_PATTERNS_REGISTRY_3RD_DERIVATIVES = {
    'rev_176_rev_001_gap_down_frequency_5_001_accel_1': {'inputs': ['rev_151_rev_001_gap_down_frequency_5_001_roc_1'], 'func': rev_176_rev_001_gap_down_frequency_5_001_accel_1},
    'rev_177_rev_007_gap_down_frequency_126_007_accel_5': {'inputs': ['rev_152_rev_007_gap_down_frequency_126_007_roc_5'], 'func': rev_177_rev_007_gap_down_frequency_126_007_accel_5},
    'rev_178_rev_013_gap_down_frequency_1008_013_accel_42': {'inputs': ['rev_153_rev_013_gap_down_frequency_1008_013_roc_42'], 'func': rev_178_rev_013_gap_down_frequency_1008_013_accel_42},
    'rev_179_rev_019_gap_down_frequency_42_019_accel_126': {'inputs': ['rev_154_rev_019_gap_down_frequency_42_019_roc_126'], 'func': rev_179_rev_019_gap_down_frequency_42_019_accel_126},
    'rev_180_rev_025_gap_down_frequency_378_025_accel_378': {'inputs': ['rev_155_rev_025_gap_down_frequency_378_025_roc_378'], 'func': rev_180_rev_025_gap_down_frequency_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def rp_replacement_d3_001(rp_replacement_d2_001):
    feature = _clean(rp_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_001'] = {'inputs': ['rp_replacement_d2_001'], 'func': rp_replacement_d3_001}


def rp_replacement_d3_002(rp_replacement_d2_002):
    feature = _clean(rp_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_002'] = {'inputs': ['rp_replacement_d2_002'], 'func': rp_replacement_d3_002}


def rp_replacement_d3_003(rp_replacement_d2_003):
    feature = _clean(rp_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_003'] = {'inputs': ['rp_replacement_d2_003'], 'func': rp_replacement_d3_003}


def rp_replacement_d3_004(rp_replacement_d2_004):
    feature = _clean(rp_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_004'] = {'inputs': ['rp_replacement_d2_004'], 'func': rp_replacement_d3_004}


def rp_replacement_d3_005(rp_replacement_d2_005):
    feature = _clean(rp_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_005'] = {'inputs': ['rp_replacement_d2_005'], 'func': rp_replacement_d3_005}


def rp_replacement_d3_006(rp_replacement_d2_006):
    feature = _clean(rp_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_006'] = {'inputs': ['rp_replacement_d2_006'], 'func': rp_replacement_d3_006}


def rp_replacement_d3_007(rp_replacement_d2_007):
    feature = _clean(rp_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_007'] = {'inputs': ['rp_replacement_d2_007'], 'func': rp_replacement_d3_007}


def rp_replacement_d3_008(rp_replacement_d2_008):
    feature = _clean(rp_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_008'] = {'inputs': ['rp_replacement_d2_008'], 'func': rp_replacement_d3_008}


def rp_replacement_d3_009(rp_replacement_d2_009):
    feature = _clean(rp_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_009'] = {'inputs': ['rp_replacement_d2_009'], 'func': rp_replacement_d3_009}


def rp_replacement_d3_010(rp_replacement_d2_010):
    feature = _clean(rp_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_010'] = {'inputs': ['rp_replacement_d2_010'], 'func': rp_replacement_d3_010}


def rp_replacement_d3_011(rp_replacement_d2_011):
    feature = _clean(rp_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_011'] = {'inputs': ['rp_replacement_d2_011'], 'func': rp_replacement_d3_011}


def rp_replacement_d3_012(rp_replacement_d2_012):
    feature = _clean(rp_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_012'] = {'inputs': ['rp_replacement_d2_012'], 'func': rp_replacement_d3_012}


def rp_replacement_d3_013(rp_replacement_d2_013):
    feature = _clean(rp_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_013'] = {'inputs': ['rp_replacement_d2_013'], 'func': rp_replacement_d3_013}


def rp_replacement_d3_014(rp_replacement_d2_014):
    feature = _clean(rp_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_014'] = {'inputs': ['rp_replacement_d2_014'], 'func': rp_replacement_d3_014}


def rp_replacement_d3_015(rp_replacement_d2_015):
    feature = _clean(rp_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_015'] = {'inputs': ['rp_replacement_d2_015'], 'func': rp_replacement_d3_015}


def rp_replacement_d3_016(rp_replacement_d2_016):
    feature = _clean(rp_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_016'] = {'inputs': ['rp_replacement_d2_016'], 'func': rp_replacement_d3_016}


def rp_replacement_d3_017(rp_replacement_d2_017):
    feature = _clean(rp_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_017'] = {'inputs': ['rp_replacement_d2_017'], 'func': rp_replacement_d3_017}


def rp_replacement_d3_018(rp_replacement_d2_018):
    feature = _clean(rp_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_018'] = {'inputs': ['rp_replacement_d2_018'], 'func': rp_replacement_d3_018}


def rp_replacement_d3_019(rp_replacement_d2_019):
    feature = _clean(rp_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_019'] = {'inputs': ['rp_replacement_d2_019'], 'func': rp_replacement_d3_019}


def rp_replacement_d3_020(rp_replacement_d2_020):
    feature = _clean(rp_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_020'] = {'inputs': ['rp_replacement_d2_020'], 'func': rp_replacement_d3_020}


def rp_replacement_d3_021(rp_replacement_d2_021):
    feature = _clean(rp_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_021'] = {'inputs': ['rp_replacement_d2_021'], 'func': rp_replacement_d3_021}


def rp_replacement_d3_022(rp_replacement_d2_022):
    feature = _clean(rp_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_022'] = {'inputs': ['rp_replacement_d2_022'], 'func': rp_replacement_d3_022}


def rp_replacement_d3_023(rp_replacement_d2_023):
    feature = _clean(rp_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_023'] = {'inputs': ['rp_replacement_d2_023'], 'func': rp_replacement_d3_023}


def rp_replacement_d3_024(rp_replacement_d2_024):
    feature = _clean(rp_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_024'] = {'inputs': ['rp_replacement_d2_024'], 'func': rp_replacement_d3_024}


def rp_replacement_d3_025(rp_replacement_d2_025):
    feature = _clean(rp_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_025'] = {'inputs': ['rp_replacement_d2_025'], 'func': rp_replacement_d3_025}


def rp_replacement_d3_026(rp_replacement_d2_026):
    feature = _clean(rp_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_026'] = {'inputs': ['rp_replacement_d2_026'], 'func': rp_replacement_d3_026}


def rp_replacement_d3_027(rp_replacement_d2_027):
    feature = _clean(rp_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_027'] = {'inputs': ['rp_replacement_d2_027'], 'func': rp_replacement_d3_027}


def rp_replacement_d3_028(rp_replacement_d2_028):
    feature = _clean(rp_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_028'] = {'inputs': ['rp_replacement_d2_028'], 'func': rp_replacement_d3_028}


def rp_replacement_d3_029(rp_replacement_d2_029):
    feature = _clean(rp_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_029'] = {'inputs': ['rp_replacement_d2_029'], 'func': rp_replacement_d3_029}


def rp_replacement_d3_030(rp_replacement_d2_030):
    feature = _clean(rp_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_030'] = {'inputs': ['rp_replacement_d2_030'], 'func': rp_replacement_d3_030}


def rp_replacement_d3_031(rp_replacement_d2_031):
    feature = _clean(rp_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_031'] = {'inputs': ['rp_replacement_d2_031'], 'func': rp_replacement_d3_031}


def rp_replacement_d3_032(rp_replacement_d2_032):
    feature = _clean(rp_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_032'] = {'inputs': ['rp_replacement_d2_032'], 'func': rp_replacement_d3_032}


def rp_replacement_d3_033(rp_replacement_d2_033):
    feature = _clean(rp_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_033'] = {'inputs': ['rp_replacement_d2_033'], 'func': rp_replacement_d3_033}


def rp_replacement_d3_034(rp_replacement_d2_034):
    feature = _clean(rp_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_034'] = {'inputs': ['rp_replacement_d2_034'], 'func': rp_replacement_d3_034}


def rp_replacement_d3_035(rp_replacement_d2_035):
    feature = _clean(rp_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_035'] = {'inputs': ['rp_replacement_d2_035'], 'func': rp_replacement_d3_035}


def rp_replacement_d3_036(rp_replacement_d2_036):
    feature = _clean(rp_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_036'] = {'inputs': ['rp_replacement_d2_036'], 'func': rp_replacement_d3_036}


def rp_replacement_d3_037(rp_replacement_d2_037):
    feature = _clean(rp_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_037'] = {'inputs': ['rp_replacement_d2_037'], 'func': rp_replacement_d3_037}


def rp_replacement_d3_038(rp_replacement_d2_038):
    feature = _clean(rp_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_038'] = {'inputs': ['rp_replacement_d2_038'], 'func': rp_replacement_d3_038}


def rp_replacement_d3_039(rp_replacement_d2_039):
    feature = _clean(rp_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_039'] = {'inputs': ['rp_replacement_d2_039'], 'func': rp_replacement_d3_039}


def rp_replacement_d3_040(rp_replacement_d2_040):
    feature = _clean(rp_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_040'] = {'inputs': ['rp_replacement_d2_040'], 'func': rp_replacement_d3_040}


def rp_replacement_d3_041(rp_replacement_d2_041):
    feature = _clean(rp_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_041'] = {'inputs': ['rp_replacement_d2_041'], 'func': rp_replacement_d3_041}


def rp_replacement_d3_042(rp_replacement_d2_042):
    feature = _clean(rp_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_042'] = {'inputs': ['rp_replacement_d2_042'], 'func': rp_replacement_d3_042}


def rp_replacement_d3_043(rp_replacement_d2_043):
    feature = _clean(rp_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_043'] = {'inputs': ['rp_replacement_d2_043'], 'func': rp_replacement_d3_043}


def rp_replacement_d3_044(rp_replacement_d2_044):
    feature = _clean(rp_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_044'] = {'inputs': ['rp_replacement_d2_044'], 'func': rp_replacement_d3_044}


def rp_replacement_d3_045(rp_replacement_d2_045):
    feature = _clean(rp_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_045'] = {'inputs': ['rp_replacement_d2_045'], 'func': rp_replacement_d3_045}


def rp_replacement_d3_046(rp_replacement_d2_046):
    feature = _clean(rp_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_046'] = {'inputs': ['rp_replacement_d2_046'], 'func': rp_replacement_d3_046}


def rp_replacement_d3_047(rp_replacement_d2_047):
    feature = _clean(rp_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_047'] = {'inputs': ['rp_replacement_d2_047'], 'func': rp_replacement_d3_047}


def rp_replacement_d3_048(rp_replacement_d2_048):
    feature = _clean(rp_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_048'] = {'inputs': ['rp_replacement_d2_048'], 'func': rp_replacement_d3_048}


def rp_replacement_d3_049(rp_replacement_d2_049):
    feature = _clean(rp_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_049'] = {'inputs': ['rp_replacement_d2_049'], 'func': rp_replacement_d3_049}


def rp_replacement_d3_050(rp_replacement_d2_050):
    feature = _clean(rp_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_050'] = {'inputs': ['rp_replacement_d2_050'], 'func': rp_replacement_d3_050}


def rp_replacement_d3_051(rp_replacement_d2_051):
    feature = _clean(rp_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_051'] = {'inputs': ['rp_replacement_d2_051'], 'func': rp_replacement_d3_051}


def rp_replacement_d3_052(rp_replacement_d2_052):
    feature = _clean(rp_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_052'] = {'inputs': ['rp_replacement_d2_052'], 'func': rp_replacement_d3_052}


def rp_replacement_d3_053(rp_replacement_d2_053):
    feature = _clean(rp_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_053'] = {'inputs': ['rp_replacement_d2_053'], 'func': rp_replacement_d3_053}


def rp_replacement_d3_054(rp_replacement_d2_054):
    feature = _clean(rp_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_054'] = {'inputs': ['rp_replacement_d2_054'], 'func': rp_replacement_d3_054}


def rp_replacement_d3_055(rp_replacement_d2_055):
    feature = _clean(rp_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_055'] = {'inputs': ['rp_replacement_d2_055'], 'func': rp_replacement_d3_055}


def rp_replacement_d3_056(rp_replacement_d2_056):
    feature = _clean(rp_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_056'] = {'inputs': ['rp_replacement_d2_056'], 'func': rp_replacement_d3_056}


def rp_replacement_d3_057(rp_replacement_d2_057):
    feature = _clean(rp_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_057'] = {'inputs': ['rp_replacement_d2_057'], 'func': rp_replacement_d3_057}


def rp_replacement_d3_058(rp_replacement_d2_058):
    feature = _clean(rp_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_058'] = {'inputs': ['rp_replacement_d2_058'], 'func': rp_replacement_d3_058}


def rp_replacement_d3_059(rp_replacement_d2_059):
    feature = _clean(rp_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_059'] = {'inputs': ['rp_replacement_d2_059'], 'func': rp_replacement_d3_059}


def rp_replacement_d3_060(rp_replacement_d2_060):
    feature = _clean(rp_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_060'] = {'inputs': ['rp_replacement_d2_060'], 'func': rp_replacement_d3_060}


def rp_replacement_d3_061(rp_replacement_d2_061):
    feature = _clean(rp_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_061'] = {'inputs': ['rp_replacement_d2_061'], 'func': rp_replacement_d3_061}


def rp_replacement_d3_062(rp_replacement_d2_062):
    feature = _clean(rp_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_062'] = {'inputs': ['rp_replacement_d2_062'], 'func': rp_replacement_d3_062}


def rp_replacement_d3_063(rp_replacement_d2_063):
    feature = _clean(rp_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_063'] = {'inputs': ['rp_replacement_d2_063'], 'func': rp_replacement_d3_063}


def rp_replacement_d3_064(rp_replacement_d2_064):
    feature = _clean(rp_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_064'] = {'inputs': ['rp_replacement_d2_064'], 'func': rp_replacement_d3_064}


def rp_replacement_d3_065(rp_replacement_d2_065):
    feature = _clean(rp_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_065'] = {'inputs': ['rp_replacement_d2_065'], 'func': rp_replacement_d3_065}


def rp_replacement_d3_066(rp_replacement_d2_066):
    feature = _clean(rp_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_066'] = {'inputs': ['rp_replacement_d2_066'], 'func': rp_replacement_d3_066}


def rp_replacement_d3_067(rp_replacement_d2_067):
    feature = _clean(rp_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_067'] = {'inputs': ['rp_replacement_d2_067'], 'func': rp_replacement_d3_067}


def rp_replacement_d3_068(rp_replacement_d2_068):
    feature = _clean(rp_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_068'] = {'inputs': ['rp_replacement_d2_068'], 'func': rp_replacement_d3_068}


def rp_replacement_d3_069(rp_replacement_d2_069):
    feature = _clean(rp_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_069'] = {'inputs': ['rp_replacement_d2_069'], 'func': rp_replacement_d3_069}


def rp_replacement_d3_070(rp_replacement_d2_070):
    feature = _clean(rp_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_070'] = {'inputs': ['rp_replacement_d2_070'], 'func': rp_replacement_d3_070}


def rp_replacement_d3_071(rp_replacement_d2_071):
    feature = _clean(rp_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_071'] = {'inputs': ['rp_replacement_d2_071'], 'func': rp_replacement_d3_071}


def rp_replacement_d3_072(rp_replacement_d2_072):
    feature = _clean(rp_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_072'] = {'inputs': ['rp_replacement_d2_072'], 'func': rp_replacement_d3_072}


def rp_replacement_d3_073(rp_replacement_d2_073):
    feature = _clean(rp_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_073'] = {'inputs': ['rp_replacement_d2_073'], 'func': rp_replacement_d3_073}


def rp_replacement_d3_074(rp_replacement_d2_074):
    feature = _clean(rp_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_074'] = {'inputs': ['rp_replacement_d2_074'], 'func': rp_replacement_d3_074}


def rp_replacement_d3_075(rp_replacement_d2_075):
    feature = _clean(rp_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_075'] = {'inputs': ['rp_replacement_d2_075'], 'func': rp_replacement_d3_075}


def rp_replacement_d3_076(rp_replacement_d2_076):
    feature = _clean(rp_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_076'] = {'inputs': ['rp_replacement_d2_076'], 'func': rp_replacement_d3_076}


def rp_replacement_d3_077(rp_replacement_d2_077):
    feature = _clean(rp_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_077'] = {'inputs': ['rp_replacement_d2_077'], 'func': rp_replacement_d3_077}


def rp_replacement_d3_078(rp_replacement_d2_078):
    feature = _clean(rp_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_078'] = {'inputs': ['rp_replacement_d2_078'], 'func': rp_replacement_d3_078}


def rp_replacement_d3_079(rp_replacement_d2_079):
    feature = _clean(rp_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_079'] = {'inputs': ['rp_replacement_d2_079'], 'func': rp_replacement_d3_079}


def rp_replacement_d3_080(rp_replacement_d2_080):
    feature = _clean(rp_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_080'] = {'inputs': ['rp_replacement_d2_080'], 'func': rp_replacement_d3_080}


def rp_replacement_d3_081(rp_replacement_d2_081):
    feature = _clean(rp_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_081'] = {'inputs': ['rp_replacement_d2_081'], 'func': rp_replacement_d3_081}


def rp_replacement_d3_082(rp_replacement_d2_082):
    feature = _clean(rp_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_082'] = {'inputs': ['rp_replacement_d2_082'], 'func': rp_replacement_d3_082}


def rp_replacement_d3_083(rp_replacement_d2_083):
    feature = _clean(rp_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_083'] = {'inputs': ['rp_replacement_d2_083'], 'func': rp_replacement_d3_083}


def rp_replacement_d3_084(rp_replacement_d2_084):
    feature = _clean(rp_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_084'] = {'inputs': ['rp_replacement_d2_084'], 'func': rp_replacement_d3_084}


def rp_replacement_d3_085(rp_replacement_d2_085):
    feature = _clean(rp_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_085'] = {'inputs': ['rp_replacement_d2_085'], 'func': rp_replacement_d3_085}


def rp_replacement_d3_086(rp_replacement_d2_086):
    feature = _clean(rp_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_086'] = {'inputs': ['rp_replacement_d2_086'], 'func': rp_replacement_d3_086}


def rp_replacement_d3_087(rp_replacement_d2_087):
    feature = _clean(rp_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_087'] = {'inputs': ['rp_replacement_d2_087'], 'func': rp_replacement_d3_087}


def rp_replacement_d3_088(rp_replacement_d2_088):
    feature = _clean(rp_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_088'] = {'inputs': ['rp_replacement_d2_088'], 'func': rp_replacement_d3_088}


def rp_replacement_d3_089(rp_replacement_d2_089):
    feature = _clean(rp_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_089'] = {'inputs': ['rp_replacement_d2_089'], 'func': rp_replacement_d3_089}


def rp_replacement_d3_090(rp_replacement_d2_090):
    feature = _clean(rp_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_090'] = {'inputs': ['rp_replacement_d2_090'], 'func': rp_replacement_d3_090}


def rp_replacement_d3_091(rp_replacement_d2_091):
    feature = _clean(rp_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_091'] = {'inputs': ['rp_replacement_d2_091'], 'func': rp_replacement_d3_091}


def rp_replacement_d3_092(rp_replacement_d2_092):
    feature = _clean(rp_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_092'] = {'inputs': ['rp_replacement_d2_092'], 'func': rp_replacement_d3_092}


def rp_replacement_d3_093(rp_replacement_d2_093):
    feature = _clean(rp_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_093'] = {'inputs': ['rp_replacement_d2_093'], 'func': rp_replacement_d3_093}


def rp_replacement_d3_094(rp_replacement_d2_094):
    feature = _clean(rp_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_094'] = {'inputs': ['rp_replacement_d2_094'], 'func': rp_replacement_d3_094}


def rp_replacement_d3_095(rp_replacement_d2_095):
    feature = _clean(rp_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_095'] = {'inputs': ['rp_replacement_d2_095'], 'func': rp_replacement_d3_095}


def rp_replacement_d3_096(rp_replacement_d2_096):
    feature = _clean(rp_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_096'] = {'inputs': ['rp_replacement_d2_096'], 'func': rp_replacement_d3_096}


def rp_replacement_d3_097(rp_replacement_d2_097):
    feature = _clean(rp_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_097'] = {'inputs': ['rp_replacement_d2_097'], 'func': rp_replacement_d3_097}


def rp_replacement_d3_098(rp_replacement_d2_098):
    feature = _clean(rp_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_098'] = {'inputs': ['rp_replacement_d2_098'], 'func': rp_replacement_d3_098}


def rp_replacement_d3_099(rp_replacement_d2_099):
    feature = _clean(rp_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_099'] = {'inputs': ['rp_replacement_d2_099'], 'func': rp_replacement_d3_099}


def rp_replacement_d3_100(rp_replacement_d2_100):
    feature = _clean(rp_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_100'] = {'inputs': ['rp_replacement_d2_100'], 'func': rp_replacement_d3_100}


def rp_replacement_d3_101(rp_replacement_d2_101):
    feature = _clean(rp_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_101'] = {'inputs': ['rp_replacement_d2_101'], 'func': rp_replacement_d3_101}


def rp_replacement_d3_102(rp_replacement_d2_102):
    feature = _clean(rp_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_102'] = {'inputs': ['rp_replacement_d2_102'], 'func': rp_replacement_d3_102}


def rp_replacement_d3_103(rp_replacement_d2_103):
    feature = _clean(rp_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_103'] = {'inputs': ['rp_replacement_d2_103'], 'func': rp_replacement_d3_103}


def rp_replacement_d3_104(rp_replacement_d2_104):
    feature = _clean(rp_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_104'] = {'inputs': ['rp_replacement_d2_104'], 'func': rp_replacement_d3_104}


def rp_replacement_d3_105(rp_replacement_d2_105):
    feature = _clean(rp_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_105'] = {'inputs': ['rp_replacement_d2_105'], 'func': rp_replacement_d3_105}


def rp_replacement_d3_106(rp_replacement_d2_106):
    feature = _clean(rp_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_106'] = {'inputs': ['rp_replacement_d2_106'], 'func': rp_replacement_d3_106}


def rp_replacement_d3_107(rp_replacement_d2_107):
    feature = _clean(rp_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_107'] = {'inputs': ['rp_replacement_d2_107'], 'func': rp_replacement_d3_107}


def rp_replacement_d3_108(rp_replacement_d2_108):
    feature = _clean(rp_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_108'] = {'inputs': ['rp_replacement_d2_108'], 'func': rp_replacement_d3_108}


def rp_replacement_d3_109(rp_replacement_d2_109):
    feature = _clean(rp_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_109'] = {'inputs': ['rp_replacement_d2_109'], 'func': rp_replacement_d3_109}


def rp_replacement_d3_110(rp_replacement_d2_110):
    feature = _clean(rp_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_110'] = {'inputs': ['rp_replacement_d2_110'], 'func': rp_replacement_d3_110}


def rp_replacement_d3_111(rp_replacement_d2_111):
    feature = _clean(rp_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_111'] = {'inputs': ['rp_replacement_d2_111'], 'func': rp_replacement_d3_111}


def rp_replacement_d3_112(rp_replacement_d2_112):
    feature = _clean(rp_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_112'] = {'inputs': ['rp_replacement_d2_112'], 'func': rp_replacement_d3_112}


def rp_replacement_d3_113(rp_replacement_d2_113):
    feature = _clean(rp_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_113'] = {'inputs': ['rp_replacement_d2_113'], 'func': rp_replacement_d3_113}


def rp_replacement_d3_114(rp_replacement_d2_114):
    feature = _clean(rp_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_114'] = {'inputs': ['rp_replacement_d2_114'], 'func': rp_replacement_d3_114}


def rp_replacement_d3_115(rp_replacement_d2_115):
    feature = _clean(rp_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_115'] = {'inputs': ['rp_replacement_d2_115'], 'func': rp_replacement_d3_115}


def rp_replacement_d3_116(rp_replacement_d2_116):
    feature = _clean(rp_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_116'] = {'inputs': ['rp_replacement_d2_116'], 'func': rp_replacement_d3_116}


def rp_replacement_d3_117(rp_replacement_d2_117):
    feature = _clean(rp_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_117'] = {'inputs': ['rp_replacement_d2_117'], 'func': rp_replacement_d3_117}


def rp_replacement_d3_118(rp_replacement_d2_118):
    feature = _clean(rp_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_118'] = {'inputs': ['rp_replacement_d2_118'], 'func': rp_replacement_d3_118}


def rp_replacement_d3_119(rp_replacement_d2_119):
    feature = _clean(rp_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_119'] = {'inputs': ['rp_replacement_d2_119'], 'func': rp_replacement_d3_119}


def rp_replacement_d3_120(rp_replacement_d2_120):
    feature = _clean(rp_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_120'] = {'inputs': ['rp_replacement_d2_120'], 'func': rp_replacement_d3_120}


def rp_replacement_d3_121(rp_replacement_d2_121):
    feature = _clean(rp_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_121'] = {'inputs': ['rp_replacement_d2_121'], 'func': rp_replacement_d3_121}


def rp_replacement_d3_122(rp_replacement_d2_122):
    feature = _clean(rp_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_122'] = {'inputs': ['rp_replacement_d2_122'], 'func': rp_replacement_d3_122}


def rp_replacement_d3_123(rp_replacement_d2_123):
    feature = _clean(rp_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_123'] = {'inputs': ['rp_replacement_d2_123'], 'func': rp_replacement_d3_123}


def rp_replacement_d3_124(rp_replacement_d2_124):
    feature = _clean(rp_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_124'] = {'inputs': ['rp_replacement_d2_124'], 'func': rp_replacement_d3_124}


def rp_replacement_d3_125(rp_replacement_d2_125):
    feature = _clean(rp_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_125'] = {'inputs': ['rp_replacement_d2_125'], 'func': rp_replacement_d3_125}


def rp_replacement_d3_126(rp_replacement_d2_126):
    feature = _clean(rp_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_126'] = {'inputs': ['rp_replacement_d2_126'], 'func': rp_replacement_d3_126}


def rp_replacement_d3_127(rp_replacement_d2_127):
    feature = _clean(rp_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_127'] = {'inputs': ['rp_replacement_d2_127'], 'func': rp_replacement_d3_127}


def rp_replacement_d3_128(rp_replacement_d2_128):
    feature = _clean(rp_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_128'] = {'inputs': ['rp_replacement_d2_128'], 'func': rp_replacement_d3_128}


def rp_replacement_d3_129(rp_replacement_d2_129):
    feature = _clean(rp_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_129'] = {'inputs': ['rp_replacement_d2_129'], 'func': rp_replacement_d3_129}


def rp_replacement_d3_130(rp_replacement_d2_130):
    feature = _clean(rp_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_130'] = {'inputs': ['rp_replacement_d2_130'], 'func': rp_replacement_d3_130}


def rp_replacement_d3_131(rp_replacement_d2_131):
    feature = _clean(rp_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_131'] = {'inputs': ['rp_replacement_d2_131'], 'func': rp_replacement_d3_131}


def rp_replacement_d3_132(rp_replacement_d2_132):
    feature = _clean(rp_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_132'] = {'inputs': ['rp_replacement_d2_132'], 'func': rp_replacement_d3_132}


def rp_replacement_d3_133(rp_replacement_d2_133):
    feature = _clean(rp_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_133'] = {'inputs': ['rp_replacement_d2_133'], 'func': rp_replacement_d3_133}


def rp_replacement_d3_134(rp_replacement_d2_134):
    feature = _clean(rp_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_134'] = {'inputs': ['rp_replacement_d2_134'], 'func': rp_replacement_d3_134}


def rp_replacement_d3_135(rp_replacement_d2_135):
    feature = _clean(rp_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_135'] = {'inputs': ['rp_replacement_d2_135'], 'func': rp_replacement_d3_135}


def rp_replacement_d3_136(rp_replacement_d2_136):
    feature = _clean(rp_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_136'] = {'inputs': ['rp_replacement_d2_136'], 'func': rp_replacement_d3_136}


def rp_replacement_d3_137(rp_replacement_d2_137):
    feature = _clean(rp_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_137'] = {'inputs': ['rp_replacement_d2_137'], 'func': rp_replacement_d3_137}


def rp_replacement_d3_138(rp_replacement_d2_138):
    feature = _clean(rp_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_138'] = {'inputs': ['rp_replacement_d2_138'], 'func': rp_replacement_d3_138}


def rp_replacement_d3_139(rp_replacement_d2_139):
    feature = _clean(rp_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_139'] = {'inputs': ['rp_replacement_d2_139'], 'func': rp_replacement_d3_139}


def rp_replacement_d3_140(rp_replacement_d2_140):
    feature = _clean(rp_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_140'] = {'inputs': ['rp_replacement_d2_140'], 'func': rp_replacement_d3_140}


def rp_replacement_d3_141(rp_replacement_d2_141):
    feature = _clean(rp_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_141'] = {'inputs': ['rp_replacement_d2_141'], 'func': rp_replacement_d3_141}


def rp_replacement_d3_142(rp_replacement_d2_142):
    feature = _clean(rp_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_142'] = {'inputs': ['rp_replacement_d2_142'], 'func': rp_replacement_d3_142}


def rp_replacement_d3_143(rp_replacement_d2_143):
    feature = _clean(rp_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_143'] = {'inputs': ['rp_replacement_d2_143'], 'func': rp_replacement_d3_143}


def rp_replacement_d3_144(rp_replacement_d2_144):
    feature = _clean(rp_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_144'] = {'inputs': ['rp_replacement_d2_144'], 'func': rp_replacement_d3_144}


def rp_replacement_d3_145(rp_replacement_d2_145):
    feature = _clean(rp_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_145'] = {'inputs': ['rp_replacement_d2_145'], 'func': rp_replacement_d3_145}


def rp_replacement_d3_146(rp_replacement_d2_146):
    feature = _clean(rp_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_146'] = {'inputs': ['rp_replacement_d2_146'], 'func': rp_replacement_d3_146}


def rp_replacement_d3_147(rp_replacement_d2_147):
    feature = _clean(rp_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_147'] = {'inputs': ['rp_replacement_d2_147'], 'func': rp_replacement_d3_147}


def rp_replacement_d3_148(rp_replacement_d2_148):
    feature = _clean(rp_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_148'] = {'inputs': ['rp_replacement_d2_148'], 'func': rp_replacement_d3_148}


def rp_replacement_d3_149(rp_replacement_d2_149):
    feature = _clean(rp_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_149'] = {'inputs': ['rp_replacement_d2_149'], 'func': rp_replacement_d3_149}


def rp_replacement_d3_150(rp_replacement_d2_150):
    feature = _clean(rp_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_150'] = {'inputs': ['rp_replacement_d2_150'], 'func': rp_replacement_d3_150}


def rp_replacement_d3_151(rp_replacement_d2_151):
    feature = _clean(rp_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_151'] = {'inputs': ['rp_replacement_d2_151'], 'func': rp_replacement_d3_151}


def rp_replacement_d3_152(rp_replacement_d2_152):
    feature = _clean(rp_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_152'] = {'inputs': ['rp_replacement_d2_152'], 'func': rp_replacement_d3_152}


def rp_replacement_d3_153(rp_replacement_d2_153):
    feature = _clean(rp_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_153'] = {'inputs': ['rp_replacement_d2_153'], 'func': rp_replacement_d3_153}


def rp_replacement_d3_154(rp_replacement_d2_154):
    feature = _clean(rp_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_154'] = {'inputs': ['rp_replacement_d2_154'], 'func': rp_replacement_d3_154}


def rp_replacement_d3_155(rp_replacement_d2_155):
    feature = _clean(rp_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_155'] = {'inputs': ['rp_replacement_d2_155'], 'func': rp_replacement_d3_155}


def rp_replacement_d3_156(rp_replacement_d2_156):
    feature = _clean(rp_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_156'] = {'inputs': ['rp_replacement_d2_156'], 'func': rp_replacement_d3_156}


def rp_replacement_d3_157(rp_replacement_d2_157):
    feature = _clean(rp_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_157'] = {'inputs': ['rp_replacement_d2_157'], 'func': rp_replacement_d3_157}


def rp_replacement_d3_158(rp_replacement_d2_158):
    feature = _clean(rp_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_158'] = {'inputs': ['rp_replacement_d2_158'], 'func': rp_replacement_d3_158}


def rp_replacement_d3_159(rp_replacement_d2_159):
    feature = _clean(rp_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_159'] = {'inputs': ['rp_replacement_d2_159'], 'func': rp_replacement_d3_159}


def rp_replacement_d3_160(rp_replacement_d2_160):
    feature = _clean(rp_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
RP_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rp_replacement_d3_160'] = {'inputs': ['rp_replacement_d2_160'], 'func': rp_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rev_base_universe_d3_001_rev_002_gap_magnitude_10_002(rev_base_universe_d2_001_rev_002_gap_magnitude_10_002):
    return _base_universe_d3(rev_base_universe_d2_001_rev_002_gap_magnitude_10_002, 1)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_001_rev_002_gap_magnitude_10_002'] = {'inputs': ['rev_base_universe_d2_001_rev_002_gap_magnitude_10_002'], 'func': rev_base_universe_d3_001_rev_002_gap_magnitude_10_002}


def rev_base_universe_d3_002_rev_003_open_close_pressure_21_003(rev_base_universe_d2_002_rev_003_open_close_pressure_21_003):
    return _base_universe_d3(rev_base_universe_d2_002_rev_003_open_close_pressure_21_003, 2)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_002_rev_003_open_close_pressure_21_003'] = {'inputs': ['rev_base_universe_d2_002_rev_003_open_close_pressure_21_003'], 'func': rev_base_universe_d3_002_rev_003_open_close_pressure_21_003}


def rev_base_universe_d3_003_rev_004_lower_wick_ratio_42_004(rev_base_universe_d2_003_rev_004_lower_wick_ratio_42_004):
    return _base_universe_d3(rev_base_universe_d2_003_rev_004_lower_wick_ratio_42_004, 3)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_003_rev_004_lower_wick_ratio_42_004'] = {'inputs': ['rev_base_universe_d2_003_rev_004_lower_wick_ratio_42_004'], 'func': rev_base_universe_d3_003_rev_004_lower_wick_ratio_42_004}


def rev_base_universe_d3_004_rev_005_upper_wick_ratio_63_005(rev_base_universe_d2_004_rev_005_upper_wick_ratio_63_005):
    return _base_universe_d3(rev_base_universe_d2_004_rev_005_upper_wick_ratio_63_005, 4)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_004_rev_005_upper_wick_ratio_63_005'] = {'inputs': ['rev_base_universe_d2_004_rev_005_upper_wick_ratio_63_005'], 'func': rev_base_universe_d3_004_rev_005_upper_wick_ratio_63_005}


def rev_base_universe_d3_005_rev_006_body_to_range_84_006(rev_base_universe_d2_005_rev_006_body_to_range_84_006):
    return _base_universe_d3(rev_base_universe_d2_005_rev_006_body_to_range_84_006, 5)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_005_rev_006_body_to_range_84_006'] = {'inputs': ['rev_base_universe_d2_005_rev_006_body_to_range_84_006'], 'func': rev_base_universe_d3_005_rev_006_body_to_range_84_006}


def rev_base_universe_d3_006_rev_008_gap_magnitude_189_008(rev_base_universe_d2_006_rev_008_gap_magnitude_189_008):
    return _base_universe_d3(rev_base_universe_d2_006_rev_008_gap_magnitude_189_008, 6)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_006_rev_008_gap_magnitude_189_008'] = {'inputs': ['rev_base_universe_d2_006_rev_008_gap_magnitude_189_008'], 'func': rev_base_universe_d3_006_rev_008_gap_magnitude_189_008}


def rev_base_universe_d3_007_rev_009_open_close_pressure_252_009(rev_base_universe_d2_007_rev_009_open_close_pressure_252_009):
    return _base_universe_d3(rev_base_universe_d2_007_rev_009_open_close_pressure_252_009, 7)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_007_rev_009_open_close_pressure_252_009'] = {'inputs': ['rev_base_universe_d2_007_rev_009_open_close_pressure_252_009'], 'func': rev_base_universe_d3_007_rev_009_open_close_pressure_252_009}


def rev_base_universe_d3_008_rev_010_lower_wick_ratio_378_010(rev_base_universe_d2_008_rev_010_lower_wick_ratio_378_010):
    return _base_universe_d3(rev_base_universe_d2_008_rev_010_lower_wick_ratio_378_010, 8)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_008_rev_010_lower_wick_ratio_378_010'] = {'inputs': ['rev_base_universe_d2_008_rev_010_lower_wick_ratio_378_010'], 'func': rev_base_universe_d3_008_rev_010_lower_wick_ratio_378_010}


def rev_base_universe_d3_009_rev_011_upper_wick_ratio_504_011(rev_base_universe_d2_009_rev_011_upper_wick_ratio_504_011):
    return _base_universe_d3(rev_base_universe_d2_009_rev_011_upper_wick_ratio_504_011, 9)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_009_rev_011_upper_wick_ratio_504_011'] = {'inputs': ['rev_base_universe_d2_009_rev_011_upper_wick_ratio_504_011'], 'func': rev_base_universe_d3_009_rev_011_upper_wick_ratio_504_011}


def rev_base_universe_d3_010_rev_012_body_to_range_756_012(rev_base_universe_d2_010_rev_012_body_to_range_756_012):
    return _base_universe_d3(rev_base_universe_d2_010_rev_012_body_to_range_756_012, 10)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_010_rev_012_body_to_range_756_012'] = {'inputs': ['rev_base_universe_d2_010_rev_012_body_to_range_756_012'], 'func': rev_base_universe_d3_010_rev_012_body_to_range_756_012}


def rev_base_universe_d3_011_rev_014_gap_magnitude_1260_014(rev_base_universe_d2_011_rev_014_gap_magnitude_1260_014):
    return _base_universe_d3(rev_base_universe_d2_011_rev_014_gap_magnitude_1260_014, 11)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_011_rev_014_gap_magnitude_1260_014'] = {'inputs': ['rev_base_universe_d2_011_rev_014_gap_magnitude_1260_014'], 'func': rev_base_universe_d3_011_rev_014_gap_magnitude_1260_014}


def rev_base_universe_d3_012_rev_015_open_close_pressure_1512_015(rev_base_universe_d2_012_rev_015_open_close_pressure_1512_015):
    return _base_universe_d3(rev_base_universe_d2_012_rev_015_open_close_pressure_1512_015, 12)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_012_rev_015_open_close_pressure_1512_015'] = {'inputs': ['rev_base_universe_d2_012_rev_015_open_close_pressure_1512_015'], 'func': rev_base_universe_d3_012_rev_015_open_close_pressure_1512_015}


def rev_base_universe_d3_013_rev_016_lower_wick_ratio_5_016(rev_base_universe_d2_013_rev_016_lower_wick_ratio_5_016):
    return _base_universe_d3(rev_base_universe_d2_013_rev_016_lower_wick_ratio_5_016, 13)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_013_rev_016_lower_wick_ratio_5_016'] = {'inputs': ['rev_base_universe_d2_013_rev_016_lower_wick_ratio_5_016'], 'func': rev_base_universe_d3_013_rev_016_lower_wick_ratio_5_016}


def rev_base_universe_d3_014_rev_017_upper_wick_ratio_10_017(rev_base_universe_d2_014_rev_017_upper_wick_ratio_10_017):
    return _base_universe_d3(rev_base_universe_d2_014_rev_017_upper_wick_ratio_10_017, 14)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_014_rev_017_upper_wick_ratio_10_017'] = {'inputs': ['rev_base_universe_d2_014_rev_017_upper_wick_ratio_10_017'], 'func': rev_base_universe_d3_014_rev_017_upper_wick_ratio_10_017}


def rev_base_universe_d3_015_rev_018_body_to_range_21_018(rev_base_universe_d2_015_rev_018_body_to_range_21_018):
    return _base_universe_d3(rev_base_universe_d2_015_rev_018_body_to_range_21_018, 15)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_015_rev_018_body_to_range_21_018'] = {'inputs': ['rev_base_universe_d2_015_rev_018_body_to_range_21_018'], 'func': rev_base_universe_d3_015_rev_018_body_to_range_21_018}


def rev_base_universe_d3_016_rev_020_gap_magnitude_63_020(rev_base_universe_d2_016_rev_020_gap_magnitude_63_020):
    return _base_universe_d3(rev_base_universe_d2_016_rev_020_gap_magnitude_63_020, 16)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_016_rev_020_gap_magnitude_63_020'] = {'inputs': ['rev_base_universe_d2_016_rev_020_gap_magnitude_63_020'], 'func': rev_base_universe_d3_016_rev_020_gap_magnitude_63_020}


def rev_base_universe_d3_017_rev_021_open_close_pressure_84_021(rev_base_universe_d2_017_rev_021_open_close_pressure_84_021):
    return _base_universe_d3(rev_base_universe_d2_017_rev_021_open_close_pressure_84_021, 17)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_017_rev_021_open_close_pressure_84_021'] = {'inputs': ['rev_base_universe_d2_017_rev_021_open_close_pressure_84_021'], 'func': rev_base_universe_d3_017_rev_021_open_close_pressure_84_021}


def rev_base_universe_d3_018_rev_022_lower_wick_ratio_126_022(rev_base_universe_d2_018_rev_022_lower_wick_ratio_126_022):
    return _base_universe_d3(rev_base_universe_d2_018_rev_022_lower_wick_ratio_126_022, 18)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_018_rev_022_lower_wick_ratio_126_022'] = {'inputs': ['rev_base_universe_d2_018_rev_022_lower_wick_ratio_126_022'], 'func': rev_base_universe_d3_018_rev_022_lower_wick_ratio_126_022}


def rev_base_universe_d3_019_rev_023_upper_wick_ratio_189_023(rev_base_universe_d2_019_rev_023_upper_wick_ratio_189_023):
    return _base_universe_d3(rev_base_universe_d2_019_rev_023_upper_wick_ratio_189_023, 19)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_019_rev_023_upper_wick_ratio_189_023'] = {'inputs': ['rev_base_universe_d2_019_rev_023_upper_wick_ratio_189_023'], 'func': rev_base_universe_d3_019_rev_023_upper_wick_ratio_189_023}


def rev_base_universe_d3_020_rev_024_body_to_range_252_024(rev_base_universe_d2_020_rev_024_body_to_range_252_024):
    return _base_universe_d3(rev_base_universe_d2_020_rev_024_body_to_range_252_024, 20)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_020_rev_024_body_to_range_252_024'] = {'inputs': ['rev_base_universe_d2_020_rev_024_body_to_range_252_024'], 'func': rev_base_universe_d3_020_rev_024_body_to_range_252_024}


def rev_base_universe_d3_021_rev_026_gap_magnitude_504_026(rev_base_universe_d2_021_rev_026_gap_magnitude_504_026):
    return _base_universe_d3(rev_base_universe_d2_021_rev_026_gap_magnitude_504_026, 21)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_021_rev_026_gap_magnitude_504_026'] = {'inputs': ['rev_base_universe_d2_021_rev_026_gap_magnitude_504_026'], 'func': rev_base_universe_d3_021_rev_026_gap_magnitude_504_026}


def rev_base_universe_d3_022_rev_027_open_close_pressure_756_027(rev_base_universe_d2_022_rev_027_open_close_pressure_756_027):
    return _base_universe_d3(rev_base_universe_d2_022_rev_027_open_close_pressure_756_027, 22)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_022_rev_027_open_close_pressure_756_027'] = {'inputs': ['rev_base_universe_d2_022_rev_027_open_close_pressure_756_027'], 'func': rev_base_universe_d3_022_rev_027_open_close_pressure_756_027}


def rev_base_universe_d3_023_rev_028_lower_wick_ratio_1008_028(rev_base_universe_d2_023_rev_028_lower_wick_ratio_1008_028):
    return _base_universe_d3(rev_base_universe_d2_023_rev_028_lower_wick_ratio_1008_028, 23)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_023_rev_028_lower_wick_ratio_1008_028'] = {'inputs': ['rev_base_universe_d2_023_rev_028_lower_wick_ratio_1008_028'], 'func': rev_base_universe_d3_023_rev_028_lower_wick_ratio_1008_028}


def rev_base_universe_d3_024_rev_029_upper_wick_ratio_1260_029(rev_base_universe_d2_024_rev_029_upper_wick_ratio_1260_029):
    return _base_universe_d3(rev_base_universe_d2_024_rev_029_upper_wick_ratio_1260_029, 24)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_024_rev_029_upper_wick_ratio_1260_029'] = {'inputs': ['rev_base_universe_d2_024_rev_029_upper_wick_ratio_1260_029'], 'func': rev_base_universe_d3_024_rev_029_upper_wick_ratio_1260_029}


def rev_base_universe_d3_025_rev_030_body_to_range_1512_030(rev_base_universe_d2_025_rev_030_body_to_range_1512_030):
    return _base_universe_d3(rev_base_universe_d2_025_rev_030_body_to_range_1512_030, 25)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_025_rev_030_body_to_range_1512_030'] = {'inputs': ['rev_base_universe_d2_025_rev_030_body_to_range_1512_030'], 'func': rev_base_universe_d3_025_rev_030_body_to_range_1512_030}


def rev_base_universe_d3_026_rev_basefill_031(rev_base_universe_d2_026_rev_basefill_031):
    return _base_universe_d3(rev_base_universe_d2_026_rev_basefill_031, 26)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_026_rev_basefill_031'] = {'inputs': ['rev_base_universe_d2_026_rev_basefill_031'], 'func': rev_base_universe_d3_026_rev_basefill_031}


def rev_base_universe_d3_027_rev_basefill_032(rev_base_universe_d2_027_rev_basefill_032):
    return _base_universe_d3(rev_base_universe_d2_027_rev_basefill_032, 27)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_027_rev_basefill_032'] = {'inputs': ['rev_base_universe_d2_027_rev_basefill_032'], 'func': rev_base_universe_d3_027_rev_basefill_032}


def rev_base_universe_d3_028_rev_basefill_033(rev_base_universe_d2_028_rev_basefill_033):
    return _base_universe_d3(rev_base_universe_d2_028_rev_basefill_033, 28)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_028_rev_basefill_033'] = {'inputs': ['rev_base_universe_d2_028_rev_basefill_033'], 'func': rev_base_universe_d3_028_rev_basefill_033}


def rev_base_universe_d3_029_rev_basefill_034(rev_base_universe_d2_029_rev_basefill_034):
    return _base_universe_d3(rev_base_universe_d2_029_rev_basefill_034, 29)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_029_rev_basefill_034'] = {'inputs': ['rev_base_universe_d2_029_rev_basefill_034'], 'func': rev_base_universe_d3_029_rev_basefill_034}


def rev_base_universe_d3_030_rev_basefill_035(rev_base_universe_d2_030_rev_basefill_035):
    return _base_universe_d3(rev_base_universe_d2_030_rev_basefill_035, 30)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_030_rev_basefill_035'] = {'inputs': ['rev_base_universe_d2_030_rev_basefill_035'], 'func': rev_base_universe_d3_030_rev_basefill_035}


def rev_base_universe_d3_031_rev_basefill_036(rev_base_universe_d2_031_rev_basefill_036):
    return _base_universe_d3(rev_base_universe_d2_031_rev_basefill_036, 31)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_031_rev_basefill_036'] = {'inputs': ['rev_base_universe_d2_031_rev_basefill_036'], 'func': rev_base_universe_d3_031_rev_basefill_036}


def rev_base_universe_d3_032_rev_basefill_037(rev_base_universe_d2_032_rev_basefill_037):
    return _base_universe_d3(rev_base_universe_d2_032_rev_basefill_037, 32)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_032_rev_basefill_037'] = {'inputs': ['rev_base_universe_d2_032_rev_basefill_037'], 'func': rev_base_universe_d3_032_rev_basefill_037}


def rev_base_universe_d3_033_rev_basefill_038(rev_base_universe_d2_033_rev_basefill_038):
    return _base_universe_d3(rev_base_universe_d2_033_rev_basefill_038, 33)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_033_rev_basefill_038'] = {'inputs': ['rev_base_universe_d2_033_rev_basefill_038'], 'func': rev_base_universe_d3_033_rev_basefill_038}


def rev_base_universe_d3_034_rev_basefill_039(rev_base_universe_d2_034_rev_basefill_039):
    return _base_universe_d3(rev_base_universe_d2_034_rev_basefill_039, 34)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_034_rev_basefill_039'] = {'inputs': ['rev_base_universe_d2_034_rev_basefill_039'], 'func': rev_base_universe_d3_034_rev_basefill_039}


def rev_base_universe_d3_035_rev_basefill_040(rev_base_universe_d2_035_rev_basefill_040):
    return _base_universe_d3(rev_base_universe_d2_035_rev_basefill_040, 35)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_035_rev_basefill_040'] = {'inputs': ['rev_base_universe_d2_035_rev_basefill_040'], 'func': rev_base_universe_d3_035_rev_basefill_040}


def rev_base_universe_d3_036_rev_basefill_041(rev_base_universe_d2_036_rev_basefill_041):
    return _base_universe_d3(rev_base_universe_d2_036_rev_basefill_041, 36)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_036_rev_basefill_041'] = {'inputs': ['rev_base_universe_d2_036_rev_basefill_041'], 'func': rev_base_universe_d3_036_rev_basefill_041}


def rev_base_universe_d3_037_rev_basefill_042(rev_base_universe_d2_037_rev_basefill_042):
    return _base_universe_d3(rev_base_universe_d2_037_rev_basefill_042, 37)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_037_rev_basefill_042'] = {'inputs': ['rev_base_universe_d2_037_rev_basefill_042'], 'func': rev_base_universe_d3_037_rev_basefill_042}


def rev_base_universe_d3_038_rev_basefill_043(rev_base_universe_d2_038_rev_basefill_043):
    return _base_universe_d3(rev_base_universe_d2_038_rev_basefill_043, 38)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_038_rev_basefill_043'] = {'inputs': ['rev_base_universe_d2_038_rev_basefill_043'], 'func': rev_base_universe_d3_038_rev_basefill_043}


def rev_base_universe_d3_039_rev_basefill_044(rev_base_universe_d2_039_rev_basefill_044):
    return _base_universe_d3(rev_base_universe_d2_039_rev_basefill_044, 39)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_039_rev_basefill_044'] = {'inputs': ['rev_base_universe_d2_039_rev_basefill_044'], 'func': rev_base_universe_d3_039_rev_basefill_044}


def rev_base_universe_d3_040_rev_basefill_045(rev_base_universe_d2_040_rev_basefill_045):
    return _base_universe_d3(rev_base_universe_d2_040_rev_basefill_045, 40)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_040_rev_basefill_045'] = {'inputs': ['rev_base_universe_d2_040_rev_basefill_045'], 'func': rev_base_universe_d3_040_rev_basefill_045}


def rev_base_universe_d3_041_rev_basefill_046(rev_base_universe_d2_041_rev_basefill_046):
    return _base_universe_d3(rev_base_universe_d2_041_rev_basefill_046, 41)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_041_rev_basefill_046'] = {'inputs': ['rev_base_universe_d2_041_rev_basefill_046'], 'func': rev_base_universe_d3_041_rev_basefill_046}


def rev_base_universe_d3_042_rev_basefill_047(rev_base_universe_d2_042_rev_basefill_047):
    return _base_universe_d3(rev_base_universe_d2_042_rev_basefill_047, 42)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_042_rev_basefill_047'] = {'inputs': ['rev_base_universe_d2_042_rev_basefill_047'], 'func': rev_base_universe_d3_042_rev_basefill_047}


def rev_base_universe_d3_043_rev_basefill_048(rev_base_universe_d2_043_rev_basefill_048):
    return _base_universe_d3(rev_base_universe_d2_043_rev_basefill_048, 43)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_043_rev_basefill_048'] = {'inputs': ['rev_base_universe_d2_043_rev_basefill_048'], 'func': rev_base_universe_d3_043_rev_basefill_048}


def rev_base_universe_d3_044_rev_basefill_049(rev_base_universe_d2_044_rev_basefill_049):
    return _base_universe_d3(rev_base_universe_d2_044_rev_basefill_049, 44)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_044_rev_basefill_049'] = {'inputs': ['rev_base_universe_d2_044_rev_basefill_049'], 'func': rev_base_universe_d3_044_rev_basefill_049}


def rev_base_universe_d3_045_rev_basefill_050(rev_base_universe_d2_045_rev_basefill_050):
    return _base_universe_d3(rev_base_universe_d2_045_rev_basefill_050, 45)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_045_rev_basefill_050'] = {'inputs': ['rev_base_universe_d2_045_rev_basefill_050'], 'func': rev_base_universe_d3_045_rev_basefill_050}


def rev_base_universe_d3_046_rev_basefill_051(rev_base_universe_d2_046_rev_basefill_051):
    return _base_universe_d3(rev_base_universe_d2_046_rev_basefill_051, 46)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_046_rev_basefill_051'] = {'inputs': ['rev_base_universe_d2_046_rev_basefill_051'], 'func': rev_base_universe_d3_046_rev_basefill_051}


def rev_base_universe_d3_047_rev_basefill_052(rev_base_universe_d2_047_rev_basefill_052):
    return _base_universe_d3(rev_base_universe_d2_047_rev_basefill_052, 47)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_047_rev_basefill_052'] = {'inputs': ['rev_base_universe_d2_047_rev_basefill_052'], 'func': rev_base_universe_d3_047_rev_basefill_052}


def rev_base_universe_d3_048_rev_basefill_053(rev_base_universe_d2_048_rev_basefill_053):
    return _base_universe_d3(rev_base_universe_d2_048_rev_basefill_053, 48)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_048_rev_basefill_053'] = {'inputs': ['rev_base_universe_d2_048_rev_basefill_053'], 'func': rev_base_universe_d3_048_rev_basefill_053}


def rev_base_universe_d3_049_rev_basefill_054(rev_base_universe_d2_049_rev_basefill_054):
    return _base_universe_d3(rev_base_universe_d2_049_rev_basefill_054, 49)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_049_rev_basefill_054'] = {'inputs': ['rev_base_universe_d2_049_rev_basefill_054'], 'func': rev_base_universe_d3_049_rev_basefill_054}


def rev_base_universe_d3_050_rev_basefill_055(rev_base_universe_d2_050_rev_basefill_055):
    return _base_universe_d3(rev_base_universe_d2_050_rev_basefill_055, 50)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_050_rev_basefill_055'] = {'inputs': ['rev_base_universe_d2_050_rev_basefill_055'], 'func': rev_base_universe_d3_050_rev_basefill_055}


def rev_base_universe_d3_051_rev_basefill_056(rev_base_universe_d2_051_rev_basefill_056):
    return _base_universe_d3(rev_base_universe_d2_051_rev_basefill_056, 51)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_051_rev_basefill_056'] = {'inputs': ['rev_base_universe_d2_051_rev_basefill_056'], 'func': rev_base_universe_d3_051_rev_basefill_056}


def rev_base_universe_d3_052_rev_basefill_057(rev_base_universe_d2_052_rev_basefill_057):
    return _base_universe_d3(rev_base_universe_d2_052_rev_basefill_057, 52)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_052_rev_basefill_057'] = {'inputs': ['rev_base_universe_d2_052_rev_basefill_057'], 'func': rev_base_universe_d3_052_rev_basefill_057}


def rev_base_universe_d3_053_rev_basefill_058(rev_base_universe_d2_053_rev_basefill_058):
    return _base_universe_d3(rev_base_universe_d2_053_rev_basefill_058, 53)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_053_rev_basefill_058'] = {'inputs': ['rev_base_universe_d2_053_rev_basefill_058'], 'func': rev_base_universe_d3_053_rev_basefill_058}


def rev_base_universe_d3_054_rev_basefill_059(rev_base_universe_d2_054_rev_basefill_059):
    return _base_universe_d3(rev_base_universe_d2_054_rev_basefill_059, 54)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_054_rev_basefill_059'] = {'inputs': ['rev_base_universe_d2_054_rev_basefill_059'], 'func': rev_base_universe_d3_054_rev_basefill_059}


def rev_base_universe_d3_055_rev_basefill_060(rev_base_universe_d2_055_rev_basefill_060):
    return _base_universe_d3(rev_base_universe_d2_055_rev_basefill_060, 55)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_055_rev_basefill_060'] = {'inputs': ['rev_base_universe_d2_055_rev_basefill_060'], 'func': rev_base_universe_d3_055_rev_basefill_060}


def rev_base_universe_d3_056_rev_basefill_061(rev_base_universe_d2_056_rev_basefill_061):
    return _base_universe_d3(rev_base_universe_d2_056_rev_basefill_061, 56)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_056_rev_basefill_061'] = {'inputs': ['rev_base_universe_d2_056_rev_basefill_061'], 'func': rev_base_universe_d3_056_rev_basefill_061}


def rev_base_universe_d3_057_rev_basefill_062(rev_base_universe_d2_057_rev_basefill_062):
    return _base_universe_d3(rev_base_universe_d2_057_rev_basefill_062, 57)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_057_rev_basefill_062'] = {'inputs': ['rev_base_universe_d2_057_rev_basefill_062'], 'func': rev_base_universe_d3_057_rev_basefill_062}


def rev_base_universe_d3_058_rev_basefill_063(rev_base_universe_d2_058_rev_basefill_063):
    return _base_universe_d3(rev_base_universe_d2_058_rev_basefill_063, 58)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_058_rev_basefill_063'] = {'inputs': ['rev_base_universe_d2_058_rev_basefill_063'], 'func': rev_base_universe_d3_058_rev_basefill_063}


def rev_base_universe_d3_059_rev_basefill_064(rev_base_universe_d2_059_rev_basefill_064):
    return _base_universe_d3(rev_base_universe_d2_059_rev_basefill_064, 59)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_059_rev_basefill_064'] = {'inputs': ['rev_base_universe_d2_059_rev_basefill_064'], 'func': rev_base_universe_d3_059_rev_basefill_064}


def rev_base_universe_d3_060_rev_basefill_065(rev_base_universe_d2_060_rev_basefill_065):
    return _base_universe_d3(rev_base_universe_d2_060_rev_basefill_065, 60)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_060_rev_basefill_065'] = {'inputs': ['rev_base_universe_d2_060_rev_basefill_065'], 'func': rev_base_universe_d3_060_rev_basefill_065}


def rev_base_universe_d3_061_rev_basefill_066(rev_base_universe_d2_061_rev_basefill_066):
    return _base_universe_d3(rev_base_universe_d2_061_rev_basefill_066, 61)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_061_rev_basefill_066'] = {'inputs': ['rev_base_universe_d2_061_rev_basefill_066'], 'func': rev_base_universe_d3_061_rev_basefill_066}


def rev_base_universe_d3_062_rev_basefill_067(rev_base_universe_d2_062_rev_basefill_067):
    return _base_universe_d3(rev_base_universe_d2_062_rev_basefill_067, 62)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_062_rev_basefill_067'] = {'inputs': ['rev_base_universe_d2_062_rev_basefill_067'], 'func': rev_base_universe_d3_062_rev_basefill_067}


def rev_base_universe_d3_063_rev_basefill_068(rev_base_universe_d2_063_rev_basefill_068):
    return _base_universe_d3(rev_base_universe_d2_063_rev_basefill_068, 63)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_063_rev_basefill_068'] = {'inputs': ['rev_base_universe_d2_063_rev_basefill_068'], 'func': rev_base_universe_d3_063_rev_basefill_068}


def rev_base_universe_d3_064_rev_basefill_069(rev_base_universe_d2_064_rev_basefill_069):
    return _base_universe_d3(rev_base_universe_d2_064_rev_basefill_069, 64)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_064_rev_basefill_069'] = {'inputs': ['rev_base_universe_d2_064_rev_basefill_069'], 'func': rev_base_universe_d3_064_rev_basefill_069}


def rev_base_universe_d3_065_rev_basefill_070(rev_base_universe_d2_065_rev_basefill_070):
    return _base_universe_d3(rev_base_universe_d2_065_rev_basefill_070, 65)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_065_rev_basefill_070'] = {'inputs': ['rev_base_universe_d2_065_rev_basefill_070'], 'func': rev_base_universe_d3_065_rev_basefill_070}


def rev_base_universe_d3_066_rev_basefill_071(rev_base_universe_d2_066_rev_basefill_071):
    return _base_universe_d3(rev_base_universe_d2_066_rev_basefill_071, 66)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_066_rev_basefill_071'] = {'inputs': ['rev_base_universe_d2_066_rev_basefill_071'], 'func': rev_base_universe_d3_066_rev_basefill_071}


def rev_base_universe_d3_067_rev_basefill_072(rev_base_universe_d2_067_rev_basefill_072):
    return _base_universe_d3(rev_base_universe_d2_067_rev_basefill_072, 67)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_067_rev_basefill_072'] = {'inputs': ['rev_base_universe_d2_067_rev_basefill_072'], 'func': rev_base_universe_d3_067_rev_basefill_072}


def rev_base_universe_d3_068_rev_basefill_073(rev_base_universe_d2_068_rev_basefill_073):
    return _base_universe_d3(rev_base_universe_d2_068_rev_basefill_073, 68)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_068_rev_basefill_073'] = {'inputs': ['rev_base_universe_d2_068_rev_basefill_073'], 'func': rev_base_universe_d3_068_rev_basefill_073}


def rev_base_universe_d3_069_rev_basefill_074(rev_base_universe_d2_069_rev_basefill_074):
    return _base_universe_d3(rev_base_universe_d2_069_rev_basefill_074, 69)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_069_rev_basefill_074'] = {'inputs': ['rev_base_universe_d2_069_rev_basefill_074'], 'func': rev_base_universe_d3_069_rev_basefill_074}


def rev_base_universe_d3_070_rev_basefill_075(rev_base_universe_d2_070_rev_basefill_075):
    return _base_universe_d3(rev_base_universe_d2_070_rev_basefill_075, 70)
REV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rev_base_universe_d3_070_rev_basefill_075'] = {'inputs': ['rev_base_universe_d2_070_rev_basefill_075'], 'func': rev_base_universe_d3_070_rev_basefill_075}
