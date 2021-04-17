const region = {
    'CBD': 0,
    'Qilizhuang': 1,
    'Wanshou Road': 2,
    'Wanliu': 3,
    'Wanda': 4,
    'Sanyuanqiao': 5,
    'Sanlitun': 6,
    'Shangdi': 7,
    'Century City': 8,
    'Dongguan': 9,
    'Dongdan': 10,
    'Dongsi': 11,
    'Dongba': 12,
    'East Bridge': 13,
    'Dongzhimen': 14,
    'Donghua Market': 15,
    'Zhongguancun': 16,
    'Central Villa': 17,
    'Fengtai others': 18,
    'Linheli': 19,
    'Lizer': 20,
    'Yihezhuang': 21,
    'Qiaozhuang': 22,
    'jiukeshuCarrefour': 23,
    'Erlizhuang': 24,
    'Wukesong': 25,
    'Wudaokou': 26,
    'Wulidian': 27,
    'Asian Games Village': 28,
    'Asian Games Village Camp': 29,
    'crossing': 30,
    'Yizhuang': 31,
    'Others in Yizhuang Development Zone': 32,
    'Liangmaqiao': 33,
    'Jianxiangqiao': 34,
    'Anise': 35,
    'princess grave': 36,
    'Liuli bridge': 37,
    'Liupu Kang': 38,
    'Junbo': 39,
    'Agricultural Exhibition Hall': 40,
    'Feng Village': 41,
    'Liu Jia Yao': 42,
    'front door': 43,
    'Jinsong': 44,
    'Beiqijia': 45,
    'Beijing South Railway Station': 46,
    'Beiguan': 47,
    'Beidadi': 48,
    'Beitaipingzhuang': 49,
    'Beijing University of Technology': 50,
    'Beiyuan': 51,
    'Shibalidian': 52,
    'Shilibao': 53,
    'Shilibao Town': 54,
    'Shilihe': 55,
    'Huawei bridge': 56,
    'south central axis airport business district': 57,
    'Nankou': 58,
    'south Beach': 59,
    'Nanshao': 60,
    'Lugou Bridge': 61,
    'Changwa': 62,
    'shuangjing': 63,
    'double bridge': 64,
    'shuangyushu': 65,
    'Gubeikou Town': 66,
    'Ancient city': 67,
    'Youanmennei': 68,
    'youanmenwai': 69,
    'Houshayu': 70,
    'Heyi': 71,
    'Peace Lane': 72,
    'sijiqing': 73,
    'Sihui': 74,
    'Huiguan': 75,
    'Tuanjie Lake': 76,
    'National Exhibition': 77,
    'Yuanmingyuan': 78,
    'Dianmen': 79,
    'kuatou': 80,
    'Chengguan': 81,
    'Chengzi': 82,
    'Daxing others': 83,
    'Daxing new airport': 84,
    'daxing new airport villa area': 85,
    'Dashanzi': 86,
    'Dayu': 87,
    'Dawang road': 88,
    'Dahongmen': 89,
    'The temple of heaven': 90,
    'Tianning Temple': 91,
    'Tiangongyuan': 92,
    'Tiangongyuan South': 93,
    'tiantongyuan': 94,
    'Taiping Bridge': 95,
    'Sun Palace': 96,
    'Olympic Park': 97,
    'Xueyuan Road': 98,
    'Anning Village': 99,
    'Andingmen': 100,
    'Anzhen': 101,
    'songjiazhuang': 102,
    'Guanyuan': 103,
    'Dinghui Temple': 104,
    'Dingfu Village': 105,
    'Xuanwumen': 106,
    'Miyun others': 107,
    'Miyun Town': 108,
    'Xiaotangshan': 109,
    'Xiaoxitian': 110,
    'Yuegezhuang': 111,
    'Chongwenmen': 112,
    'Gongti': 113,
    'Zuoanmen': 114,
    'Changying': 115,
    'Pinggu others': 116,
    'Guanganmen': 117,
    'Guangqumen': 118,
    'Yanqing others': 119,
    'Jianguo men Nei': 120,
    'Outside Jianguo': 121,
    'Deshengmen': 122,
    'Huairou': 123,
    'Huixin West Street': 124,
    'Chengshou Temple': 125,
    'Fangshan others': 126,
    'New palace': 127,
    'Xinjiekou': 128,
    'Fangzhuang': 129,
    'Old palace': 130,
    'Changping others': 131,
    'Yuetan': 132,
    'Wangjing': 133,
    'Chaoyang Park': 134,
    'Chaoyang others': 135,
    'Inside Chaoyang Gate': 136,
    'Outside Chaoyang Gate': 137,
    'Chaoqing': 138,
    'Muxiyuan': 139,
    'muxidi': 140,
    'Li Qiao': 141,
    'Yangzhuang': 142,
    'Orchard': 143,
    'Orchard Street': 144,
    'Jujube Garden': 145,
    'pear garden': 146,
    'Happy Valley': 147,
    'Wuyi Garden': 148,
    'Yongdingmen': 149,
    'Shahe': 150,
    'Foreign bridge': 151,
    'Haidian others': 152,
    'Haidian North New District': 153,
    'Qinghe': 154,
    'Xiwengzhuang Town': 155,
    'riverside West': 156,
    'Pan Jiayuan': 157,
    'Lu Yuan': 158,
    'Yinghai': 159,
    'dengshikou': 160,
    'Yanshan': 161,
    'Yansha': 162,
    'Niujie': 163,
    'Peony Garden': 164,
    'Jade bridge': 165,
    'Yuquanying': 166,
    'Yuquan Road': 167,
    'Liuli River': 168,
    'Ganjiakou': 169,
    'Manna garden': 170,
    'Sweet water garden': 171,
    'Tiancun': 172,
    'Baishiqiao': 173,
    'White paper shop': 174,
    'Baiziwan': 175,
    'Zaojun Temple': 176,
    'See Dan bridge': 177,
    'Zhichun Road': 178,
    'shifoying': 179,
    'shijingshan others': 180,
    'Shimen camp': 181,
    'science and Technology Park': 182,
    'Doudian': 183,
    'Lishui bridge': 184,
    'Guanzhuang': 185,
    'Zizhuqiao': 186,
    'Red temple': 187,
    'Laoshan': 188,
    'Good country': 189,
    'shaoyaoju': 190,
    'Hometown of flowers': 191,
    'Suzhou bridge': 192,
    'Apple Orchard': 193,
    'Caoqiao': 194,
    'Caihuying': 195,
    'Puhuangyu': 196,
    'Xisanqi': 197,
    'Xierqi': 198,
    'Xiguan Huandao': 199,
    'Xibeiwang': 200,
    'Xidan': 201,
    'Xisi': 202,
    'Xiba River': 203,
    'Xishan': 204,
    'Xizhimen': 205,
    'Xihongmen': 206,
    'Xiluoyuan': 207,
    'Guanyin Temple': 208,
    'Corner Gate': 209,
    'dougezhuang': 210,
    'Zhao Gongkou': 211,
    'Chegongzhuang': 212,
    'Tongzhou others': 213,
    'Tongzhou Beiyuan': 214,
    'Jiuxianqiao': 215,
    'Jinbao Street': 216,
    'Financial Street': 217,
    'Changchun Street': 218,
    'Changyang': 219,
    'Mentougou others': 220,
    'Yan Village': 221,
    'fumen': 222,
    'Taoran Pavilion': 223,
    'Huoying': 224,
    'green pagoda': 225,
    'Hancun River': 226,
    'Shunyi others': 227,
    'Shunyi City': 228,
    'Summer Palace': 229,
    'Capital Airport': 230,
    'Ma Po': 231,
    'Majiabao': 232,
    'Madian': 233,
    'malianwa': 234,
    'malian road': 235,
    'majuqiao': 236,
    'Gaobeidian': 237,
    'Gaomi shop': 238,
    'Weigong Village': 239,
    'Lugu': 240,
    'Huangcunzhong': 241,
    'Huangcun railway station': 242,
    'Gulou Street': 243,
    'Gulou Streets': 244
};

const district = {
    'Dongcheng': 0,
    'Fengtai': 1,
    'Yizhuang': 2,
    'Daxing': 3,
    'Miyun': 4,
    'Pinggu': 5,
    'Yanqing': 6,
    'Huairou': 7,
    'Fangshan': 8,
    'Changping': 9,
    'Chaoyang': 10,
    'Haidian': 11,
    'Shijingshan': 12,
    'Xicheng': 13,
    'Tongzhou': 14,
    'Mentougou': 15,
    'Shunyi': 16
};

const propertyInfo= {'non co ownership': 0, 'co ownership': 1};//  '产权信息': {'非共有': 0, '共有': 1},

// const  house_structure = {flat floor: 0, duplex: 1, skip floor: 2, staggered floor: 3, no data yet: 4};//'户型结构': {'平层': 0, "复式": 1, '跃层': 2, '错层': 3,'暂无数据':4},
const  house_structure = {'flat floor': 0, 'duplex': 1, 'skip floor': 2, 'staggered floor': 3};


// const building_type = {Banlou: 0, "tower": 1, banta combination: 2, bungalow: 3, no data yet: 4};// '建筑类型': {'板楼': 0, "塔楼": 1, '板塔结合': 2, '平房': 3, '暂无数据':4},
const building_type = {'Banlou': 0, "tower": 1, 'banta combination': 2, 'bungalow': 3};

// const building_structure = {
//     steel concrete structure: 0,
//     mixed structure: 1,
//     brick concrete structure: 2,
//     unknown structure: 3,
//     steel structure: 4,
//     brick wood structure: 5,
//     frame structure: 6
// };// '建筑结构': {'钢混结构': 0, "混合结构": 1, '砖混结构': 2, '未知结构': 3,'钢结构':4, '砖木结构': 5, '框架结构':6},
const building_structure = {
    'steel concrete structure': 0,
    'mixed structure': 1,
    'brick concrete structure': 2,
    'steel structure': 4,
    'brick wood structure': 5,
    'frame structure': 6
}

const decoration = {'hardcover': 0, 'simple decoration': 1, 'others': 2, 'rough': 3};//    '装修': {'精装': 0, "简装": 1, '其他': 2, '毛坯': 3},

// const heating = {central heating: 0, self heating: 1, no data yet: 2};//    '供暖': {'集中供暖': 0, "自供暖": 1, '暂无数据': 2},
const heating = {'central heating': 0, 'self heating': 1};

// const elevator = {yes: 0, no: 1, no data: 2};//  '电梯': {'有': 0, "无": 1, '暂无数据': 2},
const elevator = {'yes': 0, 'no': 1};

// const floor_type = {
//     middle floor: 0,
//     low floor: 1,
//     high floor: 2,
//     top floor: 3,
//     bottom floor: 4,
//     basement: 5,
//     unknown: 6
// };// '楼层类型': {'中楼层 ': 0, "低楼层 ": 1, '高楼层 ': 2, '顶层 ': 3,'底层 ':4, '地下室 ': 5, '未知 ':6}
const floor_type = {
    'middle floor': 0,
    'low floor': 1,
    'high floor': 2,
    'top floor': 3,
    'bottom floor': 4,
    'basement': 5,
}

const direction = {
    'east':0,
    'south':1,
    'west':2,
    'north':3,
    'southeast':4,
    'northeast':5,
    'southwest':6,
    'northwest':7,
};

export default {
    region,
    district,
    propertyInfo,
    house_structure,
    building_type,
    building_structure,
    decoration,
    heating,
    elevator,
    floor_type,
    direction
}
