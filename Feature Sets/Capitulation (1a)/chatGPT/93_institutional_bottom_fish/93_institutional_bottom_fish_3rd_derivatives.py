import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


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



def ibf_176_ibf_001_holder_exit_1_accel_1(ibf_151_ibf_001_holder_exit_1_roc_1):
    feature = _s(ibf_151_ibf_001_holder_exit_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def ibf_177_ibf_007_holder_exit_1_accel_42(ibf_152_ibf_007_holder_exit_1_roc_42):
    feature = _s(ibf_152_ibf_007_holder_exit_1_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def ibf_178_ibf_013_holder_exit_1_accel_126(ibf_153_ibf_013_holder_exit_1_roc_126):
    feature = _s(ibf_153_ibf_013_holder_exit_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def ibf_179_ibf_019_holder_exit_1_accel_378(ibf_154_ibf_019_holder_exit_1_roc_378):
    feature = _s(ibf_154_ibf_019_holder_exit_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def ibf_180_ibf_025_holder_exit_1_accel_4(ibf_155_ibf_025_holder_exit_1_roc_4):
    feature = _s(ibf_155_ibf_025_holder_exit_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















INSTITUTIONAL_BOTTOM_FISH_REGISTRY_3RD_DERIVATIVES = {
    'ibf_176_ibf_001_holder_exit_1_accel_1': {'inputs': ['ibf_151_ibf_001_holder_exit_1_roc_1'], 'func': ibf_176_ibf_001_holder_exit_1_accel_1},
    'ibf_177_ibf_007_holder_exit_1_accel_42': {'inputs': ['ibf_152_ibf_007_holder_exit_1_roc_42'], 'func': ibf_177_ibf_007_holder_exit_1_accel_42},
    'ibf_178_ibf_013_holder_exit_1_accel_126': {'inputs': ['ibf_153_ibf_013_holder_exit_1_roc_126'], 'func': ibf_178_ibf_013_holder_exit_1_accel_126},
    'ibf_179_ibf_019_holder_exit_1_accel_378': {'inputs': ['ibf_154_ibf_019_holder_exit_1_roc_378'], 'func': ibf_179_ibf_019_holder_exit_1_accel_378},
    'ibf_180_ibf_025_holder_exit_1_accel_4': {'inputs': ['ibf_155_ibf_025_holder_exit_1_roc_4'], 'func': ibf_180_ibf_025_holder_exit_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ibf_replacement_d3_001(ibf_replacement_d2_001):
    feature = _clean(ibf_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_001'] = {'inputs': ['ibf_replacement_d2_001'], 'func': ibf_replacement_d3_001}


def ibf_replacement_d3_002(ibf_replacement_d2_002):
    feature = _clean(ibf_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_002'] = {'inputs': ['ibf_replacement_d2_002'], 'func': ibf_replacement_d3_002}


def ibf_replacement_d3_003(ibf_replacement_d2_003):
    feature = _clean(ibf_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_003'] = {'inputs': ['ibf_replacement_d2_003'], 'func': ibf_replacement_d3_003}


def ibf_replacement_d3_004(ibf_replacement_d2_004):
    feature = _clean(ibf_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_004'] = {'inputs': ['ibf_replacement_d2_004'], 'func': ibf_replacement_d3_004}


def ibf_replacement_d3_005(ibf_replacement_d2_005):
    feature = _clean(ibf_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_005'] = {'inputs': ['ibf_replacement_d2_005'], 'func': ibf_replacement_d3_005}


def ibf_replacement_d3_006(ibf_replacement_d2_006):
    feature = _clean(ibf_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_006'] = {'inputs': ['ibf_replacement_d2_006'], 'func': ibf_replacement_d3_006}


def ibf_replacement_d3_007(ibf_replacement_d2_007):
    feature = _clean(ibf_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_007'] = {'inputs': ['ibf_replacement_d2_007'], 'func': ibf_replacement_d3_007}


def ibf_replacement_d3_008(ibf_replacement_d2_008):
    feature = _clean(ibf_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_008'] = {'inputs': ['ibf_replacement_d2_008'], 'func': ibf_replacement_d3_008}


def ibf_replacement_d3_009(ibf_replacement_d2_009):
    feature = _clean(ibf_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_009'] = {'inputs': ['ibf_replacement_d2_009'], 'func': ibf_replacement_d3_009}


def ibf_replacement_d3_010(ibf_replacement_d2_010):
    feature = _clean(ibf_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_010'] = {'inputs': ['ibf_replacement_d2_010'], 'func': ibf_replacement_d3_010}


def ibf_replacement_d3_011(ibf_replacement_d2_011):
    feature = _clean(ibf_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_011'] = {'inputs': ['ibf_replacement_d2_011'], 'func': ibf_replacement_d3_011}


def ibf_replacement_d3_012(ibf_replacement_d2_012):
    feature = _clean(ibf_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_012'] = {'inputs': ['ibf_replacement_d2_012'], 'func': ibf_replacement_d3_012}


def ibf_replacement_d3_013(ibf_replacement_d2_013):
    feature = _clean(ibf_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_013'] = {'inputs': ['ibf_replacement_d2_013'], 'func': ibf_replacement_d3_013}


def ibf_replacement_d3_014(ibf_replacement_d2_014):
    feature = _clean(ibf_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_014'] = {'inputs': ['ibf_replacement_d2_014'], 'func': ibf_replacement_d3_014}


def ibf_replacement_d3_015(ibf_replacement_d2_015):
    feature = _clean(ibf_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_015'] = {'inputs': ['ibf_replacement_d2_015'], 'func': ibf_replacement_d3_015}


def ibf_replacement_d3_016(ibf_replacement_d2_016):
    feature = _clean(ibf_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_016'] = {'inputs': ['ibf_replacement_d2_016'], 'func': ibf_replacement_d3_016}


def ibf_replacement_d3_017(ibf_replacement_d2_017):
    feature = _clean(ibf_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_017'] = {'inputs': ['ibf_replacement_d2_017'], 'func': ibf_replacement_d3_017}


def ibf_replacement_d3_018(ibf_replacement_d2_018):
    feature = _clean(ibf_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_018'] = {'inputs': ['ibf_replacement_d2_018'], 'func': ibf_replacement_d3_018}


def ibf_replacement_d3_019(ibf_replacement_d2_019):
    feature = _clean(ibf_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_019'] = {'inputs': ['ibf_replacement_d2_019'], 'func': ibf_replacement_d3_019}


def ibf_replacement_d3_020(ibf_replacement_d2_020):
    feature = _clean(ibf_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_020'] = {'inputs': ['ibf_replacement_d2_020'], 'func': ibf_replacement_d3_020}


def ibf_replacement_d3_021(ibf_replacement_d2_021):
    feature = _clean(ibf_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_021'] = {'inputs': ['ibf_replacement_d2_021'], 'func': ibf_replacement_d3_021}


def ibf_replacement_d3_022(ibf_replacement_d2_022):
    feature = _clean(ibf_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_022'] = {'inputs': ['ibf_replacement_d2_022'], 'func': ibf_replacement_d3_022}


def ibf_replacement_d3_023(ibf_replacement_d2_023):
    feature = _clean(ibf_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_023'] = {'inputs': ['ibf_replacement_d2_023'], 'func': ibf_replacement_d3_023}


def ibf_replacement_d3_024(ibf_replacement_d2_024):
    feature = _clean(ibf_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_024'] = {'inputs': ['ibf_replacement_d2_024'], 'func': ibf_replacement_d3_024}


def ibf_replacement_d3_025(ibf_replacement_d2_025):
    feature = _clean(ibf_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_025'] = {'inputs': ['ibf_replacement_d2_025'], 'func': ibf_replacement_d3_025}


def ibf_replacement_d3_026(ibf_replacement_d2_026):
    feature = _clean(ibf_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_026'] = {'inputs': ['ibf_replacement_d2_026'], 'func': ibf_replacement_d3_026}


def ibf_replacement_d3_027(ibf_replacement_d2_027):
    feature = _clean(ibf_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_027'] = {'inputs': ['ibf_replacement_d2_027'], 'func': ibf_replacement_d3_027}


def ibf_replacement_d3_028(ibf_replacement_d2_028):
    feature = _clean(ibf_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_028'] = {'inputs': ['ibf_replacement_d2_028'], 'func': ibf_replacement_d3_028}


def ibf_replacement_d3_029(ibf_replacement_d2_029):
    feature = _clean(ibf_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_029'] = {'inputs': ['ibf_replacement_d2_029'], 'func': ibf_replacement_d3_029}


def ibf_replacement_d3_030(ibf_replacement_d2_030):
    feature = _clean(ibf_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_030'] = {'inputs': ['ibf_replacement_d2_030'], 'func': ibf_replacement_d3_030}


def ibf_replacement_d3_031(ibf_replacement_d2_031):
    feature = _clean(ibf_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_031'] = {'inputs': ['ibf_replacement_d2_031'], 'func': ibf_replacement_d3_031}


def ibf_replacement_d3_032(ibf_replacement_d2_032):
    feature = _clean(ibf_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_032'] = {'inputs': ['ibf_replacement_d2_032'], 'func': ibf_replacement_d3_032}


def ibf_replacement_d3_033(ibf_replacement_d2_033):
    feature = _clean(ibf_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_033'] = {'inputs': ['ibf_replacement_d2_033'], 'func': ibf_replacement_d3_033}


def ibf_replacement_d3_034(ibf_replacement_d2_034):
    feature = _clean(ibf_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_034'] = {'inputs': ['ibf_replacement_d2_034'], 'func': ibf_replacement_d3_034}


def ibf_replacement_d3_035(ibf_replacement_d2_035):
    feature = _clean(ibf_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_035'] = {'inputs': ['ibf_replacement_d2_035'], 'func': ibf_replacement_d3_035}


def ibf_replacement_d3_036(ibf_replacement_d2_036):
    feature = _clean(ibf_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_036'] = {'inputs': ['ibf_replacement_d2_036'], 'func': ibf_replacement_d3_036}


def ibf_replacement_d3_037(ibf_replacement_d2_037):
    feature = _clean(ibf_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_037'] = {'inputs': ['ibf_replacement_d2_037'], 'func': ibf_replacement_d3_037}


def ibf_replacement_d3_038(ibf_replacement_d2_038):
    feature = _clean(ibf_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_038'] = {'inputs': ['ibf_replacement_d2_038'], 'func': ibf_replacement_d3_038}


def ibf_replacement_d3_039(ibf_replacement_d2_039):
    feature = _clean(ibf_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_039'] = {'inputs': ['ibf_replacement_d2_039'], 'func': ibf_replacement_d3_039}


def ibf_replacement_d3_040(ibf_replacement_d2_040):
    feature = _clean(ibf_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_040'] = {'inputs': ['ibf_replacement_d2_040'], 'func': ibf_replacement_d3_040}


def ibf_replacement_d3_041(ibf_replacement_d2_041):
    feature = _clean(ibf_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_041'] = {'inputs': ['ibf_replacement_d2_041'], 'func': ibf_replacement_d3_041}


def ibf_replacement_d3_042(ibf_replacement_d2_042):
    feature = _clean(ibf_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_042'] = {'inputs': ['ibf_replacement_d2_042'], 'func': ibf_replacement_d3_042}


def ibf_replacement_d3_043(ibf_replacement_d2_043):
    feature = _clean(ibf_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_043'] = {'inputs': ['ibf_replacement_d2_043'], 'func': ibf_replacement_d3_043}


def ibf_replacement_d3_044(ibf_replacement_d2_044):
    feature = _clean(ibf_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_044'] = {'inputs': ['ibf_replacement_d2_044'], 'func': ibf_replacement_d3_044}


def ibf_replacement_d3_045(ibf_replacement_d2_045):
    feature = _clean(ibf_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_045'] = {'inputs': ['ibf_replacement_d2_045'], 'func': ibf_replacement_d3_045}


def ibf_replacement_d3_046(ibf_replacement_d2_046):
    feature = _clean(ibf_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_046'] = {'inputs': ['ibf_replacement_d2_046'], 'func': ibf_replacement_d3_046}


def ibf_replacement_d3_047(ibf_replacement_d2_047):
    feature = _clean(ibf_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_047'] = {'inputs': ['ibf_replacement_d2_047'], 'func': ibf_replacement_d3_047}


def ibf_replacement_d3_048(ibf_replacement_d2_048):
    feature = _clean(ibf_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_048'] = {'inputs': ['ibf_replacement_d2_048'], 'func': ibf_replacement_d3_048}


def ibf_replacement_d3_049(ibf_replacement_d2_049):
    feature = _clean(ibf_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_049'] = {'inputs': ['ibf_replacement_d2_049'], 'func': ibf_replacement_d3_049}


def ibf_replacement_d3_050(ibf_replacement_d2_050):
    feature = _clean(ibf_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_050'] = {'inputs': ['ibf_replacement_d2_050'], 'func': ibf_replacement_d3_050}


def ibf_replacement_d3_051(ibf_replacement_d2_051):
    feature = _clean(ibf_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_051'] = {'inputs': ['ibf_replacement_d2_051'], 'func': ibf_replacement_d3_051}


def ibf_replacement_d3_052(ibf_replacement_d2_052):
    feature = _clean(ibf_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_052'] = {'inputs': ['ibf_replacement_d2_052'], 'func': ibf_replacement_d3_052}


def ibf_replacement_d3_053(ibf_replacement_d2_053):
    feature = _clean(ibf_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_053'] = {'inputs': ['ibf_replacement_d2_053'], 'func': ibf_replacement_d3_053}


def ibf_replacement_d3_054(ibf_replacement_d2_054):
    feature = _clean(ibf_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_054'] = {'inputs': ['ibf_replacement_d2_054'], 'func': ibf_replacement_d3_054}


def ibf_replacement_d3_055(ibf_replacement_d2_055):
    feature = _clean(ibf_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_055'] = {'inputs': ['ibf_replacement_d2_055'], 'func': ibf_replacement_d3_055}


def ibf_replacement_d3_056(ibf_replacement_d2_056):
    feature = _clean(ibf_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_056'] = {'inputs': ['ibf_replacement_d2_056'], 'func': ibf_replacement_d3_056}


def ibf_replacement_d3_057(ibf_replacement_d2_057):
    feature = _clean(ibf_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_057'] = {'inputs': ['ibf_replacement_d2_057'], 'func': ibf_replacement_d3_057}


def ibf_replacement_d3_058(ibf_replacement_d2_058):
    feature = _clean(ibf_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_058'] = {'inputs': ['ibf_replacement_d2_058'], 'func': ibf_replacement_d3_058}


def ibf_replacement_d3_059(ibf_replacement_d2_059):
    feature = _clean(ibf_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_059'] = {'inputs': ['ibf_replacement_d2_059'], 'func': ibf_replacement_d3_059}


def ibf_replacement_d3_060(ibf_replacement_d2_060):
    feature = _clean(ibf_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_060'] = {'inputs': ['ibf_replacement_d2_060'], 'func': ibf_replacement_d3_060}


def ibf_replacement_d3_061(ibf_replacement_d2_061):
    feature = _clean(ibf_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_061'] = {'inputs': ['ibf_replacement_d2_061'], 'func': ibf_replacement_d3_061}


def ibf_replacement_d3_062(ibf_replacement_d2_062):
    feature = _clean(ibf_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_062'] = {'inputs': ['ibf_replacement_d2_062'], 'func': ibf_replacement_d3_062}


def ibf_replacement_d3_063(ibf_replacement_d2_063):
    feature = _clean(ibf_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_063'] = {'inputs': ['ibf_replacement_d2_063'], 'func': ibf_replacement_d3_063}


def ibf_replacement_d3_064(ibf_replacement_d2_064):
    feature = _clean(ibf_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_064'] = {'inputs': ['ibf_replacement_d2_064'], 'func': ibf_replacement_d3_064}


def ibf_replacement_d3_065(ibf_replacement_d2_065):
    feature = _clean(ibf_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_065'] = {'inputs': ['ibf_replacement_d2_065'], 'func': ibf_replacement_d3_065}


def ibf_replacement_d3_066(ibf_replacement_d2_066):
    feature = _clean(ibf_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_066'] = {'inputs': ['ibf_replacement_d2_066'], 'func': ibf_replacement_d3_066}


def ibf_replacement_d3_067(ibf_replacement_d2_067):
    feature = _clean(ibf_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_067'] = {'inputs': ['ibf_replacement_d2_067'], 'func': ibf_replacement_d3_067}


def ibf_replacement_d3_068(ibf_replacement_d2_068):
    feature = _clean(ibf_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_068'] = {'inputs': ['ibf_replacement_d2_068'], 'func': ibf_replacement_d3_068}


def ibf_replacement_d3_069(ibf_replacement_d2_069):
    feature = _clean(ibf_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_069'] = {'inputs': ['ibf_replacement_d2_069'], 'func': ibf_replacement_d3_069}


def ibf_replacement_d3_070(ibf_replacement_d2_070):
    feature = _clean(ibf_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_070'] = {'inputs': ['ibf_replacement_d2_070'], 'func': ibf_replacement_d3_070}


def ibf_replacement_d3_071(ibf_replacement_d2_071):
    feature = _clean(ibf_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_071'] = {'inputs': ['ibf_replacement_d2_071'], 'func': ibf_replacement_d3_071}


def ibf_replacement_d3_072(ibf_replacement_d2_072):
    feature = _clean(ibf_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_072'] = {'inputs': ['ibf_replacement_d2_072'], 'func': ibf_replacement_d3_072}


def ibf_replacement_d3_073(ibf_replacement_d2_073):
    feature = _clean(ibf_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_073'] = {'inputs': ['ibf_replacement_d2_073'], 'func': ibf_replacement_d3_073}


def ibf_replacement_d3_074(ibf_replacement_d2_074):
    feature = _clean(ibf_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_074'] = {'inputs': ['ibf_replacement_d2_074'], 'func': ibf_replacement_d3_074}


def ibf_replacement_d3_075(ibf_replacement_d2_075):
    feature = _clean(ibf_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_075'] = {'inputs': ['ibf_replacement_d2_075'], 'func': ibf_replacement_d3_075}


def ibf_replacement_d3_076(ibf_replacement_d2_076):
    feature = _clean(ibf_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_076'] = {'inputs': ['ibf_replacement_d2_076'], 'func': ibf_replacement_d3_076}


def ibf_replacement_d3_077(ibf_replacement_d2_077):
    feature = _clean(ibf_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_077'] = {'inputs': ['ibf_replacement_d2_077'], 'func': ibf_replacement_d3_077}


def ibf_replacement_d3_078(ibf_replacement_d2_078):
    feature = _clean(ibf_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_078'] = {'inputs': ['ibf_replacement_d2_078'], 'func': ibf_replacement_d3_078}


def ibf_replacement_d3_079(ibf_replacement_d2_079):
    feature = _clean(ibf_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_079'] = {'inputs': ['ibf_replacement_d2_079'], 'func': ibf_replacement_d3_079}


def ibf_replacement_d3_080(ibf_replacement_d2_080):
    feature = _clean(ibf_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_080'] = {'inputs': ['ibf_replacement_d2_080'], 'func': ibf_replacement_d3_080}


def ibf_replacement_d3_081(ibf_replacement_d2_081):
    feature = _clean(ibf_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_081'] = {'inputs': ['ibf_replacement_d2_081'], 'func': ibf_replacement_d3_081}


def ibf_replacement_d3_082(ibf_replacement_d2_082):
    feature = _clean(ibf_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_082'] = {'inputs': ['ibf_replacement_d2_082'], 'func': ibf_replacement_d3_082}


def ibf_replacement_d3_083(ibf_replacement_d2_083):
    feature = _clean(ibf_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_083'] = {'inputs': ['ibf_replacement_d2_083'], 'func': ibf_replacement_d3_083}


def ibf_replacement_d3_084(ibf_replacement_d2_084):
    feature = _clean(ibf_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_084'] = {'inputs': ['ibf_replacement_d2_084'], 'func': ibf_replacement_d3_084}


def ibf_replacement_d3_085(ibf_replacement_d2_085):
    feature = _clean(ibf_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_085'] = {'inputs': ['ibf_replacement_d2_085'], 'func': ibf_replacement_d3_085}


def ibf_replacement_d3_086(ibf_replacement_d2_086):
    feature = _clean(ibf_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_086'] = {'inputs': ['ibf_replacement_d2_086'], 'func': ibf_replacement_d3_086}


def ibf_replacement_d3_087(ibf_replacement_d2_087):
    feature = _clean(ibf_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_087'] = {'inputs': ['ibf_replacement_d2_087'], 'func': ibf_replacement_d3_087}


def ibf_replacement_d3_088(ibf_replacement_d2_088):
    feature = _clean(ibf_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_088'] = {'inputs': ['ibf_replacement_d2_088'], 'func': ibf_replacement_d3_088}


def ibf_replacement_d3_089(ibf_replacement_d2_089):
    feature = _clean(ibf_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_089'] = {'inputs': ['ibf_replacement_d2_089'], 'func': ibf_replacement_d3_089}


def ibf_replacement_d3_090(ibf_replacement_d2_090):
    feature = _clean(ibf_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_090'] = {'inputs': ['ibf_replacement_d2_090'], 'func': ibf_replacement_d3_090}


def ibf_replacement_d3_091(ibf_replacement_d2_091):
    feature = _clean(ibf_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_091'] = {'inputs': ['ibf_replacement_d2_091'], 'func': ibf_replacement_d3_091}


def ibf_replacement_d3_092(ibf_replacement_d2_092):
    feature = _clean(ibf_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_092'] = {'inputs': ['ibf_replacement_d2_092'], 'func': ibf_replacement_d3_092}


def ibf_replacement_d3_093(ibf_replacement_d2_093):
    feature = _clean(ibf_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_093'] = {'inputs': ['ibf_replacement_d2_093'], 'func': ibf_replacement_d3_093}


def ibf_replacement_d3_094(ibf_replacement_d2_094):
    feature = _clean(ibf_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_094'] = {'inputs': ['ibf_replacement_d2_094'], 'func': ibf_replacement_d3_094}


def ibf_replacement_d3_095(ibf_replacement_d2_095):
    feature = _clean(ibf_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_095'] = {'inputs': ['ibf_replacement_d2_095'], 'func': ibf_replacement_d3_095}


def ibf_replacement_d3_096(ibf_replacement_d2_096):
    feature = _clean(ibf_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_096'] = {'inputs': ['ibf_replacement_d2_096'], 'func': ibf_replacement_d3_096}


def ibf_replacement_d3_097(ibf_replacement_d2_097):
    feature = _clean(ibf_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_097'] = {'inputs': ['ibf_replacement_d2_097'], 'func': ibf_replacement_d3_097}


def ibf_replacement_d3_098(ibf_replacement_d2_098):
    feature = _clean(ibf_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_098'] = {'inputs': ['ibf_replacement_d2_098'], 'func': ibf_replacement_d3_098}


def ibf_replacement_d3_099(ibf_replacement_d2_099):
    feature = _clean(ibf_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_099'] = {'inputs': ['ibf_replacement_d2_099'], 'func': ibf_replacement_d3_099}


def ibf_replacement_d3_100(ibf_replacement_d2_100):
    feature = _clean(ibf_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_100'] = {'inputs': ['ibf_replacement_d2_100'], 'func': ibf_replacement_d3_100}


def ibf_replacement_d3_101(ibf_replacement_d2_101):
    feature = _clean(ibf_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_101'] = {'inputs': ['ibf_replacement_d2_101'], 'func': ibf_replacement_d3_101}


def ibf_replacement_d3_102(ibf_replacement_d2_102):
    feature = _clean(ibf_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_102'] = {'inputs': ['ibf_replacement_d2_102'], 'func': ibf_replacement_d3_102}


def ibf_replacement_d3_103(ibf_replacement_d2_103):
    feature = _clean(ibf_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_103'] = {'inputs': ['ibf_replacement_d2_103'], 'func': ibf_replacement_d3_103}


def ibf_replacement_d3_104(ibf_replacement_d2_104):
    feature = _clean(ibf_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_104'] = {'inputs': ['ibf_replacement_d2_104'], 'func': ibf_replacement_d3_104}


def ibf_replacement_d3_105(ibf_replacement_d2_105):
    feature = _clean(ibf_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_105'] = {'inputs': ['ibf_replacement_d2_105'], 'func': ibf_replacement_d3_105}


def ibf_replacement_d3_106(ibf_replacement_d2_106):
    feature = _clean(ibf_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_106'] = {'inputs': ['ibf_replacement_d2_106'], 'func': ibf_replacement_d3_106}


def ibf_replacement_d3_107(ibf_replacement_d2_107):
    feature = _clean(ibf_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_107'] = {'inputs': ['ibf_replacement_d2_107'], 'func': ibf_replacement_d3_107}


def ibf_replacement_d3_108(ibf_replacement_d2_108):
    feature = _clean(ibf_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_108'] = {'inputs': ['ibf_replacement_d2_108'], 'func': ibf_replacement_d3_108}


def ibf_replacement_d3_109(ibf_replacement_d2_109):
    feature = _clean(ibf_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_109'] = {'inputs': ['ibf_replacement_d2_109'], 'func': ibf_replacement_d3_109}


def ibf_replacement_d3_110(ibf_replacement_d2_110):
    feature = _clean(ibf_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_110'] = {'inputs': ['ibf_replacement_d2_110'], 'func': ibf_replacement_d3_110}


def ibf_replacement_d3_111(ibf_replacement_d2_111):
    feature = _clean(ibf_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_111'] = {'inputs': ['ibf_replacement_d2_111'], 'func': ibf_replacement_d3_111}


def ibf_replacement_d3_112(ibf_replacement_d2_112):
    feature = _clean(ibf_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_112'] = {'inputs': ['ibf_replacement_d2_112'], 'func': ibf_replacement_d3_112}


def ibf_replacement_d3_113(ibf_replacement_d2_113):
    feature = _clean(ibf_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_113'] = {'inputs': ['ibf_replacement_d2_113'], 'func': ibf_replacement_d3_113}


def ibf_replacement_d3_114(ibf_replacement_d2_114):
    feature = _clean(ibf_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_114'] = {'inputs': ['ibf_replacement_d2_114'], 'func': ibf_replacement_d3_114}


def ibf_replacement_d3_115(ibf_replacement_d2_115):
    feature = _clean(ibf_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_115'] = {'inputs': ['ibf_replacement_d2_115'], 'func': ibf_replacement_d3_115}


def ibf_replacement_d3_116(ibf_replacement_d2_116):
    feature = _clean(ibf_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_116'] = {'inputs': ['ibf_replacement_d2_116'], 'func': ibf_replacement_d3_116}


def ibf_replacement_d3_117(ibf_replacement_d2_117):
    feature = _clean(ibf_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_117'] = {'inputs': ['ibf_replacement_d2_117'], 'func': ibf_replacement_d3_117}


def ibf_replacement_d3_118(ibf_replacement_d2_118):
    feature = _clean(ibf_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_118'] = {'inputs': ['ibf_replacement_d2_118'], 'func': ibf_replacement_d3_118}


def ibf_replacement_d3_119(ibf_replacement_d2_119):
    feature = _clean(ibf_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_119'] = {'inputs': ['ibf_replacement_d2_119'], 'func': ibf_replacement_d3_119}


def ibf_replacement_d3_120(ibf_replacement_d2_120):
    feature = _clean(ibf_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_120'] = {'inputs': ['ibf_replacement_d2_120'], 'func': ibf_replacement_d3_120}


def ibf_replacement_d3_121(ibf_replacement_d2_121):
    feature = _clean(ibf_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_121'] = {'inputs': ['ibf_replacement_d2_121'], 'func': ibf_replacement_d3_121}


def ibf_replacement_d3_122(ibf_replacement_d2_122):
    feature = _clean(ibf_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_122'] = {'inputs': ['ibf_replacement_d2_122'], 'func': ibf_replacement_d3_122}


def ibf_replacement_d3_123(ibf_replacement_d2_123):
    feature = _clean(ibf_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_123'] = {'inputs': ['ibf_replacement_d2_123'], 'func': ibf_replacement_d3_123}


def ibf_replacement_d3_124(ibf_replacement_d2_124):
    feature = _clean(ibf_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_124'] = {'inputs': ['ibf_replacement_d2_124'], 'func': ibf_replacement_d3_124}


def ibf_replacement_d3_125(ibf_replacement_d2_125):
    feature = _clean(ibf_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_125'] = {'inputs': ['ibf_replacement_d2_125'], 'func': ibf_replacement_d3_125}


def ibf_replacement_d3_126(ibf_replacement_d2_126):
    feature = _clean(ibf_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_126'] = {'inputs': ['ibf_replacement_d2_126'], 'func': ibf_replacement_d3_126}


def ibf_replacement_d3_127(ibf_replacement_d2_127):
    feature = _clean(ibf_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_127'] = {'inputs': ['ibf_replacement_d2_127'], 'func': ibf_replacement_d3_127}


def ibf_replacement_d3_128(ibf_replacement_d2_128):
    feature = _clean(ibf_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_128'] = {'inputs': ['ibf_replacement_d2_128'], 'func': ibf_replacement_d3_128}


def ibf_replacement_d3_129(ibf_replacement_d2_129):
    feature = _clean(ibf_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_129'] = {'inputs': ['ibf_replacement_d2_129'], 'func': ibf_replacement_d3_129}


def ibf_replacement_d3_130(ibf_replacement_d2_130):
    feature = _clean(ibf_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_130'] = {'inputs': ['ibf_replacement_d2_130'], 'func': ibf_replacement_d3_130}


def ibf_replacement_d3_131(ibf_replacement_d2_131):
    feature = _clean(ibf_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_131'] = {'inputs': ['ibf_replacement_d2_131'], 'func': ibf_replacement_d3_131}


def ibf_replacement_d3_132(ibf_replacement_d2_132):
    feature = _clean(ibf_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_132'] = {'inputs': ['ibf_replacement_d2_132'], 'func': ibf_replacement_d3_132}


def ibf_replacement_d3_133(ibf_replacement_d2_133):
    feature = _clean(ibf_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_133'] = {'inputs': ['ibf_replacement_d2_133'], 'func': ibf_replacement_d3_133}


def ibf_replacement_d3_134(ibf_replacement_d2_134):
    feature = _clean(ibf_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_134'] = {'inputs': ['ibf_replacement_d2_134'], 'func': ibf_replacement_d3_134}


def ibf_replacement_d3_135(ibf_replacement_d2_135):
    feature = _clean(ibf_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_135'] = {'inputs': ['ibf_replacement_d2_135'], 'func': ibf_replacement_d3_135}


def ibf_replacement_d3_136(ibf_replacement_d2_136):
    feature = _clean(ibf_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_136'] = {'inputs': ['ibf_replacement_d2_136'], 'func': ibf_replacement_d3_136}


def ibf_replacement_d3_137(ibf_replacement_d2_137):
    feature = _clean(ibf_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_137'] = {'inputs': ['ibf_replacement_d2_137'], 'func': ibf_replacement_d3_137}


def ibf_replacement_d3_138(ibf_replacement_d2_138):
    feature = _clean(ibf_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_138'] = {'inputs': ['ibf_replacement_d2_138'], 'func': ibf_replacement_d3_138}


def ibf_replacement_d3_139(ibf_replacement_d2_139):
    feature = _clean(ibf_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_139'] = {'inputs': ['ibf_replacement_d2_139'], 'func': ibf_replacement_d3_139}


def ibf_replacement_d3_140(ibf_replacement_d2_140):
    feature = _clean(ibf_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_140'] = {'inputs': ['ibf_replacement_d2_140'], 'func': ibf_replacement_d3_140}


def ibf_replacement_d3_141(ibf_replacement_d2_141):
    feature = _clean(ibf_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_141'] = {'inputs': ['ibf_replacement_d2_141'], 'func': ibf_replacement_d3_141}


def ibf_replacement_d3_142(ibf_replacement_d2_142):
    feature = _clean(ibf_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_142'] = {'inputs': ['ibf_replacement_d2_142'], 'func': ibf_replacement_d3_142}


def ibf_replacement_d3_143(ibf_replacement_d2_143):
    feature = _clean(ibf_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_143'] = {'inputs': ['ibf_replacement_d2_143'], 'func': ibf_replacement_d3_143}


def ibf_replacement_d3_144(ibf_replacement_d2_144):
    feature = _clean(ibf_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_144'] = {'inputs': ['ibf_replacement_d2_144'], 'func': ibf_replacement_d3_144}


def ibf_replacement_d3_145(ibf_replacement_d2_145):
    feature = _clean(ibf_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_145'] = {'inputs': ['ibf_replacement_d2_145'], 'func': ibf_replacement_d3_145}


def ibf_replacement_d3_146(ibf_replacement_d2_146):
    feature = _clean(ibf_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_146'] = {'inputs': ['ibf_replacement_d2_146'], 'func': ibf_replacement_d3_146}


def ibf_replacement_d3_147(ibf_replacement_d2_147):
    feature = _clean(ibf_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_147'] = {'inputs': ['ibf_replacement_d2_147'], 'func': ibf_replacement_d3_147}


def ibf_replacement_d3_148(ibf_replacement_d2_148):
    feature = _clean(ibf_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_148'] = {'inputs': ['ibf_replacement_d2_148'], 'func': ibf_replacement_d3_148}


def ibf_replacement_d3_149(ibf_replacement_d2_149):
    feature = _clean(ibf_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_149'] = {'inputs': ['ibf_replacement_d2_149'], 'func': ibf_replacement_d3_149}


def ibf_replacement_d3_150(ibf_replacement_d2_150):
    feature = _clean(ibf_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_150'] = {'inputs': ['ibf_replacement_d2_150'], 'func': ibf_replacement_d3_150}


def ibf_replacement_d3_151(ibf_replacement_d2_151):
    feature = _clean(ibf_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_151'] = {'inputs': ['ibf_replacement_d2_151'], 'func': ibf_replacement_d3_151}


def ibf_replacement_d3_152(ibf_replacement_d2_152):
    feature = _clean(ibf_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_152'] = {'inputs': ['ibf_replacement_d2_152'], 'func': ibf_replacement_d3_152}


def ibf_replacement_d3_153(ibf_replacement_d2_153):
    feature = _clean(ibf_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_153'] = {'inputs': ['ibf_replacement_d2_153'], 'func': ibf_replacement_d3_153}


def ibf_replacement_d3_154(ibf_replacement_d2_154):
    feature = _clean(ibf_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_154'] = {'inputs': ['ibf_replacement_d2_154'], 'func': ibf_replacement_d3_154}


def ibf_replacement_d3_155(ibf_replacement_d2_155):
    feature = _clean(ibf_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_155'] = {'inputs': ['ibf_replacement_d2_155'], 'func': ibf_replacement_d3_155}


def ibf_replacement_d3_156(ibf_replacement_d2_156):
    feature = _clean(ibf_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_156'] = {'inputs': ['ibf_replacement_d2_156'], 'func': ibf_replacement_d3_156}


def ibf_replacement_d3_157(ibf_replacement_d2_157):
    feature = _clean(ibf_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_157'] = {'inputs': ['ibf_replacement_d2_157'], 'func': ibf_replacement_d3_157}


def ibf_replacement_d3_158(ibf_replacement_d2_158):
    feature = _clean(ibf_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_158'] = {'inputs': ['ibf_replacement_d2_158'], 'func': ibf_replacement_d3_158}


def ibf_replacement_d3_159(ibf_replacement_d2_159):
    feature = _clean(ibf_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_159'] = {'inputs': ['ibf_replacement_d2_159'], 'func': ibf_replacement_d3_159}


def ibf_replacement_d3_160(ibf_replacement_d2_160):
    feature = _clean(ibf_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_160'] = {'inputs': ['ibf_replacement_d2_160'], 'func': ibf_replacement_d3_160}


def ibf_replacement_d3_161(ibf_replacement_d2_161):
    feature = _clean(ibf_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_161'] = {'inputs': ['ibf_replacement_d2_161'], 'func': ibf_replacement_d3_161}


def ibf_replacement_d3_162(ibf_replacement_d2_162):
    feature = _clean(ibf_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_162'] = {'inputs': ['ibf_replacement_d2_162'], 'func': ibf_replacement_d3_162}


def ibf_replacement_d3_163(ibf_replacement_d2_163):
    feature = _clean(ibf_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_163'] = {'inputs': ['ibf_replacement_d2_163'], 'func': ibf_replacement_d3_163}


def ibf_replacement_d3_164(ibf_replacement_d2_164):
    feature = _clean(ibf_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_164'] = {'inputs': ['ibf_replacement_d2_164'], 'func': ibf_replacement_d3_164}


def ibf_replacement_d3_165(ibf_replacement_d2_165):
    feature = _clean(ibf_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_165'] = {'inputs': ['ibf_replacement_d2_165'], 'func': ibf_replacement_d3_165}


def ibf_replacement_d3_166(ibf_replacement_d2_166):
    feature = _clean(ibf_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_166'] = {'inputs': ['ibf_replacement_d2_166'], 'func': ibf_replacement_d3_166}


def ibf_replacement_d3_167(ibf_replacement_d2_167):
    feature = _clean(ibf_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_167'] = {'inputs': ['ibf_replacement_d2_167'], 'func': ibf_replacement_d3_167}


def ibf_replacement_d3_168(ibf_replacement_d2_168):
    feature = _clean(ibf_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_168'] = {'inputs': ['ibf_replacement_d2_168'], 'func': ibf_replacement_d3_168}


def ibf_replacement_d3_169(ibf_replacement_d2_169):
    feature = _clean(ibf_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_169'] = {'inputs': ['ibf_replacement_d2_169'], 'func': ibf_replacement_d3_169}


def ibf_replacement_d3_170(ibf_replacement_d2_170):
    feature = _clean(ibf_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
IBF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibf_replacement_d3_170'] = {'inputs': ['ibf_replacement_d2_170'], 'func': ibf_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ibf_base_universe_d3_001_ibf_003_top_holder_concentration_63(ibf_base_universe_d2_001_ibf_003_top_holder_concentration_63):
    return _base_universe_d3(ibf_base_universe_d2_001_ibf_003_top_holder_concentration_63, 1)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_001_ibf_003_top_holder_concentration_63'] = {'inputs': ['ibf_base_universe_d2_001_ibf_003_top_holder_concentration_63'], 'func': ibf_base_universe_d3_001_ibf_003_top_holder_concentration_63}


def ibf_base_universe_d3_002_ibf_004_institutional_net_flow_84(ibf_base_universe_d2_002_ibf_004_institutional_net_flow_84):
    return _base_universe_d3(ibf_base_universe_d2_002_ibf_004_institutional_net_flow_84, 2)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_002_ibf_004_institutional_net_flow_84'] = {'inputs': ['ibf_base_universe_d2_002_ibf_004_institutional_net_flow_84'], 'func': ibf_base_universe_d3_002_ibf_004_institutional_net_flow_84}


def ibf_base_universe_d3_003_ibf_005_forced_selling_pressure_126(ibf_base_universe_d2_003_ibf_005_forced_selling_pressure_126):
    return _base_universe_d3(ibf_base_universe_d2_003_ibf_005_forced_selling_pressure_126, 3)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_003_ibf_005_forced_selling_pressure_126'] = {'inputs': ['ibf_base_universe_d2_003_ibf_005_forced_selling_pressure_126'], 'func': ibf_base_universe_d3_003_ibf_005_forced_selling_pressure_126}


def ibf_base_universe_d3_004_ibf_006_holder_base_volatility_189(ibf_base_universe_d2_004_ibf_006_holder_base_volatility_189):
    return _base_universe_d3(ibf_base_universe_d2_004_ibf_006_holder_base_volatility_189, 4)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_004_ibf_006_holder_base_volatility_189'] = {'inputs': ['ibf_base_universe_d2_004_ibf_006_holder_base_volatility_189'], 'func': ibf_base_universe_d3_004_ibf_006_holder_base_volatility_189}


def ibf_base_universe_d3_005_ibf_009_top_holder_concentration_504(ibf_base_universe_d2_005_ibf_009_top_holder_concentration_504):
    return _base_universe_d3(ibf_base_universe_d2_005_ibf_009_top_holder_concentration_504, 5)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_005_ibf_009_top_holder_concentration_504'] = {'inputs': ['ibf_base_universe_d2_005_ibf_009_top_holder_concentration_504'], 'func': ibf_base_universe_d3_005_ibf_009_top_holder_concentration_504}


def ibf_base_universe_d3_006_ibf_010_institutional_net_flow_756(ibf_base_universe_d2_006_ibf_010_institutional_net_flow_756):
    return _base_universe_d3(ibf_base_universe_d2_006_ibf_010_institutional_net_flow_756, 6)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_006_ibf_010_institutional_net_flow_756'] = {'inputs': ['ibf_base_universe_d2_006_ibf_010_institutional_net_flow_756'], 'func': ibf_base_universe_d3_006_ibf_010_institutional_net_flow_756}


def ibf_base_universe_d3_007_ibf_011_forced_selling_pressure_1008(ibf_base_universe_d2_007_ibf_011_forced_selling_pressure_1008):
    return _base_universe_d3(ibf_base_universe_d2_007_ibf_011_forced_selling_pressure_1008, 7)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_007_ibf_011_forced_selling_pressure_1008'] = {'inputs': ['ibf_base_universe_d2_007_ibf_011_forced_selling_pressure_1008'], 'func': ibf_base_universe_d3_007_ibf_011_forced_selling_pressure_1008}


def ibf_base_universe_d3_008_ibf_012_holder_base_volatility_1260(ibf_base_universe_d2_008_ibf_012_holder_base_volatility_1260):
    return _base_universe_d3(ibf_base_universe_d2_008_ibf_012_holder_base_volatility_1260, 8)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_008_ibf_012_holder_base_volatility_1260'] = {'inputs': ['ibf_base_universe_d2_008_ibf_012_holder_base_volatility_1260'], 'func': ibf_base_universe_d3_008_ibf_012_holder_base_volatility_1260}


def ibf_base_universe_d3_009_ibf_015_top_holder_concentration_252(ibf_base_universe_d2_009_ibf_015_top_holder_concentration_252):
    return _base_universe_d3(ibf_base_universe_d2_009_ibf_015_top_holder_concentration_252, 9)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_009_ibf_015_top_holder_concentration_252'] = {'inputs': ['ibf_base_universe_d2_009_ibf_015_top_holder_concentration_252'], 'func': ibf_base_universe_d3_009_ibf_015_top_holder_concentration_252}


def ibf_base_universe_d3_010_ibf_016_institutional_net_flow_21(ibf_base_universe_d2_010_ibf_016_institutional_net_flow_21):
    return _base_universe_d3(ibf_base_universe_d2_010_ibf_016_institutional_net_flow_21, 10)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_010_ibf_016_institutional_net_flow_21'] = {'inputs': ['ibf_base_universe_d2_010_ibf_016_institutional_net_flow_21'], 'func': ibf_base_universe_d3_010_ibf_016_institutional_net_flow_21}


def ibf_base_universe_d3_011_ibf_017_forced_selling_pressure_42(ibf_base_universe_d2_011_ibf_017_forced_selling_pressure_42):
    return _base_universe_d3(ibf_base_universe_d2_011_ibf_017_forced_selling_pressure_42, 11)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_011_ibf_017_forced_selling_pressure_42'] = {'inputs': ['ibf_base_universe_d2_011_ibf_017_forced_selling_pressure_42'], 'func': ibf_base_universe_d3_011_ibf_017_forced_selling_pressure_42}


def ibf_base_universe_d3_012_ibf_018_holder_base_volatility_63(ibf_base_universe_d2_012_ibf_018_holder_base_volatility_63):
    return _base_universe_d3(ibf_base_universe_d2_012_ibf_018_holder_base_volatility_63, 12)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_012_ibf_018_holder_base_volatility_63'] = {'inputs': ['ibf_base_universe_d2_012_ibf_018_holder_base_volatility_63'], 'func': ibf_base_universe_d3_012_ibf_018_holder_base_volatility_63}


def ibf_base_universe_d3_013_ibf_021_top_holder_concentration_189(ibf_base_universe_d2_013_ibf_021_top_holder_concentration_189):
    return _base_universe_d3(ibf_base_universe_d2_013_ibf_021_top_holder_concentration_189, 13)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_013_ibf_021_top_holder_concentration_189'] = {'inputs': ['ibf_base_universe_d2_013_ibf_021_top_holder_concentration_189'], 'func': ibf_base_universe_d3_013_ibf_021_top_holder_concentration_189}


def ibf_base_universe_d3_014_ibf_022_institutional_net_flow_252(ibf_base_universe_d2_014_ibf_022_institutional_net_flow_252):
    return _base_universe_d3(ibf_base_universe_d2_014_ibf_022_institutional_net_flow_252, 14)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_014_ibf_022_institutional_net_flow_252'] = {'inputs': ['ibf_base_universe_d2_014_ibf_022_institutional_net_flow_252'], 'func': ibf_base_universe_d3_014_ibf_022_institutional_net_flow_252}


def ibf_base_universe_d3_015_ibf_023_forced_selling_pressure_378(ibf_base_universe_d2_015_ibf_023_forced_selling_pressure_378):
    return _base_universe_d3(ibf_base_universe_d2_015_ibf_023_forced_selling_pressure_378, 15)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_015_ibf_023_forced_selling_pressure_378'] = {'inputs': ['ibf_base_universe_d2_015_ibf_023_forced_selling_pressure_378'], 'func': ibf_base_universe_d3_015_ibf_023_forced_selling_pressure_378}


def ibf_base_universe_d3_016_ibf_024_holder_base_volatility_504(ibf_base_universe_d2_016_ibf_024_holder_base_volatility_504):
    return _base_universe_d3(ibf_base_universe_d2_016_ibf_024_holder_base_volatility_504, 16)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_016_ibf_024_holder_base_volatility_504'] = {'inputs': ['ibf_base_universe_d2_016_ibf_024_holder_base_volatility_504'], 'func': ibf_base_universe_d3_016_ibf_024_holder_base_volatility_504}


def ibf_base_universe_d3_017_ibf_027_top_holder_concentration_1260(ibf_base_universe_d2_017_ibf_027_top_holder_concentration_1260):
    return _base_universe_d3(ibf_base_universe_d2_017_ibf_027_top_holder_concentration_1260, 17)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_017_ibf_027_top_holder_concentration_1260'] = {'inputs': ['ibf_base_universe_d2_017_ibf_027_top_holder_concentration_1260'], 'func': ibf_base_universe_d3_017_ibf_027_top_holder_concentration_1260}


def ibf_base_universe_d3_018_ibf_028_institutional_net_flow_1512(ibf_base_universe_d2_018_ibf_028_institutional_net_flow_1512):
    return _base_universe_d3(ibf_base_universe_d2_018_ibf_028_institutional_net_flow_1512, 18)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_018_ibf_028_institutional_net_flow_1512'] = {'inputs': ['ibf_base_universe_d2_018_ibf_028_institutional_net_flow_1512'], 'func': ibf_base_universe_d3_018_ibf_028_institutional_net_flow_1512}


def ibf_base_universe_d3_019_ibf_029_forced_selling_pressure_63(ibf_base_universe_d2_019_ibf_029_forced_selling_pressure_63):
    return _base_universe_d3(ibf_base_universe_d2_019_ibf_029_forced_selling_pressure_63, 19)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_019_ibf_029_forced_selling_pressure_63'] = {'inputs': ['ibf_base_universe_d2_019_ibf_029_forced_selling_pressure_63'], 'func': ibf_base_universe_d3_019_ibf_029_forced_selling_pressure_63}


def ibf_base_universe_d3_020_ibf_030_holder_base_volatility_252(ibf_base_universe_d2_020_ibf_030_holder_base_volatility_252):
    return _base_universe_d3(ibf_base_universe_d2_020_ibf_030_holder_base_volatility_252, 20)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_020_ibf_030_holder_base_volatility_252'] = {'inputs': ['ibf_base_universe_d2_020_ibf_030_holder_base_volatility_252'], 'func': ibf_base_universe_d3_020_ibf_030_holder_base_volatility_252}


def ibf_base_universe_d3_021_ibf_basefill_001(ibf_base_universe_d2_021_ibf_basefill_001):
    return _base_universe_d3(ibf_base_universe_d2_021_ibf_basefill_001, 21)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_021_ibf_basefill_001'] = {'inputs': ['ibf_base_universe_d2_021_ibf_basefill_001'], 'func': ibf_base_universe_d3_021_ibf_basefill_001}


def ibf_base_universe_d3_022_ibf_basefill_002(ibf_base_universe_d2_022_ibf_basefill_002):
    return _base_universe_d3(ibf_base_universe_d2_022_ibf_basefill_002, 22)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_022_ibf_basefill_002'] = {'inputs': ['ibf_base_universe_d2_022_ibf_basefill_002'], 'func': ibf_base_universe_d3_022_ibf_basefill_002}


def ibf_base_universe_d3_023_ibf_basefill_007(ibf_base_universe_d2_023_ibf_basefill_007):
    return _base_universe_d3(ibf_base_universe_d2_023_ibf_basefill_007, 23)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_023_ibf_basefill_007'] = {'inputs': ['ibf_base_universe_d2_023_ibf_basefill_007'], 'func': ibf_base_universe_d3_023_ibf_basefill_007}


def ibf_base_universe_d3_024_ibf_basefill_008(ibf_base_universe_d2_024_ibf_basefill_008):
    return _base_universe_d3(ibf_base_universe_d2_024_ibf_basefill_008, 24)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_024_ibf_basefill_008'] = {'inputs': ['ibf_base_universe_d2_024_ibf_basefill_008'], 'func': ibf_base_universe_d3_024_ibf_basefill_008}


def ibf_base_universe_d3_025_ibf_basefill_013(ibf_base_universe_d2_025_ibf_basefill_013):
    return _base_universe_d3(ibf_base_universe_d2_025_ibf_basefill_013, 25)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_025_ibf_basefill_013'] = {'inputs': ['ibf_base_universe_d2_025_ibf_basefill_013'], 'func': ibf_base_universe_d3_025_ibf_basefill_013}


def ibf_base_universe_d3_026_ibf_basefill_014(ibf_base_universe_d2_026_ibf_basefill_014):
    return _base_universe_d3(ibf_base_universe_d2_026_ibf_basefill_014, 26)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_026_ibf_basefill_014'] = {'inputs': ['ibf_base_universe_d2_026_ibf_basefill_014'], 'func': ibf_base_universe_d3_026_ibf_basefill_014}


def ibf_base_universe_d3_027_ibf_basefill_019(ibf_base_universe_d2_027_ibf_basefill_019):
    return _base_universe_d3(ibf_base_universe_d2_027_ibf_basefill_019, 27)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_027_ibf_basefill_019'] = {'inputs': ['ibf_base_universe_d2_027_ibf_basefill_019'], 'func': ibf_base_universe_d3_027_ibf_basefill_019}


def ibf_base_universe_d3_028_ibf_basefill_020(ibf_base_universe_d2_028_ibf_basefill_020):
    return _base_universe_d3(ibf_base_universe_d2_028_ibf_basefill_020, 28)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_028_ibf_basefill_020'] = {'inputs': ['ibf_base_universe_d2_028_ibf_basefill_020'], 'func': ibf_base_universe_d3_028_ibf_basefill_020}


def ibf_base_universe_d3_029_ibf_basefill_025(ibf_base_universe_d2_029_ibf_basefill_025):
    return _base_universe_d3(ibf_base_universe_d2_029_ibf_basefill_025, 29)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_029_ibf_basefill_025'] = {'inputs': ['ibf_base_universe_d2_029_ibf_basefill_025'], 'func': ibf_base_universe_d3_029_ibf_basefill_025}


def ibf_base_universe_d3_030_ibf_basefill_026(ibf_base_universe_d2_030_ibf_basefill_026):
    return _base_universe_d3(ibf_base_universe_d2_030_ibf_basefill_026, 30)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_030_ibf_basefill_026'] = {'inputs': ['ibf_base_universe_d2_030_ibf_basefill_026'], 'func': ibf_base_universe_d3_030_ibf_basefill_026}


def ibf_base_universe_d3_031_ibf_basefill_031(ibf_base_universe_d2_031_ibf_basefill_031):
    return _base_universe_d3(ibf_base_universe_d2_031_ibf_basefill_031, 31)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_031_ibf_basefill_031'] = {'inputs': ['ibf_base_universe_d2_031_ibf_basefill_031'], 'func': ibf_base_universe_d3_031_ibf_basefill_031}


def ibf_base_universe_d3_032_ibf_basefill_032(ibf_base_universe_d2_032_ibf_basefill_032):
    return _base_universe_d3(ibf_base_universe_d2_032_ibf_basefill_032, 32)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_032_ibf_basefill_032'] = {'inputs': ['ibf_base_universe_d2_032_ibf_basefill_032'], 'func': ibf_base_universe_d3_032_ibf_basefill_032}


def ibf_base_universe_d3_033_ibf_basefill_033(ibf_base_universe_d2_033_ibf_basefill_033):
    return _base_universe_d3(ibf_base_universe_d2_033_ibf_basefill_033, 33)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_033_ibf_basefill_033'] = {'inputs': ['ibf_base_universe_d2_033_ibf_basefill_033'], 'func': ibf_base_universe_d3_033_ibf_basefill_033}


def ibf_base_universe_d3_034_ibf_basefill_034(ibf_base_universe_d2_034_ibf_basefill_034):
    return _base_universe_d3(ibf_base_universe_d2_034_ibf_basefill_034, 34)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_034_ibf_basefill_034'] = {'inputs': ['ibf_base_universe_d2_034_ibf_basefill_034'], 'func': ibf_base_universe_d3_034_ibf_basefill_034}


def ibf_base_universe_d3_035_ibf_basefill_035(ibf_base_universe_d2_035_ibf_basefill_035):
    return _base_universe_d3(ibf_base_universe_d2_035_ibf_basefill_035, 35)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_035_ibf_basefill_035'] = {'inputs': ['ibf_base_universe_d2_035_ibf_basefill_035'], 'func': ibf_base_universe_d3_035_ibf_basefill_035}


def ibf_base_universe_d3_036_ibf_basefill_036(ibf_base_universe_d2_036_ibf_basefill_036):
    return _base_universe_d3(ibf_base_universe_d2_036_ibf_basefill_036, 36)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_036_ibf_basefill_036'] = {'inputs': ['ibf_base_universe_d2_036_ibf_basefill_036'], 'func': ibf_base_universe_d3_036_ibf_basefill_036}


def ibf_base_universe_d3_037_ibf_basefill_037(ibf_base_universe_d2_037_ibf_basefill_037):
    return _base_universe_d3(ibf_base_universe_d2_037_ibf_basefill_037, 37)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_037_ibf_basefill_037'] = {'inputs': ['ibf_base_universe_d2_037_ibf_basefill_037'], 'func': ibf_base_universe_d3_037_ibf_basefill_037}


def ibf_base_universe_d3_038_ibf_basefill_038(ibf_base_universe_d2_038_ibf_basefill_038):
    return _base_universe_d3(ibf_base_universe_d2_038_ibf_basefill_038, 38)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_038_ibf_basefill_038'] = {'inputs': ['ibf_base_universe_d2_038_ibf_basefill_038'], 'func': ibf_base_universe_d3_038_ibf_basefill_038}


def ibf_base_universe_d3_039_ibf_basefill_039(ibf_base_universe_d2_039_ibf_basefill_039):
    return _base_universe_d3(ibf_base_universe_d2_039_ibf_basefill_039, 39)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_039_ibf_basefill_039'] = {'inputs': ['ibf_base_universe_d2_039_ibf_basefill_039'], 'func': ibf_base_universe_d3_039_ibf_basefill_039}


def ibf_base_universe_d3_040_ibf_basefill_040(ibf_base_universe_d2_040_ibf_basefill_040):
    return _base_universe_d3(ibf_base_universe_d2_040_ibf_basefill_040, 40)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_040_ibf_basefill_040'] = {'inputs': ['ibf_base_universe_d2_040_ibf_basefill_040'], 'func': ibf_base_universe_d3_040_ibf_basefill_040}


def ibf_base_universe_d3_041_ibf_basefill_041(ibf_base_universe_d2_041_ibf_basefill_041):
    return _base_universe_d3(ibf_base_universe_d2_041_ibf_basefill_041, 41)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_041_ibf_basefill_041'] = {'inputs': ['ibf_base_universe_d2_041_ibf_basefill_041'], 'func': ibf_base_universe_d3_041_ibf_basefill_041}


def ibf_base_universe_d3_042_ibf_basefill_042(ibf_base_universe_d2_042_ibf_basefill_042):
    return _base_universe_d3(ibf_base_universe_d2_042_ibf_basefill_042, 42)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_042_ibf_basefill_042'] = {'inputs': ['ibf_base_universe_d2_042_ibf_basefill_042'], 'func': ibf_base_universe_d3_042_ibf_basefill_042}


def ibf_base_universe_d3_043_ibf_basefill_043(ibf_base_universe_d2_043_ibf_basefill_043):
    return _base_universe_d3(ibf_base_universe_d2_043_ibf_basefill_043, 43)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_043_ibf_basefill_043'] = {'inputs': ['ibf_base_universe_d2_043_ibf_basefill_043'], 'func': ibf_base_universe_d3_043_ibf_basefill_043}


def ibf_base_universe_d3_044_ibf_basefill_044(ibf_base_universe_d2_044_ibf_basefill_044):
    return _base_universe_d3(ibf_base_universe_d2_044_ibf_basefill_044, 44)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_044_ibf_basefill_044'] = {'inputs': ['ibf_base_universe_d2_044_ibf_basefill_044'], 'func': ibf_base_universe_d3_044_ibf_basefill_044}


def ibf_base_universe_d3_045_ibf_basefill_045(ibf_base_universe_d2_045_ibf_basefill_045):
    return _base_universe_d3(ibf_base_universe_d2_045_ibf_basefill_045, 45)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_045_ibf_basefill_045'] = {'inputs': ['ibf_base_universe_d2_045_ibf_basefill_045'], 'func': ibf_base_universe_d3_045_ibf_basefill_045}


def ibf_base_universe_d3_046_ibf_basefill_046(ibf_base_universe_d2_046_ibf_basefill_046):
    return _base_universe_d3(ibf_base_universe_d2_046_ibf_basefill_046, 46)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_046_ibf_basefill_046'] = {'inputs': ['ibf_base_universe_d2_046_ibf_basefill_046'], 'func': ibf_base_universe_d3_046_ibf_basefill_046}


def ibf_base_universe_d3_047_ibf_basefill_047(ibf_base_universe_d2_047_ibf_basefill_047):
    return _base_universe_d3(ibf_base_universe_d2_047_ibf_basefill_047, 47)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_047_ibf_basefill_047'] = {'inputs': ['ibf_base_universe_d2_047_ibf_basefill_047'], 'func': ibf_base_universe_d3_047_ibf_basefill_047}


def ibf_base_universe_d3_048_ibf_basefill_048(ibf_base_universe_d2_048_ibf_basefill_048):
    return _base_universe_d3(ibf_base_universe_d2_048_ibf_basefill_048, 48)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_048_ibf_basefill_048'] = {'inputs': ['ibf_base_universe_d2_048_ibf_basefill_048'], 'func': ibf_base_universe_d3_048_ibf_basefill_048}


def ibf_base_universe_d3_049_ibf_basefill_049(ibf_base_universe_d2_049_ibf_basefill_049):
    return _base_universe_d3(ibf_base_universe_d2_049_ibf_basefill_049, 49)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_049_ibf_basefill_049'] = {'inputs': ['ibf_base_universe_d2_049_ibf_basefill_049'], 'func': ibf_base_universe_d3_049_ibf_basefill_049}


def ibf_base_universe_d3_050_ibf_basefill_050(ibf_base_universe_d2_050_ibf_basefill_050):
    return _base_universe_d3(ibf_base_universe_d2_050_ibf_basefill_050, 50)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_050_ibf_basefill_050'] = {'inputs': ['ibf_base_universe_d2_050_ibf_basefill_050'], 'func': ibf_base_universe_d3_050_ibf_basefill_050}


def ibf_base_universe_d3_051_ibf_basefill_051(ibf_base_universe_d2_051_ibf_basefill_051):
    return _base_universe_d3(ibf_base_universe_d2_051_ibf_basefill_051, 51)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_051_ibf_basefill_051'] = {'inputs': ['ibf_base_universe_d2_051_ibf_basefill_051'], 'func': ibf_base_universe_d3_051_ibf_basefill_051}


def ibf_base_universe_d3_052_ibf_basefill_052(ibf_base_universe_d2_052_ibf_basefill_052):
    return _base_universe_d3(ibf_base_universe_d2_052_ibf_basefill_052, 52)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_052_ibf_basefill_052'] = {'inputs': ['ibf_base_universe_d2_052_ibf_basefill_052'], 'func': ibf_base_universe_d3_052_ibf_basefill_052}


def ibf_base_universe_d3_053_ibf_basefill_053(ibf_base_universe_d2_053_ibf_basefill_053):
    return _base_universe_d3(ibf_base_universe_d2_053_ibf_basefill_053, 53)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_053_ibf_basefill_053'] = {'inputs': ['ibf_base_universe_d2_053_ibf_basefill_053'], 'func': ibf_base_universe_d3_053_ibf_basefill_053}


def ibf_base_universe_d3_054_ibf_basefill_054(ibf_base_universe_d2_054_ibf_basefill_054):
    return _base_universe_d3(ibf_base_universe_d2_054_ibf_basefill_054, 54)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_054_ibf_basefill_054'] = {'inputs': ['ibf_base_universe_d2_054_ibf_basefill_054'], 'func': ibf_base_universe_d3_054_ibf_basefill_054}


def ibf_base_universe_d3_055_ibf_basefill_055(ibf_base_universe_d2_055_ibf_basefill_055):
    return _base_universe_d3(ibf_base_universe_d2_055_ibf_basefill_055, 55)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_055_ibf_basefill_055'] = {'inputs': ['ibf_base_universe_d2_055_ibf_basefill_055'], 'func': ibf_base_universe_d3_055_ibf_basefill_055}


def ibf_base_universe_d3_056_ibf_basefill_056(ibf_base_universe_d2_056_ibf_basefill_056):
    return _base_universe_d3(ibf_base_universe_d2_056_ibf_basefill_056, 56)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_056_ibf_basefill_056'] = {'inputs': ['ibf_base_universe_d2_056_ibf_basefill_056'], 'func': ibf_base_universe_d3_056_ibf_basefill_056}


def ibf_base_universe_d3_057_ibf_basefill_057(ibf_base_universe_d2_057_ibf_basefill_057):
    return _base_universe_d3(ibf_base_universe_d2_057_ibf_basefill_057, 57)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_057_ibf_basefill_057'] = {'inputs': ['ibf_base_universe_d2_057_ibf_basefill_057'], 'func': ibf_base_universe_d3_057_ibf_basefill_057}


def ibf_base_universe_d3_058_ibf_basefill_058(ibf_base_universe_d2_058_ibf_basefill_058):
    return _base_universe_d3(ibf_base_universe_d2_058_ibf_basefill_058, 58)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_058_ibf_basefill_058'] = {'inputs': ['ibf_base_universe_d2_058_ibf_basefill_058'], 'func': ibf_base_universe_d3_058_ibf_basefill_058}


def ibf_base_universe_d3_059_ibf_basefill_059(ibf_base_universe_d2_059_ibf_basefill_059):
    return _base_universe_d3(ibf_base_universe_d2_059_ibf_basefill_059, 59)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_059_ibf_basefill_059'] = {'inputs': ['ibf_base_universe_d2_059_ibf_basefill_059'], 'func': ibf_base_universe_d3_059_ibf_basefill_059}


def ibf_base_universe_d3_060_ibf_basefill_060(ibf_base_universe_d2_060_ibf_basefill_060):
    return _base_universe_d3(ibf_base_universe_d2_060_ibf_basefill_060, 60)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_060_ibf_basefill_060'] = {'inputs': ['ibf_base_universe_d2_060_ibf_basefill_060'], 'func': ibf_base_universe_d3_060_ibf_basefill_060}


def ibf_base_universe_d3_061_ibf_basefill_061(ibf_base_universe_d2_061_ibf_basefill_061):
    return _base_universe_d3(ibf_base_universe_d2_061_ibf_basefill_061, 61)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_061_ibf_basefill_061'] = {'inputs': ['ibf_base_universe_d2_061_ibf_basefill_061'], 'func': ibf_base_universe_d3_061_ibf_basefill_061}


def ibf_base_universe_d3_062_ibf_basefill_062(ibf_base_universe_d2_062_ibf_basefill_062):
    return _base_universe_d3(ibf_base_universe_d2_062_ibf_basefill_062, 62)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_062_ibf_basefill_062'] = {'inputs': ['ibf_base_universe_d2_062_ibf_basefill_062'], 'func': ibf_base_universe_d3_062_ibf_basefill_062}


def ibf_base_universe_d3_063_ibf_basefill_063(ibf_base_universe_d2_063_ibf_basefill_063):
    return _base_universe_d3(ibf_base_universe_d2_063_ibf_basefill_063, 63)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_063_ibf_basefill_063'] = {'inputs': ['ibf_base_universe_d2_063_ibf_basefill_063'], 'func': ibf_base_universe_d3_063_ibf_basefill_063}


def ibf_base_universe_d3_064_ibf_basefill_064(ibf_base_universe_d2_064_ibf_basefill_064):
    return _base_universe_d3(ibf_base_universe_d2_064_ibf_basefill_064, 64)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_064_ibf_basefill_064'] = {'inputs': ['ibf_base_universe_d2_064_ibf_basefill_064'], 'func': ibf_base_universe_d3_064_ibf_basefill_064}


def ibf_base_universe_d3_065_ibf_basefill_065(ibf_base_universe_d2_065_ibf_basefill_065):
    return _base_universe_d3(ibf_base_universe_d2_065_ibf_basefill_065, 65)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_065_ibf_basefill_065'] = {'inputs': ['ibf_base_universe_d2_065_ibf_basefill_065'], 'func': ibf_base_universe_d3_065_ibf_basefill_065}


def ibf_base_universe_d3_066_ibf_basefill_066(ibf_base_universe_d2_066_ibf_basefill_066):
    return _base_universe_d3(ibf_base_universe_d2_066_ibf_basefill_066, 66)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_066_ibf_basefill_066'] = {'inputs': ['ibf_base_universe_d2_066_ibf_basefill_066'], 'func': ibf_base_universe_d3_066_ibf_basefill_066}


def ibf_base_universe_d3_067_ibf_basefill_067(ibf_base_universe_d2_067_ibf_basefill_067):
    return _base_universe_d3(ibf_base_universe_d2_067_ibf_basefill_067, 67)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_067_ibf_basefill_067'] = {'inputs': ['ibf_base_universe_d2_067_ibf_basefill_067'], 'func': ibf_base_universe_d3_067_ibf_basefill_067}


def ibf_base_universe_d3_068_ibf_basefill_068(ibf_base_universe_d2_068_ibf_basefill_068):
    return _base_universe_d3(ibf_base_universe_d2_068_ibf_basefill_068, 68)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_068_ibf_basefill_068'] = {'inputs': ['ibf_base_universe_d2_068_ibf_basefill_068'], 'func': ibf_base_universe_d3_068_ibf_basefill_068}


def ibf_base_universe_d3_069_ibf_basefill_069(ibf_base_universe_d2_069_ibf_basefill_069):
    return _base_universe_d3(ibf_base_universe_d2_069_ibf_basefill_069, 69)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_069_ibf_basefill_069'] = {'inputs': ['ibf_base_universe_d2_069_ibf_basefill_069'], 'func': ibf_base_universe_d3_069_ibf_basefill_069}


def ibf_base_universe_d3_070_ibf_basefill_070(ibf_base_universe_d2_070_ibf_basefill_070):
    return _base_universe_d3(ibf_base_universe_d2_070_ibf_basefill_070, 70)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_070_ibf_basefill_070'] = {'inputs': ['ibf_base_universe_d2_070_ibf_basefill_070'], 'func': ibf_base_universe_d3_070_ibf_basefill_070}


def ibf_base_universe_d3_071_ibf_basefill_071(ibf_base_universe_d2_071_ibf_basefill_071):
    return _base_universe_d3(ibf_base_universe_d2_071_ibf_basefill_071, 71)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_071_ibf_basefill_071'] = {'inputs': ['ibf_base_universe_d2_071_ibf_basefill_071'], 'func': ibf_base_universe_d3_071_ibf_basefill_071}


def ibf_base_universe_d3_072_ibf_basefill_072(ibf_base_universe_d2_072_ibf_basefill_072):
    return _base_universe_d3(ibf_base_universe_d2_072_ibf_basefill_072, 72)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_072_ibf_basefill_072'] = {'inputs': ['ibf_base_universe_d2_072_ibf_basefill_072'], 'func': ibf_base_universe_d3_072_ibf_basefill_072}


def ibf_base_universe_d3_073_ibf_basefill_073(ibf_base_universe_d2_073_ibf_basefill_073):
    return _base_universe_d3(ibf_base_universe_d2_073_ibf_basefill_073, 73)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_073_ibf_basefill_073'] = {'inputs': ['ibf_base_universe_d2_073_ibf_basefill_073'], 'func': ibf_base_universe_d3_073_ibf_basefill_073}


def ibf_base_universe_d3_074_ibf_basefill_074(ibf_base_universe_d2_074_ibf_basefill_074):
    return _base_universe_d3(ibf_base_universe_d2_074_ibf_basefill_074, 74)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_074_ibf_basefill_074'] = {'inputs': ['ibf_base_universe_d2_074_ibf_basefill_074'], 'func': ibf_base_universe_d3_074_ibf_basefill_074}


def ibf_base_universe_d3_075_ibf_basefill_075(ibf_base_universe_d2_075_ibf_basefill_075):
    return _base_universe_d3(ibf_base_universe_d2_075_ibf_basefill_075, 75)
IBF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibf_base_universe_d3_075_ibf_basefill_075'] = {'inputs': ['ibf_base_universe_d2_075_ibf_basefill_075'], 'func': ibf_base_universe_d3_075_ibf_basefill_075}
