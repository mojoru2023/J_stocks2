import time

import pyecharts.options as opts
from pyecharts.charts import Line
import os
import xlrd
import sys
from xlrd import xldate_as_tuple
import datetime
# 读取xlxs数据
# 数据处理整理
# 测试
# 可以部署到服务器上面！彻底解放人力！

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=line-log

目前无法实现的功能:

1、暂无
"""


from shutil import copyfile

#! -*- coding:utf-8 -*-
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import copy
import operator

app = Flask(__name__)



@app.route('/snz')
def js_j225():
    return render_template('us_zgg.html') # 在一个目录下,templates中


@app.route('/')
def index():
    return "部署测试"





def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

       # # if 去掉表头
       # if rowNum > 0:


    return dataFile


def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")



# 时间日期的转换




#float--->日期字符串？
def handle_date(dates):
    f_ =[]

    for item in dates:

        tuple = xldate_as_tuple(item, 0)
        excel_datetime=datetime.datetime(*tuple)
        f_.append(str(excel_datetime))

    return f_

# 需要修改纵坐标刻度 # 默认是从
def get_v(l):
    f =[]

    for num in range(0,len(l)-1):
        if l[0] != 0:

            f_da = "%.4f" % (l[num]/l[0]-1)

            f.append(f_da)
        else:
            f.append(0)



    return f

# 467
def jsIn_ep():
    y_data_1 = []
    y_data_2 = []
    y_data_3 = []
    y_data_4 = []
    y_data_5 = []
    y_data_6 = []
    y_data_7 = []
    y_data_8 = []
    y_data_9 = []
    y_data_10 = []
    y_data_11 = []
    y_data_12 = []
    y_data_13 = []
    y_data_14 = []
    y_data_15 = []
    y_data_16 = []
    y_data_17 = []
    y_data_18 = []
    y_data_19 = []
    y_data_20 = []
    y_data_21 = []
    y_data_22 = []
    y_data_23 = []
    y_data_24 = []
    y_data_25 = []
    y_data_26 = []
    y_data_27 = []
    y_data_28 = []
    y_data_29 = []
    y_data_30 = []
    y_data_31 = []
    y_data_32 = []
    y_data_33 = []
    y_data_34 = []
    y_data_35 = []
    y_data_36 = []
    y_data_37 = []
    y_data_38 = []
    y_data_39 = []
    y_data_40 = []
    y_data_41 = []
    y_data_42 = []
    y_data_43 = []
    y_data_44 = []
    y_data_45 = []
    y_data_46 = []
    y_data_47 = []
    y_data_48 = []
    y_data_49 = []
    y_data_50 = []
    y_data_51 = []
    y_data_52 = []
    y_data_53 = []
    y_data_54 = []
    y_data_55 = []
    y_data_56 = []
    y_data_57 = []
    y_data_58 = []
    y_data_59 = []
    y_data_60 = []
    y_data_61 = []
    y_data_62 = []
    y_data_63 = []
    y_data_64 = []
    y_data_65 = []
    y_data_66 = []
    y_data_67 = []
    y_data_68 = []
    y_data_69 = []
    y_data_70 = []
    y_data_71 = []
    y_data_72 = []
    y_data_73 = []
    y_data_74 = []
    y_data_75 = []
    y_data_76 = []
    y_data_77 = []
    y_data_78 = []
    y_data_79 = []
    y_data_80 = []
    y_data_81 = []
    y_data_82 = []
    y_data_83 = []
    y_data_84 = []
    y_data_85 = []
    y_data_86 = []
    y_data_87 = []
    y_data_88 = []
    y_data_89 = []
    y_data_90 = []
    y_data_91 = []
    y_data_92 = []
    y_data_93 = []
    y_data_94 = []
    y_data_95 = []
    y_data_96 = []
    y_data_97 = []
    y_data_98 = []
    y_data_99 = []
    y_data_100 = []
    y_data_101 = []
    y_data_102 = []
    y_data_103 = []
    y_data_104 = []
    y_data_105 = []
    y_data_106 = []
    y_data_107 = []
    y_data_108 = []
    y_data_109 = []
    y_data_110 = []
    y_data_111 = []
    y_data_112 = []
    y_data_113 = []
    y_data_114 = []
    y_data_115 = []
    y_data_116 = []
    y_data_117 = []
    y_data_118 = []
    y_data_119 = []
    y_data_120 = []
    y_data_121 = []
    y_data_122 = []
    y_data_123 = []
    y_data_124 = []
    y_data_125 = []
    y_data_126 = []
    y_data_127 = []
    y_data_128 = []
    y_data_129 = []
    y_data_130 = []
    y_data_131 = []
    y_data_132 = []
    y_data_133 = []
    y_data_134 = []
    y_data_135 = []
    y_data_136 = []
    y_data_137 = []
    y_data_138 = []
    y_data_139 = []
    y_data_140 = []
    y_data_141 = []
    y_data_142 = []
    y_data_143 = []
    y_data_144 = []
    y_data_145 = []
    y_data_146 = []
    y_data_147 = []
    y_data_148 = []
    y_data_149 = []
    y_data_150 = []
    y_data_151 = []
    y_data_152 = []
    y_data_153 = []
    y_data_154 = []
    y_data_155 = []
    y_data_156 = []
    y_data_157 = []
    y_data_158 = []
    y_data_159 = []
    y_data_160 = []
    y_data_161 = []
    y_data_162 = []
    y_data_163 = []
    y_data_164 = []
    y_data_165 = []
    y_data_166 = []
    y_data_167 = []
    y_data_168 = []
    y_data_169 = []
    y_data_170 = []
    y_data_171 = []
    y_data_172 = []
    y_data_173 = []
    y_data_174 = []
    y_data_175 = []
    y_data_176 = []
    y_data_177 = []
    y_data_178 = []
    y_data_179 = []
    y_data_180 = []
    y_data_181 = []
    y_data_182 = []
    y_data_183 = []
    y_data_184 = []
    y_data_185 = []
    y_data_186 = []
    y_data_187 = []
    y_data_188 = []
    y_data_189 = []
    y_data_190 = []
    y_data_191 = []
    y_data_192 = []
    y_data_193 = []
    y_data_194 = []
    y_data_195 = []
    y_data_196 = []
    y_data_197 = []
    y_data_198 = []
    y_data_199 = []
    y_data_200 = []
    y_data_201 = []
    y_data_202 = []
    y_data_203 = []
    y_data_204 = []
    y_data_205 = []
    y_data_206 = []
    y_data_207 = []
    y_data_208 = []
    y_data_209 = []
    y_data_210 = []
    y_data_211 = []
    y_data_212 = []
    y_data_213 = []
    y_data_214 = []
    y_data_215 = []
    y_data_216 = []
    y_data_217 = []
    y_data_218 = []
    y_data_219 = []
    y_data_220 = []
    y_data_221 = []
    y_data_222 = []
    y_data_223 = []
    y_data_224 = []
    y_data_225 = []
    y_data_226 = []
    y_data_227 = []
    y_data_228 = []
    y_data_229 = []
    y_data_230 = []
    y_data_231 = []
    y_data_232 = []
    y_data_233 = []
    y_data_234 = []
    y_data_235 = []
    y_data_236 = []
    y_data_237 = []
    y_data_238 = []
    y_data_239 = []
    y_data_240 = []
    y_data_241 = []
    y_data_242 = []
    y_data_243 = []
    y_data_244 = []
    y_data_245 = []
    y_data_246 = []
    y_data_247 = []
    y_data_248 = []
    y_data_249 = []
    y_data_250 = []
    y_data_251 = []
    y_data_252 = []
    y_data_253 = []
    y_data_254 = []
    y_data_255 = []
    y_data_256 = []
    y_data_257 = []
    y_data_258 = []
    y_data_259 = []
    y_data_260 = []
    y_data_261 = []
    y_data_262 = []
    y_data_263 = []
    y_data_264 = []
    y_data_265 = []
    y_data_266 = []
    y_data_267 = []
    y_data_268 = []
    y_data_269 = []
    y_data_270 = []
    y_data_271 = []
    y_data_272 = []
    y_data_273 = []
    y_data_274 = []
    y_data_275 = []
    y_data_276 = []
    y_data_277 = []
    y_data_278 = []
    y_data_279 = []
    y_data_280 = []
    y_data_281 = []
    y_data_282 = []
    y_data_283 = []
    y_data_284 = []
    y_data_285 = []
    y_data_286 = []
    y_data_287 = []
    y_data_288 = []
    y_data_289 = []
    y_data_290 = []
    y_data_291 = []
    y_data_292 = []
    y_data_293 = []
    y_data_294 = []
    y_data_295 = []
    y_data_296 = []
    y_data_297 = []
    y_data_298 = []
    y_data_299 = []
    y_data_300 = []
    y_data_301 = []
    y_data_302 = []
    y_data_303 = []
    y_data_304 = []
    y_data_305 = []
    y_data_306 = []
    y_data_307 = []
    y_data_308 = []
    y_data_309 = []
    y_data_310 = []
    y_data_311 = []
    y_data_312 = []
    y_data_313 = []
    y_data_314 = []
    y_data_315 = []
    y_data_316 = []
    y_data_317 = []
    y_data_318 = []
    y_data_319 = []
    y_data_320 = []
    y_data_321 = []
    y_data_322 = []
    y_data_323 = []
    y_data_324 = []
    y_data_325 = []
    y_data_326 = []
    y_data_327 = []
    y_data_328 = []
    y_data_329 = []
    y_data_330 = []
    y_data_331 = []
    y_data_332 = []
    y_data_333 = []
    y_data_334 = []
    y_data_335 = []
    y_data_336 = []
    y_data_337 = []
    y_data_338 = []
    y_data_339 = []
    y_data_340 = []
    y_data_341 = []
    y_data_342 = []
    y_data_343 = []
    y_data_344 = []
    y_data_345 = []
    y_data_346 = []
    y_data_347 = []
    y_data_348 = []
    y_data_349 = []
    y_data_350 = []
    y_data_351 = []
    y_data_352 = []
    y_data_353 = []
    y_data_354 = []
    y_data_355 = []
    y_data_356 = []
    y_data_357 = []
    y_data_358 = []
    y_data_359 = []
    y_data_360 = []
    y_data_361 = []
    y_data_362 = []
    y_data_363 = []
    y_data_364 = []
    y_data_365 = []
    y_data_366 = []
    y_data_367 = []
    y_data_368 = []
    y_data_369 = []
    y_data_370 = []
    y_data_371 = []
    y_data_372 = []
    y_data_373 = []
    y_data_374 = []
    y_data_375 = []
    y_data_376 = []
    y_data_377 = []
    y_data_378 = []
    y_data_379 = []
    y_data_380 = []
    y_data_381 = []
    y_data_382 = []
    y_data_383 = []
    y_data_384 = []
    y_data_385 = []
    y_data_386 = []
    y_data_387 = []
    y_data_388 = []
    y_data_389 = []
    y_data_390 = []
    y_data_391 = []
    y_data_392 = []
    y_data_393 = []
    y_data_394 = []
    y_data_395 = []
    y_data_396 = []
    y_data_397 = []
    y_data_398 = []
    y_data_399 = []
    y_data_400 = []
    y_data_401 = []
    y_data_402 = []
    y_data_403 = []
    y_data_404 = []
    y_data_405 = []
    y_data_406 = []
    y_data_407 = []
    y_data_408 = []
    y_data_409 = []
    y_data_410 = []
    y_data_411 = []
    y_data_412 = []
    y_data_413 = []
    y_data_414 = []
    y_data_415 = []
    y_data_416 = []
    y_data_417 = []
    y_data_418 = []
    y_data_419 = []
    y_data_420 = []
    y_data_421 = []
    y_data_422 = []
    y_data_423 = []
    y_data_424 = []
    y_data_425 = []
    y_data_426 = []
    y_data_427 = []
    y_data_428 = []
    y_data_429 = []
    y_data_430 = []
    y_data_431 = []
    y_data_432 = []
    y_data_433 = []
    y_data_434 = []
    y_data_435 = []
    y_data_436 = []
    y_data_437 = []
    y_data_438 = []
    y_data_439 = []
    y_data_440 = []
    y_data_441 = []
    y_data_442 = []
    y_data_443 = []
    y_data_444 = []
    y_data_445 = []
    y_data_446 = []
    y_data_447 = []
    y_data_448 = []
    y_data_449 = []
    y_data_450 = []
    y_data_451 = []
    y_data_452 = []
    y_data_453 = []
    y_data_454 = []
    y_data_455 = []
    y_data_456 = []
    y_data_457 = []
    y_data_458 = []
    y_data_459 = []
    y_data_460 = []
    y_data_461 = []
    y_data_462 = []
    y_data_463 = []
    y_data_464 = []
    y_data_465 = []
    y_data_466 = []
    y_data_467 = []

    date_ = []
    excelFile = 'SP_Nas_ZZG.xlsx'
    full_items = read_xlrd(excelFile=excelFile)
    for item in full_items:

        if type(item[2]) == float:
            y_data_1.append(item[2])
        if type(item[3]) == float:
            y_data_2.append(item[3])
        if type(item[4]) == float:
            y_data_3.append(item[4])
        if type(item[5]) == float:
            y_data_4.append(item[5])
        if type(item[6]) == float:
            y_data_5.append(item[6])
        if type(item[7]) == float:
            y_data_6.append(item[7])
        if type(item[8]) == float:
            y_data_7.append(item[8])
        if type(item[9]) == float:
            y_data_8.append(item[9])
        if type(item[10]) == float:
            y_data_9.append(item[10])
        if type(item[11]) == float:
            y_data_10.append(item[11])
        if type(item[12]) == float:
            y_data_11.append(item[12])
        if type(item[13]) == float:
            y_data_12.append(item[13])
        if type(item[14]) == float:
            y_data_13.append(item[14])
        if type(item[15]) == float:
            y_data_14.append(item[15])
        if type(item[16]) == float:
            y_data_15.append(item[16])
        if type(item[17]) == float:
            y_data_16.append(item[17])
        if type(item[18]) == float:
            y_data_17.append(item[18])
        if type(item[19]) == float:
            y_data_18.append(item[19])
        if type(item[20]) == float:
            y_data_19.append(item[20])
        if type(item[21]) == float:
            y_data_20.append(item[21])
        if type(item[22]) == float:
            y_data_21.append(item[22])
        if type(item[23]) == float:
            y_data_22.append(item[23])
        if type(item[24]) == float:
            y_data_23.append(item[24])
        if type(item[25]) == float:
            y_data_24.append(item[25])
        if type(item[26]) == float:
            y_data_25.append(item[26])
        if type(item[27]) == float:
            y_data_26.append(item[27])
        if type(item[28]) == float:
            y_data_27.append(item[28])
        if type(item[29]) == float:
            y_data_28.append(item[29])
        if type(item[30]) == float:
            y_data_29.append(item[30])
        if type(item[31]) == float:
            y_data_30.append(item[31])
        if type(item[32]) == float:
            y_data_31.append(item[32])
        if type(item[33]) == float:
            y_data_32.append(item[33])
        if type(item[34]) == float:
            y_data_33.append(item[34])
        if type(item[35]) == float:
            y_data_34.append(item[35])
        if type(item[36]) == float:
            y_data_35.append(item[36])
        if type(item[37]) == float:
            y_data_36.append(item[37])
        if type(item[38]) == float:
            y_data_37.append(item[38])
        if type(item[39]) == float:
            y_data_38.append(item[39])
        if type(item[40]) == float:
            y_data_39.append(item[40])
        if type(item[41]) == float:
            y_data_40.append(item[41])
        if type(item[42]) == float:
            y_data_41.append(item[42])
        if type(item[43]) == float:
            y_data_42.append(item[43])
        if type(item[44]) == float:
            y_data_43.append(item[44])
        if type(item[45]) == float:
            y_data_44.append(item[45])
        if type(item[46]) == float:
            y_data_45.append(item[46])
        if type(item[47]) == float:
            y_data_46.append(item[47])
        if type(item[48]) == float:
            y_data_47.append(item[48])
        if type(item[49]) == float:
            y_data_48.append(item[49])
        if type(item[50]) == float:
            y_data_49.append(item[50])
        if type(item[51]) == float:
            y_data_50.append(item[51])
        if type(item[52]) == float:
            y_data_51.append(item[52])
        if type(item[53]) == float:
            y_data_52.append(item[53])
        if type(item[54]) == float:
            y_data_53.append(item[54])
        if type(item[55]) == float:
            y_data_54.append(item[55])
        if type(item[56]) == float:
            y_data_55.append(item[56])
        if type(item[57]) == float:
            y_data_56.append(item[57])
        if type(item[58]) == float:
            y_data_57.append(item[58])
        if type(item[59]) == float:
            y_data_58.append(item[59])
        if type(item[60]) == float:
            y_data_59.append(item[60])
        if type(item[61]) == float:
            y_data_60.append(item[61])
        if type(item[62]) == float:
            y_data_61.append(item[62])
        if type(item[63]) == float:
            y_data_62.append(item[63])
        if type(item[64]) == float:
            y_data_63.append(item[64])
        if type(item[65]) == float:
            y_data_64.append(item[65])
        if type(item[66]) == float:
            y_data_65.append(item[66])
        if type(item[67]) == float:
            y_data_66.append(item[67])
        if type(item[68]) == float:
            y_data_67.append(item[68])
        if type(item[69]) == float:
            y_data_68.append(item[69])
        if type(item[70]) == float:
            y_data_69.append(item[70])
        if type(item[71]) == float:
            y_data_70.append(item[71])
        if type(item[72]) == float:
            y_data_71.append(item[72])
        if type(item[73]) == float:
            y_data_72.append(item[73])
        if type(item[74]) == float:
            y_data_73.append(item[74])
        if type(item[75]) == float:
            y_data_74.append(item[75])
        if type(item[76]) == float:
            y_data_75.append(item[76])
        if type(item[77]) == float:
            y_data_76.append(item[77])
        if type(item[78]) == float:
            y_data_77.append(item[78])
        if type(item[79]) == float:
            y_data_78.append(item[79])
        if type(item[80]) == float:
            y_data_79.append(item[80])
        if type(item[81]) == float:
            y_data_80.append(item[81])
        if type(item[82]) == float:
            y_data_81.append(item[82])
        if type(item[83]) == float:
            y_data_82.append(item[83])
        if type(item[84]) == float:
            y_data_83.append(item[84])
        if type(item[85]) == float:
            y_data_84.append(item[85])
        if type(item[86]) == float:
            y_data_85.append(item[86])
        if type(item[87]) == float:
            y_data_86.append(item[87])
        if type(item[88]) == float:
            y_data_87.append(item[88])
        if type(item[89]) == float:
            y_data_88.append(item[89])
        if type(item[90]) == float:
            y_data_89.append(item[90])
        if type(item[91]) == float:
            y_data_90.append(item[91])
        if type(item[92]) == float:
            y_data_91.append(item[92])
        if type(item[93]) == float:
            y_data_92.append(item[93])
        if type(item[94]) == float:
            y_data_93.append(item[94])
        if type(item[95]) == float:
            y_data_94.append(item[95])
        if type(item[96]) == float:
            y_data_95.append(item[96])
        if type(item[97]) == float:
            y_data_96.append(item[97])
        if type(item[98]) == float:
            y_data_97.append(item[98])
        if type(item[99]) == float:
            y_data_98.append(item[99])
        if type(item[100]) == float:
            y_data_99.append(item[100])
        if type(item[101]) == float:
            y_data_100.append(item[101])
        if type(item[102]) == float:
            y_data_101.append(item[102])
        if type(item[103]) == float:
            y_data_102.append(item[103])
        if type(item[104]) == float:
            y_data_103.append(item[104])
        if type(item[105]) == float:
            y_data_104.append(item[105])
        if type(item[106]) == float:
            y_data_105.append(item[106])
        if type(item[107]) == float:
            y_data_106.append(item[107])
        if type(item[108]) == float:
            y_data_107.append(item[108])
        if type(item[109]) == float:
            y_data_108.append(item[109])
        if type(item[110]) == float:
            y_data_109.append(item[110])
        if type(item[111]) == float:
            y_data_110.append(item[111])
        if type(item[112]) == float:
            y_data_111.append(item[112])
        if type(item[113]) == float:
            y_data_112.append(item[113])
        if type(item[114]) == float:
            y_data_113.append(item[114])
        if type(item[115]) == float:
            y_data_114.append(item[115])
        if type(item[116]) == float:
            y_data_115.append(item[116])
        if type(item[117]) == float:
            y_data_116.append(item[117])
        if type(item[118]) == float:
            y_data_117.append(item[118])
        if type(item[119]) == float:
            y_data_118.append(item[119])
        if type(item[120]) == float:
            y_data_119.append(item[120])
        if type(item[121]) == float:
            y_data_120.append(item[121])
        if type(item[122]) == float:
            y_data_121.append(item[122])
        if type(item[123]) == float:
            y_data_122.append(item[123])
        if type(item[124]) == float:
            y_data_123.append(item[124])
        if type(item[125]) == float:
            y_data_124.append(item[125])
        if type(item[126]) == float:
            y_data_125.append(item[126])
        if type(item[127]) == float:
            y_data_126.append(item[127])
        if type(item[128]) == float:
            y_data_127.append(item[128])
        if type(item[129]) == float:
            y_data_128.append(item[129])
        if type(item[130]) == float:
            y_data_129.append(item[130])
        if type(item[131]) == float:
            y_data_130.append(item[131])
        if type(item[132]) == float:
            y_data_131.append(item[132])
        if type(item[133]) == float:
            y_data_132.append(item[133])
        if type(item[134]) == float:
            y_data_133.append(item[134])
        if type(item[135]) == float:
            y_data_134.append(item[135])
        if type(item[136]) == float:
            y_data_135.append(item[136])
        if type(item[137]) == float:
            y_data_136.append(item[137])
        if type(item[138]) == float:
            y_data_137.append(item[138])
        if type(item[139]) == float:
            y_data_138.append(item[139])
        if type(item[140]) == float:
            y_data_139.append(item[140])
        if type(item[141]) == float:
            y_data_140.append(item[141])
        if type(item[142]) == float:
            y_data_141.append(item[142])
        if type(item[143]) == float:
            y_data_142.append(item[143])
        if type(item[144]) == float:
            y_data_143.append(item[144])
        if type(item[145]) == float:
            y_data_144.append(item[145])
        if type(item[146]) == float:
            y_data_145.append(item[146])
        if type(item[147]) == float:
            y_data_146.append(item[147])
        if type(item[148]) == float:
            y_data_147.append(item[148])
        if type(item[149]) == float:
            y_data_148.append(item[149])
        if type(item[150]) == float:
            y_data_149.append(item[150])
        if type(item[151]) == float:
            y_data_150.append(item[151])
        if type(item[152]) == float:
            y_data_151.append(item[152])
        if type(item[153]) == float:
            y_data_152.append(item[153])
        if type(item[154]) == float:
            y_data_153.append(item[154])
        if type(item[155]) == float:
            y_data_154.append(item[155])
        if type(item[156]) == float:
            y_data_155.append(item[156])
        if type(item[157]) == float:
            y_data_156.append(item[157])
        if type(item[158]) == float:
            y_data_157.append(item[158])
        if type(item[159]) == float:
            y_data_158.append(item[159])
        if type(item[160]) == float:
            y_data_159.append(item[160])
        if type(item[161]) == float:
            y_data_160.append(item[161])
        if type(item[162]) == float:
            y_data_161.append(item[162])
        if type(item[163]) == float:
            y_data_162.append(item[163])
        if type(item[164]) == float:
            y_data_163.append(item[164])
        if type(item[165]) == float:
            y_data_164.append(item[165])
        if type(item[166]) == float:
            y_data_165.append(item[166])
        if type(item[167]) == float:
            y_data_166.append(item[167])
        if type(item[168]) == float:
            y_data_167.append(item[168])
        if type(item[169]) == float:
            y_data_168.append(item[169])
        if type(item[170]) == float:
            y_data_169.append(item[170])
        if type(item[171]) == float:
            y_data_170.append(item[171])
        if type(item[172]) == float:
            y_data_171.append(item[172])
        if type(item[173]) == float:
            y_data_172.append(item[173])
        if type(item[174]) == float:
            y_data_173.append(item[174])
        if type(item[175]) == float:
            y_data_174.append(item[175])
        if type(item[176]) == float:
            y_data_175.append(item[176])
        if type(item[177]) == float:
            y_data_176.append(item[177])
        if type(item[178]) == float:
            y_data_177.append(item[178])
        if type(item[179]) == float:
            y_data_178.append(item[179])
        if type(item[180]) == float:
            y_data_179.append(item[180])
        if type(item[181]) == float:
            y_data_180.append(item[181])
        if type(item[182]) == float:
            y_data_181.append(item[182])
        if type(item[183]) == float:
            y_data_182.append(item[183])
        if type(item[184]) == float:
            y_data_183.append(item[184])
        if type(item[185]) == float:
            y_data_184.append(item[185])
        if type(item[186]) == float:
            y_data_185.append(item[186])
        if type(item[187]) == float:
            y_data_186.append(item[187])
        if type(item[188]) == float:
            y_data_187.append(item[188])
        if type(item[189]) == float:
            y_data_188.append(item[189])
        if type(item[190]) == float:
            y_data_189.append(item[190])
        if type(item[191]) == float:
            y_data_190.append(item[191])
        if type(item[192]) == float:
            y_data_191.append(item[192])
        if type(item[193]) == float:
            y_data_192.append(item[193])
        if type(item[194]) == float:
            y_data_193.append(item[194])
        if type(item[195]) == float:
            y_data_194.append(item[195])
        if type(item[196]) == float:
            y_data_195.append(item[196])
        if type(item[197]) == float:
            y_data_196.append(item[197])
        if type(item[198]) == float:
            y_data_197.append(item[198])
        if type(item[199]) == float:
            y_data_198.append(item[199])
        if type(item[200]) == float:
            y_data_199.append(item[200])
        if type(item[201]) == float:
            y_data_200.append(item[201])
        if type(item[202]) == float:
            y_data_201.append(item[202])
        if type(item[203]) == float:
            y_data_202.append(item[203])
        if type(item[204]) == float:
            y_data_203.append(item[204])
        if type(item[205]) == float:
            y_data_204.append(item[205])
        if type(item[206]) == float:
            y_data_205.append(item[206])
        if type(item[207]) == float:
            y_data_206.append(item[207])
        if type(item[208]) == float:
            y_data_207.append(item[208])
        if type(item[209]) == float:
            y_data_208.append(item[209])
        if type(item[210]) == float:
            y_data_209.append(item[210])
        if type(item[211]) == float:
            y_data_210.append(item[211])
        if type(item[212]) == float:
            y_data_211.append(item[212])
        if type(item[213]) == float:
            y_data_212.append(item[213])
        if type(item[214]) == float:
            y_data_213.append(item[214])
        if type(item[215]) == float:
            y_data_214.append(item[215])
        if type(item[216]) == float:
            y_data_215.append(item[216])
        if type(item[217]) == float:
            y_data_216.append(item[217])
        if type(item[218]) == float:
            y_data_217.append(item[218])
        if type(item[219]) == float:
            y_data_218.append(item[219])
        if type(item[220]) == float:
            y_data_219.append(item[220])
        if type(item[221]) == float:
            y_data_220.append(item[221])
        if type(item[222]) == float:
            y_data_221.append(item[222])
        if type(item[223]) == float:
            y_data_222.append(item[223])
        if type(item[224]) == float:
            y_data_223.append(item[224])
        if type(item[225]) == float:
            y_data_224.append(item[225])
        if type(item[226]) == float:
            y_data_225.append(item[226])
        if type(item[227]) == float:
            y_data_226.append(item[227])
        if type(item[228]) == float:
            y_data_227.append(item[228])
        if type(item[229]) == float:
            y_data_228.append(item[229])
        if type(item[230]) == float:
            y_data_229.append(item[230])
        if type(item[231]) == float:
            y_data_230.append(item[231])
        if type(item[232]) == float:
            y_data_231.append(item[232])
        if type(item[233]) == float:
            y_data_232.append(item[233])
        if type(item[234]) == float:
            y_data_233.append(item[234])
        if type(item[235]) == float:
            y_data_234.append(item[235])
        if type(item[236]) == float:
            y_data_235.append(item[236])
        if type(item[237]) == float:
            y_data_236.append(item[237])
        if type(item[238]) == float:
            y_data_237.append(item[238])
        if type(item[239]) == float:
            y_data_238.append(item[239])
        if type(item[240]) == float:
            y_data_239.append(item[240])
        if type(item[241]) == float:
            y_data_240.append(item[241])
        if type(item[242]) == float:
            y_data_241.append(item[242])
        if type(item[243]) == float:
            y_data_242.append(item[243])
        if type(item[244]) == float:
            y_data_243.append(item[244])
        if type(item[245]) == float:
            y_data_244.append(item[245])
        if type(item[246]) == float:
            y_data_245.append(item[246])
        if type(item[247]) == float:
            y_data_246.append(item[247])
        if type(item[248]) == float:
            y_data_247.append(item[248])
        if type(item[249]) == float:
            y_data_248.append(item[249])
        if type(item[250]) == float:
            y_data_249.append(item[250])
        if type(item[251]) == float:
            y_data_250.append(item[251])
        if type(item[252]) == float:
            y_data_251.append(item[252])
        if type(item[253]) == float:
            y_data_252.append(item[253])
        if type(item[254]) == float:
            y_data_253.append(item[254])
        if type(item[255]) == float:
            y_data_254.append(item[255])
        if type(item[256]) == float:
            y_data_255.append(item[256])
        if type(item[257]) == float:
            y_data_256.append(item[257])
        if type(item[258]) == float:
            y_data_257.append(item[258])
        if type(item[259]) == float:
            y_data_258.append(item[259])
        if type(item[260]) == float:
            y_data_259.append(item[260])
        if type(item[261]) == float:
            y_data_260.append(item[261])
        if type(item[262]) == float:
            y_data_261.append(item[262])
        if type(item[263]) == float:
            y_data_262.append(item[263])
        if type(item[264]) == float:
            y_data_263.append(item[264])
        if type(item[265]) == float:
            y_data_264.append(item[265])
        if type(item[266]) == float:
            y_data_265.append(item[266])
        if type(item[267]) == float:
            y_data_266.append(item[267])
        if type(item[268]) == float:
            y_data_267.append(item[268])
        if type(item[269]) == float:
            y_data_268.append(item[269])
        if type(item[270]) == float:
            y_data_269.append(item[270])
        if type(item[271]) == float:
            y_data_270.append(item[271])
        if type(item[272]) == float:
            y_data_271.append(item[272])
        if type(item[273]) == float:
            y_data_272.append(item[273])
        if type(item[274]) == float:
            y_data_273.append(item[274])
        if type(item[275]) == float:
            y_data_274.append(item[275])
        if type(item[276]) == float:
            y_data_275.append(item[276])
        if type(item[277]) == float:
            y_data_276.append(item[277])
        if type(item[278]) == float:
            y_data_277.append(item[278])
        if type(item[279]) == float:
            y_data_278.append(item[279])
        if type(item[280]) == float:
            y_data_279.append(item[280])
        if type(item[281]) == float:
            y_data_280.append(item[281])
        if type(item[282]) == float:
            y_data_281.append(item[282])
        if type(item[283]) == float:
            y_data_282.append(item[283])
        if type(item[284]) == float:
            y_data_283.append(item[284])
        if type(item[285]) == float:
            y_data_284.append(item[285])
        if type(item[286]) == float:
            y_data_285.append(item[286])
        if type(item[287]) == float:
            y_data_286.append(item[287])
        if type(item[288]) == float:
            y_data_287.append(item[288])
        if type(item[289]) == float:
            y_data_288.append(item[289])
        if type(item[290]) == float:
            y_data_289.append(item[290])
        if type(item[291]) == float:
            y_data_290.append(item[291])
        if type(item[292]) == float:
            y_data_291.append(item[292])
        if type(item[293]) == float:
            y_data_292.append(item[293])
        if type(item[294]) == float:
            y_data_293.append(item[294])
        if type(item[295]) == float:
            y_data_294.append(item[295])
        if type(item[296]) == float:
            y_data_295.append(item[296])
        if type(item[297]) == float:
            y_data_296.append(item[297])
        if type(item[298]) == float:
            y_data_297.append(item[298])
        if type(item[299]) == float:
            y_data_298.append(item[299])
        if type(item[300]) == float:
            y_data_299.append(item[300])
        if type(item[301]) == float:
            y_data_300.append(item[301])
        if type(item[302]) == float:
            y_data_301.append(item[302])
        if type(item[303]) == float:
            y_data_302.append(item[303])
        if type(item[304]) == float:
            y_data_303.append(item[304])
        if type(item[305]) == float:
            y_data_304.append(item[305])
        if type(item[306]) == float:
            y_data_305.append(item[306])
        if type(item[307]) == float:
            y_data_306.append(item[307])
        if type(item[308]) == float:
            y_data_307.append(item[308])
        if type(item[309]) == float:
            y_data_308.append(item[309])
        if type(item[310]) == float:
            y_data_309.append(item[310])
        if type(item[311]) == float:
            y_data_310.append(item[311])
        if type(item[312]) == float:
            y_data_311.append(item[312])
        if type(item[313]) == float:
            y_data_312.append(item[313])
        if type(item[314]) == float:
            y_data_313.append(item[314])
        if type(item[315]) == float:
            y_data_314.append(item[315])
        if type(item[316]) == float:
            y_data_315.append(item[316])
        if type(item[317]) == float:
            y_data_316.append(item[317])
        if type(item[318]) == float:
            y_data_317.append(item[318])
        if type(item[319]) == float:
            y_data_318.append(item[319])
        if type(item[320]) == float:
            y_data_319.append(item[320])
        if type(item[321]) == float:
            y_data_320.append(item[321])
        if type(item[322]) == float:
            y_data_321.append(item[322])
        if type(item[323]) == float:
            y_data_322.append(item[323])
        if type(item[324]) == float:
            y_data_323.append(item[324])
        if type(item[325]) == float:
            y_data_324.append(item[325])
        if type(item[326]) == float:
            y_data_325.append(item[326])
        if type(item[327]) == float:
            y_data_326.append(item[327])
        if type(item[328]) == float:
            y_data_327.append(item[328])
        if type(item[329]) == float:
            y_data_328.append(item[329])
        if type(item[330]) == float:
            y_data_329.append(item[330])
        if type(item[331]) == float:
            y_data_330.append(item[331])
        if type(item[332]) == float:
            y_data_331.append(item[332])
        if type(item[333]) == float:
            y_data_332.append(item[333])
        if type(item[334]) == float:
            y_data_333.append(item[334])
        if type(item[335]) == float:
            y_data_334.append(item[335])
        if type(item[336]) == float:
            y_data_335.append(item[336])
        if type(item[337]) == float:
            y_data_336.append(item[337])
        if type(item[338]) == float:
            y_data_337.append(item[338])
        if type(item[339]) == float:
            y_data_338.append(item[339])
        if type(item[340]) == float:
            y_data_339.append(item[340])
        if type(item[341]) == float:
            y_data_340.append(item[341])
        if type(item[342]) == float:
            y_data_341.append(item[342])
        if type(item[343]) == float:
            y_data_342.append(item[343])
        if type(item[344]) == float:
            y_data_343.append(item[344])
        if type(item[345]) == float:
            y_data_344.append(item[345])
        if type(item[346]) == float:
            y_data_345.append(item[346])
        if type(item[347]) == float:
            y_data_346.append(item[347])
        if type(item[348]) == float:
            y_data_347.append(item[348])
        if type(item[349]) == float:
            y_data_348.append(item[349])
        if type(item[350]) == float:
            y_data_349.append(item[350])
        if type(item[351]) == float:
            y_data_350.append(item[351])
        if type(item[352]) == float:
            y_data_351.append(item[352])
        if type(item[353]) == float:
            y_data_352.append(item[353])
        if type(item[354]) == float:
            y_data_353.append(item[354])
        if type(item[355]) == float:
            y_data_354.append(item[355])
        if type(item[356]) == float:
            y_data_355.append(item[356])
        if type(item[357]) == float:
            y_data_356.append(item[357])
        if type(item[358]) == float:
            y_data_357.append(item[358])
        if type(item[359]) == float:
            y_data_358.append(item[359])
        if type(item[360]) == float:
            y_data_359.append(item[360])
        if type(item[361]) == float:
            y_data_360.append(item[361])
        if type(item[362]) == float:
            y_data_361.append(item[362])
        if type(item[363]) == float:
            y_data_362.append(item[363])
        if type(item[364]) == float:
            y_data_363.append(item[364])
        if type(item[365]) == float:
            y_data_364.append(item[365])
        if type(item[366]) == float:
            y_data_365.append(item[366])
        if type(item[367]) == float:
            y_data_366.append(item[367])
        if type(item[368]) == float:
            y_data_367.append(item[368])
        if type(item[369]) == float:
            y_data_368.append(item[369])
        if type(item[370]) == float:
            y_data_369.append(item[370])
        if type(item[371]) == float:
            y_data_370.append(item[371])
        if type(item[372]) == float:
            y_data_371.append(item[372])
        if type(item[373]) == float:
            y_data_372.append(item[373])
        if type(item[374]) == float:
            y_data_373.append(item[374])
        if type(item[375]) == float:
            y_data_374.append(item[375])
        if type(item[376]) == float:
            y_data_375.append(item[376])
        if type(item[377]) == float:
            y_data_376.append(item[377])
        if type(item[378]) == float:
            y_data_377.append(item[378])
        if type(item[379]) == float:
            y_data_378.append(item[379])
        if type(item[380]) == float:
            y_data_379.append(item[380])
        if type(item[381]) == float:
            y_data_380.append(item[381])
        if type(item[382]) == float:
            y_data_381.append(item[382])
        if type(item[383]) == float:
            y_data_382.append(item[383])
        if type(item[384]) == float:
            y_data_383.append(item[384])
        if type(item[385]) == float:
            y_data_384.append(item[385])
        if type(item[386]) == float:
            y_data_385.append(item[386])
        if type(item[387]) == float:
            y_data_386.append(item[387])
        if type(item[388]) == float:
            y_data_387.append(item[388])
        if type(item[389]) == float:
            y_data_388.append(item[389])
        if type(item[390]) == float:
            y_data_389.append(item[390])
        if type(item[391]) == float:
            y_data_390.append(item[391])
        if type(item[392]) == float:
            y_data_391.append(item[392])
        if type(item[393]) == float:
            y_data_392.append(item[393])
        if type(item[394]) == float:
            y_data_393.append(item[394])
        if type(item[395]) == float:
            y_data_394.append(item[395])
        if type(item[396]) == float:
            y_data_395.append(item[396])
        if type(item[397]) == float:
            y_data_396.append(item[397])
        if type(item[398]) == float:
            y_data_397.append(item[398])
        if type(item[399]) == float:
            y_data_398.append(item[399])
        if type(item[400]) == float:
            y_data_399.append(item[400])
        if type(item[401]) == float:
            y_data_400.append(item[401])
        if type(item[402]) == float:
            y_data_401.append(item[402])
        if type(item[403]) == float:
            y_data_402.append(item[403])
        if type(item[404]) == float:
            y_data_403.append(item[404])
        if type(item[405]) == float:
            y_data_404.append(item[405])
        if type(item[406]) == float:
            y_data_405.append(item[406])
        if type(item[407]) == float:
            y_data_406.append(item[407])
        if type(item[408]) == float:
            y_data_407.append(item[408])
        if type(item[409]) == float:
            y_data_408.append(item[409])
        if type(item[410]) == float:
            y_data_409.append(item[410])
        if type(item[411]) == float:
            y_data_410.append(item[411])
        if type(item[412]) == float:
            y_data_411.append(item[412])
        if type(item[413]) == float:
            y_data_412.append(item[413])
        if type(item[414]) == float:
            y_data_413.append(item[414])
        if type(item[415]) == float:
            y_data_414.append(item[415])
        if type(item[416]) == float:
            y_data_415.append(item[416])
        if type(item[417]) == float:
            y_data_416.append(item[417])
        if type(item[418]) == float:
            y_data_417.append(item[418])
        if type(item[419]) == float:
            y_data_418.append(item[419])
        if type(item[420]) == float:
            y_data_419.append(item[420])
        if type(item[421]) == float:
            y_data_420.append(item[421])
        if type(item[422]) == float:
            y_data_421.append(item[422])
        if type(item[423]) == float:
            y_data_422.append(item[423])
        if type(item[424]) == float:
            y_data_423.append(item[424])
        if type(item[425]) == float:
            y_data_424.append(item[425])
        if type(item[426]) == float:
            y_data_425.append(item[426])
        if type(item[427]) == float:
            y_data_426.append(item[427])
        if type(item[428]) == float:
            y_data_427.append(item[428])
        if type(item[429]) == float:
            y_data_428.append(item[429])
        if type(item[430]) == float:
            y_data_429.append(item[430])
        if type(item[431]) == float:
            y_data_430.append(item[431])
        if type(item[432]) == float:
            y_data_431.append(item[432])
        if type(item[433]) == float:
            y_data_432.append(item[433])
        if type(item[434]) == float:
            y_data_433.append(item[434])
        if type(item[435]) == float:
            y_data_434.append(item[435])
        if type(item[436]) == float:
            y_data_435.append(item[436])
        if type(item[437]) == float:
            y_data_436.append(item[437])
        if type(item[438]) == float:
            y_data_437.append(item[438])
        if type(item[439]) == float:
            y_data_438.append(item[439])
        if type(item[440]) == float:
            y_data_439.append(item[440])
        if type(item[441]) == float:
            y_data_440.append(item[441])
        if type(item[442]) == float:
            y_data_441.append(item[442])
        if type(item[443]) == float:
            y_data_442.append(item[443])
        if type(item[444]) == float:
            y_data_443.append(item[444])
        if type(item[445]) == float:
            y_data_444.append(item[445])
        if type(item[446]) == float:
            y_data_445.append(item[446])
        if type(item[447]) == float:
            y_data_446.append(item[447])
        if type(item[448]) == float:
            y_data_447.append(item[448])
        if type(item[449]) == float:
            y_data_448.append(item[449])
        if type(item[450]) == float:
            y_data_449.append(item[450])
        if type(item[451]) == float:
            y_data_450.append(item[451])
        if type(item[452]) == float:
            y_data_451.append(item[452])
        if type(item[453]) == float:
            y_data_452.append(item[453])
        if type(item[454]) == float:
            y_data_453.append(item[454])
        if type(item[455]) == float:
            y_data_454.append(item[455])
        if type(item[456]) == float:
            y_data_455.append(item[456])
        if type(item[457]) == float:
            y_data_456.append(item[457])
        if type(item[458]) == float:
            y_data_457.append(item[458])
        if type(item[459]) == float:
            y_data_458.append(item[459])
        if type(item[460]) == float:
            y_data_459.append(item[460])
        if type(item[461]) == float:
            y_data_460.append(item[461])
        if type(item[462]) == float:
            y_data_461.append(item[462])
        if type(item[463]) == float:
            y_data_462.append(item[463])
        if type(item[464]) == float:
            y_data_463.append(item[464])
        if type(item[465]) == float:
            y_data_464.append(item[465])
        if type(item[466]) == float:
            y_data_465.append(item[466])
        if type(item[467]) == float:
            y_data_466.append(item[467])

        if item[len(item)-1] != "LastTime":
            date_.append(item[len(item)-1])
    # 日期搞定
    x_data = handle_date(date_)

    f_y_data_1 = get_v(y_data_1)
    f_y_data_2 = get_v(y_data_2)
    f_y_data_3 = get_v(y_data_3)
    f_y_data_4 = get_v(y_data_4)
    f_y_data_5 = get_v(y_data_5)
    f_y_data_6 = get_v(y_data_6)
    f_y_data_7 = get_v(y_data_7)
    f_y_data_8 = get_v(y_data_8)
    f_y_data_9 = get_v(y_data_9)
    f_y_data_10 = get_v(y_data_10)
    f_y_data_11 = get_v(y_data_11)
    f_y_data_12 = get_v(y_data_12)
    f_y_data_13 = get_v(y_data_13)
    f_y_data_14 = get_v(y_data_14)
    f_y_data_15 = get_v(y_data_15)
    f_y_data_16 = get_v(y_data_16)
    f_y_data_17 = get_v(y_data_17)
    f_y_data_18 = get_v(y_data_18)
    f_y_data_19 = get_v(y_data_19)
    f_y_data_20 = get_v(y_data_20)
    f_y_data_21 = get_v(y_data_21)
    f_y_data_22 = get_v(y_data_22)
    f_y_data_23 = get_v(y_data_23)
    f_y_data_24 = get_v(y_data_24)
    f_y_data_25 = get_v(y_data_25)
    f_y_data_26 = get_v(y_data_26)
    f_y_data_27 = get_v(y_data_27)
    f_y_data_28 = get_v(y_data_28)
    f_y_data_29 = get_v(y_data_29)
    f_y_data_30 = get_v(y_data_30)
    f_y_data_31 = get_v(y_data_31)
    f_y_data_32 = get_v(y_data_32)
    f_y_data_33 = get_v(y_data_33)
    f_y_data_34 = get_v(y_data_34)
    f_y_data_35 = get_v(y_data_35)
    f_y_data_36 = get_v(y_data_36)
    f_y_data_37 = get_v(y_data_37)
    f_y_data_38 = get_v(y_data_38)
    f_y_data_39 = get_v(y_data_39)
    f_y_data_40 = get_v(y_data_40)
    f_y_data_41 = get_v(y_data_41)
    f_y_data_42 = get_v(y_data_42)
    f_y_data_43 = get_v(y_data_43)
    f_y_data_44 = get_v(y_data_44)
    f_y_data_45 = get_v(y_data_45)
    f_y_data_46 = get_v(y_data_46)
    f_y_data_47 = get_v(y_data_47)
    f_y_data_48 = get_v(y_data_48)
    f_y_data_49 = get_v(y_data_49)
    f_y_data_50 = get_v(y_data_50)
    f_y_data_51 = get_v(y_data_51)
    f_y_data_52 = get_v(y_data_52)
    f_y_data_53 = get_v(y_data_53)
    f_y_data_54 = get_v(y_data_54)
    f_y_data_55 = get_v(y_data_55)
    f_y_data_56 = get_v(y_data_56)
    f_y_data_57 = get_v(y_data_57)
    f_y_data_58 = get_v(y_data_58)
    f_y_data_59 = get_v(y_data_59)
    f_y_data_60 = get_v(y_data_60)
    f_y_data_61 = get_v(y_data_61)
    f_y_data_62 = get_v(y_data_62)
    f_y_data_63 = get_v(y_data_63)
    f_y_data_64 = get_v(y_data_64)
    f_y_data_65 = get_v(y_data_65)
    f_y_data_66 = get_v(y_data_66)
    f_y_data_67 = get_v(y_data_67)
    f_y_data_68 = get_v(y_data_68)
    f_y_data_69 = get_v(y_data_69)
    f_y_data_70 = get_v(y_data_70)
    f_y_data_71 = get_v(y_data_71)
    f_y_data_72 = get_v(y_data_72)
    f_y_data_73 = get_v(y_data_73)
    f_y_data_74 = get_v(y_data_74)
    f_y_data_75 = get_v(y_data_75)
    f_y_data_76 = get_v(y_data_76)
    f_y_data_77 = get_v(y_data_77)
    f_y_data_78 = get_v(y_data_78)
    f_y_data_79 = get_v(y_data_79)
    f_y_data_80 = get_v(y_data_80)
    f_y_data_81 = get_v(y_data_81)
    f_y_data_82 = get_v(y_data_82)
    f_y_data_83 = get_v(y_data_83)
    f_y_data_84 = get_v(y_data_84)
    f_y_data_85 = get_v(y_data_85)
    f_y_data_86 = get_v(y_data_86)
    f_y_data_87 = get_v(y_data_87)
    f_y_data_88 = get_v(y_data_88)
    f_y_data_89 = get_v(y_data_89)
    f_y_data_90 = get_v(y_data_90)
    f_y_data_91 = get_v(y_data_91)
    f_y_data_92 = get_v(y_data_92)
    f_y_data_93 = get_v(y_data_93)
    f_y_data_94 = get_v(y_data_94)
    f_y_data_95 = get_v(y_data_95)
    f_y_data_96 = get_v(y_data_96)
    f_y_data_97 = get_v(y_data_97)
    f_y_data_98 = get_v(y_data_98)
    f_y_data_99 = get_v(y_data_99)
    f_y_data_100 = get_v(y_data_100)
    f_y_data_101 = get_v(y_data_101)
    f_y_data_102 = get_v(y_data_102)
    f_y_data_103 = get_v(y_data_103)
    f_y_data_104 = get_v(y_data_104)
    f_y_data_105 = get_v(y_data_105)
    f_y_data_106 = get_v(y_data_106)
    f_y_data_107 = get_v(y_data_107)
    f_y_data_108 = get_v(y_data_108)
    f_y_data_109 = get_v(y_data_109)
    f_y_data_110 = get_v(y_data_110)
    f_y_data_111 = get_v(y_data_111)
    f_y_data_112 = get_v(y_data_112)
    f_y_data_113 = get_v(y_data_113)
    f_y_data_114 = get_v(y_data_114)
    f_y_data_115 = get_v(y_data_115)
    f_y_data_116 = get_v(y_data_116)
    f_y_data_117 = get_v(y_data_117)
    f_y_data_118 = get_v(y_data_118)
    f_y_data_119 = get_v(y_data_119)
    f_y_data_120 = get_v(y_data_120)
    f_y_data_121 = get_v(y_data_121)
    f_y_data_122 = get_v(y_data_122)
    f_y_data_123 = get_v(y_data_123)
    f_y_data_124 = get_v(y_data_124)
    f_y_data_125 = get_v(y_data_125)
    f_y_data_126 = get_v(y_data_126)
    f_y_data_127 = get_v(y_data_127)
    f_y_data_128 = get_v(y_data_128)
    f_y_data_129 = get_v(y_data_129)
    f_y_data_130 = get_v(y_data_130)
    f_y_data_131 = get_v(y_data_131)
    f_y_data_132 = get_v(y_data_132)
    f_y_data_133 = get_v(y_data_133)
    f_y_data_134 = get_v(y_data_134)
    f_y_data_135 = get_v(y_data_135)
    f_y_data_136 = get_v(y_data_136)
    f_y_data_137 = get_v(y_data_137)
    f_y_data_138 = get_v(y_data_138)
    f_y_data_139 = get_v(y_data_139)
    f_y_data_140 = get_v(y_data_140)
    f_y_data_141 = get_v(y_data_141)
    f_y_data_142 = get_v(y_data_142)
    f_y_data_143 = get_v(y_data_143)
    f_y_data_144 = get_v(y_data_144)
    f_y_data_145 = get_v(y_data_145)
    f_y_data_146 = get_v(y_data_146)
    f_y_data_147 = get_v(y_data_147)
    f_y_data_148 = get_v(y_data_148)
    f_y_data_149 = get_v(y_data_149)
    f_y_data_150 = get_v(y_data_150)
    f_y_data_151 = get_v(y_data_151)
    f_y_data_152 = get_v(y_data_152)
    f_y_data_153 = get_v(y_data_153)
    f_y_data_154 = get_v(y_data_154)
    f_y_data_155 = get_v(y_data_155)
    f_y_data_156 = get_v(y_data_156)
    f_y_data_157 = get_v(y_data_157)
    f_y_data_158 = get_v(y_data_158)
    f_y_data_159 = get_v(y_data_159)
    f_y_data_160 = get_v(y_data_160)
    f_y_data_161 = get_v(y_data_161)
    f_y_data_162 = get_v(y_data_162)
    f_y_data_163 = get_v(y_data_163)
    f_y_data_164 = get_v(y_data_164)
    f_y_data_165 = get_v(y_data_165)
    f_y_data_166 = get_v(y_data_166)
    f_y_data_167 = get_v(y_data_167)
    f_y_data_168 = get_v(y_data_168)
    f_y_data_169 = get_v(y_data_169)
    f_y_data_170 = get_v(y_data_170)
    f_y_data_171 = get_v(y_data_171)
    f_y_data_172 = get_v(y_data_172)
    f_y_data_173 = get_v(y_data_173)
    f_y_data_174 = get_v(y_data_174)
    f_y_data_175 = get_v(y_data_175)
    f_y_data_176 = get_v(y_data_176)
    f_y_data_177 = get_v(y_data_177)
    f_y_data_178 = get_v(y_data_178)
    f_y_data_179 = get_v(y_data_179)
    f_y_data_180 = get_v(y_data_180)
    f_y_data_181 = get_v(y_data_181)
    f_y_data_182 = get_v(y_data_182)
    f_y_data_183 = get_v(y_data_183)
    f_y_data_184 = get_v(y_data_184)
    f_y_data_185 = get_v(y_data_185)
    f_y_data_186 = get_v(y_data_186)
    f_y_data_187 = get_v(y_data_187)
    f_y_data_188 = get_v(y_data_188)
    f_y_data_189 = get_v(y_data_189)
    f_y_data_190 = get_v(y_data_190)
    f_y_data_191 = get_v(y_data_191)
    f_y_data_192 = get_v(y_data_192)
    f_y_data_193 = get_v(y_data_193)
    f_y_data_194 = get_v(y_data_194)
    f_y_data_195 = get_v(y_data_195)
    f_y_data_196 = get_v(y_data_196)
    f_y_data_197 = get_v(y_data_197)
    f_y_data_198 = get_v(y_data_198)
    f_y_data_199 = get_v(y_data_199)
    f_y_data_200 = get_v(y_data_200)
    f_y_data_201 = get_v(y_data_201)
    f_y_data_202 = get_v(y_data_202)
    f_y_data_203 = get_v(y_data_203)
    f_y_data_204 = get_v(y_data_204)
    f_y_data_205 = get_v(y_data_205)
    f_y_data_206 = get_v(y_data_206)
    f_y_data_207 = get_v(y_data_207)
    f_y_data_208 = get_v(y_data_208)
    f_y_data_209 = get_v(y_data_209)
    f_y_data_210 = get_v(y_data_210)
    f_y_data_211 = get_v(y_data_211)
    f_y_data_212 = get_v(y_data_212)
    f_y_data_213 = get_v(y_data_213)
    f_y_data_214 = get_v(y_data_214)
    f_y_data_215 = get_v(y_data_215)
    f_y_data_216 = get_v(y_data_216)
    f_y_data_217 = get_v(y_data_217)
    f_y_data_218 = get_v(y_data_218)
    f_y_data_219 = get_v(y_data_219)
    f_y_data_220 = get_v(y_data_220)
    f_y_data_221 = get_v(y_data_221)
    f_y_data_222 = get_v(y_data_222)
    f_y_data_223 = get_v(y_data_223)
    f_y_data_224 = get_v(y_data_224)
    f_y_data_225 = get_v(y_data_225)
    f_y_data_226 = get_v(y_data_226)
    f_y_data_227 = get_v(y_data_227)
    f_y_data_228 = get_v(y_data_228)
    f_y_data_229 = get_v(y_data_229)
    f_y_data_230 = get_v(y_data_230)
    f_y_data_231 = get_v(y_data_231)
    f_y_data_232 = get_v(y_data_232)
    f_y_data_233 = get_v(y_data_233)
    f_y_data_234 = get_v(y_data_234)
    f_y_data_235 = get_v(y_data_235)
    f_y_data_236 = get_v(y_data_236)
    f_y_data_237 = get_v(y_data_237)
    f_y_data_238 = get_v(y_data_238)
    f_y_data_239 = get_v(y_data_239)
    f_y_data_240 = get_v(y_data_240)
    f_y_data_241 = get_v(y_data_241)
    f_y_data_242 = get_v(y_data_242)
    f_y_data_243 = get_v(y_data_243)
    f_y_data_244 = get_v(y_data_244)
    f_y_data_245 = get_v(y_data_245)
    f_y_data_246 = get_v(y_data_246)
    f_y_data_247 = get_v(y_data_247)
    f_y_data_248 = get_v(y_data_248)
    f_y_data_249 = get_v(y_data_249)
    f_y_data_250 = get_v(y_data_250)
    f_y_data_251 = get_v(y_data_251)
    f_y_data_252 = get_v(y_data_252)
    f_y_data_253 = get_v(y_data_253)
    f_y_data_254 = get_v(y_data_254)
    f_y_data_255 = get_v(y_data_255)
    f_y_data_256 = get_v(y_data_256)
    f_y_data_257 = get_v(y_data_257)
    f_y_data_258 = get_v(y_data_258)
    f_y_data_259 = get_v(y_data_259)
    f_y_data_260 = get_v(y_data_260)
    f_y_data_261 = get_v(y_data_261)
    f_y_data_262 = get_v(y_data_262)
    f_y_data_263 = get_v(y_data_263)
    f_y_data_264 = get_v(y_data_264)
    f_y_data_265 = get_v(y_data_265)
    f_y_data_266 = get_v(y_data_266)
    f_y_data_267 = get_v(y_data_267)
    f_y_data_268 = get_v(y_data_268)
    f_y_data_269 = get_v(y_data_269)
    f_y_data_270 = get_v(y_data_270)
    f_y_data_271 = get_v(y_data_271)
    f_y_data_272 = get_v(y_data_272)
    f_y_data_273 = get_v(y_data_273)
    f_y_data_274 = get_v(y_data_274)
    f_y_data_275 = get_v(y_data_275)
    f_y_data_276 = get_v(y_data_276)
    f_y_data_277 = get_v(y_data_277)
    f_y_data_278 = get_v(y_data_278)
    f_y_data_279 = get_v(y_data_279)
    f_y_data_280 = get_v(y_data_280)
    f_y_data_281 = get_v(y_data_281)
    f_y_data_282 = get_v(y_data_282)
    f_y_data_283 = get_v(y_data_283)
    f_y_data_284 = get_v(y_data_284)
    f_y_data_285 = get_v(y_data_285)
    f_y_data_286 = get_v(y_data_286)
    f_y_data_287 = get_v(y_data_287)
    f_y_data_288 = get_v(y_data_288)
    f_y_data_289 = get_v(y_data_289)
    f_y_data_290 = get_v(y_data_290)
    f_y_data_291 = get_v(y_data_291)
    f_y_data_292 = get_v(y_data_292)
    f_y_data_293 = get_v(y_data_293)
    f_y_data_294 = get_v(y_data_294)
    f_y_data_295 = get_v(y_data_295)
    f_y_data_296 = get_v(y_data_296)
    f_y_data_297 = get_v(y_data_297)
    f_y_data_298 = get_v(y_data_298)
    f_y_data_299 = get_v(y_data_299)
    f_y_data_300 = get_v(y_data_300)
    f_y_data_301 = get_v(y_data_301)
    f_y_data_302 = get_v(y_data_302)
    f_y_data_303 = get_v(y_data_303)
    f_y_data_304 = get_v(y_data_304)
    f_y_data_305 = get_v(y_data_305)
    f_y_data_306 = get_v(y_data_306)
    f_y_data_307 = get_v(y_data_307)
    f_y_data_308 = get_v(y_data_308)
    f_y_data_309 = get_v(y_data_309)
    f_y_data_310 = get_v(y_data_310)
    f_y_data_311 = get_v(y_data_311)
    f_y_data_312 = get_v(y_data_312)
    f_y_data_313 = get_v(y_data_313)
    f_y_data_314 = get_v(y_data_314)
    f_y_data_315 = get_v(y_data_315)
    f_y_data_316 = get_v(y_data_316)
    f_y_data_317 = get_v(y_data_317)
    f_y_data_318 = get_v(y_data_318)
    f_y_data_319 = get_v(y_data_319)
    f_y_data_320 = get_v(y_data_320)
    f_y_data_321 = get_v(y_data_321)
    f_y_data_322 = get_v(y_data_322)
    f_y_data_323 = get_v(y_data_323)
    f_y_data_324 = get_v(y_data_324)
    f_y_data_325 = get_v(y_data_325)
    f_y_data_326 = get_v(y_data_326)
    f_y_data_327 = get_v(y_data_327)
    f_y_data_328 = get_v(y_data_328)
    f_y_data_329 = get_v(y_data_329)
    f_y_data_330 = get_v(y_data_330)
    f_y_data_331 = get_v(y_data_331)
    f_y_data_332 = get_v(y_data_332)
    f_y_data_333 = get_v(y_data_333)
    f_y_data_334 = get_v(y_data_334)
    f_y_data_335 = get_v(y_data_335)
    f_y_data_336 = get_v(y_data_336)
    f_y_data_337 = get_v(y_data_337)
    f_y_data_338 = get_v(y_data_338)
    f_y_data_339 = get_v(y_data_339)
    f_y_data_340 = get_v(y_data_340)
    f_y_data_341 = get_v(y_data_341)
    f_y_data_342 = get_v(y_data_342)
    f_y_data_343 = get_v(y_data_343)
    f_y_data_344 = get_v(y_data_344)
    f_y_data_345 = get_v(y_data_345)
    f_y_data_346 = get_v(y_data_346)
    f_y_data_347 = get_v(y_data_347)
    f_y_data_348 = get_v(y_data_348)
    f_y_data_349 = get_v(y_data_349)
    f_y_data_350 = get_v(y_data_350)
    f_y_data_351 = get_v(y_data_351)
    f_y_data_352 = get_v(y_data_352)
    f_y_data_353 = get_v(y_data_353)
    f_y_data_354 = get_v(y_data_354)
    f_y_data_355 = get_v(y_data_355)
    f_y_data_356 = get_v(y_data_356)
    f_y_data_357 = get_v(y_data_357)
    f_y_data_358 = get_v(y_data_358)
    f_y_data_359 = get_v(y_data_359)
    f_y_data_360 = get_v(y_data_360)
    f_y_data_361 = get_v(y_data_361)
    f_y_data_362 = get_v(y_data_362)
    f_y_data_363 = get_v(y_data_363)
    f_y_data_364 = get_v(y_data_364)
    f_y_data_365 = get_v(y_data_365)
    f_y_data_366 = get_v(y_data_366)
    f_y_data_367 = get_v(y_data_367)
    f_y_data_368 = get_v(y_data_368)
    f_y_data_369 = get_v(y_data_369)
    f_y_data_370 = get_v(y_data_370)
    f_y_data_371 = get_v(y_data_371)
    f_y_data_372 = get_v(y_data_372)
    f_y_data_373 = get_v(y_data_373)
    f_y_data_374 = get_v(y_data_374)
    f_y_data_375 = get_v(y_data_375)
    f_y_data_376 = get_v(y_data_376)
    f_y_data_377 = get_v(y_data_377)
    f_y_data_378 = get_v(y_data_378)
    f_y_data_379 = get_v(y_data_379)
    f_y_data_380 = get_v(y_data_380)
    f_y_data_381 = get_v(y_data_381)
    f_y_data_382 = get_v(y_data_382)
    f_y_data_383 = get_v(y_data_383)
    f_y_data_384 = get_v(y_data_384)
    f_y_data_385 = get_v(y_data_385)
    f_y_data_386 = get_v(y_data_386)
    f_y_data_387 = get_v(y_data_387)
    f_y_data_388 = get_v(y_data_388)
    f_y_data_389 = get_v(y_data_389)
    f_y_data_390 = get_v(y_data_390)
    f_y_data_391 = get_v(y_data_391)
    f_y_data_392 = get_v(y_data_392)
    f_y_data_393 = get_v(y_data_393)
    f_y_data_394 = get_v(y_data_394)
    f_y_data_395 = get_v(y_data_395)
    f_y_data_396 = get_v(y_data_396)
    f_y_data_397 = get_v(y_data_397)
    f_y_data_398 = get_v(y_data_398)
    f_y_data_399 = get_v(y_data_399)
    f_y_data_400 = get_v(y_data_400)
    f_y_data_401 = get_v(y_data_401)
    f_y_data_402 = get_v(y_data_402)
    f_y_data_403 = get_v(y_data_403)
    f_y_data_404 = get_v(y_data_404)
    f_y_data_405 = get_v(y_data_405)
    f_y_data_406 = get_v(y_data_406)
    f_y_data_407 = get_v(y_data_407)
    f_y_data_408 = get_v(y_data_408)
    f_y_data_409 = get_v(y_data_409)
    f_y_data_410 = get_v(y_data_410)
    f_y_data_411 = get_v(y_data_411)
    f_y_data_412 = get_v(y_data_412)
    f_y_data_413 = get_v(y_data_413)
    f_y_data_414 = get_v(y_data_414)
    f_y_data_415 = get_v(y_data_415)
    f_y_data_416 = get_v(y_data_416)
    f_y_data_417 = get_v(y_data_417)
    f_y_data_418 = get_v(y_data_418)
    f_y_data_419 = get_v(y_data_419)
    f_y_data_420 = get_v(y_data_420)
    f_y_data_421 = get_v(y_data_421)
    f_y_data_422 = get_v(y_data_422)
    f_y_data_423 = get_v(y_data_423)
    f_y_data_424 = get_v(y_data_424)
    f_y_data_425 = get_v(y_data_425)
    f_y_data_426 = get_v(y_data_426)
    f_y_data_427 = get_v(y_data_427)
    f_y_data_428 = get_v(y_data_428)
    f_y_data_429 = get_v(y_data_429)
    f_y_data_430 = get_v(y_data_430)
    f_y_data_431 = get_v(y_data_431)
    f_y_data_432 = get_v(y_data_432)
    f_y_data_433 = get_v(y_data_433)
    f_y_data_434 = get_v(y_data_434)
    f_y_data_435 = get_v(y_data_435)
    f_y_data_436 = get_v(y_data_436)
    f_y_data_437 = get_v(y_data_437)
    f_y_data_438 = get_v(y_data_438)
    f_y_data_439 = get_v(y_data_439)
    f_y_data_440 = get_v(y_data_440)
    f_y_data_441 = get_v(y_data_441)
    f_y_data_442 = get_v(y_data_442)
    f_y_data_443 = get_v(y_data_443)
    f_y_data_444 = get_v(y_data_444)
    f_y_data_445 = get_v(y_data_445)
    f_y_data_446 = get_v(y_data_446)
    f_y_data_447 = get_v(y_data_447)
    f_y_data_448 = get_v(y_data_448)
    f_y_data_449 = get_v(y_data_449)
    f_y_data_450 = get_v(y_data_450)
    f_y_data_451 = get_v(y_data_451)
    f_y_data_452 = get_v(y_data_452)
    f_y_data_453 = get_v(y_data_453)
    f_y_data_454 = get_v(y_data_454)
    f_y_data_455 = get_v(y_data_455)
    f_y_data_456 = get_v(y_data_456)
    f_y_data_457 = get_v(y_data_457)
    f_y_data_458 = get_v(y_data_458)
    f_y_data_459 = get_v(y_data_459)
    f_y_data_460 = get_v(y_data_460)
    f_y_data_461 = get_v(y_data_461)
    f_y_data_462 = get_v(y_data_462)
    f_y_data_463 = get_v(y_data_463)
    f_y_data_464 = get_v(y_data_464)
    f_y_data_465 = get_v(y_data_465)
    f_y_data_466 = get_v(y_data_466)
    f_y_data_467 = get_v(y_data_467)

    print(x_data)


    c = (
        Line()
            .add_xaxis(xaxis_data=x_data)

            .add_yaxis(
            "ZZG_index",
            y_axis=f_y_data_1,
            linestyle_opts=opts.LineStyleOpts(width=4, color="blue"),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "A",
            y_axis=f_y_data_2,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AAL",
            y_axis=f_y_data_3,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AAPL",
            y_axis=f_y_data_4,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ABBV",
            y_axis=f_y_data_5,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ABC",
            y_axis=f_y_data_6,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ABMD",
            y_axis=f_y_data_7,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ABT",
            y_axis=f_y_data_8,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ACN",
            y_axis=f_y_data_9,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ADBE",
            y_axis=f_y_data_10,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ADI",
            y_axis=f_y_data_11,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ADM",
            y_axis=f_y_data_12,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ADP",
            y_axis=f_y_data_13,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ADS",
            y_axis=f_y_data_14,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ADSK",
            y_axis=f_y_data_15,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AEE",
            y_axis=f_y_data_16,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AEP",
            y_axis=f_y_data_17,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AES",
            y_axis=f_y_data_18,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AFL",
            y_axis=f_y_data_19,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AGN",
            y_axis=f_y_data_20,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AIG",
            y_axis=f_y_data_21,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AIV",
            y_axis=f_y_data_22,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AIZ",
            y_axis=f_y_data_23,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AJG",
            y_axis=f_y_data_24,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AKAM",
            y_axis=f_y_data_25,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ALB",
            y_axis=f_y_data_26,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ALGN",
            y_axis=f_y_data_27,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ALK",
            y_axis=f_y_data_28,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ALL_",
            y_axis=f_y_data_29,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ALLE",
            y_axis=f_y_data_30,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ALXN",
            y_axis=f_y_data_31,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AMAT",
            y_axis=f_y_data_32,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AMD",
            y_axis=f_y_data_33,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AME",
            y_axis=f_y_data_34,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AMGN",
            y_axis=f_y_data_35,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AMP",
            y_axis=f_y_data_36,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AMT",
            y_axis=f_y_data_37,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AMZN",
            y_axis=f_y_data_38,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ANSS",
            y_axis=f_y_data_39,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AON",
            y_axis=f_y_data_40,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AOS",
            y_axis=f_y_data_41,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "APA",
            y_axis=f_y_data_42,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "APD",
            y_axis=f_y_data_43,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "APH",
            y_axis=f_y_data_44,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "APTV",
            y_axis=f_y_data_45,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ARE",
            y_axis=f_y_data_46,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ASML",
            y_axis=f_y_data_47,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ATO",
            y_axis=f_y_data_48,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ATVI",
            y_axis=f_y_data_49,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AVB",
            y_axis=f_y_data_50,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AVGO",
            y_axis=f_y_data_51,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AVY",
            y_axis=f_y_data_52,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AWK",
            y_axis=f_y_data_53,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AXP",
            y_axis=f_y_data_54,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "AZO",
            y_axis=f_y_data_55,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BA",
            y_axis=f_y_data_56,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BAC",
            y_axis=f_y_data_57,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BAX",
            y_axis=f_y_data_58,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BBY",
            y_axis=f_y_data_59,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BDX",
            y_axis=f_y_data_60,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BEN",
            y_axis=f_y_data_61,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BF_B",
            y_axis=f_y_data_62,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BIDU",
            y_axis=f_y_data_63,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BIIB",
            y_axis=f_y_data_64,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BK",
            y_axis=f_y_data_65,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BLK",
            y_axis=f_y_data_66,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BLL",
            y_axis=f_y_data_67,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BMRN",
            y_axis=f_y_data_68,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BMY",
            y_axis=f_y_data_69,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BR",
            y_axis=f_y_data_70,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BRK_B",
            y_axis=f_y_data_71,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BSX",
            y_axis=f_y_data_72,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BWA",
            y_axis=f_y_data_73,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "BXP",
            y_axis=f_y_data_74,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "C",
            y_axis=f_y_data_75,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CAG",
            y_axis=f_y_data_76,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CAH",
            y_axis=f_y_data_77,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CAT",
            y_axis=f_y_data_78,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CB",
            y_axis=f_y_data_79,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CBOE",
            y_axis=f_y_data_80,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CCI",
            y_axis=f_y_data_81,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CCL",
            y_axis=f_y_data_82,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CDNS",
            y_axis=f_y_data_83,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CDW",
            y_axis=f_y_data_84,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CE",
            y_axis=f_y_data_85,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CERN",
            y_axis=f_y_data_86,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CF",
            y_axis=f_y_data_87,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CHD",
            y_axis=f_y_data_88,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CHKP",
            y_axis=f_y_data_89,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CHRW",
            y_axis=f_y_data_90,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CHTR",
            y_axis=f_y_data_91,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CI",
            y_axis=f_y_data_92,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CINF",
            y_axis=f_y_data_93,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CL",
            y_axis=f_y_data_94,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CLX",
            y_axis=f_y_data_95,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CMA",
            y_axis=f_y_data_96,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CMCSA",
            y_axis=f_y_data_97,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CME",
            y_axis=f_y_data_98,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CMG",
            y_axis=f_y_data_99,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CMI",
            y_axis=f_y_data_100,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CMS",
            y_axis=f_y_data_101,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CNC",
            y_axis=f_y_data_102,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CNP",
            y_axis=f_y_data_103,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "COF",
            y_axis=f_y_data_104,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "COG",
            y_axis=f_y_data_105,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "COO",
            y_axis=f_y_data_106,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "COP",
            y_axis=f_y_data_107,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "COST",
            y_axis=f_y_data_108,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "COTY",
            y_axis=f_y_data_109,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CPB",
            y_axis=f_y_data_110,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CPRI",
            y_axis=f_y_data_111,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CPRT",
            y_axis=f_y_data_112,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CRM",
            y_axis=f_y_data_113,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CSCO",
            y_axis=f_y_data_114,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CSGP",
            y_axis=f_y_data_115,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CSX",
            y_axis=f_y_data_116,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CTAS",
            y_axis=f_y_data_117,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CTL",
            y_axis=f_y_data_118,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CTSH",
            y_axis=f_y_data_119,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CTXS",
            y_axis=f_y_data_120,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CVS",
            y_axis=f_y_data_121,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CVX",
            y_axis=f_y_data_122,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "CXO",
            y_axis=f_y_data_123,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "D",
            y_axis=f_y_data_124,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DAL",
            y_axis=f_y_data_125,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DE",
            y_axis=f_y_data_126,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DFS",
            y_axis=f_y_data_127,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DG",
            y_axis=f_y_data_128,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DGX",
            y_axis=f_y_data_129,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DHI",
            y_axis=f_y_data_130,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DHR",
            y_axis=f_y_data_131,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DIS",
            y_axis=f_y_data_132,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DISCA",
            y_axis=f_y_data_133,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DISCK",
            y_axis=f_y_data_134,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DISH",
            y_axis=f_y_data_135,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DLR",
            y_axis=f_y_data_136,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DLTR",
            y_axis=f_y_data_137,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DOV",
            y_axis=f_y_data_138,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DRE",
            y_axis=f_y_data_139,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DRI",
            y_axis=f_y_data_140,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DTE",
            y_axis=f_y_data_141,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DUK",
            y_axis=f_y_data_142,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DVA",
            y_axis=f_y_data_143,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DVN",
            y_axis=f_y_data_144,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "DXC",
            y_axis=f_y_data_145,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EA",
            y_axis=f_y_data_146,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EBAY",
            y_axis=f_y_data_147,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ECL",
            y_axis=f_y_data_148,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ED",
            y_axis=f_y_data_149,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EFX",
            y_axis=f_y_data_150,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EIX",
            y_axis=f_y_data_151,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EL",
            y_axis=f_y_data_152,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EMN",
            y_axis=f_y_data_153,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EMR",
            y_axis=f_y_data_154,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EOG",
            y_axis=f_y_data_155,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EQIX",
            y_axis=f_y_data_156,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EQR",
            y_axis=f_y_data_157,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ESS",
            y_axis=f_y_data_158,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ETFC",
            y_axis=f_y_data_159,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ETN",
            y_axis=f_y_data_160,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ETR",
            y_axis=f_y_data_161,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EW",
            y_axis=f_y_data_162,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EXC",
            y_axis=f_y_data_163,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "EXPD",
            y_axis=f_y_data_164,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "F",
            y_axis=f_y_data_165,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FAST",
            y_axis=f_y_data_166,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FB",
            y_axis=f_y_data_167,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FCX",
            y_axis=f_y_data_168,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FDX",
            y_axis=f_y_data_169,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FE",
            y_axis=f_y_data_170,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FFIV",
            y_axis=f_y_data_171,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FIS",
            y_axis=f_y_data_172,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FISV",
            y_axis=f_y_data_173,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FITB",
            y_axis=f_y_data_174,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FLIR",
            y_axis=f_y_data_175,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FLS",
            y_axis=f_y_data_176,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FLT",
            y_axis=f_y_data_177,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FMC",
            y_axis=f_y_data_178,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FOX",
            y_axis=f_y_data_179,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FOXA",
            y_axis=f_y_data_180,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FRC",
            y_axis=f_y_data_181,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FRT",
            y_axis=f_y_data_182,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FTI",
            y_axis=f_y_data_183,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FTNT",
            y_axis=f_y_data_184,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "FTV",
            y_axis=f_y_data_185,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GD",
            y_axis=f_y_data_186,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GE",
            y_axis=f_y_data_187,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GILD",
            y_axis=f_y_data_188,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GIS",
            y_axis=f_y_data_189,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GLW",
            y_axis=f_y_data_190,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GM",
            y_axis=f_y_data_191,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GOOG",
            y_axis=f_y_data_192,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GOOGL",
            y_axis=f_y_data_193,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GPC",
            y_axis=f_y_data_194,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GPN",
            y_axis=f_y_data_195,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GPS",
            y_axis=f_y_data_196,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GRMN",
            y_axis=f_y_data_197,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GS",
            y_axis=f_y_data_198,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "GWW",
            y_axis=f_y_data_199,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HAL",
            y_axis=f_y_data_200,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HAS",
            y_axis=f_y_data_201,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HBAN",
            y_axis=f_y_data_202,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HBI",
            y_axis=f_y_data_203,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HCA",
            y_axis=f_y_data_204,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HD",
            y_axis=f_y_data_205,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HES",
            y_axis=f_y_data_206,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HFC",
            y_axis=f_y_data_207,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HIG",
            y_axis=f_y_data_208,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HLT",
            y_axis=f_y_data_209,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HOG",
            y_axis=f_y_data_210,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HOLX",
            y_axis=f_y_data_211,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HON",
            y_axis=f_y_data_212,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HP",
            y_axis=f_y_data_213,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HPE",
            y_axis=f_y_data_214,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HPQ",
            y_axis=f_y_data_215,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HRB",
            y_axis=f_y_data_216,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HRL",
            y_axis=f_y_data_217,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HSIC",
            y_axis=f_y_data_218,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HST",
            y_axis=f_y_data_219,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HSY",
            y_axis=f_y_data_220,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "HUM",
            y_axis=f_y_data_221,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IBM",
            y_axis=f_y_data_222,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ICE",
            y_axis=f_y_data_223,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IDXX",
            y_axis=f_y_data_224,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IEX",
            y_axis=f_y_data_225,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IFF",
            y_axis=f_y_data_226,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "INCY",
            y_axis=f_y_data_227,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "INFO",
            y_axis=f_y_data_228,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "INTC",
            y_axis=f_y_data_229,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "INTU",
            y_axis=f_y_data_230,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IP",
            y_axis=f_y_data_231,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IPG",
            y_axis=f_y_data_232,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IPGP",
            y_axis=f_y_data_233,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IR",
            y_axis=f_y_data_234,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IRM",
            y_axis=f_y_data_235,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ISRG",
            y_axis=f_y_data_236,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IT",
            y_axis=f_y_data_237,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ITW",
            y_axis=f_y_data_238,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "IVZ",
            y_axis=f_y_data_239,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "JBHT",
            y_axis=f_y_data_240,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "JCI",
            y_axis=f_y_data_241,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "JD",
            y_axis=f_y_data_242,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "JKHY",
            y_axis=f_y_data_243,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "JNJ",
            y_axis=f_y_data_244,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "JNPR",
            y_axis=f_y_data_245,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "JPM",
            y_axis=f_y_data_246,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "JWN",
            y_axis=f_y_data_247,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "K",
            y_axis=f_y_data_248,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KEY_",
            y_axis=f_y_data_249,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KHC",
            y_axis=f_y_data_250,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KIM",
            y_axis=f_y_data_251,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KLAC",
            y_axis=f_y_data_252,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KMB",
            y_axis=f_y_data_253,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KMI",
            y_axis=f_y_data_254,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KMX",
            y_axis=f_y_data_255,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KO",
            y_axis=f_y_data_256,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KR",
            y_axis=f_y_data_257,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KSS",
            y_axis=f_y_data_258,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "KSU",
            y_axis=f_y_data_259,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "L",
            y_axis=f_y_data_260,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LBTYA",
            y_axis=f_y_data_261,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LBTYK",
            y_axis=f_y_data_262,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LEG",
            y_axis=f_y_data_263,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LEN",
            y_axis=f_y_data_264,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LH",
            y_axis=f_y_data_265,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LKQ",
            y_axis=f_y_data_266,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LLY",
            y_axis=f_y_data_267,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LMT",
            y_axis=f_y_data_268,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LNC",
            y_axis=f_y_data_269,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LNT",
            y_axis=f_y_data_270,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LOW",
            y_axis=f_y_data_271,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LRCX",
            y_axis=f_y_data_272,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LUV",
            y_axis=f_y_data_273,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LVS",
            y_axis=f_y_data_274,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "LYB",
            y_axis=f_y_data_275,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "M",
            y_axis=f_y_data_276,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MA",
            y_axis=f_y_data_277,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MAA",
            y_axis=f_y_data_278,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MAR",
            y_axis=f_y_data_279,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MAS",
            y_axis=f_y_data_280,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MCD",
            y_axis=f_y_data_281,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MCHP",
            y_axis=f_y_data_282,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MCK",
            y_axis=f_y_data_283,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MCO",
            y_axis=f_y_data_284,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MDLZ",
            y_axis=f_y_data_285,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MDT",
            y_axis=f_y_data_286,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MET",
            y_axis=f_y_data_287,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MGM",
            y_axis=f_y_data_288,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MHK",
            y_axis=f_y_data_289,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MKC",
            y_axis=f_y_data_290,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MLM",
            y_axis=f_y_data_291,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MMC",
            y_axis=f_y_data_292,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MMM",
            y_axis=f_y_data_293,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MNST",
            y_axis=f_y_data_294,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MO",
            y_axis=f_y_data_295,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MOS",
            y_axis=f_y_data_296,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MPC",
            y_axis=f_y_data_297,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MRK",
            y_axis=f_y_data_298,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MRO",
            y_axis=f_y_data_299,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MS",
            y_axis=f_y_data_300,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MSFT",
            y_axis=f_y_data_301,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MSI",
            y_axis=f_y_data_302,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MTB",
            y_axis=f_y_data_303,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MTD",
            y_axis=f_y_data_304,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MU",
            y_axis=f_y_data_305,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MXIM",
            y_axis=f_y_data_306,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "MYL",
            y_axis=f_y_data_307,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NBL",
            y_axis=f_y_data_308,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NCLH",
            y_axis=f_y_data_309,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NDAQ",
            y_axis=f_y_data_310,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NEE",
            y_axis=f_y_data_311,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NEM",
            y_axis=f_y_data_312,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NFLX",
            y_axis=f_y_data_313,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NI",
            y_axis=f_y_data_314,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NKE",
            y_axis=f_y_data_315,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NLSN",
            y_axis=f_y_data_316,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NOC",
            y_axis=f_y_data_317,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NOV",
            y_axis=f_y_data_318,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NOW",
            y_axis=f_y_data_319,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NRG",
            y_axis=f_y_data_320,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NSC",
            y_axis=f_y_data_321,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NTAP",
            y_axis=f_y_data_322,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NTES",
            y_axis=f_y_data_323,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NTRS",
            y_axis=f_y_data_324,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NUE",
            y_axis=f_y_data_325,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NVDA",
            y_axis=f_y_data_326,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NWL",
            y_axis=f_y_data_327,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NWS",
            y_axis=f_y_data_328,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NWSA",
            y_axis=f_y_data_329,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "NXPI",
            y_axis=f_y_data_330,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "O",
            y_axis=f_y_data_331,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "OKE",
            y_axis=f_y_data_332,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "OMC",
            y_axis=f_y_data_333,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ORCL",
            y_axis=f_y_data_334,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ORLY",
            y_axis=f_y_data_335,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "OXY",
            y_axis=f_y_data_336,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PAYX",
            y_axis=f_y_data_337,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PBCT",
            y_axis=f_y_data_338,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PCAR",
            y_axis=f_y_data_339,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PEG",
            y_axis=f_y_data_340,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PEP",
            y_axis=f_y_data_341,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PFE",
            y_axis=f_y_data_342,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PFG",
            y_axis=f_y_data_343,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PG",
            y_axis=f_y_data_344,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PGR",
            y_axis=f_y_data_345,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PH",
            y_axis=f_y_data_346,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PHM",
            y_axis=f_y_data_347,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PKG",
            y_axis=f_y_data_348,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PKI",
            y_axis=f_y_data_349,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PLD",
            y_axis=f_y_data_350,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PM",
            y_axis=f_y_data_351,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PNC",
            y_axis=f_y_data_352,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PNR",
            y_axis=f_y_data_353,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PNW",
            y_axis=f_y_data_354,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PPG",
            y_axis=f_y_data_355,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PPL",
            y_axis=f_y_data_356,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PRGO",
            y_axis=f_y_data_357,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PRU",
            y_axis=f_y_data_358,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PSA",
            y_axis=f_y_data_359,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PSX",
            y_axis=f_y_data_360,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PVH",
            y_axis=f_y_data_361,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PWR",
            y_axis=f_y_data_362,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PXD",
            y_axis=f_y_data_363,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "PYPL",
            y_axis=f_y_data_364,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "QCOM",
            y_axis=f_y_data_365,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "RCL",
            y_axis=f_y_data_366,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "RE",
            y_axis=f_y_data_367,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "REG",
            y_axis=f_y_data_368,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "REGN",
            y_axis=f_y_data_369,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "RF",
            y_axis=f_y_data_370,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "RHI",
            y_axis=f_y_data_371,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "RJF",
            y_axis=f_y_data_372,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "RL",
            y_axis=f_y_data_373,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "RMD",
            y_axis=f_y_data_374,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ROK",
            y_axis=f_y_data_375,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ROP",
            y_axis=f_y_data_376,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ROST",
            y_axis=f_y_data_377,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "RSG",
            y_axis=f_y_data_378,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "RTN",
            y_axis=f_y_data_379,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SBAC",
            y_axis=f_y_data_380,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SBUX",
            y_axis=f_y_data_381,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SCHW",
            y_axis=f_y_data_382,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SEE",
            y_axis=f_y_data_383,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SHW",
            y_axis=f_y_data_384,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SIVB",
            y_axis=f_y_data_385,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SJM",
            y_axis=f_y_data_386,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SLB",
            y_axis=f_y_data_387,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SLG",
            y_axis=f_y_data_388,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SNA",
            y_axis=f_y_data_389,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SNPS",
            y_axis=f_y_data_390,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SO",
            y_axis=f_y_data_391,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SPG",
            y_axis=f_y_data_392,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SPGI",
            y_axis=f_y_data_393,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SRE",
            y_axis=f_y_data_394,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "STE",
            y_axis=f_y_data_395,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "STT",
            y_axis=f_y_data_396,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "STX",
            y_axis=f_y_data_397,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "STZ",
            y_axis=f_y_data_398,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SWK",
            y_axis=f_y_data_399,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SWKS",
            y_axis=f_y_data_400,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SYF",
            y_axis=f_y_data_401,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SYK",
            y_axis=f_y_data_402,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "SYY",
            y_axis=f_y_data_403,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "T",
            y_axis=f_y_data_404,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TAP",
            y_axis=f_y_data_405,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TEL",
            y_axis=f_y_data_406,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TFX",
            y_axis=f_y_data_407,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TGT",
            y_axis=f_y_data_408,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TIF",
            y_axis=f_y_data_409,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TJX",
            y_axis=f_y_data_410,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TMO",
            y_axis=f_y_data_411,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TROW",
            y_axis=f_y_data_412,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TRV",
            y_axis=f_y_data_413,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TSCO",
            y_axis=f_y_data_414,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TSLA",
            y_axis=f_y_data_415,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TSN",
            y_axis=f_y_data_416,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TWTR",
            y_axis=f_y_data_417,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TXN",
            y_axis=f_y_data_418,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "TXT",
            y_axis=f_y_data_419,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "UA",
            y_axis=f_y_data_420,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "UAL",
            y_axis=f_y_data_421,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "UDR",
            y_axis=f_y_data_422,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ULTA",
            y_axis=f_y_data_423,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "UNH",
            y_axis=f_y_data_424,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "UNM",
            y_axis=f_y_data_425,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "UNP",
            y_axis=f_y_data_426,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "UPS",
            y_axis=f_y_data_427,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "URI",
            y_axis=f_y_data_428,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "USB",
            y_axis=f_y_data_429,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "UTX",
            y_axis=f_y_data_430,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "V",
            y_axis=f_y_data_431,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "VAR",
            y_axis=f_y_data_432,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "VFC",
            y_axis=f_y_data_433,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "VLO",
            y_axis=f_y_data_434,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "VMC",
            y_axis=f_y_data_435,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "VNO",
            y_axis=f_y_data_436,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "VRSN",
            y_axis=f_y_data_437,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "VRTX",
            y_axis=f_y_data_438,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "VTR",
            y_axis=f_y_data_439,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "VZ",
            y_axis=f_y_data_440,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WAB",
            y_axis=f_y_data_441,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WAT",
            y_axis=f_y_data_442,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WBA",
            y_axis=f_y_data_443,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WDAY",
            y_axis=f_y_data_444,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WDC",
            y_axis=f_y_data_445,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WEC",
            y_axis=f_y_data_446,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WFC",
            y_axis=f_y_data_447,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WHR",
            y_axis=f_y_data_448,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WLTW",
            y_axis=f_y_data_449,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WM",
            y_axis=f_y_data_450,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WMB",
            y_axis=f_y_data_451,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WMT",
            y_axis=f_y_data_452,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WRB",
            y_axis=f_y_data_453,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WRK",
            y_axis=f_y_data_454,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WU",
            y_axis=f_y_data_455,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WY",
            y_axis=f_y_data_456,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "WYNN",
            y_axis=f_y_data_457,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "XEC",
            y_axis=f_y_data_458,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "XEL",
            y_axis=f_y_data_459,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "XLNX",
            y_axis=f_y_data_460,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "XOM",
            y_axis=f_y_data_461,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "XRAY",
            y_axis=f_y_data_462,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "XRX",
            y_axis=f_y_data_463,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "XYL",
            y_axis=f_y_data_464,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "YUM",
            y_axis=f_y_data_465,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ZBRA",
            y_axis=f_y_data_466,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ZION",
            y_axis=f_y_data_467,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )

            .set_global_opts(
            title_opts=opts.TitleOpts(title="US_ZGG", pos_bottom="bottom", pos_right="middle"),
            # xaxis_opts=opts.AxisOpts(name="x"),
            yaxis_opts=opts.AxisOpts(
                # name="y",
                splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True,

            ),
            legend_opts=opts.LegendOpts(is_show=False),  # 隐藏图例

        )

            .render("us_zgg.html")
    )





















if __name__=="__main__":
    jsIn_ep()

    # 等待5秒钟，然后将文件移动到templates目录下

    srcJSin = 'd:\\Downloads\\us_zgg.html'
    dstJSin = 'd:\\Downloads\\templates\\us_zgg.html'
    copyfile(srcJSin, dstJSin)
    app.run(debug=True)
    


