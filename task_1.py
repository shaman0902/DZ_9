from time import sleep

class TrafficLight:
    __color = 'Черный'

    def running(self):
        while True:
            print('Светофор красный')
            sleep(10)
            print('Светофор желтый')
            sleep(3)
            print('Светофор зеленый')
            sleep(10)


svetofor = TrafficLight()
svetofor.running()
