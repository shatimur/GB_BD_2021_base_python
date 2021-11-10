import time


# class TrafficLight:
#     color = ['red', 'yellow', 'green']
#
#     def running(self):
#         print(self.color[0])
#         time.sleep(7)
#         print(self.color[1])
#         time.sleep(2)
#         print(self.color[2])
#         time.sleep(5)
#         print('Светофор выключен')
#
#
# a = TrafficLight()
# a.running()


class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        for i in range(3):
            print(list(self.__color.keys())[i])
            time.sleep(list(self.__color.values())[i])
        print('Светофор выключен')


a = TrafficLight()
a.running()
