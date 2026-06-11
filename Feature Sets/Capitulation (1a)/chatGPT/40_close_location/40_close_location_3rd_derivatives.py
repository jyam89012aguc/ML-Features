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



def clv_001_realized_vol_z_accel_1(clv_001_realized_vol_z_roc_1):
    feature = _s(clv_001_realized_vol_z_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def clv_007_realized_vol_z_accel_5(clv_007_realized_vol_z_roc_5):
    feature = _s(clv_007_realized_vol_z_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def clv_013_realized_vol_z_accel_42(clv_013_realized_vol_z_roc_42):
    feature = _s(clv_013_realized_vol_z_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def clv_179_clv_019_realized_vol_z_42_019_accel_126(clv_154_clv_019_realized_vol_z_42_019_roc_126):
    feature = _s(clv_154_clv_019_realized_vol_z_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def clv_180_clv_025_realized_vol_z_378_025_accel_378(clv_155_clv_025_realized_vol_z_378_025_roc_378):
    feature = _s(clv_155_clv_025_realized_vol_z_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















CLOSE_LOCATION_REGISTRY_3RD_DERIVATIVES = {
    'clv_001_realized_vol_z_accel_1': {'inputs': ['clv_001_realized_vol_z_roc_1'], 'func': clv_001_realized_vol_z_accel_1},
    'clv_007_realized_vol_z_accel_5': {'inputs': ['clv_007_realized_vol_z_roc_5'], 'func': clv_007_realized_vol_z_accel_5},
    'clv_013_realized_vol_z_accel_42': {'inputs': ['clv_013_realized_vol_z_roc_42'], 'func': clv_013_realized_vol_z_accel_42},
    'clv_179_clv_019_realized_vol_z_42_019_accel_126': {'inputs': ['clv_154_clv_019_realized_vol_z_42_019_roc_126'], 'func': clv_179_clv_019_realized_vol_z_42_019_accel_126},
    'clv_180_clv_025_realized_vol_z_378_025_accel_378': {'inputs': ['clv_155_clv_025_realized_vol_z_378_025_roc_378'], 'func': clv_180_clv_025_realized_vol_z_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def cl_replacement_d3_001(cl_replacement_d2_001):
    feature = _clean(cl_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_001'] = {'inputs': ['cl_replacement_d2_001'], 'func': cl_replacement_d3_001}


def cl_replacement_d3_002(cl_replacement_d2_002):
    feature = _clean(cl_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_002'] = {'inputs': ['cl_replacement_d2_002'], 'func': cl_replacement_d3_002}


def cl_replacement_d3_003(cl_replacement_d2_003):
    feature = _clean(cl_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_003'] = {'inputs': ['cl_replacement_d2_003'], 'func': cl_replacement_d3_003}


def cl_replacement_d3_004(cl_replacement_d2_004):
    feature = _clean(cl_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_004'] = {'inputs': ['cl_replacement_d2_004'], 'func': cl_replacement_d3_004}


def cl_replacement_d3_005(cl_replacement_d2_005):
    feature = _clean(cl_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_005'] = {'inputs': ['cl_replacement_d2_005'], 'func': cl_replacement_d3_005}


def cl_replacement_d3_006(cl_replacement_d2_006):
    feature = _clean(cl_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_006'] = {'inputs': ['cl_replacement_d2_006'], 'func': cl_replacement_d3_006}


def cl_replacement_d3_007(cl_replacement_d2_007):
    feature = _clean(cl_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_007'] = {'inputs': ['cl_replacement_d2_007'], 'func': cl_replacement_d3_007}


def cl_replacement_d3_008(cl_replacement_d2_008):
    feature = _clean(cl_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_008'] = {'inputs': ['cl_replacement_d2_008'], 'func': cl_replacement_d3_008}


def cl_replacement_d3_009(cl_replacement_d2_009):
    feature = _clean(cl_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_009'] = {'inputs': ['cl_replacement_d2_009'], 'func': cl_replacement_d3_009}


def cl_replacement_d3_010(cl_replacement_d2_010):
    feature = _clean(cl_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_010'] = {'inputs': ['cl_replacement_d2_010'], 'func': cl_replacement_d3_010}


def cl_replacement_d3_011(cl_replacement_d2_011):
    feature = _clean(cl_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_011'] = {'inputs': ['cl_replacement_d2_011'], 'func': cl_replacement_d3_011}


def cl_replacement_d3_012(cl_replacement_d2_012):
    feature = _clean(cl_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_012'] = {'inputs': ['cl_replacement_d2_012'], 'func': cl_replacement_d3_012}


def cl_replacement_d3_013(cl_replacement_d2_013):
    feature = _clean(cl_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_013'] = {'inputs': ['cl_replacement_d2_013'], 'func': cl_replacement_d3_013}


def cl_replacement_d3_014(cl_replacement_d2_014):
    feature = _clean(cl_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_014'] = {'inputs': ['cl_replacement_d2_014'], 'func': cl_replacement_d3_014}


def cl_replacement_d3_015(cl_replacement_d2_015):
    feature = _clean(cl_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_015'] = {'inputs': ['cl_replacement_d2_015'], 'func': cl_replacement_d3_015}


def cl_replacement_d3_016(cl_replacement_d2_016):
    feature = _clean(cl_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_016'] = {'inputs': ['cl_replacement_d2_016'], 'func': cl_replacement_d3_016}


def cl_replacement_d3_017(cl_replacement_d2_017):
    feature = _clean(cl_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_017'] = {'inputs': ['cl_replacement_d2_017'], 'func': cl_replacement_d3_017}


def cl_replacement_d3_018(cl_replacement_d2_018):
    feature = _clean(cl_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_018'] = {'inputs': ['cl_replacement_d2_018'], 'func': cl_replacement_d3_018}


def cl_replacement_d3_019(cl_replacement_d2_019):
    feature = _clean(cl_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_019'] = {'inputs': ['cl_replacement_d2_019'], 'func': cl_replacement_d3_019}


def cl_replacement_d3_020(cl_replacement_d2_020):
    feature = _clean(cl_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_020'] = {'inputs': ['cl_replacement_d2_020'], 'func': cl_replacement_d3_020}


def cl_replacement_d3_021(cl_replacement_d2_021):
    feature = _clean(cl_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_021'] = {'inputs': ['cl_replacement_d2_021'], 'func': cl_replacement_d3_021}


def cl_replacement_d3_022(cl_replacement_d2_022):
    feature = _clean(cl_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_022'] = {'inputs': ['cl_replacement_d2_022'], 'func': cl_replacement_d3_022}


def cl_replacement_d3_023(cl_replacement_d2_023):
    feature = _clean(cl_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_023'] = {'inputs': ['cl_replacement_d2_023'], 'func': cl_replacement_d3_023}


def cl_replacement_d3_024(cl_replacement_d2_024):
    feature = _clean(cl_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_024'] = {'inputs': ['cl_replacement_d2_024'], 'func': cl_replacement_d3_024}


def cl_replacement_d3_025(cl_replacement_d2_025):
    feature = _clean(cl_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_025'] = {'inputs': ['cl_replacement_d2_025'], 'func': cl_replacement_d3_025}


def cl_replacement_d3_026(cl_replacement_d2_026):
    feature = _clean(cl_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_026'] = {'inputs': ['cl_replacement_d2_026'], 'func': cl_replacement_d3_026}


def cl_replacement_d3_027(cl_replacement_d2_027):
    feature = _clean(cl_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_027'] = {'inputs': ['cl_replacement_d2_027'], 'func': cl_replacement_d3_027}


def cl_replacement_d3_028(cl_replacement_d2_028):
    feature = _clean(cl_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_028'] = {'inputs': ['cl_replacement_d2_028'], 'func': cl_replacement_d3_028}


def cl_replacement_d3_029(cl_replacement_d2_029):
    feature = _clean(cl_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_029'] = {'inputs': ['cl_replacement_d2_029'], 'func': cl_replacement_d3_029}


def cl_replacement_d3_030(cl_replacement_d2_030):
    feature = _clean(cl_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_030'] = {'inputs': ['cl_replacement_d2_030'], 'func': cl_replacement_d3_030}


def cl_replacement_d3_031(cl_replacement_d2_031):
    feature = _clean(cl_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_031'] = {'inputs': ['cl_replacement_d2_031'], 'func': cl_replacement_d3_031}


def cl_replacement_d3_032(cl_replacement_d2_032):
    feature = _clean(cl_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_032'] = {'inputs': ['cl_replacement_d2_032'], 'func': cl_replacement_d3_032}


def cl_replacement_d3_033(cl_replacement_d2_033):
    feature = _clean(cl_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_033'] = {'inputs': ['cl_replacement_d2_033'], 'func': cl_replacement_d3_033}


def cl_replacement_d3_034(cl_replacement_d2_034):
    feature = _clean(cl_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_034'] = {'inputs': ['cl_replacement_d2_034'], 'func': cl_replacement_d3_034}


def cl_replacement_d3_035(cl_replacement_d2_035):
    feature = _clean(cl_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_035'] = {'inputs': ['cl_replacement_d2_035'], 'func': cl_replacement_d3_035}


def cl_replacement_d3_036(cl_replacement_d2_036):
    feature = _clean(cl_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_036'] = {'inputs': ['cl_replacement_d2_036'], 'func': cl_replacement_d3_036}


def cl_replacement_d3_037(cl_replacement_d2_037):
    feature = _clean(cl_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_037'] = {'inputs': ['cl_replacement_d2_037'], 'func': cl_replacement_d3_037}


def cl_replacement_d3_038(cl_replacement_d2_038):
    feature = _clean(cl_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_038'] = {'inputs': ['cl_replacement_d2_038'], 'func': cl_replacement_d3_038}


def cl_replacement_d3_039(cl_replacement_d2_039):
    feature = _clean(cl_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_039'] = {'inputs': ['cl_replacement_d2_039'], 'func': cl_replacement_d3_039}


def cl_replacement_d3_040(cl_replacement_d2_040):
    feature = _clean(cl_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_040'] = {'inputs': ['cl_replacement_d2_040'], 'func': cl_replacement_d3_040}


def cl_replacement_d3_041(cl_replacement_d2_041):
    feature = _clean(cl_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_041'] = {'inputs': ['cl_replacement_d2_041'], 'func': cl_replacement_d3_041}


def cl_replacement_d3_042(cl_replacement_d2_042):
    feature = _clean(cl_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_042'] = {'inputs': ['cl_replacement_d2_042'], 'func': cl_replacement_d3_042}


def cl_replacement_d3_043(cl_replacement_d2_043):
    feature = _clean(cl_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_043'] = {'inputs': ['cl_replacement_d2_043'], 'func': cl_replacement_d3_043}


def cl_replacement_d3_044(cl_replacement_d2_044):
    feature = _clean(cl_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_044'] = {'inputs': ['cl_replacement_d2_044'], 'func': cl_replacement_d3_044}


def cl_replacement_d3_045(cl_replacement_d2_045):
    feature = _clean(cl_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_045'] = {'inputs': ['cl_replacement_d2_045'], 'func': cl_replacement_d3_045}


def cl_replacement_d3_046(cl_replacement_d2_046):
    feature = _clean(cl_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_046'] = {'inputs': ['cl_replacement_d2_046'], 'func': cl_replacement_d3_046}


def cl_replacement_d3_047(cl_replacement_d2_047):
    feature = _clean(cl_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_047'] = {'inputs': ['cl_replacement_d2_047'], 'func': cl_replacement_d3_047}


def cl_replacement_d3_048(cl_replacement_d2_048):
    feature = _clean(cl_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_048'] = {'inputs': ['cl_replacement_d2_048'], 'func': cl_replacement_d3_048}


def cl_replacement_d3_049(cl_replacement_d2_049):
    feature = _clean(cl_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_049'] = {'inputs': ['cl_replacement_d2_049'], 'func': cl_replacement_d3_049}


def cl_replacement_d3_050(cl_replacement_d2_050):
    feature = _clean(cl_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_050'] = {'inputs': ['cl_replacement_d2_050'], 'func': cl_replacement_d3_050}


def cl_replacement_d3_051(cl_replacement_d2_051):
    feature = _clean(cl_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_051'] = {'inputs': ['cl_replacement_d2_051'], 'func': cl_replacement_d3_051}


def cl_replacement_d3_052(cl_replacement_d2_052):
    feature = _clean(cl_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_052'] = {'inputs': ['cl_replacement_d2_052'], 'func': cl_replacement_d3_052}


def cl_replacement_d3_053(cl_replacement_d2_053):
    feature = _clean(cl_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_053'] = {'inputs': ['cl_replacement_d2_053'], 'func': cl_replacement_d3_053}


def cl_replacement_d3_054(cl_replacement_d2_054):
    feature = _clean(cl_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_054'] = {'inputs': ['cl_replacement_d2_054'], 'func': cl_replacement_d3_054}


def cl_replacement_d3_055(cl_replacement_d2_055):
    feature = _clean(cl_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_055'] = {'inputs': ['cl_replacement_d2_055'], 'func': cl_replacement_d3_055}


def cl_replacement_d3_056(cl_replacement_d2_056):
    feature = _clean(cl_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_056'] = {'inputs': ['cl_replacement_d2_056'], 'func': cl_replacement_d3_056}


def cl_replacement_d3_057(cl_replacement_d2_057):
    feature = _clean(cl_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_057'] = {'inputs': ['cl_replacement_d2_057'], 'func': cl_replacement_d3_057}


def cl_replacement_d3_058(cl_replacement_d2_058):
    feature = _clean(cl_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_058'] = {'inputs': ['cl_replacement_d2_058'], 'func': cl_replacement_d3_058}


def cl_replacement_d3_059(cl_replacement_d2_059):
    feature = _clean(cl_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_059'] = {'inputs': ['cl_replacement_d2_059'], 'func': cl_replacement_d3_059}


def cl_replacement_d3_060(cl_replacement_d2_060):
    feature = _clean(cl_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_060'] = {'inputs': ['cl_replacement_d2_060'], 'func': cl_replacement_d3_060}


def cl_replacement_d3_061(cl_replacement_d2_061):
    feature = _clean(cl_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_061'] = {'inputs': ['cl_replacement_d2_061'], 'func': cl_replacement_d3_061}


def cl_replacement_d3_062(cl_replacement_d2_062):
    feature = _clean(cl_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_062'] = {'inputs': ['cl_replacement_d2_062'], 'func': cl_replacement_d3_062}


def cl_replacement_d3_063(cl_replacement_d2_063):
    feature = _clean(cl_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_063'] = {'inputs': ['cl_replacement_d2_063'], 'func': cl_replacement_d3_063}


def cl_replacement_d3_064(cl_replacement_d2_064):
    feature = _clean(cl_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_064'] = {'inputs': ['cl_replacement_d2_064'], 'func': cl_replacement_d3_064}


def cl_replacement_d3_065(cl_replacement_d2_065):
    feature = _clean(cl_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_065'] = {'inputs': ['cl_replacement_d2_065'], 'func': cl_replacement_d3_065}


def cl_replacement_d3_066(cl_replacement_d2_066):
    feature = _clean(cl_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_066'] = {'inputs': ['cl_replacement_d2_066'], 'func': cl_replacement_d3_066}


def cl_replacement_d3_067(cl_replacement_d2_067):
    feature = _clean(cl_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_067'] = {'inputs': ['cl_replacement_d2_067'], 'func': cl_replacement_d3_067}


def cl_replacement_d3_068(cl_replacement_d2_068):
    feature = _clean(cl_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_068'] = {'inputs': ['cl_replacement_d2_068'], 'func': cl_replacement_d3_068}


def cl_replacement_d3_069(cl_replacement_d2_069):
    feature = _clean(cl_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_069'] = {'inputs': ['cl_replacement_d2_069'], 'func': cl_replacement_d3_069}


def cl_replacement_d3_070(cl_replacement_d2_070):
    feature = _clean(cl_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_070'] = {'inputs': ['cl_replacement_d2_070'], 'func': cl_replacement_d3_070}


def cl_replacement_d3_071(cl_replacement_d2_071):
    feature = _clean(cl_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_071'] = {'inputs': ['cl_replacement_d2_071'], 'func': cl_replacement_d3_071}


def cl_replacement_d3_072(cl_replacement_d2_072):
    feature = _clean(cl_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_072'] = {'inputs': ['cl_replacement_d2_072'], 'func': cl_replacement_d3_072}


def cl_replacement_d3_073(cl_replacement_d2_073):
    feature = _clean(cl_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_073'] = {'inputs': ['cl_replacement_d2_073'], 'func': cl_replacement_d3_073}


def cl_replacement_d3_074(cl_replacement_d2_074):
    feature = _clean(cl_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_074'] = {'inputs': ['cl_replacement_d2_074'], 'func': cl_replacement_d3_074}


def cl_replacement_d3_075(cl_replacement_d2_075):
    feature = _clean(cl_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_075'] = {'inputs': ['cl_replacement_d2_075'], 'func': cl_replacement_d3_075}


def cl_replacement_d3_076(cl_replacement_d2_076):
    feature = _clean(cl_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_076'] = {'inputs': ['cl_replacement_d2_076'], 'func': cl_replacement_d3_076}


def cl_replacement_d3_077(cl_replacement_d2_077):
    feature = _clean(cl_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_077'] = {'inputs': ['cl_replacement_d2_077'], 'func': cl_replacement_d3_077}


def cl_replacement_d3_078(cl_replacement_d2_078):
    feature = _clean(cl_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_078'] = {'inputs': ['cl_replacement_d2_078'], 'func': cl_replacement_d3_078}


def cl_replacement_d3_079(cl_replacement_d2_079):
    feature = _clean(cl_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_079'] = {'inputs': ['cl_replacement_d2_079'], 'func': cl_replacement_d3_079}


def cl_replacement_d3_080(cl_replacement_d2_080):
    feature = _clean(cl_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_080'] = {'inputs': ['cl_replacement_d2_080'], 'func': cl_replacement_d3_080}


def cl_replacement_d3_081(cl_replacement_d2_081):
    feature = _clean(cl_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_081'] = {'inputs': ['cl_replacement_d2_081'], 'func': cl_replacement_d3_081}


def cl_replacement_d3_082(cl_replacement_d2_082):
    feature = _clean(cl_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_082'] = {'inputs': ['cl_replacement_d2_082'], 'func': cl_replacement_d3_082}


def cl_replacement_d3_083(cl_replacement_d2_083):
    feature = _clean(cl_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_083'] = {'inputs': ['cl_replacement_d2_083'], 'func': cl_replacement_d3_083}


def cl_replacement_d3_084(cl_replacement_d2_084):
    feature = _clean(cl_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_084'] = {'inputs': ['cl_replacement_d2_084'], 'func': cl_replacement_d3_084}


def cl_replacement_d3_085(cl_replacement_d2_085):
    feature = _clean(cl_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_085'] = {'inputs': ['cl_replacement_d2_085'], 'func': cl_replacement_d3_085}


def cl_replacement_d3_086(cl_replacement_d2_086):
    feature = _clean(cl_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_086'] = {'inputs': ['cl_replacement_d2_086'], 'func': cl_replacement_d3_086}


def cl_replacement_d3_087(cl_replacement_d2_087):
    feature = _clean(cl_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_087'] = {'inputs': ['cl_replacement_d2_087'], 'func': cl_replacement_d3_087}


def cl_replacement_d3_088(cl_replacement_d2_088):
    feature = _clean(cl_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_088'] = {'inputs': ['cl_replacement_d2_088'], 'func': cl_replacement_d3_088}


def cl_replacement_d3_089(cl_replacement_d2_089):
    feature = _clean(cl_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_089'] = {'inputs': ['cl_replacement_d2_089'], 'func': cl_replacement_d3_089}


def cl_replacement_d3_090(cl_replacement_d2_090):
    feature = _clean(cl_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_090'] = {'inputs': ['cl_replacement_d2_090'], 'func': cl_replacement_d3_090}


def cl_replacement_d3_091(cl_replacement_d2_091):
    feature = _clean(cl_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_091'] = {'inputs': ['cl_replacement_d2_091'], 'func': cl_replacement_d3_091}


def cl_replacement_d3_092(cl_replacement_d2_092):
    feature = _clean(cl_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_092'] = {'inputs': ['cl_replacement_d2_092'], 'func': cl_replacement_d3_092}


def cl_replacement_d3_093(cl_replacement_d2_093):
    feature = _clean(cl_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_093'] = {'inputs': ['cl_replacement_d2_093'], 'func': cl_replacement_d3_093}


def cl_replacement_d3_094(cl_replacement_d2_094):
    feature = _clean(cl_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_094'] = {'inputs': ['cl_replacement_d2_094'], 'func': cl_replacement_d3_094}


def cl_replacement_d3_095(cl_replacement_d2_095):
    feature = _clean(cl_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_095'] = {'inputs': ['cl_replacement_d2_095'], 'func': cl_replacement_d3_095}


def cl_replacement_d3_096(cl_replacement_d2_096):
    feature = _clean(cl_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_096'] = {'inputs': ['cl_replacement_d2_096'], 'func': cl_replacement_d3_096}


def cl_replacement_d3_097(cl_replacement_d2_097):
    feature = _clean(cl_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_097'] = {'inputs': ['cl_replacement_d2_097'], 'func': cl_replacement_d3_097}


def cl_replacement_d3_098(cl_replacement_d2_098):
    feature = _clean(cl_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_098'] = {'inputs': ['cl_replacement_d2_098'], 'func': cl_replacement_d3_098}


def cl_replacement_d3_099(cl_replacement_d2_099):
    feature = _clean(cl_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_099'] = {'inputs': ['cl_replacement_d2_099'], 'func': cl_replacement_d3_099}


def cl_replacement_d3_100(cl_replacement_d2_100):
    feature = _clean(cl_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_100'] = {'inputs': ['cl_replacement_d2_100'], 'func': cl_replacement_d3_100}


def cl_replacement_d3_101(cl_replacement_d2_101):
    feature = _clean(cl_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_101'] = {'inputs': ['cl_replacement_d2_101'], 'func': cl_replacement_d3_101}


def cl_replacement_d3_102(cl_replacement_d2_102):
    feature = _clean(cl_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_102'] = {'inputs': ['cl_replacement_d2_102'], 'func': cl_replacement_d3_102}


def cl_replacement_d3_103(cl_replacement_d2_103):
    feature = _clean(cl_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_103'] = {'inputs': ['cl_replacement_d2_103'], 'func': cl_replacement_d3_103}


def cl_replacement_d3_104(cl_replacement_d2_104):
    feature = _clean(cl_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_104'] = {'inputs': ['cl_replacement_d2_104'], 'func': cl_replacement_d3_104}


def cl_replacement_d3_105(cl_replacement_d2_105):
    feature = _clean(cl_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_105'] = {'inputs': ['cl_replacement_d2_105'], 'func': cl_replacement_d3_105}


def cl_replacement_d3_106(cl_replacement_d2_106):
    feature = _clean(cl_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_106'] = {'inputs': ['cl_replacement_d2_106'], 'func': cl_replacement_d3_106}


def cl_replacement_d3_107(cl_replacement_d2_107):
    feature = _clean(cl_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_107'] = {'inputs': ['cl_replacement_d2_107'], 'func': cl_replacement_d3_107}


def cl_replacement_d3_108(cl_replacement_d2_108):
    feature = _clean(cl_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_108'] = {'inputs': ['cl_replacement_d2_108'], 'func': cl_replacement_d3_108}


def cl_replacement_d3_109(cl_replacement_d2_109):
    feature = _clean(cl_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_109'] = {'inputs': ['cl_replacement_d2_109'], 'func': cl_replacement_d3_109}


def cl_replacement_d3_110(cl_replacement_d2_110):
    feature = _clean(cl_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_110'] = {'inputs': ['cl_replacement_d2_110'], 'func': cl_replacement_d3_110}


def cl_replacement_d3_111(cl_replacement_d2_111):
    feature = _clean(cl_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_111'] = {'inputs': ['cl_replacement_d2_111'], 'func': cl_replacement_d3_111}


def cl_replacement_d3_112(cl_replacement_d2_112):
    feature = _clean(cl_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_112'] = {'inputs': ['cl_replacement_d2_112'], 'func': cl_replacement_d3_112}


def cl_replacement_d3_113(cl_replacement_d2_113):
    feature = _clean(cl_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_113'] = {'inputs': ['cl_replacement_d2_113'], 'func': cl_replacement_d3_113}


def cl_replacement_d3_114(cl_replacement_d2_114):
    feature = _clean(cl_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_114'] = {'inputs': ['cl_replacement_d2_114'], 'func': cl_replacement_d3_114}


def cl_replacement_d3_115(cl_replacement_d2_115):
    feature = _clean(cl_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_115'] = {'inputs': ['cl_replacement_d2_115'], 'func': cl_replacement_d3_115}


def cl_replacement_d3_116(cl_replacement_d2_116):
    feature = _clean(cl_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_116'] = {'inputs': ['cl_replacement_d2_116'], 'func': cl_replacement_d3_116}


def cl_replacement_d3_117(cl_replacement_d2_117):
    feature = _clean(cl_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_117'] = {'inputs': ['cl_replacement_d2_117'], 'func': cl_replacement_d3_117}


def cl_replacement_d3_118(cl_replacement_d2_118):
    feature = _clean(cl_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_118'] = {'inputs': ['cl_replacement_d2_118'], 'func': cl_replacement_d3_118}


def cl_replacement_d3_119(cl_replacement_d2_119):
    feature = _clean(cl_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_119'] = {'inputs': ['cl_replacement_d2_119'], 'func': cl_replacement_d3_119}


def cl_replacement_d3_120(cl_replacement_d2_120):
    feature = _clean(cl_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_120'] = {'inputs': ['cl_replacement_d2_120'], 'func': cl_replacement_d3_120}


def cl_replacement_d3_121(cl_replacement_d2_121):
    feature = _clean(cl_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_121'] = {'inputs': ['cl_replacement_d2_121'], 'func': cl_replacement_d3_121}


def cl_replacement_d3_122(cl_replacement_d2_122):
    feature = _clean(cl_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_122'] = {'inputs': ['cl_replacement_d2_122'], 'func': cl_replacement_d3_122}


def cl_replacement_d3_123(cl_replacement_d2_123):
    feature = _clean(cl_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_123'] = {'inputs': ['cl_replacement_d2_123'], 'func': cl_replacement_d3_123}


def cl_replacement_d3_124(cl_replacement_d2_124):
    feature = _clean(cl_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_124'] = {'inputs': ['cl_replacement_d2_124'], 'func': cl_replacement_d3_124}


def cl_replacement_d3_125(cl_replacement_d2_125):
    feature = _clean(cl_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_125'] = {'inputs': ['cl_replacement_d2_125'], 'func': cl_replacement_d3_125}


def cl_replacement_d3_126(cl_replacement_d2_126):
    feature = _clean(cl_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_126'] = {'inputs': ['cl_replacement_d2_126'], 'func': cl_replacement_d3_126}


def cl_replacement_d3_127(cl_replacement_d2_127):
    feature = _clean(cl_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_127'] = {'inputs': ['cl_replacement_d2_127'], 'func': cl_replacement_d3_127}


def cl_replacement_d3_128(cl_replacement_d2_128):
    feature = _clean(cl_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_128'] = {'inputs': ['cl_replacement_d2_128'], 'func': cl_replacement_d3_128}


def cl_replacement_d3_129(cl_replacement_d2_129):
    feature = _clean(cl_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_129'] = {'inputs': ['cl_replacement_d2_129'], 'func': cl_replacement_d3_129}


def cl_replacement_d3_130(cl_replacement_d2_130):
    feature = _clean(cl_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_130'] = {'inputs': ['cl_replacement_d2_130'], 'func': cl_replacement_d3_130}


def cl_replacement_d3_131(cl_replacement_d2_131):
    feature = _clean(cl_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_131'] = {'inputs': ['cl_replacement_d2_131'], 'func': cl_replacement_d3_131}


def cl_replacement_d3_132(cl_replacement_d2_132):
    feature = _clean(cl_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_132'] = {'inputs': ['cl_replacement_d2_132'], 'func': cl_replacement_d3_132}


def cl_replacement_d3_133(cl_replacement_d2_133):
    feature = _clean(cl_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_133'] = {'inputs': ['cl_replacement_d2_133'], 'func': cl_replacement_d3_133}


def cl_replacement_d3_134(cl_replacement_d2_134):
    feature = _clean(cl_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_134'] = {'inputs': ['cl_replacement_d2_134'], 'func': cl_replacement_d3_134}


def cl_replacement_d3_135(cl_replacement_d2_135):
    feature = _clean(cl_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_135'] = {'inputs': ['cl_replacement_d2_135'], 'func': cl_replacement_d3_135}


def cl_replacement_d3_136(cl_replacement_d2_136):
    feature = _clean(cl_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_136'] = {'inputs': ['cl_replacement_d2_136'], 'func': cl_replacement_d3_136}


def cl_replacement_d3_137(cl_replacement_d2_137):
    feature = _clean(cl_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_137'] = {'inputs': ['cl_replacement_d2_137'], 'func': cl_replacement_d3_137}


def cl_replacement_d3_138(cl_replacement_d2_138):
    feature = _clean(cl_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_138'] = {'inputs': ['cl_replacement_d2_138'], 'func': cl_replacement_d3_138}


def cl_replacement_d3_139(cl_replacement_d2_139):
    feature = _clean(cl_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_139'] = {'inputs': ['cl_replacement_d2_139'], 'func': cl_replacement_d3_139}


def cl_replacement_d3_140(cl_replacement_d2_140):
    feature = _clean(cl_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_140'] = {'inputs': ['cl_replacement_d2_140'], 'func': cl_replacement_d3_140}


def cl_replacement_d3_141(cl_replacement_d2_141):
    feature = _clean(cl_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_141'] = {'inputs': ['cl_replacement_d2_141'], 'func': cl_replacement_d3_141}


def cl_replacement_d3_142(cl_replacement_d2_142):
    feature = _clean(cl_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_142'] = {'inputs': ['cl_replacement_d2_142'], 'func': cl_replacement_d3_142}


def cl_replacement_d3_143(cl_replacement_d2_143):
    feature = _clean(cl_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_143'] = {'inputs': ['cl_replacement_d2_143'], 'func': cl_replacement_d3_143}


def cl_replacement_d3_144(cl_replacement_d2_144):
    feature = _clean(cl_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_144'] = {'inputs': ['cl_replacement_d2_144'], 'func': cl_replacement_d3_144}


def cl_replacement_d3_145(cl_replacement_d2_145):
    feature = _clean(cl_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_145'] = {'inputs': ['cl_replacement_d2_145'], 'func': cl_replacement_d3_145}


def cl_replacement_d3_146(cl_replacement_d2_146):
    feature = _clean(cl_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_146'] = {'inputs': ['cl_replacement_d2_146'], 'func': cl_replacement_d3_146}


def cl_replacement_d3_147(cl_replacement_d2_147):
    feature = _clean(cl_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_147'] = {'inputs': ['cl_replacement_d2_147'], 'func': cl_replacement_d3_147}


def cl_replacement_d3_148(cl_replacement_d2_148):
    feature = _clean(cl_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_148'] = {'inputs': ['cl_replacement_d2_148'], 'func': cl_replacement_d3_148}


def cl_replacement_d3_149(cl_replacement_d2_149):
    feature = _clean(cl_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_149'] = {'inputs': ['cl_replacement_d2_149'], 'func': cl_replacement_d3_149}


def cl_replacement_d3_150(cl_replacement_d2_150):
    feature = _clean(cl_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_150'] = {'inputs': ['cl_replacement_d2_150'], 'func': cl_replacement_d3_150}


def cl_replacement_d3_151(cl_replacement_d2_151):
    feature = _clean(cl_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_151'] = {'inputs': ['cl_replacement_d2_151'], 'func': cl_replacement_d3_151}


def cl_replacement_d3_152(cl_replacement_d2_152):
    feature = _clean(cl_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_152'] = {'inputs': ['cl_replacement_d2_152'], 'func': cl_replacement_d3_152}


def cl_replacement_d3_153(cl_replacement_d2_153):
    feature = _clean(cl_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_153'] = {'inputs': ['cl_replacement_d2_153'], 'func': cl_replacement_d3_153}


def cl_replacement_d3_154(cl_replacement_d2_154):
    feature = _clean(cl_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_154'] = {'inputs': ['cl_replacement_d2_154'], 'func': cl_replacement_d3_154}


def cl_replacement_d3_155(cl_replacement_d2_155):
    feature = _clean(cl_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_155'] = {'inputs': ['cl_replacement_d2_155'], 'func': cl_replacement_d3_155}


def cl_replacement_d3_156(cl_replacement_d2_156):
    feature = _clean(cl_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_156'] = {'inputs': ['cl_replacement_d2_156'], 'func': cl_replacement_d3_156}


def cl_replacement_d3_157(cl_replacement_d2_157):
    feature = _clean(cl_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_157'] = {'inputs': ['cl_replacement_d2_157'], 'func': cl_replacement_d3_157}


def cl_replacement_d3_158(cl_replacement_d2_158):
    feature = _clean(cl_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_158'] = {'inputs': ['cl_replacement_d2_158'], 'func': cl_replacement_d3_158}


def cl_replacement_d3_159(cl_replacement_d2_159):
    feature = _clean(cl_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_159'] = {'inputs': ['cl_replacement_d2_159'], 'func': cl_replacement_d3_159}


def cl_replacement_d3_160(cl_replacement_d2_160):
    feature = _clean(cl_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_160'] = {'inputs': ['cl_replacement_d2_160'], 'func': cl_replacement_d3_160}


def cl_replacement_d3_161(cl_replacement_d2_161):
    feature = _clean(cl_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_161'] = {'inputs': ['cl_replacement_d2_161'], 'func': cl_replacement_d3_161}


def cl_replacement_d3_162(cl_replacement_d2_162):
    feature = _clean(cl_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_162'] = {'inputs': ['cl_replacement_d2_162'], 'func': cl_replacement_d3_162}


def cl_replacement_d3_163(cl_replacement_d2_163):
    feature = _clean(cl_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_163'] = {'inputs': ['cl_replacement_d2_163'], 'func': cl_replacement_d3_163}


def cl_replacement_d3_164(cl_replacement_d2_164):
    feature = _clean(cl_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_164'] = {'inputs': ['cl_replacement_d2_164'], 'func': cl_replacement_d3_164}


def cl_replacement_d3_165(cl_replacement_d2_165):
    feature = _clean(cl_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_165'] = {'inputs': ['cl_replacement_d2_165'], 'func': cl_replacement_d3_165}


def cl_replacement_d3_166(cl_replacement_d2_166):
    feature = _clean(cl_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_166'] = {'inputs': ['cl_replacement_d2_166'], 'func': cl_replacement_d3_166}


def cl_replacement_d3_167(cl_replacement_d2_167):
    feature = _clean(cl_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_167'] = {'inputs': ['cl_replacement_d2_167'], 'func': cl_replacement_d3_167}


def cl_replacement_d3_168(cl_replacement_d2_168):
    feature = _clean(cl_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_168'] = {'inputs': ['cl_replacement_d2_168'], 'func': cl_replacement_d3_168}


def cl_replacement_d3_169(cl_replacement_d2_169):
    feature = _clean(cl_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_169'] = {'inputs': ['cl_replacement_d2_169'], 'func': cl_replacement_d3_169}


def cl_replacement_d3_170(cl_replacement_d2_170):
    feature = _clean(cl_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_170'] = {'inputs': ['cl_replacement_d2_170'], 'func': cl_replacement_d3_170}


def cl_replacement_d3_171(cl_replacement_d2_171):
    feature = _clean(cl_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_171'] = {'inputs': ['cl_replacement_d2_171'], 'func': cl_replacement_d3_171}


def cl_replacement_d3_172(cl_replacement_d2_172):
    feature = _clean(cl_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_172'] = {'inputs': ['cl_replacement_d2_172'], 'func': cl_replacement_d3_172}


def cl_replacement_d3_173(cl_replacement_d2_173):
    feature = _clean(cl_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_173'] = {'inputs': ['cl_replacement_d2_173'], 'func': cl_replacement_d3_173}


def cl_replacement_d3_174(cl_replacement_d2_174):
    feature = _clean(cl_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_174'] = {'inputs': ['cl_replacement_d2_174'], 'func': cl_replacement_d3_174}


def cl_replacement_d3_175(cl_replacement_d2_175):
    feature = _clean(cl_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_175'] = {'inputs': ['cl_replacement_d2_175'], 'func': cl_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def clv_base_universe_d3_001_clv_002_range_expansion_10_002(clv_base_universe_d2_001_clv_002_range_expansion_10_002):
    return _base_universe_d3(clv_base_universe_d2_001_clv_002_range_expansion_10_002, 1)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_001_clv_002_range_expansion_10_002'] = {'inputs': ['clv_base_universe_d2_001_clv_002_range_expansion_10_002'], 'func': clv_base_universe_d3_001_clv_002_range_expansion_10_002}


def clv_base_universe_d3_002_clv_004_close_location_42_004(clv_base_universe_d2_002_clv_004_close_location_42_004):
    return _base_universe_d3(clv_base_universe_d2_002_clv_004_close_location_42_004, 2)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_002_clv_004_close_location_42_004'] = {'inputs': ['clv_base_universe_d2_002_clv_004_close_location_42_004'], 'func': clv_base_universe_d3_002_clv_004_close_location_42_004}


def clv_base_universe_d3_003_clv_005_atr_move_63_005(clv_base_universe_d2_003_clv_005_atr_move_63_005):
    return _base_universe_d3(clv_base_universe_d2_003_clv_005_atr_move_63_005, 3)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_003_clv_005_atr_move_63_005'] = {'inputs': ['clv_base_universe_d2_003_clv_005_atr_move_63_005'], 'func': clv_base_universe_d3_003_clv_005_atr_move_63_005}


def clv_base_universe_d3_004_clv_008_range_expansion_189_008(clv_base_universe_d2_004_clv_008_range_expansion_189_008):
    return _base_universe_d3(clv_base_universe_d2_004_clv_008_range_expansion_189_008, 4)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_004_clv_008_range_expansion_189_008'] = {'inputs': ['clv_base_universe_d2_004_clv_008_range_expansion_189_008'], 'func': clv_base_universe_d3_004_clv_008_range_expansion_189_008}


def clv_base_universe_d3_005_clv_010_close_location_378_010(clv_base_universe_d2_005_clv_010_close_location_378_010):
    return _base_universe_d3(clv_base_universe_d2_005_clv_010_close_location_378_010, 5)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_005_clv_010_close_location_378_010'] = {'inputs': ['clv_base_universe_d2_005_clv_010_close_location_378_010'], 'func': clv_base_universe_d3_005_clv_010_close_location_378_010}


def clv_base_universe_d3_006_clv_011_atr_move_504_011(clv_base_universe_d2_006_clv_011_atr_move_504_011):
    return _base_universe_d3(clv_base_universe_d2_006_clv_011_atr_move_504_011, 6)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_006_clv_011_atr_move_504_011'] = {'inputs': ['clv_base_universe_d2_006_clv_011_atr_move_504_011'], 'func': clv_base_universe_d3_006_clv_011_atr_move_504_011}


def clv_base_universe_d3_007_clv_014_range_expansion_1260_014(clv_base_universe_d2_007_clv_014_range_expansion_1260_014):
    return _base_universe_d3(clv_base_universe_d2_007_clv_014_range_expansion_1260_014, 7)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_007_clv_014_range_expansion_1260_014'] = {'inputs': ['clv_base_universe_d2_007_clv_014_range_expansion_1260_014'], 'func': clv_base_universe_d3_007_clv_014_range_expansion_1260_014}


def clv_base_universe_d3_008_clv_016_close_location_5_016(clv_base_universe_d2_008_clv_016_close_location_5_016):
    return _base_universe_d3(clv_base_universe_d2_008_clv_016_close_location_5_016, 8)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_008_clv_016_close_location_5_016'] = {'inputs': ['clv_base_universe_d2_008_clv_016_close_location_5_016'], 'func': clv_base_universe_d3_008_clv_016_close_location_5_016}


def clv_base_universe_d3_009_clv_017_atr_move_10_017(clv_base_universe_d2_009_clv_017_atr_move_10_017):
    return _base_universe_d3(clv_base_universe_d2_009_clv_017_atr_move_10_017, 9)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_009_clv_017_atr_move_10_017'] = {'inputs': ['clv_base_universe_d2_009_clv_017_atr_move_10_017'], 'func': clv_base_universe_d3_009_clv_017_atr_move_10_017}


def clv_base_universe_d3_010_clv_020_range_expansion_63_020(clv_base_universe_d2_010_clv_020_range_expansion_63_020):
    return _base_universe_d3(clv_base_universe_d2_010_clv_020_range_expansion_63_020, 10)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_010_clv_020_range_expansion_63_020'] = {'inputs': ['clv_base_universe_d2_010_clv_020_range_expansion_63_020'], 'func': clv_base_universe_d3_010_clv_020_range_expansion_63_020}


def clv_base_universe_d3_011_clv_022_close_location_126_022(clv_base_universe_d2_011_clv_022_close_location_126_022):
    return _base_universe_d3(clv_base_universe_d2_011_clv_022_close_location_126_022, 11)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_011_clv_022_close_location_126_022'] = {'inputs': ['clv_base_universe_d2_011_clv_022_close_location_126_022'], 'func': clv_base_universe_d3_011_clv_022_close_location_126_022}


def clv_base_universe_d3_012_clv_023_atr_move_189_023(clv_base_universe_d2_012_clv_023_atr_move_189_023):
    return _base_universe_d3(clv_base_universe_d2_012_clv_023_atr_move_189_023, 12)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_012_clv_023_atr_move_189_023'] = {'inputs': ['clv_base_universe_d2_012_clv_023_atr_move_189_023'], 'func': clv_base_universe_d3_012_clv_023_atr_move_189_023}


def clv_base_universe_d3_013_clv_026_range_expansion_504_026(clv_base_universe_d2_013_clv_026_range_expansion_504_026):
    return _base_universe_d3(clv_base_universe_d2_013_clv_026_range_expansion_504_026, 13)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_013_clv_026_range_expansion_504_026'] = {'inputs': ['clv_base_universe_d2_013_clv_026_range_expansion_504_026'], 'func': clv_base_universe_d3_013_clv_026_range_expansion_504_026}


def clv_base_universe_d3_014_clv_028_close_location_1008_028(clv_base_universe_d2_014_clv_028_close_location_1008_028):
    return _base_universe_d3(clv_base_universe_d2_014_clv_028_close_location_1008_028, 14)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_014_clv_028_close_location_1008_028'] = {'inputs': ['clv_base_universe_d2_014_clv_028_close_location_1008_028'], 'func': clv_base_universe_d3_014_clv_028_close_location_1008_028}


def clv_base_universe_d3_015_clv_029_atr_move_1260_029(clv_base_universe_d2_015_clv_029_atr_move_1260_029):
    return _base_universe_d3(clv_base_universe_d2_015_clv_029_atr_move_1260_029, 15)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_015_clv_029_atr_move_1260_029'] = {'inputs': ['clv_base_universe_d2_015_clv_029_atr_move_1260_029'], 'func': clv_base_universe_d3_015_clv_029_atr_move_1260_029}


def clv_base_universe_d3_016_clv_basefill_001(clv_base_universe_d2_016_clv_basefill_001):
    return _base_universe_d3(clv_base_universe_d2_016_clv_basefill_001, 16)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_016_clv_basefill_001'] = {'inputs': ['clv_base_universe_d2_016_clv_basefill_001'], 'func': clv_base_universe_d3_016_clv_basefill_001}


def clv_base_universe_d3_017_clv_basefill_003(clv_base_universe_d2_017_clv_basefill_003):
    return _base_universe_d3(clv_base_universe_d2_017_clv_basefill_003, 17)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_017_clv_basefill_003'] = {'inputs': ['clv_base_universe_d2_017_clv_basefill_003'], 'func': clv_base_universe_d3_017_clv_basefill_003}


def clv_base_universe_d3_018_clv_basefill_006(clv_base_universe_d2_018_clv_basefill_006):
    return _base_universe_d3(clv_base_universe_d2_018_clv_basefill_006, 18)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_018_clv_basefill_006'] = {'inputs': ['clv_base_universe_d2_018_clv_basefill_006'], 'func': clv_base_universe_d3_018_clv_basefill_006}


def clv_base_universe_d3_019_clv_basefill_007(clv_base_universe_d2_019_clv_basefill_007):
    return _base_universe_d3(clv_base_universe_d2_019_clv_basefill_007, 19)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_019_clv_basefill_007'] = {'inputs': ['clv_base_universe_d2_019_clv_basefill_007'], 'func': clv_base_universe_d3_019_clv_basefill_007}


def clv_base_universe_d3_020_clv_basefill_009(clv_base_universe_d2_020_clv_basefill_009):
    return _base_universe_d3(clv_base_universe_d2_020_clv_basefill_009, 20)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_020_clv_basefill_009'] = {'inputs': ['clv_base_universe_d2_020_clv_basefill_009'], 'func': clv_base_universe_d3_020_clv_basefill_009}


def clv_base_universe_d3_021_clv_basefill_012(clv_base_universe_d2_021_clv_basefill_012):
    return _base_universe_d3(clv_base_universe_d2_021_clv_basefill_012, 21)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_021_clv_basefill_012'] = {'inputs': ['clv_base_universe_d2_021_clv_basefill_012'], 'func': clv_base_universe_d3_021_clv_basefill_012}


def clv_base_universe_d3_022_clv_basefill_013(clv_base_universe_d2_022_clv_basefill_013):
    return _base_universe_d3(clv_base_universe_d2_022_clv_basefill_013, 22)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_022_clv_basefill_013'] = {'inputs': ['clv_base_universe_d2_022_clv_basefill_013'], 'func': clv_base_universe_d3_022_clv_basefill_013}


def clv_base_universe_d3_023_clv_basefill_015(clv_base_universe_d2_023_clv_basefill_015):
    return _base_universe_d3(clv_base_universe_d2_023_clv_basefill_015, 23)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_023_clv_basefill_015'] = {'inputs': ['clv_base_universe_d2_023_clv_basefill_015'], 'func': clv_base_universe_d3_023_clv_basefill_015}


def clv_base_universe_d3_024_clv_basefill_018(clv_base_universe_d2_024_clv_basefill_018):
    return _base_universe_d3(clv_base_universe_d2_024_clv_basefill_018, 24)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_024_clv_basefill_018'] = {'inputs': ['clv_base_universe_d2_024_clv_basefill_018'], 'func': clv_base_universe_d3_024_clv_basefill_018}


def clv_base_universe_d3_025_clv_basefill_019(clv_base_universe_d2_025_clv_basefill_019):
    return _base_universe_d3(clv_base_universe_d2_025_clv_basefill_019, 25)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_025_clv_basefill_019'] = {'inputs': ['clv_base_universe_d2_025_clv_basefill_019'], 'func': clv_base_universe_d3_025_clv_basefill_019}


def clv_base_universe_d3_026_clv_basefill_021(clv_base_universe_d2_026_clv_basefill_021):
    return _base_universe_d3(clv_base_universe_d2_026_clv_basefill_021, 26)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_026_clv_basefill_021'] = {'inputs': ['clv_base_universe_d2_026_clv_basefill_021'], 'func': clv_base_universe_d3_026_clv_basefill_021}


def clv_base_universe_d3_027_clv_basefill_024(clv_base_universe_d2_027_clv_basefill_024):
    return _base_universe_d3(clv_base_universe_d2_027_clv_basefill_024, 27)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_027_clv_basefill_024'] = {'inputs': ['clv_base_universe_d2_027_clv_basefill_024'], 'func': clv_base_universe_d3_027_clv_basefill_024}


def clv_base_universe_d3_028_clv_basefill_025(clv_base_universe_d2_028_clv_basefill_025):
    return _base_universe_d3(clv_base_universe_d2_028_clv_basefill_025, 28)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_028_clv_basefill_025'] = {'inputs': ['clv_base_universe_d2_028_clv_basefill_025'], 'func': clv_base_universe_d3_028_clv_basefill_025}


def clv_base_universe_d3_029_clv_basefill_027(clv_base_universe_d2_029_clv_basefill_027):
    return _base_universe_d3(clv_base_universe_d2_029_clv_basefill_027, 29)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_029_clv_basefill_027'] = {'inputs': ['clv_base_universe_d2_029_clv_basefill_027'], 'func': clv_base_universe_d3_029_clv_basefill_027}


def clv_base_universe_d3_030_clv_basefill_030(clv_base_universe_d2_030_clv_basefill_030):
    return _base_universe_d3(clv_base_universe_d2_030_clv_basefill_030, 30)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_030_clv_basefill_030'] = {'inputs': ['clv_base_universe_d2_030_clv_basefill_030'], 'func': clv_base_universe_d3_030_clv_basefill_030}


def clv_base_universe_d3_031_clv_basefill_031(clv_base_universe_d2_031_clv_basefill_031):
    return _base_universe_d3(clv_base_universe_d2_031_clv_basefill_031, 31)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_031_clv_basefill_031'] = {'inputs': ['clv_base_universe_d2_031_clv_basefill_031'], 'func': clv_base_universe_d3_031_clv_basefill_031}


def clv_base_universe_d3_032_clv_basefill_032(clv_base_universe_d2_032_clv_basefill_032):
    return _base_universe_d3(clv_base_universe_d2_032_clv_basefill_032, 32)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_032_clv_basefill_032'] = {'inputs': ['clv_base_universe_d2_032_clv_basefill_032'], 'func': clv_base_universe_d3_032_clv_basefill_032}


def clv_base_universe_d3_033_clv_basefill_033(clv_base_universe_d2_033_clv_basefill_033):
    return _base_universe_d3(clv_base_universe_d2_033_clv_basefill_033, 33)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_033_clv_basefill_033'] = {'inputs': ['clv_base_universe_d2_033_clv_basefill_033'], 'func': clv_base_universe_d3_033_clv_basefill_033}


def clv_base_universe_d3_034_clv_basefill_034(clv_base_universe_d2_034_clv_basefill_034):
    return _base_universe_d3(clv_base_universe_d2_034_clv_basefill_034, 34)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_034_clv_basefill_034'] = {'inputs': ['clv_base_universe_d2_034_clv_basefill_034'], 'func': clv_base_universe_d3_034_clv_basefill_034}


def clv_base_universe_d3_035_clv_basefill_035(clv_base_universe_d2_035_clv_basefill_035):
    return _base_universe_d3(clv_base_universe_d2_035_clv_basefill_035, 35)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_035_clv_basefill_035'] = {'inputs': ['clv_base_universe_d2_035_clv_basefill_035'], 'func': clv_base_universe_d3_035_clv_basefill_035}


def clv_base_universe_d3_036_clv_basefill_036(clv_base_universe_d2_036_clv_basefill_036):
    return _base_universe_d3(clv_base_universe_d2_036_clv_basefill_036, 36)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_036_clv_basefill_036'] = {'inputs': ['clv_base_universe_d2_036_clv_basefill_036'], 'func': clv_base_universe_d3_036_clv_basefill_036}


def clv_base_universe_d3_037_clv_basefill_037(clv_base_universe_d2_037_clv_basefill_037):
    return _base_universe_d3(clv_base_universe_d2_037_clv_basefill_037, 37)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_037_clv_basefill_037'] = {'inputs': ['clv_base_universe_d2_037_clv_basefill_037'], 'func': clv_base_universe_d3_037_clv_basefill_037}


def clv_base_universe_d3_038_clv_basefill_038(clv_base_universe_d2_038_clv_basefill_038):
    return _base_universe_d3(clv_base_universe_d2_038_clv_basefill_038, 38)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_038_clv_basefill_038'] = {'inputs': ['clv_base_universe_d2_038_clv_basefill_038'], 'func': clv_base_universe_d3_038_clv_basefill_038}


def clv_base_universe_d3_039_clv_basefill_039(clv_base_universe_d2_039_clv_basefill_039):
    return _base_universe_d3(clv_base_universe_d2_039_clv_basefill_039, 39)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_039_clv_basefill_039'] = {'inputs': ['clv_base_universe_d2_039_clv_basefill_039'], 'func': clv_base_universe_d3_039_clv_basefill_039}


def clv_base_universe_d3_040_clv_basefill_040(clv_base_universe_d2_040_clv_basefill_040):
    return _base_universe_d3(clv_base_universe_d2_040_clv_basefill_040, 40)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_040_clv_basefill_040'] = {'inputs': ['clv_base_universe_d2_040_clv_basefill_040'], 'func': clv_base_universe_d3_040_clv_basefill_040}


def clv_base_universe_d3_041_clv_basefill_041(clv_base_universe_d2_041_clv_basefill_041):
    return _base_universe_d3(clv_base_universe_d2_041_clv_basefill_041, 41)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_041_clv_basefill_041'] = {'inputs': ['clv_base_universe_d2_041_clv_basefill_041'], 'func': clv_base_universe_d3_041_clv_basefill_041}


def clv_base_universe_d3_042_clv_basefill_042(clv_base_universe_d2_042_clv_basefill_042):
    return _base_universe_d3(clv_base_universe_d2_042_clv_basefill_042, 42)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_042_clv_basefill_042'] = {'inputs': ['clv_base_universe_d2_042_clv_basefill_042'], 'func': clv_base_universe_d3_042_clv_basefill_042}


def clv_base_universe_d3_043_clv_basefill_043(clv_base_universe_d2_043_clv_basefill_043):
    return _base_universe_d3(clv_base_universe_d2_043_clv_basefill_043, 43)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_043_clv_basefill_043'] = {'inputs': ['clv_base_universe_d2_043_clv_basefill_043'], 'func': clv_base_universe_d3_043_clv_basefill_043}


def clv_base_universe_d3_044_clv_basefill_044(clv_base_universe_d2_044_clv_basefill_044):
    return _base_universe_d3(clv_base_universe_d2_044_clv_basefill_044, 44)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_044_clv_basefill_044'] = {'inputs': ['clv_base_universe_d2_044_clv_basefill_044'], 'func': clv_base_universe_d3_044_clv_basefill_044}


def clv_base_universe_d3_045_clv_basefill_045(clv_base_universe_d2_045_clv_basefill_045):
    return _base_universe_d3(clv_base_universe_d2_045_clv_basefill_045, 45)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_045_clv_basefill_045'] = {'inputs': ['clv_base_universe_d2_045_clv_basefill_045'], 'func': clv_base_universe_d3_045_clv_basefill_045}


def clv_base_universe_d3_046_clv_basefill_046(clv_base_universe_d2_046_clv_basefill_046):
    return _base_universe_d3(clv_base_universe_d2_046_clv_basefill_046, 46)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_046_clv_basefill_046'] = {'inputs': ['clv_base_universe_d2_046_clv_basefill_046'], 'func': clv_base_universe_d3_046_clv_basefill_046}


def clv_base_universe_d3_047_clv_basefill_047(clv_base_universe_d2_047_clv_basefill_047):
    return _base_universe_d3(clv_base_universe_d2_047_clv_basefill_047, 47)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_047_clv_basefill_047'] = {'inputs': ['clv_base_universe_d2_047_clv_basefill_047'], 'func': clv_base_universe_d3_047_clv_basefill_047}


def clv_base_universe_d3_048_clv_basefill_048(clv_base_universe_d2_048_clv_basefill_048):
    return _base_universe_d3(clv_base_universe_d2_048_clv_basefill_048, 48)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_048_clv_basefill_048'] = {'inputs': ['clv_base_universe_d2_048_clv_basefill_048'], 'func': clv_base_universe_d3_048_clv_basefill_048}


def clv_base_universe_d3_049_clv_basefill_049(clv_base_universe_d2_049_clv_basefill_049):
    return _base_universe_d3(clv_base_universe_d2_049_clv_basefill_049, 49)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_049_clv_basefill_049'] = {'inputs': ['clv_base_universe_d2_049_clv_basefill_049'], 'func': clv_base_universe_d3_049_clv_basefill_049}


def clv_base_universe_d3_050_clv_basefill_050(clv_base_universe_d2_050_clv_basefill_050):
    return _base_universe_d3(clv_base_universe_d2_050_clv_basefill_050, 50)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_050_clv_basefill_050'] = {'inputs': ['clv_base_universe_d2_050_clv_basefill_050'], 'func': clv_base_universe_d3_050_clv_basefill_050}


def clv_base_universe_d3_051_clv_basefill_051(clv_base_universe_d2_051_clv_basefill_051):
    return _base_universe_d3(clv_base_universe_d2_051_clv_basefill_051, 51)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_051_clv_basefill_051'] = {'inputs': ['clv_base_universe_d2_051_clv_basefill_051'], 'func': clv_base_universe_d3_051_clv_basefill_051}


def clv_base_universe_d3_052_clv_basefill_052(clv_base_universe_d2_052_clv_basefill_052):
    return _base_universe_d3(clv_base_universe_d2_052_clv_basefill_052, 52)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_052_clv_basefill_052'] = {'inputs': ['clv_base_universe_d2_052_clv_basefill_052'], 'func': clv_base_universe_d3_052_clv_basefill_052}


def clv_base_universe_d3_053_clv_basefill_053(clv_base_universe_d2_053_clv_basefill_053):
    return _base_universe_d3(clv_base_universe_d2_053_clv_basefill_053, 53)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_053_clv_basefill_053'] = {'inputs': ['clv_base_universe_d2_053_clv_basefill_053'], 'func': clv_base_universe_d3_053_clv_basefill_053}


def clv_base_universe_d3_054_clv_basefill_054(clv_base_universe_d2_054_clv_basefill_054):
    return _base_universe_d3(clv_base_universe_d2_054_clv_basefill_054, 54)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_054_clv_basefill_054'] = {'inputs': ['clv_base_universe_d2_054_clv_basefill_054'], 'func': clv_base_universe_d3_054_clv_basefill_054}


def clv_base_universe_d3_055_clv_basefill_055(clv_base_universe_d2_055_clv_basefill_055):
    return _base_universe_d3(clv_base_universe_d2_055_clv_basefill_055, 55)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_055_clv_basefill_055'] = {'inputs': ['clv_base_universe_d2_055_clv_basefill_055'], 'func': clv_base_universe_d3_055_clv_basefill_055}


def clv_base_universe_d3_056_clv_basefill_056(clv_base_universe_d2_056_clv_basefill_056):
    return _base_universe_d3(clv_base_universe_d2_056_clv_basefill_056, 56)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_056_clv_basefill_056'] = {'inputs': ['clv_base_universe_d2_056_clv_basefill_056'], 'func': clv_base_universe_d3_056_clv_basefill_056}


def clv_base_universe_d3_057_clv_basefill_057(clv_base_universe_d2_057_clv_basefill_057):
    return _base_universe_d3(clv_base_universe_d2_057_clv_basefill_057, 57)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_057_clv_basefill_057'] = {'inputs': ['clv_base_universe_d2_057_clv_basefill_057'], 'func': clv_base_universe_d3_057_clv_basefill_057}


def clv_base_universe_d3_058_clv_basefill_058(clv_base_universe_d2_058_clv_basefill_058):
    return _base_universe_d3(clv_base_universe_d2_058_clv_basefill_058, 58)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_058_clv_basefill_058'] = {'inputs': ['clv_base_universe_d2_058_clv_basefill_058'], 'func': clv_base_universe_d3_058_clv_basefill_058}


def clv_base_universe_d3_059_clv_basefill_059(clv_base_universe_d2_059_clv_basefill_059):
    return _base_universe_d3(clv_base_universe_d2_059_clv_basefill_059, 59)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_059_clv_basefill_059'] = {'inputs': ['clv_base_universe_d2_059_clv_basefill_059'], 'func': clv_base_universe_d3_059_clv_basefill_059}


def clv_base_universe_d3_060_clv_basefill_060(clv_base_universe_d2_060_clv_basefill_060):
    return _base_universe_d3(clv_base_universe_d2_060_clv_basefill_060, 60)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_060_clv_basefill_060'] = {'inputs': ['clv_base_universe_d2_060_clv_basefill_060'], 'func': clv_base_universe_d3_060_clv_basefill_060}


def clv_base_universe_d3_061_clv_basefill_061(clv_base_universe_d2_061_clv_basefill_061):
    return _base_universe_d3(clv_base_universe_d2_061_clv_basefill_061, 61)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_061_clv_basefill_061'] = {'inputs': ['clv_base_universe_d2_061_clv_basefill_061'], 'func': clv_base_universe_d3_061_clv_basefill_061}


def clv_base_universe_d3_062_clv_basefill_062(clv_base_universe_d2_062_clv_basefill_062):
    return _base_universe_d3(clv_base_universe_d2_062_clv_basefill_062, 62)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_062_clv_basefill_062'] = {'inputs': ['clv_base_universe_d2_062_clv_basefill_062'], 'func': clv_base_universe_d3_062_clv_basefill_062}


def clv_base_universe_d3_063_clv_basefill_063(clv_base_universe_d2_063_clv_basefill_063):
    return _base_universe_d3(clv_base_universe_d2_063_clv_basefill_063, 63)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_063_clv_basefill_063'] = {'inputs': ['clv_base_universe_d2_063_clv_basefill_063'], 'func': clv_base_universe_d3_063_clv_basefill_063}


def clv_base_universe_d3_064_clv_basefill_064(clv_base_universe_d2_064_clv_basefill_064):
    return _base_universe_d3(clv_base_universe_d2_064_clv_basefill_064, 64)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_064_clv_basefill_064'] = {'inputs': ['clv_base_universe_d2_064_clv_basefill_064'], 'func': clv_base_universe_d3_064_clv_basefill_064}


def clv_base_universe_d3_065_clv_basefill_065(clv_base_universe_d2_065_clv_basefill_065):
    return _base_universe_d3(clv_base_universe_d2_065_clv_basefill_065, 65)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_065_clv_basefill_065'] = {'inputs': ['clv_base_universe_d2_065_clv_basefill_065'], 'func': clv_base_universe_d3_065_clv_basefill_065}


def clv_base_universe_d3_066_clv_basefill_066(clv_base_universe_d2_066_clv_basefill_066):
    return _base_universe_d3(clv_base_universe_d2_066_clv_basefill_066, 66)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_066_clv_basefill_066'] = {'inputs': ['clv_base_universe_d2_066_clv_basefill_066'], 'func': clv_base_universe_d3_066_clv_basefill_066}


def clv_base_universe_d3_067_clv_basefill_067(clv_base_universe_d2_067_clv_basefill_067):
    return _base_universe_d3(clv_base_universe_d2_067_clv_basefill_067, 67)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_067_clv_basefill_067'] = {'inputs': ['clv_base_universe_d2_067_clv_basefill_067'], 'func': clv_base_universe_d3_067_clv_basefill_067}


def clv_base_universe_d3_068_clv_basefill_068(clv_base_universe_d2_068_clv_basefill_068):
    return _base_universe_d3(clv_base_universe_d2_068_clv_basefill_068, 68)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_068_clv_basefill_068'] = {'inputs': ['clv_base_universe_d2_068_clv_basefill_068'], 'func': clv_base_universe_d3_068_clv_basefill_068}


def clv_base_universe_d3_069_clv_basefill_069(clv_base_universe_d2_069_clv_basefill_069):
    return _base_universe_d3(clv_base_universe_d2_069_clv_basefill_069, 69)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_069_clv_basefill_069'] = {'inputs': ['clv_base_universe_d2_069_clv_basefill_069'], 'func': clv_base_universe_d3_069_clv_basefill_069}


def clv_base_universe_d3_070_clv_basefill_070(clv_base_universe_d2_070_clv_basefill_070):
    return _base_universe_d3(clv_base_universe_d2_070_clv_basefill_070, 70)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_070_clv_basefill_070'] = {'inputs': ['clv_base_universe_d2_070_clv_basefill_070'], 'func': clv_base_universe_d3_070_clv_basefill_070}


def clv_base_universe_d3_071_clv_basefill_071(clv_base_universe_d2_071_clv_basefill_071):
    return _base_universe_d3(clv_base_universe_d2_071_clv_basefill_071, 71)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_071_clv_basefill_071'] = {'inputs': ['clv_base_universe_d2_071_clv_basefill_071'], 'func': clv_base_universe_d3_071_clv_basefill_071}


def clv_base_universe_d3_072_clv_basefill_072(clv_base_universe_d2_072_clv_basefill_072):
    return _base_universe_d3(clv_base_universe_d2_072_clv_basefill_072, 72)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_072_clv_basefill_072'] = {'inputs': ['clv_base_universe_d2_072_clv_basefill_072'], 'func': clv_base_universe_d3_072_clv_basefill_072}


def clv_base_universe_d3_073_clv_basefill_073(clv_base_universe_d2_073_clv_basefill_073):
    return _base_universe_d3(clv_base_universe_d2_073_clv_basefill_073, 73)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_073_clv_basefill_073'] = {'inputs': ['clv_base_universe_d2_073_clv_basefill_073'], 'func': clv_base_universe_d3_073_clv_basefill_073}


def clv_base_universe_d3_074_clv_basefill_074(clv_base_universe_d2_074_clv_basefill_074):
    return _base_universe_d3(clv_base_universe_d2_074_clv_basefill_074, 74)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_074_clv_basefill_074'] = {'inputs': ['clv_base_universe_d2_074_clv_basefill_074'], 'func': clv_base_universe_d3_074_clv_basefill_074}


def clv_base_universe_d3_075_clv_basefill_075(clv_base_universe_d2_075_clv_basefill_075):
    return _base_universe_d3(clv_base_universe_d2_075_clv_basefill_075, 75)
CLV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['clv_base_universe_d3_075_clv_basefill_075'] = {'inputs': ['clv_base_universe_d2_075_clv_basefill_075'], 'func': clv_base_universe_d3_075_clv_basefill_075}
