from Hot_Rod_Super_Speedway import track_original
racing_line_calculation = [[6.78572867, 3.55837579],
                           [6.57618268, 3.62802675],
                           [6.35225069, 3.68473194],
                           [6.11750611, 3.73049912],
                           [5.87537452, 3.76798065],
                           [5.62842761, 3.7995473],
                           [5.37909055, 3.82794845],
                           [5.12932611, 3.85578048],
                           [4.87973802, 3.88297393],
                           [4.63038152, 3.90941982],
                           [4.38129914, 3.93500603],
                           [4.13254918, 3.95956688],
                           [3.88420995, 3.98287601],
                           [3.63633823, 4.0047735],
                           [3.38900255, 4.02506405],
                           [3.14225492, 4.0436022],
                           [2.89616839, 4.0601802],
                           [2.65081855, 4.07458421],
                           [2.40627717, 4.08661261],
                           [2.16259865, 4.09611592],
                           [1.91981862, 4.10300054],
                           [1.67795059, 4.10723778],
                           [1.43708125, 4.10858832],
                           [1.19730895, 4.10678249],
                           [0.95880685, 4.10134119],
                           [0.72182027, 4.09158949],
                           [0.48663394, 4.07675618],
                           [0.25362327, 4.05583755],
                           [0.02318391, 4.02780374],
                           [-0.20394733, 3.99073722],
                           [-0.42668442, 3.94188911],
                           [-0.64382567, 3.87838911],
                           [-0.85363836, 3.79623896],
                           [-1.05912718, 3.70317563],
                           [-1.26166019, 3.60249579],
                           [-1.46232005, 3.49685482],
                           [-1.66205214, 3.38871123],
                           [-1.86415215, 3.28089366],
                           [-2.06723338, 3.17478776],
                           [-2.27150461, 3.07095718],
                           [-2.47718068, 2.97004348],
                           [-2.68446099, 2.87271964],
                           [-2.89357942, 2.77979353],
                           [-3.10477221, 2.69211424],
                           [-3.31850231, 2.61115413],
                           [-3.5352714, 2.5385919],
                           [-3.75590633, 2.47730044],
                           [-3.9795659, 2.42533326],
                           [-4.20567274, 2.38128301],
                           [-4.43371836, 2.34384677],
                           [-4.66334705, 2.31216646],
                           [-4.8942449, 2.28547977],
                           [-5.1261185, 2.26300915],
                           [-5.35872677, 2.24407132],
                           [-5.59187581, 2.22808909],
                           [-5.8253951, 2.21448883],
                           [-6.05917006, 2.20297269],
                           [-6.2873773, 2.19362909],
                           [-6.51453695, 2.181959],
                           [-6.73960001, 2.16564518],
                           [-6.96133175, 2.14200277],
                           [-7.17845859, 2.10838512],
                           [-7.3894437, 2.06187904],
                           [-7.59226769, 1.99923235],
                           [-7.78391445, 1.91659967],
                           [-7.95993416, 1.81035357],
                           [-8.12348805, 1.68834029],
                           [-8.27464616, 1.55264888],
                           [-8.41300953, 1.40472513],
                           [-8.53813564, 1.24604976],
                           [-8.6488722, 1.07775772],
                           [-8.74399429, 0.90126874],
                           [-8.8211088, 0.71794461],
                           [-8.87760251, 0.5299036],
                           [-8.91096633, 0.34002071],
                           [-8.91707388, 0.15219196],
                           [-8.8915326, -0.0277633],
                           [-8.83113617, -0.19237123],
                           [-8.73274824, -0.33157096],
                           [-8.60354853, -0.44206714],
                           [-8.45186428, -0.52595599],
                           [-8.28337881, -0.58589423],
                           [-8.10171121, -0.62362504],
                           [-7.90988138, -0.64132171],
                           [-7.71047954, -0.64181404],
                           [-7.50570168, -0.62855186],
                           [-7.29746133, -0.60562119],
                           [-7.08751233, -0.57766438],
                           [-6.87799197, -0.55299237],
                           [-6.66927967, -0.53355228],
                           [-6.46177486, -0.5217348],
                           [-6.25590223, -0.51988631],
                           [-6.05218562, -0.53065282],
                           [-5.85134486, -0.55730478],
                           [-5.65458995, -0.60468625],
                           [-5.46335212, -0.67702038],
                           [-5.2764116, -0.7671723],
                           [-5.09243426, -0.86914425],
                           [-4.90998118, -0.97709391],
                           [-4.71459123, -1.09040341],
                           [-4.51737178, -1.20227783],
                           [-4.31832889, -1.31255376],
                           [-4.11745253, -1.42107413],
                           [-3.91470987, -1.52766884],
                           [-3.70987546, -1.63193831],
                           [-3.50270561, -1.73338294],
                           [-3.29290892, -1.83133607],
                           [-3.08011642, -1.9248828],
                           [-2.86359838, -2.01236686],
                           [-2.64408368, -2.09465736],
                           [-2.42208123, -2.17251256],
                           [-2.19806472, -2.24671813],
                           [-1.97230403, -2.31773029],
                           [-1.74500968, -2.38591414],
                           [-1.51636788, -2.45160083],
                           [-1.28654596, -2.51509462],
                           [-1.0557075, -2.57670436],
                           [-0.82402678, -2.63678476],
                           [-0.59161739, -2.69564042],
                           [-0.35853274, -2.75356914],
                           [-0.12440659, -2.81081502],
                           [0.10976973, -2.86893029],
                           [0.34368746, -2.92786291],
                           [0.57732123, -2.98758149],
                           [0.81066471, -3.04809403],
                           [1.04373351, -3.10935744],
                           [1.27655484, -3.1712979],
                           [1.50919028, -3.23374738],
                           [1.74166755, -3.29663022],
                           [1.97404066, -3.35979867],
                           [2.20636412, -3.42310331],
                           [2.43952818, -3.48685767],
                           [2.67287912, -3.55005664],
                           [2.90657252, -3.61221926],
                           [3.14070851, -3.67300413],
                           [3.37538967, -3.73202814],
                           [3.61069274, -3.78894537],
                           [3.84666495, -3.84345502],
                           [4.08332426, -3.89529977],
                           [4.32066007, -3.94426361],
                           [4.5586343, -3.990169],
                           [4.79718277, -4.03287278],
                           [5.03621671, -4.07226159],
                           [5.27562425, -4.10825704],
                           [5.51527189, -4.14086658],
                           [5.75501837, -4.1699277],
                           [5.99468863, -4.19519355],
                           [6.23405522, -4.21626014],
                           [6.47280707, -4.23256997],
                           [6.71050561, -4.24338696],
                           [6.94651287, -4.24770489],
                           [7.17993886, -4.24431061],
                           [7.40955687, -4.23173555],
                           [7.63395189, -4.2086364],
                           [7.85088235, -4.1727009],
                           [8.05767197, -4.12168985],
                           [8.25106146, -4.05326366],
                           [8.42637741, -3.9644469],
                           [8.57802248, -3.85323117],
                           [8.69903212, -3.71944042],
                           [8.77852755, -3.56556009],
                           [8.82340732, -3.40235632],
                           [8.83859379, -3.23540285],
                           [8.82797041, -3.06812444],
                           [8.79398648, -2.90280445],
                           [8.73848688, -2.74114653],
                           [8.66049874, -2.58532148],
                           [8.55459469, -2.44022432],
                           [8.423438, -2.30857151],
                           [8.27156061, -2.19071175],
                           [8.10232883, -2.08643447],
                           [7.91875524, -1.99488105],
                           [7.72343866, -1.91481313],
                           [7.51846976, -1.84493696],
                           [7.30566787, -1.78384281],
                           [7.08673365, -1.72994609],
                           [6.86340582, -1.6813755],
                           [6.63730408, -1.63623607],
                           [6.40941531, -1.59309743],
                           [6.17816681, -1.54698815],
                           [5.94782317, -1.49864266],
                           [5.71862648, -1.44791402],
                           [5.49071629, -1.39461497],
                           [5.264256, -1.3385044],
                           [5.03946461, -1.27925117],
                           [4.81667782, -1.216339],
                           [4.5963043, -1.14916929],
                           [4.37880432, -1.07710744],
                           [4.16495769, -0.99906282],
                           [3.95575854, -0.91373874],
                           [3.75254453, -0.8195394],
                           [3.5574999, -0.71427978],
                           [3.36817792, -0.60201996],
                           [3.18530497, -0.48247519],
                           [3.00991256, -0.35524176],
                           [2.84350799, -0.2197633],
                           [2.68773709, -0.0757527],
                           [2.54571541, 0.07757303],
                           [2.42126683, 0.24034102],
                           [2.31942288, 0.41177216],
                           [2.2471027, 0.58936591],
                           [2.21065525, 0.76761121],
                           [2.21485851, 0.93900046],
                           [2.26295319, 1.09574795],
                           [2.361418, 1.22744479],
                           [2.48913893, 1.3406005],
                           [2.64247211, 1.43533918],
                           [2.81832168, 1.51196254],
                           [3.01401032, 1.5708422],
                           [3.22620747, 1.61342696],
                           [3.45168466, 1.64171616],
                           [3.68735744, 1.65821107],
                           [3.93039854, 1.66572189],
                           [4.17834074, 1.66713258],
                           [4.42898042, 1.66536727],
                           [4.67865369, 1.66699941],
                           [4.92615987, 1.67292679],
                           [5.17068813, 1.68417775],
                           [5.41129812, 1.70182912],
                           [5.64694396, 1.72692594],
                           [5.87650597, 1.76041435],
                           [6.09885355, 1.80305544],
                           [6.31282767, 1.85546631],
                           [6.5167066, 1.91864062],
                           [6.70885894, 1.99312805],
                           [6.88744404, 2.0793498],
                           [7.05031946, 2.17759987],
                           [7.19424137, 2.28839883],
                           [7.315914, 2.41148839],
                           [7.41149392, 2.54599436],
                           [7.47637009, 2.69017999],
                           [7.50440952, 2.84105346],
                           [7.4861029, 2.99320919],
                           [7.40446756, 3.13342695],
                           [7.28990746, 3.26125288],
                           [7.14643848, 3.37528876],
                           [6.97710792, 3.47436505],
                           [6.78572867, 3.55837579]]

def compare():
    print("len(track_original):\t" + str(len(track_original)))
    print("len(racing_line_calculation):\t" + str(len(racing_line_calculation)))

    every_nth_result = 20

    print("\nFirst Element Compare\nTO\t\tRL")
    for i in range(len(racing_line_calculation)):
        if i % every_nth_result == 0:
            print(str(round(track_original[i][0], 3)) + "\t" + str(round(racing_line_calculation[i][0], 3)))

    print("\nSecond Element Compare\nTO\t\tRL")
    for i in range(len(racing_line_calculation)):
        if i % every_nth_result == 0:
            print(str(round(track_original[i][1], 3)) + "\t" + str(round(racing_line_calculation[i][1], 3)))

def main():
    

if __name__ == '__main__':
    main()