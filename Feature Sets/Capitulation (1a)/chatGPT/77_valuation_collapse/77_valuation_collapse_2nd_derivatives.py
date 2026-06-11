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



def vcl_151_vcl_001_pe_compression_z_21_roc_1(vcl_001_pe_compression_z_21):
    feature = _s(vcl_001_pe_compression_z_21)
    return (_roc(feature, 1)).reindex(feature.index)

def vcl_152_vcl_007_earnings_yield_spike_252_roc_42(vcl_007_earnings_yield_spike_252):
    feature = _s(vcl_007_earnings_yield_spike_252)
    return (_roc(feature, 42)).reindex(feature.index)

def vcl_153_vcl_013_ev_marketcap_gap_1512_roc_126(vcl_013_ev_marketcap_gap_1512):
    feature = _s(vcl_013_ev_marketcap_gap_1512)
    return (_roc(feature, 126)).reindex(feature.index)

def vcl_154_vcl_019_ps_compression_z_84_roc_378(vcl_019_ps_compression_z_84):
    feature = _s(vcl_019_ps_compression_z_84)
    return (_roc(feature, 378)).reindex(feature.index)

def vcl_155_vcl_025_pe_compression_z_756_roc_4(vcl_025_pe_compression_z_756):
    feature = _s(vcl_025_pe_compression_z_756)
    return (_roc(feature, 4)).reindex(feature.index)






















VALUATION_COLLAPSE_REGISTRY_2ND_DERIVATIVES = {
    'vcl_151_vcl_001_pe_compression_z_21_roc_1': {'inputs': ['vcl_001_pe_compression_z_21'], 'func': vcl_151_vcl_001_pe_compression_z_21_roc_1},
    'vcl_152_vcl_007_earnings_yield_spike_252_roc_42': {'inputs': ['vcl_007_earnings_yield_spike_252'], 'func': vcl_152_vcl_007_earnings_yield_spike_252_roc_42},
    'vcl_153_vcl_013_ev_marketcap_gap_1512_roc_126': {'inputs': ['vcl_013_ev_marketcap_gap_1512'], 'func': vcl_153_vcl_013_ev_marketcap_gap_1512_roc_126},
    'vcl_154_vcl_019_ps_compression_z_84_roc_378': {'inputs': ['vcl_019_ps_compression_z_84'], 'func': vcl_154_vcl_019_ps_compression_z_84_roc_378},
    'vcl_155_vcl_025_pe_compression_z_756_roc_4': {'inputs': ['vcl_025_pe_compression_z_756'], 'func': vcl_155_vcl_025_pe_compression_z_756_roc_4},
}


# Replacement 2nd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY = {}


def vc_replacement_d2_001(vcl_025_pe_compression_z_756):
    feature = _clean(vcl_025_pe_compression_z_756)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00001000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_001'] = {'inputs': ['vcl_025_pe_compression_z_756'], 'func': vc_replacement_d2_001}


def vc_replacement_d2_002(vc_replacement_001):
    feature = _clean(vc_replacement_001)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00002000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_002'] = {'inputs': ['vc_replacement_001'], 'func': vc_replacement_d2_002}


def vc_replacement_d2_003(vc_replacement_002):
    feature = _clean(vc_replacement_002)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00003000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_003'] = {'inputs': ['vc_replacement_002'], 'func': vc_replacement_d2_003}


def vc_replacement_d2_004(vc_replacement_003):
    feature = _clean(vc_replacement_003)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00004000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_004'] = {'inputs': ['vc_replacement_003'], 'func': vc_replacement_d2_004}


def vc_replacement_d2_005(vc_replacement_004):
    feature = _clean(vc_replacement_004)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00005000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_005'] = {'inputs': ['vc_replacement_004'], 'func': vc_replacement_d2_005}


def vc_replacement_d2_006(vc_replacement_005):
    feature = _clean(vc_replacement_005)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00006000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_006'] = {'inputs': ['vc_replacement_005'], 'func': vc_replacement_d2_006}


def vc_replacement_d2_007(vc_replacement_006):
    feature = _clean(vc_replacement_006)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00007000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_007'] = {'inputs': ['vc_replacement_006'], 'func': vc_replacement_d2_007}


def vc_replacement_d2_008(vc_replacement_007):
    feature = _clean(vc_replacement_007)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00008000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_008'] = {'inputs': ['vc_replacement_007'], 'func': vc_replacement_d2_008}


def vc_replacement_d2_009(vc_replacement_008):
    feature = _clean(vc_replacement_008)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00009000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_009'] = {'inputs': ['vc_replacement_008'], 'func': vc_replacement_d2_009}


def vc_replacement_d2_010(vc_replacement_009):
    feature = _clean(vc_replacement_009)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00010000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_010'] = {'inputs': ['vc_replacement_009'], 'func': vc_replacement_d2_010}


def vc_replacement_d2_011(vc_replacement_010):
    feature = _clean(vc_replacement_010)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00011000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_011'] = {'inputs': ['vc_replacement_010'], 'func': vc_replacement_d2_011}


def vc_replacement_d2_012(vc_replacement_011):
    feature = _clean(vc_replacement_011)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00012000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_012'] = {'inputs': ['vc_replacement_011'], 'func': vc_replacement_d2_012}


def vc_replacement_d2_013(vc_replacement_012):
    feature = _clean(vc_replacement_012)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00013000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_013'] = {'inputs': ['vc_replacement_012'], 'func': vc_replacement_d2_013}


def vc_replacement_d2_014(vc_replacement_013):
    feature = _clean(vc_replacement_013)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00014000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_014'] = {'inputs': ['vc_replacement_013'], 'func': vc_replacement_d2_014}


def vc_replacement_d2_015(vc_replacement_014):
    feature = _clean(vc_replacement_014)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00015000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_015'] = {'inputs': ['vc_replacement_014'], 'func': vc_replacement_d2_015}


def vc_replacement_d2_016(vc_replacement_015):
    feature = _clean(vc_replacement_015)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00016000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_016'] = {'inputs': ['vc_replacement_015'], 'func': vc_replacement_d2_016}


def vc_replacement_d2_017(vc_replacement_016):
    feature = _clean(vc_replacement_016)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00017000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_017'] = {'inputs': ['vc_replacement_016'], 'func': vc_replacement_d2_017}


def vc_replacement_d2_018(vc_replacement_017):
    feature = _clean(vc_replacement_017)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00018000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_018'] = {'inputs': ['vc_replacement_017'], 'func': vc_replacement_d2_018}


def vc_replacement_d2_019(vc_replacement_018):
    feature = _clean(vc_replacement_018)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00019000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_019'] = {'inputs': ['vc_replacement_018'], 'func': vc_replacement_d2_019}


def vc_replacement_d2_020(vc_replacement_019):
    feature = _clean(vc_replacement_019)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00020000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_020'] = {'inputs': ['vc_replacement_019'], 'func': vc_replacement_d2_020}


def vc_replacement_d2_021(vc_replacement_020):
    feature = _clean(vc_replacement_020)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00021000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_021'] = {'inputs': ['vc_replacement_020'], 'func': vc_replacement_d2_021}


def vc_replacement_d2_022(vc_replacement_021):
    feature = _clean(vc_replacement_021)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00022000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_022'] = {'inputs': ['vc_replacement_021'], 'func': vc_replacement_d2_022}


def vc_replacement_d2_023(vc_replacement_022):
    feature = _clean(vc_replacement_022)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00023000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_023'] = {'inputs': ['vc_replacement_022'], 'func': vc_replacement_d2_023}


def vc_replacement_d2_024(vc_replacement_023):
    feature = _clean(vc_replacement_023)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00024000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_024'] = {'inputs': ['vc_replacement_023'], 'func': vc_replacement_d2_024}


def vc_replacement_d2_025(vc_replacement_024):
    feature = _clean(vc_replacement_024)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00025000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_025'] = {'inputs': ['vc_replacement_024'], 'func': vc_replacement_d2_025}


def vc_replacement_d2_026(vc_replacement_025):
    feature = _clean(vc_replacement_025)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00026000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_026'] = {'inputs': ['vc_replacement_025'], 'func': vc_replacement_d2_026}


def vc_replacement_d2_027(vc_replacement_026):
    feature = _clean(vc_replacement_026)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00027000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_027'] = {'inputs': ['vc_replacement_026'], 'func': vc_replacement_d2_027}


def vc_replacement_d2_028(vc_replacement_027):
    feature = _clean(vc_replacement_027)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00028000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_028'] = {'inputs': ['vc_replacement_027'], 'func': vc_replacement_d2_028}


def vc_replacement_d2_029(vc_replacement_028):
    feature = _clean(vc_replacement_028)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00029000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_029'] = {'inputs': ['vc_replacement_028'], 'func': vc_replacement_d2_029}


def vc_replacement_d2_030(vc_replacement_029):
    feature = _clean(vc_replacement_029)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00030000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_030'] = {'inputs': ['vc_replacement_029'], 'func': vc_replacement_d2_030}


def vc_replacement_d2_031(vc_replacement_030):
    feature = _clean(vc_replacement_030)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00031000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_031'] = {'inputs': ['vc_replacement_030'], 'func': vc_replacement_d2_031}


def vc_replacement_d2_032(vc_replacement_031):
    feature = _clean(vc_replacement_031)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00032000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_032'] = {'inputs': ['vc_replacement_031'], 'func': vc_replacement_d2_032}


def vc_replacement_d2_033(vc_replacement_032):
    feature = _clean(vc_replacement_032)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00033000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_033'] = {'inputs': ['vc_replacement_032'], 'func': vc_replacement_d2_033}


def vc_replacement_d2_034(vc_replacement_033):
    feature = _clean(vc_replacement_033)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00034000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_034'] = {'inputs': ['vc_replacement_033'], 'func': vc_replacement_d2_034}


def vc_replacement_d2_035(vc_replacement_034):
    feature = _clean(vc_replacement_034)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00035000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_035'] = {'inputs': ['vc_replacement_034'], 'func': vc_replacement_d2_035}


def vc_replacement_d2_036(vc_replacement_035):
    feature = _clean(vc_replacement_035)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00036000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_036'] = {'inputs': ['vc_replacement_035'], 'func': vc_replacement_d2_036}


def vc_replacement_d2_037(vc_replacement_036):
    feature = _clean(vc_replacement_036)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00037000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_037'] = {'inputs': ['vc_replacement_036'], 'func': vc_replacement_d2_037}


def vc_replacement_d2_038(vc_replacement_037):
    feature = _clean(vc_replacement_037)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00038000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_038'] = {'inputs': ['vc_replacement_037'], 'func': vc_replacement_d2_038}


def vc_replacement_d2_039(vc_replacement_038):
    feature = _clean(vc_replacement_038)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00039000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_039'] = {'inputs': ['vc_replacement_038'], 'func': vc_replacement_d2_039}


def vc_replacement_d2_040(vc_replacement_039):
    feature = _clean(vc_replacement_039)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00040000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_040'] = {'inputs': ['vc_replacement_039'], 'func': vc_replacement_d2_040}


def vc_replacement_d2_041(vc_replacement_040):
    feature = _clean(vc_replacement_040)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00041000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_041'] = {'inputs': ['vc_replacement_040'], 'func': vc_replacement_d2_041}


def vc_replacement_d2_042(vc_replacement_041):
    feature = _clean(vc_replacement_041)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00042000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_042'] = {'inputs': ['vc_replacement_041'], 'func': vc_replacement_d2_042}


def vc_replacement_d2_043(vc_replacement_042):
    feature = _clean(vc_replacement_042)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00043000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_043'] = {'inputs': ['vc_replacement_042'], 'func': vc_replacement_d2_043}


def vc_replacement_d2_044(vc_replacement_043):
    feature = _clean(vc_replacement_043)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00044000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_044'] = {'inputs': ['vc_replacement_043'], 'func': vc_replacement_d2_044}


def vc_replacement_d2_045(vc_replacement_044):
    feature = _clean(vc_replacement_044)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00045000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_045'] = {'inputs': ['vc_replacement_044'], 'func': vc_replacement_d2_045}


def vc_replacement_d2_046(vc_replacement_045):
    feature = _clean(vc_replacement_045)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00046000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_046'] = {'inputs': ['vc_replacement_045'], 'func': vc_replacement_d2_046}


def vc_replacement_d2_047(vc_replacement_046):
    feature = _clean(vc_replacement_046)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00047000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_047'] = {'inputs': ['vc_replacement_046'], 'func': vc_replacement_d2_047}


def vc_replacement_d2_048(vc_replacement_047):
    feature = _clean(vc_replacement_047)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00048000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_048'] = {'inputs': ['vc_replacement_047'], 'func': vc_replacement_d2_048}


def vc_replacement_d2_049(vc_replacement_048):
    feature = _clean(vc_replacement_048)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00049000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_049'] = {'inputs': ['vc_replacement_048'], 'func': vc_replacement_d2_049}


def vc_replacement_d2_050(vc_replacement_049):
    feature = _clean(vc_replacement_049)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00050000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_050'] = {'inputs': ['vc_replacement_049'], 'func': vc_replacement_d2_050}


def vc_replacement_d2_051(vc_replacement_050):
    feature = _clean(vc_replacement_050)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00051000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_051'] = {'inputs': ['vc_replacement_050'], 'func': vc_replacement_d2_051}


def vc_replacement_d2_052(vc_replacement_051):
    feature = _clean(vc_replacement_051)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00052000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_052'] = {'inputs': ['vc_replacement_051'], 'func': vc_replacement_d2_052}


def vc_replacement_d2_053(vc_replacement_052):
    feature = _clean(vc_replacement_052)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00053000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_053'] = {'inputs': ['vc_replacement_052'], 'func': vc_replacement_d2_053}


def vc_replacement_d2_054(vc_replacement_053):
    feature = _clean(vc_replacement_053)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00054000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_054'] = {'inputs': ['vc_replacement_053'], 'func': vc_replacement_d2_054}


def vc_replacement_d2_055(vc_replacement_054):
    feature = _clean(vc_replacement_054)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00055000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_055'] = {'inputs': ['vc_replacement_054'], 'func': vc_replacement_d2_055}


def vc_replacement_d2_056(vc_replacement_055):
    feature = _clean(vc_replacement_055)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00056000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_056'] = {'inputs': ['vc_replacement_055'], 'func': vc_replacement_d2_056}


def vc_replacement_d2_057(vc_replacement_056):
    feature = _clean(vc_replacement_056)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00057000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_057'] = {'inputs': ['vc_replacement_056'], 'func': vc_replacement_d2_057}


def vc_replacement_d2_058(vc_replacement_057):
    feature = _clean(vc_replacement_057)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00058000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_058'] = {'inputs': ['vc_replacement_057'], 'func': vc_replacement_d2_058}


def vc_replacement_d2_059(vc_replacement_058):
    feature = _clean(vc_replacement_058)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00059000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_059'] = {'inputs': ['vc_replacement_058'], 'func': vc_replacement_d2_059}


def vc_replacement_d2_060(vc_replacement_059):
    feature = _clean(vc_replacement_059)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00060000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_060'] = {'inputs': ['vc_replacement_059'], 'func': vc_replacement_d2_060}


def vc_replacement_d2_061(vc_replacement_060):
    feature = _clean(vc_replacement_060)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00061000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_061'] = {'inputs': ['vc_replacement_060'], 'func': vc_replacement_d2_061}


def vc_replacement_d2_062(vc_replacement_061):
    feature = _clean(vc_replacement_061)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00062000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_062'] = {'inputs': ['vc_replacement_061'], 'func': vc_replacement_d2_062}


def vc_replacement_d2_063(vc_replacement_062):
    feature = _clean(vc_replacement_062)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00063000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_063'] = {'inputs': ['vc_replacement_062'], 'func': vc_replacement_d2_063}


def vc_replacement_d2_064(vc_replacement_063):
    feature = _clean(vc_replacement_063)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00064000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_064'] = {'inputs': ['vc_replacement_063'], 'func': vc_replacement_d2_064}


def vc_replacement_d2_065(vc_replacement_064):
    feature = _clean(vc_replacement_064)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00065000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_065'] = {'inputs': ['vc_replacement_064'], 'func': vc_replacement_d2_065}


def vc_replacement_d2_066(vc_replacement_065):
    feature = _clean(vc_replacement_065)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00066000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_066'] = {'inputs': ['vc_replacement_065'], 'func': vc_replacement_d2_066}


def vc_replacement_d2_067(vc_replacement_066):
    feature = _clean(vc_replacement_066)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00067000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_067'] = {'inputs': ['vc_replacement_066'], 'func': vc_replacement_d2_067}


def vc_replacement_d2_068(vc_replacement_067):
    feature = _clean(vc_replacement_067)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00068000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_068'] = {'inputs': ['vc_replacement_067'], 'func': vc_replacement_d2_068}


def vc_replacement_d2_069(vc_replacement_068):
    feature = _clean(vc_replacement_068)
    delta = feature.diff(89)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00069000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_069'] = {'inputs': ['vc_replacement_068'], 'func': vc_replacement_d2_069}


def vc_replacement_d2_070(vc_replacement_069):
    feature = _clean(vc_replacement_069)
    delta = feature.diff(1)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00070000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_070'] = {'inputs': ['vc_replacement_069'], 'func': vc_replacement_d2_070}


def vc_replacement_d2_071(vc_replacement_070):
    feature = _clean(vc_replacement_070)
    delta = feature.diff(2)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00071000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_071'] = {'inputs': ['vc_replacement_070'], 'func': vc_replacement_d2_071}


def vc_replacement_d2_072(vc_replacement_071):
    feature = _clean(vc_replacement_071)
    delta = feature.diff(3)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00072000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_072'] = {'inputs': ['vc_replacement_071'], 'func': vc_replacement_d2_072}


def vc_replacement_d2_073(vc_replacement_072):
    feature = _clean(vc_replacement_072)
    delta = feature.diff(5)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00073000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_073'] = {'inputs': ['vc_replacement_072'], 'func': vc_replacement_d2_073}


def vc_replacement_d2_074(vc_replacement_073):
    feature = _clean(vc_replacement_073)
    delta = feature.diff(8)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00074000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_074'] = {'inputs': ['vc_replacement_073'], 'func': vc_replacement_d2_074}


def vc_replacement_d2_075(vc_replacement_074):
    feature = _clean(vc_replacement_074)
    delta = feature.diff(13)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00075000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_075'] = {'inputs': ['vc_replacement_074'], 'func': vc_replacement_d2_075}


def vc_replacement_d2_076(vc_replacement_075):
    feature = _clean(vc_replacement_075)
    delta = feature.diff(21)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00076000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_076'] = {'inputs': ['vc_replacement_075'], 'func': vc_replacement_d2_076}


def vc_replacement_d2_077(vc_replacement_076):
    feature = _clean(vc_replacement_076)
    delta = feature.diff(34)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00077000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_077'] = {'inputs': ['vc_replacement_076'], 'func': vc_replacement_d2_077}


def vc_replacement_d2_078(vc_replacement_077):
    feature = _clean(vc_replacement_077)
    delta = feature.diff(55)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00078000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_078'] = {'inputs': ['vc_replacement_077'], 'func': vc_replacement_d2_078}


def vc_replacement_d2_079(vc_replacement_078):
    feature = _clean(vc_replacement_078)
    delta = feature.diff(89)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00079000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_079'] = {'inputs': ['vc_replacement_078'], 'func': vc_replacement_d2_079}


def vc_replacement_d2_080(vc_replacement_079):
    feature = _clean(vc_replacement_079)
    delta = feature.diff(1)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00080000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_080'] = {'inputs': ['vc_replacement_079'], 'func': vc_replacement_d2_080}


def vc_replacement_d2_081(vc_replacement_080):
    feature = _clean(vc_replacement_080)
    delta = feature.diff(2)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00081000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_081'] = {'inputs': ['vc_replacement_080'], 'func': vc_replacement_d2_081}


def vc_replacement_d2_082(vc_replacement_081):
    feature = _clean(vc_replacement_081)
    delta = feature.diff(3)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00082000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_082'] = {'inputs': ['vc_replacement_081'], 'func': vc_replacement_d2_082}


def vc_replacement_d2_083(vc_replacement_082):
    feature = _clean(vc_replacement_082)
    delta = feature.diff(5)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00083000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_083'] = {'inputs': ['vc_replacement_082'], 'func': vc_replacement_d2_083}


def vc_replacement_d2_084(vc_replacement_083):
    feature = _clean(vc_replacement_083)
    delta = feature.diff(8)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00084000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_084'] = {'inputs': ['vc_replacement_083'], 'func': vc_replacement_d2_084}


def vc_replacement_d2_085(vc_replacement_084):
    feature = _clean(vc_replacement_084)
    delta = feature.diff(13)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00085000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_085'] = {'inputs': ['vc_replacement_084'], 'func': vc_replacement_d2_085}


def vc_replacement_d2_086(vc_replacement_085):
    feature = _clean(vc_replacement_085)
    delta = feature.diff(21)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00086000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_086'] = {'inputs': ['vc_replacement_085'], 'func': vc_replacement_d2_086}


def vc_replacement_d2_087(vc_replacement_086):
    feature = _clean(vc_replacement_086)
    delta = feature.diff(34)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00087000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_087'] = {'inputs': ['vc_replacement_086'], 'func': vc_replacement_d2_087}


def vc_replacement_d2_088(vc_replacement_087):
    feature = _clean(vc_replacement_087)
    delta = feature.diff(55)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00088000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_088'] = {'inputs': ['vc_replacement_087'], 'func': vc_replacement_d2_088}


def vc_replacement_d2_089(vc_replacement_088):
    feature = _clean(vc_replacement_088)
    delta = feature.diff(89)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00089000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_089'] = {'inputs': ['vc_replacement_088'], 'func': vc_replacement_d2_089}


def vc_replacement_d2_090(vc_replacement_089):
    feature = _clean(vc_replacement_089)
    delta = feature.diff(1)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00090000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_090'] = {'inputs': ['vc_replacement_089'], 'func': vc_replacement_d2_090}


def vc_replacement_d2_091(vc_replacement_090):
    feature = _clean(vc_replacement_090)
    delta = feature.diff(2)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00091000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_091'] = {'inputs': ['vc_replacement_090'], 'func': vc_replacement_d2_091}


def vc_replacement_d2_092(vc_replacement_091):
    feature = _clean(vc_replacement_091)
    delta = feature.diff(3)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00092000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_092'] = {'inputs': ['vc_replacement_091'], 'func': vc_replacement_d2_092}


def vc_replacement_d2_093(vc_replacement_092):
    feature = _clean(vc_replacement_092)
    delta = feature.diff(5)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00093000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_093'] = {'inputs': ['vc_replacement_092'], 'func': vc_replacement_d2_093}


def vc_replacement_d2_094(vc_replacement_093):
    feature = _clean(vc_replacement_093)
    delta = feature.diff(8)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00094000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_094'] = {'inputs': ['vc_replacement_093'], 'func': vc_replacement_d2_094}


def vc_replacement_d2_095(vc_replacement_094):
    feature = _clean(vc_replacement_094)
    delta = feature.diff(13)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00095000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_095'] = {'inputs': ['vc_replacement_094'], 'func': vc_replacement_d2_095}


def vc_replacement_d2_096(vc_replacement_095):
    feature = _clean(vc_replacement_095)
    delta = feature.diff(21)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00096000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_096'] = {'inputs': ['vc_replacement_095'], 'func': vc_replacement_d2_096}


def vc_replacement_d2_097(vc_replacement_096):
    feature = _clean(vc_replacement_096)
    delta = feature.diff(34)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00097000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_097'] = {'inputs': ['vc_replacement_096'], 'func': vc_replacement_d2_097}


def vc_replacement_d2_098(vc_replacement_097):
    feature = _clean(vc_replacement_097)
    delta = feature.diff(55)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00098000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_098'] = {'inputs': ['vc_replacement_097'], 'func': vc_replacement_d2_098}


def vc_replacement_d2_099(vc_replacement_098):
    feature = _clean(vc_replacement_098)
    delta = feature.diff(89)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00099000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_099'] = {'inputs': ['vc_replacement_098'], 'func': vc_replacement_d2_099}


def vc_replacement_d2_100(vc_replacement_099):
    feature = _clean(vc_replacement_099)
    delta = feature.diff(1)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00100000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_100'] = {'inputs': ['vc_replacement_099'], 'func': vc_replacement_d2_100}


def vc_replacement_d2_101(vc_replacement_100):
    feature = _clean(vc_replacement_100)
    delta = feature.diff(2)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00101000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_101'] = {'inputs': ['vc_replacement_100'], 'func': vc_replacement_d2_101}


def vc_replacement_d2_102(vc_replacement_101):
    feature = _clean(vc_replacement_101)
    delta = feature.diff(3)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00102000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_102'] = {'inputs': ['vc_replacement_101'], 'func': vc_replacement_d2_102}


def vc_replacement_d2_103(vc_replacement_102):
    feature = _clean(vc_replacement_102)
    delta = feature.diff(5)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00103000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_103'] = {'inputs': ['vc_replacement_102'], 'func': vc_replacement_d2_103}


def vc_replacement_d2_104(vc_replacement_103):
    feature = _clean(vc_replacement_103)
    delta = feature.diff(8)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00104000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_104'] = {'inputs': ['vc_replacement_103'], 'func': vc_replacement_d2_104}


def vc_replacement_d2_105(vc_replacement_104):
    feature = _clean(vc_replacement_104)
    delta = feature.diff(13)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00105000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_105'] = {'inputs': ['vc_replacement_104'], 'func': vc_replacement_d2_105}


def vc_replacement_d2_106(vc_replacement_105):
    feature = _clean(vc_replacement_105)
    delta = feature.diff(21)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00106000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_106'] = {'inputs': ['vc_replacement_105'], 'func': vc_replacement_d2_106}


def vc_replacement_d2_107(vc_replacement_106):
    feature = _clean(vc_replacement_106)
    delta = feature.diff(34)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00107000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_107'] = {'inputs': ['vc_replacement_106'], 'func': vc_replacement_d2_107}


def vc_replacement_d2_108(vc_replacement_107):
    feature = _clean(vc_replacement_107)
    delta = feature.diff(55)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00108000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_108'] = {'inputs': ['vc_replacement_107'], 'func': vc_replacement_d2_108}


def vc_replacement_d2_109(vc_replacement_108):
    feature = _clean(vc_replacement_108)
    delta = feature.diff(89)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00109000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_109'] = {'inputs': ['vc_replacement_108'], 'func': vc_replacement_d2_109}


def vc_replacement_d2_110(vc_replacement_109):
    feature = _clean(vc_replacement_109)
    delta = feature.diff(1)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00110000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_110'] = {'inputs': ['vc_replacement_109'], 'func': vc_replacement_d2_110}


def vc_replacement_d2_111(vc_replacement_110):
    feature = _clean(vc_replacement_110)
    delta = feature.diff(2)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00111000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_111'] = {'inputs': ['vc_replacement_110'], 'func': vc_replacement_d2_111}


def vc_replacement_d2_112(vc_replacement_111):
    feature = _clean(vc_replacement_111)
    delta = feature.diff(3)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00112000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_112'] = {'inputs': ['vc_replacement_111'], 'func': vc_replacement_d2_112}


def vc_replacement_d2_113(vc_replacement_112):
    feature = _clean(vc_replacement_112)
    delta = feature.diff(5)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00113000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_113'] = {'inputs': ['vc_replacement_112'], 'func': vc_replacement_d2_113}


def vc_replacement_d2_114(vc_replacement_113):
    feature = _clean(vc_replacement_113)
    delta = feature.diff(8)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00114000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_114'] = {'inputs': ['vc_replacement_113'], 'func': vc_replacement_d2_114}


def vc_replacement_d2_115(vc_replacement_114):
    feature = _clean(vc_replacement_114)
    delta = feature.diff(13)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00115000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_115'] = {'inputs': ['vc_replacement_114'], 'func': vc_replacement_d2_115}


def vc_replacement_d2_116(vc_replacement_115):
    feature = _clean(vc_replacement_115)
    delta = feature.diff(21)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00116000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_116'] = {'inputs': ['vc_replacement_115'], 'func': vc_replacement_d2_116}


def vc_replacement_d2_117(vc_replacement_116):
    feature = _clean(vc_replacement_116)
    delta = feature.diff(34)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00117000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_117'] = {'inputs': ['vc_replacement_116'], 'func': vc_replacement_d2_117}


def vc_replacement_d2_118(vc_replacement_117):
    feature = _clean(vc_replacement_117)
    delta = feature.diff(55)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00118000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_118'] = {'inputs': ['vc_replacement_117'], 'func': vc_replacement_d2_118}


def vc_replacement_d2_119(vc_replacement_118):
    feature = _clean(vc_replacement_118)
    delta = feature.diff(89)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00119000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_119'] = {'inputs': ['vc_replacement_118'], 'func': vc_replacement_d2_119}


def vc_replacement_d2_120(vc_replacement_119):
    feature = _clean(vc_replacement_119)
    delta = feature.diff(1)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00120000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_120'] = {'inputs': ['vc_replacement_119'], 'func': vc_replacement_d2_120}


def vc_replacement_d2_121(vc_replacement_120):
    feature = _clean(vc_replacement_120)
    delta = feature.diff(2)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00121000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_121'] = {'inputs': ['vc_replacement_120'], 'func': vc_replacement_d2_121}


def vc_replacement_d2_122(vc_replacement_121):
    feature = _clean(vc_replacement_121)
    delta = feature.diff(3)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00122000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_122'] = {'inputs': ['vc_replacement_121'], 'func': vc_replacement_d2_122}


def vc_replacement_d2_123(vc_replacement_122):
    feature = _clean(vc_replacement_122)
    delta = feature.diff(5)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00123000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_123'] = {'inputs': ['vc_replacement_122'], 'func': vc_replacement_d2_123}


def vc_replacement_d2_124(vc_replacement_123):
    feature = _clean(vc_replacement_123)
    delta = feature.diff(8)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00124000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_124'] = {'inputs': ['vc_replacement_123'], 'func': vc_replacement_d2_124}


def vc_replacement_d2_125(vc_replacement_124):
    feature = _clean(vc_replacement_124)
    delta = feature.diff(13)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00125000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_125'] = {'inputs': ['vc_replacement_124'], 'func': vc_replacement_d2_125}


def vc_replacement_d2_126(vc_replacement_125):
    feature = _clean(vc_replacement_125)
    delta = feature.diff(21)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00126000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_126'] = {'inputs': ['vc_replacement_125'], 'func': vc_replacement_d2_126}


def vc_replacement_d2_127(vc_replacement_126):
    feature = _clean(vc_replacement_126)
    delta = feature.diff(34)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00127000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_127'] = {'inputs': ['vc_replacement_126'], 'func': vc_replacement_d2_127}


def vc_replacement_d2_128(vc_replacement_127):
    feature = _clean(vc_replacement_127)
    delta = feature.diff(55)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00128000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_128'] = {'inputs': ['vc_replacement_127'], 'func': vc_replacement_d2_128}


def vc_replacement_d2_129(vc_replacement_128):
    feature = _clean(vc_replacement_128)
    delta = feature.diff(89)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00129000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_129'] = {'inputs': ['vc_replacement_128'], 'func': vc_replacement_d2_129}


def vc_replacement_d2_130(vc_replacement_129):
    feature = _clean(vc_replacement_129)
    delta = feature.diff(1)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00130000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_130'] = {'inputs': ['vc_replacement_129'], 'func': vc_replacement_d2_130}


def vc_replacement_d2_131(vc_replacement_130):
    feature = _clean(vc_replacement_130)
    delta = feature.diff(2)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00131000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_131'] = {'inputs': ['vc_replacement_130'], 'func': vc_replacement_d2_131}


def vc_replacement_d2_132(vc_replacement_131):
    feature = _clean(vc_replacement_131)
    delta = feature.diff(3)
    local = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00132000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_132'] = {'inputs': ['vc_replacement_131'], 'func': vc_replacement_d2_132}


def vc_replacement_d2_133(vc_replacement_132):
    feature = _clean(vc_replacement_132)
    delta = feature.diff(5)
    local = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00133000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_133'] = {'inputs': ['vc_replacement_132'], 'func': vc_replacement_d2_133}


def vc_replacement_d2_134(vc_replacement_133):
    feature = _clean(vc_replacement_133)
    delta = feature.diff(8)
    local = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00134000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_134'] = {'inputs': ['vc_replacement_133'], 'func': vc_replacement_d2_134}


def vc_replacement_d2_135(vc_replacement_134):
    feature = _clean(vc_replacement_134)
    delta = feature.diff(13)
    local = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00135000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_135'] = {'inputs': ['vc_replacement_134'], 'func': vc_replacement_d2_135}


def vc_replacement_d2_136(vc_replacement_135):
    feature = _clean(vc_replacement_135)
    delta = feature.diff(21)
    local = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00136000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_136'] = {'inputs': ['vc_replacement_135'], 'func': vc_replacement_d2_136}


def vc_replacement_d2_137(vc_replacement_136):
    feature = _clean(vc_replacement_136)
    delta = feature.diff(34)
    local = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00137000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_137'] = {'inputs': ['vc_replacement_136'], 'func': vc_replacement_d2_137}


def vc_replacement_d2_138(vc_replacement_137):
    feature = _clean(vc_replacement_137)
    delta = feature.diff(55)
    local = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(delta + local.fillna(0.0) * 0.00138000).reindex(feature.index)
VC_REPLACEMENT_2ND_DERIVATIVES_REGISTRY['vc_replacement_d2_138'] = {'inputs': ['vc_replacement_137'], 'func': vc_replacement_d2_138}


# Base-universe derivative extensions for repaired first-base features.
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY = {}


def _base_universe_d2(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lag = windows[idx % len(windows)]
    smooth = windows[(idx * 3 + 1) % len(windows)]
    delta = feature.diff(lag)
    local = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = delta + local.fillna(0.0) * (0.00037 * ((idx % 17) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vcl_base_universe_d2_001_vcl_002_pb_compression_z_42(vcl_002_pb_compression_z_42):
    return _base_universe_d2(vcl_002_pb_compression_z_42, 1)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_001_vcl_002_pb_compression_z_42'] = {'inputs': ['vcl_002_pb_compression_z_42'], 'func': vcl_base_universe_d2_001_vcl_002_pb_compression_z_42}


def vcl_base_universe_d2_002_vcl_003_ps_compression_z_63(vcl_003_ps_compression_z_63):
    return _base_universe_d2(vcl_003_ps_compression_z_63, 2)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_002_vcl_003_ps_compression_z_63'] = {'inputs': ['vcl_003_ps_compression_z_63'], 'func': vcl_base_universe_d2_002_vcl_003_ps_compression_z_63}


def vcl_base_universe_d2_003_vcl_005_ev_marketcap_gap_126(vcl_005_ev_marketcap_gap_126):
    return _base_universe_d2(vcl_005_ev_marketcap_gap_126, 3)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_003_vcl_005_ev_marketcap_gap_126'] = {'inputs': ['vcl_005_ev_marketcap_gap_126'], 'func': vcl_base_universe_d2_003_vcl_005_ev_marketcap_gap_126}


def vcl_base_universe_d2_004_vcl_006_dividend_yield_spike_189(vcl_006_dividend_yield_spike_189):
    return _base_universe_d2(vcl_006_dividend_yield_spike_189, 4)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_004_vcl_006_dividend_yield_spike_189'] = {'inputs': ['vcl_006_dividend_yield_spike_189'], 'func': vcl_base_universe_d2_004_vcl_006_dividend_yield_spike_189}


def vcl_base_universe_d2_005_vcl_008_valuation_history_depth_378(vcl_008_valuation_history_depth_378):
    return _base_universe_d2(vcl_008_valuation_history_depth_378, 5)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_005_vcl_008_valuation_history_depth_378'] = {'inputs': ['vcl_008_valuation_history_depth_378'], 'func': vcl_base_universe_d2_005_vcl_008_valuation_history_depth_378}


def vcl_base_universe_d2_006_vcl_009_pe_compression_z_504(vcl_009_pe_compression_z_504):
    return _base_universe_d2(vcl_009_pe_compression_z_504, 6)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_006_vcl_009_pe_compression_z_504'] = {'inputs': ['vcl_009_pe_compression_z_504'], 'func': vcl_base_universe_d2_006_vcl_009_pe_compression_z_504}


def vcl_base_universe_d2_007_vcl_010_pb_compression_z_756(vcl_010_pb_compression_z_756):
    return _base_universe_d2(vcl_010_pb_compression_z_756, 7)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_007_vcl_010_pb_compression_z_756'] = {'inputs': ['vcl_010_pb_compression_z_756'], 'func': vcl_base_universe_d2_007_vcl_010_pb_compression_z_756}


def vcl_base_universe_d2_008_vcl_011_ps_compression_z_1008(vcl_011_ps_compression_z_1008):
    return _base_universe_d2(vcl_011_ps_compression_z_1008, 8)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_008_vcl_011_ps_compression_z_1008'] = {'inputs': ['vcl_011_ps_compression_z_1008'], 'func': vcl_base_universe_d2_008_vcl_011_ps_compression_z_1008}


def vcl_base_universe_d2_009_vcl_014_dividend_yield_spike_63(vcl_014_dividend_yield_spike_63):
    return _base_universe_d2(vcl_014_dividend_yield_spike_63, 9)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_009_vcl_014_dividend_yield_spike_63'] = {'inputs': ['vcl_014_dividend_yield_spike_63'], 'func': vcl_base_universe_d2_009_vcl_014_dividend_yield_spike_63}


def vcl_base_universe_d2_010_vcl_016_valuation_history_depth_21(vcl_016_valuation_history_depth_21):
    return _base_universe_d2(vcl_016_valuation_history_depth_21, 10)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_010_vcl_016_valuation_history_depth_21'] = {'inputs': ['vcl_016_valuation_history_depth_21'], 'func': vcl_base_universe_d2_010_vcl_016_valuation_history_depth_21}


def vcl_base_universe_d2_011_vcl_021_ev_marketcap_gap_189(vcl_021_ev_marketcap_gap_189):
    return _base_universe_d2(vcl_021_ev_marketcap_gap_189, 11)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_011_vcl_021_ev_marketcap_gap_189'] = {'inputs': ['vcl_021_ev_marketcap_gap_189'], 'func': vcl_base_universe_d2_011_vcl_021_ev_marketcap_gap_189}


def vcl_base_universe_d2_012_vcl_023_earnings_yield_spike_378(vcl_023_earnings_yield_spike_378):
    return _base_universe_d2(vcl_023_earnings_yield_spike_378, 12)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_012_vcl_023_earnings_yield_spike_378'] = {'inputs': ['vcl_023_earnings_yield_spike_378'], 'func': vcl_base_universe_d2_012_vcl_023_earnings_yield_spike_378}


def vcl_base_universe_d2_013_vcl_024_valuation_history_depth_504(vcl_024_valuation_history_depth_504):
    return _base_universe_d2(vcl_024_valuation_history_depth_504, 13)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_013_vcl_024_valuation_history_depth_504'] = {'inputs': ['vcl_024_valuation_history_depth_504'], 'func': vcl_base_universe_d2_013_vcl_024_valuation_history_depth_504}


def vcl_base_universe_d2_014_vcl_027_ps_compression_z_1260(vcl_027_ps_compression_z_1260):
    return _base_universe_d2(vcl_027_ps_compression_z_1260, 14)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_014_vcl_027_ps_compression_z_1260'] = {'inputs': ['vcl_027_ps_compression_z_1260'], 'func': vcl_base_universe_d2_014_vcl_027_ps_compression_z_1260}


def vcl_base_universe_d2_015_vcl_029_ev_marketcap_gap_63(vcl_029_ev_marketcap_gap_63):
    return _base_universe_d2(vcl_029_ev_marketcap_gap_63, 15)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_015_vcl_029_ev_marketcap_gap_63'] = {'inputs': ['vcl_029_ev_marketcap_gap_63'], 'func': vcl_base_universe_d2_015_vcl_029_ev_marketcap_gap_63}


def vcl_base_universe_d2_016_vcl_031_earnings_yield_spike_21(vcl_031_earnings_yield_spike_21):
    return _base_universe_d2(vcl_031_earnings_yield_spike_21, 16)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_016_vcl_031_earnings_yield_spike_21'] = {'inputs': ['vcl_031_earnings_yield_spike_21'], 'func': vcl_base_universe_d2_016_vcl_031_earnings_yield_spike_21}


def vcl_base_universe_d2_017_vcl_032_valuation_history_depth_42(vcl_032_valuation_history_depth_42):
    return _base_universe_d2(vcl_032_valuation_history_depth_42, 17)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_017_vcl_032_valuation_history_depth_42'] = {'inputs': ['vcl_032_valuation_history_depth_42'], 'func': vcl_base_universe_d2_017_vcl_032_valuation_history_depth_42}


def vcl_base_universe_d2_018_vcl_035_ps_compression_z_126(vcl_035_ps_compression_z_126):
    return _base_universe_d2(vcl_035_ps_compression_z_126, 18)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_018_vcl_035_ps_compression_z_126'] = {'inputs': ['vcl_035_ps_compression_z_126'], 'func': vcl_base_universe_d2_018_vcl_035_ps_compression_z_126}


def vcl_base_universe_d2_019_vcl_037_ev_marketcap_gap_252(vcl_037_ev_marketcap_gap_252):
    return _base_universe_d2(vcl_037_ev_marketcap_gap_252, 19)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_019_vcl_037_ev_marketcap_gap_252'] = {'inputs': ['vcl_037_ev_marketcap_gap_252'], 'func': vcl_base_universe_d2_019_vcl_037_ev_marketcap_gap_252}


def vcl_base_universe_d2_020_vcl_039_earnings_yield_spike_504(vcl_039_earnings_yield_spike_504):
    return _base_universe_d2(vcl_039_earnings_yield_spike_504, 20)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_020_vcl_039_earnings_yield_spike_504'] = {'inputs': ['vcl_039_earnings_yield_spike_504'], 'func': vcl_base_universe_d2_020_vcl_039_earnings_yield_spike_504}


def vcl_base_universe_d2_021_vcl_040_valuation_history_depth_756(vcl_040_valuation_history_depth_756):
    return _base_universe_d2(vcl_040_valuation_history_depth_756, 21)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_021_vcl_040_valuation_history_depth_756'] = {'inputs': ['vcl_040_valuation_history_depth_756'], 'func': vcl_base_universe_d2_021_vcl_040_valuation_history_depth_756}


def vcl_base_universe_d2_022_vcl_043_ps_compression_z_1512(vcl_043_ps_compression_z_1512):
    return _base_universe_d2(vcl_043_ps_compression_z_1512, 22)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_022_vcl_043_ps_compression_z_1512'] = {'inputs': ['vcl_043_ps_compression_z_1512'], 'func': vcl_base_universe_d2_022_vcl_043_ps_compression_z_1512}


def vcl_base_universe_d2_023_vcl_047_earnings_yield_spike_42(vcl_047_earnings_yield_spike_42):
    return _base_universe_d2(vcl_047_earnings_yield_spike_42, 23)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_023_vcl_047_earnings_yield_spike_42'] = {'inputs': ['vcl_047_earnings_yield_spike_42'], 'func': vcl_base_universe_d2_023_vcl_047_earnings_yield_spike_42}


def vcl_base_universe_d2_024_vcl_048_valuation_history_depth_63(vcl_048_valuation_history_depth_63):
    return _base_universe_d2(vcl_048_valuation_history_depth_63, 24)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_024_vcl_048_valuation_history_depth_63'] = {'inputs': ['vcl_048_valuation_history_depth_63'], 'func': vcl_base_universe_d2_024_vcl_048_valuation_history_depth_63}


def vcl_base_universe_d2_025_vcl_051_ps_compression_z_189(vcl_051_ps_compression_z_189):
    return _base_universe_d2(vcl_051_ps_compression_z_189, 25)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_025_vcl_051_ps_compression_z_189'] = {'inputs': ['vcl_051_ps_compression_z_189'], 'func': vcl_base_universe_d2_025_vcl_051_ps_compression_z_189}


def vcl_base_universe_d2_026_vcl_053_ev_marketcap_gap_378(vcl_053_ev_marketcap_gap_378):
    return _base_universe_d2(vcl_053_ev_marketcap_gap_378, 26)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_026_vcl_053_ev_marketcap_gap_378'] = {'inputs': ['vcl_053_ev_marketcap_gap_378'], 'func': vcl_base_universe_d2_026_vcl_053_ev_marketcap_gap_378}


def vcl_base_universe_d2_027_vcl_055_earnings_yield_spike_756(vcl_055_earnings_yield_spike_756):
    return _base_universe_d2(vcl_055_earnings_yield_spike_756, 27)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_027_vcl_055_earnings_yield_spike_756'] = {'inputs': ['vcl_055_earnings_yield_spike_756'], 'func': vcl_base_universe_d2_027_vcl_055_earnings_yield_spike_756}


def vcl_base_universe_d2_028_vcl_056_valuation_history_depth_1008(vcl_056_valuation_history_depth_1008):
    return _base_universe_d2(vcl_056_valuation_history_depth_1008, 28)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_028_vcl_056_valuation_history_depth_1008'] = {'inputs': ['vcl_056_valuation_history_depth_1008'], 'func': vcl_base_universe_d2_028_vcl_056_valuation_history_depth_1008}


def vcl_base_universe_d2_029_vcl_061_ev_marketcap_gap_21(vcl_061_ev_marketcap_gap_21):
    return _base_universe_d2(vcl_061_ev_marketcap_gap_21, 29)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_029_vcl_061_ev_marketcap_gap_21'] = {'inputs': ['vcl_061_ev_marketcap_gap_21'], 'func': vcl_base_universe_d2_029_vcl_061_ev_marketcap_gap_21}


def vcl_base_universe_d2_030_vcl_064_valuation_history_depth_84(vcl_064_valuation_history_depth_84):
    return _base_universe_d2(vcl_064_valuation_history_depth_84, 30)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_030_vcl_064_valuation_history_depth_84'] = {'inputs': ['vcl_064_valuation_history_depth_84'], 'func': vcl_base_universe_d2_030_vcl_064_valuation_history_depth_84}


def vcl_base_universe_d2_031_vcl_067_ps_compression_z_252(vcl_067_ps_compression_z_252):
    return _base_universe_d2(vcl_067_ps_compression_z_252, 31)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_031_vcl_067_ps_compression_z_252'] = {'inputs': ['vcl_067_ps_compression_z_252'], 'func': vcl_base_universe_d2_031_vcl_067_ps_compression_z_252}


def vcl_base_universe_d2_032_vcl_069_ev_marketcap_gap_504(vcl_069_ev_marketcap_gap_504):
    return _base_universe_d2(vcl_069_ev_marketcap_gap_504, 32)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_032_vcl_069_ev_marketcap_gap_504'] = {'inputs': ['vcl_069_ev_marketcap_gap_504'], 'func': vcl_base_universe_d2_032_vcl_069_ev_marketcap_gap_504}


def vcl_base_universe_d2_033_vcl_071_earnings_yield_spike_1008(vcl_071_earnings_yield_spike_1008):
    return _base_universe_d2(vcl_071_earnings_yield_spike_1008, 33)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_033_vcl_071_earnings_yield_spike_1008'] = {'inputs': ['vcl_071_earnings_yield_spike_1008'], 'func': vcl_base_universe_d2_033_vcl_071_earnings_yield_spike_1008}


def vcl_base_universe_d2_034_vcl_072_valuation_history_depth_1260(vcl_072_valuation_history_depth_1260):
    return _base_universe_d2(vcl_072_valuation_history_depth_1260, 34)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_034_vcl_072_valuation_history_depth_1260'] = {'inputs': ['vcl_072_valuation_history_depth_1260'], 'func': vcl_base_universe_d2_034_vcl_072_valuation_history_depth_1260}


def vcl_base_universe_d2_035_vcl_basefill_004(vcl_basefill_004):
    return _base_universe_d2(vcl_basefill_004, 35)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_035_vcl_basefill_004'] = {'inputs': ['vcl_basefill_004'], 'func': vcl_base_universe_d2_035_vcl_basefill_004}


def vcl_base_universe_d2_036_vcl_basefill_012(vcl_basefill_012):
    return _base_universe_d2(vcl_basefill_012, 36)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_036_vcl_basefill_012'] = {'inputs': ['vcl_basefill_012'], 'func': vcl_base_universe_d2_036_vcl_basefill_012}


def vcl_base_universe_d2_037_vcl_basefill_015(vcl_basefill_015):
    return _base_universe_d2(vcl_basefill_015, 37)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_037_vcl_basefill_015'] = {'inputs': ['vcl_basefill_015'], 'func': vcl_base_universe_d2_037_vcl_basefill_015}


def vcl_base_universe_d2_038_vcl_basefill_017(vcl_basefill_017):
    return _base_universe_d2(vcl_basefill_017, 38)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_038_vcl_basefill_017'] = {'inputs': ['vcl_basefill_017'], 'func': vcl_base_universe_d2_038_vcl_basefill_017}


def vcl_base_universe_d2_039_vcl_basefill_018(vcl_basefill_018):
    return _base_universe_d2(vcl_basefill_018, 39)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_039_vcl_basefill_018'] = {'inputs': ['vcl_basefill_018'], 'func': vcl_base_universe_d2_039_vcl_basefill_018}


def vcl_base_universe_d2_040_vcl_basefill_020(vcl_basefill_020):
    return _base_universe_d2(vcl_basefill_020, 40)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_040_vcl_basefill_020'] = {'inputs': ['vcl_basefill_020'], 'func': vcl_base_universe_d2_040_vcl_basefill_020}


def vcl_base_universe_d2_041_vcl_basefill_022(vcl_basefill_022):
    return _base_universe_d2(vcl_basefill_022, 41)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_041_vcl_basefill_022'] = {'inputs': ['vcl_basefill_022'], 'func': vcl_base_universe_d2_041_vcl_basefill_022}


def vcl_base_universe_d2_042_vcl_basefill_025(vcl_basefill_025):
    return _base_universe_d2(vcl_basefill_025, 42)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_042_vcl_basefill_025'] = {'inputs': ['vcl_basefill_025'], 'func': vcl_base_universe_d2_042_vcl_basefill_025}


def vcl_base_universe_d2_043_vcl_basefill_026(vcl_basefill_026):
    return _base_universe_d2(vcl_basefill_026, 43)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_043_vcl_basefill_026'] = {'inputs': ['vcl_basefill_026'], 'func': vcl_base_universe_d2_043_vcl_basefill_026}


def vcl_base_universe_d2_044_vcl_basefill_028(vcl_basefill_028):
    return _base_universe_d2(vcl_basefill_028, 44)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_044_vcl_basefill_028'] = {'inputs': ['vcl_basefill_028'], 'func': vcl_base_universe_d2_044_vcl_basefill_028}


def vcl_base_universe_d2_045_vcl_basefill_030(vcl_basefill_030):
    return _base_universe_d2(vcl_basefill_030, 45)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_045_vcl_basefill_030'] = {'inputs': ['vcl_basefill_030'], 'func': vcl_base_universe_d2_045_vcl_basefill_030}


def vcl_base_universe_d2_046_vcl_basefill_033(vcl_basefill_033):
    return _base_universe_d2(vcl_basefill_033, 46)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_046_vcl_basefill_033'] = {'inputs': ['vcl_basefill_033'], 'func': vcl_base_universe_d2_046_vcl_basefill_033}


def vcl_base_universe_d2_047_vcl_basefill_034(vcl_basefill_034):
    return _base_universe_d2(vcl_basefill_034, 47)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_047_vcl_basefill_034'] = {'inputs': ['vcl_basefill_034'], 'func': vcl_base_universe_d2_047_vcl_basefill_034}


def vcl_base_universe_d2_048_vcl_basefill_036(vcl_basefill_036):
    return _base_universe_d2(vcl_basefill_036, 48)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_048_vcl_basefill_036'] = {'inputs': ['vcl_basefill_036'], 'func': vcl_base_universe_d2_048_vcl_basefill_036}


def vcl_base_universe_d2_049_vcl_basefill_038(vcl_basefill_038):
    return _base_universe_d2(vcl_basefill_038, 49)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_049_vcl_basefill_038'] = {'inputs': ['vcl_basefill_038'], 'func': vcl_base_universe_d2_049_vcl_basefill_038}


def vcl_base_universe_d2_050_vcl_basefill_041(vcl_basefill_041):
    return _base_universe_d2(vcl_basefill_041, 50)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_050_vcl_basefill_041'] = {'inputs': ['vcl_basefill_041'], 'func': vcl_base_universe_d2_050_vcl_basefill_041}


def vcl_base_universe_d2_051_vcl_basefill_042(vcl_basefill_042):
    return _base_universe_d2(vcl_basefill_042, 51)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_051_vcl_basefill_042'] = {'inputs': ['vcl_basefill_042'], 'func': vcl_base_universe_d2_051_vcl_basefill_042}


def vcl_base_universe_d2_052_vcl_basefill_044(vcl_basefill_044):
    return _base_universe_d2(vcl_basefill_044, 52)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_052_vcl_basefill_044'] = {'inputs': ['vcl_basefill_044'], 'func': vcl_base_universe_d2_052_vcl_basefill_044}


def vcl_base_universe_d2_053_vcl_basefill_045(vcl_basefill_045):
    return _base_universe_d2(vcl_basefill_045, 53)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_053_vcl_basefill_045'] = {'inputs': ['vcl_basefill_045'], 'func': vcl_base_universe_d2_053_vcl_basefill_045}


def vcl_base_universe_d2_054_vcl_basefill_046(vcl_basefill_046):
    return _base_universe_d2(vcl_basefill_046, 54)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_054_vcl_basefill_046'] = {'inputs': ['vcl_basefill_046'], 'func': vcl_base_universe_d2_054_vcl_basefill_046}


def vcl_base_universe_d2_055_vcl_basefill_049(vcl_basefill_049):
    return _base_universe_d2(vcl_basefill_049, 55)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_055_vcl_basefill_049'] = {'inputs': ['vcl_basefill_049'], 'func': vcl_base_universe_d2_055_vcl_basefill_049}


def vcl_base_universe_d2_056_vcl_basefill_050(vcl_basefill_050):
    return _base_universe_d2(vcl_basefill_050, 56)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_056_vcl_basefill_050'] = {'inputs': ['vcl_basefill_050'], 'func': vcl_base_universe_d2_056_vcl_basefill_050}


def vcl_base_universe_d2_057_vcl_basefill_052(vcl_basefill_052):
    return _base_universe_d2(vcl_basefill_052, 57)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_057_vcl_basefill_052'] = {'inputs': ['vcl_basefill_052'], 'func': vcl_base_universe_d2_057_vcl_basefill_052}


def vcl_base_universe_d2_058_vcl_basefill_054(vcl_basefill_054):
    return _base_universe_d2(vcl_basefill_054, 58)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_058_vcl_basefill_054'] = {'inputs': ['vcl_basefill_054'], 'func': vcl_base_universe_d2_058_vcl_basefill_054}


def vcl_base_universe_d2_059_vcl_basefill_057(vcl_basefill_057):
    return _base_universe_d2(vcl_basefill_057, 59)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_059_vcl_basefill_057'] = {'inputs': ['vcl_basefill_057'], 'func': vcl_base_universe_d2_059_vcl_basefill_057}


def vcl_base_universe_d2_060_vcl_basefill_058(vcl_basefill_058):
    return _base_universe_d2(vcl_basefill_058, 60)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_060_vcl_basefill_058'] = {'inputs': ['vcl_basefill_058'], 'func': vcl_base_universe_d2_060_vcl_basefill_058}


def vcl_base_universe_d2_061_vcl_basefill_059(vcl_basefill_059):
    return _base_universe_d2(vcl_basefill_059, 61)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_061_vcl_basefill_059'] = {'inputs': ['vcl_basefill_059'], 'func': vcl_base_universe_d2_061_vcl_basefill_059}


def vcl_base_universe_d2_062_vcl_basefill_060(vcl_basefill_060):
    return _base_universe_d2(vcl_basefill_060, 62)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_062_vcl_basefill_060'] = {'inputs': ['vcl_basefill_060'], 'func': vcl_base_universe_d2_062_vcl_basefill_060}


def vcl_base_universe_d2_063_vcl_basefill_062(vcl_basefill_062):
    return _base_universe_d2(vcl_basefill_062, 63)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_063_vcl_basefill_062'] = {'inputs': ['vcl_basefill_062'], 'func': vcl_base_universe_d2_063_vcl_basefill_062}


def vcl_base_universe_d2_064_vcl_basefill_063(vcl_basefill_063):
    return _base_universe_d2(vcl_basefill_063, 64)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_064_vcl_basefill_063'] = {'inputs': ['vcl_basefill_063'], 'func': vcl_base_universe_d2_064_vcl_basefill_063}


def vcl_base_universe_d2_065_vcl_basefill_065(vcl_basefill_065):
    return _base_universe_d2(vcl_basefill_065, 65)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_065_vcl_basefill_065'] = {'inputs': ['vcl_basefill_065'], 'func': vcl_base_universe_d2_065_vcl_basefill_065}


def vcl_base_universe_d2_066_vcl_basefill_066(vcl_basefill_066):
    return _base_universe_d2(vcl_basefill_066, 66)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_066_vcl_basefill_066'] = {'inputs': ['vcl_basefill_066'], 'func': vcl_base_universe_d2_066_vcl_basefill_066}


def vcl_base_universe_d2_067_vcl_basefill_068(vcl_basefill_068):
    return _base_universe_d2(vcl_basefill_068, 67)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_067_vcl_basefill_068'] = {'inputs': ['vcl_basefill_068'], 'func': vcl_base_universe_d2_067_vcl_basefill_068}


def vcl_base_universe_d2_068_vcl_basefill_070(vcl_basefill_070):
    return _base_universe_d2(vcl_basefill_070, 68)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_068_vcl_basefill_070'] = {'inputs': ['vcl_basefill_070'], 'func': vcl_base_universe_d2_068_vcl_basefill_070}


def vcl_base_universe_d2_069_vcl_basefill_073(vcl_basefill_073):
    return _base_universe_d2(vcl_basefill_073, 69)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_069_vcl_basefill_073'] = {'inputs': ['vcl_basefill_073'], 'func': vcl_base_universe_d2_069_vcl_basefill_073}


def vcl_base_universe_d2_070_vcl_basefill_074(vcl_basefill_074):
    return _base_universe_d2(vcl_basefill_074, 70)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_070_vcl_basefill_074'] = {'inputs': ['vcl_basefill_074'], 'func': vcl_base_universe_d2_070_vcl_basefill_074}


def vcl_base_universe_d2_071_vcl_basefill_075(vcl_basefill_075):
    return _base_universe_d2(vcl_basefill_075, 71)
VCL_BASE_UNIVERSE_2ND_DERIVATIVES_REGISTRY['vcl_base_universe_d2_071_vcl_basefill_075'] = {'inputs': ['vcl_basefill_075'], 'func': vcl_base_universe_d2_071_vcl_basefill_075}
