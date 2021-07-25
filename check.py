import pandas as pd
import numpy as np


class Check():
    def __init__(self, temprature, feed_rate, pressure, components, components1, components2, components3, components4,
                 components5, z1, z2, z3, z4, z5):
        K_by_Z = 0
        K_Z = 0
        Ks = []
        Zs = []
        Xs = []
        Ys = []
        self.answer = {}
        self.d = {}
        flag = 0
        self.temprature = float(temprature)
        self.feed_rate = float(feed_rate)
        self.pressure = float(pressure)
        self.components = int(components)

        self.components1 = components1
        self.components2 = components2
        self.components3 = components3
        self.components4 = components4
        self.components5 = components5

        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        self.z4 = z4
        self.z5 = z5

        df = pd.read_excel("antoine.xlsx")
        df['Psat']=(np.power(10,(df['A']-(df['B']/(self.temprature + df['C']))))).astype(float)
        df = df.set_index('SUBSTANCE')

        self.d[self.components1] = self.z1
        self.d[self.components2] = self.z2
        self.d[self.components3] = self.z3
        self.d[self.components4] = self.z4
        self.d[self.components5] = self.z5

        for ind in df.index:
            for values, keys in self.d.items():
                if ind == values:
                    Ki = df['Psat'][values] / self.pressure
                    Ki = Ki.astype('float')
                    Ks.append(Ki)
                    if keys == 0.0:
                        pass
                    else:
                        Zs.append(float(keys))
                        K_by_Z += float(keys) / (Ki)
                        K_Z += (Ki) * float(keys)
                        K_by_Z = round(K_by_Z, 5)
                        K_Z = round(K_Z, 5)
        if K_Z >= 0.995 and K_Z <= 1:
            K_Z = 1
        if K_by_Z >= 0.995 and K_by_Z <= 1:
            K_by_Z = 1
        
        if flag == 0:
            # make a button to calcuate this summation values and make an label
            # and output of these values

            self.answer["Summation of Ki*Zi"] = K_Z
            self.answer["Summation of Zi/Ki"] = K_by_Z

            # calculating bubble point and dew point
            bubble_point = 0
            min_error = 10000

            for T in np.arange(0.01, 200.0, 0.1):
                P = 0
                for ind in df.index:
                    for values, keys in (self.d.items()):
                        if keys != "0.0":
                            if ind == values:
                                P += float(keys) * (
                                    np.power(10, (df['A'][values] - (df['B'][values] / (T + df['C'][values])))))
                        else:
                            pass
                error = (abs(P - self.pressure)) / self.pressure

                if error < min_error:
                    min_error = error
                    bubble_point = T
                    bubble_point = bubble_point.astype('float')
                    bubble_point = round(bubble_point, 4)
            # make a button for calculating both bubble and dew point and show the output

            self.answer["Bubble point"] = bubble_point

            dew_point = 0
            min_error = 10000

            for Td in np.arange(0.01, 200.00, 0.1):
                sth = 0
                for ind in df.index:
                    for values, keys in self.d.items():
                        if keys != "0.0":
                            if ind == values:
                                sth += float(keys) / (
                                    np.power(10, (df['A'][values] - (df['B'][values] / (Td + df['C'][values])))))
                        else:
                            pass

                Pd = 1 / sth
                error = (abs(Pd - self.pressure)) / self.pressure

                if error < min_error:
                    min_error = error
                    dew_point = Td
                    dew_point = dew_point.astype('float')
                    dew_point = round(dew_point,4)
            self.answer['dewpoint'] = dew_point

            if K_Z > 1 and K_by_Z > 1:
                self.answer["condition"] = "Feed has both liquid and vapour composition"
            elif K_Z == 1:
                self.answer["condition"] = "Feed is in SATURATED LIQUID state"
            elif K_by_Z == 1:
                self.answer["condition"] = "Feed is in SATURATED VAPOUR state"
            elif K_Z < 1:
                self.answer["condition"] = "Feed is in SUB-COOLED LIQIUD state"
            elif K_by_Z < 1:
                self.answer["condition"] = "Feed is in SUPER-HEATED state"

            if K_Z > 1 and K_by_Z > 1:
                # write the summation equation and calculate V,xi,yi,L,and q
                req_V = 0
                min_error = 10000
                for V in np.arange(0.01, self.feed_rate, 0.1):
                    sth = 0
                    for i in range(self.components - 1):
                        sth += (((self.feed_rate * Zs[i]) / (self.feed_rate - V + (V * Ks[i]))) * (
                                    Ks[self.components - 1] - Ks[i]))
                    s = abs(Ks[self.components - 1] - 1)
                    error = (abs(s - abs(sth))) / s

                    if error < min_error:
                        min_error = error
                        req_V = V
                        req_V = req_V.astype('float')
                        req_V = round(req_V, 4)


                self.answer["Vapour Rate(V)"] = req_V
                L = self.feed_rate - req_V
                self.answer["Liquid Rate(L)"] = L
                Q = L / self.feed_rate
                self.answer["Q"] = Q
                for i in range(self.components):
                    Xi = ((self.feed_rate * Zs[i]) / (self.feed_rate - req_V + (req_V * Ks[i])))
                    Xi = Xi.astype('float')
                    Xi = round(Xi,4)
                    Xs.append(Xi)
                    Yi = Ks[i] * Xs[i]
                    Yi = Yi.astype('float')
                    Yi = round(Yi,4)
                    Ys.append(Yi)
                    self.answer["Liquid Composition(Xi)"] = Xs
                    self.answer["Vapour Composition(Yi)"] = Ys
            elif K_Z == 1:
                self.answer["Q"] = 1
            elif K_by_Z == 1:
                self.answer["Q"] = 0
            elif K_Z < 1:
                self.answer["Q"] = "Greater than 1"
            elif K_by_Z < 1:
                self.answer["Q"] = "Less than 0"

    def final_answer(self, ):
        return self.answer

