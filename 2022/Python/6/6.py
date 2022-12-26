signal = open(r'Input.txt','r').readlines()[0]

for indx in range(len(signal)-14):
    package = signal[indx:indx+14]
    single_signals = list(set([_ for _ in package]))

    if len(single_signals) == 14:
        print(indx+14)
        break

